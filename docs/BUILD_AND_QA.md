# Reproducible build and document QA

The canonical build is the eight `book.tex` wrappers in `books/vol01_*` through
`books/vol08_*`.  Use a clean checkout of the target revision; generated PDFs,
logs, and QA reports belong in ignored build output and are never source inputs.

## Required tools

- Python 3.10 or newer (standard library only)
- a TeX distribution with `latexmk` and `pdflatex` available on `PATH`

The root [`.latexmkrc`](../.latexmkrc) is loaded explicitly by the build wrapper.
It fixes PDF mode, recorder output, noninteractive error handling, and the maximum
number of convergence passes.  The QA report records the detected tool versions,
Python version, platform, UTC timestamp, and exact Git commit.

## Canonical command

From the repository root in PowerShell:

```powershell
.\BUILD_ALL.ps1 -CanonicalOnly -CleanFirst
```

The command builds every canonical volume, writes a stable inventory to
`reports/series/BUILD_I_VIII.tsv`, gathers PDFs under `build/pdf/`, and then runs
the document QA.  The transient QA results are written to:

```text
build/qa/document-qa.json
build/qa/document-qa.md
build/qa/latex-environment.json
```

Use `-SkipQa` only while diagnosing a TeX failure.  The batch-file entry point is
also available as `BUILD_ALL.bat -CanonicalOnly -CleanFirst`.

## QA contract

For each active canonical TeX graph, the QA checks that inputs resolve, labels are
unique, and references resolve.  It reads the fresh `book.log` for undefined
references/citations, duplicate labels, missing assets, undefined control
sequences (the compiler-detectable boundary for notation/macros), and fatal TeX
errors.  It also scans reader-facing TeX for unambiguous production-workflow
phrases.  The check deliberately permits the C02 source/provenance policy in
front matter and C06 pedagogical phrases such as “proof dossier”; neither is
repository bookkeeping in mathematical exposition.

The build inventory gives deterministic collection names of the form
`volNN_name_book.pdf`.  A build fails if any canonical wrapper fails; its inventory
and QA report identify the affected volume and reason.  Run release-specific
freeze and archival checks separately; those are not replaced by this development
gate.
