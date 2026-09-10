# Volume II — Mathematical Navigation

This sidecar adds cross-volume prerequisites, continuations, and see-also links without changing the frozen theorem/chapter text.

## Comes from

No curated incoming cross-volume bridge.

## Leads to

- **II/04 — Open and Closed Sets** → **VII/01 — Topological Manifolds** — Open and closed sets supply the local topological language of manifolds.
- **II/05 — Metric Spaces and Continuity** → **VII/01 — Topological Manifolds** — Metric-space continuity prepares the topology underlying manifolds.
- **II/08 — Differentiability in Several Variables** → **VII/03 — Smooth Maps and Diffeomorphisms** — Several-variable differentiability is the analytic model for smooth maps.
- **II/09 — Inverse and Implicit Function Principles** → **VII/06 — Submanifolds and Products** — Inverse and implicit function principles drive submanifold constructions.
- **II/06 — Compactness** → **VIII/02 — Homotopy Equivalence and Contractibility** — Compactness interacts strongly with homotopy equivalence and global topology.

## Numerical interpretation inherited from Volume I

Volume II follows the repository-wide numerical interpretation policy established
from Volume I.  Exact analytic theorems and floating-point evidence are kept
distinct, and local tolerances or residuals are introduced only where numerical
computation is materially used.

The principal Volume II hotspots are:

- **II/08 Differentiability in Several Variables:** an exact derivative is a
  linear map; a computed Jacobian may require error bounds, singular-value
  tolerances, and conditioning information before rank is inferred.
- **II/09 Inverse and Implicit Function Principles:** exact invertibility is the
  theorem hypothesis, while \(\sigma_{\min}\) and the inverse condition number
  describe numerical sensitivity.
- **II/20 Polynomial Interpolation:** exact uniqueness at distinct nodes does
  not imply a well-conditioned Vandermonde solve or stable coefficient
  representation.
- **II/22 Chebyshev and Minimax Approximation:** a sampled maximum error is a
  lower estimate of the continuum sup norm unless between-grid behavior is
  controlled.
- **II/24 Numerical Quadrature:** truncation error, adaptive error indicators,
  floating-point error, and uncertainty in sampled data are distinct parts of
  the numerical error budget.

Pure topology, compactness, connectedness, and exact convergence arguments in
the other chapters remain exact mathematics and do not acquire numerical
caveats merely because later implementations may discretize them.

## Reading principle

These links are editorial navigation, not formal logical dependencies. They identify especially useful conceptual transitions in the frozen 256-chapter series.
