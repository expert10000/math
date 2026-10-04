# Part II C_REWRITE — R1 Metric and Topological Foundations

This batch repairs all 16 `C_REWRITE` rows in the Part II thematic section
**Metric and Topological Foundations**.

The editorial target is the Part III convention:

1. descriptive problem name;
2. exact/canonical problem statement;
3. focused theory if needed;
4. complete worked solution;
5. examples if useful;
6. extensions if useful.

## Targets

`CP-II-0086`, `0108`, `0127`, `0249`, `0303`, `0310`, `0322`, `0395`,
`0434`, `0508`, `0523`, `0544`, `0545`, `0547`, `0551`, `0569`.

## Important source repairs

- `CP-II-0086`: the mapped range had swallowed later theory and a new
  mollification exercise; the paired solution was unrelated to the visible
  problem. The canonical pair is the three-part distribution-order exercise.
- `CP-II-0303`: the source's proposed `U_n` family was not a valid open cover
  of the whole function set. The repair uses an explicit separated sequence
  and the cover by sup-norm balls.
- `CP-II-0322`: the source Runge proof only establishes convergence off the
  imaginary-axis interface (and inside the open disk in part (a)); the
  reader-facing statement is normalized to exactly what that proof supports.
- `CP-II-0434`, `0523`, `0544`: isolated source rows are restored from their
  immediate surrounding statement context instead of being left as fragments.
- `CP-II-0310`: the mapped range genuinely contains two consecutive, tightly
  related quotient-space problems; both are retained as one coherent
  vertical-fiber / torus problem.

## Expected audit movement

Before this batch, after the blocking repair, the deterministic audit is
expected to be approximately:

```text
A_STRONG:    70
B_POLISH:   438
C_REWRITE:   62
D_BLOCKING:   0
```

After R1:

```text
A_STRONG:    86
B_POLISH:   438
C_REWRITE:   46
D_BLOCKING:   0
```

The regression validator checks the 16 target rows directly and also checks
those aggregate counts.
