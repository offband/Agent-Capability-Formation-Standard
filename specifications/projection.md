# Projection

Projection defines how ACFS records become visible through external retrieval or
interaction surfaces. Projection support is optional and is not a Core service.
The requirements here apply to implementations that provide projections.

ACFS records are the source of truth. A projection is a policy-governed view of
one or more records for a specific Consumer, scope, transport, or use case.

Projection is transport-neutral. An implementation may project records into MCP
resources, HTTP responses, files, search indexes, prompts, local UI views, or
other surfaces.

## Purpose

Projection lets ACFS-compatible systems expose durable records without letting
those surfaces bypass status, scope, authority, risk, provenance, or revocation
rules.

Projection answers:

- Which records are visible?
- Which records may guide behavior?
- Which records are audit-only?
- How are records rendered or composed?
- How can a Consumer trace the projection back to source records?

## Source of Truth

A projection MUST NOT be treated as the canonical record unless the projection
is itself an ACFS record.

Projected artifacts SHOULD preserve traceability to their source records.

Traceability SHOULD include:

- Source record identifiers.
- Record status.
- Kind.
- Scope.
- Authority when available.
- Risk when available.
- Provenance or provenance reference.
- Projection timestamp or revision when available.

## Behavioral Projection

A behavioral projection is intended to guide future agent or system behavior.

Behavioral projections SHOULD include only active records that match the
Consumer's authorized scope, authority, permissions, and retrieval request.

Revoked records MUST NOT be projected as behavioral guidance.

Draft and superseded records MAY be included as clearly identified non-active
review, historical, or explanatory context. Superseded records MUST NOT remain
authoritative guidance. Draft capability inspection MUST be clearly marked
non-active and MUST NOT authorize reusable executable behavior.

## Audit Projection

An audit projection is intended for inspection, review, debugging, compliance,
or historical understanding.

Audit projections MAY include draft, superseded, or revoked records when
explicitly requested by an authorized Consumer.

Audit projections MUST NOT cause revoked records to guide future behavior.

## State Capsules

A state capsule is a compact behavioral projection for a task, workspace, or
session.

A state capsule SHOULD:

- Include active scoped records most relevant to the current task.
- Prefer summaries and identifiers over full record bodies when space is tight.
- Preserve source record identifiers for follow-up lookup.
- Exclude revoked records.
- Exclude draft capabilities from behavioral guidance.

State capsules are projections, not source records.

## Projection Policy

Implementations SHOULD define projection policy for each surface.

Projection policy SHOULD define:

- Eligible record kinds.
- Required statuses.
- Required scopes and authority rules.
- Risk limits.
- Whether relations and dependencies are included.
- Whether records may be composed into aggregate artifacts.
- Whether non-active records may appear for explanation or audit.
- Required traceability metadata.
- Cache invalidation or refresh behavior.

Projection policy MUST NOT broaden scope, change authority, ignore risk, or
override revocation unless an authorized review or policy process first changes
the underlying ACFS records.

## Composition

A projected artifact MAY compose multiple ACFS records.

For example:

- A handoff may combine decisions, issues, and recent evidence.
- A state capsule may combine workspace standards and current blockers.
- A promoted capability may be projected with its evidence and active policy
  constraints.

Composed projections SHOULD preserve source record identifiers for each included
record.

If any required source record is revoked, unavailable, unsupported, or outside
the Consumer's authorized scope, the composed projection SHOULD NOT be used for
behavioral guidance.

## Caching and Indexing

Implementations MAY cache or index projections.

Cached projections MUST NOT outlive ACFS status, scope, authority, risk, or
revocation rules.

When a source record is revoked, superseded, or otherwise removed from
behavioral eligibility, implementations MUST prevent cached or projected copies
from continuing to act as authoritative guidance. They MAY invalidate, refresh,
or withhold the affected guidance; audit copies may remain available when
authorized. A cached `active` value or an unexpired cache lifetime MUST NOT
override a later revocation or supersession.

Implementations providing cached behavioral guidance MUST document how current
eligibility is established before use and how lifecycle changes reach consumers.
Consumers MUST NOT use a cached copy as guidance if current eligibility cannot
be established. ACFS does not prescribe polling, notifications, a cache lifetime,
or a distributed consistency protocol, and does not guarantee instantaneous
notification across disconnected participants. Lack of connectivity is not
permission to rely on stale approval. Reactivation requires
[fresh authorization](lifecycle.md#reactivation).

## Projection Metadata

Projected artifacts SHOULD include or make available projection metadata.

Recommended metadata:

```json
{
  "projection": {
    "mode": "behavioral",
    "surface": "mcp",
    "projected_at": "2026-08-15T00:00:00Z",
    "source_records": ["acfs:record:example"],
    "scope": "repository:github.com/example/project",
    "authority": "organization:example"
  }
}
```

## Relationship to Retrieval

Retrieval selects records. Projection renders selected records into a surface.

An implementation MAY combine retrieval and projection in one operation, but it
SHOULD preserve the distinction internally.

Retrieval rules determine which records are eligible. Projection rules determine
how eligible records are exposed.

## Relationship to MCP

MCP is one possible projection surface.

An ACFS implementation MAY project active records into MCP resources or tools.
MCP resource or tool availability MUST NOT override ACFS projection rules.

An MCP resource SHOULD be traceable to the ACFS records that produced it.

## Requirements

ACFS-compatible implementations that support projection:

- MUST treat ACFS records as the source of truth.
- MUST NOT project revoked records as behavioral guidance.
- MUST preserve scope, authority, status, risk, and revocation rules during
  projection.
- SHOULD preserve traceability from projections to source records.
- SHOULD distinguish behavioral projection from audit projection.
- SHOULD define projection policy for each exposed surface.
- MUST prevent cached or projected copies from continuing as authoritative
  guidance when source records lose behavioral eligibility, as specified above.
