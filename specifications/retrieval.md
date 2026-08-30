# Retrieval

ACFS retrieval is recall for durable agent records.

The default consumer is an agent starting or resuming work. It needs a compact,
scoped set of relevant records, not a raw archive.

## Modes

**Behavioral recall** returns records that may guide future behavior. It SHOULD
return active records within scope and MUST NOT return revoked records.

**Audit retrieval** returns records for inspection, debugging, compliance, or
history. It MAY include draft, superseded, and revoked records when explicitly
requested and authorized.

## Search

Search returns matching records using text, tags, kind, scope, status, recency,
and relation filters.

Search may be broader than recall. Consumers SHOULD avoid treating every search
result as behavioral guidance unless the result is explicitly marked behavioral.

## Recall

Recall returns task-relevant active records for a scope.

Recommended response:

```json
{
  "mode": "behavioral",
  "scope": "workspace:example",
  "task": "ship payment integration",
  "records": [],
  "omitted": {
    "draft": 0,
    "superseded": 0,
    "revoked": 0,
    "out_of_scope": 0
  },
  "warnings": []
}
```

## State Capsules

A state capsule is a compact briefing composed from recalled records.

State capsules SHOULD be short enough to load at task start and SHOULD include
source record identifiers so the agent can inspect details only when needed.

State capsules SHOULD NOT include revoked records as behavioral guidance.

## Filters

ACFS-Retrieval implementations SHOULD support filters for:

- Record identifier
- Kind
- Status
- Scope
- Tags
- Authority
- Risk
- Recency
- Relation type
- Related record identifier

## Conflict Handling

Recall may find conflicting active records.

When unresolved contradictions exist, retrieval SHOULD include a warning or
reduce confidence. Consumers SHOULD request review or avoid using the affected
records when the conflict impacts behavior.

## Requirements

ACFS-Retrieval implementations:

- MUST distinguish behavioral recall from audit retrieval.
- MUST NOT return revoked records for behavioral guidance.
- SHOULD return active scoped records by default.
- SHOULD expose omission and warning metadata.
- SHOULD support task-scoped recall and compact state capsules.
- MUST NOT allow retrieval to bypass status, scope, authority, or revocation
  rules.
