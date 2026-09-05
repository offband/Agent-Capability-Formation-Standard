# Status and Lifecycle

ACFS v0.2.1 uses a small base status model and reserves heavier lifecycle
governance for optional profiles.

## Base Status Values

- **draft**: captured but not default behavioral guidance.
- **active**: eligible for behavioral recall inside scope.
- **superseded**: replaced by a newer active record.
- **revoked**: withdrawn and MUST NOT guide future behavior.

## Draft

Draft records are useful for capture, review, and capability formation.

Draft records SHOULD NOT be returned as default behavioral guidance. They MAY be
returned for review, audit, or explicit drafting workflows.

Executable or behavior-shaping capabilities MUST begin as draft unless an
implementation has explicit policy allowing immediate activation.

## Active

Active records may guide future agent behavior inside their declared scope.

Active records are not globally trusted. They apply only within their scope and
policy boundaries.

## Superseded

Superseded records have been replaced by newer or more authoritative records.

Superseded records SHOULD NOT guide future behavior when an active replacement
exists. They SHOULD remain inspectable unless retention or redaction policy
removes them.

## Revoked

Revoked records MUST NOT guide future behavior.

Revoked records MUST NOT be returned by default behavioral recall. They MAY be
returned for audit retrieval when explicitly requested and authorized.

## Promotion

Promotion is the act of changing a record from draft to active.

Low-risk memories, decisions, standards, handoffs, issues, and evidence MAY be
promoted automatically by local workspace policy.

Capabilities that reference scripts, workflows, tools, or deterministic prompts
that can shape future behavior SHOULD require explicit promotion.

Capabilities that execute code, touch production systems, handle credentials,
affect finance/legal/security, or broaden authority MUST require explicit
authorization before becoming active.

## Transition History

ACFS-Records implementations SHOULD preserve enough history to explain why a
record became active, superseded, or revoked.

ACFS-Governance implementations MUST preserve transition history with actor,
timestamp, prior status, new status, and reason when available.

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
- MUST prevent revoked records from guiding future behavior.
- SHOULD preserve transition history.
- SHOULD represent substantive changes through new or superseding records.
- MUST NOT allow status to override scope or revocation rules.
