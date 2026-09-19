# Companion statement recovery audit

This review-only pass runs after the safe structural split.

It takes every row in `POST_SPLIT_LINK_REVIEW.tsv`, collapses duplicate solution
copies by semantic solution unit, and searches the entire imported statement
corpus for plausible companion statements.

Candidate statements come from:

- `STRUCTURAL_REBUILD_CANDIDATES_V3.tsv`;
- the active post-split `PROBLEM_LEDGER.tsv`.

Duplicate statement copies are collapsed by `statement_hash`.

Ranking evidence combines:

- TF-IDF lexical overlap between solution and statement;
- mathematical-token overlap;
- exact source problem number;
- filename/source-family similarity;
- broad subject-family consistency.

Problem numbering is intentionally a minority signal so that a numerically
matching but mathematically unrelated exercise does not win.

Outputs:

- `COMPANION_STATEMENT_CANDIDATE_RANKINGS.tsv`
- `COMPANION_STATEMENT_RECOVERY_DECISIONS.tsv`
- `COMPANION_STATEMENT_RECOVERY_PACKET.md`
- `COMPANION_STATEMENT_RECOVERY_SUMMARY.md`

No links are changed.
