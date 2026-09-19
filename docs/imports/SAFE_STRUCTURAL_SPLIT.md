# Safe structural split

This pass supersedes only the 75 current ledger rows classified
`SAFE_SPLIT_PREVIEW` by the v3 structural-rebuild quality audit.

The current reviewed snapshot is locked to:

- 75 safe parent/container rows;
- 667 replacement child problem rows.

Default mode is a dry run. It creates:

- `SAFE_STRUCTURAL_SPLIT_PLAN.tsv`;
- a shadow repaired `PROBLEM_LEDGER`;
- shadow problem/solution links;
- `POST_SPLIT_LINK_REVIEW.tsv`;
- a superseded-row archive preview;
- shadow semantic units and orphan ledgers.

Existing direct solution links are remapped only by:

1. unique source-problem-number match; or
2. unique same-file nearest-preceding child.

If neither rule is unique, the old direct link is cleared only in the shadow
ledger and placed in `POST_SPLIT_LINK_REVIEW.tsv`.

Candidate-problem lists are also rewritten so no unresolved link continues to
refer only to a superseded parent ID.

`-Apply` freezes the pre-split master inventory files and promotes the shadow
files. It does not touch canonical book content.
