# Compile-Ready Import

This folder is generated from imports/ALL_TEX_AND_FIGURES.

- Top-level *.tex files are document-level TeX files, flattened with collision-safe names.
- igures/ contains all copied image assets and figure/TikZ .tex files, also flattened with collision-safe names.
- Copied TeX files were rewritten so resolvable \includegraphics, \input, and \include references point at the flattened names.
- Original import folders were not modified.

Manifests:

- TEX_FILES.tsv: document TeX mapping.
- FIGURE_FILES.tsv: figure/image mapping.
- REWRITES.tsv: rewritten references.
- MISSING_REFERENCES.tsv: references not resolved.
- AMBIGUOUS_REFERENCES.tsv: references with more than one possible target.
