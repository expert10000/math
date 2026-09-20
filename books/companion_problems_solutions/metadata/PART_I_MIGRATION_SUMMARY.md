# Companion Part I migration — Volume I problem corpus

This pass materializes the Volume I semantic atlas rows as reader-facing Companion problems.
Source provenance, classification confidence, and alternate solution variants remain in the migration ledger rather than the mathematical prose.

## Coverage

- Part I atlas units: **123**
- Reader-facing problems migrated: **123**
- Editorial holds with no safely recoverable statement: **0**
- Problems with a migrated primary solution: **85**
- Atlas rows marked as having a reconciled solution: **86**
- Expected solutions not safely recovered in this pass: **1**
- Problems with multiple distinct solution variants retained in provenance: **12**
- Atlas placement-review rows included in Part I: **13**

## Reader-facing thematic sections

- Vector Spaces (I/01--I/06): **39** problems
- Matrices and Operators (I/07--I/12): **73** problems
- Euclidean and Hilbert-Space Geometry (I/13--I/18): **11** problems

## Visual layer

No new plots or diagrams are introduced in this migration commit.
Existing/source visual requirements remain recorded in `COMPANION_PROBLEM_ATLAS.tsv` and `PART_I_MIGRATION.tsv` for the later visual-enrichment pass.

## Integrity rule

Every Part I atlas unit has exactly one migration-ledger row and therefore one explicit disposition.
No missing statement or solution is fabricated.
