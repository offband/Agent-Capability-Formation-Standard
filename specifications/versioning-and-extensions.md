# Versioning and Extensions

Versioning and extensions define how ACFS evolves without breaking durable
records or forcing every implementation to support every feature.

## Standard Version

ACFS documents SHOULD identify the standard version or revision they target.

Capability Records MAY include a standard version in metadata:

```json
{
  "metadata": {
    "acfs_version": "0.1"
  }
}
```

Implementations SHOULD document which ACFS version or revision they support.

## Record Compatibility

Implementations MUST preserve required fields even when they do not understand
all optional or implementation-specific metadata.

Unknown metadata fields SHOULD be preserved during import, export, retrieval,
revision, and lifecycle transitions unless policy requires removal.

Unknown relation types SHOULD NOT be treated as behavioral guidance unless the
implementation understands their meaning.

## Extensions

Implementations MAY define extensions.

Extensions SHOULD declare:

- Extension name
- Version
- Required conformance profiles
- Added record fields, metadata fields, relation types, or lifecycle behavior
- Whether the extension is optional or mandatory for records that use it

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

## Requirements

ACFS-compatible implementations:

- MUST preserve required fields across version boundaries
- SHOULD preserve unknown optional metadata
- SHOULD document supported ACFS versions and extensions
- SHOULD reject, quarantine, or restrict records that require unsupported mandatory extensions
- MUST NOT allow unknown extensions to bypass lifecycle, scope, authority, risk, retrieval, or revocation rules
