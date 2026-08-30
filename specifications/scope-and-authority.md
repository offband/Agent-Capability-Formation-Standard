# Scope and Authority

Scope defines where an ACFS Record may influence future behavior.

Authority identifies who is responsible for trust decisions within a scope.
Authority is optional in the base ACFS-Records profile and required only by
governance profiles or workspace policy.

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
policy or authorized reviewer broadens that scope.

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

ACFS-Governance implementations MUST distinguish the actor that submitted a
record from the authority or reviewer that promoted it.

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
- SHOULD require authority for high-risk promotion and governance profiles.
- MUST NOT allow scope or authority rules to bypass status or revocation.
