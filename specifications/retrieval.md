# Retrieval

Retrieval defines how Consumers request Capability Records from a Capability Store.

ACFS retrieval is not simple search. A Consumer may be asking for records that can influence future behavior, so retrieval MUST respect lifecycle state, scope, authority, risk, provenance, and revocation rules.

## Purpose

Retrieval allows Consumers to:

- Find records relevant to a task or scope
- Load active procedures, skills, policies, and evidence
- Avoid stale, revoked, or out-of-scope records
- Inspect historical records when authorized
- Resolve relationships between records before use

## Default Retrieval

By default, Consumers SHOULD retrieve Active records within the requested scope.

A default retrieval result SHOULD NOT include Submitted, Rejected, Deprecated, Superseded, or Revoked records unless explicitly requested and authorized.

Default retrieval is intended for behavioral guidance.

## Audit Retrieval

Audit retrieval is retrieval for inspection, review, debugging, compliance, or historical understanding.

Audit retrieval MAY return records in any lifecycle state when the Consumer is authorized to inspect them.

Audit retrieval MUST NOT cause Revoked records to guide future agent behavior.

## Filters

Capability Stores SHOULD support retrieval filters for:

- Record identifier
- Record type
- Lifecycle state
- Scope
- Authority
- Risk
- Provenance
- Recency
- Relation type
- Related record identifier

Implementations MAY support additional filters.

## Scope

Consumers MUST NOT apply a retrieved record outside its declared scope unless an authorized Reviewer or policy explicitly broadens that scope.

A record that matches a query but falls outside the Consumer’s authorized scope SHOULD NOT be returned for behavioral guidance.

## Lifecycle Handling

Retrieval behavior depends on lifecycle state:

- **Active** records SHOULD be returned by default when they match scope and query.
- **Deprecated** records MAY be returned when explicitly requested.
- **Superseded** records MAY be returned when explicitly requested or when needed to explain formation history.
- **Submitted** records SHOULD NOT be returned for behavioral guidance.
- **Rejected** records SHOULD NOT be returned for behavioral guidance.
- **Revoked** records MUST NOT be returned for behavioral guidance.

Revoked records MAY be returned for audit retrieval when explicitly requested by an authorized Consumer.

## Relations During Retrieval

Consumers SHOULD be able to request related records.

For example, a Consumer may request:

- Evidence supporting a skill
- Records superseded by a newer policy
- Dependencies required by a procedure
- Corrections that apply to a prior decision
- Contradictions affecting a record

Capability Stores SHOULD expose declared relations when requested.

Consumers SHOULD resolve required dependencies before applying a record for behavioral guidance.

## Conflict Handling

Retrieval may return records that conflict.

When records contradict one another, Consumers SHOULD consider lifecycle state, authority, scope, recency, risk, and evidence before using them.

Unresolved contradictions SHOULD reduce confidence, trigger review, or prevent behavioral use of the affected records.

## Authority

Retrieval MUST respect authority rules within the requested scope.

A Consumer SHOULD be able to identify which Authority accepted, rejected, superseded, deprecated, or revoked a record when that information is available.

Records from an unrelated or lower-priority Authority SHOULD NOT override records from the Authority responsible for the requested scope.

## Requirements

ACFS-compatible implementations that support retrieval:

- SHOULD return Active records by default
- SHOULD support filtering by scope, type, lifecycle state, authority, provenance, risk, recency, and relation
- MUST NOT return Revoked records for behavioral guidance
- MUST NOT allow retrieval to bypass scope, authority, or lifecycle rules
- SHOULD distinguish behavioral retrieval from audit retrieval
- SHOULD expose relation metadata when requested
- SHOULD allow Consumers to identify superseded, deprecated, or revoked records during audit retrieval
