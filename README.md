# Agent Capability Formation Standard

The Agent Capability Formation Standard (ACFS) defines how agentic systems preserve, govern, and reuse durable records that allow agents to develop knowledge, refine behavior, and form reusable abilities over time.

ACFS is concerned with durable state produced through agentic work. This state may include observations, corrections, decisions, procedures, skills, policies, run evidence, and other records that allow future agents and adjacent systems to build on prior work rather than reconstructing behavior from context alone.

ACFS does not define how agents interact with external systems. It defines how agentic systems retain, govern, revise, and reuse contributed knowledge, behavior, and abilities over time.

## Requirement Language

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “NOT RECOMMENDED”, “MAY”, and “OPTIONAL” in ACFS documents are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals.

## Overview

Agentic systems do not only consume context or call external tools. Over time, they produce observations, corrections, procedures, policies, skills, evidence, and other records that may influence future behavior.

Without a shared structure for retaining and governing these records, each agent, host, or tool must reconstruct useful behavior from isolated context. ACFS defines a standard for preserving agent-contributed state so future systems can evaluate, retrieve, revise, and reuse it.

ACFS is not a storage engine, memory product, agent framework, or tool-calling protocol. It defines the lifecycle and governance model for agent-contributed state as it becomes future capability.

## Basic Concepts

ACFS defines state management between the following roles:

- **Contributor**: an agent, user, tool, service, or other system that submits a capability record.
- **Capability Store**: a system that receives capability records and is responsible for validation, indexing, persistence, retrieval, and lifecycle state.
- **Reviewer**: a user, policy engine, trusted agent, or system process that evaluates capability records and changes their lifecycle state.
- **Consumer**: an agent, host, tool, service, or other system that retrieves capability records for future use.
- **Authority**: the person, organization, policy boundary, or system responsible for determining trust within a scope.

A single implementation may combine multiple roles, but ACFS treats these responsibilities as distinct concepts.

## Capability Records

A Capability Record is the core primitive of ACFS. It is a durable, typed object submitted into an ACFS-compatible system so that agentic work can be retained, evaluated, retrieved, and revised over time.

A Capability Record is not always a complete capability. It is a durable record that may contribute to future knowledge, behavior, policy, procedure, or reusable ability.

Capability Records may include, but are not limited to:

- Observations
- Corrections
- Decisions
- Procedures
- Skills
- Policies
- Run results
- Evidence
- Deprecations

Each Capability Record MUST have a stable identifier, a record type, a lifecycle state, scope, authority, provenance metadata, and relationship metadata.

A Capability Record MUST define the scope in which it may influence future behavior. Consumers MUST NOT apply a record outside its declared scope unless an authorized reviewer or policy explicitly broadens that scope.

## Capability Formation

ACFS treats durable records as inputs to capability formation. Implementations MAY promote related records through formation paths such as:

- Observation
- Correction
- Procedure
- Skill
- Policy

Promotion MUST preserve provenance and SHOULD retain links to supporting evidence. A promoted record MUST NOT erase the source records that justified it.

## Lifecycle

Capability Records move through explicit lifecycle states. Lifecycle state determines whether a record may be retrieved, trusted, applied, ignored, corrected, deprecated, superseded, or revoked.

Initial lifecycle states are:

- **Submitted**: the record has been received but has not yet been validated.
- **Validated**: the record satisfies the structural requirements of the standard.
- **Rejected**: the record is structurally valid but has not been accepted for future use.
- **Active**: the record has been accepted for use within its defined scope.
- **Superseded**: the record has been replaced by a newer or more authoritative record.
- **Deprecated**: the record remains available for historical or audit purposes but SHOULD NOT be used for new agent work.
- **Revoked**: the record has been withdrawn from use and MUST NOT guide future agent behavior.

Validation does not imply that a record is true, trusted, or approved for future use.

## Retrieval

By default, Consumers SHOULD retrieve Active records within the requested scope.

Deprecated and Superseded records MAY be returned when explicitly requested. Revoked records MUST NOT be returned for behavioral guidance, but MAY be returned for audit purposes.

Retrieval SHOULD support filtering by type, scope, lifecycle state, authority, provenance, recency, and relation.

## Relationship to MCP

ACFS is not a replacement for MCP.

MCP defines how applications expose context, tools, prompts, and related capabilities to AI systems. ACFS defines how durable records from agents and related systems are written, classified, governed, revised, and made available for future use.

An ACFS implementation MAY expose ACFS operations through MCP tools, resources, or prompts. However, ACFS lifecycle state, authority, scope, and revocation rules remain binding regardless of transport.

## Security and Trust

Durable agent-contributed records can influence future agent behavior. ACFS implementations MUST treat record writing, promotion, retrieval, correction, and deletion as security-sensitive operations.

ACFS records are not passive storage. A Capability Record may affect what a future agent believes, what procedure it follows, what skill it loads, what policy it respects, or what ability it attempts to use.

ACFS implementations SHOULD preserve provenance, enforce scope boundaries, support revocation, and apply least privilege to record operations.

Implementations SHOULD classify records by risk. Observations and evidence are generally lower risk. Decisions, corrections, and procedures may affect behavior and require review. Skills, policies, authority changes, triggers, and records that can cause future actions are high risk and SHOULD require review before becoming Active.

Implementations SHOULD consider risks such as unauthorized writes, contribution poisoning, unsafe promotion, stale records, sensitive data persistence, unclear authority, and cross-agent propagation of unreviewed records.

## Implementation

ACFS does not require a specific runtime, transport, storage engine, or agent framework.

An ACFS-compatible implementation preserves the standard requirements for Capability Records, lifecycle state, provenance, scope, retrieval, correction, and revocation.

Implementations MAY use files, databases, graph stores, object storage, content-addressed storage, or other persistence mechanisms.

Future versions may define standard transports, schemas, compatibility profiles, and reference implementation behavior.
