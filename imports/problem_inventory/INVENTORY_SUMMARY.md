# Imported problem inventory — structural discovery pass

> This inventory is discovery/provenance data. It does not modify canonical book content and does not yet assert canonical placement.

## Counts

- Source TeX files scanned: **231**
- Structural problem-like detections: **5130**
- Statement-bearing ledger problems: **5120**
- Empty structural markers quarantined: **2**
- Detached solution-heading markers: **8**
- Solution/hint blocks detected: **1778**
- Exact duplicate groups: **1858**
- Orphan solution/hint blocks needing review: **209**
- Problem-like objects without a detected solution: **4001**

## By source collection

- Downloads: **2825**
- MATH-ALLS-2: **1262**
- MATH_ALLS-3: **1033**

## By detected type

- EXERCISE: **721**
- EXERCISE_ITEM: **322**
- PROBLEM: **1308**
- PROBLEM_ITEM: **1105**
- PROOF_EXERCISE_CANDIDATE: **8**
- WORKED_EXAMPLE: **1656**

## Next reconciliation pass

1. Review LOW-confidence `PROOF_EXERCISE_CANDIDATE` rows.
2. Reconcile detached solution files and numbering mismatches.
3. Classify mathematical subject from actual statement content.
4. Assign Volume/chapter/section.
5. Compare statement hashes/fingerprints against canonical problem index.
6. Replace `UNREVIEWED`/`UNCLASSIFIED` fields with explicit dispositions.
