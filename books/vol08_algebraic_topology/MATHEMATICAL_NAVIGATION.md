# Volume VIII — Mathematical Navigation

This sidecar records the **internal prerequisite graph**, the standing notation/conventions, and the main cross-volume bridges for **Volume VIII — Algebraic Topology**.

Editorial navigation does not weaken theorem hypotheses: each chapter remains responsible for stating the precise assumptions of the result it uses.

## Internal prerequisite graph

### Homotopy and cell constructions

- **VIII/01 Homotopies of Maps** is the starting point.
- **VIII/02 Homotopy Equivalence and Contractibility** depends on VIII/01.
- **VIII/03 Degree of Maps** depends on VIII/01–VIII/02 plus orientation ideas from Volume VII.
- **VIII/04 Spheres and Antipodal Maps** depends on VIII/03.
- **VIII/05 Cell Attachments** depends on quotient spaces and VIII/01–VIII/02.
- **VIII/06 CW Complexes** depends on VIII/05.
- **VIII/07 Mapping Cones** depends on VIII/01, VIII/05–VIII/06.
- **VIII/08 Homotopic Attaching Maps** depends on VIII/05–VIII/07.

### Fundamental groups and coverings

- **VIII/09 Paths and Fundamental Groups** depends on VIII/01.
- **VIII/10 Covering Spaces** depends on VIII/09 and local topology.
- **VIII/11 Lifting Properties** depends on VIII/10.
- **VIII/12 Deck Transformations and Group Actions** depends on VIII/09–VIII/11.
- **VIII/13 SU(2) to SO(3)** depends on VIII/10–VIII/12 and Lie-group background.
- **VIII/14 Free Groups and Covering Graphs** depends on VIII/09–VIII/12.

### Simplicial, singular and cellular homology

- **VIII/15 Simplicial Complexes** provides the combinatorial model.
- **VIII/16 Chain Complexes** provides the algebraic language.
- **VIII/17 Simplicial and Singular Homology** depends on VIII/15–VIII/16.
- **VIII/18 Cellular Homology** depends on VIII/06 and VIII/16–VIII/17.
- **VIII/19 Relative Homology and Exact Sequences** depends on VIII/16–VIII/17.
- **VIII/20 Homotopy Invariance** depends on VIII/01 and VIII/16–VIII/19.
- **VIII/21 Euler Characteristic** depends on VIII/06, VIII/17–VIII/20 and finiteness hypotheses.
- **VIII/22 Chain Homotopies** depends on VIII/16 and supports the algebra behind VIII/20.
- **VIII/23 Chain Contractions** depends on VIII/22.
- **VIII/24 Mapping Cones of Chain Maps** depends on VIII/16, VIII/19 and VIII/22.

### Coefficients, products and cohomology

- **VIII/25 Homology with Coefficients** depends on VIII/16–VIII/19 and tensor products.
- **VIII/26 The Universal Coefficient Theorem** depends on VIII/25 and `Hom`/`Ext` or tensor/`Tor`, according to the formulation.
- **VIII/27 Products and the Künneth Theorem** depends on VIII/25–VIII/26 and tensor/`Tor`.
- **VIII/28 Cohomology** depends on VIII/16–VIII/19 and dual complexes.
- **VIII/29 Cup Products** depends on VIII/28 and product/diagonal constructions.

### Bundles, characteristic classes and duality

- **VIII/30 Vector Bundles and Clutching** depends on VII/07 and VIII/01–VIII/06.
- **VIII/31 Thom Classes** depends on VIII/28–VIII/30 and bundle orientations.
- **VIII/32 Sphere Bundles and Euler Classes** depends on VIII/30–VIII/31.
- **VIII/33 Poincaré Duality** depends on VII/10, VIII/19, VIII/28–VIII/29, orientation and the fundamental class.
- **VIII/34 Intersection Forms** depends on VIII/29 and VIII/33.
- **VIII/35 Lefschetz Theory** depends on VIII/20–VIII/21, VIII/28–VIII/29 and the trace on induced homology maps.

## Standing notation

Unless a chapter explicitly states otherwise:

