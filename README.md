# Agent Capability Formation Standard

ACFS v0.2.1 defines a durable record primitive for agent workspaces.

## Version

The current release is **v0.2.1**. ACFS Core in this release covers durable
records, scoped recall, state capsules, and capability lifecycle.

ACFS Core is deliberately small: durable records, scoped recall, state
capsules, and capability lifecycle. An agent should be able to persist and
recall the durable facts that make a workspace reliable across sessions,
reboots, model changes, and tool boundaries. Those records may capture memory,
decisions, standards, evidence, issues, handoffs, and draft capabilities.

ACFS is not a chat history format, storage engine, app framework, or
inter-agent message bus. It does not define runtime execution, tool invocation,
hosting, authentication, package managers, billing, or agent orchestration. It
defines how agent-contributed records are written, addressed, scoped, recalled,
summarized into state capsules, superseded, revoked, and promoted into reusable
capability.

ACFS is the portable standard. Implementations such as FlowOS may provide the
runtime that saves, updates, executes, reviews, packages, and presents ACFS
records and capabilities. Runtime objects such as artifacts, actions, runs,
triggers, packages, and UI state are valid implementation concepts when they map
cleanly to ACFS records, relations, metadata, or documented extensions at the
portable boundary.

## Requirement Language

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”,
“SHOULD NOT”, “RECOMMENDED”, “NOT RECOMMENDED”, “MAY”, and “OPTIONAL” in ACFS
documents are to be interpreted as described in BCP 14 [RFC2119] [RFC8174]
when, and only when, they appear in all capitals.

## Core Primitive

An ACFS Record is a durable, typed object written to an ACFS-compatible store
so future agents can quickly recall relevant workspace context instead of
reconstructing it from large prompt files or prior chat.

The base profile is **ACFS-Records**. It requires only the fields needed for
durable recall and safe behavioral use:

```json
{
  "id": "acfs:record:workspace:decision:example",
  "kind": "decision",
  "status": "active",
  "scope": "workspace:example",
  "title": "Use ACFS Records as the base primitive",
  "body": "ACFS v0.2.1 centers on durable records, scoped recall, state capsules, and capability lifecycle.",
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

The initial record kinds are:

- **memory**: durable project context, repeated facts, or user preferences.
- **decision**: a choice that future agents should respect inside scope.
- **standard**: a rule, convention, interface, or invariant for future work.
- **capability**: a reusable behavior, skill, script, deterministic prompt, or
  workflow candidate.
- **evidence**: support for or against another record or capability.
- **handoff**: concise continuity context for the next agent/session.
- **issue**: a durable blocker, risk, bug, or unresolved question.

Implementations MAY define additional kinds when documented.

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

Agents may draft capabilities when repeated behavior emerges. A capability can
reference a skill, script, deterministic prompt, workflow, or external artifact,
but executable or behavior-shaping capabilities MUST NOT become default
behavioral guidance until explicitly promoted by policy, user approval, or an
authorized review path.

This preserves the useful part of the original ACFS idea: agents can form
capabilities over time without turning every durable note into executable trust.

## Retrieval

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

- **ACFS-Records**: minimum durable record and recall profile.
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
- `specifications/conformance.md`: compatibility profiles
- `specifications/versioning-and-extensions.md`: extension/version rules
- `specifications/workflow-artifacts.md`: non-core workflow artifact notes
- `specifications/fabric-coordination.md`: non-core coordination fabric notes
- `security/trust-and-safety.md`: durable record safety guidance
- `schemas/acfs-record.schema.json`: ACFS v0.2.1 record schema
- `schemas/capability-record.schema.json`: legacy governed record schema
- `examples/valid/`: ACFS v0.2.1 Core examples
- `examples/invalid/`: ACFS v0.2.1 Core negative examples
- `examples/legacy/`: deprecated ACFS 0.1 compatibility examples

## License

See [LICENSE](LICENSE).
