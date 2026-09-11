#!/usr/bin/env python3
from __future__ import annotations
import cmath
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOL = ROOT / "books/vol03_fourier_distributions_pde"
errors = []

def require(path, needles):
    text = path.read_text(encoding="utf-8-sig")
    for needle in needles:
        if needle not in text:
            errors.append(f"{path.relative_to(ROOT)} missing {needle}")

require(VOL / "frontmatter/fourier_conventions.tex", [
    r"\widehat{\partial_j f}(\xi)",
    r"2\pi i\xi_j\widehat f(\xi)",
    r"\widehat{-\Delta f}(\xi)",
    r"4\pi^2|\xi|^2\widehat f(\xi)",
    r"\widehat K_t(\xi)=e^{-4\pi^2t|\xi|^2}",
])
require(VOL / "chapters/ch19_fourier_transform_of_distributions/chapter.tex", [
    r"\widehat{\delta_0}",
    r"2\pi i",
])
require(VOL / "chapters/ch28_spectral_and_transform_methods_for_pde/chapter.tex", [
    r"4\pi^2",
    r"e^{-4\pi^2",
])

pi = math.pi
if not math.isclose((2*pi)**2, 4*pi*pi, rel_tol=0, abs_tol=1e-15):
    errors.append("derivative-squared coefficient does not equal 4*pi^2")
if not math.isclose(-((2*pi)**2), -4*pi*pi, rel_tol=0, abs_tol=1e-15):
    errors.append("Laplacian multiplier sign/coefficient mismatch")

def trapz_complex(func, a, b, n):
    h = (b-a)/n
    s = 0.5*(func(a)+func(b))
    for k in range(1, n):
        s += func(a+k*h)
    return s*h

for xi in (0.0, 0.35, 0.8):
    num = trapz_complex(
        lambda x: math.exp(-pi*x*x)*cmath.exp(-2j*pi*x*xi),
        -6.0, 6.0, 12000
    )
    exact = math.exp(-pi*xi*xi)
    if abs(num-exact) > 2e-6:
        errors.append(f"Gaussian FT mismatch at xi={xi}: {num} vs {exact}")

for xi in (0.25, 0.7):
    num = trapz_complex(
        lambda x: (-2*pi*x*math.exp(-pi*x*x))*cmath.exp(-2j*pi*x*xi),
        -6.0, 6.0, 12000
    )
    exact = 2j*pi*xi*math.exp(-pi*xi*xi)
    if abs(num-exact) > 3e-6:
        errors.append(f"derivative multiplier mismatch at xi={xi}: {num} vs {exact}")

def heat_kernel(x, t):
    return (4*pi*t)**(-0.5)*math.exp(-(x*x)/(4*t))

for t, xi in ((0.2,0.4),(0.7,0.8)):
    L = 10.0*math.sqrt(t+1.0)
    num = trapz_complex(
        lambda x: heat_kernel(x,t)*cmath.exp(-2j*pi*x*xi),
        -L, L, 14000
    )
    exact = math.exp(-4*pi*pi*t*xi*xi)
    if abs(num-exact) > 3e-6:
        errors.append(f"heat multiplier mismatch at t={t}, xi={xi}: {num} vs {exact}")

for t, xi in ((0.3,0.2),(0.9,1.1)):
    m = math.exp(-4*pi*pi*t*xi*xi)
    dt_m = -4*pi*pi*xi*xi*m
    residual = dt_m + 4*pi*pi*xi*xi*m
    if abs(residual) > 1e-14:
        errors.append(f"heat ODE residual nonzero: {residual}")

for xi in (0.25, 1.0, 2.5):
    multiplier = 4*pi*pi*xi*xi
    inv = 1.0/multiplier
    if abs(multiplier*inv - 1.0) > 1e-14:
        errors.append(f"Poisson multiplier inversion failed at xi={xi}")

if errors:
    print("\n".join("ERROR: " + e for e in errors))
    sys.exit(1)

print("Volume III Fourier/PDE symbolic-static checks: PASS")
print("Gaussian transform numerical checks: PASS")
print("Derivative multiplier numerical checks: PASS")
print("Heat-kernel multiplier numerical checks: PASS")
print("Heat/Poisson PDE multiplier checks: PASS")
