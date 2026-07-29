# Compile audit for chapters

Last local audit: 2026-07-29.

## Result

```text
Attempted TeX files: 169
PDFs produced:       125
Still failing:       44
```

Generated PDFs and logs are local review artifacts in:

```text
content/pdfs/chapters/
```

That folder is ignored by git.

## Notes

- The permanent source folder is `chapters/`.
- PDFs are generated from `chapters/tex/`.
- Two internal interpolation `\input{...}` paths were fixed after filename cleanup.
- Three `fontspec` documents produced PDFs with XeLaTeX after failing with pdfLaTeX.
- Remaining failures are mostly snippets/partials or source-level LaTeX errors.

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
content/pdfs/chapters/compile-failures.tsv
```
