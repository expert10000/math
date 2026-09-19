# Imported problem reconciliation — duplicates and solutions

> This pass changes only import/provenance inventory data. Canonical book content and semantic Volume/chapter placement remain untouched.

## Exact duplicate collapse

- Statement-bearing source rows: **6127**
- Unique statement hashes / semantic units: **2963**
- `SEMANTIC_PROBLEM_UNITS.tsv` rows ready for classification: **2963**
- Exact duplicate groups: **2092**
- Source rows participating in duplicate groups: **5256**
- Source rows deleted: **0** (collapse is semantic/provenance-only)

## Solution reconciliation

- Solution/hint blocks: **1778**
- Existing structural links retained: **1595**
- New conservative companion links applied: **4**
- Remaining unresolved solution/hint blocks: **179**
- Ambiguous candidate sets left for review: **171**
- Numbering-mismatch file pairs detected: **1**

## Recomputed ledger

- Rows with directly linked local/companion solution: **1332**
- Rows gaining solution availability only through exact-duplicate propagation: **27**
- Rows with any reconciled solution availability: **1359**
- Rows still without reconciled solution availability: **4768**

## Detached solution headings

- Heading markers: **8**
- Resolved: **0**
- Partial: **0**
- Unresolved: **8**

## Next pass

1. Review any remaining explicit orphan/numbering cases.
2. Review LOW-confidence `PROOF_EXERCISE_CANDIDATE` rows.
3. Classify mathematical subject from actual statement content.
4. Assign Volume/chapter/section.
5. Compare semantic units against the canonical problem index.
