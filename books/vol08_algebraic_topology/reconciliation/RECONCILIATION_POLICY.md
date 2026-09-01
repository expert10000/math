# Volume VIII - Reconciliation Policy

The Volume VIII freeze does not accept "covered by topic" as corpus evidence.

The reconciliation pass works from `editorial/SOURCE_MIGRATION.tsv` and the
retained source files.  It enumerates concrete structured legacy instances,
assigns their canonical destination from the migration selectors, and records
an explicit evidence target.

Required dispositions are:

- legacy `problem` -> canonical labeled `Problem`;
- legacy `exercise` -> canonical `Exercise`;
- canonical Problem/Exercise -> paired `Solution`;
- theorem-like source block -> direct canonical theorem-like target or an
  explicit consolidation into a named canonical section;
- source/support visual -> unique canonical visual evidence or an explicit
  provenance-only visual disposition;
- archive duplicate/variant -> explicit provenance classification;
- canonical Problem/Exercise with no legacy source instance -> explicit
  `CANONICAL_ADDITION_NOT_LEGACY`.

`FILE_FALLBACK` is only a routing aid.  It does not count as coverage by
itself.  Any instance routed through fallback must still receive direct
instance-level evidence.

The pass also writes a SHA-256 manifest over the migration ledger, canonical
chapters, Volume VIII visual assets, and primary legacy source files actually
inspected.  Freeze verifies this manifest before building.
