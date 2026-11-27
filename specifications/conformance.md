# Conformance

Conformance defines how implementations describe which ACFS v0.2.1 requirements
they support.

**ACFS Core is ACFS-Records.** This document defines the minimum compatibility
contract and the additional requirements of optional profiles. The record shape
is defined in [ACFS Records](records.md); base status and scope meanings are
specified in [Lifecycle](lifecycle.md) and [Scope and Authority](scope-and-authority.md).
Implementations SHOULD publish a conformance declaration listing supported
profiles and extensions.

Core requires governed contextual records, not a particular service API. The
presence of a capability kind, relation field, or authority metadata does not
require formation, graph, or governance services. Optional features MUST NOT
bypass Core status, scope, provenance, or revocation rules.

## ACFS-Records

ACFS-Records is the minimum compatibility profile.

An ACFS-Records implementation MUST:

- Preserve required ACFS Record fields.
- Validate record structure with the base schema and apply the conditional
  [extension compatibility rules](versioning-and-extensions.md#extension-representation).
- Preserve status and scope.
- Preserve provenance.
- Preserve `metadata.acfs_version: "v0.2.1"` on v0.2.1 records.
- Prevent knowingly using revoked or superseded records as authoritative
  guidance, including enforcement of the policy-authorized validity windows and
  verification rules in [Projection](projection.md#caching-and-indexing) when
  cached or offline guidance is provided.
- Apply records only inside their declared scope unless explicitly broadened
  by policy or an authorized reviewer.
- Support revocation and preserve the meanings of `draft`, `active`,
  `superseded`, and `revoked`.
- Distinguish behavioral use from audit inspection when exposing records;
  this does not require separate retrieval APIs.
- Prevent draft executable or behavior-shaping capabilities from default
  behavioral use and require explicit promotion by policy or authorized review
  before they become active guidance, when such capabilities are supported.
- Preserve relation type and target identifier when relations are present.

ACFS-Records implementations SHOULD support import/export using the v0.2.1
record shape. Core does not mandate an import/export service; ACFS-Portable
adds exchange-specific expectations.

Validation MUST NOT be treated as approval, promotion, or execution permission.
Core does not require an authority or risk field on every record, a reviewer
identity provider, an event schema, a workflow engine, or a policy backend.
Existing conditional safety requirements remain applicable when a feature is
provided, using the authorization rules in [Lifecycle](lifecycle.md#promotion).

## Minimum Independent Implementation

A local file store can validate and retain the record in the README using
`schemas/acfs-record.schema.json`, preserve its identifier, version and
provenance, and constrain use to its declared scope and status. It can mark a
withdrawn record `revoked` and exclude it from guidance while retaining it for
inspection. A documented local read/write process is sufficient; no recall
ranking, state capsule, promotion endpoint, FlowOS, MCP, GitHub, or agent runtime
is required. A second implementation can interpret the same record meanings
without adopting the first implementation's storage or APIs.

## ACFS-Capabilities

ACFS-Capabilities covers reusable behavior formed from records.

An ACFS-Capabilities implementation MUST support ACFS-Records and MUST:

- Represent capability drafts as `kind=capability`.
- Prevent draft executable or behavior-shaping capabilities from default
  behavioral recall/use.
- Require explicit promotion by applicable policy or authorized review before
  executable or behavior-shaping capabilities become active, including explicit
  authorization for high-risk capabilities as defined in [Lifecycle](lifecycle.md#promotion).
- Preserve artifact references and runtime constraints when present.
- Preserve provenance from source records, evidence, or review.

## ACFS-Governance

ACFS-Governance covers review, authority, risk, and transition history.

An ACFS-Governance implementation MUST support ACFS-Records and MUST:

- Preserve authority and risk when supplied or required by policy.
- Preserve review and promotion decisions, including denials, and the minimum
  [transition evidence](lifecycle.md#transition-history) for activation,
  supersession, revocation, reactivation, and scope or authority changes.
- Distinguish contributor, transition actor, reviewer, authorizing policy, and
  applicable authority, even where one actor performs multiple authorized roles.
- Require explicit authorization for high-risk activation by applicable policy
  or authorized review; ordinary write permission is insufficient.
- Preserve the effective timestamp, prior and resulting status, affected scope,
  applicable authority, authorization basis, and reason as specified in lifecycle.
- Make evidence discoverable and interpretable by authorized consumers using
  [Governance Evidence Interchange](governance-evidence.md), without requiring
  a universal history/event schema.

Governance evidence identifies the authorization basis; a cached copy of that
evidence does not itself approve use, renew authority, or override withdrawal.
Policy-authorized offline use follows the validity windows, risk boundaries,
and verification rules in [Projection](projection.md#caching-and-indexing).

These stronger evidence requirements do not add required fields to every Core
record. Automatic activation remains permitted by applicable policy; a separate
human reviewer is not mandatory.

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
- Prevent knowingly returning revoked or superseded records as authoritative
  guidance; cached recall follows the validity and verification rules in projection.
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
- Preserve required-extension declarations and evidence locators.

The mandatory safe-handling rules for unsupported required extensions apply
regardless of whether ACFS-Portable is claimed; the recommendations above do
not weaken them.

## Validation Claims

Implementations MUST distinguish a base JSON Schema pass, extension validation,
and semantic conformance. An active record with valid structure is not thereby
authorized. A claim of ACFS-Governance requires the lifecycle evidence and
interchange behavior, including explicit reasons for withholding unsupported or
unverifiable guidance. See [Conformance Validation](validation.md) for executable
fixture checks and their limits.

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
