# VI/43 Source Audit — Plane Cubics

## Canonical destination

- Chapter code: `VI/43`
- Title: **Plane Cubics**
- Canonical path: `books/vol06_algebraic_geometry/chapters/ch43_plane_cubics/chapter.tex`
- Planned status transition: `PLANNED` → `DRAFTED`
- Planned next action: `MAP_AND_REWRITE` → `REVIEW_AND_FREEZE`

## Migration-ledger evidence

`editorial/CHAPTER_STATUS.tsv` records `mapped_rule_count = 10` for VI/43.  The ten rules are accounted for exactly by three source lineages in `editorial/SOURCE_MIGRATION.tsv`:

### 1. `theory-of-algebraic-geometry-19.tex` — 3 rules

- `T03.SECTION`
  - selector: `plane cubic|cubic curve`
  - title/pattern: `plane cubic bridge`
  - destination: `VI/43`
  - action: `MIGRATE`
  - precedence: `100`
  - note: `cross-reference rather than duplicate proof`
- `T03.EXERCISE_CHILDREN`
  - descendant problems/exercises/solutions inherit VI/43
- `T03.THEORY_CHILDREN`
  - descendant theorem-like blocks inherit VI/43

The same legacy file also contains elliptic-curve/Riemann-surface material routed to Volume IV.  VI/43 therefore keeps the algebraic plane-cubic geometry and uses cross-references rather than duplicating the analytic Riemann-surface development.

### 2. `theory-of-differential-geometry-4.tex` — 3 rules

This file is explicitly marked as containing mislabelled algebraic geometry.

- `T05.SECTION`
  - selector: `affine curve|plane curve`
  - title/pattern: `curves`
  - destination: `VI/43`
  - action: `MIGRATE`
  - precedence: `100`
  - note: `if cubic-specific`
- `T05.EXERCISE_CHILDREN`
- `T05.THEORY_CHILDREN`

Only cubic-specific continuation belongs here; generic affine-curve material is not duplicated merely because the broad selector matched it.

### 3. `theory-of-differential-geometry-5.tex` — 4 rules

This file is also marked as mislabelled algebraic geometry and is the principal dedicated plane-cubic lineage.

- `T01.SECTION`
  - selector: `plane cubic|cubic curve`
  - title/pattern: `plane cubics`
  - destination: `VI/43`
  - action: `MIGRATE`
  - precedence: `100`
- `T01.EXERCISE_CHILDREN`
- `T01.THEORY_CHILDREN`
- `FALLBACK.ALL_UNMATCHED`
  - destination: `VI/43`
  - precedence: `10`
  - status: `COVERED_PENDING_INSTANCE_DIFF`

The fallback is provenance coverage, not permission to absorb material explicitly routed to VI/44 (Cremona transformations), VI/45 (blow-ups), or VI/42 (Picard groups).

Total: `3 + 3 + 4 = 10`, exactly matching `CHAPTER_STATUS.tsv`.

## Reconstruction rule used

The accessible repository exposes the migration and status ledgers and the completed neighboring divisor/Picard chapters, but the raw legacy prose is not available as a directly inspectable canonical chapter source through the present repository interface.  This package is therefore a mathematically audited reconstruction guided by:

1. the ten mapped ledger rules above;
2. the VI/42 endpoint `P ↦ O_E(P-O) ∈ Pic^0(E)`;
3. the established Volume VI chapter production pattern;
4. strict separation from VI/44 and VI/45;
5. standard algebraic-geometry hypotheses and characteristic caveats.

No claim of verbatim legacy recovery is made.

## Scope retained

- homogeneous plane cubics and the projective Jacobian smoothness test;
- reducible/nonreduced cubics as necessarily singular over an algebraically closed field;
- smooth, nodal, and cuspidal examples;
- Bézout for line–cubic intersection with multiplicity;
- the hyperplane divisor class `H` and `O_E(1)`;
- the principal-divisor calculation from a ratio of linear forms;
- tangents, residual intersections, and flexes;
- `H ~ 3O` for a flex origin;
- the Abel–Picard map `P ↦ [O_E(P-O)]`;
- degree-one rigidity for smooth cubics;
- a geometric reduction proof that every degree-zero divisor class is represented by `P-O`;
- `E ≅ Pic^0(E)` at the point/class level needed for the group law;
- the chord-and-tangent law with an arbitrary chosen origin;
- the simpler flex-origin relation `P+Q+R ~ 3O`;
- associativity and commutativity transported from the Picard group;
- generalized and short Weierstrass form;
- the discriminant criterion in characteristic not `2,3`;
- explicit secant/tangent addition formulas;
- geometric descriptions of `2`- and `3`-torsion;
- nodal/cuspidal degenerations toward `G_m` and `G_a`;
- rational-point closure of the group law over nonclosed fields;
- a bridge to VI/44 via degree/multiplicity/divisor bookkeeping.

## Explicitly deferred

- Cremona transformations and quadratic plane birational maps → VI/44;
- blow-ups, exceptional divisors, and strict-transform intersection bookkeeping → VI/45;
- systematic sheaf-cohomological Riemann–Roch proofs → later cohomology architecture;
- Picard schemes and representability beyond the minimal `Pic^0` bridge;
- complex-analytic uniformization of elliptic curves → Volume IV analytic/Riemann-surface chapters;
- arithmetic of Mordell–Weil groups, heights, descent, and reduction → later arithmetic development.

## Mathematical guardrails

1. The main divisor-reduction and pointwise Abel–Picard bijection is stated first over an **algebraically closed field**.
2. The chord/tangent construction counts **intersection multiplicities**, so tangent and repeated-point cases are not treated as exceptional hacks.
3. `P+Q+R ~ 3O` is asserted only after choosing a **flex origin**.  For an arbitrary origin the correct construction uses two line sections.
4. Degree-one rigidity uses the fact that a smooth plane cubic has genus `1`; a degree-one map to `P^1` would force an impossible isomorphism with a genus-zero curve.
5. Short Weierstrass form and the displayed slope/discriminant formulas are restricted to `char(k) != 2,3`.
6. The flex/`3`-torsion equivalence uses that a degree-one section of `O_E(1)` comes from a linear form; in characteristic `3`, the count of distinct geometric `3`-torsion points requires group-scheme care.
7. The singular-cubic `G_m`/`G_a` discussion is presented as normalization/generalized-Jacobian geometry, not as a claim that the singular curve itself is an elliptic curve.
8. Over nonclosed fields, rational points and Picard-scheme points are distinguished from naive Galois-fixed geometric divisor classes; a chosen rational origin supplies the needed rigidification.
9. The chapter does not use Cremona or blow-up machinery before their dedicated chapters.

## Structural target

- 8 TikZ figures
- 24 exercises, each with hint and solution
- 12 solved problem dossiers
- 5 challenges
- source audit
- ledger status update to `DRAFTED / REVIEW_AND_FREEZE`
