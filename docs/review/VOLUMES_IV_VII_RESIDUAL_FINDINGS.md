# Volumes IV–VII residual findings

Baseline: `280841981748bb1991d8f29b6bb5a5a92d7c5fdc`

Audit-only ledger; no reader-facing book prose is changed in this commit.

## Volume IV

- **R001 / P1 / GEN_WORKED** — 365 occurrence(s); first line 103: tic]\label{ex:iv01-worked-01} Give a rigorous worked analysis of Complex derivative. State the relevant holomorphic, contour, series, or singularity hypothesis → `refactor(v4): replace templated synthesis and exercise boilerplate with chapter-specific analysis` [RESOLVED]
- **R002 / P1 / CENTRAL_PRINCIPLE_EXERCISE** — 248 occurrence(s); first line 209: {exercise}\label{exr:iv01-01} State and apply the central principle behind Complex derivative. Give one concrete consequence. \end{exercise} \begin{hint} Compar → `refactor(v4): replace templated synthesis and exercise boilerplate with chapter-specific analysis` [RESOLVED]
- **R003 / P1 / STOCK_DECISIVE_STEP** — 365 occurrence(s); first line 103: arbitrary complex directions. The decisive step is to use the complex-analytic structure globally rather than reason from real-variable intuition alone. \end{ex → `refactor(v4): replace templated synthesis and exercise boilerplate with chapter-specific analysis` [RESOLVED]
- **R004 / P1 / STOCK_REUSE_ENDING** — 248 occurrence(s); first line 215: arbitrary complex directions. The same principle can then be reused in later contour, residue, conformal, or Riemann-surface arguments. \end{solution} \begin{e → `refactor(v4): replace templated synthesis and exercise boilerplate with chapter-specific analysis` [RESOLVED]
- **R005 / P1 / STOCK_CHAPTER_STRATEGY** — 31 occurrence(s); first line 202: quickly leads to analyticity. The reusable strategy is to identify the analytic domain, choose the correct local expansion or contour representation, apply the → `refactor(v4): replace templated synthesis and exercise boilerplate with chapter-specific analysis` [RESOLVED]
- **R006 / P2 / INTERNAL_MARKERS** — 279 marker comment(s); first line 23: % BEGIN VOL04-EXPANSION IV01-example-01 → `chore(editorial): classify and remove obsolete reconstruction markers from volumes IV-VII` [RESOLVED]
- **R007 / P2 / BUILD_LAYOUT_AUDIT** — status=PASS; overfull=0; underfull=0; undefined=0; reviewed=2026-09-12 → `style(v4): replace overwide conceptual roadmaps with breakable layout` [RESOLVED]

## Volume V

- **R008 / P1 / GEN_WORKED** — 336 occurrence(s); first line 86: stic]\label{ex:v01-worked-01} Give a rigorous worked analysis of Commutative rings. State the ring, module, finiteness, localization, or homological hypotheses → `refactor(v5): replace generic diagnostic and exercise boilerplate with chapter-specific algebra` [RESOLVED]
- **R009 / P1 / CENTRAL_PRINCIPLE_EXERCISE** — 224 occurrence(s); first line 191: n{exercise}\label{exr:v01-01} State and apply the central principle behind Commutative rings. Give one concrete algebraic consequence. \end{exercise} \begin{hin → `refactor(v5): replace generic diagnostic and exercise boilerplate with chapter-specific algebra` [RESOLVED]
- **R010 / P1 / STOCK_DECISIVE_STEP** — 336 occurrence(s); first line 86: d commutative multiplication. The decisive step is to use the universal property, exactness criterion, localization test, or finite-generation mechanism appropr → `refactor(v5): replace generic diagnostic and exercise boilerplate with chapter-specific algebra` [RESOLVED]
- **R011 / P1 / STOCK_REUSE_ENDING** — 224 occurrence(s); first line 197: d commutative multiplication. The same principle can then be reused in later localization, support, base-change, resolution, Tor, or Ext arguments. \end{solutio → `refactor(v5): replace generic diagnostic and exercise boilerplate with chapter-specific algebra` [RESOLVED]
- **R012 / P1 / STOCK_ALGEBRA_STRATEGY** — 28 occurrence(s); first line 185: tions into algebraic objects. The recurring strategy is to encode the algebraic object by kernels, quotients, localization, finite presentation, or a resolution → `refactor(v5): replace generic diagnostic and exercise boilerplate with chapter-specific algebra` [RESOLVED]
- **R013 / P2 / INTERNAL_MARKERS** — 224 marker comment(s); first line 26: % BEGIN VOL05-EXPANSION V01-example-01 → `chore(editorial): classify and remove obsolete reconstruction markers from volumes IV-VII` [RESOLVED]
- **R014 / P2 / BUILD_LAYOUT_AUDIT** — status=PASS; overfull=0; underfull=0; undefined=0; reviewed=2026-09-12 → `style(v5): replace overwide conceptual roadmaps with breakable layout` [RESOLVED]

## Volume VI

- **R015 / P1 / DRAFTED** — 6 occurrence(s); first line 2: 01 — Algebraic Sets % Status: DRAFTED % % Editorial provenance: % - governed by editorial/SOURCE_MIGRATION.tsv % - primary legacy family: theory-of-differen → `refactor(v6): replace generic supplementary hints with problem-specific algebraic-geometry guidance` [RESOLVED]
- **R016 / P2 / INTERNAL_MARKERS** — 446 marker comment(s); first line 5: %   - governed by editorial/SOURCE_MIGRATION.tsv → `chore(editorial): classify and remove obsolete reconstruction markers from volumes IV-VII` [RESOLVED]
- **R017 / P2 / BUILD_LAYOUT_AUDIT** — status=PASS; overfull=6; underfull=20; undefined=0 → `style(v6): layout cleanup if needed` [OPEN]

## Volume VII

- **R018 / P2 / INTERNAL_MARKERS** — 1008 marker comment(s); first line 158: % PEDAGOGY-ENRICHED-VII → `chore(editorial): classify and remove obsolete reconstruction markers from volumes IV-VII` [RESOLVED]
- **R019 / P2 / BUILD_LAYOUT_AUDIT** — status=PASS; overfull=0; underfull=7; undefined=0; reviewed=2026-09-12 → `style(v7): break overwide differential-geometry displays` [RESOLVED]

## Rules

- Existing professional-review commits are baseline and are not repeated.
- Genuine mathematical errors get dedicated `fix(vN)` commits before editorial cleanup.
- Semantic cleanup preserves stable labels and exercise/problem counts.
- Freeze/page/hash metadata is not touched before the final built PDF.
