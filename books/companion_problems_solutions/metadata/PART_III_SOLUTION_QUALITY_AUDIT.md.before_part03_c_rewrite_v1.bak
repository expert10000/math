# Companion Part III solution-quality audit

Status after the blocking-repair pass.

- problems / paired solutions: **25 / 25**
- source-backed migrated solutions: **3**
- canonical authored solutions: **22**

## Rubric

- `A_STRONG` — mathematically sound, substantially complete, and suitable as a worked solution apart from copy-editing.
- `B_POLISH` — basically sound but still needs expansion, hypothesis cleanup, or statement normalization.
- `C_REWRITE` — substantial mismatch, incompleteness, repetition, or weak pedagogy; rewrite before publication.
- `D_BLOCKING` — correctness or pairing defect that blocks editorial freeze.

## Current result

- `A_STRONG`: **13**
- `B_POLISH`: **8**
- `C_REWRITE`: **4**
- `D_BLOCKING`: **0**
- still needing editorial work (`B+C`): **12 / 25**

The previous `P0` blocking queue is now empty.

## Blocking repairs completed

### CP-III-0006

The migration had overcaptured a source range: the actual exercise item is the Sobolev derivative task at `imports/Downloads/theory-of-analysis-FD2.tex` lines 4927--4932. The following `Theory and Solutions`, Heat Equation 5.9, and Schrödinger 5.10 material belonged to later source sections and had been absorbed into the same reader-facing problem. The canonical problem/solution pair is now narrowed to the actual exercise item and solved by the Fourier multiplier estimate.

This also removes the false sentence

\[
\mathcal S(\mathbb R^n)=\bigcap_{s\in\mathbb R}H^s(\mathbb R^n),
\]

which had survived inside the overmerged solution. In general the Sobolev intersection is `H^infinity`, strictly larger than Schwartz space.

### CP-III-0023

The source's periodic-distribution exercise is retained, but two mathematical defects are corrected explicitly:

1. Mean-value independence is proved using periodicity and the locally finite partition of unity.
2. The algebraic dual basis `mu_j dot lambda_k = delta_jk` is distinguished from the Fourier dual basis `lambda_j^*=2pi mu_j`, for which `lambda_j^* dot lambda_k=2pi delta_jk` and which genuinely generates the stated `Lambda^*`.

The canonical proof also establishes that every periodic distribution is tempered before applying the Fourier transform.

## Remaining rewrite queue (`P1`)

- `CP-III-0001` — several Baire-category genericity assertions are still asserted rather than justified.
- `CP-III-0013` — long Fourier/tempered-distribution amalgam remains incompletely solved.
- `CP-III-0014` — radial Fourier examples remain substantially unsolved.
- `CP-III-0016` — source-backed solution remains repetitive and poorly aligned with the lettered tasks.

## Remaining polish queue (`P2`)

- `CP-III-0004`, `0005`, `0008`, `0009`, `0017`, `0018`, `0020`, `0025`.

## Strong solutions (`P3`)

`CP-III-0002`, `0003`, `0006`, `0007`, `0010`, `0011`, `0012`, `0015`, `0019`, `0021`, `0022`, `0023`, `0024`.

## Theme summary

| Theme | A strong | B polish | C rewrite | D blocking |
|---|---:|---:|---:|---:|
| Measure and Integration | 3 | 2 | 2 | 0 |
| Fourier Analysis | 6 | 3 | 2 | 0 |
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
| `CP-III-0006` | SOURCE_BACKED | CANONICAL_RECONCILED | **A_STRONG** | P3 | Blocking overmerge repaired. The canonical reader-facing problem is now narrowed to the actual source exercise item at theory-of-analysis-FD2.tex L4927-L4932: boundedness of D^alpha:H^{s+k}->H^s. The paired solution now proves exactly that Fourier-multiplier estimate. The accidentally captured heat/Schrodinger material and the false Schwartz=intersection_s H^s claim are removed from this canonical pair. | Retain; regression validator protects the narrowed statement and derivative estimate. |
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
| `CP-III-0023` | SOURCE_BACKED | SOURCE_CORRECTED | **A_STRONG** | P3 | Blocking defects repaired. Mean-value independence is now proved by periodicity plus the partition of unity, not by the invalid cutoff argument. The algebraic dual basis mu_j dot lambda_k=delta_jk is distinguished from the Fourier dual basis lambda_j^*=2pi mu_j, so Lambda^* is generated with the correct 2pi normalization. The proof also establishes that periodic distributions are tempered before taking Fourier transforms. | Retain; regression validator protects the partition-of-unity proof and 2pi dual-lattice normalization. |
| `CP-III-0024` | CANONICAL_AUTHORED | CLEAN | **A_STRONG** | P3 | Standard locally convex continuity argument is correct and the examples have valid Schwartz-seminorm bounds. | Retain. |
| `CP-III-0025` | CANONICAL_AUTHORED | FRAGMENT | **B_POLISH** | P2 | The solution is correct once the standard mollifier assumptions phi in C_c^infinity, phi>=0, integral phi=1 are supplied, but the problem begins mid-fragment. | Restore the missing opening hypotheses in the problem statement; then retain the solution with minor polish. |

## Recommended next editorial commit

`companion: rewrite weak Part III solutions` — rewrite `CP-III-0001`, `0013`, `0014`, and `0016` to the canonical worked-solution standard.