- `X,Y,Z` denote topological spaces.
- `I=[0,1]` is the unit interval.
- `f \simeq g` denotes homotopy of maps; based/relative homotopy is stated when required.
- `[X,Y]` denotes homotopy classes only after the based/unbased convention is specified.
- `\pi_1(X,x_0)` is the fundamental group at basepoint `x_0`.
- `p:E\to B` denotes a covering map or bundle projection according to context.
- `C_n`, `\partial_n`, `Z_n`, `B_n`, `H_n` denote chains, boundary, cycles, boundaries and homology.
- `\widetilde H_n` denotes reduced homology.
- `H_n(X,A;G)` denotes relative homology with coefficients `G`.
- `C^n`, `\delta`, `H^n` denote cochains, coboundary and cohomology.
- `\smile` and `\frown` denote cup and cap products.
- `\otimes`, `\operatorname{Tor}`, `\operatorname{Hom}`, and `\operatorname{Ext}` retain their algebraic meanings from Volume V.
- `[M]` denotes the fundamental class of an oriented manifold when it exists with the chosen coefficients.
- `u` denotes a Thom class when one has been chosen.
- `e(E)` denotes the Euler class of an oriented real vector bundle `E`.
- `Q_M` denotes an intersection pairing/form when its domain and coefficients have been fixed.
- `L(f)` denotes the Lefschetz number.

## Global conventions

### Homology and cohomology

Singular homology with integer coefficients is the default unless a chapter names a different theory or coefficient object. Reduced groups carry a tilde. Boundary maps lower degree by one; coboundary maps raise degree by one.

### Exact sequences

Every displayed exact sequence must make the direction and degree of its connecting map visible. Natural exact sequences are treated as natural transformations, not merely as abstract group isomorphisms.

### Coefficients

Tensor, `Tor`, `Hom`, and `Ext` terms are not interchangeable. A split short exact sequence arising from a universal-coefficient or Künneth theorem is called **noncanonical** unless a canonical splitting is actually supplied.

### Products

Cup and cap products use one fixed grading/sign convention across VIII/28–VIII/35. Graded commutativity always includes the Koszul sign.

### Orientation

Thom classes, Euler classes, Poincaré duality and intersection forms use compatible orientation/coefficient conventions. Integral statements requiring orientability are not silently transferred to the nonorientable case.

## Comes from

- **II/06 — Compactness** → **VIII/02 — Homotopy Equivalence and Contractibility** — compactness reappears in global topological arguments and later fixed-point hypotheses.
- **IV/23 — Covering Maps and Monodromy** → **VIII/10 — Covering Spaces** — analytic monodromy passes to general covering theory.
- **V/22 — Chain Complexes** → **VIII/16 — Chain Complexes** — chain complexes become the algebraic engine of homology.
- **V/23 — Free Resolutions** → **VIII/26 — The Universal Coefficient Theorem** — resolutions underlie derived coefficient terms.
- **V/26 — The Tor Functor** → **VIII/27 — Products and the Künneth Theorem** — `Tor` is the correction term in Künneth phenomena.
- **VII/01 — Topological Manifolds** → **VIII/01 — Homotopies of Maps**.
- **VII/07 — Vector Bundles** → **VIII/30 — Vector Bundles and Clutching**.
- **VII/09 — Differential Forms** → **VIII/28 — Cohomology** — differential forms provide geometric cohomological intuition.
- **VII/10 — Orientation and Integration** → **VIII/33 — Poincaré Duality**.
- **VII/20–VII/30 — Riemannian/Lorentzian manifolds** provide manifold examples whose global invariants are studied here.

## Leads to

Volume VIII is the terminal volume of the current eight-volume canonical sequence, so there is no later volume dependency. Its outgoing role is integrative: homotopy, homology, cohomology, bundles, characteristic classes, duality, intersection theory and fixed-point theory provide the global language used across geometry, topology and mathematical physics.

## Reading principle

Use the prerequisite graph to decide what must be known before a chapter. Use the cross-volume arrows for conceptual continuity. Neither substitutes for the precise local hypotheses of a theorem.
