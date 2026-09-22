# Companion Part IV figures

This directory contains source-grounded visual material for **Part IV â€” Complex Analysis and Riemann Surfaces**.

The first visual migration batch is intentionally conservative:

- external source figures are copied from `imports/ALL_TEX_AND_FIGURES/figures/...`;
- problem-local TikZ is extracted from the exact source line span recorded in the imported-problem ledger;
- source captions/labels are preserved when the source uses a complete TikZ `figure` float;
- figures are **not inserted into the Part IV chapter scaffold yet** because the corresponding Companion problems have not been migrated;
- candidate figures that were not already present in source are deferred to a later design pass.

Canonical integration should occur when the matching `CP-IV-xxxx` problem is inserted into
`chapters/part04_volume_iv/chapter.tex`.

See `metadata/PART_IV_FIGURE_AUDIT.tsv` for provenance and disposition.