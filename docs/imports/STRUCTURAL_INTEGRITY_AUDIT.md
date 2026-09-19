# Imported problem structural-integrity audit

This review-only pass checks whether `PROBLEM_LEDGER.tsv` rows are structurally
well segmented before semantic classification.

It flags oversized rows, rows containing multiple problem/exercise/example
headings, and rows containing multiple solution markers.

It also previews recovery of the five Tier-2 cases already identified as
`NEEDS_STRUCTURAL_RESCAN`.

No canonical book content and no problem/solution links are modified.
