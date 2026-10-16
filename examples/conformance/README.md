# Isolated Conformance Cases

These fixtures are not the cross-agent demonstration for #7. Run them using
[Conformance Validation](../../specifications/validation.md).

`cases.json` is a test manifest, not an ACFS exchange envelope. `defaults` holds
a complete base-valid record and synthetic context. Each case replaces only
the named top-level `record` or `context` members (no recursive merge); other
case members supply local related records, external-resource stand-ins, or
previously verified cached evidence. `expected` is checked against the fixture
helper's computed outcome, not used as a policy input.

## Example Mapping

`https://example.org/acfs/test-evidence-v1` is an example-only format identifier,
not a network service or a mandatory ACFS event schema. Its one-decision payload
maps lifecycle meanings as follows:

| Meaning | Example payload key |
| --- | --- |
| Affected record and contributor | `record`, `contributor` |
| Applying actor | `actor` |
| Reviewer or authorizing policy | `reviewer` or `policy`; policy values identify the retained revision (`@1`) |
| Applicable authority | `authority` |
| Effective RFC 3339 instant | `at` |
| Initial activation and resulting status | `from: null` (no prior status), `to: "active"` |
| Affected scope and reason | `scope`, `reason` |

Embedded locators contain this payload directly; related-record locators point
to a supplied base-valid evidence record with `metadata.test_evidence`; external
URI locators resolve only through the manifest's `resources` map. Unresolved
references simulate inaccessible evidence. Other formats are unsupported by
this example helper. A deniable transition or a non-initial history is not
interpreted as an initial activation approval. General mappings must document
all decision types they represent; this fixture mapping deliberately covers
only initial activation.

The context's `grants` are explicit synthetic trust assumptions supplied by the
test author independently of the record. They authorize a particular reviewer
or versioned policy for the specified authority, scope, kind, and risk. A
contributor's assertion alone does not create such a grant. The helper does not
authenticate identities, evaluate a policy language, infer risk from arbitrary
prose, or validate a general history. Real consumers must do the applicable
verification; `risk=low` is not an escape from high-risk behavior constraints.

`context.cache` likewise represents an already established synthetic offline
permission with a scope/kind/risk boundary and bounded time window. The helper
checks that window and verification triggers before using `cached_evidence`;
it does not create authorization from those asserted values. Known withdrawal,
expiry, uncertain validity, reconnection, and explicit policy verification demand
prevent continued offline use. It does not simulate a distributed system.

## Example Custom Extension

`example.procedure.v1` refines a Core `capability` into a procedure and adds
custom `reviewed_by` edges within its metadata payload. Edges point from the
procedure to a reviewer identifier and do not certify the reviewer's authority.
The payload is declared required because it changes interpretation. It uses
ACFS-Records and the unchanged lifecycle semantics; it does not require a
runtime. Its constraints are in the [example schema](../extensions/procedure.schema.json).
A supported consumer validates base plus extension, while an unsupported
consumer must withhold guidance requiring that interpretation. The example
schema is illustrative and not another ACFS profile or Core schema.
