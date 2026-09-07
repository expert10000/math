# Volume III — remaining mathematical statements and proofs

**Status: PASS. No known blocking mathematical finding remains in this review.**

Source pin: `9b5a9df81037a845af81982efc95dcd6139ab53a`. HEAD matched and `git status --short` was empty before source editing.

Reviewed all 28 chapters, including repeated theorem/dossier/exercise statements and supplementary examples, solutions and hints. The JSON records 157 targeted repair operations with before/after text and rationale; these are audit records, not a claim of that many independent defects. Correct prose was not rewritten for style.

Preserved current-source counts: **28 chapters; 336 solved dossiers/problems; 672 exercises; 672 hints; 1,008 solutions; 196 examples.** Each chapter retains 12 problems, 24 exercises, 24 hints and 36 solutions. Every pinned label and environment count is preserved.

Only 6 of the 672 hints changed, for mathematical errors (null-integral implication, Schwartz support/decay, test support, classical/weak differentiation, formal transpose, heat normalization). No bulk hint normalization or prerequisite graph was performed.

## Chapter review matrix

| Chapter | Result | Checked and repaired |
|---|---|---|
| III/01 | PASS | Measurable-set domains, finite-stage continuity from above, completion and strict enlargement. |
| III/02 | PASS | Borel codomains, extended-real limits, finite-valued algebra and simple approximation at infinity. |
| III/03 | PASS | Nonnegative construction, defined signed integral versus integrability, null invariance and concrete counterexamples. |
| III/04 | PASS | MCT extended-integral proof, measurable a.e. hypotheses, domination, convergence modes and finite-mass Scheffe. |
| III/05 | PASS | Product sigma-algebra versus completion, every measurable section, sigma-finiteness, Tonelli construction and Fubini counterexample. |
| III/06 | PASS | A.e. quotient, finite/infinite exponents, completeness including essential supremum, density and typewriter example. |
| III/07 | PASS | Conjugate endpoints, zero normalization, Minkowski integrability, interpolation range and dual extremizer. |
| III/08 | PASS | Finite-measure Egorov, boundedness plus small-set uniform integrability, Vitali proof, weak quasi-norm and tail quantity. |
| III/09 | PASS | Global circle period and normalization, Parseval input, Dirichlet kernel limitations, exact Dirichlet and Fejer convergence. |
| III/10 | PASS | Convolution existence, Young exponents, compact support/closure, smoothing domains and approximate-identity hypotheses. |
| III/11 | PASS | Global transform and inverse signs, moments, differentiation, inversion modes and independent Gaussian input. |
| III/12 | PASS | Gaussian scaling by dimension and positive-definite matrix, heat-kernel mass and time range, Hermite qualification. |
| III/13 | PASS | Schwartz-core Parseval, L2 extension, inverse/surjectivity, agreement with L1 transform and multipliers. |
| III/14 | PASS | Schwartz seminorm estimates, continuous operations, convolution decay requirements and false compact-support hint. |
| III/15 | PASS | Fixed-support topology versus LF topology, continuity estimates, standard theorem scope, quotient domain and composition counterexample. |
| III/16 | PASS | Linear distribution pairing, locally integrable representatives, mollifiers, locally finite jump formula and distributional convergence example. |
| III/17 | PASS | Support, derivative and delta support, total variation, closed locally finite surfaces and precise jump regularity. |
| III/18 | PASS | Schwartz linear pairing, polynomial growth, measure variation and elimination of ambiguous inverse convention. |
| III/19 | PASS | Exact dual transform convention, derivative/moment constants, principal-value extension and signed fundamental solution. |
| III/20 | PASS | Local integrability, a.e. uniqueness, C1 versus classical differentiability, interior mollification and exact chain-rule scope. |
| III/21 | PASS | Wkp/Hk/H01 definitions, genuine Hilbert norm, trace endpoints, Poincare proof, Sobolev/Rellich ranges and homogeneous scaling. |
| III/22 | PASS | Finite-p density, interior versus global mollification, extension geometry, corrected indicator and fixed frequency cutoff. |
| III/23 | PASS | Real Hilbert Lax--Milgram hypotheses, elliptic coefficient bounds, weak versus classical solution, Neumann compatibility and Cea. |
| III/24 | PASS | Constant-coefficient convolution, signs/dimensions of Laplace kernels, causal heat kernel, off-source regularity and logarithmic scaling. |
| III/25 | PASS | Precise real Dirichlet representation, pole excision, boundary term sign, Hermitian qualification and Neumann normalization. |
| III/26 | PASS | Weighted Sturm--Liouville operator/domain, separated real boundary conditions, Wronskian sign, resonance and L2 kernel expansion. |
| III/27 | PASS | Ellipticity versus uniform ellipticity, principal/lower-order signs, comparison conflict, perturbation proof, strong/Hopf hypotheses. |
| III/28 | PASS | Heat/wave data and solution topology, self-adjoint compact-resolvent inputs, spectral convergence and Poisson/heat constants. |

