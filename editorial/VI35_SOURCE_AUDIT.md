# VI/35 source audit - Proj

## Direct legacy support
The repository migration ledger routes the `theory-of-algebraic-geometry-4.tex` selector `Proj` to VI/35, with inherited problem/exercise/solution and theorem-like descendants. The project audit describes the same legacy file as covering graded rings, the irrelevant ideal, `Proj S`, homogeneous primes, the structure sheaf, degree-zero localization, `D_+(f)`, projective space, and closed projective subschemes.

## Canonical consumption in VI/35
VI/35 consumes the general Proj construction:
- homogeneous-prime point set excluding the irrelevant ideal;
- `V_+(I)` topology;
- standard opens `D_+(f)`;
- affine chart theorem `D_+(f) ~= Spec S_(f)`;
- chart overlap/localization compatibility;
- structure sheaf and stalks;
- sheaves associated to graded modules using `M_(f)`.

## Reserved downstream
- VI/36: projective space and homogeneous coordinates;
- VI/37: projective schemes / homogeneous closed subschemes;
- VI/38: projective morphisms and closed embeddings.

## Canonical extensions
The graded-module sheaf exactness, shift preview, Veronese invariance, saturation warning, and reducible/nonreduced prototype computations are extensions motivated by VI/33-VI/34. No separately numbered legacy problem is claimed for them.
