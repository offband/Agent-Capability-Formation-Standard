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

## Deferred Governance Questions — Issue #5

- Normalize the strength and conditions of promotion language: README and
  ACFS-Capabilities require explicit promotion for executable or behavior-shaping
  capability guidance, while formation and lifecycle also use SHOULD wording.
  Lifecycle permits explicit policy for immediate activation. Clarify what
  constitutes policy authorization and what evidence is needed, without a new
  state or mandatory governance backend. This pass preserves the existing
  safety constraints and does not define a new transition protocol.
- Clarify recording versus proposing versus approving for non-capability kinds.
  `active` expresses eligibility within scope, not universal truth, execution
  permission, or proof of review. Low-risk automatic activation remains allowed
  by existing policy semantics; no universal human-review requirement is added.
- Reconcile optional authority/risk fields with governance and high-risk policy
  obligations. Decide when supplied authority and reviewer evidence are
  sufficient; do not infer an organizational hierarchy from Core.
- Normalize promotion terminology (all draft-to-active records in lifecycle,
  capability-focused wording elsewhere), revocation reversal, and replacement
  handling. Retain the four current statuses until reviewed.
- Clarify the distinction between non-active explanatory/audit context and
  behavioral guidance. Revoked records remain prohibited as guidance in every
  mode, regardless of wording about authorized non-active inspection.

## Deferred Schema and Conformance Questions — Issue #6

- Records/relations prose allows documented additional kinds and relation types,
  but the current schema rejects them. Decide extension validation and
  advertisement rules without silently widening the base enums. Additional
  properties do not make enum extensions schema-valid.
- Decide how governance evidence and mandatory-extension declarations are
  validated. Current metadata is open-ended; schema validity cannot certify
  these semantics or safe behavioral use.
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
#5 and #6 resolve governance evidence and schema expectations. No new lifecycle
fixture or runtime demonstration is introduced here.
