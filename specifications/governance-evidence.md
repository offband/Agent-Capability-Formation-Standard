# Governance Evidence Interchange

This document defines discovery of the evidence already required by
[ACFS-Governance](lifecycle.md#transition-history). ACFS Core remains
ACFS-Records. No locator, authority field, or history is required on every Core
record. Neither a locator nor an evidence payload is proof of authorization.

## Discovery at the Portable Boundary

When exchanging a record as governed guidance, ACFS-Governance implementations
MUST make its required evidence discoverable to authorized consumers. Portable
exports MUST include the following conditional convention in existing metadata,
or a documented adapter MUST produce it before the consumer interprets the
record as governed guidance:

```json
{
  "metadata": {
    "governance": {
      "format": "https://example.org/governance/evidence-v1",
      "evidence": [{"embedded": {"example": "format-specific evidence"}}]
    }
  }
}
```

This fragment is a locator, not a complete record or a universal event schema.
`format` MUST be a nonempty, version-specific identifier for a documented
mapping from the evidence representation to the lifecycle evidence meanings.
It need not be a retrievable URL. `evidence` MUST be a nonempty array; each entry
MUST identify exactly one of these locations:

| Locator | Meaning |
| --- | --- |
| `embedded` | An embedded evidence payload interpreted by the named format. |
| `record` | A nonempty ACFS record identifier resolved through a supplied exchange bundle or a documented implementation lookup. The format specifies where the evidence resides in that record. |
| `uri` | A nonempty external reference, including a fragment when needed, resolved under the consumer's access and trust policy. The format specifies the referenced representation. |

Multiple entries MAY jointly supply a history or its supporting evidence; the
mapping MUST explain how to combine them and identify the decision governing
the particular record content, status, scope, and relevant constraints. All
required parts must be available (including previously verified cached evidence
when policy permits), not merely one successful locator. Base
`evidence_for` relations remain directional support edges and MUST NOT be
assumed to be a complete governance history or an authority grant. Related
records can be located explicitly without adding a relation type.

## Interpretation and Verification

The format documentation MUST map the lifecycle evidence meanings to payload
locations, distinguish contribution, reviewer, applying actor, authorizing
policy and applicable authority, and explain initial creation (no prior status),
denials, and scope/authority changes when represented. It MUST define timestamp
syntax and time zone interpretation; portable mappings SHOULD use RFC 3339
instants. Policy evidence MUST identify the rule/decision and policy basis in
effect at the decision time, through an immutable revision, retained snapshot,
or equivalent inspectable reference. A mutable policy name alone is insufficient.

Implementations MUST expose or exchange this mapping with their conformance
information or evidence package; no central registry or shared runtime is
required. Consumers MUST support the declared mapping or explicitly withhold
semantic interpretation. They MUST verify that evidence applies to the supplied
record and decision and that the reviewer or policy is authorized for the scope
under applicable trust policy. Names, signatures, URIs, and `status=active`
alone do not establish that authorization. ACFS mandates no identity provider,
policy language, transport, signature mechanism, or universal event encoding.

External references MUST NOT cause automatic execution or privileged retrieval.
Implementations MUST document resolution/access requirements and preserve the
locator, format identifier, and required policy/history references during
exchange unless redaction policy prohibits disclosure. If evidence cannot be
shared, the record can still be retained as data without claiming verified
governed behavioral eligibility.

## Missing, Inaccessible, or Unsupported Evidence

Consumers MUST distinguish structural validity from verified governance.
Missing or malformed discovery information, an unsupported format, inaccessible
required evidence, incomplete transition evidence, mismatched record/scope,
denied approval, or unverified applicable authority MUST NOT be treated as
successful authorization. Consumers MUST withhold governed guidance until the
required interpretation and verification succeed, subject to the previously
verified cache allowance below, and MUST expose a reason to
the authorized caller. They MAY reject, quarantine, or retain it for audit;
these are handling choices, not new lifecycle states. They MUST NOT rewrite an
active record to pretend that a verified transition occurred.

Previously verified evidence MAY be used from cache under the existing
[policy-bounded offline-use rules](projection.md#caching-and-indexing). Temporary
source inaccessibility does not invalidate an otherwise established policy
window. When validity cannot be established, the window expires, reconnection
occurs, or policy requires verification, further use requires verification as
specified there. Known withdrawal always prohibits authoritative use. Discovery
and exchange do not renew an offline window or authorize reactivation.

## Compatibility

The base record schema remains open to these metadata entries and is unchanged
in its acceptance behavior. Existing local governance histories MAY remain in
their current formats; adapters can expose the locator and mapping on exchange.
Existing records lacking the locator remain structurally valid, but cannot by
that fact alone establish portable ACFS-Governance conformance. Existing Core
implementations do not acquire a history service requirement.
