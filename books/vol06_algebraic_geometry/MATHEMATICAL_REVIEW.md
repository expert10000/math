# Volume VI mathematical review — VI/01–VI/49

Pinned base: `54402bb`

This pass is deliberately conservative. Volume VI is a 49-chapter frozen algebraic-geometry
volume with extensive hand-developed and migrated material. The review therefore does not
perform global regex replacements of mathematical prose.

## Hypothesis-sensitive audit map

The professional review treats the following as release-critical distinctions:

- affine algebraic sets versus affine schemes;
- algebraically closed field hypotheses in classical affine geometry and Nullstellensatz uses;
- irreducible versus reduced versus integral;
- generic points versus closed points;
- stalk/local-ring/residue-field formulas;
- presheaf image versus image sheaf;
- sheaf cokernels and quotient sheaves versus sectionwise quotients;
- exactness on stalks versus sectionwise surjectivity;
- affine scheme recovery from global sections;
- morphisms of locally ringed spaces;
- gluing hypotheses and compatibility;
- fiber products and base change;
- ordinary versus geometric fibers;
- finite type, finite presentation, and Noetherian hypotheses;
- integral schemes, function fields, normalization, and finiteness of normalization;
- Krull dimension and codimension conventions;
- tangent-space residue-field conventions;
- quasi-coherent sheaves and affine module dictionaries;
- graded rings, Proj, twisting sheaves, and projective embeddings;
- Weil versus Cartier divisors and normality assumptions;
- divisor class groups versus Picard groups;
- blow-ups and Rees-algebra conventions;
- Čech cohomology versus sheaf cohomology;
- long exact cohomology sequences and vanishing hypotheses.

## Concrete correction in this pass

Several canonical chapter files retain the legacy header

`% Status: DRAFTED (extended review before repository write)`

even though Volume VI is frozen and these chapters are compiled into the canonical book.
This pass normalizes that exact stale header to

`% Status: FROZEN (Volume VI v1.0 release baseline)`

wherever it occurs under the 49 canonical Volume VI chapter files.

This is an editorial correctness fix only; it does not alter theorem content.

## Rule

If later mathematical corrections are discovered by the build/PDF review, they should be
made as targeted follow-up corrections with exact chapter-local evidence, not by broad
replacement.
