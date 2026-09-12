# Theory of Mathematics I–VIII — v1.3-rc1 Release Candidate

This directory is the canonical v1.3-rc1 release-candidate bundle for the eight-volume series.

## Release state

- Canonical volumes: **8 / 8**
- Canonical chapters: **256 / 256**
- Chapter status: **256 FROZEN / 256 COMPLETE**
- Canonical PDF builds: **8 PASS / 0 FAIL / 0 NO_WRAPPER**
- SOURCE_MIGRATION rows: **1463**
- Unresolved source-map rows: **0**
- Missing mapped source files: **0**
- Duplicate canonical labels: **0**
- Missing canonical references: **0**
- Reconstruction scaffolds remaining: **0**

## PDFs

- Volume I — Linear Algebra: **174 pages**, SHA-256 `439c20054c5392e743c3ded20b51d692a99e2a4141f4f961e32f73678a3611ff`
- Volume II — Real Analysis and Topological Foundations: **225 pages**, SHA-256 `82194227a46db53b5c0383df0dcfb53c6fe029869e30cf2297c4d7b6c116d2c8`
- Volume III — Measure, Fourier Analysis, Distributions and PDE: **272 pages**, SHA-256 `9d4891ef2eea045f7af30e67cfffb75ecd8db2649e6d0bf171f3f701ae249972`
- Volume IV — Complex Analysis and Riemann Surfaces: **327 pages**, SHA-256 `59625efe670d4b3d00322bea2eda30e93ab14812fcf16df85175e298c825586b`
- Volume V — Commutative Algebra and Homological Methods: **276 pages**, SHA-256 `7bdeff50eec9a63f5df7b1808b8fd5107f4d50f93823fcf4ee764b8abfb362e0`
- Volume VI — Algebraic Geometry and Sheaf Theory: **800 pages**, SHA-256 `185f4e48eebec8359cf8db5539e97d53cbea020699fa3f2a9b9301e453732ecf`
- Volume VII — Differential, Riemannian and Hyperbolic Geometry: **496 pages**, SHA-256 `64e0f4970caee6c05456e214264896e6459f8f159d17ec788ef00ddfe83502bd`
- Volume VIII — Algebraic Topology: **469 pages**, SHA-256 `4e7d3d0be3b65896abcafba9ae90f2dd66ca5f43f5c75c22c4af52e9f98ea2ef`

## Manifests

- `manifests/CHAPTERS.tsv` — one row per canonical chapter with source hash.
- `manifests/PDFS.tsv` — one row per canonical volume PDF with page count, size, and SHA-256.
- `SHA256SUMS.txt` — hashes for every file in this release bundle except the hash file itself.

## Evidence

The `evidence/` directory contains the global audits, source-migration reconciliation, build inventories, navigation, dashboard, and available per-volume freeze evidence.


## v1.3-rc1 professional-review candidate

- Final Volume I-VIII release-candidate gate: **PASS**.
- All **256 / 256** canonical chapters are FROZEN / COMPLETE.
- Clean canonical builds: **8 / 8 PASS**.
- Blocking >=20pt overfull boxes in the final gate: **0**.
- Cross-volume mathematical navigation and release metadata: **reconciled / PASS**.
- This directory is a release candidate; it does not replace the frozen v1.2 final release.
