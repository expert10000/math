# Volume VII — Mathematical Navigation

This sidecar records the internal prerequisite graph, standing notation and conventions, and the principal cross-volume transitions for Volume VII.

## Internal prerequisite graph

### Smooth manifolds
- **VII/01 Topological Manifolds** is the topological starting point.
- **VII/02 Smooth Structures and Atlases** depends on VII/01.
- **VII/03 Smooth Maps and Diffeomorphisms** depends on VII/01–VII/02 and multivariable differentiability.
- **VII/04 Tangent Spaces** depends on VII/03 and linear algebra.
- **VII/05 Cotangent Spaces** depends on VII/04 and dual spaces.
- **VII/06 Submanifolds and Products** depends on VII/03–VII/05 and inverse/implicit-function principles.

### Bundles, forms and integration
- **VII/07 Vector Bundles** depends on VII/01–VII/06 and fiberwise linear algebra.
- **VII/08 Principal and Frame Bundles** depends on VII/07 and group actions.
- **VII/09 Differential Forms** depends on VII/04–VII/05 and multilinear/exterior algebra.
- **VII/10 Orientation and Integration** depends on VII/09 and manifold orientation.
- **VII/11 Stokes' Theorem** depends on VII/09–VII/10 and manifolds with boundary.

### Curves and surfaces
- **VII/12 Regular Curves** depends on VII/03–VII/04.
- **VII/13 Frenet Frames, Curvature and Torsion** depends on VII/12 and Euclidean inner-product geometry.
- **VII/14 Regular Surfaces** depends on VII/03–VII/06.
- **VII/15 First and Second Fundamental Forms** depends on VII/14.
- **VII/16 The Gauss Map and Shape Operator** depends on VII/14–VII/15.
- **VII/17 Principal, Gaussian and Mean Curvature** depends on VII/15–VII/16.
- **VII/18 Ruled and Developable Surfaces** depends on VII/12–VII/17.
- **VII/19 Minimal Surfaces** depends on VII/14–VII/17.

### Riemannian geometry
- **VII/20 Riemannian Metrics** depends on VII/04–VII/07.
- **VII/21 Connections** depends on VII/07 and VII/20.
- **VII/22 The Levi–Civita Connection** depends on VII/20–VII/21.
- **VII/23 Geodesics** depends on VII/22.
- **VII/24 Parallel Transport** depends on VII/21–VII/23.
- **VII/25 Holonomy** depends on VII/24 and loop/fundamental-group intuition.
- **VII/26 The Riemann Curvature Tensor** depends on VII/21–VII/24.
- **VII/27 Ricci and Scalar Curvature** depends on VII/26.
- **VII/28 Weyl Curvature** depends on VII/26–VII/27 and dimension-sensitive tensor decompositions.

### Lorentzian geometry
- **VII/29 Indefinite Metrics** depends on VII/20–VII/22.
- **VII/30 Riemannian versus Lorentzian Geometry** depends on VII/23, VII/26–VII/29.

### Hyperbolic geometry
- **VII/31 Hyperbolic Plane Models** depends on VII/20, VII/23 and constant-curvature geometry.
- **VII/32 The Poincaré Metric** depends on VII/31.
- **VII/33 Möbius Transformations and PSL(2,R)** depends on VII/31–VII/32 and Volume IV complex analysis.
- **VII/34 Hyperbolic Isometries** depends on VII/31–VII/33.
- **VII/35 Fuchsian Groups** depends on VII/33–VII/34 and discrete group actions.
- **VII/36 Hyperbolic Three-Space and PSL(2,C)** depends on VII/31–VII/35.
- **VII/37 Kleinian Groups and Boundary Geometry** depends on VII/36 and the discrete-action language of VII/35.

### Computational geometry
- **VII/38 Discrete Geodesic Problems** depends on VII/14–VII/17 and VII/23.
- **VII/39 Graph and Exact Mesh Geodesics** depends on VII/38 plus graph algorithms and polyhedral geometry.
- **VII/40 The Heat Method** depends on VII/20–VII/27, VII/38, and PDE/weak-derivative material from Volume III.
- **VII/41 Discrete Laplacians** depends on VII/15–VII/17, VII/20–VII/27, and triangulated-mesh geometry.
- **VII/42 Curvature Lines, Ridges and Valleys** depends on VII/16–VII/17 and VII/41.

## Standing notation and conventions

Unless a chapter explicitly states otherwise:

