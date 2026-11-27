# Agent Capability Formation Standard

ACFS standardizes governed, reusable agent context through durable, scoped
records whose status and provenance constrain their use as guidance.

## Version

The current release is **v0.2.1**. **ACFS Core is ACFS-Records**, the minimum
compatibility profile defined in [Conformance](specifications/conformance.md).
Its foundational primitive is the governed contextual record: identity, kind,
content, scope, provenance, version metadata, and the existing four statuses.

Core preserves these record meanings and safe behavioral use. Capability
formation and promotion services, richer governance and relation services,
recall, search, state capsules, projections, transport bindings, and portable
exchange services are optional. Their safety rules apply when those features
are provided; optional does not mean that status or scope can be bypassed.

ACFS is independent of FlowOS, MCP, GitHub, and specific agent runtimes. Storage,
indexing, authentication, communication, scheduling, and tool execution belong
to implementations. FlowOS is one possible implementation, not a dependency.
ACFS complements instruction files, memory stores, and orchestration systems by
standardizing the records they exchange and the limits on their authority.

## Requirement Language

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”,
“SHOULD NOT”, “RECOMMENDED”, “NOT RECOMMENDED”, “MAY”, and “OPTIONAL” in ACFS
documents are to be interpreted as described in BCP 14 [RFC2119] [RFC8174]
when, and only when, they appear in all capitals.

## Core Primitive

An ACFS Record is a durable, addressable, typed, scoped object that preserves
context and its provenance for reuse. Recording content or validating its shape
does not itself authorize that content as guidance.

The base profile is **ACFS-Records**. It requires only the fields needed for
durable context and safe behavioral use:

```json
{
  "id": "acfs:record:workspace:decision:example",
  "kind": "decision",
  "status": "active",
  "scope": "workspace:example",
  "title": "Use ACFS Records as the base primitive",
  "body": "ACFS Core is ACFS-Records: governed, reusable contextual records.",
  "metadata": {
    "acfs_version": "v0.2.1"
  },
  "provenance": {
    "actor": "agent",
    "created_at": "2026-08-15T00:00:00Z",
    "source": "design session"
  }
}
```

## Record Kinds

The seven Core record kinds are:

- **memory**: durable project context, repeated facts, or user preferences.
- **decision**: a choice that future agents should respect inside scope.
- **standard**: a rule, convention, interface, or invariant for future work.
- **capability**: a reusable behavior, skill, script, deterministic prompt, or
  workflow candidate.
- **evidence**: support for or against another record or capability.
- **handoff**: concise continuity context for the next agent/session.
- **issue**: a durable blocker, risk, bug, or unresolved question.

