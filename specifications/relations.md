# Relations

Relations connect ACFS Records without making graph management mandatory for the
base primitive.

ACFS vNext uses sparse relation objects:

```json
{
  "relations": [
    {"type": "supersedes", "target": "acfs:record:workspace:decision:old"},
    {"type": "evidence_for", "target": "acfs:record:workspace:capability:deploy"}
  ]
}
```

The `relations` field is OPTIONAL in ACFS-Records. If present, implementations
MUST preserve relation type and target identifier.

## Initial Relation Types

- `supersedes`: this record replaces another record.
- `corrects`: this record corrects another record.
- `contradicts`: this record conflicts with another record.
- `depends_on`: this record requires another record.
- `derived_from`: this record was formed from another record.
- `evidence_for`: this record supports another record.
- `evidence_against`: this record challenges another record.

Implementations MAY define additional relation types when documented.

## Direction

Relations are directional.

If record A supersedes record B, record A SHOULD include a `supersedes`
relation targeting record B. Implementations MAY maintain reverse indexes, but
Consumers MUST NOT assume reverse relations unless the store documents them.

## Supersession

Supersession replaces old guidance without silently rewriting history.

A superseding record SHOULD be active before the old record is treated as
superseded for behavioral recall.

## Safety

Relations MUST NOT broaden scope, promote drafts, revive revoked records, or
bypass authorization.

If a required dependency is revoked, unavailable, unsupported, or outside scope,
the dependent record SHOULD NOT be used for behavioral guidance.

## Requirements

ACFS-Relations implementations:

- MUST preserve declared relation type and target record identifier.
- SHOULD support reverse lookup when feasible.
- SHOULD expose relations when requested.
- MUST NOT allow relations to bypass status, scope, authority, risk, or
  revocation rules.
