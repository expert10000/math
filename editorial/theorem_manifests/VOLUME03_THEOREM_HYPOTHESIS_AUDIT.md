# Volume III theorem-hypothesis audit

This pass audits theorem interfaces where missing assumptions are especially
dangerous: measure convergence, product integration, Egorov/Vitali, Sobolev
inequalities and embeddings, weak elliptic problems, and maximum principles.

The adjacent TSV is the release-review manifest. `proved`, `proof-sketch`, and
`deferred` describe the proof status in Volume III.

## Release rules

1. Every theorem identifies its ambient space.
2. Finiteness, sigma-finiteness, domination, uniform integrability, exponent,
   domain, boundary, ellipticity and sign assumptions are theorem data.
3. Deferred advanced results say so explicitly in reader-facing prose.
4. Stronger-than-minimal assumptions are allowed when deliberate and recorded.
5. Operator sign conventions must agree among theorem, examples, dossiers and
   Fourier/PDE formulas.

## Correction made in this pass

III/27 fixes the positive-principal-sign operator convention
\(Lu=a_{ij}D_{ij}u+b_iD_iu+cu\), \(c\le0\).
For this convention comparison uses \(Lu\ge Lv\) together with \(u\le v\) on
the boundary. Dossier 05 previously asked for the reversed operator inequality.
