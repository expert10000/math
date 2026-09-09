# Volume VI — Mathematical Navigation

This sidecar records the internal prerequisite graph, standing notation, and major cross-volume
continuations for Volume VI.

## Internal prerequisite graph

### Classical affine geometry
- **VI/01 Algebraic Sets** is the classical affine starting point.
- **VI/02 Zariski Topology** depends on VI/01.
- **VI/03 Coordinate Rings** depends on VI/01–VI/02 and the ring/ideal material of Volume V.
- **VI/04 Morphisms of Affine Algebraic Sets** depends on VI/03.
- **VI/05 Irreducibility, Components and Connectedness** depends on VI/01–VI/04.

### Prime spectra
- **VI/06 Prime Ideals as Geometric Points** depends on V/02 and VI/03.
- **VI/07 Spectrum of a Ring** depends on VI/06.
- **VI/08 Basic Open Sets D(f)** depends on V/05–V/06 and VI/07.
- **VI/09 Generic and Closed Points** depends on VI/06–VI/08.
- **VI/10 Reduced and Nonreduced Geometry** depends on V/03 and VI/07–VI/09.
- **VI/11 Local Rings and Residue Fields** depends on V/08 and VI/07–VI/09.

### Sheaves
- **VI/12 Presheaves** starts the sheaf-theoretic language.
- **VI/13 Sheaves and Stalks** depends on VI/12.
- **VI/14 Sheafification** depends on VI/12–VI/13.
- **VI/15 Kernels, Images and Quotients of Sheaves** depends on VI/13–VI/14.
- **VI/16 Exact Sequences of Sheaves** depends on V/09, VI/13, and VI/15.
- **VI/17 Structure Sheaf** depends on V/06–V/08 and VI/07–VI/16.

### Schemes
- **VI/18 Affine Schemes** depends on VI/07–VI/17.
- **VI/19 Morphisms of Affine Schemes** depends on VI/18 and the contravariant ring–affine correspondence.
- **VI/20 Gluing Affine Schemes** depends on VI/13, VI/17–VI/19.
- **VI/21 Schemes and Their Points** depends on VI/18–VI/20.
- **VI/22 Open and Closed Subschemes** depends on VI/17–VI/21.

### Morphisms and families
- **VI/23 Fiber Products** depends on V/10 and VI/19–VI/22.
- **VI/24 Base Change** depends on V/11, V/14 and VI/23.
- **VI/25 Fibers and Geometric Fibers** depends on VI/23–VI/24.
- **VI/26 Finite-Type and Noetherian Morphisms** depends on V/15 and VI/19–VI/25.
- **VI/27 Integral Schemes and Function Fields** depends on V/19 and VI/10, VI/21, VI/26.
- **VI/28 Normalization** depends on V/20 and VI/27.

### Dimension and local geometry
- **VI/29 Krull Dimension** depends on V/02 and VI/07.
- **VI/30 Dimension of Schemes** depends on VI/21 and VI/29.
- **VI/31 Codimension** depends on VI/27, VI/29–VI/30.
- **VI/32 Tangent Spaces and Local Geometry** depends on VI/11, VI/21, VI/29–VI/31.

### Modules and projective geometry
- **VI/33 O_X-Modules and Quasi-Coherent Sheaves** depends on V/09–V/14 and VI/16–VI/21.
- **VI/34 Graded Rings** depends on Volume V ring/module algebra.
- **VI/35 Proj** depends on VI/34 and VI/07–VI/18.
- **VI/36 Projective Space** depends on VI/35.
- **VI/37 Projective Schemes** depends on VI/35–VI/36.
- **VI/38 Projective Morphisms and Closed Embeddings** depends on VI/22–VI/24 and VI/35–VI/37.

### Divisors and birational geometry
- **VI/39 Weil Divisors** depends on VI/27–VI/31; normality hypotheses must be stated where used.
- **VI/40 Cartier Divisors** depends on VI/17, VI/21, VI/33 and VI/39.
- **VI/41 Divisor Class Groups** depends on VI/39.
- **VI/42 Line Bundles and Picard Groups** depends on VI/33 and VI/40.
- **VI/43 Plane Cubics** depends on VI/36–VI/42.
- **VI/44 Cremona Transformations** depends on VI/36–VI/43.
- **VI/45 Blow-Ups** depends on VI/23–VI/24, VI/34–VI/38, and birational language from VI/39–VI/44.

### Sheaf cohomology
- **VI/46 Flabby Sheaves** depends on VI/13–VI/16.
- **VI/47 Cech Cohomology** depends on VI/12–VI/16.
- **VI/48 Exact Sequences and Cohomology** depends on V/27, VI/16, VI/46–VI/47.
- **VI/49 Basic Vanishing Results** depends on V/28, VI/33, VI/35–VI/38, VI/46–VI/48.

## Standing notation and conventions

Unless explicitly stated otherwise:

- \(k\) denotes a field; algebraic-closure hypotheses are stated where required.
- \(A,B\) denote commutative rings with identity.
- \(\operatorname{Spec}A\) is the prime spectrum.
- \(V(I)\) is the closed set of primes containing \(I\).
- \(D(f)=\operatorname{Spec}A\setminus V(f)\) is a distinguished open.
- \(\mathcal O_X\) is the structure sheaf.
- \(\mathcal O_{X,x}\) is the local ring at \(x\).
- \(\kappa(x)\) is the residue field at \(x\).
- \(\Gamma(U,\mathcal F)\) denotes sections of a sheaf over \(U\).
- For a morphism \(f:X\to Y\), \(f^{-1}\) is the inverse-image functor and \(f_*\) the direct image.
- \(\widetilde M\) denotes the quasi-coherent sheaf associated to a module on an affine scheme.
- \(\operatorname{Proj}S\) denotes Proj of a graded ring under the chapter's stated grading hypotheses.
- \(\mathcal O_X(n)\) denotes the standard twisting sheaf where defined.
- \(\operatorname{Div}(X)\), \(\operatorname{Cl}(X)\), and \(\operatorname{Pic}(X)\) denote divisor, class, and Picard groups with the hypotheses stated in their chapters.
- \(H^i(X,\mathcal F)\) denotes sheaf cohomology.

## Hypothesis discipline

The following words are structural hypotheses, not stylistic qualifiers, and must not be dropped:
`algebraically closed`, `Noetherian`, `locally Noetherian`, `integral`, `normal`,
`reduced`, `quasi-compact`, `quasi-separated`, `finite type`, `finite presentation`,
`proper/projective`, and `quasi-coherent`.

## Comes from

Volume V supplies the principal algebraic prerequisites: primes, localization, local rings,
exact sequences, tensor/base change, flatness, Noetherianity, support, integral dependence,
normalization, Tor/Ext and derived-functor language.

## Leads to

Volume VII uses schemes, tangent/local geometry and vector-bundle language; Volume VIII
reuses complexes and cohomological constructions. Later geometry should refer back to the
canonical scheme/sheaf conventions fixed here.

## Reading principle

Navigation never weakens theorem hypotheses. Classical affine-variety statements and
scheme-theoretic statements must remain distinguished, especially when field assumptions or
reducedness are involved.
