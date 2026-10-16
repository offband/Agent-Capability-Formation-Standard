# Status and Lifecycle

ACFS v0.2.1 uses a small base status model and reserves heavier lifecycle
governance for optional profiles. ACFS Core remains ACFS-Records; the
transition-evidence requirements below apply only to ACFS-Governance.

## Base Status Values

- **draft**: captured but not default behavioral guidance.
- **active**: eligible for behavioral recall inside scope.
- **superseded**: replaced by a newer active record.
- **revoked**: withdrawn; consumers MUST NOT knowingly use it as authoritative
  guidance.

## Draft

Recording captures information. Proposing guidance presents that information
for possible activation; it does not grant authority. Draft records support both
capture and proposals without introducing another lifecycle state.

Structural validation establishes only that a record has a valid shape.
Validation, successful execution, artifact availability, or repeated use MUST
NOT be treated as approval or authorization.

Draft records SHOULD NOT be returned as default behavioral guidance. They MAY be
returned for review, audit, or explicit drafting workflows.

Executable or behavior-shaping capabilities MUST begin as draft unless an
applicable policy or authorized review explicitly permits immediate activation
under the same authorization rules as promotion. This does not require storing
an intermediate draft or introduce another status.

## Active

Active records may guide future agent behavior inside their declared scope.

Active records are not globally trusted. They apply only within their scope and
policy boundaries. Setting or importing `status=active` does not itself prove
that activation was authorized. Consumers MUST NOT infer approval authority
from a status value, contributor identity, or structural validity alone.

## Superseded

Superseded records have been replaced by newer or more authoritative records.

Supersession MUST be permitted by applicable policy or an authorized reviewer
for the affected scope. A `supersedes` relation alone MUST NOT activate a
replacement or authorize withdrawal of the prior guidance. The replacement MUST
have its own authorized activation before it is used as guidance.

Consumers MUST NOT knowingly use a superseded record as authoritative guidance.
It MAY be shown as clearly identified historical or explanatory context, not as an
instruction to apply. Implementations MUST distinguish the superseded record
from its replacement. Loss or revocation of the replacement MUST NOT silently
reactivate the old record. Superseded records SHOULD remain inspectable unless
retention or redaction policy removes them.

## Revoked

