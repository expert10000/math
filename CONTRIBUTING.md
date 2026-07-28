# Contributing

This project is being stabilized. Contributions should make the repository clearer, more accurate, and easier to learn from.

## Before adding material

Ask three quick questions:

1. Is this curated course/manuscript material, or is it a raw import?
2. Does it duplicate something already present?
3. Does it follow the naming conventions in `docs/NAMING_CONVENTIONS.md`?

If the material is a raw snapshot, generated build output, or exploratory draft, place it under `imports/` or wait for review.

## What to avoid

Do not add:

- build artifacts such as `.aux`, `.log`, `.out`, `.toc`, `.synctex.gz`;
- generated PDFs unless they are intentional releases;
- duplicate archive folders without a short explanation;
- files with unclear names such as `final2.tex`, `new.tex`, or `copy.tex`;
- quantum/QM material unless the roadmap explicitly reopens that scope.

## LaTeX conventions

Use:

- meaningful section headings;
- consistent theorem, definition, example, proof, and remark environments;
- `amsmath`, `amssymb`, `amsthm`, and `mathtools` when needed;
- `\texorpdfstring{...}{...}` for section titles with mathematical notation;
- short comments only where they clarify structure.

Avoid:

- duplicating large preambles between future modular chapters;
- hard-coded absolute paths;
- image references to files not committed in the repository;
- hidden dependencies on local editor/build settings.

## Figures

Place curated figures in `figures/` or, after the course structure is active, in the appropriate course asset folder.

Use descriptive lowercase names, for example:

```text
fig_sheaf_exact_sequence_stalks.png
fig_complex_torus_lattice.svg
```

Every figure used by a source file should be referenced with a relative path.

## Review checklist

Before a commit:

- run `git status --short` and check that only intended files are included;
- confirm that generated build artifacts are excluded;
- check that new files have stable names;
- if adding LaTeX, confirm whether it compiles or note that it has not been tested;
- if adding figures, confirm the source file references them correctly.

## Commit messages

Prefer short, concrete messages:

```text
Add algebraic geometry chapters 12-22
Document repository structure
Add contribution guidelines
```

