# Volume VIII — Algebraic Topology

**Status:** Canonical reconstruction underway through `VIII/21`.

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

## Source rule for VIII/19–VIII/21

Reconstruction follows `../../editorial/SOURCE_MIGRATION.tsv`.

- VIII/19 merges the explicit `relative homology|long exact` stream from
  `theory-of-algebraic-topology-5.tex` with the explicit `relative homology`
  stream from `theory-of-algebraic-topology-7.tex`, including inherited
  problem/exercise/solution and theorem descendants.
- VIII/20 follows the explicit `homotopy invariance` stream from
  `theory-of-algebraic-topology-7.tex`, with the prism/chain-homotopy proof kept
  here and later abstract chain-homotopy machinery reserved for VIII/22.
- VIII/21 merges the explicit `Euler characteristic` stream from
  `theory-of-algebraic-topology-5.tex` with the explicit
  `Euler characteristic|Euler-Poincare` stream from
  `theory-of-algebraic-topology-8.tex`, including inherited descendants.

Higher-precedence material for VIII/22 and later chapters is not absorbed into
this batch.

## Dossier policy

Solved dossiers are expanded by subject coverage during reconstruction. The
definitive one-to-one legacy dossier reconciliation remains scheduled after
VIII/35.

Current reconstructed batch:
- VIII/19: **24 solved dossiers**
- VIII/20: **22 solved dossiers**
- VIII/21: **24 solved dossiers**

Each reconstructed chapter also has **24 exercises and 24 hints**.

## Reconstruction status
- VIII/01–VIII/18: DRAFTED
- VIII/19: DRAFTED
- VIII/20: DRAFTED
- VIII/21: DRAFTED
- VIII/22: PLANNED
- VIII/23: PLANNED
- VIII/24: PLANNED

## Build
```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\books\vol08_algebraic_topology\BUILD_WINDOWS.ps1 `
  -Repo $PWD `
  -Clean
```
