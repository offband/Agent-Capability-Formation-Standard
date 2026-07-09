# MCP Binding

The ACFS MCP binding defines an optional projection from ACFS records into MCP
resources or tools.

ACFS is not an MCP extension and does not require MCP. MCP is one possible
transport for exposing ACFS records and operations to agents.

## Binding Principle

MCP availability MUST NOT override ACFS lifecycle, scope, authority, risk,
retrieval, or revocation rules.

An MCP server MAY expose ACFS records as resources, tools, prompts, or a
combination of those surfaces. The server remains responsible for enforcing ACFS
projection rules before records influence agent behavior.

## Resource URIs

ACFS records exposed as MCP resources SHOULD use stable URIs.

Recommended forms:

```text
acfs://{authority}/{scope}/{type}/{id}
acfs://{authority}/{scope}/{type}/{id}?rev={revision}
```

Implementations MAY use implementation-native URIs when documented.

MCP resource URIs are projection addresses. They SHOULD remain traceable to the
source ACFS record identifiers that govern lifecycle, scope, authority, risk,
and revocation.

## Resources

An ACFS-MCP implementation MAY expose:

- Individual Capability Records
- Retrieval result sets
- Audit views
- Scope or Authority metadata
- Conformance declarations

Behavioral resource listings SHOULD include only records that are eligible for
behavioral guidance under ACFS retrieval and projection rules.

Audit resource listings MAY include non-Active records when explicitly requested
and authorized.

## Tools

An ACFS-MCP implementation MAY expose tools such as:

- `acfs.submit_record`
- `acfs.get_record`
- `acfs.retrieve_records`
- `acfs.get_related_records`
- `acfs.propose_transition`
- `acfs.validate_record`
- `acfs.conformance`

Tool names are recommendations, not mandatory protocol names.

Tools that write records, change lifecycle state, broaden scope, change
Authority, redact content, delete records, or expose audit retrieval MUST enforce
authorization appropriate to the operation.

## Retrieval Modes

MCP bindings SHOULD distinguish behavioral retrieval from audit retrieval.

A behavioral retrieval tool or resource listing MUST NOT return Revoked records
as guidance.

An audit retrieval tool MAY return Revoked, Rejected, Deprecated, Superseded, or
Submitted records only when explicitly requested by an authorized Consumer.

## Submission

Record submission through MCP SHOULD accept the standard Capability Record shape
or an implementation-defined draft shape that is validated before becoming a
Capability Record.

Failed validation SHOULD be returned as a tool result or audit event. Failed
validation SHOULD NOT create behavioral guidance.

## Requirements

ACFS-MCP implementations:

- MUST support ACFS-Core and ACFS-Projection
- MUST enforce lifecycle, scope, authority, risk, retrieval, and revocation rules
- MUST NOT expose Revoked records as behavioral guidance
- SHOULD preserve traceability from MCP artifacts to source ACFS records
- SHOULD expose conformance information
- SHOULD provide stable resource URIs
- SHOULD distinguish behavioral retrieval from audit retrieval
