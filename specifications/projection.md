# Projection

Projection defines how ACFS records become visible through external retrieval or
interaction surfaces.

ACFS records are the source of truth. A projection is a policy-governed view of
one or more records for a specific Consumer, scope, transport, or use case.

Projection is transport-neutral. An implementation may project records into MCP
resources, HTTP responses, files, search indexes, prompts, local UI views, or
other surfaces.

## Purpose

Projection allows ACFS-compatible systems to expose durable records without
letting those surfaces bypass lifecycle, scope, authority, risk, provenance, or
revocation rules.

Projection answers:

- Which records are visible?
- Which records may guide behavior?
- Which records are audit-only?
- How are records rendered or composed?
- How can a Consumer trace the projection back to source records?

## Source of Truth

A projection MUST NOT be treated as the canonical record unless the projection is
itself a Capability Record.

Projected artifacts SHOULD preserve traceability to their source Capability
Records.

Traceability SHOULD include:

- Source record identifiers
- Lifecycle state
- Scope
- Authority
- Risk
- Provenance or provenance reference
- Projection timestamp or revision when available

## Behavioral Projection

A behavioral projection is intended to guide future agent or system behavior.

Behavioral projections SHOULD include only Active records that match the
Consumer's authorized scope, authority, permissions, and retrieval request.

Revoked records MUST NOT be projected as behavioral guidance.

Submitted, Rejected, Deprecated, and Superseded records SHOULD NOT be projected
as behavioral guidance unless an implementation defines a specific safe use, such
as explanatory context attached to an Active replacement.

## Audit Projection

An audit projection is intended for inspection, review, debugging, compliance,
or historical understanding.

Audit projections MAY include Submitted, Rejected, Deprecated, Superseded, or
Revoked records when explicitly requested by an authorized Consumer.

Audit projections MUST NOT cause Revoked records to guide future behavior.

## Projection Policy

Implementations SHOULD define projection policy for each surface.

Projection policy SHOULD define:

- Eligible record types
- Required lifecycle states
- Required scopes and authority rules
- Risk limits
- Whether relations and dependencies are included
- Whether records may be composed into aggregate artifacts
- Whether non-Active records may appear for explanation or audit
- Required traceability metadata
- Cache invalidation or refresh behavior

Projection policy MUST NOT broaden scope, change authority, ignore risk, or
override revocation unless an authorized review or policy process first changes
the underlying ACFS records.

## Composition

A projected artifact MAY compose multiple Capability Records.

For example:

- A procedure may be projected with supporting evidence.
- A skill may be projected with dependencies and active policy constraints.
- A memory view may combine observations and decisions within one scope.

Composed projections SHOULD preserve source record identifiers for each included
record.

If any required source record is Revoked, unavailable, unsupported, or outside
the Consumer's authorized scope, the composed projection SHOULD NOT be used for
behavioral guidance.

## Caching and Indexing

Implementations MAY cache or index projections.

Cached projections MUST NOT outlive ACFS lifecycle, scope, authority, risk, or
revocation rules.

When a source record is Revoked, Superseded, Deprecated, or otherwise removed
from behavioral eligibility, implementations SHOULD invalidate or refresh any
behavioral projection that includes it.

## Projection Metadata

Projected artifacts SHOULD include or make available projection metadata.

Recommended metadata:

```json
{
  "projection": {
    "mode": "behavioral",
    "surface": "mcp",
    "projected_at": "2026-07-09T00:00:00Z",
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

An ACFS implementation MAY project Active records into MCP resources or tools.
MCP resource or tool availability MUST NOT override ACFS projection rules.

An MCP resource SHOULD be traceable to the ACFS records that produced it.

## Requirements

ACFS-compatible implementations that support projection:

- MUST treat ACFS records as the source of truth
- MUST NOT project Revoked records as behavioral guidance
- MUST preserve scope, authority, lifecycle, risk, and revocation rules during projection
- SHOULD preserve traceability from projections to source records
- SHOULD distinguish behavioral projection from audit projection
- SHOULD define projection policy for each exposed surface
- SHOULD invalidate or refresh behavioral projections when source records lose behavioral eligibility
