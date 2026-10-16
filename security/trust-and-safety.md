# Trust and Safety

Trust and safety defines how ACFS-compatible systems prevent durable records
from becoming unsafe future guidance.

ACFS records may influence what future agents believe, retrieve, execute, avoid,
or trust. For this reason, record writing, promotion, retrieval, correction,
supersession, revocation, deletion, and redaction are security-sensitive
operations.

## Core Principle

Durable records are a trust boundary.

An ACFS record is not passive storage. It may affect future agent behavior, tool
use, policy interpretation, workflow execution, security posture, or user
decision-making.

Implementations MUST treat durable records as potentially behavior-shaping
inputs.

## Threat Model

ACFS-compatible systems SHOULD consider threats including:

- Unauthorized record writes.
- Contribution poisoning.
- Unsafe promotion of untrusted capabilities.
- Records applied outside their declared scope.
- Conflicting records with unclear authority.
- Stale records that remain active after conditions change.
- Sensitive data persistence.
- Tool-bound records that cause unsafe future actions.
- Cross-agent propagation of unreviewed records.
- Incomplete correction, supersession, or revocation.
- Audit history tampering.
- Prompt injection preserved as durable guidance.

## Least Privilege

Implementations SHOULD apply least privilege to all record operations.

A Contributor SHOULD only be allowed to write records within authorized scopes.

A Consumer SHOULD only retrieve records appropriate to its task, authority, trust
level, risk tolerance, and execution context.

A Reviewer MUST only change status within scopes where it is authorized to
act.

Authority changes, scope broadening, revocation reversal, and high-risk
promotion SHOULD require stricter authorization than ordinary record writes.

## Provenance

