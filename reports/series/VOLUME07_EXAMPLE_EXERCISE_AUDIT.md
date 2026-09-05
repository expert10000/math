# Volume VII worked-example and graded-exercise audit

**Result:** PASS
**Stage:** 1 — protected baseline captured
**Architecture:** split pedagogy layer; canonical chapter sources remain byte-for-byte unchanged.

The audit establishes the immutable source baseline for all 42 chapters and the expansion target
of three worked examples plus sixteen graded exercise/hint/solution triads per enriched chapter.

| Range | Mathematical block | Content commit | Target per chapter |
|---|---|---:|---|
| VII/01--VII/11 | Smooth Manifolds; Bundles and Forms | 2 | 3 examples + 16 triads |
| VII/12--VII/19 | Curves and Surfaces | 3 | 3 examples + 16 triads |
| VII/20--VII/30 | Riemannian and Lorentzian Geometry | 4 | 3 examples + 16 triads |
| VII/31--VII/42 | Hyperbolic and Computational Geometry | 5 | 3 examples + 16 triads |

## Protection contract

The 42 canonical `chapter.tex` files are tracked by Git blob SHA-1 in the baseline JSON.
All pedagogy additions are separate files and are included only from `book.tex`.
Any canonical-chapter drift is therefore an audit failure.

## Grading balance

Every enriched chapter must contain exactly:
- 5 standard computations/constructions;
- 4 proofs;
- 3 counterexamples or hypothesis tests;
- 2 applications/investigations;
- 2 challenges.

Stage 1 intentionally adds no mathematical content. Stages 2--5 are required to satisfy the
per-chapter target.
