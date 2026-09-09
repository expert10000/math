# Volume VIII mathematical review — VIII/01–VIII/35

Pinned base: `93a9802fd0b9085db57562e15941a42874b6c3d7`

This is a conservative post-freeze professional review of **Volume VIII — Algebraic Topology**. The canonical 35-chapter corpus, reconstruction/reconciliation data, figures, and freeze manifest are preserved. Chapter source is to be edited only when a concrete mathematical defect is demonstrated; global search-and-replace rewriting of theorem prose is prohibited.

## Review contract

Every theorem, proof, example, exercise, hint, and solution is reviewed with the following invariants in mind:

- distinguish based from unbased homotopy data;
- distinguish homotopy equivalence from homeomorphism and deformation retraction;
- retain connectedness, local connectedness, semilocal simple-connectivity, compactness, finiteness, orientability, and coefficient hypotheses where required;
- keep boundary/coboundary degree and sign conventions fixed;
- distinguish reduced from unreduced homology;
- distinguish absolute from relative groups and maps of pairs;
- state exact sequences in the correct direction with the correct connecting morphism;
- state naturality rather than merely group-level isomorphism when the theorem is natural;
- state when splittings are noncanonical;
- preserve torsion terms in universal-coefficient and Künneth statements;
- keep cup/cap signs and grading conventions consistent;
- distinguish existence implications from converses for characteristic classes;
- state Poincaré-duality, intersection-form, and Lefschetz hypotheses explicitly.

## VIII/01–VIII/08 — homotopy, degree and cell attachments

Audit:

- continuity of homotopies and endpoint conventions;
- relative and based homotopies where used;
- homotopy equivalence versus strong/deformation retract;
- contractibility and its consequences without confusing them with simple connectedness in the absence of hypotheses;
- degree of maps: domain/codomain dimension, orientation, normalization, multiplicativity and homotopy invariance;
- antipodal-map degree and parity;
- quotient-space topology in cell attachments;
- dependence of attached-cell homotopy type on the homotopy class of the attaching map;
- mapping-cone convention and the special case of nullhomotopic maps.

## VIII/09–VIII/14 — fundamental groups and covering spaces

Audit:

- basepoints and change-of-basepoint isomorphisms;
- path concatenation order;
- van Kampen hypotheses where invoked;
- covering-space definition and evenly covered neighborhoods;
- unique path and homotopy lifting;
- classification of connected coverings only under the stated local hypotheses;
- subgroup correspondence up to conjugacy for unbased classification;
- regular/normal coverings versus arbitrary coverings;
- deck group formula: `Deck(p) ≅ N(H)/H` in general and `π_1(B)/H` only when `H` is normal;
- the double cover `SU(2) -> SO(3)`;
- free groups and covering graphs, including connectedness and chosen base vertex.

## VIII/15–VIII/24 — chain complexes and homology

Audit:

- orientation/sign convention for simplicial boundaries;
- `∂²=0` calculations;
- chain maps and induced maps on homology;
- simplicial versus singular homology comparison hypotheses;
- cellular chain groups and cellular boundary maps;
- relative chain complex `C_*(X,A)=C_*(X)/C_*(A)`;
- long exact sequence of a pair and the direction/degree of the connecting map;
- homotopy invariance and the prism/chain-homotopy operator;
- Euler characteristic: finite CW or finiteness hypotheses whenever alternating sums are used;
- chain homotopies and chain contractions;
- algebraic mapping-cone signs and the exact sequence induced by a cone.

## VIII/25–VIII/29 — coefficients, UCT, Künneth and cohomology

Audit:

- coefficient group/ring specified rather than silently changed;
- tensor-product and `Tor` terms;
- hypotheses under which the homology Künneth short exact sequence is stated;
- any splitting declared noncanonical unless a canonical splitting is actually constructed;
- Universal Coefficient Theorem stated in the appropriate homology/cohomology form;
- `Hom`/`Ext` versus tensor/`Tor` kept distinct;
- cochain differential raises degree;
- reduced cohomology conventions;
- cup-product grading and the sign in graded commutativity;
- naturality of cup products;
- cohomology-ring computations distinguished from additive-group computations.

## VIII/30–VIII/32 — vector bundles, Thom and Euler classes

Audit:

- rank and structure group of bundles;
- clutching maps and the precise sphere/base-space classification being used;
- homotopy classes of clutching maps with based/unbased distinctions when relevant;
- orientation of a real vector bundle relative to coefficient ring;
- Thom class in the correct relative/compactly-supported cohomology group;
- degree shift in the Thom isomorphism;
- Euler class as pullback of the Thom class by the zero section;
- a nowhere-zero section implies vanishing Euler class;
- do **not** state the converse without the additional obstruction-theoretic hypotheses under which it holds;
- sphere-bundle/Gysin constructions use the same orientation and coefficient conventions.

## VIII/33 — Poincaré duality

Audit:

- dimension `n`;
- closed/compact versus noncompact and boundary cases;
- orientability and coefficient ring;
- fundamental class `[M]`;
- cap-product degree shift;
- duality map direction;
- reduced/relative variants for manifolds with boundary;
- local-coefficient caveat for nonorientable manifolds;
- naturality and sign conventions for cap products.

## VIII/34 — intersection forms

Audit:

- closed oriented manifold hypotheses;
- correct middle dimension;
- quotient by torsion when an integral free pairing is claimed;
- symmetry/skew-symmetry determined by degree parity;
- unimodularity only under the appropriate Poincaré-duality hypotheses;
- four-manifold specialization separated from general `2k`-manifold statements;
- geometric intersections require transversality/orientation conventions.

## VIII/35 — Lefschetz theory

Audit:

- definition `L(f)=Σ_i (-1)^i tr(f_*|H_i)` over a coefficient field or in a setting where the trace is defined;
- finiteness hypotheses on homology;
- Lefschetz fixed-point theorem: `L(f) != 0` implies a fixed point under the stated compact-polyhedron/ENR/CW hypotheses;
- do not assert the converse;
- local fixed-point index only under the conditions in which it is defined;
- graph/diagonal intersections use compatible orientation and transversality conventions.

## Standing conventions that must remain globally consistent

1. path-concatenation order;
2. based versus unbased homotopy notation;
3. singular homology as the default unless another theory is named;
4. integer coefficients as the default unless another coefficient object is named;
5. reduced homology notation `\widetilde H_*`;
6. boundary maps lower degree and coboundary maps raise degree;
7. mapping-cone sign convention;
8. connecting-homomorphism degree;
9. cup/cap product sign convention;
10. orientation conventions for Thom classes and Poincaré duality;
11. intersection-product orientation/sign convention;
12. Lefschetz-number trace convention.

## Outcome of this pass

The review is intentionally non-destructive. The existing freeze manifest remains the authority for frozen chapter/book/figure/reconciliation sources. This professional-review layer may add or replace editorial navigation/review sidecars without altering those frozen mathematical-source hashes.

Any later chapter-local mathematical correction must be made explicitly and must trigger freeze-manifest regeneration rather than silently invalidating the frozen release.
