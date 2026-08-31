# Volume VII — Differential, Riemannian and Hyperbolic Geometry

**Status:** Canonical reconstruction complete for `VII/01`–`VII/42`; volume-level audit and freeze workflow available.

Volume VII develops smooth manifolds, bundles and forms, the geometry of curves and surfaces, Riemannian and Lorentzian geometry, hyperbolic geometry, and a final computational-geometry part linking smooth theory to discrete geodesics, Laplacians, and curvature-feature extraction.

## Part I — Smooth Manifolds

- **VII/01** — Topological Manifolds
- **VII/02** — Smooth Structures and Atlases
- **VII/03** — Smooth Maps and Diffeomorphisms
- **VII/04** — Tangent Spaces
- **VII/05** — Cotangent Spaces
- **VII/06** — Submanifolds and Products

## Part II — Bundles and Forms

- **VII/07** — Vector Bundles
- **VII/08** — Principal and Frame Bundles
- **VII/09** — Differential Forms
- **VII/10** — Orientation and Integration
- **VII/11** — Stokes' Theorem

## Part III — Curves and Surfaces

- **VII/12** — Regular Curves
- **VII/13** — Frenet Frames, Curvature and Torsion
- **VII/14** — Regular Surfaces
- **VII/15** — First and Second Fundamental Forms
- **VII/16** — The Gauss Map and Shape Operator
- **VII/17** — Principal, Gaussian and Mean Curvature
- **VII/18** — Ruled and Developable Surfaces
- **VII/19** — Minimal Surfaces

## Part IV — Riemannian Geometry

- **VII/20** — Riemannian Metrics
- **VII/21** — Connections
- **VII/22** — The Levi–Civita Connection
- **VII/23** — Geodesics
- **VII/24** — Parallel Transport
- **VII/25** — Holonomy
- **VII/26** — The Riemann Curvature Tensor
- **VII/27** — Ricci and Scalar Curvature
- **VII/28** — Weyl Curvature

## Part V — Lorentzian Geometry

- **VII/29** — Indefinite Metrics
- **VII/30** — Riemannian versus Lorentzian Geometry

## Part VI — Hyperbolic Geometry

- **VII/31** — Hyperbolic Plane Models
- **VII/32** — The Poincaré Metric
- **VII/33** — Möbius Transformations and PSL(2,R)
- **VII/34** — Hyperbolic Isometries
- **VII/35** — Fuchsian Groups
- **VII/36** — Hyperbolic Three-Space and PSL(2,C)
- **VII/37** — Kleinian Groups and Boundary Geometry

## Part VII — Computational Geometry

- **VII/38** — Discrete Geodesic Problems
- **VII/39** — Graph and Exact Mesh Geodesics
- **VII/40** — The Heat Method
- **VII/41** — Discrete Laplacians
- **VII/42** — Curvature Lines, Ridges and Valleys

## Canonical files

- Volume wrapper: `books/vol07_differential_geometry/book.tex`
- Chapters: `books/vol07_differential_geometry/chapters/chNN_*/chapter.tex`
- Corpus audit: `books/vol07_differential_geometry/AUDIT_VOLUME07.ps1`
- Windows build: `books/vol07_differential_geometry/BUILD_WINDOWS.ps1`
- Editorial status ledger: `editorial/CHAPTER_STATUS.tsv`
- Audit reports: `editorial/VOLUME_VII_CORPUS_AUDIT.md` and `.json`
- Freeze manifest: `editorial/VOLUME_VII_FREEZE_SHA256.tsv`
- Release note: `editorial/VOLUME_VII_RELEASE.md`

## Build

From the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\books\vol07_differential_geometry\BUILD_WINDOWS.ps1 `
  -Repo $PWD `
  -Clean
```

The canonical PDF is produced at:

```text
books/vol07_differential_geometry/book.pdf
```

The build script runs the corpus audit first, invokes `latexmk`, and rejects undefined or multiply defined references after the build.

## Audit only

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\books\vol07_differential_geometry\AUDIT_VOLUME07.ps1 `
  -Repo $PWD
```

The audit verifies:

- exactly 42 `VII/01`–`VII/42` ledger rows;
- all canonical chapter paths exist;
- exactly 42 active `\include{...}` entries in `book.tex`;
- exactly one chapter label with the established `ch:viiNN...` prefix per chapter;
- no case-sensitive duplicate labels;
- no unresolved Volume VII local references;
- no `TODO`, `FIXME`, `TBD`, `PLACEHOLDER`, or `\lipsum` markers;
- exercise/hint balance and `solutions = exercises + solved problems` in every chapter.

## Freeze policy

A Volume VII freeze is valid only when:

1. the corpus audit passes;
2. a clean `latexmk` build passes;
3. the build log has no unresolved-reference regression;
4. all 42 `CHAPTER_STATUS.tsv` rows are `FROZEN` with `next_action=COMPLETE`;
5. `editorial/VOLUME_VII_FREEZE_SHA256.tsv` records SHA-256 hashes for the canonical volume sources and QA files.

Once those conditions are met, Volume VII is closed and Volume VIII can begin.
