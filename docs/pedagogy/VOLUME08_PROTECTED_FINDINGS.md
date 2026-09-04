# Volume VIII — protected-source findings

Inspected baseline: `9e8346d067f47d6d49b1d3da228ad07386de6e93` (`expert10000/math`, `main`).

These observations are preserved as open findings. This package does not rewrite exercise statements, theorem statements, solutions, labels or existing outcomes. Source pairing can pass while mathematical/pedagogical readiness remains **HOLD**.

## VIII-P01 — 216 missing exercise statements

**BLOCKING_STATEMENTS**. `books/vol08_algebraic_topology/chapters/ch22_chain_homotopies/chapter.tex` — exr:viii22-01 through exr:viii30-24.

VIII/22--VIII/30 each contain 24 exercise bodies consisting only of "Exercise N". They are not mathematical questions. The new hints are inferred from the preserved solutions, explicitly marked as solution-derived in the bank metadata; they cannot make those statements complete. An independently approved statement-restoration patch is required before a pedagogy release.

## VIII-M01 — Deck transformations: domain of a lift

**CORRECTION_REQUIRED**. `books/vol08_algebraic_topology/chapters/ch11_lifting_properties/chapter.tex` — exr:viii11-24, solution.

The solution calls deck transformations lifts of the identity. A deck transformation h:E->E satisfies p h=p: it is a lift of p through p, and lies over the identity of the base. A lift of id_X through p is instead a section X->E. The original solution is preserved.

## VIII-M02 — Free-word reduction stops too early

**CORRECTION_REQUIRED**. `books/vol08_algebraic_topology/chapters/ch14_free_groups_and_covering_graphs/chapter.tex` — prob:viii14-01, solution.

The word a b a^{-1} a b^{-1} b reduces to a b. After the terminal b^{-1} b cancels, a^{-1} a still cancels. The assertion that no further inverse pair occurs is false. The original solution is preserved.

## VIII-M03 — Disk-pair connecting map at n=1

**HYPOTHESIS_REVIEW**. `books/vol08_algebraic_topology/chapters/ch19_relative_homology_and_exact_sequences/chapter.tex` — prob:viii19-06, solution.

The solution identifies both H_n(D^n,S^{n-1}) and H_{n-1}(S^{n-1}) with Z and calls the connecting map an isomorphism. This requires n>=2 in ordinary homology. For n=1 the target is H_0(S^0)=Z^2; the map has image the augmentation kernel. A reduced target also repairs the formulation.

## VIII-M04 — Reduced versus ordinary cone chains

**CONVENTION_REVIEW**. `books/vol08_algebraic_topology/chapters/ch24_mapping_cones_of_chain_maps/chapter.tex` — Topological versus algebraic cones.

Any direct equivalence between ordinary singular chains of the topological cone and the algebraic cone needs a reduced/augmented convention or an explicit degree-zero adjustment. The algebraic cone of the identity is acyclic, while a nonempty contractible topological cone still has ordinary H_0=Z. The added hints state this distinction; the source exposition is not rewritten.

## VIII-M05 — Real clutching classification needs an equivalence convention

**HYPOTHESIS_REVIEW**. `books/vol08_algebraic_topology/chapters/ch30_vector_bundles_and_clutching/chapter.tex` — Classification by clutching; Real line bundles over the circle.

The raw set [S^{n-1},O(k)] is not an unrestricted classification of unframed real bundles as written. At n=k=1, [S^0,O(1)] has four maps up to homotopy, whereas there are two real line bundles over S^1. Changes of hemisphere trivializations identify clutching data. Fix orientation/framing conventions or quotient by the appropriate changes of trivialization.

## VIII-M06 — Rank-one exception to the sphere obstruction formula

**HYPOTHESIS_REVIEW**. `books/vol08_algebraic_topology/chapters/ch32_sphere_bundles_and_euler_classes/chapter.tex` — exr:viii32-21, solution.

The displayed primary obstruction formula using pi_{r-1}(S^{r-1})=Z requires r>=2 in this form. For rank one the sphere fiber is S^0 and the obstruction discussion is different; an oriented real line bundle is trivial. The new hint makes the rank restriction explicit without modifying the solution.

## Release consequence

Do not proceed directly from this hint package to an I–VIII freeze. Restore the 216 statements in a separately authorized content patch, resolve the protected mathematical findings, review chapter outcomes, then rebuild and rerun independent volume/series gates. No freeze evidence is manufactured by this package.
