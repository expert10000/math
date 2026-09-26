# Companion Part III solution-quality audit

Audit target: `books/companion_problems_solutions/chapters/part03_volume_iii/chapter.tex`.

Repository snapshot reviewed:

- Part III chapter blob: `c9dae3cdccfa2371d134ad732a1eb6cb1b00e338`
- Part III migration ledger blob: `8518ce8057fc4affa98d8049cb2a5065e35b54ac`
- problems / paired solutions reviewed: **25 / 25**
- source-backed migrated solutions: **3**
- canonical authored solutions: **22**

This is an **editorial-quality audit**, not a coverage audit. The existing `25/25` pairing remains intact.

## Rubric

- `A_STRONG` — mathematically sound, substantially complete, and already suitable as a worked solution apart from copy-editing.
- `B_POLISH` — basically sound but too compressed, insufficiently explicit about hypotheses, or weakened by an overgrown/fragmentary statement.
- `C_REWRITE` — substantial mismatch, incompleteness, repetition, or weak pedagogy; rewrite before publication.
- `D_BLOCKING` — correctness or pairing defect that must be repaired before the Part III solution set can be considered editorially frozen.

Priorities: `P0` blocking correction, `P1` rewrite, `P2` polish/expansion, `P3` retain.

## Executive result

- `A_STRONG`: **11**
- `B_POLISH`: **8**
- `C_REWRITE`: **4**
- `D_BLOCKING`: **2**
- not yet publication-ready (`B+C+D`): **14 / 25**

The most important result is that **both blocking defects are source-backed migrations**, not later canonical-authored solutions. All three source-backed Part III solutions require intervention: `CP-III-0006` is blocking, `CP-III-0016` requires a rewrite, and `CP-III-0023` is blocking.

## Blocking corrections (`P0`)

### CP-III-0006

The reader-facing problem is overmerged: it begins with boundedness of distributional derivatives between Sobolev spaces and continues through approximation, heat, and Schrödinger material. The paired solution is essentially a Schrödinger mini-chapter, so it is not a valid matched solution to the full problem block. It also states

\[
\mathcal S(\mathbb R^n)=\bigcap_{s\in\mathbb R}H^s(\mathbb R^n),
\]

which is false. The right-hand side is the smooth Sobolev intersection `H^infinity`, which is strictly larger than Schwartz space.

### CP-III-0023

The mean-value-independence proof is invalid: multiplying

