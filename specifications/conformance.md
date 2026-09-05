# Conformance

Conformance defines how implementations describe which ACFS v0.2.1 requirements
they support.

ACFS Core covers durable records, scoped recall, state capsules, and capability
lifecycle. Implementations SHOULD publish a conformance declaration that lists
supported profiles and extensions.

## ACFS-Records

ACFS-Records is the minimum compatibility profile.

An ACFS-Records implementation MUST:

- Preserve required ACFS Record fields.
- Validate record structure.
- Preserve status and scope.
- Preserve provenance.
- Preserve `metadata.acfs_version: "v0.2.1"` on v0.2.1 records.
- Prevent revoked records from guiding future behavior.
- Distinguish behavioral recall from audit retrieval.
- Support import/export of records using the v0.2.1 record shape.

## ACFS-Capabilities

ACFS-Capabilities covers reusable behavior formed from records.

An ACFS-Capabilities implementation MUST support ACFS-Records and MUST:

- Represent capability drafts as `kind=capability`.
- Prevent draft executable or behavior-shaping capabilities from default
  behavioral recall/use.
- Require explicit promotion before executable capabilities become active.
- Preserve artifact references and runtime constraints when present.
- Preserve provenance from source records, evidence, or review.

## ACFS-Governance

ACFS-Governance covers review, authority, risk, and transition history.

An ACFS-Governance implementation MUST support ACFS-Records and MUST:

- Preserve authority and risk when supplied or required by policy.
- Preserve review and promotion events.
- Distinguish contributors from reviewers or authorities.
- Require authorized review for high-risk activation.
- Preserve reasons for rejection, promotion, supersession, and revocation when
  available.

## ACFS-Relations

ACFS-Relations covers governed record graphs.

An ACFS-Relations implementation MUST support ACFS-Records and MUST:

- Preserve relation type and target record identifier.
- Expose relation metadata during retrieval when requested.
- Prevent relations from bypassing status, scope, authority, risk, or revocation
  rules.

ACFS-Relations implementations SHOULD support reverse relation lookup.

## ACFS-Retrieval

ACFS-Retrieval covers behavioral recall, search, state capsules, and audit
retrieval.

An ACFS-Retrieval implementation MUST support ACFS-Records and MUST:

- Distinguish behavioral recall from audit retrieval.
- Prevent revoked records from behavioral recall.
- Expose status in retrieval results.
- Enforce scope during behavioral recall.

ACFS-Retrieval implementations SHOULD support filters for kind, scope, status,
authority, risk, tags, recency, and relation.

## ACFS-MCP

ACFS-MCP covers optional exposure through MCP.

An ACFS-MCP implementation MUST support ACFS-Records and MUST ensure MCP tools
or resources do not override ACFS status, scope, promotion, retrieval, or
revocation rules.

ACFS-MCP implementations SHOULD follow `specifications/mcp-binding.md`.

## ACFS-Portable

ACFS-Portable covers exchange between implementations.

An ACFS-Portable implementation MUST support ACFS-Records and SHOULD:

- Export records using the v0.2.1 record shape.
- Preserve required fields and known optional fields.
- Document extension fields.
- Reject, quarantine, or mark audit-only records that require unsupported
  mandatory extensions.

## Legacy ACFS 0.1

Implementations MAY claim compatibility with the legacy Capability Record
profile described in `specifications/capability-records.md`.

Legacy compatibility is not required for ACFS-Records.

## Non-Core Notes

Runtime execution, tool invocation, hosting, authentication, package managers,
workflow engines, billing, and agent orchestration are outside ACFS Core.
Documents such as `specifications/agent-packaging.md`,
`specifications/workflow-artifacts.md`, and
`specifications/fabric-coordination.md` are non-core implementation notes unless
a future ACFS release promotes a focused extension.

## Requirements

Implementations claiming ACFS compatibility:

- MUST support ACFS-Records.
- MUST document supported optional profiles.
- MUST NOT claim support for a profile unless profile requirements are met.
- SHOULD expose conformance information to administrators, integrators, and
  agents.
