# Repository structure

This document defines the intended Phase 1 layout. Existing files are not moved yet unless a later migration step explicitly does so.

## Curated root material

The root currently keeps the main standalone algebraic-geometry lecture sequence:

```text
theory-of-algebraic-geometry-1.tex
...
theory-of-algebraic-geometry-22.tex
```

This is allowed during stabilization because it preserves the existing workflow.

## Main folders

```text
courses/
```

Future course-ready material. Use this for modules that have learning objectives, lesson order, exercises, and references.

```text
chapters/
```

Main LaTeX chapter workspace. It contains cleaned TeX sources, referenced
figures, compile helpers, and the import manifest.

```text
figures/
```

Current curated figures used by main notes.

```text
notebooks/
```

Future Jupyter or Quarto notebooks for interactive examples, computations, visualizations, and exercises.

```text
styles/
```

Future shared LaTeX style files, macros, theorem environments, and page styling.

```text
templates/
```

Reusable lesson, exercise, and chapter skeletons.

```text
docs/
```

Project documentation, roadmap notes, naming conventions, and contributor-facing explanations.

```text
tools/
```

Helper scripts for validation, conversion, builds, and maintenance.

```text
tests/
```

Future automated checks for links, notebook execution, LaTeX compilation, and repository hygiene.

```text
releases/
```

Generated release PDFs or other intentional public artifacts.

```text
content/pdfs/
```

Local generated PDFs and compile logs, including `content/pdfs/chapters/`.
This folder is ignored by git and is used for review builds, not source
control.

```text
imports/
```

Raw imported material, legacy snapshots, source archives, and uncurated content. Files in this folder are not automatically part of the curated course.

```text
archive/
```

Retired curated material that should remain available but no longer belongs to the active sequence.

## Migration principle

Move slowly:

1. preserve original standalone files;
2. document the target structure;
3. extract shared styles;
4. migrate one chapter at a time;
5. verify compilation before removing old wrappers.
