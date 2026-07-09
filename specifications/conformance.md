# Conformance

Conformance defines how implementations describe which ACFS requirements they
support.

ACFS is intended to support small local stores, agent runtimes, MCP-backed
servers, hosted services, and audit-oriented archives. Not every implementation
needs every optional capability, but implementations that claim compatibility
MUST state which conformance profiles they support.

## Profile Declarations

An implementation SHOULD publish a conformance declaration.

A conformance declaration SHOULD include:

- Implementation name and version
- ACFS version or revision targeted
- Supported conformance profiles
- Supported record types
- Supported lifecycle states
- Supported retrieval modes
- Storage and transport notes
- Extension fields or compatibility profiles required for use

## ACFS-Core

ACFS-Core is the minimum compatibility profile.

An ACFS-Core implementation MUST:

- Preserve required Capability Record fields
- Validate record structure
- Preserve lifecycle state
- Preserve scope and authority
- Preserve provenance
- Preserve risk classification
- Preserve the `relations` object
- Prevent Revoked records from guiding future behavior
- Distinguish validation from acceptance

ACFS-Core implementations SHOULD support import and export of Capability Records
using the standard record shape.

## ACFS-Review

ACFS-Review covers review and lifecycle governance.

An ACFS-Review implementation MUST support ACFS-Core and MUST:

- Support lifecycle transitions
- Preserve transition history
- Distinguish Contributors from Reviewers and Authorities
- Require authorized review or policy approval for high-risk activation
- Preserve reasons for rejection, promotion, deprecation, supersession, and revocation when available

## ACFS-Relations

ACFS-Relations covers governed record graphs.

An ACFS-Relations implementation MUST support ACFS-Core and MUST:

- Preserve declared relation type and target record identifiers
- Expose relation metadata during retrieval when requested
- Prevent relations from bypassing lifecycle, scope, authority, risk, or revocation rules

ACFS-Relations implementations SHOULD support reverse relation lookup.

## ACFS-Retrieval

ACFS-Retrieval covers behavioral and audit retrieval.

An ACFS-Retrieval implementation MUST support ACFS-Core and MUST:

- Distinguish behavioral retrieval from audit retrieval
- Prevent Revoked records from behavioral retrieval
- Enforce scope and authority during retrieval
- Expose lifecycle state in retrieval results

ACFS-Retrieval implementations SHOULD support filters for type, scope, lifecycle
state, authority, risk, provenance, recency, and relation.

## ACFS-Projection

ACFS-Projection covers policy-governed external views of records.

An ACFS-Projection implementation MUST support ACFS-Core and MUST:

- Treat ACFS records as the source of truth
- Prevent Revoked records from being projected as behavioral guidance
- Preserve lifecycle, scope, authority, risk, and revocation rules during projection
- Distinguish behavioral projection from audit projection

ACFS-Projection implementations SHOULD preserve traceability from projected
artifacts to source records and SHOULD define projection policy for each exposed
surface.

## ACFS-Audit

ACFS-Audit covers durable history and explanation.

An ACFS-Audit implementation MUST support ACFS-Core and MUST preserve enough
history to explain:

- Record creation
- Validation results
- Review decisions
- Lifecycle transitions
- Scope changes
- Authority changes
- Relation changes
- Supersession, deprecation, revocation, deletion, and redaction events

Audit history SHOULD be protected from unauthorized modification.

## ACFS-MCP

ACFS-MCP covers optional exposure through MCP.

An ACFS-MCP implementation MUST support ACFS-Core and ACFS-Projection, and MUST
ensure that MCP resource or tool availability does not override ACFS lifecycle,
scope, authority, risk, retrieval, projection, or revocation rules.

ACFS-MCP implementations SHOULD follow `specifications/mcp-binding.md`.

## ACFS-Portable

ACFS-Portable covers exchange between implementations.

An ACFS-Portable implementation MUST support ACFS-Core and SHOULD:

- Export records using the standard record shape
- Preserve required fields, lifecycle state, scope, authority, provenance, risk,
  and relations during import/export
- Document extension fields
- Reject or quarantine records that require unsupported mandatory extensions

## Requirements

Implementations claiming ACFS compatibility:

- MUST support ACFS-Core
- MUST document which optional profiles are supported
- MUST NOT claim support for a profile unless the profile requirements are met
- SHOULD expose conformance information to administrators, integrators, or Consumers
