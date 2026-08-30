# Agent Packaging

Agent packaging defines how ACFS workflow guidance and compatibility metadata
are distributed to agent hosts as a skill, plugin, or implementation package.

This specification is optional. It does not change the ACFS record shape.

## Purpose

An ACFS implementation may be correct as storage but still fail in practice if
agents do not know when to recall records, when to write records, or how to
avoid unsafe capability drafts.

Agent packaging SHOULD make the default behavior obvious:

- Recall scoped records at task start.
- Write only durable future-useful records.
- Use active records as behavioral guidance.
- Keep draft capabilities out of default behavior.
- Never use revoked records as guidance.

## Skill Packages

A skill package teaches agent behavior. It does not, by itself, provide durable
storage.

An ACFS skill SHOULD include:

- A focused name and description with clear activation terms.
- Short workflow instructions in the main skill file.
- Record schema, examples, and longer references in supporting files.
- Clear fallback behavior when no ACFS store or MCP server is available.
- Safety rules for revoked records, scope, and draft executable capabilities.

The skill description SHOULD front-load terms such as `ACFS`, `durable records`,
`recall`, `handoff`, `decision`, `standard`, and `capability draft` when those
are intended activation signals.

The main skill file SHOULD stay small enough to load frequently. Detailed
schemas, examples, migration notes, and implementation guidance SHOULD live in
references.

## Plugin Packages

A plugin package distributes installable ACFS behavior to agent hosts.

An ACFS plugin MAY be:

- **Skills-only**: packages ACFS workflow instructions, schemas, examples, and
  test prompts.
- **Implementation-backed**: configures an ACFS-compatible implementation that
  exposes records and recall through MCP or another documented transport.
- **Combined**: bundles ACFS workflow instructions with an implementation
  connection.

A skills-only plugin MUST NOT imply live durable persistence unless it is paired
with an ACFS-compatible store.

An implementation-backed plugin SHOULD include a skill or implementation
instructions that explain the recall/write/promotion workflow. Tool
availability alone is not enough.

## MCP-Imported Skills

Some plugin ecosystems import skills from an implementation endpoint during
submission or review.

When a skill is imported from MCP, implementations SHOULD treat the imported
skill as a versioned snapshot. After changing the skill, the implementation
SHOULD expose an updated skill version and package maintainers SHOULD rescan or
resubmit the plugin according to host policy.

An implementation conformance surface SHOULD expose the ACFS version, supported
profiles, and skill or packaging version when available.

## Host Instructions

An implementation exposing ACFS through MCP SHOULD provide concise server-level
instructions when the host supports them.

The first paragraph SHOULD be self-contained and state:

- The implementation stores durable ACFS records.
- Behavioral recall returns active scoped records.
- Revoked records must not guide behavior.
- Draft capabilities require explicit promotion before reuse.

## Tool Safety Metadata

When a host supports tool annotations or permission metadata, ACFS tools SHOULD
declare whether each tool is read-only, open-world, or destructive.

Recommended classifications:

| Tool | Safety class |
| --- | --- |
| `acfs.get_record` | read-only |
| `acfs.search` | read-only |
| `acfs.recall` | read-only |
| `acfs.state_capsule` | read-only |
| `acfs.conformance` | read-only |
| `acfs.write_record` | write |
| `acfs.supersede` | write/status-changing |
| `acfs.promote_capability` | write/status-changing/high-risk when executable |

Promotion, revocation reversal, deletion, redaction, authority broadening, and
scope broadening SHOULD require stronger authorization than ordinary record
writes.

## Test Cases

ACFS packages SHOULD include representative positive and negative tests for
agent activation and safety.

Positive tests SHOULD cover:

- Recalling workspace context at task start.
- Writing a durable decision.
- Writing a handoff at task end.
- Drafting a capability after repeated behavior.
- Promoting a capability only through an authorized path.

Negative tests SHOULD cover:

- Avoiding activation for unrelated memory or note-taking tasks.
- Refusing to use revoked records as behavioral guidance.
- Refusing to execute or rely on draft executable capabilities.
- Avoiding records outside the requested scope.
- Handling missing or unavailable ACFS tools without inventing records.

## Requirements

ACFS packages:

- SHOULD distinguish skills from live storage.
- SHOULD keep main skill instructions focused and move detailed references out
  of the main skill file.
- SHOULD include positive and negative activation tests.
- SHOULD document whether the package is skills-only, MCP-only, or combined.
- MUST NOT allow packaging, imported skills, or tool metadata to bypass ACFS
  status, scope, promotion, authorization, or revocation rules.
