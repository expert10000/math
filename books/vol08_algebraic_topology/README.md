# Volume VIII — Algebraic Topology

**Status:** FROZEN — Volume VIII Algebraic Topology v1.0 release baseline.

Canonical chapter codes: `VIII/01`–`VIII/35`.

## Parts I–V

VIII/01–VIII/27 contain the homotopy, covering-space, simplicial, homological,
chain-complex, coefficient, universal-coefficient, and product foundations.

## Part VI — Cohomology, Bundles and Manifolds

- **VIII/28 — Cohomology**
- **VIII/29 — Cup Products**
- **VIII/30 — Vector Bundles and Clutching**
- **VIII/31 — Thom Classes**
- **VIII/32 — Sphere Bundles and Euler Classes**
- **VIII/33 — Poincaré Duality**
- **VIII/34 — Intersection Forms**
- **VIII/35 — Lefschetz Theory**

## Source rule for VIII/28–VIII/30

Reconstruction follows `../../editorial/SOURCE_MIGRATION.tsv`.

- **VIII/28:** the ledger contains the mapped annulus/connecting support visual
  from `problems_9_10_visuals_embedded.tex`; the chapter is a principled
  reconstruction from the canonical chain, homology, and UCT foundations while
  preserving that mapped topic.
- **VIII/29:** follows the targeted cup-product and cohomology-ring stream in
  `theory-of-algebraic-topology-15.tex`, including inherited theorem/problem
  descendants.
- **VIII/30:** follows the vector-bundle, Möbius-bundle, and clutching streams
  in `theory-of-algebraic-topology-14.tex`, including inherited
  theorem/problem descendants and reviewed fallback material.

Material assigned to Thom classes, Euler classes, Poincaré duality,
intersection forms, or Lefschetz theory remains in VIII/31–VIII/35.

## Visual layer

The volume retains editable SVG teaching assets alongside canonical LaTeX.
The LaTeX build does not require Inkscape, `svg.sty`, shell escape, or an
external SVG renderer.

## Release state

All 35 canonical chapters are `FROZEN / COMPLETE`. The release baseline has:

- one-to-one corpus reconciliation with zero unresolved source instances;
- paired final exercise solutions;
- 35 active canonical chapter includes;
- duplicate-label and internal-reference audits;
- visual inventory and integration audits;
- a clean canonical PDF build;
- source and release SHA-256 evidence.

## Complete-volume integration

See `VOLUME08_INTEGRATION_VISUAL_HARMONIZATION.md`,
`VOLUME08_NAVIGATION.md`, `VOLUME08_SVG_INVENTORY.md`, and
`VOLUME08_INTEGRATION_AUDIT.md`.

## One-to-one corpus reconciliation

See `reconciliation/VOLUME08_RECONCILIATION_REPORT.md` and
`reconciliation/VOLUME08_RECONCILIATION.tsv`.

## Freeze/release evidence

See `freeze/VOLUME08_FREEZE_REPORT.md` and
`freeze/VOLUME08_FREEZE_MANIFEST.sha256`.
