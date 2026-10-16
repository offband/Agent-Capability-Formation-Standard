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

Consumers and implementations MUST NOT knowingly project or use revoked or
superseded records as authoritative guidance. Cached observations of status
are subject to the validity rules in [Caching and Indexing](#caching-and-indexing).

Draft and superseded records MAY be included as clearly identified non-active
review, historical, or explanatory context. Known superseded records MUST NOT
remain authoritative guidance. Draft capability inspection MUST be clearly marked
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

Consumers and implementations MUST NOT knowingly use revoked or superseded
records as authoritative guidance, even within an unexpired cache window.
On learning of withdrawal, they MUST stop the affected behavioral use and
invalidate, refresh, or withhold the guidance. Authorized audit copies MAY remain.

Applicable policy MAY explicitly permit cached or offline guidance based on
previously verified authorization and status. Such permission MUST define a
bounded validity window and the permitted scope, uses, and risk boundaries.
Implementations MUST document how the window is determined, how consumers
establish that it remains valid, and how lifecycle changes are handled when
received or on reconnection. An ordinary storage cache lifetime is insufficient
unless applicable policy explicitly authorizes behavioral use for that window.

Before each use, consumers MUST establish that the policy permission and its
validity window still cover the guidance, scope, intended use, and risk, and
that no known revocation or supersession prohibits use. This does not require
contacting the source on each use when policy permits offline use. Consumers
MUST obtain fresh verification before further behavioral use when cached
authorization expires, its validity cannot be established, or applicable policy
requires verification. If verification cannot be obtained, they MUST withhold
the affected guidance. Reconnection MUST include verification before further
use, rather than silently renewing the offline window from a stale copy.

For high-risk operations, applicable policy MAY require continuous connectivity
or immediate revalidation. Offline permission MUST NOT bypass these conditions,
explicit high-risk authorization, or runtime execution restrictions.

Cache validity does not grant new authority, broaden scope, constitute approval,
or override revocation or supersession. Fresh verification checks continued
eligibility under existing authorization; restoring a withdrawn record instead
requires [fresh authorization](lifecycle.md#reactivation).

Disconnected consumers may temporarily use guidance revoked or superseded
elsewhere without knowing it, until reconnection and verification, expiry of
the authorized validity window, or earlier receipt of withdrawal information.
This is an unavoidable consistency limitation of policy-authorized offline use,
not permission to ignore known withdrawal. ACFS prescribes no synchronization
protocol, notification service, cache duration, or instantaneous consistency
guarantee. Policy determines the acceptable window and risk boundaries.

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
- MUST NOT knowingly project or use revoked or superseded records as
  authoritative guidance.
- MUST preserve scope, authority, status, risk, and revocation rules during
  projection.
- SHOULD preserve traceability from projections to source records.
- SHOULD distinguish behavioral projection from audit projection.
- SHOULD define projection policy for each exposed surface.
- MUST enforce policy-authorized validity windows and risk boundaries for cached
  or offline guidance, require verification when due, and stop behavioral use
  upon learning of withdrawal, as specified above.
