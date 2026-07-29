# Compile audit for imported chapters

Last local audit: 2026-07-29.

## Result

```text
Attempted TeX files: 158
PDFs produced:       114
Still failing:       44
```

Generated PDFs and logs are local review artifacts in:

```text
pdfs/imported/
```

That folder is ignored by git.

## Notes

- The permanent source folder is `chapters/imported/`.
- PDFs are generated from `chapters/imported/tex/`.
- Two internal interpolation `\input{...}` paths were fixed after filename cleanup.
- Three `fontspec` documents produced PDFs with XeLaTeX after failing with pdfLaTeX.
- Remaining failures are mostly imported snippets/partials or source-level LaTeX errors.

## Main remaining failure types

```text
21  Undefined control sequence
 9  fontspec requires XeTeX/LuaTeX, but still failed or needs engine-specific cleanup
 4  figure environment undefined
 2  Command \k unavailable in OT1 encoding
 2  Improper \spacefactor
 2  Extra }, or forgotten $
 2  enumitem label error
 1  TikZ key error
 1  Missing $ inserted
```

The detailed local failure report is:

```text
pdfs/imported/compile-failures.tsv
```
