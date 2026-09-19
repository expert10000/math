# Imported-problem reconciliation provenance policy

This file records the repository policy used for the one-time cleanup following the
structural/P2-P3 reconciliation.

## Canonical records

Commit artifacts that preserve information which is not safely reconstructed from a
fresh diagnostic run:

- explicit editorial decisions, overrides, exceptions, and dispositions;
- exact applied repair, closure, retention, and supersession records;
- current semantic-unit state used by later classification work;
- final structural compatibility/integrity/quality certification;
- current disposition-aware structural status and remaining actionable risks.

## Working artifacts

Do not commit generated working state once its result is represented by canonical
records. This includes SHADOW/PRE/baseline copies, previews, plans, candidate and
ranking tables, review packets, temporary queues, resegmentation/recovery/promotion
work products, and superseded phase summaries.

`PROVENANCE_CLEANUP_DECISIONS.tsv` is the authoritative path-by-path classification
for this cleanup. `REMOVE_IGNORE` paths are ignored individually rather than by broad
`*_AUDIT*`, `*_REPORT*`, or `*_SUMMARY*` patterns, so future canonical records remain
visible to Git.

This cleanup does not alter the already-valid reconciliation commit or rewrite tracked
problem/solution ledgers.
