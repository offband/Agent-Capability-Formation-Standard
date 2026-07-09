# Lifecycle

Lifecycle state defines the current standing of a Capability Record within a declared scope.

A record’s lifecycle state determines whether it may be retrieved, trusted, applied, corrected, superseded, deprecated, revoked, or used for future agent behavior.

Lifecycle state does not define the record type. An observation, skill, policy, run result, or evidence record may each move through lifecycle states.

## States

Initial lifecycle states are:

- **Submitted**: the record has been received by a Capability Store but has not yet been validated.
- **Validated**: the record satisfies the structural requirements of the standard.
- **Rejected**: the record is structurally valid but has not been accepted for future use.
- **Active**: the record has been accepted for use within its declared scope.
- **Superseded**: the record has been replaced by a newer or more authoritative record.
- **Deprecated**: the record remains available for historical or audit purposes but SHOULD NOT be used for new agent work.
- **Revoked**: the record has been withdrawn from use and MUST NOT guide future agent behavior.

Validation does not imply that a record is true, trusted, or approved for future use.

## Submitted

A Submitted record has been received but has not yet passed structural validation.

Submitted records MUST NOT be treated as trusted durable state.

Submitted records SHOULD NOT be returned for behavioral guidance unless the Consumer explicitly requests unvalidated records and is authorized to receive them.

## Validated

A Validated record satisfies the structural requirements of ACFS.

Validation confirms that required fields are present and well-formed. It does not confirm truth, safety, authority, scope correctness, or fitness for future use.

Validated records MAY be reviewed, rejected, promoted, corrected, or revoked.

## Rejected

A Rejected record is structurally valid but has not been accepted for future use.

Rejected records MUST NOT guide future agent behavior.

Rejected records MAY remain available for audit, review history, or future reconsideration.

A Rejected record SHOULD include a rejection reason when available.

Invalid submissions are not Rejected Capability Records unless an implementation
chooses to preserve them as structurally valid records with an error payload.
Failed structural validation SHOULD be represented as validation results or audit
events rather than behavioral records.

## Active

An Active record has been accepted for use within its declared scope.

Active records MAY be returned by default retrieval when they match the Consumer’s scope, authority, permissions, and query.

Active records are not globally trusted. They are only active within the scope and policy boundaries that accepted them.

## Superseded

A Superseded record has been replaced by a newer or more authoritative record.

Superseded records SHOULD NOT guide new agent behavior when an Active replacement exists within the same scope.

Superseded records SHOULD identify the replacement record through relation metadata such as `superseded_by`.

Superseded records MAY remain available for audit, provenance, compatibility, or explanation.

## Deprecated

A Deprecated record remains available but SHOULD NOT be used for new agent work.

Deprecation is appropriate when a record is obsolete, discouraged, no longer preferred, or maintained only for historical purposes.

Deprecated records SHOULD include a reason for deprecation and, when applicable, a replacement or migration path.

## Revoked

A Revoked record has been withdrawn from use because it is unsafe, invalid, unauthorized, superseded by correction, no longer permitted, or otherwise disallowed within its scope.

Revoked records MUST NOT guide future agent behavior.

Revoked records MUST NOT be returned by default retrieval for behavioral guidance.

Revoked records MAY be returned for audit purposes when explicitly requested by an authorized Consumer.

A Revoked record SHOULD include revocation metadata, including actor, timestamp, reason, and replacement record when applicable.

## Transitions

Capability Stores SHOULD preserve lifecycle transition history.

Transition history SHOULD include:

- Prior state
- New state
- Actor responsible for the transition
- Timestamp
- Reason
- Related record identifiers when applicable

Implementations MUST NOT allow lifecycle transitions to bypass authority, scope, or review policy.

## Common Transitions

Common lifecycle transitions include:

- Submitted -> Validated
- Validated -> Rejected
- Validated -> Active
- Active -> Superseded
- Active -> Deprecated
- Active -> Revoked
- Deprecated -> Revoked
- Superseded -> Revoked

Implementations MAY support additional transitions when documented.

## Transition Metadata

Lifecycle transitions SHOULD be recorded as append-only events.

Transition events SHOULD include:

| From | To | Actor | Required metadata |
| --- | --- | --- | --- |
| Submitted | Validated | Capability Store or validator | validation timestamp, validation result |
| Validated | Rejected | Reviewer or policy | reason, authority, reviewer or policy identifier |
| Validated | Active | Reviewer or policy | reason, authority, reviewer or policy identifier |
| Active | Superseded | Reviewer or policy | reason, `superseded_by` record identifier when available |
| Active | Deprecated | Reviewer or policy | reason, migration or replacement guidance when available |
| Active | Revoked | Authority or authorized reviewer | reason, actor, timestamp, affected scope |
| Deprecated | Revoked | Authority or authorized reviewer | reason, actor, timestamp, affected scope |
| Superseded | Revoked | Authority or authorized reviewer | reason, actor, timestamp, affected scope |

Implementations MAY support additional transitions when documented.

## Review Requirements

Records that may influence future behavior SHOULD be reviewed before becoming Active.

High-risk records SHOULD require explicit review before becoming Active. High-risk records include skills, policies, authority changes, triggers, and records that may cause future actions.

Low-risk records, such as observations or run evidence, MAY become Active automatically when allowed by scope policy.

## Retrieval Behavior

By default, Consumers SHOULD retrieve Active records within the requested scope.

Deprecated and Superseded records MAY be returned when explicitly requested.

Rejected and Submitted records SHOULD NOT be returned for behavioral guidance.

Revoked records MUST NOT be returned for behavioral guidance.

Audit retrieval MAY return any lifecycle state when the Consumer is authorized to inspect historical records.

## Requirements

ACFS-compatible implementations that support lifecycle state:

- MUST preserve lifecycle state for each Capability Record
- MUST distinguish validation from acceptance
- MUST prevent Revoked records from guiding future behavior
- SHOULD preserve lifecycle transition history
- SHOULD represent lifecycle changes as transition events rather than silent mutation
- SHOULD require review for high-risk records before activation
- SHOULD expose lifecycle state during retrieval
- MUST NOT allow lifecycle state to override scope, authority, or revocation rules
