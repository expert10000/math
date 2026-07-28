"""Show how a matrix transforms a square and two basis vectors."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT = Path(__file__).resolve().parents[3] / "figures/ch01/computational/linear_transformation.pdf"
A = np.array([[1.5, 0.7], [0.3, 1.2]])
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]], dtype=float)
transformed = square @ A.T

fig, ax = plt.subplots(figsize=(6.0, 4.8))
ax.plot(square[:, 0], square[:, 1], linestyle="--", label="original square")
ax.plot(transformed[:, 0], transformed[:, 1], label="transformed square")
for vector, label in [(A @ np.array([1., 0.]), r"$A\mathbf{e}_1$"),
                      (A @ np.array([0., 1.]), r"$A\mathbf{e}_2$")]:
    ax.quiver(0, 0, *vector, angles="xy", scale_units="xy", scale=1, width=0.008)
    ax.text(*(vector * 1.08), label)
ax.set(xlim=(-0.25, 2.6), ylim=(-0.25, 1.8), xlabel="$x$", ylabel="$y$")
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(OUTPUT)
