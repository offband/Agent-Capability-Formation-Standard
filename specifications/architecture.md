# Architecture

Architecture defines the major components and responsibilities of an ACFS-compatible system.

ACFS does not require a specific runtime, storage engine, transport, framework, or deployment model. The architecture describes roles and boundaries that implementations SHOULD preserve even when multiple roles are combined in a single system.

## Purpose

The purpose of ACFS architecture is to separate durable capability formation from ordinary memory, tool calling, and unstructured logs.

An ACFS-compatible architecture allows agentic systems to:

- Submit durable Capability Records
- Validate record structure
- Preserve provenance, scope, authority, lifecycle state, and relations
- Review and promote records according to policy
- Retrieve records for future behavioral guidance
- Audit, revise, supersede, deprecate, or revoke records over time

## Components

An ACFS-compatible system may include the following components:

- **Agentic System**: the agent, host, workflow, tool, or automation environment producing or consuming records.
- **Contributor**: the actor or system that submits a Capability Record.
- **Capability Store**: the system responsible for validating, indexing, persisting, and retrieving Capability Records.
- **Reviewer**: the user, policy engine, trusted agent, or system process that evaluates records and changes lifecycle state.
- **Authority**: the person, organization, policy boundary, or system responsible for trust decisions within a scope.
- **Consumer**: the actor or system that retrieves Capability Records for future use.
- **Audit Layer**: the system or process responsible for preserving record history, lifecycle transitions, and review decisions.

A single implementation MAY combine multiple components. For example, one local service may act as Capability Store, Reviewer, Consumer, and Audit Layer. Even when combined, implementations SHOULD preserve the conceptual boundaries between these responsibilities.

## Basic Flow

A typical ACFS flow is:

1. A Contributor submits a Capability Record.
2. A Capability Store validates the record structure.
3. The record is assigned or checked against scope and authority.
4. A Reviewer or policy process accepts, rejects, promotes, supersedes, deprecates, or revokes the record.
5. A Consumer retrieves applicable records for future agent work.
6. Lifecycle transitions and review decisions are preserved for audit.

This flow is illustrative, not mandatory. Implementations MAY support additional steps such as quarantine, redaction, conflict review, retention checks, signature verification, or policy evaluation.

## Capability Store

The Capability Store is responsible for preserving ACFS records and making them available under the rules of the standard.

A Capability Store SHOULD support:

- Record submission
- Structural validation
- Persistence
- Indexing
- Retrieval
- Lifecycle state changes
- Relation lookup
- Provenance preservation
- Scope and authority enforcement
- Audit retrieval

A Capability Store MUST NOT treat storage alone as ACFS compatibility. Compatibility requires preserving the required record fields, lifecycle state, provenance, scope, authority, relations, retrieval behavior, and revocation rules.

## Validation Boundary

Validation is a structural boundary, not a trust boundary.

A Capability Store MAY validate that a record includes required fields, valid lifecycle state, valid type, declared scope, declared authority, provenance metadata, and relation metadata.

Validation MUST NOT be treated as acceptance, truth, safety, or authorization.

A Validated record still requires review or policy approval before it can safely guide future agent behavior.

## Review Boundary

Review is the boundary where a record may become usable future guidance.

Review MAY be performed by a human, policy engine, trusted agent, or system process.

Implementations SHOULD require review before high-risk records become Active. High-risk records include skills, policies, authority changes, triggers, records that can cause future actions, and records that influence security-sensitive behavior.

A Contributor is not automatically authorized to review, promote, or activate its own records.

## Retrieval Boundary

Retrieval is the boundary where durable records may influence future behavior.

Consumers SHOULD retrieve Active records by default within the requested scope.

Consumers MUST NOT use Revoked records for behavioral guidance.

Consumers MUST NOT apply records outside their declared scope unless an authorized Reviewer or policy explicitly broadens that scope.

Consumers SHOULD resolve required dependencies, lifecycle state, authority, risk, and contradictions before applying a record.

## Transport

ACFS does not require a specific transport.

Implementations MAY expose ACFS operations through local function calls, command-line tools, HTTP APIs, message queues, MCP tools, MCP resources, or other transports.

Transport availability MUST NOT override ACFS lifecycle, authority, scope, retrieval, or revocation rules.

## Storage

ACFS does not require a specific storage backend.

Implementations MAY use:

- Files
- Relational databases
- Document databases
- Graph stores
- Object storage
- Content-addressed storage
- Append-only logs
- Hybrid storage systems

Storage choice MUST NOT weaken ACFS requirements for provenance, lifecycle state, scope, authority, relations, retrieval, correction, supersession, deprecation, or revocation.

## Audit

ACFS-compatible systems SHOULD preserve enough history to explain how records changed over time.

Audit history SHOULD include:

- Record creation
- Validation results
- Lifecycle transitions
- Review decisions
- Scope changes
- Authority changes
- Supersession
- Deprecation
- Revocation
- Relevant actors and timestamps

Audit retrieval MAY expose records that are not available for behavioral guidance, including Rejected, Deprecated, Superseded, or Revoked records, when the Consumer is authorized to inspect them.

## Security Boundaries

ACFS architecture SHOULD treat the following operations as security-sensitive:

- Submitting records
- Promoting records
- Changing lifecycle state
- Broadening scope
- Changing authority
- Retrieving behavioral guidance
- Revising records
- Superseding records
- Deprecating records
- Revoking records
- Deleting or redacting records

Implementations SHOULD apply least privilege to each operation.

## Requirements

ACFS-compatible implementations:

- MUST preserve required Capability Record fields
- MUST preserve lifecycle state
- MUST preserve scope and authority
- MUST preserve provenance
- MUST NOT allow transport or storage choice to bypass ACFS rules
- MUST NOT allow Revoked records to guide future behavior
- SHOULD preserve relation metadata
- SHOULD distinguish validation from review
- SHOULD distinguish behavioral retrieval from audit retrieval
- SHOULD preserve audit history for lifecycle and authority changes