- `M,N` denote smooth manifolds.
- `p in M`; `T_pM` and `T_p^*M` denote tangent and cotangent spaces.
- `TM`, `T^*M` denote tangent and cotangent bundles.
- `dF_p` denotes the differential of a smooth map at `p`.
- `Omega^k(M)` denotes smooth differential `k`-forms; `d` is the exterior derivative and `wedge` the exterior product.
- `g` denotes a Riemannian or explicitly specified pseudo-Riemannian metric.
- `nabla` denotes a connection; when used without qualification in the Riemannian part it is the Levi–Civita connection.
- `gamma` denotes a curve or geodesic as context requires.
- `exp_p` is the exponential map at `p` on its natural domain.
- `R(X,Y)Z` denotes the Riemann curvature operator with the sign convention fixed in the curvature chapters.
- `Ric`, `Scal`, and `K(sigma)` denote Ricci, scalar, and sectional curvature.
- `S` denotes the shape operator; its sign must remain consistent with the second fundamental form.
- `k_1,k_2`, `K`, and `H` denote principal, Gaussian, and mean curvature under the chapter's fixed normalization.
- Hyperbolic metrics are normalized to sectional curvature `-1` unless explicitly rescaled.
- `PSL(2,R)` and `PSL(2,C)` denote the projective special linear groups acting in the standard hyperbolic models.
- `Delta` denotes the Laplace–Beltrami/discrete Laplacian with the sign convention stated before computational use.
- For meshes, `M` may also denote a mass matrix only when clearly distinguished typographically from a manifold.
- `d_M` denotes intrinsic distance when that notation is introduced; graph distance and polyhedral exact distance must be named separately.

## Convention discipline

The following are structural conventions, not cosmetic notation:

1. boundary orientation in Stokes' theorem;
2. sign of the shape operator;
3. normalization of mean curvature;
4. sign of the Riemann tensor and resulting Ricci contraction;
5. Lorentzian signature convention;
6. sign of the Laplace–Beltrami operator;
7. hyperbolic curvature normalization;
8. exact versus approximate terminology for mesh algorithms.

Any chapter that changes one of these conventions must state the change locally and translate formulas accordingly.

## Comes from

- **I/03 — Bases and Dimension** → **VII/04 — Tangent Spaces** — bases and dimension become the local linear language of tangent spaces.
- **I/05 — Linear Transformations** → **VII/03 — Smooth Maps and Diffeomorphisms** — linear maps model differentials.
- **I/14 — Gram–Schmidt and Orthogonal Projection** → **VII/08 — Principal and Frame Bundles** — orthogonality supports frame and metric constructions.
- **II/04 — Open and Closed Sets** and **II/05 — Metric Spaces and Continuity** → **VII/01 — Topological Manifolds**.
- **II/08 — Differentiability in Several Variables** → **VII/03 — Smooth Maps and Diffeomorphisms**.
- **II/09 — Inverse and Implicit Function Principles** → **VII/06 — Submanifolds and Products**.
- **III/20 — Weak Derivatives** → **VII/40 — The Heat Method**.
- **IV/27 — Lattices and Complex Tori** → **VII/07 — Vector Bundles**.
- **V/13 — Free and Projective Modules** → **VII/07 — Vector Bundles**.
- **VI/32 — Tangent Spaces and Local Geometry** provides an algebraic-geometric counterpart to VII/04 and VII/20.

## Leads to

- **VII/01 — Topological Manifolds** → **VIII/01 — Homotopies of Maps**.
- **VII/07 — Vector Bundles** → **VIII/30 — Vector Bundles and Clutching**.
- **VII/09 — Differential Forms** → **VIII/28 — Cohomology**.
- **VII/10 — Orientation and Integration** → **VIII/33 — Poincaré Duality**.
- Riemannian curvature, bundles, and characteristic geometric constructions provide the geometric intuition used throughout later topology.

## Numerical geometry and verification policy

Volume VII is the most computationally numerical volume in the series so far.
Its exact differential-geometric definitions remain the reference objects, but
coordinate formulas and mesh algorithms require explicit conditioning,
discretization, and residual diagnostics.

The principal hotspots are:

- **VII/20 Riemannian Metrics:** a positive-definite metric can have a badly
  conditioned coordinate matrix.  Report coordinate conditioning without
  confusing chart pathology with intrinsic degeneracy.
- **VII/23 Geodesics:** numerical ODE integration should track step refinement,
  ODE residuals, constant-speed drift, chart conditioning, and any embedded
  constraint error.  Solving the geodesic equation does not certify global
  minimizing behavior.
- **VII/38 Discrete Geodesic Problems:** benchmarks must state whether the
  reference is graph distance, exact polyhedral distance, or a smooth-surface
  distance, and should measure path as well as scalar distance error.
- **VII/40 The Heat Method:** distinguish sparse-solver residuals from mesh,
  finite-element, time-scale, normalization, and reconstruction errors.
- **VII/41 Discrete Laplacians:** verify symmetry, null modes, masses,
  generalized-eigenpair residuals, and \(M\)-orthogonality before interpreting
  discrete spectra; discrete residual accuracy is not continuum convergence.
- **VII/42 Curvature Lines, Ridges and Valleys:** eigengap, local-fit
  conditioning, scale dependence, line-field ambiguity, and multiscale
  persistence should feed explicit confidence diagnostics.

For computational geometry, reproducible claims should state the mesh/model,
boundary convention, discretization, normalization/sign convention, solver
tolerance, and comparison norm.  Exact smooth geometry, discrete geometry, and
floating-point solution error are separate layers.

## Reading principle

The dependency graph records the intended mathematical order, while the cross-volume arrows are curated conceptual bridges. Navigation never weakens theorem hypotheses or silently changes sign/normalization conventions.
