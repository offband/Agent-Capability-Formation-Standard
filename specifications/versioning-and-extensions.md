# Versioning and Extensions

Versioning and extensions define how ACFS evolves without breaking durable
records or forcing every implementation to support every feature.

## Standard Version

ACFS documents SHOULD identify the standard version or revision they target.

Records claiming ACFS v0.2.1 MUST include `metadata.acfs_version: "v0.2.1"`,
as required by the record specification and schema:

```json
{
  "metadata": {
    "acfs_version": "v0.2.1"
  }
}
```

Implementations SHOULD document which ACFS version, revision, and conformance
profiles they support.

## Record Compatibility

Implementations MUST preserve required fields even when they do not understand
all optional or implementation-specific metadata.

Unknown metadata fields SHOULD be preserved during import, export, retrieval,
revision, and status changes unless policy requires removal.

Unknown values in base `kind`, `status`, or `relations[].type` fail base
validation. Unknown custom semantics in namespaced extension data follow the
handling rules below; additional properties do not widen base enums.

## Compatibility Profiles

ACFS v0.2.1 uses named profiles so simple implementations can stay small.

Implementations claiming ACFS compatibility MUST support `ACFS-Records`, which
is ACFS Core. Other profiles are optional additions; see [Conformance](conformance.md).

Implementations MAY additionally claim:

- `ACFS-Capabilities`
- `ACFS-Governance`
- `ACFS-Relations`
- `ACFS-Retrieval`
- `ACFS-MCP`
- `ACFS-Portable`
- `ACFS-Legacy-Capability-Records`

See `specifications/conformance.md` for profile requirements.

Runtime execution, tool invocation, hosting, authentication, package managers,
workflow engines, billing, and agent orchestration are not ACFS Core profiles in
v0.2.1. They require implementation documentation or a future non-core
extension.

## Extensions

Implementations MAY define extensions.

Extensions are the preferred way to standardize runtime concepts that prove
useful across implementations. Do not add a concept to the ACFS base profile
only because one implementation uses it internally. First document how the
concept maps to records, relations, metadata, recall behavior, and safety
boundaries.

Extensions MUST document their identifier and version, payload location and
meaning, required profiles, validation constraints, and whether safe use requires
understanding them. Identifiers SHOULD be namespaced and version-specific.
Definitions MAY be exchanged as documentation or JSON Schema; no registry,
network lookup, or new schema language is required. A declaration is not proof
that the extension or its source is trusted.

## Extension Representation

Portable v0.2.1 records MUST pass the unchanged base record schema. The seven
Core kinds, four statuses, and seven base relation types remain closed.
Custom kinds MUST map to an appropriate Core kind; custom relation types MUST
live in a namespaced metadata payload. The extension definition MUST specify
the mapping and custom relation direction. If no safe Core mapping exists,
the native object is not a portable v0.2.1 record; retain it as an external
artifact or reject it, rather than widening the Core enums.

Records using custom semantics MUST explicitly declare their versioned
identifiers in `metadata.extensions`, an array of distinct nonempty strings.
Payloads SHOULD use metadata keys equal to their extension identifiers.
Required extensions MUST also be listed in `metadata.required_extensions`,
an array of distinct identifiers drawn from `metadata.extensions`. Both fields
are conditional metadata conventions, not new required Core fields. Ordinary
optional implementation metadata need not be declared as an extension.

Example fragment (not a complete record):

```json
{
  "kind": "capability",
  "metadata": {
    "acfs_version": "v0.2.1",
    "extensions": ["example.procedure.v1"],
    "required_extensions": ["example.procedure.v1"],
    "example.procedure.v1": {
      "kind": "procedure",
      "relations": [{"type": "reviewed_by", "target": "user:reviewer"}]
    }
  }
}
```

Here the custom kind refines `capability`; `reviewed_by` is not a new base
relation and does not itself prove authorized review. See the
[example extension schema](../examples/extensions/procedure.schema.json).
An extension schema MUST constrain the extension payload in addition to, not
instead of, base validation. It MAY use JSON Schema `allOf` with a reference to
the base schema, or be applied separately after base validation. Validators
MUST NOT remove enums, discard metadata requirements, or rewrite an input into
a passing shape. Schema/document resolution MUST use explicitly supported
local or otherwise trusted definitions; arbitrary record-supplied URIs MUST
NOT cause automatic code execution or privileged network access.

## Unsupported and Mandatory Extensions

If safe interpretation depends on custom semantics, the producer MUST declare
the extension required. Custom kind or relation semantics that affect
behavioral eligibility, authorization, dependencies, or scope require this
marking. A producer MUST NOT label a safety-critical requirement optional.

Consumers MUST distinguish these outcomes:

| Condition | Handling |
| --- | --- |
| Base schema fails, including custom values in base enums | Reject as a portable v0.2.1 record; MAY retain the original for audit/quarantine. |
| Supported extension | Validate its payload against the documented constraints as well as the base shape; then apply its semantics and normal lifecycle/policy checks. |
| Invalid optional payload | MUST NOT infer its custom semantics; MAY ignore only if safe interpretation does not depend on it. |
| Unknown optional extension | SHOULD preserve its data; MAY ignore its custom semantics only when the remaining record is safely interpretable without them. No automatic authorization follows. |
| Unknown/unsupported required extension, malformed declaration, or invalid required payload | MUST NOT use as behavioral guidance; reject, quarantine, or retain audit-only with the reason. |
| A required extension is not in `metadata.extensions` | The declaration is inconsistent; MUST NOT use as behavioral guidance. |

Unknown optional metadata remains preservable; the base schema intentionally
accepts it. A schema pass does not validate these conditional declarations.
Consumers MUST NOT silently strip a required marker or payload and then treat
the remainder as approved guidance. Import/export SHOULD preserve declarations,
payloads, and evidence locators unless policy requires redaction; a redacted
requirement remains unsatisfied, not implicitly optional.

Existing documented extension encodings MAY be accepted through an explicit,
documented adapter that preserves their meaning and safety requirements.
New portable exports MUST use these declarations. Native custom base enum
values were never accepted by the v0.2.1 base schema; map them before export,
retaining their original meaning in the declared payload. This clarification
does not change the set of records accepted by the base JSON Schema.

## Schema Evolution

Future ACFS versions SHOULD preserve compatibility with existing required fields
where practical.

New required fields SHOULD be introduced through a new major version or a
clearly named conformance profile.

Implementations SHOULD provide migration guidance when record shapes change.

Legacy ACFS 0.1 `type/lifecycle` records MAY be imported into v0.2.1 by mapping
them to `kind/status` records. Implementations SHOULD preserve the original
fields in metadata when audit fidelity matters.

## Requirements

ACFS-compatible implementations:

- MUST preserve required fields across version boundaries.
- SHOULD preserve unknown optional metadata.
- SHOULD document supported ACFS versions, profiles, and extensions.
- SHOULD document implementation-specific runtime concepts that are not part of
  the ACFS base profile.
- MUST exclude records requiring unsupported extensions from behavioral
  guidance; rejection, quarantine, or audit-only retention remain choices.
- MUST NOT allow unknown extensions to bypass status, scope, authority, risk,
  retrieval, or revocation rules.
