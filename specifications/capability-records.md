# Legacy Capability Records

The original ACFS 0.1 Capability Record shape remains a governed compatibility
profile. It is useful for systems that need explicit authority, risk,
transition history, relation arrays, and review policy on every record.

ACFS v0.2.1 uses `specifications/records.md` as the base primitive. New
implementations SHOULD start with ACFS-Records and add governance only when
records can shape future behavior, execute code, broaden authority, or affect
high-risk work.

## Legacy Shape

The legacy Capability Record shape requires:

```json
{
  "id": "acfs:record:string",
  "type": "observation|correction|decision|procedure|skill|policy|run_result|evidence|deprecation",
  "lifecycle": "submitted|validated|rejected|active|superseded|deprecated|revoked",
  "scope": "string",
  "authority": "string",
  "title": "string",
  "body": "string",
  "risk": "low|medium|high",
  "provenance": {
    "contributor": "string",
    "submitted_at": "RFC3339 timestamp",
    "source": "string"
  },
  "relations": {
    "supersedes": [],
    "superseded_by": [],
    "corrects": [],
    "contradicts": [],
    "depends_on": [],
    "derived_from": [],
    "evidence_for": [],
    "evidence_against": []
  },
  "metadata": {}
}
```

This shape maps to ACFS v0.2.1 as follows:

| Legacy field | ACFS v0.2.1 field |
| --- | --- |
| `type` | `kind` |
| `lifecycle=submitted|validated` | `status=draft` |
| `lifecycle=active` | `status=active` |
| `lifecycle=superseded|deprecated` | `status=superseded` |
| `lifecycle=revoked|rejected` | `status=revoked` or audit-only draft |
| `provenance.contributor` | `provenance.actor` |
| `provenance.submitted_at` | `provenance.created_at` |

This table identifies corresponding field roles, not a literal renaming
algorithm. Legacy `observation`, `procedure`, `skill`, `policy`, `run_result`,
and other non-Core type values cannot simply be copied into `kind`. An adapter
MUST document its mapping to one of the seven Core kinds, preserve the original
meaning in metadata when needed, and validate the resulting record against the
base schema. Legacy `rejected` is not approval; mapping it to an audit-only draft
MUST NOT make it default guidance. Legacy compatibility remains optional.

Legacy relation arrays SHOULD be converted to sparse relation objects when
exporting to ACFS v0.2.1.

## When To Use This Profile

Use the governed Capability Record profile when records:

- define executable skills, scripts, workflows, triggers, or policies;
- change authority, scope, or production behavior;
- need formal review and transition history;
- must satisfy audit, compliance, or organizational governance rules.

Do not require this profile for ordinary durable memory, decisions, handoffs, or
low-risk evidence unless the workspace policy explicitly demands it.

## Requirements

Implementations that claim legacy Capability Record compatibility:

- MUST preserve the required legacy fields.
- MUST distinguish validation from acceptance.
- MUST preserve authority and risk.
- MUST preserve relation arrays.
- MUST prevent revoked records from guiding future behavior.
- SHOULD provide a migration or adapter path to ACFS v0.2.1 records.
