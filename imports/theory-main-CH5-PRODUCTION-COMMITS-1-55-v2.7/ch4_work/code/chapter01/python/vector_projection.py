"""Visualize a vector and its orthogonal projection onto another vector."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT = Path(__file__).resolve().parents[3] / "figures/ch01/computational/vector_projection.pdf"
a = np.array([4.0, 3.0])
b = np.array([5.0, 1.0])
projection = (a @ b) / (b @ b) * b
perpendicular = a - projection

fig, ax = plt.subplots(figsize=(6.2, 4.5))
for vector, label in [(a, r"$\mathbf{a}$"), (b, r"$\mathbf{b}$"),
                      (projection, r"$\mathrm{proj}_{\mathbf{b}}\mathbf{a}$")]:
    ax.quiver(0, 0, *vector, angles="xy", scale_units="xy", scale=1, width=0.008)
    ax.text(*(vector + np.array([0.12, 0.12])), label)
ax.plot([projection[0], a[0]], [projection[1], a[1]], linestyle="--")
ax.set(xlim=(-0.5, 5.8), ylim=(-0.5, 4.2), xlabel="$x$", ylabel="$y$")
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(OUTPUT)
print(f"projection = {projection}; perpendicular = {perpendicular}")
