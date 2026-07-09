# Scope and Authority

Scope and Authority define where a Capability Record may apply and who is responsible for trust decisions within that boundary.

ACFS treats scope as security-critical. A record that is useful in one project, user context, repository, organization, node, workflow, or time window may be unsafe or incorrect in another.

## Scope

Scope defines the boundary in which a Capability Record may influence future behavior.

A Capability Record MUST declare a scope.

Examples of scope include:

- User
- Project
- Repository
- Organization
- Workflow
- Tool
- Node
- Domain
- Time window

Implementations MAY support additional scope types.

## Scope Boundaries

Consumers MUST NOT apply a Capability Record outside its declared scope unless an authorized Reviewer or policy explicitly broadens that scope.

A record declared for one scope does not automatically apply to parent, child, sibling, or adjacent scopes.

For example, a procedure accepted for one repository does not automatically apply to every repository in the same organization. A policy accepted for one user does not automatically apply to all users.

## Authority

Authority identifies the person, organization, policy boundary, or system responsible for trust decisions within a scope.

A Capability Record MUST identify an Authority.

Authority determines who may:

- Accept or reject records
- Promote records to Active
- Broaden or narrow scope
- Supersede, deprecate, or revoke records
- Define review requirements
- Resolve conflicts between records

## Reviewers

A Reviewer acts on behalf of an Authority.

A Reviewer may be a user, policy engine, trusted agent, service, or system process.

Implementations MUST distinguish between the Contributor that submits a record and the Authority or Reviewer that accepts it for use.

A Contributor is not automatically authorized to promote its own record.

## Scope Changes

Changing scope is a security-sensitive operation.

A scope change may cause a record to influence more systems, users, tools, or future behavior than originally intended.

Implementations SHOULD preserve scope change history, including:

- Prior scope
- New scope
- Actor responsible for the change
- Timestamp
- Reason

A record’s scope MUST NOT be broadened without authorization from the relevant Authority.

## Authority Conflicts

Records from different Authorities may conflict.

When records conflict, Consumers SHOULD prefer records from the Authority responsible for the requested scope.

If no clear Authority applies, Consumers SHOULD reduce confidence, request review, or avoid using the conflicting records for behavioral guidance.

A record from one Authority MUST NOT override a record from another Authority unless policy explicitly permits it.

## Nested Scopes

Implementations MAY support nested scopes.

Examples:

- Organization → project → repository
- User → workflow → task
- Domain → service → tool
- Node fabric → node → service

Nested scopes MUST NOT imply automatic inheritance unless the implementation defines inheritance rules.

If inheritance is supported, implementations SHOULD document:

- Which scopes inherit from parent scopes
- Which record types may inherit
- Which lifecycle states may inherit
- Which Authorities may override inherited records
- How conflicts are resolved

## Time-Bound Scope

Some records may only apply during a defined time window.

A time-bound record SHOULD declare when it becomes valid and when it expires.

Expired records SHOULD NOT guide future behavior unless explicitly requested for audit or historical purposes.

Time-bound scope is especially important for temporary decisions, incident response procedures, credentials, migration windows, experiments, and environment-specific work.

## Requirements

ACFS-compatible implementations that support scope and authority:

- MUST require scope on each Capability Record
- MUST require authority on each Capability Record
- MUST NOT apply records outside their declared scope without authorization
- SHOULD preserve scope and authority change history
- SHOULD distinguish Contributors from Reviewers and Authorities
- SHOULD document inheritance behavior when nested scopes are supported
- MUST NOT allow scope or authority rules to bypass lifecycle or revocation rules
