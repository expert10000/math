"""Apply Gram-Schmidt orthogonalization and visualize the result."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT = Path(__file__).resolve().parents[3] / "figures/ch01/computational/gram_schmidt.pdf"
v1 = np.array([3.0, 1.0])
v2 = np.array([2.0, 3.0])
e1 = v1 / np.linalg.norm(v1)
u2 = v2 - (v2 @ e1) * e1
e2 = u2 / np.linalg.norm(u2)

fig, ax = plt.subplots(figsize=(5.7, 4.7))
for vector, label in [(v1, r"$\mathbf{v}_1$"), (v2, r"$\mathbf{v}_2$"),
                      (2.2 * e1, r"$\mathbf{e}_1$"), (2.2 * e2, r"$\mathbf{e}_2$")]:
    ax.quiver(0, 0, *vector, angles="xy", scale_units="xy", scale=1, width=0.008)
    ax.text(*(vector * 1.08), label)
ax.set(xlim=(-1.2, 3.8), ylim=(-0.5, 3.8), xlabel="$x$", ylabel="$y$")
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(OUTPUT)
print(f"e1 dot e2 = {e1 @ e2:.3e}")
