# Volume III Fourier/PDE constant checks

Release command:

`python scripts/validation/run_vol03_release_math_checks.py`

Checks cover the global transform convention, derivative/Laplacian constants,
Gaussian self-duality, the Gaussian derivative multiplier, the heat-kernel
multiplier, the heat-mode ODE residual, and Poisson multiplier inversion away
from zero frequency.

The numerical quadrature uses only the Python standard library so this release
gate adds no SymPy/NumPy dependency.