\[
\sum_{g\in\Lambda}\tau_g(\psi-\psi')=0
\]

by a compact cutoff does not imply `psi-psi'=0`. In addition, the problem defines

\[
\Lambda^*=\{\xi:g\cdot\xi\in2\pi\mathbb Z\ \forall g\in\Lambda\},
\]

but then asks for a basis satisfying `lambda*_j dot lambda_k = delta_jk` and claims that this basis itself generates `Lambda*`. A factor `2pi` is missing. The current solution notices the factor but "absorbs" it into the notation, which changes the stated definition instead of resolving the inconsistency.

## Rewrite queue (`P1`)

- `CP-III-0001` — proves only part of the long Baire-category example list; several genericity claims are merely asserted.
- `CP-III-0013` — long Fourier/tempered-distribution amalgam; the short solution does not work through the appended material.
- `CP-III-0014` — solves the ODE/Green-kernel portion but leaves the radial Fourier examples essentially unsolved.
- `CP-III-0016` — source-backed, mathematically useful but extremely repetitive and poorly aligned with the lettered tasks.

## Polish queue (`P2`)

- `CP-III-0004`, `CP-III-0005` — expand compressed Fourier derivations.
- `CP-III-0008` — state the duality/Fubini hypotheses carefully.
- `CP-III-0009` — make the singular-frequency and normalization issues explicit.
- `CP-III-0017` — show the finite-sum/simple-function Minkowski step explicitly and choose one proof route.
- `CP-III-0018` — clarify that this is figure interpretation rather than a conventional exercise.
- `CP-III-0020` — separate three analytic mechanisms and qualify critical singular extensions.
- `CP-III-0025` — restore the missing standard-mollifier hypotheses in the problem statement.

## Strong solutions (`P3`)

`CP-III-0002`, `0003`, `0007`, `0010`, `0011`, `0012`, `0015`, `0019`, `0021`, `0022`, `0024`.

## Theme summary

| Theme | A strong | B polish | C rewrite | D blocking |
|---|---:|---:|---:|---:|
| Measure and Integration | 3 | 2 | 2 | 0 |
| Fourier Analysis | 4 | 3 | 2 | 2 |
| Distribution Theory | 4 | 2 | 0 | 0 |
| Sobolev and PDE Methods | 0 | 1 | 0 | 0 |

## Full 25-problem audit

| ID | Provenance | Scope | Status | Priority | Main finding | Required action |
|---|---|---|---|---|---|---|
| `CP-III-0001` | CANONICAL_AUTHORED | SOURCE_DEFECT | **C_REWRITE** | P1 | The solution proves the Q/Cantor and countable-family finite-dimensional examples, but merely asserts the C([0,1]) genericity claims and omits the hyperplane case. It correctly notices that the literal union of all finite-dimensional subspaces is the whole space. | Rewrite as a structured example set; justify or explicitly cite every genericity claim, include the hyperplane case, and preserve the correction to the finite-dimensional wording. |
| `CP-III-0002` | CANONICAL_AUTHORED | CLEAN | **A_STRONG** | P3 | Correct Schwartz decay estimate, absolute convergence, and a controlling Schwartz seminorm prove continuity and temperedness. | Retain; copy-edit only. |
| `CP-III-0003` | CANONICAL_AUTHORED | CLEAN | **A_STRONG** | P3 | Generalized Holder and Minkowski are proved by standard complete arguments, including the zero case and endpoints. | Retain; optional endpoint notation polish. |
| `CP-III-0004` | CANONICAL_AUTHORED | OVERMERGED | **B_POLISH** | P2 | Covers Plancherel, double transform, truncation, derivatives, sinc, convolution, and Yukawa, but several nontrivial steps are compressed to one-line assertions. | Expand F^2, continuity of f*g, the sinc transform, and the radial Yukawa calculation. |
| `CP-III-0005` | CANONICAL_AUTHORED | CLEAN_MULTI_PART | **B_POLISH** | P2 | Correctly repairs the duplicated Fg typo in Plancherel and reaches the requested identities, but the long multi-part exercise is answered at summary level. | Expand each lettered subpart, especially sinc and convolution continuity, while retaining the source typo note. |
| `CP-III-0006` | SOURCE_BACKED | OVERMERGED | **D_BLOCKING** | P0 | The problem begins with D^alpha:H^{s+k}->H^s and then merges approximation, heat, and Schrodinger material. The paired solution is essentially a Schrodinger chapter and does not solve the full block. It also falsely states S(R^n)=intersection_s H^s; the intersection is H^infinity and is strictly larger than Schwartz. | Re-segment the overmerged problem into canonical exercises, then write matched solutions. Remove the false Schwartz/intersection claim. |
| `CP-III-0007` | CANONICAL_AUTHORED | CLEAN_EXAMPLE | **A_STRONG** | P3 | Heaviside and principal-value calculations are correct and proportionate. | Retain; copy-edit only. |
| `CP-III-0008` | CANONICAL_AUTHORED | EXPOSITORY | **B_POLISH** | P2 | Fenchel-Young to Holder is clear; the Minkowski integral proof invokes L^p duality and Fubini/Tonelli without stating the range and integrability assumptions carefully. | State 1<p<infinity for duality, handle p=1 separately, and state the hypotheses justifying integral interchange. |
| `CP-III-0009` | CANONICAL_AUTHORED | CLEAN_EXAMPLE | **B_POLISH** | P2 | The Laplace fundamental-solution formula is correct under the intended normalization, but the singular frequency k=0 is treated formally and omega_n is not defined explicitly. | Add a distributional justification at k=0 and define omega_n consistently. |
| `CP-III-0010` | CANONICAL_AUTHORED | BLOATED_BUT_CLEAR | **A_STRONG** | P3 | Rigorous density proof via simple functions, regularity, rational rectangles, and rational coefficients; it correctly avoids the source's invalid uniform-on-small-rectangles idea. | Retain; later trim the oversized problem body. |
| `CP-III-0011` | CANONICAL_AUTHORED | FIGURE_CONTEXT | **A_STRONG** | P3 | The change-of-variables proof of the translation phase and magnitude invariance is exactly proportionate to the short example. | Retain; restore a clearer example heading later. |
| `CP-III-0012` | CANONICAL_AUTHORED | SOURCE_DEFECT | **A_STRONG** | P3 | Correctly rejects the source claim sin(x)/(1+x^2) in Schwartz and proves temperedness from L^1/local integrability instead. | Retain the correction; later remove the false sentence from the reader-facing problem. |
| `CP-III-0013` | CANONICAL_AUTHORED | OVERMERGED | **C_REWRITE** | P1 | Long Fourier/tempered-distribution amalgam; the short solution lists standard identities but does not work through the appended distribution theory or many embedded claims. | Re-segment or rewrite into matched subparts; replace 'remaining conclusions follow from standard...' style with actual derivations. |
| `CP-III-0014` | CANONICAL_AUTHORED | OVERMERGED | **C_REWRITE** | P1 | The solution handles the -phi''+phi=f Green-kernel portion but leaves the substantial radial Fourier examples (ball, Gaussian, Yukawa) essentially unsolved. | Split radial Fourier material into separate problems or derive every displayed transform explicitly. |
| `CP-III-0015` | CANONICAL_AUTHORED | CLEAN_EXAMPLE | **A_STRONG** | P3 | Clean causal heat-kernel derivation by spatial Fourier transform and inversion. | Retain. |
| `CP-III-0016` | SOURCE_BACKED | OVERMERGED | **C_REWRITE** | P1 | Core p=1/Young/Holder/Minkowski chain is present, but the source-backed solution is extremely repetitive, mixes notes and examples with the requested proof, and is difficult to navigate. | Rewrite to follow parts (a)-(e) exactly once; keep one Young proof, one Holder normalization, one Minkowski derivation, and one controlled simple-to-general passage. |
| `CP-III-0017` | CANONICAL_AUTHORED | EXPOSITORY | **B_POLISH** | P2 | The duality proof is useful, but saying Minkowski is immediate for finite simple functions skips the finite-dimensional Minkowski step; two proof routes are mixed. | Choose one primary proof and explicitly show the finite-sum step if retaining the simple-function route. |
| `CP-III-0018` | CANONICAL_AUTHORED | FIGURE_NARRATIVE | **B_POLISH** | P2 | Accurately explains the figures, but functions as figure commentary rather than a worked mathematical solution. | Convert the statement into an explicit figure-interpretation task or add precise claims to prove. |
| `CP-III-0019` | CANONICAL_AUTHORED | BLOATED_BUT_FRONT_TASK_CLEAR | **A_STRONG** | P3 | Directly derives the Schrodinger multiplier, K_t, convolution formula, and the L^1-to-L^infinity dispersive bound. | Retain; later trim unrelated extra Sobolev exposition from the problem body. |
| `CP-III-0020` | CANONICAL_AUTHORED | OVERMERGED | **B_POLISH** | P2 | Coherently extracts three mechanisms from a long anthology, but the critical-singularity extension language is compressed and the three tasks should be separated. | Split into labeled subparts and qualify principal-value/finite-part extensions at critical singularities. |
| `CP-III-0021` | CANONICAL_AUTHORED | CLEAN_EXAMPLE | **A_STRONG** | P3 | Clearly verifies the three examples separating Baire category from Lebesgue measure. | Retain. |
| `CP-III-0022` | CANONICAL_AUTHORED | CLEAN | **A_STRONG** | P3 | Fourier multiplier, Green kernel, convolution representation, and uniqueness are all aligned with the ODE. | Retain. |
| `CP-III-0023` | SOURCE_BACKED | SOURCE_DEFECT | **D_BLOCKING** | P0 | Part (b) is invalid: sum_g tau_g(psi-psi')=0 does not imply psi-psi'=0 after multiplying by a cutoff. Part (c) is inconsistent with the 2pi definition of Lambda*: lambda*_j dot lambda_k=delta_jk generates the algebraic dual lattice, while the Fourier dual lattice is generated by 2pi times that basis. | Correct statement and solution together: prove mean-value independence using periodicity plus a partition-of-unity/cutoff argument, and distinguish the algebraic dual basis from the 2pi Fourier dual lattice; then recheck parts (e)-(f). |
| `CP-III-0024` | CANONICAL_AUTHORED | CLEAN | **A_STRONG** | P3 | Standard locally convex continuity argument is correct and the examples have valid Schwartz-seminorm bounds. | Retain. |
| `CP-III-0025` | CANONICAL_AUTHORED | FRAGMENT | **B_POLISH** | P2 | The solution is correct once the standard mollifier assumptions phi in C_c^infinity, phi>=0, integral phi=1 are supplied, but the problem begins mid-fragment. | Restore the missing opening hypotheses in the problem statement; then retain the solution with minor polish. |

## Recommended next editorial commits

1. `companion: repair blocking Part III solutions` — correct `CP-III-0006` and `CP-III-0023`, including statement segmentation/normalization where required.
2. `companion: rewrite weak Part III solutions` — rewrite `CP-III-0001`, `0013`, `0014`, `0016` to the canonical worked-solution style.
3. `companion: polish remaining Part III solutions` — expand/normalize the eight `B_POLISH` rows.
4. Re-run the Part III validator and full clean Companion build, then create a new Part III editorial freeze.
