# Fabric Coordination

Fabric coordination defines an optional ACFS extension for representing live
agent presence, task leases, coordination events, and deterministic context
packs without making that coordination state the source of truth for durable
capability.

This extension is named `acfs.fabric.v1`.

## Purpose

ACFS defines durable records and policy-governed projections. Some agent
systems also need short-lived coordination state so multiple agents can share
context, avoid duplicate work, ask questions, acknowledge work, and expose their
activity to an operator.

Fabric coordination MAY be used for:

- agent identity and runtime presence
- agent sessions and heartbeats
- task claims or leases
- coordination messages
- receipts and acknowledgements
- append-only coordination events
- context packs composed from ACFS records and projections

Fabric coordination MUST NOT replace ACFS Records, status governance, scope,
authority, retrieval, projection, or audit requirements.

## Relationship To ACFS Records

Fabric entities are adjunct coordination primitives. They are not ACFS Records
unless an implementation explicitly stores a fabric entity using the standard
record shape.

Fabric state MAY contribute to ACFS Records. For example:

- a completed task claim MAY produce an `evidence` record
- an agent message MAY become a `memory`, `decision`, or `issue` record after
  review
- a repeated successful coordination pattern MAY become a `capability` draft
- a conflict MAY produce evidence for correction, supersession, or revocation

When fabric state contributes to an ACFS Record, the record SHOULD preserve
traceability to the fabric subject, event, claim, session, or context pack that
informed it.

## Required Boundary

Implementations that support `acfs.fabric.v1` MUST preserve this boundary:

```text
ACFS Records remain authority.
Fabric entities coordinate work.
Projections expose governed views.
Events and audit explain what happened.
```

Fabric state MUST NOT make a record active, broaden a record's scope, change a
record's authority, override status, or allow revoked records to guide
future behavior.

## Entity Families

An implementation MAY define these fabric entity families.

### Agent

An agent entity represents a durable identity or runtime summary for an agentic
system, host, workflow, tool, or service.

An agent entity SHOULD include:

- stable agent identifier
- workspace or scope
- kind or runtime type
- display name
- status
- permissions or capability flags visible to the fabric
- creation timestamp
- last-seen timestamp when available
- redaction metadata when runtime details are hidden

Agent identity does not grant ACFS authority by itself. Implementations MUST
distinguish agent identity from Contributor, Reviewer, Authority, and Consumer
permissions.

### Agent Session

An agent session represents a time-bounded connection, boot, process, task
context, or transport binding for an agent.

An agent session SHOULD include:

- stable session identifier
- related agent identifier
- principal or authenticated actor identifier
- transport or runtime channel
- status
- start timestamp
- last-seen timestamp
- expiration timestamp or time-to-live policy
- optional context projection URI

Sessions SHOULD expire or become inactive when heartbeats stop or the declared
TTL is exceeded.

### Task Claim

A task claim represents leased ownership of a task, work item, subject, or
coordination target.

A task claim SHOULD include:

- stable claim identifier
- task or subject identifier
- owner agent identifier
- owner session identifier
- status
- lease version
- claimed timestamp
- renew-after timestamp when available
- expiration timestamp
- release timestamp when applicable
- conflict metadata
- idempotency key or idempotency reference for mutations

Task claims SHOULD be treated as leases, not permanent authority. Expired or
released claims SHOULD NOT be treated as active ownership.

### Fabric Event

A fabric event is an append-oriented coordination event.

A fabric event SHOULD include:

- stable event identifier
- lane
- event type
- subject identifier
- actor agent identifier when available
- actor session identifier when available
- causation identifier when available
- correlation identifier when available
- payload
- redaction metadata
- retention metadata
- creation timestamp
- expiration timestamp when applicable

Common lanes MAY include:

- `identity`
- `session`
- `claim`
- `message`
- `receipt`
- `evidence`
- `audit`
- `projection`

Fabric events MAY be used for operator visibility, audit support, and later
formation into ACFS Records. Event payloads MUST NOT bypass ACFS review or
status requirements before guiding future behavior.

### Message And Receipt

Messages are fabric events intended to communicate status, questions, blockers,
requests, or handoffs.

Receipts are fabric events intended to acknowledge that a message, claim,
projection, record, or action result was seen, accepted, rejected, completed, or
otherwise handled.

Messages and receipts SHOULD use stable subject identifiers so an operator or
agent can trace them to records, runs, claims, sessions, projections, or other
fabric events.

## Context Pack

A context pack is a deterministic projection prepared for a Consumer, task,
scope, session, or operator view.

A context pack is a projection, not an editable memory store.

A context pack SHOULD include:

- projection identifier
- projection type
- scope
- requested task or query
- editable flag
- source trace
- payload
- redaction metadata

The source trace SHOULD identify source records, projections, evidence, or other
inputs with stable identifiers, URIs, digests, status, scope, authority, and
risk when available.

Context packs intended for behavioral guidance MUST follow ACFS behavioral
projection rules. Revoked records MUST NOT be included as behavioral guidance.

## Write Constraints

Shared or remote fabric write operations SHOULD require:

- authorization for the specific operation
- idempotency keys for retryable mutations
- stable subject identifiers
- audit or event emission
- redaction metadata for payloads that may hide sensitive content
- retention or TTL metadata
- quota and rate-limit behavior

Fabric write operations SHOULD NOT grant broad record, run, action, or workflow
permissions unless those permissions are independently authorized.

## Operator Visibility

Fabric coordination exists partly to reduce friction without making the
operator blind.

Implementations SHOULD expose operator-visible read surfaces for:

- active agents and sessions
- task claims and conflicts
- messages and unresolved questions
- receipts and acknowledgements
- capability health derived from ACFS records
- evidence related to active work
- context-pack source traces
- audit and redaction state

Operator views MUST preserve the distinction between behavioral guidance and
audit inspection.

## MCP And Other Transports

Fabric coordination MAY be exposed through MCP tools, HTTP APIs, local user
interfaces, files, event streams, or other transports.

Transport availability MUST NOT override ACFS status, scope, authority, risk,
retrieval, projection, or revocation rules.

Tools that create, renew, release, or mutate fabric state SHOULD enforce
operation-specific authorization and SHOULD emit fabric events or audit history.

## Conformance

`acfs.fabric.v1` is an optional extension. Implementations that claim support
for this extension:

- MUST support ACFS-Records.
- MUST preserve the boundary between ACFS Records and fabric coordination
  state.
- MUST NOT allow fabric state to bypass status, scope, authority, risk,
  retrieval, projection, or revocation rules.
- SHOULD expose stable identifiers for agents, sessions, claims, events,
  receipts, and context packs.
- SHOULD preserve source traceability from context packs to source records and
  projections.
- SHOULD preserve enough audit or event history to explain fabric mutations.
- SHOULD require idempotency for shared or remote write mutations.
- SHOULD document retention, redaction, quota, and rate-limit behavior.
