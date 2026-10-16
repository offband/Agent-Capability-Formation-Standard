# Core Consistency Audit (Issue #4)

This is an informative audit for [#4](https://github.com/offband/Agent-Capability-Formation-Standard/issues/4)
under [#3](https://github.com/offband/Agent-Capability-Formation-Standard/issues/3).
[Conformance](conformance.md) defines the Core contract. This audit adds no
fields, kinds, statuses, profiles, or schema requirements.

## Resolved Inconsistencies

| Before | Clarification |
| --- | --- |
| README and conformance overview called records, scoped recall, state capsules, and capability lifecycle Core, while named profiles separated them. | Core is ACFS-Records. Retrieval and capability formation services are optional; base status meanings and safe-use constraints still apply. |
| Implementation boundary described a broader Core and implied that mapping a runtime concept into a record could make it Core. | The governed contextual record is foundational. Representing runtime data in a record does not require the associated runtime service. |
| Architecture implied indexing and recall were base services, while structural validation was only MAY. | Service architecture is illustrative; Core requires structural validation and record semantics, not indexes or retrieval APIs. |
| Conformance required import/export while records only recommended it and ACFS-Portable described exchange separately. | Import/export remains recommended in Core; ACFS-Portable adds exchange-specific expectations. No existing exchange functionality is removed. |
| Versioning allowed missing version metadata; records and the schema required it. | v0.2.1 records require `metadata.acfs_version: "v0.2.1"`. |
| The optional-field illustration showed empty metadata, and versioning omitted ACFS-Retrieval from its profile list. | Metadata is identified as required; ACFS-Retrieval is listed as optional. |
| MCP's recommended tool list could imply mandatory capability and retrieval services. | Binding recommendations apply to supported features and do not require all optional profiles. |

## Existing Schema Behavior and Compatibility

At the #4/#5 boundary both schemas and JSON examples were unchanged. Issue #6
adds validation fixtures and corrects two misleading example edges; the base
schema acceptance set remains unchanged. The v0.2.1 schema
requires `id`, `kind`, `status`, `scope`, `title`, `body`, `metadata`, and
`provenance`. Metadata requires the exact version string; provenance requires
`actor`, `created_at`, and `source`. Scope accepts a nonempty string or an
object with `type` and `id`. Authority, risk, relations, summaries, tags, and
time fields remain optional. The four statuses and seven kinds are unchanged.

The schema permits extra top-level and metadata properties, but enumerates
`kind`, `status`, and relation `type`. It validates shape, not authorization,
promotion evidence, scope applicability, relation resolution, or whether a
retrieval result is safe guidance. Draft and active capability examples are
both structurally valid; that does not prove an authorized transition occurred.
Timestamp `format` checks depend on validator configuration.

No wire-format or schema compatibility change is introduced. Requiring version
metadata in the versioning prose reflects the existing schema rather than a
new field. Implementations relying on that document's former MAY language may
already produce nonconforming records. Making import/export recommended rather
than mandatory relaxes an inconsistent service obligation; consumers must not
infer an exchange API solely from a Core claim. Existing broader implementations
can continue supporting their current services and declaring optional profiles.

## Governance Refinement — Issue #5

The #4 audit identified contradictory MUST/SHOULD promotion language, policy
exceptions without a shared authorization definition, optional transition
reasons, and unclear withdrawal and cache behavior. Issue #5 resolves these in
[Lifecycle](lifecycle.md), with corresponding changes in formation, scope and
authority, conformance, trust and safety, record status rules, and projection.

| Prior inconsistency | Normalized rule |
| --- | --- |
| Lifecycle allowed immediate policy activation while formation only recommended keeping capabilities draft and conformance required promotion. | All activation needs applicable policy or authorized review; explicit policy-authorized initial activation counts as the promotion decision for capabilities. No stored intermediate draft is required. |
| Promotion meant draft-to-active for records in lifecycle but only capabilities in safety text. | Promotion means draft-to-active for any record; initial activation and reactivation obey the same authorization rules. |
| High-risk capability authorization was mandatory in some documents but review only recommended elsewhere. | Explicit authorization must cover high-risk capability behavior, scope, and risk. A write permission or low-risk auto-activation rule is insufficient; human review is not universally required. |
| Contributor/reviewer identity and authority metadata could be conflated. | Submission does not grant approval authority. Self-review requires independent policy authorization. Governance evidence identifies the roles and applicable authority; Core does not acquire a mandatory authority field. |
| Governance transition history only required reasons “when available.” | Governance requires inspectable record/contributor, transition actor, reviewer or authorizing policy, applicable authority, timestamp, prior/resulting status and scope, and reason. Initial/automatic activation and scope/authority changes are included. |
| Superseded guidance was only discouraged, and cache refresh only recommended. | Known superseded or revoked records cannot be used authoritatively; policy may permit offline use of previously verified guidance within defined validity windows and risk boundaries. Verification is required on reconnection, expiry, uncertain validity, or policy demand; reactivation requires fresh authorization. Historical inspection remains possible. |

The three required edge cases are documented as semantic outcomes in
[Lifecycle](lifecycle.md#required-edge-cases): valid submission without approval
authority, low-risk policy activation, and revocation while a participant holds
a cached active copy. These are not the full cross-agent fixtures for #7.

At completion of #5 the v0.2.1 record shape, four statuses, seven kinds, schemas,
and JSON examples were unchanged. Stronger governance evidence can use existing metadata,
provenance extensions, related records, or inspectable implementation history;
there is no new mandatory event schema. Existing Core records remain valid.
Implementations claiming ACFS-Governance may need to retain more evidence than
before, especially reasons and policy bases. Implementations relying on
known superseded guidance, implicit self-approval, or cached use outside an
authorized validity window must change that behavior to meet the clarified safety contract. Structural validation
alone does not demonstrate this semantic conformance.

ACFS does not supply policy evaluation, identity verification, cache delivery,
or instantaneous revocation notifications. Implementations must document their
validity and evidence handling. Explicit policy may permit offline guidance
within a bounded validity window and risk boundaries. Consumers must verify on
reconnection, expiry, uncertain validity, or policy demand; a cache window is
not approval and cannot override known withdrawal. Disconnected consumers may
temporarily use guidance revoked elsewhere until reconnection and verification,
window expiry, or earlier knowledge of withdrawal. This consistency limitation
does not change the lifecycle states or permit knowingly using withdrawn
guidance. High-risk policy may demand continuous connectivity or immediate
revalidation; no new service, profile, or synchronization protocol is introduced.

## Schema and Evidence Interoperability — Issue #6

| Prior inconsistency or gap | Resolution |
| --- | --- |
| Custom kinds/relations allowed by prose but rejected by the schema | Keep all base enums closed. Map custom kinds to an appropriate Core kind and put custom edges in a declared namespaced payload. Validate base plus supported extension constraints. |
| Required extension handling lacked a portable declaration | Use the existing `metadata.extensions` list plus conditional `metadata.required_extensions`; require the latter to be a subset of the former. Unsupported requirements cannot guide behavior. No new required Core field or registry. |
| Governance history had meanings but no common discovery mechanism | Conditional `metadata.governance` locates embedded, related-record, or external evidence under a documented versioned mapping. Existing histories can be adapted; unsupported/inaccessible required evidence cannot imply approval. |
| A schema-valid active record could be mistaken for authorized guidance | Validation documentation and isolated cases separate base, extension, and semantic outcomes, using explicit synthetic authority inputs. |
| A revoked retrieval envelope was mixed with record-shape negatives | Validate it as a semantic negative separately from the legacy and base record schemas. |
| Two example relations implied incorrect support/replacement direction | The promoted capability uses `derived_from` for its source evidence, not a reversed `evidence_for` edge. The revoked memory no longer claims to supersede current guidance without support. |

The seven kinds, four statuses, required fields, Core contract, and #5 lifecycle
and policy-bounded offline decisions are unchanged. Only a schema comment is
added to the base schema; required version metadata remains enforced. Existing
unknown optional metadata remains structurally acceptable. Previously native
custom enum values require mapping at export because they already failed base
validation. Governance exchange and conditional extension declarations may need
adapters, not migrations of every Core record. No universal evidence payload or
event schema is mandated.

[Conformance Validation](validation.md) describes the reproducible checks and
what they do not prove. [Governance Evidence Interchange](governance-evidence.md)
defines discovery, interpretation, and safe handling of required evidence.

## Remaining Demonstration and Limitations — Issue #7

The full cross-agent capture, approval, discovery, reuse, correction, and
withdrawal example remains #7. It should choose and document its actual evidence
mapping, expose complete supporting histories, and provide independent trust
inputs rather than treating a record's self-asserted authority as a grant.
The isolated initial-activation fixture mapping is not a universal event schema
or a claim of independent runtime interoperability.

Remaining implementation choices include identity and evidence authenticity,
external reference retention/access, content/revision binding, full transition
chains and conflicting decisions, and policy-specific cache validity. Preserve
the policy basis in effect at decision time when designing that demonstration.
Legacy import still needs an explicit semantic adapter: `type` to `kind` is not
literal enum substitution. ACFS-Portable's SHOULD requirements do not create a
shared exchange protocol. No runtime, synchronization protocol, or full
cross-agent demonstration is implemented in this pass.
