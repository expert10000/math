# Volume VIII pedagogy — stage 1

- Pinned base: `9e8346d067f47d6d49b1d3da228ad07386de6e93`.
- Structural source checks: **PASS**.
- Pedagogy readiness: **HOLD** (not a release/freeze audit).
- Canonical PDF build: **NOT RUN by this audit**.
- I–VIII audit, release hashes, inventory refresh, tags and freeze: **NOT RUN**.

## Direct source counts

| Chapters | Problems | Exercises | Hints | Solutions | Curated hints applied |
|---:|---:|---:|---:|---:|---:|
| 35 | 742 | 840 | 840 | 1582 | 0 |

These counts were computed from the active TeX input graph, not copied from a release ledger.

## Blocking/review findings

Unresolved placeholder exercise/problem statements: **216**.
Chapters without a recognized outcome heading: **35**. This is a detection flag requiring review, not a claim that no learning outcome exists elsewhere.

**VIII-P01 — 216 missing exercise statements.** VIII/22--VIII/30 each contain 24 exercise bodies consisting only of "Exercise N". They are not mathematical questions. The new hints are inferred from the preserved solutions, explicitly marked as solution-derived in the bank metadata; they cannot make those statements complete. An independently approved statement-restoration patch is required before a pedagogy release. Source: `books/vol08_algebraic_topology/chapters/ch22_chain_homotopies/chapter.tex`, exr:viii22-01 through exr:viii30-24. Status: `OPEN_PROTECTED_CONTENT`.

**VIII-M01 — Deck transformations: domain of a lift.** The solution calls deck transformations lifts of the identity. A deck transformation h:E->E satisfies p h=p: it is a lift of p through p, and lies over the identity of the base. A lift of id_X through p is instead a section X->E. The original solution is preserved. Source: `books/vol08_algebraic_topology/chapters/ch11_lifting_properties/chapter.tex`, exr:viii11-24, solution. Status: `OPEN_PROTECTED_CONTENT`.

**VIII-M02 — Free-word reduction stops too early.** The word a b a^{-1} a b^{-1} b reduces to a b. After the terminal b^{-1} b cancels, a^{-1} a still cancels. The assertion that no further inverse pair occurs is false. The original solution is preserved. Source: `books/vol08_algebraic_topology/chapters/ch14_free_groups_and_covering_graphs/chapter.tex`, prob:viii14-01, solution. Status: `OPEN_PROTECTED_CONTENT`.

**VIII-M03 — Disk-pair connecting map at n=1.** The solution identifies both H_n(D^n,S^{n-1}) and H_{n-1}(S^{n-1}) with Z and calls the connecting map an isomorphism. This requires n>=2 in ordinary homology. For n=1 the target is H_0(S^0)=Z^2; the map has image the augmentation kernel. A reduced target also repairs the formulation. Source: `books/vol08_algebraic_topology/chapters/ch19_relative_homology_and_exact_sequences/chapter.tex`, prob:viii19-06, solution. Status: `OPEN_PROTECTED_CONTENT`.

**VIII-M04 — Reduced versus ordinary cone chains.** Any direct equivalence between ordinary singular chains of the topological cone and the algebraic cone needs a reduced/augmented convention or an explicit degree-zero adjustment. The algebraic cone of the identity is acyclic, while a nonempty contractible topological cone still has ordinary H_0=Z. The added hints state this distinction; the source exposition is not rewritten. Source: `books/vol08_algebraic_topology/chapters/ch24_mapping_cones_of_chain_maps/chapter.tex`, Topological versus algebraic cones. Status: `OPEN_PROTECTED_CONTENT`.

**VIII-M05 — Real clutching classification needs an equivalence convention.** The raw set [S^{n-1},O(k)] is not an unrestricted classification of unframed real bundles as written. At n=k=1, [S^0,O(1)] has four maps up to homotopy, whereas there are two real line bundles over S^1. Changes of hemisphere trivializations identify clutching data. Fix orientation/framing conventions or quotient by the appropriate changes of trivialization. Source: `books/vol08_algebraic_topology/chapters/ch30_vector_bundles_and_clutching/chapter.tex`, Classification by clutching; Real line bundles over the circle. Status: `OPEN_PROTECTED_CONTENT`.

