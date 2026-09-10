# Volume IV — Mathematical Navigation

This professional-review sidecar records the logical and notational dependencies of IV/01--IV/31. The historical freeze remains provenance; current source and this graph are the review baseline.

## Comes from

- **II/03 — Sequences and Cauchy Sequences** → **IV/03 — Power Series and Analytic Functions** — convergence language and completeness underlie power-series arguments.
- **II/04–II/07 — Topological foundations** → **IV/04–IV/05 — Complex Integration and Cauchy's Theorem** — open sets, continuity, connectedness and path-connectedness support domains, contours, homotopies and simply connected regions.
- **II/08 — Differentiability in Several Variables** → **IV/01–IV/02 — Complex Differentiability and Cauchy--Riemann Equations** — the real derivative/Jacobian viewpoint makes complex linearity and the Cauchy--Riemann equations precise.
- **II/09 — Inverse and Implicit Function Principles** → **IV/17, IV/22, IV/24** — the inverse-function principle reappears in local biholomorphisms, unramified projections and ramification models.
- **II/10 — Riemann Integration** → **IV/04 — Complex Integration** — line integrals are built from ordinary real-variable integration along parametrized curves.
- **II/11–II/13 — Sequences and Series of Functions** → **IV/03, IV/08, IV/29** — locally uniform convergence supports differentiation/integration of analytic series, Laurent expansions and Weierstrass series.

## Internal logical spine

```text
IV/01 -> IV/02 -> IV/03
   \       \        \
    \       \        -> IV/08 -> IV/09 -> IV/10 -> IV/11
     -> IV/04 -> IV/05 -> IV/06 -> IV/07
                              \       \
                               \       -> IV/12 -> IV/13 -> IV/14 -> IV/15
                                -> IV/16 -> IV/17 -> IV/18

IV/19 -> IV/20 -> IV/21

IV/14 + IV/15 -> IV/22 -> IV/23 -> IV/24 -> IV/26
                         \       \        \
                          -> IV/25 -------->

IV/26 -> IV/27 -> IV/28 -> IV/29 -> IV/30 -> IV/31
```

The graph is not purely linear. `reports/vol04/VOL04_PREREQUISITE_GRAPH.tsv` records the actual earlier chapters and external standard inputs used by each chapter.

## Proof-scope policy

- Local complex differentiation, contour integration, Cauchy theory, residues, winding numbers, local ramification, Riemann--Hurwitz and elliptic-function identities are developed inside Volume IV where stated with proofs.
- The **Riemann mapping theorem existence statement** is explicitly imported as a standard theorem; its normal-family/Montel proof is outside the present volume's developed machinery.
- Basic real multivariable calculus, Riemann integration, elementary point-set topology, compact orientable-surface topology and triangulation are named as external/foundational inputs when used.

## Leads to

- **IV/23 — Covering Maps and Monodromy** → **VIII/10 — Covering Spaces** — analytic covering theory continues in algebraic topology.
- **IV/27 — Lattices and Complex Tori** → **VII/07 — Vector Bundles** — complex tori are geometric quotient examples relevant to bundle constructions.
- **IV/31 — Elliptic Curves as Riemann Surfaces** → **VI/43 — Plane Cubics** — the analytic torus/cubic equivalence meets algebraic plane-cubic geometry.

## Numerical interpretation inherited from Volumes I--III

Volume IV inherits the series-wide rule that exact complex-analytic theorems and
finite numerical evidence are distinct claims.

The principal computational hotspots are:

- **IV/04 Complex Integration:** computed contour integrals must state the
  parameterization, quadrature/refinement rule, tolerance, and relevant
  distance from nearby singularities.  Exact reparameterization invariance does
  not imply equal discretization error under different parameterizations.
- **IV/12 Winding Numbers and the Argument Principle:** an integer zero/pole
  count obtained numerically needs a certified contour-clearance and integral
  error margin; closeness to an integer alone is heuristic.
- **IV/13 Rouch\'e's Theorem:** the strict domination inequality must hold on
  the whole contour.  Sampled inequalities need between-sample control and a
  positive margin that survives evaluation error.
- **IV/15 Analytic Continuation:** finite local representations require overlap
  checks, singularity-distance control, and explicit branch/sheet tracking.
  Numerical endpoint agreement does not certify trivial monodromy.
- **IV/18 Schwarz--Christoffel Transformations:** accessory-parameter solves
  require normalization, nonlinear residuals, Jacobian conditioning,
  prevertex-order/crowding checks, and branch-aware quadrature near algebraic
  endpoint singularities.

The remaining holomorphic, residue, Riemann-surface, and elliptic-function
theorems remain exact mathematics unless a chapter explicitly turns them into a
finite computational procedure.

## Reading principle

Follow `established_prerequisites` backward for logical dependencies. Treat `external_standard_imports` as declared inputs rather than hidden later-chapter dependencies. Forward previews are motivational only unless the row says otherwise.
