# VI/39 full-solutions and dossier audit

## Canonical chapter

- Chapter: `VI/39 — Weil Divisors`
- Canonical path: `books/vol06_algebraic_geometry/chapters/ch39_weil_divisors/chapter.tex`
- Guarded source blob at package construction: `5948df7e2f4a920163a9ca3cf61f39b7e7dc3d6c`
- Status ledger: `DRAFTED`, `LEGACY_SOURCE_IDENTIFIED`, 8 mapped rules, `REVIEW_AND_FREEZE`.

## Source-routing audit

The 8 VI/39 migration rules split as follows.

### Canonical AG9 source — 4 rules

1. `T01.SECTION`: selector `Weil divisor|prime divisor` → VI/39, `MIGRATE`, canonical `YES`.
2. `T01.EXERCISE_CHILDREN`: descendants of that section → VI/39.
3. `T01.THEORY_CHILDREN`: theorem-like descendants → VI/39.
4. `FALLBACK.ALL_UNMATCHED`: AG9 safety-net destination VI/39, subject to instance-level splitting.

AG9 separately routes Cartier divisors to VI/40, class groups to VI/41, line bundles/Picard to VI/42, quasi-coherent material to VI/33, and projective-morphism overlap to VI/38.  Those boundaries are preserved.

### AG10 comparison source — 4 rules

1. `T01.SECTION`: broad selector `divisor|Picard|line bundle|coherent` → VI/39 as `COMPARE_AND_MIGRATE`.
2. `T01.EXERCISE_CHILDREN`: comparison descendants.
3. `T01.THEORY_CHILDREN`: comparison descendants.
4. `FALLBACK.ALL_UNMATCHED`: comparison safety net.

AG10 is explicitly comparison-only rather than an independent canonical chapter source.

## Canonical live corpus preserved

The apply script is guarded by the live chapter blob and transforms only hint/solution regions plus one insertion point before the Cartier bridge.  It preserves the canonical problem environments themselves.

- 24 exercises: labels `exr:vi39-01` … `exr:vi39-24`.
- 12 dossier problems: labels `prob:vi39-p1` … `prob:vi39-p12`.
- 5 challenges: labels `chal:vi39-1` … `chal:vi39-5`.

Canonical dossier titles retained:

1. Factorization on an affine factorial scheme.
2. Restriction changes the visible divisor.
3. A projective ratio.
4. Orders on the quadric cone.
5. Degree check on `P^1`.
6. Effective principal divisors on a proper curve.
7. Detecting a unit at a generic point.
8. Why the cusp is not a DVR computation.
9. Same support, different multiplicity.
10. A rational function with no divisor on an open torus.
11. Principal pullback only.
12. Cartier coefficients are well defined.

## Mathematical refinement

The detailed layer strengthens the chapter in four places:

- explicit DVR/order calculations in affine and projective examples;
- the Krull-domain extension principle `div(u)=0 ⇔ u` is a global unit on a normal Noetherian integral scheme;
- controlled pullback and pushforward under finite dominant morphisms, including ramification indices, residue degrees, and the norm formula;
- a local Nakayama proof that the quadric-cone divisor `P=(x,z)` is not principal at the vertex even though `div(x)=2[P]`.

### P11 correction

The original short P11 solution said that equality `div_X(f)=div_X(h)` need not force equality after pullback.  In the chapter's normal Noetherian setting that is too weak: `u=f/h` has zero divisor, hence is a global unit by the height-one intersection property of normal Noetherian domains.  Pullback preserves units, so

`div_Y(g^*f)=div_Y(g^*h)`.

The package removes the old short inline solution and supplies the corrected detailed argument without changing the canonical P11 problem statement.

## Scope boundary

This commit intentionally stops before the next chapters' main theories:

- VI/40: Cartier divisors and their general local-equation pullback theory;
- VI/41: divisor class groups and factoriality;
- VI/42: line bundles and Picard groups.

The finite-morphism formulas included here are a controlled codimension-one case, not a substitute for general cycle/intersection theory.
