# Companion Part IV migration — Volume IV problem corpus

This pass materializes the Volume IV semantic atlas rows as reader-facing Companion problems.
Source provenance, classification confidence, and alternate solution variants remain in the migration ledger rather than the mathematical prose.

## Coverage

- Part IV atlas units: **139**
- Reader-facing problems migrated: **139**
- Editorial holds with no safely recoverable statement: **0**
- Problems with a migrated primary solution: **39**
- Atlas rows marked as having a reconciled solution: **39**
- Expected solutions not safely recovered in this pass: **0**
- Problems with multiple distinct solution variants retained in provenance: **4**
- Atlas placement-review rows included in Part IV: **68**

## Reader-facing thematic sections

- Holomorphic Functions (IV/01--IV/06): **36** problems
- Singularities and Residues (IV/07--IV/11): **16** problems
- Global Complex Analysis (IV/12--IV/18): **17** problems
- Special Functions (IV/19--IV/21): **68** problems
- Riemann Surfaces (IV/22--IV/26): **0** problems
- Elliptic Functions (IV/27--IV/31): **2** problems

## Visual layer

- Designed Part IV TikZ figures placed automatically: **34**
- Designed manifest rows missing a staged file: **0**
- Designed manifest available: **YES**

Source-backed Part IV visual assets remain staged in `figures/part04/` and are tracked in `PART_IV_FIGURE_AUDIT.tsv`. They are intentionally not auto-inserted by this migration pass because raw multi-image groups require caption/placement review.

## Integrity rule

Every Part IV atlas unit has exactly one migration-ledger row and therefore one explicit disposition.
No missing statement or solution is fabricated.
