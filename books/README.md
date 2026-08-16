# Canonical Mathematics Series

This tree contains the reconstructed canonical books. The legacy manuscripts remain in `chapters/tex/` until their mapped content has been migrated and audited.

The chapter code and title list is governed by `../editorial/CONTENT_ATLAS.md`; source selection is governed by `../editorial/SOURCE_MIGRATION.tsv`.

## Volumes

- **Volume I — Linear Algebra** → `vol01_linear_algebra/`
- **Volume II — Real Analysis and Topological Foundations** → `vol02_real_analysis/`
- **Volume III — Measure, Fourier Analysis, Distributions and PDE** → `vol03_fourier_distributions_pde/`
- **Volume IV — Complex Analysis and Riemann Surfaces** → `vol04_complex_analysis/`
- **Volume V — Commutative Algebra and Homological Methods** → `vol05_commutative_algebra/`
- **Volume VI — Algebraic Geometry and Sheaf Theory** → `vol06_algebraic_geometry/`
- **Volume VII — Differential, Riemannian and Hyperbolic Geometry** → `vol07_differential_geometry/`
- **Volume VIII — Algebraic Topology** → `vol08_algebraic_topology/`

## Chapter source convention

When reconstruction of a chapter begins, create:

```text
chapters/chNN_slug/
├── chapter.tex
├── examples.tex
├── exercises.tex
├── hints.tex
├── solutions.tex
└── figures/
```

Only create files that contain real canonical content; do not pre-create 256 empty chapter files.
