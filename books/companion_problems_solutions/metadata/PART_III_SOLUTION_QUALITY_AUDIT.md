# Companion Part III solution-quality audit

Status after the four `C_REWRITE` repairs.

- problems / paired solutions: **25 / 25**
- source-backed migrated solutions: **3**
- canonical authored solutions: **22**

## Current result

- `A_STRONG`: **17**
- `B_POLISH`: **8**
- `C_REWRITE`: **0**
- `D_BLOCKING`: **0**
- still needing editorial polish: **8 / 25**

The blocking and rewrite queues are now empty. The remaining work is the eight `B_POLISH` rows.

## Rewrites completed

### CP-III-0001

The Baire-category example set is now genuinely worked. The reader-facing statement explicitly corrects the source's false literal consequence about points lying in no finite-dimensional subspace: every vector belongs to its one-dimensional span. The correct statement is for any prescribed countable family of finite-dimensional subspaces.

### CP-III-0013

The canonical pair is narrowed to source Exercise 4.3 (`theory-of-analysis-FD2.tex` L2136--L2212). All six parts are solved in order: Plancherel, double transform/invertibility, truncated Fourier integrals, differentiation, the sinc transform, and convolution of two `L^2` functions. The source typo with two copies of `F[g]` is corrected.

### CP-III-0014

The canonical pair is narrowed to source Exercise 4.1 (`theory-of-analysis-FD2.tex` L1576--L1728). Exercise 4.2 begins at L1729 and is no longer treated as part of the same problem. The Green-kernel solution is complete and the source description of `(1+4 pi^2 xi^2)^(-1)` as 'rapidly decaying' is replaced by the correct smooth-symbol statement.

### CP-III-0016

The source-backed solution is rewritten around the exact lettered Exercise 2.5 statement (`theory-of-analysis-FD.tex` L4326--L4407), removing repeated roadmap/example material from the canonical pair. The proof now has one route through Young, Hölder, Minkowski for positive simple functions, and the measurable-complex extension.

## Remaining polish queue (`B_POLISH`)

`CP-III-0004`, `0005`, `0008`, `0009`, `0017`, `0018`, `0020`, `0025`.

## Theme summary

| Theme | A strong | B polish | C rewrite | D blocking |
|---|---:|---:|---:|---:|
| Measure and Integration | 5 | 2 | 0 | 0 |
| Fourier Analysis | 8 | 3 | 0 | 0 |
| Distribution Theory | 4 | 2 | 0 | 0 |
| Sobolev and PDE Methods | 0 | 1 | 0 | 0 |

## Full 25-problem audit

| ID | Provenance | Scope | Status | Priority | Main finding | Required action |
|---|---|---|---|---|---|---|
| `CP-III-0001` | CANONICAL_AUTHORED | SOURCE_CORRECTED | **A_STRONG** | P3 | Rewritten as a rigorous Baire-category example set. The R, C([0,1]), countable finite-dimensional-family, and hyperplane claims now have explicit category arguments. The false literal source consequence about points outside every finite-dimensional subspace is corrected to the prescribed-countable-family statement. | Retain; regression validator protects the corrected countable-family statement and the worked Baire arguments. |
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
| `CP-III-0013` | CANONICAL_AUTHORED | CANONICAL_RECONCILED | **A_STRONG** | P3 | Narrowed to source Exercise 4.3 itself (L2136-L2212) and fully solved part-by-part: Plancherel, F^2, truncation, differentiation, sinc transform, and L2 convolution. The duplicated Fg typo in part (a) is corrected explicitly. | Retain; later copy-edit only. |
| `CP-III-0014` | CANONICAL_AUTHORED | CANONICAL_RECONCILED | **A_STRONG** | P3 | Narrowed to source Exercise 4.1 (L1576-L1728), removing the separately headed Exercise 4.2 radial-Fourier material from this pair. The multiplier and Green-kernel derivations are now complete, and the source's 'rapidly decaying multiplier' wording is corrected to the precise symbol estimate needed for Schwartz preservation. | Retain; later copy-edit only. |
| `CP-III-0015` | CANONICAL_AUTHORED | CLEAN_EXAMPLE | **A_STRONG** | P3 | Clean causal heat-kernel derivation by spatial Fourier transform and inversion. | Retain. |
| `CP-III-0016` | SOURCE_BACKED | CANONICAL_RECONCILED | **A_STRONG** | P3 | Rewritten to follow source Exercise 2.5 (L4326-L4407) exactly once. The solution now gives one coherent chain: p=1, Young via concavity of log, normalized Holder, positive-simple Minkowski, and passage to general measurable complex F. | Retain; later copy-edit only. |
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

`companion: polish remaining Part III solutions` — address the eight `B_POLISH` rows and then perform the Part III editorial freeze.
