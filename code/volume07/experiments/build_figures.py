#!/usr/bin/env python3
"""Regenerate deterministic C16 metrics, TeX tables, and a ridge-stability figure."""
from __future__ import annotations

import csv
import math
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def noise_code(i: int, j: int) -> float:
    """A bounded deterministic perturbation with no hidden random state."""
    return ((i * 17 + j * 31) % 11 - 5) / 5


def heat_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    # Short-time explicit graph-heat proxy: t=m h^2, m=16*0.12.
    steps, alpha = 16, 0.12
    for n in (8, 16, 32):
        h, m = 1 / n, steps * alpha
        values: dict[tuple[int, int], float] = {(0, 0): 1.0}
        for _ in range(steps):
            next_values: dict[tuple[int, int], float] = {}
            for y in range(n + 1):
                for x in range(n + 1):
                    here = values.get((x, y), 0.0)
                    neighbors = [(a, b) for a, b in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if 0 <= a <= n and 0 <= b <= n]
                    next_values[(x, y)] = here + alpha * sum(values.get(point, 0.0) - here for point in neighbors)
            values = next_values
        errors = []
        for (x, y), value in values.items():
            reference = h * math.hypot(x, y)
            if 0 < reference <= 3 * h and value > 0:
                estimate = math.sqrt(max(0.0, -4 * m * h * h * math.log(value / values[(0, 0)])))
                errors.append(abs(estimate - reference))
        directed_edges = sum(4 - (x in (0, n)) - (y in (0, n)) for y in range(n + 1) for x in range(n + 1))
        rows.append({
            "resolution": n, "vertices": (n + 1) ** 2, "characteristic_edge_length": f"{h:.8f}",
            "time_normalization_m": f"{m:.3f}", "time_step": f"{m * h * h:.10f}",
            "mean_error": f"{sum(errors) / len(errors):.8f}", "max_error": f"{max(errors):.8f}",
            "factorization_time_ms": "N/A", "solve_work_units": steps * directed_edges,
            "boundary_condition": "zero-flux graph boundary", "reference": "planar local heat-kernel proxy (radius <= 3h)",
        })
    return rows


def mean_curvature(fx: float, fy: float, fxx: float, fxy: float, fyy: float) -> float:
    return ((1 + fy * fy) * fxx - 2 * fx * fy * fxy + (1 + fx * fx) * fyy) / (2 * (1 + fx * fx + fy * fy) ** 1.5)


def curvature_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    kappa = 0.9
    for n in (8, 16, 32):
        h = 1 / n
        for amplitude in (0.0, 0.002):
            def f(i: int, j: int) -> float:
                x, y = -0.5 + i * h, -0.5 + j * h
                return 0.5 * kappa * (x * x + y * y) + amplitude * h * h * noise_code(i, j)
            errors = []
            for j in range(1, n):
                for i in range(1, n):
                    x, y = -0.5 + i * h, -0.5 + j * h
                    fx, fy = (f(i + 1, j) - f(i - 1, j)) / (2 * h), (f(i, j + 1) - f(i, j - 1)) / (2 * h)
                    fxx, fyy = (f(i + 1, j) - 2 * f(i, j) + f(i - 1, j)) / h**2, (f(i, j + 1) - 2 * f(i, j) + f(i, j - 1)) / h**2
                    fxy = (f(i + 1, j + 1) - f(i + 1, j - 1) - f(i - 1, j + 1) + f(i - 1, j - 1)) / (4 * h**2)
                    exact = kappa * (1 + 0.5 * kappa * kappa * (x * x + y * y)) / (1 + kappa * kappa * (x * x + y * y)) ** 1.5
                    errors.append(abs(mean_curvature(fx, fy, fxx, fxy, fyy) - exact))
            rows.append({"surface": "paraboloid graph", "resolution": n, "edge_length": f"{h:.8f}", "noise_amplitude": f"{amplitude:.3f}", "l2_error": f"{math.sqrt(sum(e * e for e in errors) / len(errors)):.8f}", "linf_error": f"{max(errors):.8f}", "reference": "analytic graph mean curvature"})
    return rows


def smooth(values: list[float], radius: int) -> list[float]:
    return [sum(values[max(0, i - radius):min(len(values), i + radius + 1)]) / len(values[max(0, i - radius):min(len(values), i + radius + 1)]) for i in range(len(values))]


def extrema(values: list[float]) -> list[int]:
    return [i for i in range(1, len(values) - 1) if (values[i] > values[i - 1] and values[i] > values[i + 1]) or (values[i] < values[i - 1] and values[i] < values[i + 1])]


