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

A Reviewer SHOULD only change status within scopes where it is authorized to
act.

Authority changes, scope broadening, revocation reversal, and high-risk
promotion SHOULD require stricter authorization than ordinary record writes.

## Provenance

ACFS-compatible systems SHOULD preserve provenance for each ACFS record.

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

High-risk records SHOULD require review before becoming active.

Records that affect production systems, credentials, user identity, financial
activity, security controls, legal obligations, or persistent policy SHOULD be
treated as high risk.

## Review and Promotion

Promotion is the point where a draft capability may become reusable future
behavior.

Implementations SHOULD define explicit review policy for each scope.

Review policy SHOULD define:

- Which record kinds may become active automatically.
- Which record kinds require human review.
- Which record kinds may be reviewed by policy engine.
- Which record kinds require stronger authorization.
- Which risks prevent activation.
- Which Authorities may resolve conflicts.

A Contributor is not automatically authorized to promote its own record.

Validation MUST NOT be treated as review, approval, trust, or acceptance.

## Retrieval Safety

Retrieval can cause records to influence future behavior.

Default behavioral retrieval SHOULD return active records within the requested
scope.

Draft, superseded, and revoked records SHOULD NOT be returned for behavioral
guidance unless the retrieval mode explicitly permits them and the Consumer is
authorized.

Revoked records MUST NOT be returned for behavioral guidance.

Draft capability records MUST NOT be returned as reusable behavior by default.

Audit retrieval MAY return non-active records when explicitly requested by an
authorized Consumer.

## Revocation

Implementations MUST support revocation.

A revoked record MUST NOT guide future agent behavior.

Revocation SHOULD preserve metadata including:

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

Superseded records SHOULD NOT guide new agent behavior when an active
replacement exists within the same scope.

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

Storage availability MUST NOT cause revoked records to guide future behavior.

## Requirements

ACFS-compatible implementations:

- MUST treat durable record operations as security-sensitive.
- MUST support revocation.
- MUST prevent revoked records from guiding future behavior.
- MUST preserve scope and authority boundaries.
- SHOULD preserve provenance and audit history.
- SHOULD apply least privilege to record operations.
- SHOULD classify records by risk.
- SHOULD require review before high-risk records become active.
- SHOULD support correction, supersession, redaction, and retention policy.
- MUST NOT allow transport, storage, metadata, or relations to bypass status,
  scope, authority, risk, or revocation rules.
