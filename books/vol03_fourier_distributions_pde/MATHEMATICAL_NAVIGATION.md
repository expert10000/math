# Volume III — Mathematical Navigation

This sidecar adds cross-volume prerequisites, continuations, and see-also links without changing the frozen theorem/chapter text.

## Comes from

No curated incoming cross-volume bridge.

## Leads to

- **III/20 — Weak Derivatives** → **VII/40 — The Heat Method** — Weak derivatives and PDE methods connect to geometric heat methods.

## Numerical interpretation inherited from Volumes I--II

Volume III applies the series-wide distinction between exact analytic
identities and conclusions inferred from finite computation.

The principal numerical hotspots are:

- **III/09 Fourier Series:** distinguish the exact orthogonal projection
  \(S_Nf\) from coefficients inferred from sampled data; state truncation,
  sampling, and aliasing assumptions separately.
- **III/13 Plancherel and \(L^2\) Fourier Theory:** exact norm preservation is
  the reference identity; computed transforms should report reconstruction and
  energy defects with their grid, normalization, and tolerance.
- **III/23 Weak Boundary-Value Problems:** distinguish discretization error from
  algebraic solver error; relate residuals to solution error only through the
  correct dual norm and a stability/coercivity estimate.
- **III/28 Spectral and Transform Methods for PDE:** check computed eigenpairs
  with eigen-residuals and orthogonality defects, distinguish continuum from
  discretized spectra, and interpret resolvent residuals together with
  distance-to-spectrum conditioning.

Measure theory, exact distribution identities, and functional-analytic
existence theorems remain exact statements.  Numerical caveats are attached
only where finite truncation, sampling, discretization, or linear algebra is
actually used.

## Reading principle

These links are editorial navigation, not formal logical dependencies. They identify especially useful conceptual transitions in the frozen 256-chapter series.
