# Conformance

Conformance defines how implementations describe which ACFS vNext requirements
they support.

ACFS is intended to support local workspace stores, MCP-backed services, hosted
platforms, and portable archives. Implementations SHOULD publish a conformance
declaration that lists supported profiles and extensions.

## ACFS-Records

ACFS-Records is the minimum compatibility profile.

An ACFS-Records implementation MUST:

- Preserve required ACFS Record fields.
- Validate record structure.
- Preserve status and scope.
- Preserve provenance.
- Prevent revoked records from guiding future behavior.
- Distinguish behavioral recall from audit retrieval.
- Support import/export of records using the vNext record shape.

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

## ACFS-Fabric

ACFS-Fabric covers optional live coordination state for agent identity,
sessions, task leases, coordination events, receipts, and context-pack
projections.

ACFS-Fabric implementations MUST support ACFS-Records and MUST keep ACFS
Records as the authority layer. Fabric entities coordinate work; they do not
become behavioral guidance unless they are formed into ACFS Records or governed
projections under ACFS rules.

ACFS-Fabric implementations SHOULD follow
`specifications/fabric-coordination.md`.

## ACFS-Packaging

ACFS-Packaging covers optional distribution as skills, plugins, implementation
packages, or combined installable bundles.

An ACFS-Packaging implementation MUST support ACFS-Records and MUST:

- Document whether the package is skills-only, implementation-backed, or
  combined.
- Distinguish workflow instructions from live durable storage.
- Prevent packaging metadata from bypassing ACFS status, scope, promotion,
  authorization, or revocation rules.

ACFS-Packaging implementations SHOULD:

- Keep main skill instructions focused.
- Put detailed schemas, examples, and implementation notes in references.
- Include positive and negative activation tests.
- Expose skill, plugin, or packaging version in conformance metadata when
  available.
- Follow `specifications/agent-packaging.md`.

## ACFS-Portable

ACFS-Portable covers exchange between implementations.

An ACFS-Portable implementation MUST support ACFS-Records and SHOULD:

- Export records using the vNext record shape.
- Preserve required fields and known optional fields.
- Document extension fields.
- Reject, quarantine, or mark audit-only records that require unsupported
  mandatory extensions.

## Legacy ACFS 0.1

Implementations MAY claim compatibility with the legacy Capability Record
profile described in `specifications/capability-records.md`.

Legacy compatibility is not required for ACFS-Records.

## Requirements

Implementations claiming ACFS compatibility:

- MUST support ACFS-Records.
- MUST document supported optional profiles.
- MUST NOT claim support for a profile unless profile requirements are met.
- SHOULD expose conformance information to administrators, integrators, and
  agents.
