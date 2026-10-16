# ACFS Records

An ACFS Record is the governed contextual record and foundational primitive of
ACFS v0.2.1. ACFS Core is ACFS-Records as defined in [Conformance](conformance.md).

It is a durable, addressable, scoped object that preserves agent-contributed
workspace context so future agents can recall and reuse it without reading long
prompt files or reconstructing prior sessions.

## Minimal Shape

An ACFS-Records implementation MUST preserve these fields:

```json
{
  "id": "acfs:record:workspace:decision:example",
  "kind": "memory|decision|standard|capability|evidence|handoff|issue",
  "status": "draft|active|superseded|revoked",
  "scope": "workspace:example",
  "title": "Short durable title",
  "body": "Primary durable content.",
  "metadata": {
    "acfs_version": "v0.2.1"
  },
  "provenance": {
    "actor": "agent-or-user",
    "created_at": "2026-08-15T00:00:00Z",
    "source": "task/session/tool/user"
  }
}
```

An implementation MAY add and preserve:

```json
{
  "summary": "Short recall-oriented summary",
  "tags": ["optional", "labels"],
  "relations": [{"type": "supersedes", "target": "acfs:record:..."}],
  "authority": "organization:example",
  "risk": "low|medium|high",
  "expires_at": "2026-09-15T00:00:00Z",
  "updated_at": "2026-08-15T00:00:00Z"
}
```

Unknown optional fields SHOULD be preserved during import, export, retrieval,
and supersession unless policy requires redaction or deletion.

## Required Fields

The `id` field identifies the record. It MUST be stable and unique within the
record store.

The `kind` field identifies the record's purpose. Core kinds are:

- `memory`: durable context, repeated facts, or user preferences.
- `decision`: a choice future agents should respect inside scope.
- `standard`: a rule, convention, interface, or invariant.
- `capability`: a reusable behavior, skill, script, prompt, workflow, or
  procedure candidate.
- `evidence`: support for or against another record.
- `handoff`: continuity context for another agent/session.
- `issue`: durable blocker, risk, bug, or unresolved question.

These seven values are the complete v0.2.1 Core `kind` enum. Custom kinds MUST
use the [extension representation](versioning-and-extensions.md#extension-representation)
with an appropriate Core kind at the portable boundary. Declaring an extension
does not permit extra values in `kind` or `status`.

The `status` field identifies whether the record may guide future behavior.

The `scope` field defines where the record may influence future behavior.
Consumers MUST NOT apply a record outside its declared scope unless an explicit
policy or authorized reviewer broadens the scope.

The `title` field provides a short human-readable summary.

The `body` field contains the primary durable content.

The `provenance` field identifies the actor, timestamp, and source that created
the record.

The required `metadata` object contains `acfs_version`, which MUST be `v0.2.1`
for records claiming this version. `provenance` requires `actor`, `created_at`,
and `source`. See the existing [JSON schema](../schemas/acfs-record.schema.json)
for structural constraints. Structural validity does not confer authority.
Additional metadata entries may contain implementation-specific data. Metadata
MUST NOT bypass status, scope, revocation, or promotion rules.

## Optional Fields

The `summary` field is a compact recall summary. Implementations MAY generate it
from `body`.

The `tags` field supports lightweight retrieval.

The `relations` field contains sparse relation objects. Empty relation arrays
are not required.

The `authority` field identifies the person, organization, policy boundary, or
system responsible for trust decisions. It is optional in ACFS-Records and
required only when a claimed governance profile or policy requires it.

The `risk` field classifies behavioral impact. It is optional in ACFS-Records
and required only when a claimed governance profile or policy requires it.

## Status Rules

Default behavioral recall SHOULD return only `active` records.

`draft` records MAY be returned for review, drafting, or audit. They SHOULD NOT
be used as default behavioral guidance.

Consumers MUST NOT knowingly use `superseded` records as authoritative guidance.
They MAY be exposed as clearly identified historical or explanatory context,
as specified in
[Lifecycle](lifecycle.md#superseded).

Consumers MUST NOT knowingly use `revoked` records as authoritative guidance.
Policy-authorized cached or offline use, verification triggers, and disconnected
consistency limits are defined in [Projection](projection.md#caching-and-indexing);
these rules do not change record status or grant new authority.

## Revision and Mutation

ACFS Records SHOULD be append-oriented durable state.

Substantive content changes SHOULD create a new record related through
`supersedes` rather than silently rewriting the old record.

Implementations MAY expose a current view, but they SHOULD preserve enough
history to explain what guided prior agent behavior.

## Requirements

ACFS-Records implementations:

- MUST preserve required fields.
- MUST preserve status.
- MUST preserve scope.
- MUST preserve provenance.
- MUST preserve `metadata.acfs_version`.
- MUST prevent knowingly using revoked or superseded records as authoritative
  guidance, including cached use under the rules above.
- SHOULD support import and export using the standard shape.
- SHOULD support supersession without silent history loss.
- MUST NOT allow metadata or transport availability to bypass status, scope, or
  revocation rules.
