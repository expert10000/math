# Naming conventions

Stable names make the project navigable. Prefer names that reveal subject, order, and role.

## General rules

Use:

- lowercase words;
- ASCII letters and numbers;
- hyphens or underscores consistently within a family;
- leading numbers only when order matters.

Avoid:

- spaces in new filenames;
- names like `final`, `new`, `copy`, `draft2`, or `fixed`;
- local-language-only names for structural files;
- generated build suffixes in committed source names.

## Current standalone sequence

The existing algebraic-geometry sequence uses:

```text
theory-of-algebraic-geometry-N.tex
```

Continue this pattern only for curated standalone chapters in the same sequence.

Examples:

```text
theory-of-algebraic-geometry-23.tex
theory-of-algebraic-geometry-24.tex
```

## Future modular chapters

When the project moves into a modular structure, use:

```text
chapters/algebraic_geometry_01.tex
chapters/algebraic_geometry_02.tex
```

For course folders:

```text
courses/algebraic-geometry/01-foundations/
courses/algebraic-geometry/02-affine-schemes/
```

## Figures

Use descriptive names:

```text
fig_complex_torus_lattice.png
fig_exact_sequence_stalks.svg
fig_weierstrass_covering_diagram.pdf
```

If a figure belongs to a specific course module later, place it next to that module's assets.

## Templates

Use:

```text
lesson-template.md
exercise-template.md
chapter-template.tex
```

## Releases

Use versioned names:

```text
releases/algebraic-geometry-v0.1.pdf
releases/project-roadmap-v0.1.pdf
```

## Imports

Imported snapshots may keep their original names, but each new import folder should include a short README explaining:

- source;
- date added;
- whether quantum/QM material is included;
- whether it has been reviewed;
- what should eventually be extracted.

