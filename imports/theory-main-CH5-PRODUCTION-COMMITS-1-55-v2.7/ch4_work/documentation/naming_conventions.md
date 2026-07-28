# Naming conventions

## File names

`figNN_short_descriptive_name.tex`

Examples:

- `fig05_position_vector.tex`
- `fig14_cross_product_direction.tex`
- `fig09_gradient_contours.tex`

## Labels

Use stable chapter-prefixed labels:

```latex
\label{fig:ch01-05-position-vector}
```

## Rules

- Lowercase file names.
- Use underscores, never spaces.
- Keep one main concept per file.
- Do not put `figure` environments inside illustration body files.
- Illustration files should contain only the TikZ/PGFPlots body.
- Captions and labels belong to the manuscript or calling template.