Implementations MAY define custom semantics through explicitly declared
[extensions](specifications/versioning-and-extensions.md#extension-representation).
Portable records retain a Core `kind`; custom kinds do not extend the base enum.

## Status

The base status values are:

- **draft**: captured but not default guidance.
- **active**: eligible for behavioral recall inside scope.
- **superseded**: replaced by a newer active record.
- **revoked**: withdrawn and MUST NOT guide future behavior.

Draft records are useful for capture and review. Active records are the default
behavioral memory. Superseded records remain useful for audit. Revoked records
must not appear in behavioral recall.

## Capability Formation

Formation services are optional; capability status and promotion safety still
apply whenever capability records are used.

Agents may draft capabilities when repeated behavior emerges. A capability can
reference a skill, script, deterministic prompt, workflow, or external artifact,
but executable or behavior-shaping capabilities MUST NOT become default
behavioral guidance until explicitly promoted by policy, user approval, or an
authorized review path.

This preserves the useful part of the original ACFS idea: agents can form
capabilities over time without turning every durable note into executable trust.

## Retrieval

Retrieval services are optional under ACFS-Retrieval. Core does not require
recall, search, or state capsule operations.

ACFS retrieval should feel like recall, not archive browsing.

The common path is:

1. At task start, request `recall` or a `state_capsule` for the workspace/task.
2. During work, write only durable records future agents can reuse.
3. At task end, write a handoff or superseding record when continuity requires
   it.

Default behavioral recall returns active, scoped, non-revoked records. Audit
retrieval may expose drafts, superseded records, and revoked records only when
explicitly requested and authorized.

## Relationship to MCP and Skills

ACFS is transport-neutral. MCP is one useful agent-facing transport that an
ACFS-compatible implementation, such as FlowOS, may expose.

An implementation exposing ACFS records through MCP should keep the
ACFS-standard surface small:

```text
acfs.write_record
acfs.get_record
acfs.search
acfs.recall
acfs.state_capsule
acfs.supersede
acfs.promote_capability
acfs.conformance
```

A skill should teach the agent the behavior: recall first, write durable records
when useful, draft capabilities when repeated behavior appears, and avoid using
unpromoted executable drafts.

A plugin or skill may teach ACFS workflow and schemas. Live durable storage
belongs to an implementation, such as FlowOS, not to ACFS itself.

## Profiles

- **ACFS-Records**: Core; minimum governed contextual record profile.
- **ACFS-Capabilities**: draft/promoted capabilities and lifecycle.
- **ACFS-Governance**: optional profile for review, authority, risk, lifecycle
  events, status history, and promotion policy.
- **ACFS-Relations**: optional profile for richer record graphs.
- **ACFS-Retrieval**: optional profile for recall, search, state capsules, and
  audit retrieval.
- **ACFS-MCP**: optional transport binding for MCP tools/resources.
- **ACFS-Portable**: optional profile for import/export.

Legacy ACFS 0.1 capability records are deprecated for new records, but remain
compatible through the governed capability profile. Implementations may accept
legacy `type/lifecycle` records and map them to `kind/status` records.

Runtime execution, tool invocation, hosting, auth, package managers, workflow
engines, and agent orchestration are implementation concerns. They may be
documented as non-core notes or extensions, but they are not ACFS Core
requirements.

## Validation

See [Conformance Validation](specifications/validation.md) for the lightweight,
offline fixture checks and the distinction between shape and authorization.

## Repository Map

- `specifications/records.md`: ACFS v0.2.1 base record shape and field rules
- `specifications/capability-records.md`: legacy governed capability profile
- `specifications/lifecycle.md`: status and promotion expectations
- `specifications/formation.md`: capability drafting and promotion
- `specifications/relations.md`: sparse relation model
- `specifications/retrieval.md`: recall, search, state capsules, and audit
- `specifications/mcp-binding.md`: optional MCP transport mapping
- `specifications/agent-packaging.md`: non-core skill/plugin packaging notes
- `specifications/projection.md`: behavioral and audit projections
- `specifications/scope-and-authority.md`: scope and optional authority
- `specifications/implementation-boundary.md`: standard/runtime boundary
- `specifications/conformance.md`: authoritative Core contract and optional profiles
- `specifications/governance-evidence.md`: portable evidence discovery and interpretation
- `specifications/validation.md`: reproducible structural and semantic fixture checks
- `specifications/core-audit.md`: compatibility findings and deferred #5–#7 work
- `specifications/versioning-and-extensions.md`: extension/version rules
- `specifications/workflow-artifacts.md`: non-core workflow artifact notes
- `specifications/fabric-coordination.md`: non-core coordination fabric notes
- `security/trust-and-safety.md`: durable record safety guidance
- `schemas/acfs-record.schema.json`: ACFS v0.2.1 record schema
- `schemas/capability-record.schema.json`: legacy governed record schema
- `examples/valid/`: structurally valid v0.2.1 records, not authorization proofs
- `examples/invalid/`: record-shape negatives and the legacy unsafe retrieval envelope
- `examples/extensions/`: illustrative extension schema and payload fixtures
- `examples/conformance/`: isolated semantic cases with explicit synthetic trust inputs
- `examples/legacy/`: deprecated ACFS 0.1 compatibility examples

## License

See [LICENSE](LICENSE).