**VIII-M06 — Rank-one exception to the sphere obstruction formula.** The displayed primary obstruction formula using pi_{r-1}(S^{r-1})=Z requires r>=2 in this form. For rank one the sphere fiber is S^0 and the obstruction discussion is different; an oriented real line bundle is trivial. The new hint makes the rank restriction explicit without modifying the solution. Source: `books/vol08_algebraic_topology/chapters/ch32_sphere_bundles_and_euler_classes/chapter.tex`, exr:viii32-21, solution. Status: `OPEN_PROTECTED_CONTENT`.

## Structural failures

None detected by the static source checks.

## Chapter inventory

| Chapter | Problems | Exercises | Hints | Solutions | Enriched | Placeholders |
|---|---:|---:|---:|---:|---:|---:|
| VIII/01 | 12 | 24 | 24 | 36 | 0 | 0 |
| VIII/02 | 12 | 24 | 24 | 36 | 0 | 0 |
| VIII/03 | 12 | 24 | 24 | 36 | 0 | 0 |
| VIII/04 | 20 | 24 | 24 | 44 | 0 | 0 |
| VIII/05 | 24 | 24 | 24 | 48 | 0 | 0 |
| VIII/06 | 20 | 24 | 24 | 44 | 0 | 0 |
| VIII/07 | 20 | 24 | 24 | 44 | 0 | 0 |
| VIII/08 | 20 | 24 | 24 | 44 | 0 | 0 |
| VIII/09 | 24 | 24 | 24 | 48 | 0 | 0 |
| VIII/10 | 24 | 24 | 24 | 48 | 0 | 0 |
| VIII/11 | 22 | 24 | 24 | 46 | 0 | 0 |
| VIII/12 | 24 | 24 | 24 | 48 | 0 | 0 |
| VIII/13 | 20 | 24 | 24 | 44 | 0 | 0 |
| VIII/14 | 20 | 24 | 24 | 44 | 0 | 0 |
| VIII/15 | 24 | 24 | 24 | 48 | 0 | 0 |
| VIII/16 | 22 | 24 | 24 | 46 | 0 | 0 |
| VIII/17 | 24 | 24 | 24 | 48 | 0 | 0 |
| VIII/18 | 24 | 24 | 24 | 48 | 0 | 0 |
| VIII/19 | 24 | 24 | 24 | 48 | 0 | 0 |
| VIII/20 | 22 | 24 | 24 | 46 | 0 | 0 |
| VIII/21 | 24 | 24 | 24 | 48 | 0 | 0 |
| VIII/22 | 24 | 24 | 24 | 48 | 0 | 24 |
| VIII/23 | 24 | 24 | 24 | 48 | 0 | 24 |
| VIII/24 | 22 | 24 | 24 | 46 | 0 | 24 |
| VIII/25 | 24 | 24 | 24 | 48 | 0 | 24 |
| VIII/26 | 22 | 24 | 24 | 46 | 0 | 24 |
| VIII/27 | 24 | 24 | 24 | 48 | 0 | 24 |
| VIII/28 | 20 | 24 | 24 | 44 | 0 | 24 |
| VIII/29 | 22 | 24 | 24 | 46 | 0 | 24 |
| VIII/30 | 22 | 24 | 24 | 46 | 0 | 24 |
| VIII/31 | 20 | 24 | 24 | 44 | 0 | 0 |
| VIII/32 | 20 | 24 | 24 | 44 | 0 | 0 |
| VIII/33 | 20 | 24 | 24 | 44 | 0 | 0 |
| VIII/34 | 20 | 24 | 24 | 44 | 0 | 0 |
| VIII/35 | 20 | 24 | 24 | 44 | 0 | 0 |

## Verification boundary

Source PASS does not certify mathematical correctness, PDF references, goal sufficiency, or release readiness. Known protected findings and unrun build/review gates keep readiness on HOLD.

The full JSON lists exact placeholder labels, goal evidence, pairing failures, input occurrences, static reference results and source hashes. These hashes are preservation evidence, not refreshed PDF/release hashes.

Static-analysis limits:

No additional dynamic-TeX limits detected; a real build is still required.
