#!/usr/bin/env python3
"""Offline fixture checks, not a production authorization/policy evaluator."""
import json
import re
from datetime import datetime
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
FORMAT = "https://example.org/acfs/test-evidence-v1"
EXTENSION = "example.procedure.v1"


def read(path):
    return json.loads((ROOT / path).read_text())


base = read("schemas/acfs-record.schema.json")
legacy = read("schemas/capability-record.schema.json")
extension = read("examples/extensions/procedure.schema.json")
registry = Registry().with_resource(base["$id"], Resource.from_contents(base))
checker = FormatChecker()
if "date-time" not in checker.checkers:
    raise SystemExit("Install requirements-validation.txt to enable date-time checks")
validators = [Draft202012Validator(s, registry=registry, format_checker=checker)
              for s in (base, legacy, extension)]
for schema in (base, legacy, extension):
    Draft202012Validator.check_schema(schema)


def conforms(value, validator=validators[0]):
    return not list(validator.iter_errors(value))


def extension_result(record):
    """Conditional declarations are semantic constraints, not Core schema fields."""
    metadata = record["metadata"]
    declared = metadata.get("extensions", [])
    required = metadata.get("required_extensions", [])
    for values in (declared, required):
        if (not isinstance(values, list)
                or any(not isinstance(v, str) or not v for v in values)
                or len(set(values)) != len(values)):
            return "invalid-declaration"
    if not set(required) <= set(declared):
        return "invalid-declaration"
    if set(required) - {EXTENSION}:
        return "unsupported-required-extension"
    if EXTENSION in declared and not conforms(record, validators[2]):
        return "invalid-extension"
    return None


def cached_payload(case):
    """Synthetic permission already established by fixture trust context."""
    cache = case["context"].get("cache", {})
    if cache.get("known_withdrawal"):
        return "non-active", None
    try:
        start, now, end = (datetime.fromisoformat(cache[k].replace("Z", "+00:00"))
                           for k in ("valid_from", "now", "valid_until"))
        valid_time = start <= now < end
    except (KeyError, AttributeError, ValueError, TypeError):
        valid_time = False
    record = case["record"]
    if (not cache.get("offline_permitted") or not valid_time
            or cache.get("reconnected") or cache.get("verification_required")
            or any(cache.get(k) != record[k] for k in ("scope", "kind", "risk"))):
        return "verification-required", None
    return None, case.get("cached_evidence")


def assess(case):
    """Only the example mapping and supplied synthetic grants are understood."""
    record, context = case["record"], case["context"]
    if not conforms(record):
        return "invalid-base"
    result = extension_result(record)
    if result:
        return result
    if record["status"] != "active":
        return "non-active"
    if record["scope"] != context["scope"]:
        return "out-of-scope"
    if "cache" in context:
        result, _ = cached_payload(case)
        if result:
            return result
    discovery = record["metadata"].get("governance")
    if not isinstance(discovery, dict):
        return "missing-evidence"
    if discovery.get("format") != FORMAT:
        return "unsupported-evidence"
    locations = discovery.get("evidence")
    if not isinstance(locations, list) or not locations:
        return "missing-evidence"
    payloads = []
    for locator in locations:
        if not isinstance(locator, dict) or len(set(locator) & {"embedded", "record", "uri"}) != 1:
            return "missing-evidence"
        payload = None
        if "embedded" in locator:
            payload = locator["embedded"]
        elif "record" in locator:
            related = case.get("records", {}).get(locator["record"])
            if related and conforms(related) and related["id"] == locator["record"]:
                payload = related["metadata"].get("test_evidence")
        else:
            payload = case.get("resources", {}).get(locator["uri"])
        if payload is None and "cache" in context:
            _, payload = cached_payload(case)
        if payload is None:
            return "inaccessible-evidence"
        payloads.append(payload)
    # This example mapping accepts one complete decision, not a general history.
    if len(payloads) != 1:
        return "unsupported-evidence"
    evidence = payloads[0]
    fields = {"record", "contributor", "actor", "authority", "at", "from", "to", "scope", "reason"}
    if (not isinstance(evidence, dict) or not fields <= evidence.keys()
            or any(not isinstance(evidence[k], str) or not evidence[k]
                   for k in fields - {"from"})
            or not checker.conforms(evidence["at"], "date-time")
            or not (evidence.get("policy") or evidence.get("reviewer"))):
        return "incomplete-evidence"
    if (evidence["record"] != record["id"] or evidence["scope"] != record["scope"]
            or evidence["to"] != record["status"]
            or evidence["contributor"] != record["provenance"]["actor"]):
        return "mismatched-evidence"
    if evidence["from"] is not None:
        return "unsupported-evidence"  # initial activation only in this mapping
    for grant in context["grants"]:
        if (all(grant.get(k) == record[k] for k in ("scope", "kind", "risk"))
                and grant.get("authority") == evidence["authority"]
                and any(grant.get(k) and grant[k] == evidence.get(k)
                        for k in ("policy", "reviewer"))):
            return "eligible"
    return "unauthorized"


