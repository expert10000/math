# Part III `C_REWRITE` provenance

This file records the source basis for the four substantial Part III rewrites.

## CP-III-0001

Source: `imports/Downloads/theory-of-analysis-numbers.tex`, lines 4359--4385.

The source is an example list rather than a worked exercise. The canonical rewrite keeps
the source categories and examples, supplies the missing Baire-category arguments, and
explicitly corrects one false literal consequence: every vector in a vector space lies in
a one-dimensional subspace, so the correct claim concerns the complement of a
**prescribed countable family** of finite-dimensional subspaces.

## CP-III-0013

Source: `imports/Downloads/theory-of-analysis-FD2.tex`.

- Exercise 4.3: lines 2136--2212.
- General theory begins at line 2213.
- Tempered-distribution theory begins at line 2329.

The canonical pair is therefore narrowed to Exercise 4.3 itself. The source's part (a)
prints `(F[g],F[g])`; the intended Plancherel pairing is `(F[f],F[g])`.

## CP-III-0014

Source: `imports/Downloads/theory-of-analysis-FD2.tex`.

- Exercise 4.1: lines 1576--1728.
- Exercise 4.2 begins at line 1729.

The canonical pair is narrowed to Exercise 4.1. The source sentence calling
`(1+4 pi^2 xi^2)^(-1)` "rapidly decaying" is corrected: it has polynomial decay,
while its smooth symbol estimates are what preserve the Schwartz class under multiplication.

## CP-III-0016

Source: `imports/Downloads/theory-of-analysis-FD.tex`.

- Exercise 2.5 statement: lines 4326--4407.
- Source-backed solution/exposition begins at line 4408.

The canonical rewrite preserves the exact mathematical chain of the exercise but removes
duplicated roadmaps and examples from the paired solution. The result is one coherent proof
of the five requested stages.
