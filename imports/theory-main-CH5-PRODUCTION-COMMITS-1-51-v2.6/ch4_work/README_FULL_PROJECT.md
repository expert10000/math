# Theory of Quantum Mechanics — Full Recovered Project

This project merges the four supplied PR archives in chronological order:

1. `PR-BOOK-05-Illustration-Library`
2. `PR-BOOK-05.1A-Vector-Foundations`
3. `PR-BOOK-05.1B-Advanced-Vector-Operations`
4. `PR-BOOK-05.1C-Vector-Chapter-Completion`

Later PR files replace earlier versions of the same path. No supplied source
file was discarded: the exact original ZIP archives are retained under
`source_archives/`.

## Primary manuscript

Compile:

```bash
pdflatex main.tex
pdflatex main.tex
```

`main.tex` is an exact promoted copy of:

```text
integration/Theory_of_Quantum_Mechanics_v2_PR04_visual.tex
```

The current integrated manuscript contains the front matter and Chapters 1–4:

1. Vectors and Coordinate Systems
2. Motion in Space and Time
3. Calculus and Differential Operators
4. Newton's Laws of Motion

It also contains a visual-language preview for later quantum-mechanics chapters.

## Illustration library

The chapter illustration folders remain in their original structure. Chapter 1
includes the completed vector-foundations, advanced-operations, summary,
worked-example, and exercise additions supplied through PR-BOOK-05.1A–05.1C.

## Important preservation rule

Do not use chat history as the authoritative book source. Update the `.tex`
files in this project, then create a new ZIP or Git commit after every completed
section.

## PR-BOOK-06.1 — Chapter 1 Master Structure

The Chapter 1 expansion specification has been integrated at:

```text
documentation/PR-BOOK-06.1.md
```

It sets an 80–100 page target, retains the completed 25-figure library, and
establishes staged releases PR-BOOK-06.2 through PR-BOOK-06.6 for foundations,
vector algebra, products, transformations, fields, applications, historical
notes, programming companions, and end-of-chapter material.
