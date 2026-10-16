# Conformance Validation

ACFS Core remains ACFS-Records. Validation has distinct layers:

1. **Base structure:** the Draft 2020-12 record schema checks required fields,
   `metadata.acfs_version`, provenance shape, enums, and field types. Enable
   `date-time` format checking explicitly. The legacy schema is separate.
2. **Extension compatibility:** check conditional declarations and required
   extension support, then validate supported payloads in addition to the base
   record. The example procedure schema uses standard `allOf`; it never removes
   a base constraint. Unknown optional metadata may remain uninterpreted.
3. **Semantic conformance:** interpret governance evidence using its documented
   mapping; verify applicable authority, policy/review, record/scope binding,
   transition history, and cache validity under the lifecycle requirements.
   A structurally valid active record, URI, or claimed reviewer is not approval.

A schema cannot prove truth, reviewer identity or permission, evidence
availability, policy applicability, relation resolution, full history, current
status, or safe execution. Semantic fixtures exercise only explicitly supplied
synthetic context, not a general authorization implementation.

## Reproduce the Checks

From the repository root, with Python 3.10 or later:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-validation.txt
.venv/bin/python scripts/validate.py
git diff --check
```

The direct validation dependencies are `jsonschema` and `rfc3339-validator`
(date-time checks); JSON Schema reference handling comes with `jsonschema`.
Dependency installation needs package access; the checks themselves use local
files and a locally supplied schema reference mapping and perform no network
requests. Do not run Python with `-O`, which disables fixture assertions.

The procedure checks all positive/negative base and legacy record fixtures,
the additional example extension schema and its valid/invalid payloads,
conditional extension declarations, synthetic governance cases, the README
record, JSON syntax, and local Markdown links/anchors and fences. The existing
revoked retrieval envelope is checked separately as a semantic negative, not
misrepresented as an invalid v0.2.1 record. Existing examples under
`examples/valid/` assert structure only, not governance authorization.

See the [fixture mapping](../examples/conformance/README.md) for the exact
synthetic trust assumptions. The result `eligible` means that the isolated
fixture has sufficient evidence under those assumptions, not that a real-world
actor or policy has been authenticated. The helper accepts no remote records,
runs no policy language, and provides no storage, network, transport, execution,
or synchronization service. It is not a runtime test harness or a full
conformance certification suite.

## Compatibility and Remaining Work

The base schema's acceptance behavior is unchanged; its new comment only
identifies this validation boundary. Custom native enum values already failed
that schema. Portable producers map their custom semantics into declared
metadata while retaining a Core kind and base relation types. Existing optional
metadata remains structurally valid. The new conditional declaration and
evidence-discovery conventions may require an adapter for portable exchange;
they do not require rewriting all existing Core records or local histories.

Issue #7 should build the full cross-agent demonstration using these rules.
It must supply concrete supported evidence mappings, independent trust inputs,
and history covering capture, authorization, reuse, correction and withdrawal.
This pass does not prove independent runtime interoperability, authenticated
review, external evidence integrity/availability, full transition chains,
conflict resolution, or distributed cache behavior. Those require explicit
implementation choices and evidence; they cannot be inferred from a schema
pass or a shared synthetic mapping. No new lifecycle decision, synchronization
protocol, or extension registry is defined here.
