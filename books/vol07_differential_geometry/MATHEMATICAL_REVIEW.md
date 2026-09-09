# Volume VII mathematical review — VII/01–VII/42

Pinned base: `e0766a28be4cce2aa6393b31d25197d54f2353ac`

This is a conservative post-freeze professional review of the 42-chapter canonical Volume VII corpus. The existing reconstruction, corpus audit, labels, problem/solution structure, and release freeze are preserved. Mathematical prose is changed only where a chapter-local defect is demonstrated; broad regex rewriting is prohibited.

## Review principles

- Preserve the established chapter architecture and numbering VII/01–VII/42.
- Preserve theorem hypotheses unless a correction is mathematically required.
- Treat sign, normalization, regularity, completeness, compactness, orientation, and boundary assumptions as mathematical data.
- Distinguish smooth statements from discrete/numerical analogues.
- Do not promote numerical approximations to exact theorems.
- Keep Riemannian, Lorentzian, hyperbolic, and computational conventions explicit and mutually consistent.

## Hypothesis- and convention-sensitive audit map

### VII/01–VII/06 — smooth manifolds

Release-critical distinctions include Hausdorff and second-countable assumptions; manifolds with versus without boundary; compatibility and maximality of atlases; rank hypotheses for smooth maps; tangent-space models; and the hypotheses of inverse-, implicit-, constant-rank-, regular-value-, and submanifold results.

### VII/07–VII/11 — bundles, forms and integration

Check local triviality and transition functions; left/right principal actions; frame-bundle conventions; pullbacks; wedge-product signs; exterior derivative identities; orientation conventions; integration of top forms; partitions of unity where used; compact-support assumptions; and the induced orientation on a boundary in Stokes' theorem.

### VII/12–VII/19 — curves and surfaces

Check regular versus unit-speed curves; hypotheses for Frenet frames; curvature and torsion conventions; regular-surface hypotheses; first and second fundamental forms; normal orientation; sign of the shape operator; principal curvatures; Gaussian curvature `K`; mean-curvature normalization `H`; ruled/developable exceptional cases; and the equivalences used for minimal surfaces.

### VII/20–VII/28 — Riemannian geometry

Check positive-definiteness of the metric; affine-connection conventions; torsion; the Koszul formula; Levi-Civita existence/uniqueness; geodesic equations and parametrization; local domain of the exponential map; parallel transport; holonomy basepoint dependence; Riemann-curvature sign convention; Ricci contraction; scalar and sectional curvature; and dimension-dependent statements involving the Weyl tensor.

### VII/29–VII/30 — Lorentzian geometry

Check signature convention; timelike/spacelike/null terminology; time orientation and causal assumptions where required; the failure of Riemannian compactness/completeness implications in indefinite signature; and whether statements concern geodesic, metric, or causal completeness.

### VII/31–VII/37 — hyperbolic geometry

Check curvature `-1` normalization; disk and upper-half-plane metrics; conversion between models; Möbius actions; the quotient from `SL(2,R)` to `PSL(2,R)`; classification of orientation-preserving isometries; discreteness and proper-discontinuity hypotheses for Fuchsian groups; quotient/orbifold caveats; the `PSL(2,C)` action on hyperbolic three-space; and Kleinian limit-set/domain-of-discontinuity terminology.

### VII/38–VII/42 — computational geometry

Check the distinction between graph distance, polyhedral geodesic distance, and smooth intrinsic distance; exact versus approximate mesh-geodesic algorithms; heat-equation and Laplacian sign conventions; time-step assumptions in the heat method; gradient normalization; Poisson null spaces and boundary conditions; cotangent-weight conventions and Delaunay/positivity caveats; lumped versus consistent mass matrices; and the distinction between smooth curvature lines/ridges/valleys and discrete estimators.

## Standing consistency checks

The following conventions must be settled consistently across chapters rather than inferred locally:

1. sign of the shape operator;
2. normalization of mean curvature;
3. sign of the Riemann curvature tensor;
4. contraction convention for Ricci curvature;
5. sign of the Laplace–Beltrami operator;
6. Lorentzian signature convention;
7. hyperbolic sectional-curvature normalization;
8. orientation convention for boundaries;
9. use of exact versus approximate language in mesh algorithms.

## Result of this pass

No repository-wide stale `DRAFTED` header pattern is present in Volume VII, unlike the defect found during the preceding Volume VI review. Therefore this commit does not manufacture bulk chapter edits. It establishes the mathematical review contract and the exact points that must govern any targeted chapter-local correction discovered during subsequent PDF/content review.

The existing `AUDIT_VOLUME07.ps1` and `BUILD_WINDOWS.ps1` remain the structural and build gates.
