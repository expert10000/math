# TikZ quick reference

```latex
\draw[axis] (0,0) -- (5,0) node[right] {$x$};
\draw[vector] (0,0) -- (3,2) node[above] {$\mathbf A$};
\draw[force] (2,1) -- (4,1) node[right] {$\mathbf F$};
\draw[field] (0,0) -- (0,2) node[above] {$\mathbf E$};
\draw[construction] (3,0) -- (3,2);
```

## Standard semantic mapping

- `vector` — geometric and physical vectors
- `force` — forces and momentum-transfer arrows
- `field` — electric, magnetic, gradient, or flow fields
- `trajectory` — paths in configuration space
- `quantum` — wavefunctions and quantum-state curves
- `construction` — projections and auxiliary geometry
- `boundary` — material, device, and domain boundaries
- `virtual` — virtual, inferred, or comparison constructions
