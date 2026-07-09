# Capability Records

A Capability Record is the core primitive of ACFS.

A Capability Record is a durable, typed object submitted into an ACFS-compatible system so that agentic work can be retained, evaluated, retrieved, revised, and reused over time.

A Capability Record is not always a complete capability. It may be an observation, correction, decision, procedure, skill, policy, run result, evidence item, or deprecation record that contributes to capability formation.

## Minimal Record Shape

A Capability Record MUST include the following fields:

    {
      "id": "acfs:record:string",
      "type": "observation|correction|decision|procedure|skill|policy|run_result|evidence|deprecation",
      "lifecycle": "submitted|validated|rejected|active|superseded|deprecated|revoked",
      "scope": "string",
      "authority": "string",
      "title": "string",
      "body": "string",
      "risk": "low|medium|high",
      "provenance": {
        "contributor": "string",
        "submitted_at": "RFC3339 timestamp",
        "source": "string"
      },
      "relations": {
        "supersedes": [],
        "superseded_by": [],
        "corrects": [],
        "contradicts": [],
        "depends_on": [],
        "derived_from": [],
        "evidence_for": [],
        "evidence_against": []
      },
      "metadata": {}
    }

## Required Fields

The `id` field identifies the record. It MUST be stable and unique within the Capability Store.

The `type` field identifies the kind of record being submitted.

The `lifecycle` field identifies the current standing of the record within its declared scope.

The `scope` field defines where the record may influence future behavior.

The `authority` field identifies the person, organization, policy boundary, or system responsible for trust decisions within the declared scope.

The `title` field provides a short human-readable summary of the record.

The `body` field contains the primary content of the record.

The `risk` field identifies the potential impact of allowing the record to influence future behavior.

The `provenance` field preserves the origin of the record.

The `relations` field defines how the record connects to other Capability Records.

The `metadata` field MAY contain implementation-specific fields.

## Record Types

Initial record types are:

- **observation**: a recorded fact, pattern, condition, or repeated behavior.
- **correction**: a recorded change to prior behavior, language, assumption, or process.
- **decision**: a recorded choice made within a defined scope.
- **procedure**: a repeatable sequence of steps.
- **skill**: a reusable behavior or operational pattern.
- **policy**: a rule that constrains future behavior.
- **run_result**: the outcome of a completed agentic action.
- **evidence**: support for or against another record.
- **deprecation**: a record indicating that another record should no longer guide new work.

Implementations MAY define additional record types when documented.

## Scope and Authority

A Capability Record MUST declare the scope in which it may influence future behavior.

Consumers MUST NOT apply a record outside its declared scope unless an authorized Reviewer or policy explicitly broadens that scope.

A Capability Record MUST declare an Authority.

A Contributor is not automatically the Authority for a record. Implementations MUST distinguish between the system or actor that submitted a record and the Authority responsible for accepting, rejecting, promoting, superseding, deprecating, or revoking it.

## Risk

A Capability Record MUST declare a risk level.

Initial risk levels are:

- **low**: observations, evidence, notes, or records that do not directly alter future behavior.
- **medium**: corrections, decisions, or procedures that may influence future behavior.
- **high**: skills, policies, authority changes, triggers, or records that may cause future actions.

High-risk records SHOULD require review before becoming Active.

## Provenance

A Capability Record MUST preserve provenance metadata.

At minimum, provenance MUST include:

- Contributor
- Submission timestamp
- Source

The `submitted_at` value SHOULD use an RFC3339 timestamp.

Implementations MAY include additional provenance metadata such as run identifiers, tool calls, reviewer identifiers, source documents, commit hashes, or audit references.

## Relations

A Capability Record SHOULD use relations to preserve formation history, evidence, dependencies, corrections, and supersession.

Initial relation fields are:

- `supersedes`
- `superseded_by`
- `corrects`
- `contradicts`
- `depends_on`
- `derived_from`
- `evidence_for`
- `evidence_against`

Relation values SHOULD contain target Capability Record identifiers.

Relations MUST NOT bypass lifecycle, authority, scope, or revocation rules.

## Metadata

The `metadata` object MAY contain implementation-specific fields.

Implementation-specific metadata MUST NOT be required for basic ACFS compatibility unless declared by a separate compatibility profile.

## Requirements

ACFS-compatible implementations that support Capability Records:

- MUST preserve required fields
- MUST preserve lifecycle state
- MUST preserve scope and authority
- MUST preserve provenance
- SHOULD preserve relation metadata
- SHOULD preserve risk classification
- MUST NOT allow metadata or relations to bypass lifecycle, authority, scope, or revocation rules
