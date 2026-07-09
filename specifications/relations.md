# Relations

Relations define how Capability Records connect to one another.

ACFS treats records as part of a governed graph, not as isolated memory entries. A record may support, revise, replace, contradict, or depend on another record. These relationships allow Consumers to understand not only what a record says, but how it fits into the larger formation history.

## Purpose

Relations allow ACFS-compatible systems to:

- Preserve formation history
- Track evidence and support
- Identify superseded or corrected records
- Detect contradictions and conflicts
- Resolve dependencies before applying a record
- Prevent older records from silently overriding newer or more authoritative records

## Relation Types

A Capability Record MAY declare relationships to other records.

Initial relation types are:

- **supersedes**: this record replaces one or more earlier records.
- **superseded_by**: this record has been replaced by one or more newer or more authoritative records.
- **corrects**: this record corrects an error, assumption, behavior, or claim in another record.
- **contradicts**: this record conflicts with another record but does not necessarily replace it.
- **depends_on**: this record requires another record to be valid, understood, or applied.
- **derived_from**: this record was formed from one or more source records.
- **evidence_for**: this record supports another record.
- **evidence_against**: this record weakens, challenges, or disproves another record.

## Direction

Relations are directional.

For example, if record `A` supersedes record `B`, then `A` SHOULD include `B` in `supersedes`. Record `B` MAY include `A` in `superseded_by`.

Implementations SHOULD maintain reverse relations when possible, but Consumers MUST NOT assume that reverse relations are always present unless the Capability Store guarantees them.

## Supersession

Supersession is used when a newer or more authoritative record replaces an older record.

A Superseded record SHOULD NOT guide new agent behavior when an Active replacement exists within the same scope.

Supersession SHOULD preserve the replaced record for audit, provenance, and historical review.

A record MAY supersede multiple records.

## Correction

Correction is used when a record identifies and fixes an error in another record.

A correction MAY lead to supersession, deprecation, or revocation, but correction alone does not require any specific lifecycle transition.

Corrected records SHOULD remain inspectable unless removed by retention, privacy, or legal policy.

## Contradiction

Contradiction is used when two records conflict but the system has not resolved which record should take precedence.

Consumers SHOULD treat unresolved contradictions as a reason to reduce confidence, request review, or avoid using the affected records for behavioral guidance.

A contradiction MUST NOT automatically revoke either record.

## Dependency

Dependency is used when one record requires another record to be valid, understood, or safely applied.

Consumers SHOULD resolve dependencies before applying a record.

If a required dependency is Revoked, unavailable, or outside the Consumer’s authorized scope, the dependent record SHOULD NOT be used for behavioral guidance.

## Evidence

Evidence relations connect support or challenge records to the records they affect.

Evidence records MAY support formation, promotion, review, supersession, deprecation, or revocation.

A record with strong supporting evidence is not automatically trusted. Trust remains subject to lifecycle state, scope, authority, review policy, and risk classification.

## Scope

Relations do not automatically broaden scope.

A record in one scope MAY relate to a record in another scope, but Consumers MUST NOT apply either record outside its declared scope unless an authorized Reviewer or policy explicitly permits it.

## Requirements

ACFS-compatible implementations that support relations:

- MUST preserve declared relation type and target record identifier
- SHOULD preserve relation direction
- SHOULD support reverse lookup when feasible
- SHOULD expose relations during retrieval when requested
- MUST NOT allow relations to bypass lifecycle, authority, scope, or revocation rules
- SHOULD preserve relations when records are promoted, superseded, deprecated, or revoked
