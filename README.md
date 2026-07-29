# expert10000/math

This repository collects mathematical lecture notes, worked problems, diagrams, and source material for a future structured learning resource.

The current core sequence is the standalone LaTeX series:

- `theory-of-algebraic-geometry-1.tex` through `theory-of-algebraic-geometry-22.tex`
- `exact_sequences_sheaves_reorganized_full/exact_sequences_sheaves_reorganized_full.tex`
- supporting figures in `figures/`
- legacy and imported source material in `imports/`

## Project goal

The first roadmap goal is to turn the repository from a manuscript archive into a maintainable educational project:

1. preserve the existing mathematical material;
2. document what belongs where;
3. make future contributions predictable;
4. prepare for a course/site structure with LaTeX, Markdown, notebooks, and figures;
5. keep advanced and legacy imports separate from curated course material.

## Current status

Phase 1 is repository stabilization.

This means:

- public-facing project description;
- license status documented;
- contribution rules;
- naming conventions;
- initial folder scaffold;
- clear separation between curated material and raw imports.

No publication stack has been chosen yet. Candidate stacks include Jupyter Book, Quarto, Hugo, and Docusaurus. That decision belongs to the next phase.

## Repository map

```text
.
|-- theory-of-algebraic-geometry-*.tex     # current curated standalone notes
|-- exact_sequences_sheaves_reorganized_full/
|-- chapters/imported/                     # cleaned imported TeX sources
|-- figures/                               # existing curated figures
|-- imports/                               # legacy/imported snapshots; not yet curated
|-- pdfs/                                  # local generated PDFs; ignored by git
|-- releases/                              # intentional published release artifacts
|-- courses/                               # future course modules
|-- chapters/                              # future modular LaTeX chapter sources
|-- notebooks/                             # future Jupyter/Quarto notebooks
|-- styles/                                # future shared LaTeX/style files
|-- templates/                             # reusable lesson/exercise templates
|-- docs/                                  # project documentation
|-- tools/                                 # future helper scripts
|-- tests/                                 # future validation checks
|-- archive/                               # retired or superseded curated material
```

See:

- `docs/REPOSITORY_STRUCTURE.md`
- `docs/NAMING_CONVENTIONS.md`
- `CONTRIBUTING.md`

## Working rule for new content

For now, add new curated algebraic-geometry chapters at the repository root only if they continue the existing `theory-of-algebraic-geometry-N.tex` sequence.

Cleaned imported TeX material lives in `chapters/imported/`. Raw snapshots stay
inside `imports/` until reviewed.

## License

The license has not yet been finalized. See `LICENSE.md`.
