# MCP Binding

MCP is an optional transport binding for ACFS-compatible implementations. ACFS
does not require MCP, does not define tool invocation semantics, and does not
define a standalone ACFS server product.

An implementation, such as FlowOS, may expose ACFS tools and resources through
an MCP server. That implementation remains responsible for enforcing ACFS
status, scope, promotion, retrieval, and revocation rules.

The same MCP server MAY expose runtime-specific tools for actions, triggers,
runs, artifacts, packages, or agent coordination. Those tools are outside the
ACFS-MCP profile. They remain implementation behavior even when they preserve
ACFS boundary rules and document how their behavior maps to ACFS records,
relations, metadata, or extensions.

## Recommended Tools

Implementations claiming the ACFS-MCP profile SHOULD expose a small standard
surface:

- `acfs.write_record`: create a record from a minimal draft or complete record.
- `acfs.get_record`: retrieve one record by identifier.
- `acfs.search`: search records with filters.
- `acfs.recall`: retrieve active task-relevant records for behavioral use.
- `acfs.state_capsule`: compose a compact task-scoped briefing from records.
- `acfs.supersede`: create a replacement record and mark the old record
  superseded.
- `acfs.promote_capability`: promote a draft capability when authorized.
- `acfs.conformance`: return supported profiles, versions, and limits.

These recommendations apply to supported features; the binding does not make
ACFS-Retrieval or ACFS-Capabilities mandatory. Implementations MUST document
which optional profiles their tools support and MUST NOT claim unsupported
profile behavior. Core does not require this tool surface.

Implementations MAY expose additional tools when documented.

## Server Instructions

An implementation exposing ACFS through MCP SHOULD provide server-level
instructions when the host supports them.

The opening instructions SHOULD be concise and self-contained:

```text
This implementation stores durable ACFS records. Use recall/state_capsule for
active scoped records, write_record for future-useful durable context, and
promote_capability only after authorized review. Revoked records must not guide
behavior, and draft executable capabilities are not default guidance.
```

Host-specific instruction limits vary. Put the core safety and workflow rules
first.

## Resource URIs

ACFS records exposed as MCP resources SHOULD use stable URIs:

```text
acfs://{scope}/{kind}/{id}
acfs://{scope}/{kind}/{id}?rev={revision}
```

Implementation-native URIs are allowed when documented and traceable to source
record identifiers.

## Write Behavior

`acfs.write_record` SHOULD accept a minimal draft shape and fill safe defaults
such as generated identifiers, timestamps, default status, and actor identity
when the caller is authorized.

Failed validation SHOULD be returned as a tool result or audit event. Failed
validation SHOULD NOT create behavioral guidance.

## Recall Behavior

`acfs.recall` and `acfs.state_capsule` are behavioral surfaces. They MUST NOT
include revoked records as guidance.

Draft capability records SHOULD be omitted from behavioral recall unless the
caller explicitly asks for draft review.

## Authorization

Tools that write records, promote capabilities, change scope, broaden authority,
redact content, delete records, or expose audit retrieval MUST enforce
authorization appropriate to the operation.

## Tool Metadata

When the host supports MCP tool annotations or permission metadata, ACFS-MCP
implementations SHOULD classify tools accurately.

Recommended classifications:

| Tool | Class |
| --- | --- |
| `acfs.get_record` | read-only |
| `acfs.search` | read-only |
| `acfs.recall` | read-only |
| `acfs.state_capsule` | read-only |
| `acfs.conformance` | read-only |
| `acfs.write_record` | write |
| `acfs.supersede` | write/status-changing |
| `acfs.promote_capability` | write/status-changing/high-risk when executable |

Tool metadata is advisory. It MUST NOT replace server-side authorization,
status, scope, promotion, or revocation checks.

## Requirements

ACFS-MCP implementations:

- MUST support ACFS-Records.
- MUST enforce status, scope, retrieval, promotion, and revocation rules.
- MUST NOT expose revoked records as behavioral guidance.
- SHOULD expose conformance information.
- SHOULD provide stable record URIs.
- SHOULD provide concise server instructions when supported by the host.
- SHOULD classify tool safety metadata when supported by the host.
- SHOULD distinguish behavioral recall from audit retrieval.
