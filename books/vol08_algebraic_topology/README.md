# Volume VIII — Algebraic Topology

**Status:** Canonical reconstruction underway through `VIII/04`.

Canonical chapter codes: `VIII/01`–`VIII/35`.

## Part I — Homotopy
- **VIII/01** — Homotopies of Maps
- **VIII/02** — Homotopy Equivalence and Contractibility
- **VIII/03** — Degree of Maps
- **VIII/04** — Spheres and Antipodal Maps

## Part II — CW Complexes
- **VIII/05** — Cell Attachments
- **VIII/06** — CW Complexes
- **VIII/07** — Mapping Cones
- **VIII/08** — Homotopic Attaching Maps

## Part III — Fundamental Groups and Coverings
- **VIII/09** — Paths and Fundamental Groups
- **VIII/10** — Covering Spaces
- **VIII/11** — Lifting Properties
- **VIII/12** — Deck Transformations and Group Actions
- **VIII/13** — SU(2) to SO(3)
- **VIII/14** — Free Groups and Covering Graphs

## Part IV — Homology
- **VIII/15** — Simplicial Complexes
- **VIII/16** — Chain Complexes
- **VIII/17** — Simplicial and Singular Homology
- **VIII/18** — Cellular Homology
- **VIII/19** — Relative Homology and Exact Sequences
- **VIII/20** — Homotopy Invariance
- **VIII/21** — Euler Characteristic

## Part V — Homological Machinery
- **VIII/22** — Chain Homotopies
- **VIII/23** — Chain Contractions
- **VIII/24** — Mapping Cones of Chain Maps
- **VIII/25** — Homology with Coefficients
- **VIII/26** — The Universal Coefficient Theorem
- **VIII/27** — Products and the Künneth Theorem

## Part VI — Cohomology, Bundles and Manifolds
- **VIII/28** — Cohomology
- **VIII/29** — Cup Products
- **VIII/30** — Vector Bundles and Clutching
- **VIII/31** — Thom Classes
- **VIII/32** — Sphere Bundles and Euler Classes
- **VIII/33** — Poincaré Duality
- **VIII/34** — Intersection Forms
- **VIII/35** — Lefschetz Theory

## Source and dossier rule

Reconstruction follows `../../editorial/SOURCE_MIGRATION.tsv`.

For this batch:
- VIII/04 follows the `sphere|antipodal` stream from
  `theory-of-algebraic-topology-1.tex` and inherited descendants.
- VIII/05 merges the primary cell-attachment stream from
  `theory-of-algebraic-topology-2.tex` with relevant attachment/CW overlap
  from `theory-of-algebraic-topology-11.tex`. Higher-precedence material
  explicitly assigned to VIII/08 stays in VIII/08.
- VIII/06 follows the explicit CW-complex stream and inherited descendants.

Solved dossiers are not capped at 12. Current coverage:
- VIII/04: **20 dossiers**
- VIII/05: **24 dossiers**
- VIII/06: **20 dossiers**

Each chapter also contains **24 exercises and 24 hints**.

## Reconstruction status
- VIII/01: DRAFTED
- VIII/02: DRAFTED
- VIII/03: DRAFTED
- VIII/04: DRAFTED
- VIII/05: PLANNED
- VIII/06: PLANNED
- VIII/07: PLANNED
- VIII/08: PLANNED

## Build
```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\books\vol08_algebraic_topology\BUILD_WINDOWS.ps1 `
  -Repo $PWD `
  -Clean
```
