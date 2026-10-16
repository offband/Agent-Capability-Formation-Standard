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

Both JSON schemas and all JSON examples are unchanged. The v0.2.1 schema
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

The v0.2.1 record shape, four statuses, seven kinds, schemas, and JSON examples
remain unchanged. Stronger governance evidence can use existing metadata,
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

## Deferred Schema and Conformance Questions — Issue #6

- Records/relations prose allows documented additional kinds and relation types,
  but the current schema rejects them. Decide extension validation and
  advertisement rules without silently widening the base enums. Additional
  properties do not make enum extensions schema-valid.
- Decide how governance evidence and mandatory-extension declarations are
  validated. Issue #5 defines the evidence meanings, not a canonical encoding.
  Current metadata is open-ended; schema validity cannot certify authorization
  or safe behavioral use. Decide interoperable discovery/reference handling,
  timestamp representation, and policy identification across implementations,
  including how to retain the policy basis in effect at decision time.
- Define conformance checks for missing or inaccessible governance evidence,
  denied activation, initial active creation with no prior status, scope or
  authority changes with unchanged status, and freshly authorized reactivation.
  Do not treat all structurally valid active records as approved.
- Clarify preservation of external history references and their authorization
  basis during exchange, including unavailable evidence and stale copies.
  Issue #5 specifies safe-use constraints, not a synchronization or distributed
  freshness protocol; do not imply that a schema proves current eligibility.
- Separate structural fixture validation from behavioral conformance checks.
  `examples/invalid/revoked-behavioral-retrieval.json` is a legacy-shaped
  retrieval envelope demonstrating unsafe behavior, not a v0.2.1 record-schema
  negative test. It needs a semantic check, not merely a schema failure.
- Define legacy adaptation more precisely: the legacy schema uses different
  kinds, lifecycle, provenance, and relation shapes; its `type` to `kind` table
  is not a complete conversion algorithm. Legacy validation is separate from
  v0.2.1 validation and is optional.
- Review relation direction in the promoted capability's `evidence_for` edge
  and the revoked example's `supersedes` edge before using those fixtures as
  semantic conformance evidence. Their structural validity is unchanged.
- Decide whether portable exchange should eventually have stronger guarantees;
  this pass retains ACFS-Portable's existing SHOULD requirements and does not
  create an exchange protocol or new profile.

## Deferred Demonstration — Issue #7

The README record and conformance's file-store illustration show the minimum
portable contract without a runtime dependency. The complete cross-agent
capture, approval, discovery, reuse, and correction scenario remains #7, after
#6 aligns schema and conformance with the governance meanings established in
#5. No new lifecycle fixture or runtime demonstration is introduced here.
