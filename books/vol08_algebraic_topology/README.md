# Volume VIII — Algebraic Topology

**Status:** Canonical reconstruction underway through `VIII/07`.

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

## Source rule for VIII/07–VIII/09

Reconstruction follows `../../editorial/SOURCE_MIGRATION.tsv`:

- VIII/07: `theory-of-algebraic-topology-10.tex`, explicit `mapping cone`
  selector plus inherited theorem/problem descendants; unmatched fallback is
  reviewed for false positives before migration.
- VIII/08: `theory-of-algebraic-topology-11.tex`, explicit
  `homotopic attaching` selector plus inherited descendants.
- VIII/09: `theory-of-algebraic-topology-4.tex`, explicit
  `fundamental group|pi_1` selector plus inherited descendants; unmatched
  fallback is reviewed for false positives before migration.

## Dossier policy

During chapter creation, solved dossiers are expanded by subject coverage rather
than fixed to twelve.  The definitive **one-to-one legacy dossier reconciliation**
will be performed after all Volume VIII chapters are reconstructed, when every
source block has a stable destination.

Current reconstructed batch:
- VIII/07: **20 solved dossiers**

Each reconstructed chapter also has **24 exercises and 24 hints**.

## Reconstruction status
- VIII/01: DRAFTED
- VIII/02: DRAFTED
- VIII/03: DRAFTED
- VIII/04: DRAFTED
- VIII/05: DRAFTED
- VIII/06: DRAFTED
- VIII/07: DRAFTED
- VIII/08: PLANNED
- VIII/09: PLANNED
- VIII/10: PLANNED
- VIII/11: PLANNED

## Build
```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\books\vol08_algebraic_topology\BUILD_WINDOWS.ps1 `
  -Repo $PWD `
  -Clean
```
