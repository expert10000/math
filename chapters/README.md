# Chapter sources

This folder is the main LaTeX chapter workspace.

## Layout

```text
chapters/
  tex/          # 169 TeX files
  figures/      # 639 referenced figures
  manifest.tsv  # original import source -> current clean path
  compile-one.ps1
  compile-all.ps1
```

Raw import snapshots remain in `imports/`. The temporary test merge remains in
`tex_test/` for traceability.

## Naming rule

The source-bucket prefixes (`Downloads_`, `MATH-ALLS-2_`, `MATH_ALLS-3_`) were
removed from TeX filenames.

When two same-title files had identical content, only one clean copy was kept.
When two same-title files had different content, the alternate keeps provenance
as an end suffix, for example:

```text
theory-of-analysis--math-alls-2.tex
```

## Compile

Compile one file from the repository root:

```powershell
.\chapters\compile-one.ps1 -File tex\theory-of-analysis.tex
```

Compile all chapter TeX files:

```powershell
.\chapters\compile-all.ps1
```

Generated PDFs and logs are written to `content/`, which is intentionally
ignored by git except for `PDF_INDEX.tsv`.

See `COMPILE_AUDIT.md` for the latest local compile result.

## Known caveat

Two image names are referenced by the `Exercise_1_2_append` variants but are not
present in the original imports:

- `f_and_psi.png`
- `residual_check.png`
