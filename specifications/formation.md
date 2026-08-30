# Capability Formation

Capability formation is the process by which durable records become reusable
future behavior.

ACFS vNext treats formation as an optional layer over ACFS Records. The base
primitive captures and recalls records. The capability layer promotes repeated,
observed, or reviewed behavior into active capability.

## Inputs

Formation may use any ACFS Record kind, especially:

- `memory`: repeated context or preference.
- `decision`: selected direction.
- `standard`: invariant or convention.
- `evidence`: proof or counterproof.
- `handoff`: continuity from prior work.
- `issue`: recurring blocker or risk.
- `capability`: draft behavior to refine and promote.

## Capability Records

A capability record describes a reusable behavior. It may reference a skill,
script, deterministic prompt, workflow, procedure, or external artifact.

Example:

```json
{
  "kind": "capability",
  "status": "draft",
  "title": "Run payment-link smoke checks",
  "metadata": {
    "artifact_type": "script",
    "artifact_ref": "scripts/stripe_smoke_check.sh",
    "runtime_constraints": "approval-required"
  }
}
```

## Draft First

Agents MAY draft capabilities when repeated behavior emerges.

Executable or behavior-shaping capabilities SHOULD remain draft until promoted
by explicit approval or policy.

Draft capabilities SHOULD NOT be returned by default behavioral recall.

## Promotion

Promotion makes a draft capability active.

Promotion SHOULD preserve:

- Source records or evidence.
- Actor or reviewer.
- Timestamp.
- Reason.
- Runtime constraints.

High-risk capabilities MUST require explicit authorization before becoming
active.

## Runtime Constraints

Capability artifacts that execute code, invoke tools, touch production systems,
handle credentials, affect financial/legal/security workflows, or broaden
authority MUST declare or inherit runtime constraints.

Agents MUST NOT treat a promoted capability as permission to bypass host
sandbox, user approval, tool policy, or workspace restrictions.

## Requirements

ACFS-Capabilities implementations:

- MUST represent reusable behavior as `kind=capability`.
- MUST prevent draft executable capabilities from default behavioral use.
- SHOULD preserve source records and evidence during promotion.
- MUST require explicit authorization for high-risk activation.
- MUST NOT allow artifact references to bypass status, scope, revocation, or
  runtime constraints.