ACFS-compatible systems MUST preserve required creation provenance for each
ACFS record. Additional review and transition evidence is recommended for Core
and required for ACFS-Governance as defined in
[Lifecycle](../specifications/lifecycle.md#transition-history).

Provenance SHOULD identify:

- Contributor.
- Source.
- Creation timestamp.
- Related run, tool, document, or event when available.
- Reviewer or policy process when status changes.
- Reason for promotion, supersession, or revocation.

Records SHOULD NOT become trusted future guidance without sufficient provenance
for the relevant scope.

## Scope Safety

Scope is security-critical.

A record accepted in one scope MUST NOT be applied outside that scope unless an
authorized Reviewer or policy explicitly broadens it.

Consumers SHOULD treat missing, ambiguous, or conflicting scope as a reason to
avoid behavioral use and request review.

Nested scope inheritance MUST NOT be assumed unless the implementation defines
explicit inheritance rules.

## Risk Classes

Implementations SHOULD classify records by risk.

Initial risk classes are:

- **Low risk**: memory, evidence, notes, or records that do not directly alter
  future behavior.
- **Medium risk**: decisions, standards, issues, or procedures that may
  influence future behavior.
- **High risk**: executable capabilities, policies, authority changes, triggers,
  records that affect tool use, or records that may cause future actions.

High-risk capabilities MUST receive explicit authorization under
[Lifecycle](../specifications/lifecycle.md#promotion) before becoming active.
Review of other high-risk records is RECOMMENDED; all activation still requires
applicable policy or authorized review. Omitting or understating a `risk` value
MUST NOT bypass authorization required by the record's actual behavior.

Records that affect production systems, credentials, user identity, financial
activity, security controls, legal obligations, or persistent policy SHOULD be
treated as high risk.

## Review and Promotion

Promotion changes a record from draft to active. Initial active creation and
reactivation are subject to the same authorization rules in
[Lifecycle](../specifications/lifecycle.md#promotion).

Activation MUST be permitted by applicable policy or authorized review for the
record and scope. Established policy MAY automatically activate low-risk
records without separate human approval. High-risk capabilities MUST receive
explicit authorization covering their behavior, scope, and relevant risk; a
permission to write records or activate low-risk notes is insufficient.

Implementations SHOULD define explicit review policy for each scope.

Review policy SHOULD define:

- Which record kinds may become active automatically.
- Which record kinds require human review.
- Which record kinds may be reviewed by policy engine.
- Which record kinds require stronger authorization.
- Which risks prevent activation.
- Which Authorities may resolve conflicts.

A Contributor MUST NOT gain approval authority merely by submitting a record.
Self-review is permitted only when independently authorized by applicable policy.
ACFS-Governance implementations MUST retain the
[minimum decision and transition evidence](../specifications/lifecycle.md#transition-history),
including the policy basis for automatic activation and the reason for denial
or withdrawal. These requirements do not mandate a history on every Core record.

Validation MUST NOT be treated as review, approval, trust, or acceptance.

## Retrieval Safety

Retrieval can cause records to influence future behavior.

Default behavioral retrieval SHOULD return active records within the requested
scope.

Draft records MAY be exposed for authorized review or drafting, not as default
guidance. Known superseded records MUST NOT remain authoritative guidance; they
MAY be exposed as clearly identified historical or explanatory context. Audit
visibility does not confer behavioral eligibility.

Consumers and implementations MUST NOT knowingly return or use revoked or
superseded records as authoritative guidance. Policy-authorized offline use
follows [Projection](../specifications/projection.md#caching-and-indexing).

Draft capability records MUST NOT be returned as reusable behavior by default.

Audit retrieval MAY return non-active records when explicitly requested by an
authorized Consumer.

## Revocation

Implementations MUST support revocation.

Consumers MUST NOT knowingly use revoked records as authoritative guidance,
including through cached copies or projections. Revocation MUST be authorized
for the affected scope. Applicable policy MAY permit cached or offline guidance
within a defined validity window, scope, and risk boundaries, based on previously
verified authorization and status. Cache validity is not approval, new authority,
or an override of known withdrawal.

Fresh verification MUST precede further use on reconnection, when authorization
expires, validity cannot be established, or policy requires it. If verification
cannot be obtained when due, the guidance MUST be withheld. High-risk policy MAY
require continuous connectivity or immediate revalidation; offline permission
MUST NOT bypass those requirements. Disconnected consumers may temporarily use
guidance revoked elsewhere until reconnection and verification, authorized
window expiry, or earlier knowledge of withdrawal. ACFS does not promise
instantaneous consistency across disconnected participants.

Reactivation MUST obtain fresh authorization addressing the prior
withdrawal; old approval or a cached active value is insufficient. See
[Lifecycle](../specifications/lifecycle.md#reactivation) and
[Projection](../specifications/projection.md#caching-and-indexing).

Core implementations SHOULD preserve revocation metadata including:

- Actor responsible for revocation.
- Timestamp.
- Reason.
- Related replacement or correction record when applicable.
- Scope affected by revocation.

Revocation does not necessarily require deletion. A revoked record MAY remain
available for audit, review, legal, compliance, or historical purposes when
authorized.

## Correction and Supersession

Correction and supersession allow durable state to evolve without silently
rewriting history.

A correction SHOULD identify the record it corrects.

A superseding record SHOULD identify the record it replaces.

Consumers MUST NOT knowingly use superseded records as authoritative guidance.
Supersession requires applicable policy or authorized review; a replacement
requires its own
authorized activation. Loss of a replacement MUST NOT reactivate old guidance.
The stronger ACFS-Governance history requirements apply to both supersession
and revocation, including their reasons.

Implementations SHOULD preserve corrected and superseded records for audit
unless retention, privacy, or legal policy requires removal.

## Privacy and Retention

Durable records may preserve sensitive, personal, regulated, or stale
information.

Implementations SHOULD support retention policy, redaction, and deletion
behavior.

Records containing secrets, credentials, private keys, or tokens MUST NOT be
stored as behavioral guidance. They MUST be rejected, redacted, or restricted to
authorized audit handling according to scope policy.

Records containing sensitive personal data, regulated data, or unsafe
instructions SHOULD be rejected, redacted, restricted, or marked high risk
according to scope policy.

Revocation excludes a record from behavioral guidance. Deletion or redaction
removes or obscures stored content according to retention and privacy policy.

Redaction SHOULD preserve enough audit metadata to explain what changed, who
performed the redaction, when it occurred, and why the original content is no
longer available.

Implementations SHOULD document whether deleted or redacted records remain
visible in audit history.

## Audit Integrity

Implementations SHOULD preserve enough audit history to explain how records
influenced future behavior.

Audit history SHOULD include:

- Record creation.
- Validation results.
- Review decisions.
- Status changes.
- Scope changes.
- Authority changes.
- Relation changes.
- Supersession.
- Revocation.
- Deletion or redaction events.

Audit history SHOULD be protected from unauthorized modification.

## Transport and Storage Safety

Transport and storage choices MUST NOT weaken ACFS trust and safety rules.

An ACFS implementation MAY expose records through local files, APIs, databases,
graph stores, object storage, MCP tools, MCP resources, or other transports.

Transport availability MUST NOT override status, authority, scope, risk,
retrieval, or revocation rules.

Storage or cache availability MUST NOT justify knowingly using withdrawn
guidance or extending policy-authorized validity windows without verification.

## Requirements

ACFS-compatible implementations:

- MUST treat durable record operations as security-sensitive.
- MUST support revocation.
- MUST prevent knowingly using revoked or superseded records as authoritative
  guidance and enforce the policy-bounded offline-use rules in projection.
- MUST preserve scope and authority boundaries.
- MUST preserve required creation provenance.
- SHOULD preserve audit history; ACFS-Governance MUST retain the evidence
  specified in lifecycle.
- SHOULD apply least privilege to record operations.
- SHOULD classify records by risk.
- MUST require explicit authorization for high-risk capability activation.
- SHOULD require review before other high-risk records become active.
- SHOULD support correction, supersession, redaction, and retention policy.
- MUST NOT allow transport, storage, metadata, or relations to bypass status,
  scope, authority, risk, or revocation rules.
