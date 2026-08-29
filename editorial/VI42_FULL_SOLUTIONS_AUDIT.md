# VI/42 — Line Bundles and Picard Groups — Full-Solutions Audit

## Scope and provenance

- Canonical chapter: `books/vol06_algebraic_geometry/chapters/ch42_line_bundles_and_picard_groups/chapter.tex`
- Indexed blob guarded by this package: `e27fc14aa41e31269ff6234960dad7fb1a765175`
- Chapter-status mapped-rule count: **6**
- Canonical pedagogical corpus preserved: **24 exercises, 12 solved-problem dossier statements, 5 challenges**.
- This package does **not** replace or renumber any canonical exercise/problem/challenge statement. It removes the short inline answer layer and reinstalls expanded answers behind the existing full-solutions switches.

## Refinement focus

### VI/42
{
42: "- line-bundle gluing, cocycles/coboundaries, tensor products and duals;\n- Cartier divisor classes versus the Picard group;\n- Picard/class-group comparison on the quadric cone and punctured cone;\n- projective-space twisting sheaves, section divisors, and the bridge to `Pic^0`.",
43: "- divisor-theoretic construction of the chord-and-tangent law;\n- Abel--Picard bijection, degree-one rigidity, and associativity through `Pic^0`;\n- explicit Weierstrass addition/torsion calculations;\n- nodal/cuspidal degenerations and rational-point closure.",
44: "- primitive homogeneous representations, base loci, and the standard quadratic involution;\n- exceptional curves, conic net, degree/multiplicity formula, and degree cancellation;\n- transformed cubic models and function-field birationality;\n- explicit divisor-class and local-chart bridge to blow-ups."
}[ch]

## Production behavior

The apply script:
1. checks the indexed `chapter.tex` blob before editing;
2. preserves canonical statements and labels;
3. strips only the old inline `hint`/`solution` environments in the pedagogical tail;
4. adds guarded inputs for detailed hints, exercise solutions, dossier solutions, and challenge solutions;
5. copies this audit into `editorial/`.

The verifier checks exact label sets rather than brittle literal LaTeX titles, avoiding false failures caused solely by backslash escaping inside problem titles.
