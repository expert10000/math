"""Rotate a two-dimensional vector through several angles."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUTPUT = Path(__file__).resolve().parents[3] / "figures/ch01/computational/rotation.pdf"
v = np.array([3.0, 1.0])
angles = np.deg2rad([0, 30, 60, 90])
rotated = []
for theta in angles:
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    rotated.append(R @ v)

fig, ax = plt.subplots(figsize=(5.8, 5.2))
for theta, vector in zip(np.rad2deg(angles).astype(int), rotated):
    ax.quiver(0, 0, *vector, angles="xy", scale_units="xy", scale=1, width=0.008)
    ax.text(*(vector * 1.08), rf"${theta}^\circ$")
ax.set(xlim=(-1.7, 3.8), ylim=(-0.5, 3.8), xlabel="$x$", ylabel="$y$")
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(OUTPUT)
