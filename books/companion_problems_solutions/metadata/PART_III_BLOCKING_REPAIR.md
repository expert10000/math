# Part III blocking solution repair

This record documents the two blocking repairs identified by
`PART_III_SOLUTION_QUALITY_AUDIT.tsv`.

## CP-III-0006 — overmerge boundary repair

The source file is:

`imports/Downloads/theory-of-analysis-FD2.tex`

The actual exercise item is lines **4927--4932**:

- multiindex `alpha` with `|alpha|=k`;
- prove `D^alpha:H^{s+k}(R^n)->H^s(R^n)` is bounded.

The source then closes the enumeration at line 4934. The subsequent
`Theory and Solutions`, Heat Equation 5.9, and Schrödinger 5.10 material are
later sections; they had been overcaptured into one Companion problem.

The canonical repair therefore narrows CP-III-0006 to the actual exercise item
and uses the source's derivative proof at lines **5014--5032** as its mathematical
basis.

The old overmerged solution also contained the false assertion

\[
\mathcal S(\mathbb R^n)=\bigcap_{s\in\mathbb R}H^s(\mathbb R^n).
\]

That statement is removed. The Sobolev intersection is \(H^\infty\), which is
strictly larger than Schwartz space.

## CP-III-0023 — periodic distributions / dual lattice

The original source statement is lines **4409--4528**, with source solution
lines **4529--4887**.

Two source defects are corrected in the canonical reader-facing version.

### Mean-value independence

The source solution incorrectly inferred `psi-psi'=0` from the vanishing of the
periodization. The repaired proof uses the locally finite partition of unity and
periodicity of the distribution to shift every summand back to one fixed cell.

### The \(2\pi\) normalization

The source defines

\[
\Lambda^*=\{\xi:g\cdot\xi\in2\pi\mathbb Z\ \forall g\in\Lambda\},
\]

but simultaneously asks for generators satisfying
\(\lambda_j^*\cdot\lambda_k=\delta_{jk}\). Those two statements are
incompatible.

The canonical repair distinguishes the algebraic dual basis
\(\mu_j\cdot\lambda_k=\delta_{jk}\) from the Fourier dual basis

\[
\lambda_j^*=2\pi\mu_j,
\qquad
\lambda_j^*\cdot\lambda_k=2\pi\delta_{jk}.
\]

Then

\[
\Lambda^*=\left\{\sum_j m_j\lambda_j^*:m_j\in\mathbb Z\right\}.
\]

The repaired solution also proves that a periodic distribution is tempered
before taking its Fourier transform, and keeps the Fourier inversion
normalization explicit instead of absorbing it into unnamed constants.
