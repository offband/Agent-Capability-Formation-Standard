# Scope and Authority

Scope defines where an ACFS Record may influence future behavior.

Authority identifies who is responsible for trust decisions within a scope.
The record-level `authority` field is optional in ACFS-Records. Applicable
authority must be identifiable in ACFS-Governance decision evidence, but need
not be stored as a field on every record. Policy may require that field.

## Scope

Every ACFS Record MUST declare a scope.

Examples:

- `workspace:example`
- `repository:github.com/example/project`
- `organization:example`
- `user:alice`
- `tool:stripe`
- `workflow:release`

Consumers MUST NOT apply a record outside its declared scope unless an explicit
policy or authorized reviewer broadens that scope. Scope expansion and changes
to applicable authority MUST be authorized for the affected boundary, including
the destination scope; write access in the original scope is insufficient.
Copying, importing, nesting, or projecting a record MUST NOT implicitly broaden
scope or authority. Existing activation approval MUST NOT be assumed to cover a
broader scope. ACFS-Governance MUST retain the prior and resulting scope and
authority with the [transition evidence](lifecycle.md#transition-history).

## Scope Format

Implementations MAY represent scope as a string or structured object.

String scopes SHOULD be stable and unambiguous.

Structured scopes SHOULD use this shape:

```json
{
  "type": "repository",
  "id": "github.com/example/project",
  "path": "optional/subscope",
  "valid_from": "2026-08-15T00:00:00Z",
  "valid_until": "2026-09-15T00:00:00Z"
}
```

The `type` and `id` fields identify the boundary. `path`, `valid_from`, and
`valid_until` are optional refinements.

## Authority

Authority MAY be included on any ACFS Record and SHOULD be included when a
record changes future behavior, promotes a capability, broadens scope, or
affects high-risk work.

Authorities may be strings or structured objects:

```text
organization:example
user:alice
policy:example/security-review
system:flowos-policy-engine
```

```json
{"type": "organization", "id": "example"}
```

A contributor supplies the content; a reviewer makes an approval decision; an
authorizing policy permits a decision under its applicable rule; the applicable
authority is the trust boundary permitting that reviewer or policy to act.
These roles MUST NOT be inferred to be identical. The record's `authority`
value names a boundary, not proof that a reviewer is authorized within it.

ACFS-Governance implementations MUST distinguish these roles in the
[minimum transition evidence](lifecycle.md#transition-history). A contributor
MAY be a reviewer only when independently authorized by applicable policy;
submission alone MUST NOT confer approval authority. ACFS prescribes no identity
provider, organizational hierarchy, approval mechanism, or policy language.

## Nested Scope

Nested scope inheritance MUST NOT be assumed unless the implementation defines
explicit inheritance rules.

If inheritance is supported, implementations SHOULD document parent/child
behavior, record kinds that inherit, and conflict resolution.

## Time-Bound Scope

Records MAY include time bounds through structured scope fields or `expires_at`.

Expired records SHOULD NOT guide future behavior unless explicitly requested for
audit or historical context.

## Requirements

ACFS-compatible implementations:

- MUST require scope on each record.
- MUST NOT apply records outside declared scope without authorization.
- SHOULD preserve scope changes.
- MUST require explicit authorization for high-risk capability activation;
  authority evidence is required by ACFS-Governance, not as a universal Core field.
- MUST NOT allow scope or authority rules to bypass status or revocation.