Revocation MUST be permitted by applicable policy or an authorized reviewer for
the affected scope. Revocation removes behavioral eligibility. Consumers MUST
NOT knowingly use revoked records as authoritative guidance, including through
a cached copy or projection. A disconnected consumer's status observation may
lag a withdrawal elsewhere; policy-authorized offline use and its limits are
defined in [Projection](projection.md#caching-and-indexing). Cache validity does
not override a known withdrawal or itself authorize activation.

Known revoked records MUST NOT be returned by default behavioral recall. They MAY be
returned for audit retrieval when explicitly requested and authorized.

## Promotion

Promotion is the act of changing a record from draft to active.

Activation, including initial creation as `active`, MUST be permitted by
applicable policy or authorized review for the record and scope. An authorized
reviewer is an actor permitted by applicable policy to make that decision.
An applicable policy MUST itself be established by authority for the affected
scope; a contributor's assertion of a policy is not authorization.
A contributor MUST NOT acquire approval authority merely by submitting a
record. A contributor MAY also review its own contribution only when applicable
policy independently authorizes that role and permits self-review.

Low-risk memories, decisions, standards, handoffs, issues, and evidence MAY be
activated automatically under an established applicable policy. No separate
human approval is required when that policy authorizes the activation. A kind
alone does not establish low risk, and omitting `risk` does not imply low risk.

Executable or behavior-shaping capabilities MUST receive explicit promotion
by applicable policy or authorized review before becoming active guidance.
Policy-authorized immediate activation counts as that decision, not as a bypass.
Capabilities that execute code, touch production systems, handle credentials,
affect finance/legal/security, or broaden authority MUST receive explicit
authorization covering the capability's behavior, scope, and relevant risk.
A generic permission to write records or automatically activate low-risk notes
MUST NOT serve as this high-risk authorization. Review MAY be performed by a
human, authorized agent, or policy process; ACFS does not mandate human review
or a policy language.

Approval permits activation within its authorized scope and constraints; it
does not itself invoke tools or grant execution permission. These rules also
apply to activation during import or replacement.

## Reactivation

If an implementation permits a `revoked` or `superseded` record to become
`active` again, it MUST obtain fresh authorization under the policy applicable
at reactivation. The decision MUST address the reason for withdrawal or
replacement and the intended scope. Prior approval, a stale active copy, or
loss of a replacement MUST NOT serve as fresh authorization. An implementation
MAY instead create a new record; neither approach adds a lifecycle state.

## Transition History

ACFS-Records implementations SHOULD preserve enough history to explain why a
record became active, superseded, or revoked. Core does not require authority
metadata or governance history on every record, or a policy engine.

ACFS-Governance implementations MUST retain inspectable evidence for activation
(including initial or automatic activation), supersession, revocation,
reactivation, and changes to scope or applicable authority. Each decision MUST
identify the following, directly or through resolvable references:

| Evidence | Minimum meaning |
| --- | --- |
| Record and contributor | The affected record identifier and the actor that contributed its content, preserving creation provenance. |
| Transition actor | The actor or process that applied the change; this is distinct from the contributor's role. |
| Reviewer or authorizing policy | The reviewer and review decision when reviewed; the applicable policy and the rule or decision used when policy-authorized. When a policy process acts without a separate reviewer, identify the automated decision rather than inventing a reviewer. |
| Applicable authority | The person, organization, system, or policy boundary that permits the decision for the affected scope; a reviewer or policy name alone is insufficient unless its authority is identifiable. |
| Timestamp and transition | When the decision took effect, prior and resulting status, and affected scope. For initial creation, indicate that there was no prior record status, without inventing another status. For scope or authority changes, preserve both prior and resulting values even if status is unchanged. |
| Reason | Why the change was authorized, including applicable constraints, the policy basis for automatic activation, or the withdrawal/replacement reason. Reactivation also addresses the prior withdrawal or replacement. |

Evidence MUST distinguish contribution, review, policy authorization, and
application of the change even when the same actor legitimately performs more
than one role. For policy decisions it MUST identify the policy basis in effect
at the time, so a later policy change does not silently rewrite the explanation.
Review decisions that deny activation MUST remain distinguishable from approval;
rejection does not require a new status. Implementations MUST preserve review
and promotion decisions, including denials, with actor, time, affected record,
applicable authority, and reason; a denied request is not a completed transition.

Evidence MAY reside in existing `metadata`, extended `provenance`, related
`decision` or `evidence` records, or an implementation's inspectable history.
Creation provenance MUST NOT be overwritten with reviewer or transition-actor
identity. The optional record-level `authority` field is not made mandatory by
this evidence requirement; the applicable authority can be identified in the
history instead. Implementations MUST document how authorized consumers can
locate and interpret this evidence. ACFS defines its meaning here, not new
required JSON fields, an event schema, an identity provider, an organizational
hierarchy, an approval mechanism, or a policy language.

## Required Edge Cases

| Situation | Required interpretation |
| --- | --- |
| An agent submits a structurally valid capability but lacks approval authority. | Submission and validation do not authorize activation. The submission may be rejected or retained as draft unless independently authorized policy or review permits activation; a requested `active` status cannot supply the missing authority. |
| An established policy automatically activates a low-risk record. | Activation is permitted without a separate human review when the policy applies to the record and scope. Under ACFS-Governance, the contributor, applying process, policy basis, applicable authority, timestamp, transition, and reason remain inspectable, with automatic activation identified. |
| An active capability is revoked while another participant holds a cached copy. | The cached `active` value is not approval or renewed authority. Explicit policy may allow offline use within a defined validity window and risk boundaries before the participant learns of revocation elsewhere. It MUST stop authoritative use upon learning of withdrawal and MUST obtain fresh verification on reconnection, expiry, uncertain validity, or when policy requires it. Without verification when due, it MUST withhold guidance. Audit retention remains possible; reactivation requires fresh authorization. |

Cache and projection freshness obligations are specified in
[Projection](projection.md#caching-and-indexing). These cases define semantic
outcomes, not runtime services or the cross-agent fixture suite deferred to #7.

## Legacy Mapping

Legacy lifecycle states map to v0.2.1 status values:

- `submitted` and `validated` map to `draft`.
- `active` maps to `active`.
- `superseded` and `deprecated` map to `superseded`.
- `revoked` maps to `revoked`.
- `rejected` maps to audit-only draft or revoked, depending on policy.

## Requirements

ACFS-compatible implementations:

- MUST preserve record status.
- MUST require applicable policy or authorized review for activation and
  authority-changing lifecycle decisions.
- MUST prevent knowingly using revoked or superseded records as authoritative
  guidance and follow the policy-bounded cache rules in projection.
- SHOULD preserve transition history.
- SHOULD represent substantive changes through new or superseding records.
- MUST NOT allow status to override scope or revocation rules.
