# Companion Part V — V-G final source reconciliation

## Final six unsolved candidates
All six were resolved without creating artificial new Companion problems.

- `IMP-M3-F4E66B2919-P045` -> duplicate composite of CP-V-0021 and CP-V-0045.
- `IMP-M3-F4E66B2919-P059` -> duplicate of CP-V-0042.
- `IMP-M3-0D398C7F27-R004954-D8354E99` -> explanatory reference to CP-V-0021.
- `IMP-M3-1FB8799CDC-P057` -> duplicate of CP-V-0020.
- `IMP-M3-17140B7F4C-R004127-B3F90696` -> explanatory reference to CP-V-0045 / CP-V-0044.
- `IMP-M3-0D398C7F27-R005210-707624FA` -> explanatory reference to CP-V-0045 / CP-V-0044.

## Reconciliation result
- source candidate inventory: 738
- unresolved candidates: 0
- canonical reader-facing problems: 68
- canonical solutions: 68
- canonical labels: 68
- migration rows: 68
- continuous IDs: True
- migration/chapter ID-order match: True

### Final disposition counts
CONSOLIDATE_WITH_PARENT     190
DUPLICATE                    10
EXPLANATORY_REFERENCE        23
EXPOSITION_ONLY             425
MIGRATED_OR_CONSOLIDATED     90

## Status
**Source reconciliation is complete: zero unresolved candidate units remain.**

This is not yet the repository/PDF freeze because two external integration steps remain:

1. replace the repository Part V chapter and migration ledger with these reconciled files;
2. reconcile the exact V/01–V/28 chapter subtitles from the canonical Volume V `book(2).tex`, then run the repository validator, full Companion LaTeX build, PDF diagnostics, and freeze hashes.

No further source-problem mining is required before those integration steps.
