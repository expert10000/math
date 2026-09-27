# Part II C_REWRITE R2 provenance — Calculus

This batch rewrites the three remaining `C_REWRITE` rows in the Calculus
thematic section.

## CP-II-0129 — Takagi function

Source:
`imports/Downloads/theory-of-real-analysis.tex`, lines 477--556.

The source contains Exercise 3.8 (*) but interleaves several answer/proof
paragraphs with the requested tasks. The canonical pair separates the exercise
into six explicit tasks:

1. identify and sketch the periodic tent function;
2. prove uniform continuity and determine differentiability points of \(h\);
3. prove uniform convergence and uniform continuity of \(T\);
4. construct the unique dyadic interval \([u_n,v_n]\) containing \(x\);
5. determine endpoint values and \(\pm1\) slopes for \(h_i\);
6. prove that the dyadic secant quotients do not converge and conclude nowhere
   differentiability.

A small source-proof clarification is made in part (e): the relevant dyadic
interval contains no half-integer **in its interior**. A half-integer may occur
at an endpoint when the interval length is \(1/2\), which does not spoil
affinity on the closed interval.

The proof of part (f) also makes explicit why these are genuine successive
partial sums: the dyadic intervals are nested, so the previously determined
slopes remain unchanged as \(n\) increases.

## CP-II-0212 — Schwartz functions lie in every \(L^p\)

Source:
`imports/Downloads/theory-of-analysis-FD.tex`, lines 3384--3386.

The migrated atlas range contains only the conclusion

\[
f\in L^p(\mathbb R^n),\qquad
D^\alpha f\in L^p(\mathbb R^n),
\]

but the immediately preceding source paragraph is headed “Integrability
properties” and explicitly assumes

\[
f\in\mathcal S(\mathbb R^n).
\]

The canonical statement restores that hypothesis rather than inventing a new
one. The solution proves the \(p=\infty\) case from the zeroth Schwartz
seminorm and the finite-\(p\) case from rapid decay with \(Np>n\).

## CP-II-0454 — standalone Takagi exercise

Source:
`imports/Downloads/ex3_8_takagi.tex`, lines 11--91.

This is a standalone duplicate source of the same Exercise 3.8 material
represented by CP-II-0129. The migration ledger retains it as a distinct
canonical problem ID, so the reader-facing pair keeps the same six
mathematical tasks while recording its separate provenance.

No migration-ledger provenance status is changed by this batch.
