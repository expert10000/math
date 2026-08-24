# VI/44 Source Audit — Cremona Transformations

## Canonical destination

- Chapter code: `VI/44`
- Title: **Cremona Transformations**
- Canonical path: `books/vol06_algebraic_geometry/chapters/ch44_cremona_transformations/chapter.tex`
- Planned status transition: `PLANNED` → `DRAFTED`
- Planned next action: `MAP_AND_REWRITE` → `REVIEW_AND_FREEZE`

## Migration-ledger evidence

`editorial/CHAPTER_STATUS.tsv` records `mapped_rule_count = 3` for VI/44. The three rules are all contained in the dedicated Cremona block of `editorial/SOURCE_MIGRATION.tsv`:

### `theory-of-differential-geometry-5.tex` — 3 rules

This legacy file is explicitly identified in the migration ledger as containing mislabelled algebraic geometry.

1. `T02.SECTION`
   - selector: `Cremona|birational map`
   - title/pattern: `Cremona transformations`
   - destination: `VI/44`
   - action: `MIGRATE`
   - precedence: `100`
   - audit status: `CURATED_TOPIC_MAP`
2. `T02.EXERCISE_CHILDREN`
   - descendant problems/exercises/solutions inherit VI/44
   - precedence: `90`
   - coverage: `INHERIT_FROM_MATCHED_SECTION`
3. `T02.THEORY_CHILDREN`
   - descendant theorem-like blocks inherit VI/44
   - precedence: `90`
   - coverage: `INHERIT_FROM_MATCHED_SECTION`

Total: `3`, exactly matching `CHAPTER_STATUS.tsv`.

The same legacy file separately routes:

- plane cubics → VI/43;
- blow-ups / exceptional divisors → VI/45;
- Picard / line-bundle material → VI/42.

Its file-level fallback is assigned to VI/43, not VI/44. Therefore VI/44 has no permission to absorb unmatched content from that source. This reconstruction respects that boundary strictly.

## Reconstruction rule used

The live repository exposes the migration/status ledgers and the completed neighboring VI/43 chapter, but the raw legacy prose is not exposed as a directly inspectable canonical chapter source through the current repository interface. This package is therefore a mathematically audited reconstruction guided by:

1. the exact three VI/44 migration rules;
2. the VI/43 bridge from plane cubics to quadratic birational maps;
3. the established Volume VI production pattern;
4. strict deferral of blow-up constructions to VI/45;
5. standard algebraic-geometry definitions and characteristic-independent coordinate calculations wherever possible.

No claim of verbatim legacy recovery is made.

## Scope retained

- rational maps and domains of definition;
- birational maps and the plane Cremona group;
- homogeneous projective representations by equal-degree forms;
- primitive triples and removal of common factors;
- base loci and base points;
- the standard quadratic transformation `[x:y:z] -> [yz:xz:xy]`;
- direct verification of its involutive birationality;
- its three coordinate base points;
- contraction of the three coordinate lines;
- source/target symmetry and inverse base points;
- the net of conics through three noncollinear points;
- projective conjugacy of quadratic maps with three proper noncollinear base points;
- algebraic degree and cancellation under composition;
- birational transforms of noncontracted curves;
- the formula `deg C' = 2d - m1 - m2 - m3` for the standard quadratic map;
- line/conic transform examples;
- cubic degree behavior as the bridge from VI/43;
- function-field criterion for birationality;
- comparison with projective automorphisms;
- the symbolic divisor-class shadow `H -> 2H - E1 - E2 - E3`;
- a non-proved contextual statement of the classical Noether–Castelnuovo generation theorem;
- local direction analysis explaining why resolution requires a projective line over each base point;
- a precise bridge to VI/45.

## Explicitly deferred

- construction and universal property of the blow-up → VI/45;
- exceptional divisors as actual curves on a blown-up surface → VI/45;
- strict transforms defined via blow-up closure → VI/45;
- intersection pairing on `Pic(Bl_p P^2)` → VI/45;
- self-intersection `E^2=-1` and contraction criteria → VI/45;
- infinitely near base points and complete homaloidal type formalism → after the blow-up machinery;
- a proof of Noether–Castelnuovo → later birational-geometry development;
- higher-dimensional Cremona groups;
- modern dynamical degree / entropy theory for plane birational maps.

## Mathematical guardrails

1. A rational-map triple is reduced to a **primitive** triple before its base locus or algebraic degree is read off.
2. Equality of rational maps is equality on a dense open set, so the identity `sigma^2 = id` is not asserted at base points where `sigma` is undefined.
3. The coordinate lines are treated as **contracted exceptional curves**, not ordinary curves to which the positive-dimensional degree formula is blindly applied.
4. The formula `2d-m1-m2-m3` is proved using a **general conic** in the pullback net and B\'ezout, with the no-common-component hypothesis stated.
5. The `E_i` symbols are explicitly marked as a **preview** until VI/45 constructs the exceptional divisors.
6. The discussion of general quadratic transformations is restricted to three **proper noncollinear base points**; infinitely near degenerations are deferred.
7. The classical Noether–Castelnuovo theorem is stated only as context and is **not used** in any chapter proof.
8. A smooth cubic mapped to a sextic is not claimed to remain smooth; genus forces singularities in the sextic model.
9. Birationality is separated from preservation of plane degree, smoothness, and embedding data.
10. Resolution is motivated locally by tangent-direction dependence without presupposing the blow-up theorem.

## Structural target

- 8 TikZ figures
- 24 exercises, each with hint and solution
- 12 solved problem dossiers
- 5 challenges
- 68 labels total, all unique
- source audit
- ledger status update to `DRAFTED / REVIEW_AND_FREEZE`
