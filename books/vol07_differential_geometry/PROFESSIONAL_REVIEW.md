# Volume VII professional review — exercise, hint, theorem and release coverage

Pinned review base: `e0766a28be4cce2aa6393b31d25197d54f2353ac`

## Scope

This is the final professional reconciliation pass for VII/01–VII/42 after the mathematical/hypothesis review and prerequisite/notation review.

The pre-existing corpus audit already reports:

- 42/42 canonical chapter rows;
- 42/42 active chapter includes;
- 1008 exercises;
- 1008 hints;
- 714 solved problems;
- 1722 solutions;
- 2460 labels;
- zero duplicate labels;
- zero unresolved Volume VII local references;
- all Volume VII rows `FROZEN` / `COMPLETE`.

Those structural counts are preserved. This pass adds the semantic review contract that raw environment counts cannot prove.

## Semantic exercise and solution reconciliation

Review every chapter under these rules:

1. every exercise and solved problem must use only definitions/results already available at that point, unless it explicitly announces a forward-looking exploration;
2. every hint must materially guide the associated exercise rather than restate it;
3. every solution must actually solve the stated task and preserve all hypotheses;
4. proof exercises must not silently strengthen or weaken the theorem they reference;
5. equivalent formulations must use the volume's established sign and normalization conventions;
6. examples with exceptional or degenerate cases must state exclusions rather than hide them in calculations;
7. computational exercises must distinguish exact statements, consistency results, approximations, heuristics, and implementation choices.

## Part-specific checks

### Smooth manifolds and forms
- retain Hausdorff/second-countable and boundary hypotheses where needed;
- preserve rank/regular-value hypotheses;
- check wedge signs, pullbacks, orientation, compact support, and Stokes boundary orientation.

### Curves and surfaces
- distinguish regular from unit-speed curves;
- retain nonzero-curvature hypotheses for Frenet frames;
- keep shape-operator, second-fundamental-form, Gaussian-curvature and mean-curvature signs consistent;
- treat umbilic/parabolic/flat exceptional cases correctly.

### Riemannian and Lorentzian geometry
- use the fixed Levi–Civita and Riemann-tensor conventions;
- preserve completeness/compactness/locality hypotheses;
- distinguish Riemannian metric completeness from Lorentzian causal/geodesic notions;
- retain dimension restrictions for Weyl-curvature statements.

### Hyperbolic geometry
- keep sectional curvature normalized to `-1` unless explicitly rescaled;
- distinguish `SL` from `PSL` actions;
- retain discreteness/proper-discontinuity and torsion/orbifold caveats;
- distinguish Fuchsian and Kleinian settings.

### Computational geometry
- distinguish edge-graph paths from intrinsic polyhedral geodesics;
- distinguish exact algorithms from approximation schemes;
- state the heat-method time-step and Poisson/null-space assumptions;
- keep Laplacian sign, cotangent weights and mass-matrix conventions consistent;
- note boundary conditions where operators are not uniquely defined without them;
- distinguish smooth curvature-line/ridge/valley definitions from discrete estimators.

## Existing automated gate

Use the repository's canonical audit:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\books\vol07_differential_geometry\AUDIT_VOLUME07.ps1 `
  -Repo $PWD `
  -ExpectedStatus FROZEN `
  -ExpectedNextAction COMPLETE
```

The audit checks chapter-status rows, canonical paths, includes, chapter labels, duplicate labels, Volume VII references, placeholders, exercise/hint balance, and solution counts.

## Full build gate

From the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\books\vol07_differential_geometry\BUILD_WINDOWS.ps1 `
  -Repo $PWD `
  -Clean
```

Then inspect the log and artifact:

```powershell
Select-String `
  -Path .\books\vol07_differential_geometry\book.log `
  -Pattern "Undefined|multiply defined|LaTeX Error|Package .* Error|Overfull|Underfull"

Get-Item .\books\vol07_differential_geometry\book.pdf
Get-FileHash .\books\vol07_differential_geometry\book.pdf -Algorithm SHA256
```

Any genuine chapter correction discovered during this review must be followed by regeneration of the corpus audit and freeze hashes according to the existing Volume VII release policy.

## Final git gate

```powershell
git status --short
git diff --stat e0766a28be4cce2aa6393b31d25197d54f2353ac..HEAD
git log --oneline --decorate -4
```

Do not introduce a review branch. These three professional-review commits belong directly on `main`.
