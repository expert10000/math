# VI/45 Source Audit — Blow-Ups

## Canonical destination

- Chapter code: `VI/45`
- Title: **Blow-Ups**
- Canonical path: `books/vol06_algebraic_geometry/chapters/ch45_blow_ups/chapter.tex`
- Planned status transition: `PLANNED` → `DRAFTED`
- Planned next action: `MAP_AND_REWRITE` → `REVIEW_AND_FREEZE`

## Migration-ledger evidence

`editorial/CHAPTER_STATUS.tsv` records `mapped_rule_count = 3` for VI/45. The three rules are all contained in the dedicated blow-up block of `editorial/SOURCE_MIGRATION.tsv`.

### `theory-of-differential-geometry-5.tex` — 3 rules

This legacy file is explicitly identified in the migration ledger as containing mislabelled algebraic geometry.

1. `T03.SECTION`
   - selector: `blow-up|blowup|exceptional divisor`
   - title/pattern: `blow-ups`
   - destination: `VI/45`
   - action: `MIGRATE`
   - precedence: `100`
   - coverage: `EXPLICIT_SELECTOR`
   - audit status: `CURATED_TOPIC_MAP`
2. `T03.EXERCISE_CHILDREN`
   - descendant problems/exercises/solutions inherit VI/45
   - precedence: `90`
   - coverage: `INHERIT_FROM_MATCHED_SECTION`
   - audit status: `EXHAUSTIVE_BY_INHERITANCE`
3. `T03.THEORY_CHILDREN`
   - descendant definitions/theorems/lemmas/propositions/corollaries/remarks/warnings/examples inherit VI/45
   - precedence: `90`
   - coverage: `INHERIT_FROM_MATCHED_SECTION`
   - audit status: `EXHAUSTIVE_BY_INHERITANCE`

Total: `3`, exactly matching `CHAPTER_STATUS.tsv`.

The same legacy file separately routes:

- plane cubics → VI/43;
- Cremona transformations / birational maps → VI/44;
- Picard groups / line bundles → VI/42.

Its file-level fallback is assigned to VI/43, not VI/45. Therefore VI/45 has no permission to absorb unmatched material from that source. This reconstruction respects that boundary strictly.

## Reconstruction rule used

The live repository exposes the exact migration/status ledgers and the completed neighboring VI/44 chapter, while the raw legacy prose is not exposed as an authoritative canonical chapter source through the present reconstruction workflow. This package is therefore a mathematically audited reconstruction guided by:

1. the exact three VI/45 migration rules;
2. the explicit VI/44 bridge `H -> 2H-E1-E2-E3`;
3. the established Volume VI production pattern;
4. the already-developed Proj, projective morphism, divisor, class-group, and Picard machinery;
5. strict separation between blow-up geometry (VI/45) and the cohomological material beginning in VI/46.

No claim of verbatim legacy recovery is made.

## Scope retained

- blow-up of `A^2` at the origin as an incidence variety;
- the two affine blow-up charts and their transition map;
- the exceptional divisor `E ≅ P^1`;
- tangent-direction interpretation of exceptional points;
- intrinsic Rees-algebra definition `Bl_Z X = Proj_X ⊕ I^n`;
- projectivity and isomorphism away from the center;
- universal property for making the center ideal invertible;
- total transforms and strict transforms;
- local multiplicity formula `π^*C = C~ + mE`;
- tangent cone and `C~ ∩ E`;
- node separation and cusp example;
- `Pic(Bl_p P^2) = ZH ⊕ ZE`;
- intersection form `H^2=1`, `H·E=0`, `E^2=-1`;
- strict-transform class `dH-mE` and self-intersection correction;
- canonical-divisor formula `K_X~ = π^*K_X + E` for a smooth point blow-up;
- blow-up of three noncollinear points of `P^2`;
- strict transforms of the three coordinate lines;
- resolution of the standard quadratic Cremona transformation;
- base-point-free divisor class `2H-E1-E2-E3`;
- local chart proof that the lifted Cremona map is regular;
- source blow-up / target blow-down factorization;
- lifted involution on the common blown-up surface;
- Picard-lattice action on `H,E1,E2,E3`;
- degree and transformed-multiplicity formulas;
- general resolution of a projective rational map by blowing up its base ideal;
- infinitely near points and repeated blow-ups;
- introductory blow-down / `(-1)`-curve viewpoint;
- bridge from the birational geometry arc to VI/46 flabby sheaves.

## Explicitly deferred

- a full proof of Castelnuovo's contraction criterion;
- classification of exceptional curves on arbitrary rational surfaces;
- minimal models and the surface MMP;
- complete Noether equalities and homaloidal type classification;
- detailed theory of clusters of infinitely near points;
- full embedded resolution theorem for plane curve singularities;
- higher-dimensional blow-ups and discrepancies beyond the smooth-surface point case;
- derived blow-ups, deformation to the normal cone, and Rees-algebra asymptotics;
- sheaf cohomology computations on blown-up surfaces (deferred until the cohomological chapters).

## Mathematical guardrails

1. The exceptional divisor is introduced first in explicit charts and only then identified intrinsically as the projectivized tangent space.
2. Total and strict transforms are kept distinct throughout; the formula `π^*C = C~ + mE` is stated only for the relevant Cartier-divisor setting.
3. The tangent-cone equation on `E` is obtained after removing the maximal exceptional factor.
4. The intersection computation `E^2=-1` is derived geometrically from two strict transforms of lines through the center, not simply asserted.
5. The Picard-lattice basis uses `H=π^*(line)`; a strict transform of a line through the center is `H-E`, not `H`.
6. For three distinct blown-up points, the exceptional divisors are pairwise disjoint and each has square `-1`.
7. The resolved Cremona morphism is checked in both the local chart model and the divisor class `D=2H-E1-E2-E3`.
8. The source blow-up morphism `S -> P^2` is distinguished from the lifted automorphism `S -> S` obtained after also resolving the target.
9. The Cremona degree/multiplicity formulas are applied to noncontracted transforms with coordinate-line components excluded.
10. The lifted Picard action is checked to be involutive, to preserve the intersection form, and to fix the canonical class.
11. Infinitely near points are introduced only after the first blow-up makes their meaning precise.
12. The general base-ideal blow-up is described as resolving the given projective rational map, without claiming that one blow-up always gives a smooth or minimal resolution.

## Structural target

- 8 TikZ figures
- 24 exercises, each with hint and solution
- 12 solved problem dossiers
- 5 challenges
- 68 labels total, all unique
- source audit
- ledger status update to `DRAFTED / REVIEW_AND_FREEZE`