def ridge_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n in (16, 32, 64):
        expected = [n // 4, 3 * n // 4]
        for scale in (1, 2):
            for amplitude in (0.0, 0.01, 0.03):
                values = [math.sin(2 * math.pi * i / n) + amplitude * noise_code(i, 2 * i) for i in range(n + 1)]
                found = extrema(smooth(values, scale - 1))
                matched = [index for index in found if min(abs(index - target) for target in expected) <= scale]
                false = len(found) - len(matched)
                displacement = sum(min(abs(index - target) for target in expected) / n for index in matched) / len(matched) if matched else 1.0
                rows.append({"resolution": n, "scale_radius": scale, "noise_amplitude": f"{amplitude:.3f}", "stable_feature_length": f"{len(matched) * 2 / n:.6f}", "false_positive_length": f"{false * 2 / n:.6f}", "mean_displacement": f"{displacement:.6f}", "reference_loci": "x=1/4, 3/4 on a unit profile"})
    return rows


def csv_text(rows: list[dict[str, object]]) -> str:
    handle = StringIO(); writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader(); writer.writerows(rows)
    return handle.getvalue()


def tex_table(rows: list[dict[str, object]], columns: list[str], caption: str, label: str) -> str:
    head = " & ".join(column.replace("_", " ") for column in columns) + r"\\"
    body = "\n".join(" & ".join(str(row[column]).replace("_", r"\_") for column in columns) + r"\\" for row in rows)
    return "\n".join((r"\begin{table}[htbp]", r"\centering\scriptsize", r"\resizebox{\textwidth}{!}{%", r"\begin{tabular}{" + "l" * len(columns) + "}", r"\toprule", head, r"\midrule", body, r"\bottomrule", r"\end{tabular}%", r"}", rf"\caption{{{caption}}}", rf"\label{{{label}}}", r"\end{table}", ""))


def ridge_figure(rows: list[dict[str, object]]) -> str:
    chosen = [row for row in rows if row["scale_radius"] == 1 and row["noise_amplitude"] == "0.030"]
    points = " -- ".join(f"({i},{float(row['false_positive_length']) * 12:.3f})" for i, row in enumerate(chosen))
    return "\n".join((r"\begin{figure}[htbp]", r"\centering", r"\begin{tikzpicture}[x=1.3cm,y=1.1cm]", r"\draw[->] (0,0) -- (3.4,0) node[right]{resolution};", r"\draw[->] (0,0) -- (0,2.2) node[above]{false-positive feature length};", r"\draw[teal,thick] " + points + ";", r"\foreach \x/\n in {0/16,1/32,2/64} {\fill (\x,0) circle (1.3pt); \node[below] at (\x,0) {\n};}", r"\node[align=left,font=\scriptsize] at (2.0,1.75) {unit profile; scale radius $1$;\\deterministic noise amplitude $0.03$};", r"\end{tikzpicture}", r"\caption{Generated scale-stability summary for the deterministic unit-profile ridge/valley proxy. The vertical quantity is a one-dimensional support-length proxy, not a surface ridge arc length.}", r"\label{fig:vii42-c16-scale-stability}", r"\end{figure}", ""))


def artifacts() -> dict[Path, str]:
    heat, curvature, ridge = heat_rows(), curvature_rows(), ridge_rows()
    return {
        ROOT / "results" / "heat_distance_convergence.csv": csv_text(heat),
        ROOT / "results" / "curvature_validation.csv": csv_text(curvature),
        ROOT / "results" / "ridge_valley_robustness.csv": csv_text(ridge),
        ROOT / "results" / "heat_distance_convergence.tex": tex_table(heat, ["resolution", "characteristic_edge_length", "time_normalization_m", "mean_error", "max_error", "factorization_time_ms", "solve_work_units", "boundary_condition"], "Deterministic local heat-distance proxy results. The reference uses explicit graph diffusion, so sparse-factorization time is not applicable; work units record the solve budget.", "tab:vii40-c16-heat-convergence"),
        ROOT / "results" / "curvature_validation.tex": tex_table(curvature, ["surface", "resolution", "noise_amplitude", "l2_error", "linf_error"], "Analytic paraboloid validation for the deterministic Monge-patch curvature proxy; the controlled perturbation is a height perturbation of amplitude shown.", "tab:vii41-c16-curvature-validation"),
        ROOT / "results" / "ridge_valley_robustness.tex": tex_table(ridge, ["resolution", "scale_radius", "noise_amplitude", "stable_feature_length", "false_positive_length", "mean_displacement"], "Deterministic ridge/valley robustness proxy on a unit profile. Lengths are declared one-dimensional support measures, and displacement is measured from the analytic reference loci.", "tab:vii42-c16-ridge-robustness"),
        ROOT / "figures" / "ridge_scale_stability.tex": ridge_figure(ridge),
    }


def build(check: bool = False) -> bool:
    current = artifacts()
    stale = [path for path, text in current.items() if not path.exists() or path.read_text(encoding="utf-8") != text]
    if check:
        return not stale
    for path, text in current.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(path.relative_to(ROOT))
    return True


def main() -> int:
    return 0 if build() else 1


if __name__ == "__main__":
    raise SystemExit(main())
