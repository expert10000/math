# Volume IV â€” professional mathematical repair

**Scope:** IV/01--IV/31
**Base:** `3921b849f07dc459620528548f244f7c450ab16d`

The live source, rather than the historical v1 freeze, is the review baseline:

- chapters: **31**
- solved problems: **372**
- exercises: **744**
- hints: **744**
- total solution environments: **1116**

## Repairs applied

- **IV/05:** the primitive theorem now explicitly uses null-homotopy plus local Cauchy--Goursat, removing the compressed/circular-looking appeal to a later global form.
- **IV/12:** the argument principle is stated in the index-weighted form for general closed contours, with the Jordan-contour `N-P` formula as a corollary; the proof dossier matches it.
- **IV/17:** Riemann mapping existence is promoted from theorem-level prose to an explicit theorem and is honestly classified as a standard external theorem requiring normal-family/Montel machinery.
- **IV/18:** Schwarz--Christoffel angle notation is normalized so `alpha_k*pi` is the interior angle and the derivative exponent is `alpha_k-1` everywhere.
- **IV/22:** an arbitrary Riemann-surface chart is no longer conflated with a chart induced by a projection; the theorem is now the inverse-function statement for an unramified holomorphic projection.
- **IV/24:** the local power model is stated without the misleading word â€śoftenâ€ť, and degree is constant with multiplicity on every fiber of a nonconstant holomorphic map between connected compact Riemann surfaces.

Targeted checks of **IV/26** (Riemann--Hurwitz) and **IV/31** (torus/cubic biholomorphism) found no blocking theorem-level correction in this pass.

The historical files under `books/vol04_complex_analysis/freeze/` are intentionally unchanged.
