# Canonical Repository Layout

The repository now uses a single-source modular architecture.

- `main.tex` — concise master build file.
- `config/preamble.tex` — all packages, styles, theorem environments, and commands.
- `frontmatter/` — preface, notation, constants, roadmap, and other front matter.
- `chapters/chapterXX_name/chapterXX.tex` — one canonical file per chapter.
- `chapters/chapterXX_name/sections/` — one canonical file per section.
- `figures/` and chapter-local figure files — visual assets.
- `references.bib` — project bibliography.
- `glossary/entries.tex` — glossary and acronym definitions.
- `generated/chapters_current.tex` — currently enabled chapters.
- `BOOK_STATE.md` — generated progress report.
- `legacy_sources/monolithic/` — preserved historical source, never edited as canonical content.
- `Makefile`, `latexmkrc`, `.gitignore` — local, Overleaf, and Git workflow.

## Editing rule

New prose belongs only in the appropriate section file. Chapter files should
normally contain the chapter opening and `\input{...}` statements. Do not place
new chapter prose directly in `main.tex`.
