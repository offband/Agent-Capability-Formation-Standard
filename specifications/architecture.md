# Architecture

Architecture defines the responsibilities an ACFS-compatible system preserves
when it stores durable records for agents.

ACFS does not require a specific runtime, storage engine, transport, framework,
or deployment model. The base architecture is intentionally small: write scoped
records, index them, recall the records that matter, and prevent revoked or
out-of-scope records from shaping behavior.

ACFS defines the portable boundary for durable memory and capability. A runtime
or product built on ACFS may add local storage, user interfaces, action
execution, run history, artifacts, triggers, packages, billing, hosted identity,
or agent coordination. Those implementation concepts are outside the base ACFS
architecture unless they are represented as ACFS records, relations, metadata,
or documented extensions.

## Purpose

ACFS separates durable agent records from chat history, scratchpads, logs,
message buses, and application state.

An ACFS-compatible architecture allows agentic systems to:

- Write small durable records.
- Preserve provenance and scope.
- Index records for exact lookup and recall.
- Retrieve active records for future work.
- Keep draft, superseded, and revoked records out of default behavioral recall.
- Promote reusable capabilities only through an explicit review path.
- Audit, revise, supersede, or revoke records over time.

## Components

An implementation may include the following components:

- **Agentic System**: the agent, host, workflow, tool, or automation producing or
  consuming records.
- **Contributor**: the actor or system that writes a record.
- **Record Store**: the system responsible for validating, indexing,
  persisting, and retrieving ACFS records.
- **Reviewer**: the user, policy engine, trusted agent, or system process that
  promotes capabilities or changes status.
- **Authority**: the person, organization, policy boundary, or system
  responsible for trust decisions within a scope.
- **Consumer**: the actor or system that retrieves records for future use.
- **Audit Layer**: the system or process responsible for preserving record
  history, status changes, and review decisions.

A single local service MAY combine these components. Even when combined,
implementations SHOULD preserve the conceptual boundaries between writing,
validation, review, retrieval, and audit.

Implementation-specific objects MAY support the runtime around these
components. For example, a runtime may store artifacts, actions, runs, task
claims, or packages in native tables. When those objects influence future agent
behavior or need to be shared across implementations, they SHOULD be traceable
to ACFS records and relation edges.

## Basic Flow

A typical ACFS flow is:

1. A Contributor writes an ACFS record.
2. A Record Store validates the base shape.
3. The record is indexed by identifier, kind, status, scope, title, tags, and
   body.
4. Active records become eligible for scoped recall.
5. Draft capabilities remain draft until promoted by an authorized review path.
6. A Consumer recalls applicable records for future agent work.
7. Status changes and review decisions are preserved for audit.

This flow is illustrative. Implementations MAY support quarantine, redaction,
conflict review, retention checks, signature verification, or policy evaluation.

## Record Store

The Record Store preserves ACFS records and makes them available under the rules
of the standard.

A Record Store SHOULD support:

- Record writes.
- Structural validation.
- Persistence across process restarts.
- Indexing.
- Exact lookup by identifier.
- Scoped recall.
- Search.
- Status changes.
- Relation lookup when relations are supported.
- Provenance preservation.
- Scope enforcement.
- Audit retrieval.

A Record Store MUST NOT treat storage alone as ACFS compatibility. Base
compatibility requires preserving required record fields, status, provenance,
scope, default retrieval behavior, and revocation rules.

## Validation Boundary

Validation is a structural boundary, not a trust boundary.

A Record Store MAY validate that a record includes required fields, valid status,
valid kind, declared scope, provenance metadata, and relation metadata.

Validation MUST NOT be treated as truth, safety, authorization, or promotion.

Draft records remain draft after validation. A draft capability still requires
review or policy approval before it can safely guide future agent behavior.

## Review Boundary

Review is the boundary where a reusable capability may become active future
guidance.

Review MAY be performed by a human, policy engine, trusted agent, or system
process.

Implementations SHOULD require review before high-risk records become active.
High-risk records include executable capabilities, policies, authority changes,
triggers, records that can cause future actions, and records that influence
security-sensitive behavior.

A Contributor is not automatically authorized to promote its own capability.

## Retrieval Boundary

Retrieval is the boundary where durable records may influence future behavior.

Consumers SHOULD retrieve active records by default within the requested scope.

Consumers MUST NOT use revoked records for behavioral guidance.

Consumers MUST NOT apply records outside their declared scope unless an
authorized Reviewer or policy explicitly broadens that scope.

Consumers SHOULD resolve dependencies, status, authority, risk, and
contradictions before applying a record.

## Transport

ACFS does not require a specific transport.

Implementations MAY expose ACFS operations through local function calls,
command-line tools, HTTP APIs, message queues, MCP tools, MCP resources, or
other transports.

Transport availability MUST NOT override ACFS status, authority, scope,
retrieval, or revocation rules.

## Storage

ACFS does not require a specific storage backend.

Implementations MAY use files, relational databases, document databases, graph
stores, object storage, content-addressed storage, append-only logs, or hybrid
storage systems.

Storage choice MUST NOT weaken ACFS requirements for provenance, status, scope,
relations, retrieval, correction, supersession, or revocation.

## Audit

ACFS-compatible systems SHOULD preserve enough history to explain how records
changed over time.

Audit history SHOULD include:

- Record creation.
- Validation results.
- Status changes.
- Review decisions.
- Scope changes.
- Authority changes.
- Supersession.
- Revocation.
- Relevant actors and timestamps.

Audit retrieval MAY expose records that are not available for behavioral
guidance, including draft, superseded, or revoked records, when the Consumer is
authorized to inspect them.

## Security Boundaries

ACFS architecture SHOULD treat the following operations as security-sensitive:

- Writing records.
- Promoting capabilities.
- Changing status.
- Broadening scope.
- Changing authority.
- Retrieving behavioral guidance.
- Revising records.
- Superseding records.
- Revoking records.
- Deleting or redacting records.

Implementations SHOULD apply least privilege to each operation.

## Requirements

ACFS-compatible implementations:

- MUST preserve required ACFS Record fields.
- MUST preserve status.
- MUST preserve scope.
- MUST preserve provenance.
- MUST NOT allow transport or storage choice to bypass ACFS rules.
- MUST NOT allow implementation-specific runtime objects to bypass ACFS rules
  when those objects guide future behavior.
- MUST NOT allow revoked records to guide future behavior.
- SHOULD preserve relation metadata.
- SHOULD distinguish validation from review.
- SHOULD distinguish behavioral retrieval from audit retrieval.
- SHOULD preserve audit history for status and authority changes.
