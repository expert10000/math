# VI/40 full-solutions and dossier audit

## Canonical chapter

- Chapter: `VI/40 — Cartier Divisors`
- Canonical path: `books/vol06_algebraic_geometry/chapters/ch40_cartier_divisors/chapter.tex`
- Guarded source blob at package construction: `7f07da7a450469c6b84c1ff48963aa52f5bf86cc`
- Status ledger: `DRAFTED`, `LEGACY_SOURCE_IDENTIFIED`, 3 mapped rules, `REVIEW_AND_FREEZE`.

## Source-routing audit

VI/40 has exactly three canonical migration rules, all from `theory-of-algebraic-geometry-9.tex`:

1. `T02.SECTION`: selector `Cartier divisor` → VI/40, `MIGRATE`, canonical `YES`.
2. `T02.EXERCISE_CHILDREN`: problem/exercise/solution descendants of the Cartier-divisor section → VI/40.
3. `T02.THEORY_CHILDREN`: theorem-like descendants of the Cartier-divisor section → VI/40.

The neighboring AG9 selectors are deliberately separate: Weil divisors route to VI/39, divisor class groups to VI/41, and line bundles/Picard theory to VI/42.  The broad AG10 divisor/Picard/line-bundle/coherent block is comparison-only overlap routed to VI/39, not a second canonical VI/40 source.  This package therefore preserves the live VI/40 dossier rather than inventing a replacement corpus.

## Canonical live corpus preserved

The apply script is guarded by the live `chapter.tex` blob and modifies only hint/solution regions.  It does not rewrite the theory sections or the canonical exercise/problem/challenge statements.

- 24 exercises: labels `exr:vi40-01` … `exr:vi40-24`.
- 12 dossier problems: labels `prob:vi40-01` … `prob:vi40-12`.
- 5 challenges: labels `chal:vi40-01` … `chal:vi40-05`.

Canonical dossier titles retained:

1. Local equations on `P^1`.
2. A nonreduced effective divisor.
3. Pullback and multiplicity.
4. A failed pullback.
5. Cartier-to-Weil on a UFD.
6. Why `P` on the quadric cone is not Cartier.
7. Tensor law for divisor sheaves.
8. Hyperplane pullback under the Veronese map.
9. Cartier divisor from a line-bundle section.
10. Restriction and line bundles.
11. Effective Cartier divisors are pure codimension one.
12. Recovering a divisor from `O(D)` plus rational section.

## Mathematical refinement

The detailed solution layer strengthens the current short answers without changing their questions.

### Local-equation and effectivity layer

The solutions distinguish carefully among:

- principal ideals and effective Cartier ideals;
- non-zero-divisors versus zero-divisors;
- reduced support versus scheme-theoretic multiplicity;
- restriction of a Cartier divisor versus pullback along a morphism contained in its support.

The nonreduced example `V(x^2)` is treated as an actual infinitesimal thickening, not only as the formal coefficient `2V(x)`.

### Pullback layer

The detailed solutions make the domain of Cartier pullback explicit.  In particular:

- `t=u^4` gives `g^*V(t)=4V(u)`;
- `t=u^3(u-1)^2` gives multiplicities `3[0]+2[1]`;
- pullback to `V(t)` fails because the defining equation becomes zero, which is not in the unit group of the total quotient sheaf;
- principal Cartier divisors pull back to principal Cartier divisors whenever the pullback is defined.

Challenge 2 supplies the associated-point proof of the standard effective-pullback criterion.

### Cartier-to-Weil injectivity

Challenge 1 expands the theorem proof through the normal Noetherian height-one intersection identity

`A = ⋂_{ht p = 1} A_p ⊂ Frac(A)`.

It uses the `S_2` extension property of a normal Noetherian domain to justify the identity, then proves that a Cartier equation with zero order at every height-one prime is a unit.

### Quadric cone

For

`A = k[x,y,z]/(xy-z^2)`, `P=(x,z)`,

the detailed P6/challenge solution gives a local Nakayama argument:

`dim_k P_m / m P_m = 2`,

so `P_m` is not principal and `P` is not Cartier at the vertex.  At the same time, localization at `P` gives `ord_P(x)=2`, and `A/(x)` has only the prime component `P`, hence

`div(x)=2P`.

This is the precise bridge to the nontrivial class-group phenomenon in VI/41.

### Divisor sheaves and rational sections

The detailed solutions prove transition-function compatibility for

`O(D+E) ≅ O(D) ⊗ O(E)`,

construct effective divisors from line-bundle sections, prove

`j^*O_X(D) ≅ O_U(D|_U)`,

and explain why the pair `(L,s)` of a line bundle plus rational trivialization recovers a specific Cartier divisor whereas `L` alone remembers it only up to a principal divisor.

## Scope boundary

This commit stops deliberately at the VI/40 boundary:

- VI/41 will form divisor class groups and measure factoriality/nonfactoriality;
- VI/42 will identify the Picard group with line bundles and connect it systematically to Cartier divisors.

The present package prepares those chapters without importing their quotient-group theory prematurely.
