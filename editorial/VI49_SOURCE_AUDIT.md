# VI/49 — Basic Vanishing Results Source Audit

Canonical destination:

- `books/vol06_algebraic_geometry/chapters/ch49_basic_vanishing_results/chapter.tex`

Live ledger state before apply:

- `VI/49` — `PLANNED`
- mapped rule count: **3**
- next action: `MAP_AND_REWRITE`

## Exact mapped ownership

All three VI/49 rules come from `theory-of-algebraic-geometry-11.tex`:

1. `T04.SECTION` — selector `acyclic|vanishing|flabby resolution` → **VI/49 Basic Vanishing Results**.
2. `T04.EXERCISE_CHILDREN` — problem/exercise/solution descendants of that matched section → **VI/49**.
3. `T04.THEORY_CHILDREN` — theorem-like descendants of that matched section → **VI/49**.

The neighboring `T01`, `T02`, and `T03` blocks remain owned by VI/46, VI/47, and VI/48 respectively. The file fallback remains assigned to VI/46 and is not counted as VI/49 ownership.

## Reconstruction scope

The chapter develops:

- flabby and injective acyclicity;
- exact localization Čech complexes;
- affine vanishing for quasi-coherent sheaves;
- affine Leray covers on separated schemes;
- cohomological bounds from finite affine covers;
- complete line-bundle cohomology on `P^1`;
- propagation of vanishing through exact sequences and dimension shifting;
- a clear boundary between basic vanishing and deeper Serre vanishing.

## Production audit target

- 8 TikZ figures
- 24 exercises with 24 hints and 24 solutions
- 12 solved problem dossiers
- 5 challenges
- 68 total labels, all unique
