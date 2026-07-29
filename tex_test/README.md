# tex_test

Non-destructive test merge of imported TeX material.

This folder consolidates the three source buckets from:

- `imports/ALL_TEX_AND_FIGURES/tex/Downloads`
- `imports/ALL_TEX_AND_FIGURES/tex/MATH-ALLS-2`
- `imports/ALL_TEX_AND_FIGURES/tex/MATH_ALLS-3`

The original import folders are untouched.

## Layout

```text
tex_test/
  tex/       # 231 normalized document-level TeX files
  figures/   # referenced compile-ready flattened figure assets
  build/     # local build output
  manifest.tsv
  compile-one.ps1
```

## Compile from this folder

Run from the repository root:

```powershell
.\tex_test\compile-one.ps1 -File tex\Downloads_theory-of-analysis.tex
```

Or from inside `tex_test/`:

```powershell
.\compile-one.ps1 -File tex\Downloads_theory-of-analysis.tex
```

Build output goes to `tex_test/build/`.

The `figures/` folder is intentionally pruned to the assets referenced by the
merged TeX files, rather than copying every image from the original import
bucket.

## Known caveat

Most image references were already rewritten to `figures/...` by `imports/COMPILE_READY`.
A small number of legacy TeX files still reference missing image names directly, currently:

- `f_and_psi.png`
- `residual_check.png`

Those missing assets should be resolved during the compile audit.
