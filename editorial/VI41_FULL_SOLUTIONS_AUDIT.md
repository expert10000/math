# VI/41 — Divisor Class Groups: full-solutions audit

## Scope and provenance

- Canonical chapter: `books/vol06_algebraic_geometry/chapters/ch41_divisor_class_groups/chapter.tex`
- Audited live blob on `main`: `b94fbee2da713653b8b5aecbfd98c6ea33cc83a2`
- `editorial/CHAPTER_STATUS.tsv` marks VI/41 as `DRAFTED`, `LEGACY_SOURCE_IDENTIFIED`, with **3 mapped rules**.
- The chapter records the canonical source routing as the AG9 **class group / divisor class** section plus its theorem-like and exercise/problem descendants.
- VI/39 remains the source for Weil divisors; VI/40 remains the source for Cartier divisors; full Picard-group theory stays in VI/42.

## Canonical corpus retained

The package does not replace or renumber the live corpus.

- 24 canonical exercises: `exr:vi41-01` through `exr:vi41-24`
- 12 canonical dossier problems: `prob:vi41-01` through `prob:vi41-12`
- 5 canonical challenges: `chal:vi41-01` through `chal:vi41-05`

The 12 dossier titles retained literally are:

1. Class group of a localization
2. The cone relation from \(x/z\)
3. Why \(D(x)\) forgets the cone class
4. Why deleting the vertex does not forget the cone class
5. A factoriality test
6. Hyperplanes and rational functions
7. A degree-\(d\) hypersurface
8. Local versus global factoriality
9. Torsion and a Cartier multiple
10. Codimension-one deletion
11. The local cone obstruction
12. A divisor-class diagnostic

## Refinement supplied

The existing short inline hints and solutions are moved behind full-solutions guards and replaced by detailed solution files.

- `exercise_hints.tex`: 24 hints
- `exercise_solutions.tex`: 24 detailed solutions
- `problem_solutions.tex`: 12 detailed dossier solutions
- `challenge_solutions.tex`: 5 complete challenge solutions

The expanded mathematics includes:

- the UFD criterion through height-one valuations and the Krull intersection formula;
- the localization exact sequence with explicit valuation compatibility;
- the quadric-cone computation
  \[
  \operatorname{div}(x)=2L,\quad
  \operatorname{div}(z)=L+M,\quad
  \Cl(A)\cong\mathbb Z/2;
  \]
- the \(x\)-adic parity obstruction proving the cone generator nonprincipal;
- the local nonfactoriality obstruction at the vertex via Nakayama's lemma;
- codimension-two invariance;
- two proofs of \(\Cl(\mathbb P^n)\cong\mathbb Z\);
- the distinction between torsion, Cartier multiples, and \(\mathbb Q\)-Cartier divisors;
- the local-class-group criterion for a Weil divisor to be Cartier, preparing VI/42.

## Guard layout

The transformed chapter keeps every canonical statement and inserts:

- `\ifdefined\IncludeExerciseHints`
- `\ifdefined\IncludeExerciseSolutions`
- `\ifdefined\FullProblemDossiers`
- `\ifdefined\IncludeChallengeSolutions`

The Volume VI full-solutions wrapper already defines these switches.

## Safety

The apply script refuses to modify an unexpected VI/41 chapter blob. If the guard fails, inspect the current repository state rather than forcing the patch.
