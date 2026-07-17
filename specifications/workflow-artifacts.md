# Workflow Artifacts

Workflow artifacts define an optional ACFS extension for representing
addressable, executable procedure bodies without making the projection or
runtime surface the source of truth.

This extension is named `acfs.workflow.v1`.

## Purpose

ACFS already defines `procedure` Capability Records. A workflow is a procedure
whose steps reference other addressable actions, procedures, skills, tools, or
runtime operations.

Small workflows MAY be represented directly in a Capability Record's metadata.
Larger workflows SHOULD be stored as workflow artifacts and referenced by an
ACFS Capability Record.

The Capability Record remains the governed source of truth for lifecycle, scope,
authority, risk, provenance, retrieval, and projection eligibility. The workflow
artifact contains the structured workflow body used by a compatible runtime.

## Workflow Record

A workflow Capability Record MUST use `type=procedure`.

A workflow record that requires this extension SHOULD declare it in metadata:

```json
{
  "metadata": {
    "acfs_version": "0.1",
    "extensions": ["acfs.workflow.v1"],
    "workflow_schema": "acfs.workflow.v1",
    "workflow_id": "example.workflow",
    "workflow_ref": "flowos://workspace/workflow/example.workflow"
  }
}
```

Implementations MAY use implementation-native fields such as `backend` metadata
when documented. Implementation-specific metadata MUST NOT bypass ACFS
lifecycle, scope, authority, risk, retrieval, or revocation rules.

## Workflow Artifact

A workflow artifact using this extension MUST be a structured object with these
fields:

```yaml
schema: acfs.workflow.v1
id: example.workflow
version: 1
title: Example workflow
steps:
  - id: first-step
    action_id: example.action
```

The artifact MAY include:

```yaml
description: Human-readable purpose.
inputs: {}
outputs: {}
metadata: {}
```

Each step MUST include:

- `id`: stable step identifier within the workflow.
- `action_id`: addressable action, procedure, skill, or operation identifier
  understood by the runtime.

Each step MAY include:

- `input`: static input for the step.
- `input_mode`: one of `merge`, `workflow`, or `static`.
- `stop_on_failure`: boolean, defaulting to true.

When `input_mode=merge`, workflow input and step input are combined, with step
input taking precedence. When `input_mode=workflow`, only workflow input is
passed. When `input_mode=static`, only step input is passed.

## Future Fields

Implementations MAY add namespaced or documented fields for:

- conditions
- branches
- retries
- timeouts
- approval gates
- rollback behavior
- output mapping

Consumers that do not understand a field required for safe execution SHOULD NOT
use the workflow artifact for behavioral guidance.

## Relations

The workflow Capability Record SHOULD use relations to preserve graph structure:

- `depends_on` SHOULD include required child action records, policy records, and
  the workflow artifact record when one exists.
- `derived_from` SHOULD include design notes, prior versions, run evidence, or
  standards used to form the workflow.
- `supersedes` SHOULD link older workflow records replaced by a new version.

Workflow run evidence SHOULD use:

- `evidence_for` to point at the workflow Capability Record.
- `derived_from` to point at child step evidence records.

## Projection

Workflow artifacts MAY be projected through MCP, HTTP APIs, files, local user
interfaces, or other surfaces.

Projected workflow artifacts MUST remain traceable to their governing
Capability Record when used for behavioral guidance.

Revoked workflow records MUST NOT be projected as behavioral guidance. Deprecated
or superseded workflow records SHOULD NOT be used for new execution unless
explicitly requested for audit or migration.

## Requirements

ACFS-compatible implementations that support `acfs.workflow.v1`:

- MUST treat the workflow Capability Record as the governed source of truth.
- MUST preserve required ACFS record fields.
- MUST preserve workflow artifact identifiers and step identifiers.
- MUST reject or quarantine workflow artifacts with missing required step fields.
- MUST NOT execute a workflow outside its declared scope or authority boundary.
- SHOULD record child step evidence when a workflow runs.
- SHOULD record parent workflow evidence linked to child evidence with
  `derived_from`.
- SHOULD reject recursive workflow/action chains.
