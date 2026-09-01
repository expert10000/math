# SVG Visual Layer — VIII/28 through VIII/30

Six editable SVG teaching diagrams are supplied.

## VIII/28 — Cohomology
- `figures/ch28/ch28_chain_cochain_duality.svg`
  - boundary versus coboundary direction;
  - Hom dualization;
  - Kronecker evaluation pairing.
- `figures/ch28/ch28_annulus_connecting.svg`
  - mapped annulus/connecting support topic;
  - deformation retract to one boundary component;
  - cohomology LES fragment.

## VIII/29 — Cup Products
- `figures/ch29/ch29_cup_diagonal.svg`
  - cross product on \(X\times X\);
  - diagonal pullback;
  - \(a\smile b=\Delta^*(a\times b)\).
- `figures/ch29/ch29_torus_vs_wedge_ring.svg`
  - same Betti numbers for torus and wedge model;
  - nonzero torus product versus vanishing mixed wedge products.

## VIII/30 — Vector Bundles and Clutching
- `figures/ch30/ch30_bundle_transition.svg`
  - local trivializations;
  - transition function \(g_{ij}(x)\);
  - Möbius sign-twist inset.
- `figures/ch30/ch30_clutching_sphere.svg`
  - northern/southern trivial hemisphere bundles;
  - equatorial clutching map \(S^{n-1}\to O(k)\);
  - global twist determined by homotopy class.

## Build policy

The SVG files are intentionally tracked as editable source assets but are not
required by `book.tex`. This keeps the standard PDF build independent of
Inkscape, shell escape, and SVG-specific LaTeX packages.

A later visual-harmonization pass can convert/embed them consistently across
Volume VIII without changing their mathematical ownership.
