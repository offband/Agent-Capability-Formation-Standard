# Capability Formation

Capability formation is the process by which durable records produced through agentic work become reusable future capability.

ACFS does not assume that every record is itself a capability. An observation, correction, run result, or evidence record may only become useful when it is linked to other records, reviewed within a scope, and promoted into a procedure, skill, policy, or other reusable form.

## Purpose

Agentic systems often repeat useful work without retaining the structure that made the work successful. ACFS defines formation so that useful agent behavior can be preserved without relying on hidden chat history, unstructured memory, or one-off context reconstruction.

Capability formation allows systems to:

- Capture useful agent work as durable records
- Link related records into reusable patterns
- Preserve evidence and provenance during promotion
- Review records before they influence future behavior
- Revise, supersede, or revoke capabilities as conditions change

## Formation Inputs

A Capability Record may contribute to formation even when it is not itself a complete capability.

Formation inputs may include:

- **Observation**: a recorded fact, pattern, condition, or repeated behavior
- **Correction**: a recorded change to prior behavior, language, assumption, or process
- **Decision**: a recorded choice made within a defined scope
- **Procedure**: a repeatable sequence of steps
- **Skill**: a reusable behavior or operational pattern
- **Policy**: a rule that constrains future behavior
- **Run result**: the outcome of a completed agentic action
- **Evidence**: support for or against another record
- **Deprecation**: a record indicating that another record should no longer guide new work

These record types are not required to follow a single linear path. A policy may be formed from evidence and decisions. A skill may be formed from repeated procedures. A correction may supersede a procedure. A run result may support or contradict an existing skill.

## Formation Path

Implementations MAY promote related records through formation paths such as:

	```
    Observation
      -> Correction
      -> Procedure
      -> Skill
      -> Policy
	```

This path is illustrative, not mandatory. Capability formation is not required to be linear. Implementations MAY form capabilities from any supported record type when provenance, scope, authority, lifecycle state, and evidence requirements are preserved.
