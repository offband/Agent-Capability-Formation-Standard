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

Unknown relation types SHOULD NOT be treated as behavioral guidance unless the
implementation understands their meaning.

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

Extensions SHOULD declare:

- Extension name.
- Version.
- Required conformance profiles.
- Added record fields, metadata fields, relation types, or status behavior.
- Whether the extension is optional or mandatory for records that use it.

Extension fields SHOULD be namespaced to avoid collision.

Example:

```json
{
  "metadata": {
    "extensions": ["example.audit-signature.v1"],
    "example.audit-signature.v1": {
      "signature": "..."
    }
  }
}
```

## Mandatory Extensions

Records that require an extension for safe interpretation SHOULD declare that
requirement in metadata.

Consumers that do not support a mandatory extension SHOULD NOT use the record
for behavioral guidance.

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
- SHOULD reject, quarantine, or restrict records that require unsupported
  mandatory extensions.
- MUST NOT allow unknown extensions to bypass status, scope, authority, risk,
  retrieval, or revocation rules.
