# Implementation Boundary

ACFS is a portable standard for addressable and recallable agent memory and
capability. It is not an application framework, workflow engine, storage
product, agent runtime, user interface, billing system, or orchestration layer.

An ACFS-compatible implementation may be simple or full-featured. The standard
only requires that portable durable records and capability guidance preserve the
ACFS rules for identity, kind, status, scope, provenance, relations, recall,
promotion, supersession, and revocation.

## Core Standard Concepts

ACFS Core centers on four concepts:

- **Record**: a durable scoped object that can be recalled, audited, revised,
  superseded, or revoked.
- **Capability**: a record that describes reusable behavior, procedure, skill,
  prompt, or runtime reference without itself granting execution permission.
- **Recall and state capsules**: retrieval and compact briefings intended to
  guide future behavior, constrained by
  status, scope, provenance, authority, risk, and revocation.

Implementations SHOULD keep these concepts visible at the boundary where data is
exported, imported, projected, recalled, or shared with another agent system.

## Runtime Concepts

Runtimes MAY define richer implementation concepts such as:

- artifacts
- actions
- runs
- tasks
- triggers
- packages
- user interface state
- local storage indexes
- tool invocation
- authentication
- hosting
- billing or entitlement state
- agent session state

These concepts are not part of the ACFS base profile unless the implementation
maps them to ACFS records, relations, metadata, or a documented extension.

Runtime concepts MUST NOT bypass ACFS status, scope, provenance, promotion,
recall, supersession, or revocation rules when they are used as behavioral
guidance.

## Common Mappings

The following mappings are non-core guidance for implementations that expose
richer runtime objects while preserving ACFS portability:

| Runtime object | ACFS boundary mapping |
| --- | --- |
| Artifact | A record with a URI, content hash, summary, and relation to the artifact, or a referenced object governed by an ACFS record. |
| Action | A capability detail, workflow step, or implementation-specific operation referenced from a capability record. |
| Run | An evidence record related to the capability, action, input record, and output artifacts used during execution. |
| Trigger | A capability or policy detail requiring explicit review before it can become active behavioral guidance. |
| Package | An implementation distribution object whose behavioral contents remain governed by ACFS records. |

Small implementation details MAY live in record metadata. Larger executable
procedure bodies belong to implementation-specific systems or documented
non-core extensions while keeping the ACFS record as the governed source of
truth.

## Compatibility Rule

An implementation does not become incompatible merely because it has richer
runtime behavior than ACFS defines.

It becomes incompatible when portable or behavioral guidance cannot be expressed
as ACFS records, when recall ignores ACFS lifecycle rules, when revoked records
guide behavior, when scope is bypassed, or when executable capabilities become
active without an authorized promotion path.

## Extension Rule

If a runtime concept becomes necessary for portable interchange between ACFS
implementations, define it as a documented ACFS extension instead of relying on
an undocumented implementation convention.

Extensions SHOULD describe:

- the implementation problem they solve
- the ACFS profiles they require
- the record fields, metadata, relation types, or artifacts they add
- how behavioral recall handles unsupported consumers
- how the extension preserves status, scope, provenance, authority, risk, and
  revocation

## Refinement Rule

ACFS should be distilled without breaking existing useful implementations.

Changes to base kinds, base statuses, required fields, recall behavior, or
capability promotion rules SHOULD include migration guidance. Existing records
that already preserve ACFS-required fields SHOULD remain importable unless they
violate safety or revocation rules.

## Requirements

ACFS-compatible implementations:

- MUST preserve ACFS-required fields at portable boundaries.
- MUST prevent revoked records from guiding behavior.
- MUST keep behavioral recall constrained by status and scope.
- MUST NOT let runtime objects bypass promotion or revocation rules.
- SHOULD map artifacts, actions, runs, triggers, and packages to ACFS records,
  relations, metadata, or documented extensions when portability matters.
- SHOULD document runtime concepts that are outside the ACFS base profile.
