# Part II blocking-repair provenance

This record documents the first four `D_BLOCKING` repairs produced by the
Part II solution-quality audit.

## CP-II-0061

Source:
`imports/Downloads/theory-of-analysis-functions-II.tex`

- statement: lines 2354--2379;
- migrated source solution: lines 2380--2386.

The source-backed solution range contains only the opening Sobolev norm
definition and does not solve the five requested parts. The canonical repair
keeps the exact mathematical exercise and supplies complete proofs of:

1. Schwartz density in \(H^s\);
2. \(\delta_x\in H^s\iff s<-n/2\);
3. \(H^t\hookrightarrow H^s\) for \(s<t\);
4. boundedness of \(D^\alpha:H^{s+|\alpha|}\to H^s\);
5. \(H^s\)-\(H^{-s}\) duality and
   \(\mathcal S\subset H^s\subset\mathcal S'\).

## CP-II-0083

Source:
`imports/Downloads/theory-of-analysis-functions-II.tex`

- statement: lines 2195--2213;
- migrated source solution: lines 2214--2218.

The migrated solution range only restates the setup. The repair keeps the
two-part statement and supplies:

- smooth dependence of \(u[\phi_y]\) on \(y\), with
  \(D_y^\alpha u[\phi_y]=u[(D_y^\alpha\phi)_y]\);
- the distributional parameter integral identity;
- construction of \(f_j\in C_c^\infty\) with
  \(T_{f_j}\to u\) weak-* by cutoff plus mollification.

## CP-II-0305

Source:
`imports/Downloads/theory-of-real-analysis.tex`

- statement/background: lines 2218--2237;
- source solution: lines 2238--2244.

The numerical conclusion is correct, but the source background says in effect
that any bounded function whose nonzero set has measure zero is Riemann
integrable. That is false; \(\mathbf1_{\mathbb Q}\) is the standard
counterexample.

The canonical repair proves integrability because the discontinuity set is
exactly the horizontal line \(y=0\), which has planar measure zero. It also
gives a direct Darboux proof using an arbitrarily thin strip around that line.

## CP-II-0315

Source:
`imports/Downloads/theory-of-analysis-functions-II.tex`, lines 579--665.

The source asks for
\[
\Delta_i^h u\to D_i u.
\]
With
\[
(\tau_a\phi)(x)=\phi(x-a),
\qquad
(\tau_a u)[\phi]=u[\tau_{-a}\phi],
\]
one instead has
\[
\frac{\tau_{-he_i}\phi-\phi}{h}\to D_i\phi,
\]
so
\[
(\Delta_i^h u)[\phi]\to u[D_i\phi]=-D_i u[\phi].
\]

Therefore the corrected limit is
\[
\boxed{\Delta_i^h u\to -D_i u.}
\]

The source proof also used the false finite-\(h\) equality
\[
\frac{\tau_{-he_i}\phi-\phi}{h}
=
-\frac{\tau_{he_i}\phi-\phi}{h}.
\]
The two sides have opposite first-order limits, but they are not equal at
finite \(h\). The repaired Dirac-mass example provides an independent sign
check.