def main():
    total = 0
    for pattern, validator, expected in [
        ("examples/valid/*.json", validators[0], True),
        ("examples/invalid/*v0.2.1.json", validators[0], False),
        ("examples/legacy/valid/*.json", validators[1], True),
        ("examples/legacy/invalid/*.json", validators[1], False),
        ("examples/extensions/procedure-valid.json", validators[2], True),
        ("examples/extensions/procedure-invalid.json", validators[2], False),
    ]:
        paths = sorted(ROOT.glob(pattern))
        assert paths, pattern
        for path in paths:
            assert conforms(json.loads(path.read_text()), validator) == expected, path
            if validator is validators[0] and not expected:
                assert not conforms(json.loads(path.read_text()), validators[2]), path
            total += 1
    # An extension-invalid payload still passes Core: each layer is tested.
    assert conforms(read("examples/extensions/procedure-invalid.json"))
    manifest = read("examples/conformance/cases.json")
    cases = [dict(case, **{key: dict(default, **case.get(key, {}))
                          for key, default in manifest["defaults"].items()})
             for case in manifest["cases"]]
    assert len({c["name"] for c in cases}) == len(cases)
    for case in cases:
        assert conforms(case["record"]), case["name"]
        actual = assess(case)
        assert actual == case["expected"], (case["name"], actual, case["expected"])
    unsafe = read("examples/invalid/revoked-behavioral-retrieval.json")
    assert unsafe["mode"] == "behavioral"
    assert any(v["lifecycle"] == "revoked" for v in unsafe["records"])
    for path in ROOT.rglob("*.json"):
        if not any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            json.loads(path.read_text())
    for path in [ROOT / "README.md", *ROOT.glob("specifications/*.md"),
                 *ROOT.glob("security/*.md"), *ROOT.glob("examples/**/README.md")]:
        text = path.read_text()
        assert len(re.findall(r"^```", text, re.M)) % 2 == 0, path
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if "://" in link:
                continue
            target, _, anchor = link.partition("#")
            destination = path.parent / target if target else path
            assert destination.exists(), (path, link)
            if anchor:
                slugs = [re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-")
                         for h in re.findall(r"^#{1,6} (.+)$", destination.read_text(), re.M)]
                assert anchor in slugs, (path, link)
    sample = json.loads(re.search(r"```json\n(.*?)\n```", (ROOT / "README.md").read_text(), re.S)[1])
    assert conforms(sample)
    print(f"PASS: 3 schemas; {total} structural fixtures; {len(cases)} synthetic semantic cases;")
    print("README record, JSON parsing, local Markdown links/anchors and fences.")
    print("No network, policy execution, identity verification, or runtime conformance is tested.")


if __name__ == "__main__":
    main()
