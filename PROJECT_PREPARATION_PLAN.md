# Algebraic Geometry Project Preparation Plan

## Goal

Prepare a clean LaTeX project that reproduces the style, structure, and compilation behavior of the standalone files `theory-of-algebraic-geometry-3.tex` and `theory-of-algebraic-geometry-4.tex`, while making future chapters easier to maintain.

The project should keep the visual identity of the current notes:

- `article` class, `12pt`, `a4paper`
- one-inch margins
- Latin Modern fonts
- `microtype`
- blue internal links
- theorem/proposition/definition/example/remark/warning environments
- TikZ and `tikz-cd` diagrams
- compact list spacing
- no paragraph indentation and moderate paragraph spacing
- fancy page headers with the chapter title and page number
- table of contents at the front

## Source Model

Use these files as the style reference:

- `theory-of-algebraic-geometry-3.tex`
- `theory-of-algebraic-geometry-4.tex`

Both files compile successfully from this workspace with `pdflatex`.

Current warning profile is acceptable for initial migration:

- overfull boxes in long formulas or headings
- `hyperref` PDF-string warnings where math appears in section titles
- `\r invalid in math mode` warnings in some formulas

The first clean-project milestone is matching compile success, not eliminating every warning.

## Target Layout

Create this structure:

```text
MATH/
  main.tex
  latexmkrc
  styles/
    preamble.tex
    macros.tex
    theorem_environments.tex
    page_style.tex
  chapters/
    algebraic_geometry_03.tex
    algebraic_geometry_04.tex
  figures/
  build/
  archive/
    standalone_sources/
```

## Style Extraction

Move shared LaTeX setup out of the standalone files into `styles/`.

### `styles/preamble.tex`

Contains packages and document-wide settings:

- `fontenc`
- `inputenc`
- `lmodern`
- `microtype`
- `geometry`
- `array`
- `booktabs`
- `amsmath`, `amssymb`, `amsthm`, `mathtools`
- `tikz`
- `tikz-cd`
- `xcolor`
- `hyperref`
- `bookmark`
- `enumitem`
- paragraph spacing
- TOC and section numbering depth

### `styles/macros.tex`

Contains common notation:

- `\Spec`
- `\Proj`
- `\Hom`
- `\id`
- `\im`
- `\coker`
- `\colim`
- `\Ab`
- `\PreSh`
- `\Sh`
- `\Sch`
- `\Rings`
- `\AffSch`
- `\ZZ`
- `\RR`
- `\CC`
- `\PP`
- `\OO`
- `\OOX`
- `\F`, `\G`, `\A`, `\B`, `\C`, `\I`
- `\GammaU`
- `\GammaX`

Resolve duplicate or conflicting definitions during extraction. In particular, standardize `\Spec` and `\Proj` as `\DeclareMathOperator`.

### `styles/theorem_environments.tex`

Use one theorem environment scheme consistently:

```tex
\newtheoremstyle{notespace}{6pt}{6pt}{\normalfont}{}{\bfseries}{.}{0.5em}{}
\theoremstyle{notespace}
\newtheorem{definition}{Definition}[subsection]
\newtheorem{theorem}[definition]{Theorem}
\newtheorem{proposition}[definition]{Proposition}
\newtheorem{lemma}[definition]{Lemma}
\newtheorem{corollary}[definition]{Corollary}
\newtheorem{remark}[definition]{Remark}
\newtheorem{example}[definition]{Example}
\newtheorem{warning}[definition]{Warning}
```

This keeps the numbering style used by `theory-of-algebraic-geometry-3.tex` and adds `lemma`, which appears in `theory-of-algebraic-geometry-4.tex`.

### `styles/page_style.tex`

Contains `fancyhdr` setup. It should use a variable command for the running header:

```tex
\newcommand{\runningtitle}{Theory of Algebraic Geometry}
\pagestyle{fancy}
\fancyhf{}
\lhead{\runningtitle}
\rhead{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\setlength{\headheight}{14.5pt}
```

Each chapter file can redefine `\runningtitle` before content begins if needed.

## Main Document

Create `main.tex` as the project entry point:

```tex
\documentclass[12pt,a4paper]{article}

\input{styles/preamble}
\input{styles/macros}
\input{styles/theorem_environments}
\input{styles/page_style}

\title{\bfseries Theory of Algebraic Geometry\\
\large Lecture notes with examples}
\author{}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\clearpage

\input{chapters/algebraic_geometry_03}
\clearpage
\input{chapters/algebraic_geometry_04}

\end{document}
```

## Chapter Structure

Each chapter should follow the working pattern from files 3 and 4:

1. Problem or construction section
2. Problem statement
3. Solution
4. Theory section
5. Examples section
6. Diagrams, charts, and tables section
7. Final summary or dictionary

Recommended section skeleton:

```tex
\section{Main Topic}

\subsection*{Problem statement}

\textbf{Solution.}

\section{Theory of Main Topic}

\section{Examples}

\section{Diagrams, Charts, and Tables}

\section{Summary}
```

Use `\texorpdfstring{...}{...}` for section titles containing math, especially if the title appears in the PDF bookmarks.

## Migration Steps

1. Keep the copied standalone files unchanged as source references.
2. Create `styles/` and extract the shared preamble.
3. Create `chapters/algebraic_geometry_03.tex` from the body of `theory-of-algebraic-geometry-3.tex`.
4. Create `chapters/algebraic_geometry_04.tex` from the body of `theory-of-algebraic-geometry-4.tex`.
5. Remove each chapter's old document wrapper:
   - `\documentclass`
   - package imports
   - macro definitions now held in `styles/`
   - `\title`
   - `\author`
   - `\date`
   - `\begin{document}`
   - `\maketitle`
   - `\tableofcontents`
   - final `\end{document}`
6. Add `main.tex`.
7. Add `latexmkrc`.
8. Compile `main.tex`.
9. Compile individual standalone files only as regression references, not as project entry points.

## Build Commands

Preferred:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Fallback:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run twice when using `pdflatex` so the table of contents and references settle.

## Validation Checklist

- `main.tex` compiles from `MATH/`
- output PDF is created in `MATH/` or `build/`
- table of contents includes both migrated chapters
- section numbering is consistent
- theorem numbering is consistent within subsections
- TikZ and `tikz-cd` diagrams compile
- no missing file errors
- no package conflicts from duplicate macro definitions
- visual style matches the standalone PDFs
- standalone source files remain available as references

## Warning Cleanup After Migration

After the first successful project build, clean warnings in this order:

1. Replace math-heavy section titles with `\texorpdfstring`.
2. Fix `\r invalid in math mode` occurrences.
3. Break or resize overfull formulas.
4. Shorten overfull headings.
5. Re-run `latexmk` until no fatal errors remain and warning count is understood.

## Immediate Next Step

Build the skeleton project using chapters 3 and 4 as the first migrated chapters, then compare the generated PDF against the current standalone PDFs for style and structure.