## Proof scope and mathematical justification

The repairs follow from the displayed definitions, normalization, counterexamples or missing hypotheses in the source. Product-measure extension, Fourier completeness, LF convergence, partition refinements, Sobolev embedding/trace/extension/compactness, Green existence and the self-adjoint spectral theorem are explicitly scoped as standard inputs where full proofs are deferred. Proof dossiers using those inputs now request the stated sketch. The Plancherel inverse and maximum-principle perturbation steps are supplied directly.

For a supporting account of fixed-support seminorms and dual continuity, see [Richard Melrose, Topologies of test/distribution spaces](https://math.mit.edu/~rbm/18-155-F15/Topologies.pdf). The manuscript retains its own explicitly stated Fourier convention.

## Reproducible pre-commit gates

From the repository root run:

```text
python -B reports/vol03/verify_review.py
git diff --check
```

The pinned tree has release bundle builders but no standalone structural-preflight command. The included verifier performs a read-only bundle preflight: 256 unique editorial chapter rows, all canonical sources present, all Volume III TeX inputs present, balanced environments, pinned per-chapter counts/labels, and a scope check. It then runs the existing Volume III reconstruction and expansion-balance algorithms with explicit current-source expectations. Historical report files and scripts are not modified.

The v1.0 full reconstruction script expects 8 exercises/8 hints/20 solutions per chapter and DRAFTED status; current source has 24/24/36 and FROZEN. Its equivalent run changes only those expectations and redirects output to ignored build storage. Source-rule/provenance/reference checks remain active: **131 source rules, 131 accounting rows and 336 dossier provenance rows; no unresolved rules or missing source files.**

The expansion-balance script protects pre-expansion prose hashes. That hash gate is inapplicable to this authorized mathematical correction; its count, placement, graded-category and duplicate-label gates remain active, and a stronger comparison against the pinned chapter counts/labels runs separately. This is an explicit audit adaptation, not a raw historical-script PASS.

| Gate | Result |
|---|---|
| bundle structural preflight and Volume III labels/references | PASS |
| current-source reconstruction/reconciliation equivalent | PASS |
| expansion placement and pairing equivalent | PASS |
| Volume III three-pass LaTeX build and log inspection | PASS |

Build command (three passes, working directory `books/vol03_fourier_distributions_pde`):

```text
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=<repo>/build/vol03-review book.tex
```

All three passes exited 0. Final PDF: **275 pages**. Undefined references/citations: **0**. Duplicate labels: **0**. Overfull h/v boxes: **0**, including **0** at or above the repository professional-review significance threshold of 20 pt. Nonfatal hyperref bookmark-token and underfull-box warnings do not affect the mathematical text. Build outputs remain ignored under `build/vol03-review/`.

PDF SHA-256: `02cc0c9d803c3c4545ceffc013fd220c462f92eeea0204e1a0913da8baa85d26`.

## Changed Volume III files

- `books/vol03_fourier_distributions_pde/chapters/ch01_sigma_algebras_and_measures/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch02_measurable_functions/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch03_the_lebesgue_integral/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch04_convergence_theorems/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch05_product_measures_and_fubini_theory/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch06_lp_spaces/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch07_h_lder_minkowski_and_interpolation/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch08_egorov_vitali_and_weak_lp_ideas/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch09_fourier_series/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch10_convolution_and_approximate_identities/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch11_the_fourier_transform/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch12_the_gaussian_and_transform_calculus/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch13_plancherel_and_l2_fourier_theory/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch14_the_schwartz_space/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch15_test_function_spaces/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch16_distributions_and_distributional_derivatives/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch17_support_and_singular_distributions/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch18_tempered_distributions/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch19_fourier_transform_of_distributions/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch20_weak_derivatives/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch21_sobolev_spaces/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch22_approximation_and_density/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch23_weak_boundary_value_problems/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch24_fundamental_solutions/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch25_green_functions/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch26_sturm_liouville_green_kernels/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch27_elliptic_operators_and_maximum_principles/chapter.tex`
- `books/vol03_fourier_distributions_pde/chapters/ch28_spectral_and_transform_methods_for_pde/chapter.tex`

New review evidence:

- `reports/vol03/VOL03_REMAINING_MATH_REPAIRS.md`
- `reports/vol03/VOL03_REMAINING_MATH_REPAIRS.json`
- `reports/vol03/verify_review.py`

No content or historical release evidence from any other volume changed.

## Commit

Intended single commit: `vol03: correct remaining mathematical statements and proofs`. No push. The final commit SHA and post-commit working-tree state are reported in the task response; they cannot be embedded in a file belonging to that same commit without changing its SHA.
