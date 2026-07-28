# Theory of Quantum Mechanics - Book Style Guide

Version: PR-BOOK-13

## 1. Numbered hierarchy

Only the following levels are numbered:

1. Part
2. Chapter
3. Section
4. Subsection

A subsubsection is not numbered by default. A concept below subsection level uses `\booktopic{Title}` or a semantic environment. A subsubsection is permitted only when it contains substantial, independently navigable material (normally at least half a page).

## 2. Semantic vocabulary

Use these canonical environments:

- `bookdefinition`
- `bookproperty`
- `bookrule`
- `bookprinciple`
- `bookremark`
- `bookexample`
- `bookinsight`
- `bookhistory`
- `bookwarning`
- `booksummary`

Legacy environments remain supported for existing chapters, but new writing should use the canonical names.

## 3. Cross-references

Do not write "see above" or "the figure below". Add a label and use `\cref{...}`.

Label prefixes:

- `ch:` chapter
- `sec:` section
- `subsec:` subsection
- `fig:` figure
- `tab:` table
- `eq:` equation
- `thm:` theorem
- `def:` definition
- `ex:` example
- `exc:` exercise

## 4. Equations

Use numbered equations only when they are referenced later or are structurally important. Use `align` for multi-line derivations and align at meaningful relation symbols. Avoid manual equation numbers.

## 5. Figures

Prefer TikZ, PGFPlots, SVG, or PDF vector artwork. Every figure requires a caption, a unique `fig:` label, and explanatory discussion in the surrounding text. Avoid forced `[H]` placement unless normal floating demonstrably fails.

## 6. Chapter completion

A finished chapter should include:

- chapter opening and roadmap;
- learning objectives;
- coherent derivations and physical interpretation;
- examples and common-mistake guidance where useful;
- summary and formula/notation review as appropriate;
- exercises;
- looking-ahead transition;
- complete labels and references;
- a clean build with no undefined references.

## 7. Repository policy

The Git repository is the source of truth. Build products, release ZIPs, and release PDFs are distributed through GitHub Releases. A focused pull request should address one editorial or technical objective.
