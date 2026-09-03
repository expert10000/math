# Theory of Mathematics I–VIII — v1.1 RC1

This release candidate is a post-v1.0 editorial/proofing layer. The frozen mathematical chapter corpus remains unchanged.

## Added after v1.0

- Canonical problem/dossier index: **4061** `problem` entries.
- Additional indexed `challenge` entries: **0**.
- Curated cross-volume chapter bridges: **36**.
- Rendered proof pages: **2173 / 2173**.
- Low-text pages queued for human review: **11**.
- LaTeX overfull boxes queued for review: **118**, including **13** >=20pt.

## Release-candidate status

- Global corpus reconciliation remains PASS.
- Eight canonical volume PDFs are included.
- Every PDF page was successfully rasterized in the automated rendered proof.
- Candidate visual issues are recorded as a targeted human-proof queue rather than silently rewritten.

## Next gate

Perform the targeted human visual review of pages flagged in `evidence/RENDERED_PAGE_PROOF.tsv` and `evidence/LATEX_LAYOUT_WARNINGS.tsv`. Apply only confirmed errata before promoting v1.1 RC1 to v1.1.
