# VI/30 Full-Solutions Audit — Dimension of Schemes

## Standard

This refinement continues the VI/24–VI/29 detailed-proof standard.

- 26/26 exercise solutions are expanded to worked derivations.
- 20/20 problem dossiers receive detailed proofs.
- 5/5 challenges receive complete solutions.
- Reader/full-solutions separation is normalized.

## Legacy and corpus ownership

Two numbered AG8 anchors are chapter-owned here:

1. **AG8 Problem 2(d)** — nonempty-open dimension invariance for a variety.
2. **AG8 Problem 3(d)** — the corresponding general-scheme counterexample.

The live P1 provenance said `AG8-P2a`, but the chapter simultaneously identifies the counterexample as
`AG8-P3d` and reserves AG8 Problem 2(a)–(c) for VI/31–VI/32.  This refinement corrects P1 to `AG8-P2d`.

VI/27 retains ownership of the function-field construction.  VI/30 owns the dimension-side theorem

`dim X = trdeg_k K(X)`

for varieties.

## Mathematical strengthening

The detailed layer now proves:

- global scheme dimension agrees with affine Krull dimension;
- closed and open subset inequalities;
- component and disjoint-union formulas;
- reduction invariance;
- normalization invariance globally via affine-cover dimension;
- the finite-type theorem `dim X = trdeg_k K(X)` without circular use of open invariance;
- nonempty-open invariance for varieties;
- the AG8-P3d counterexample;
- the integral Noetherian non-finite-type counterexample `Spec k[x,y]_(x)`;
- dominant-map dimension inequality;
- equality for generically finite maps;
- finite-surjective dimension invariance;
- product with affine space;
- infinite-dimensional disjoint unions.

## Challenge strengthening

The challenge layer now includes:

- a hypothesis audit for open-dimension invariance;
- the formula
  `dim X - dim Y = trdeg_{K(Y)} K(X)`
  for dominant maps of varieties;
- a scheme of infinite global dimension whose quasi-compact opens all have finite dimension;
- explicit product splitting over `R` using `C tensor_R C = C x C`;
- a theorem/counterexample map distinguishing unconditional, integral-extension, and variety-only dimension statements.

## Boundary discipline

Reserved for later chapters:

- **VI/31** — codimension and dimension/codimension additivity.
- **VI/32** — geometric local dimension and tangent-space interaction.
- **VI/39–VI/41** — Weil divisors, Cartier divisors, and divisor class groups.

Height-one valuation criteria and divisor theory are not pulled into VI/30.
