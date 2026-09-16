# Volume VII computational-geometry validation

This package provides executable, deterministic reference checks for the
computational-geometry material in VII/38–VII/42.  It is a validation harness,
not a replacement for a production mesh-processing library.

## Scope and numerical contracts

| Chapter | Executable representative | Contract |
|---|---|---|
| VII/38 | intrinsic edge lengths and disconnected-query handling | an edge path is an upper bound for the flat intrinsic reference |
| VII/39 | Dijkstra edge-graph paths against a planar exact reference | never underestimate; report anisotropy error rather than call it exact mesh distance |
| VII/40 | deterministic graph heat diffusion | source heat is maximal and the heat-derived ordering is source-consistent |
| VII/41 | cotangent Laplacian on a planar mesh | constants and interior affine coordinate fields have zero residual to tolerance |
| VII/42 | ridge/valley candidates on sampled curvature profiles | extrema are stable under the stated bounded deterministic noise case |

The flat-square reference is exact only because the mesh is planar.  The package
does **not** label an edge-graph distance as an exact polyhedral geodesic.

## Frozen environment

See `environment.json`.  The suite uses Python 3.10+ and only the standard
library; there are no downloaded meshes, native extensions, or hidden random
state.  Every stochastic perturbation is driven by the documented seed.

## Run

From the repository root:

```powershell
python -m unittest discover -s code/volume07/tests -v
python code/volume07/experiments/run_validation.py
python code/volume07/experiments/build_figures.py
```

The first command runs the regression suite.  The second compares analytic,
boundary, resolution, and noise cases and rewrites the deterministic JSON report
in `expected/`.  The final command regenerates C16 machine-readable CSV tables,
their TeX table sources, and the scale-stability TikZ figure in `results/` and
`figures/`. The heat benchmark is a documented local explicit-diffusion proxy:
it reports deterministic work units and marks sparse-factorization timing as
not applicable, rather than treating workstation-dependent wall-clock timing as
a regression artifact. All outputs are stable for a fixed source revision and
environment.
