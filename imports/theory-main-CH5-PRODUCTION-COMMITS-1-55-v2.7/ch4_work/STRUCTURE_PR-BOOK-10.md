# PR-BOOK-10 — Canonical Book Structure

## Active book

### Part I — Mathematical Foundations
1. Vectors and Geometry
2. Differential Calculus
3. Vector Calculus

### Part II — Classical Mechanics
4. Motion
5. Newtonian Mechanics

### Part III — Quantum Mechanics
A roadmap placeholder is active. Existing later quantum chapters are preserved under `legacy_sources/chapters_pre_PR_BOOK_10/` for controlled migration.

## Editorial contract
The user's manuscript is the primary source. Editorial work may improve grammar, notation, LaTeX structure, figures, cross-references, examples, and exercises, but must not silently compress a long manuscript into a short summary.

Every mature section should converge toward:

1. Introduction
2. Motivation
3. Historical Context
4. Mathematical Definition
5. Geometric Interpretation
6. Derivation
7. Worked Examples
8. Applications
9. Connections to Physics
10. Common Mistakes
11. Summary
12. Looking Ahead
13. Exercises

Not every early scaffold contains all thirteen blocks yet. Missing blocks must be expanded explicitly rather than hidden.

## Curl location
The complete Curl manuscript is now canonical at:

`chapters/chapter03_vector_calculus/sections/3_03_curl.tex`

It is loaded by:

`chapters/chapter03_vector_calculus/chapter03.tex`

## Preservation
The pre-restructure repository is preserved at:

`legacy_sources/chapters_pre_PR_BOOK_10/`
