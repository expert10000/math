# PR-BOOK-05 — Complete Illustration Library

This package is the scalable TikZ illustration foundation for
**Theory of Quantum Mechanics**.

## Current classical inventory

- Chapter 1 — Vectors: 25 figure files
- Chapter 2 — Motion: 25 figure files
- Chapter 3 — Calculus: 30 figure files
- Chapter 4 — Newton: 25 figure files

Total current-chapter inventory: **105 figure files**.

A small set contains initial TikZ drafts. The remaining files are deliberately
structured placeholders with fixed names, labels, and chapter locations.

## Quick start

From the project root:

```latex
\input{styles/prbook05_visual_library.tex}
```

Insert a figure body:

```latex
\begin{figure}[tbp]
  \centering
  \input{chapter01_vectors/fig08_vector_addition_triangle.tex}
  \caption{Triangle rule for vector addition.}
  \label{fig:vector-addition-triangle}
\end{figure}
```

## Integration

The `integration/` folder includes the latest PR-BOOK-04 source and compiled PDF
when those files were available during package creation.

## Recommended workflow

1. Select one chapter.
2. Change figure status in `FIGURE_INDEX.xlsx`.
3. Replace the placeholder node with the final TikZ construction.
4. Compile the corresponding file in `examples/`.
5. Review scientific accuracy, labels, line weights, and caption.
6. Set status to `Review` and then `Complete`.
