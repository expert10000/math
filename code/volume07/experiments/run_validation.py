#!/usr/bin/env python3
"""Run deterministic VII/38--VII/42 numerical validation cases."""
from __future__ import annotations

import json
import sys
from math import isfinite
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from volume07_validation import (  # noqa: E402
    Mesh, bounded_noise_profile, cotangent_laplacian, dijkstra, flat_reference,
    heat_diffusion, heat_distance_ordering, profile_extrema, rectangular_mesh,
    vertex,
)


def run() -> dict:
    resolution_cases = []
    for n in (4, 8, 16):
        mesh = rectangular_mesh(n)
        source, target = vertex(mesh, n, 0, 0), vertex(mesh, n, n, n // 2)
        graph_distance = dijkstra(mesh, [source])[0][target]
        reference = flat_reference(mesh.vertices[source], mesh.vertices[target])
        resolution_cases.append({
            "resolution": n,
            "graph_distance": round(graph_distance, 12),
            "flat_reference": round(reference, 12),
            "upper_error": round(graph_distance - reference, 12),
            "upper_bound_holds": graph_distance + 1e-12 >= reference,
        })

    mesh = rectangular_mesh(8)
    source, nearby, far = vertex(mesh, 8, 0, 0), vertex(mesh, 8, 1, 0), vertex(mesh, 8, 8, 8)
    heat = heat_diffusion(mesh, source)
    ordering = heat_distance_ordering(heat)
    affine = [point[0] + 2 * point[1] for point in mesh.vertices]
    laplacian = cotangent_laplacian(mesh, affine)
    interior = [vertex(mesh, 8, x, y) for x in range(1, 8) for y in range(1, 8)]

    noisy = rectangular_mesh(8, noise=0.015)
    noisy_distance = dijkstra(noisy, [source])[0][far]
    smooth_distance = dijkstra(mesh, [source])[0][far]
    extrema = profile_extrema(bounded_noise_profile())
    disconnected = Mesh(
        ((0, 0, 0), (1, 0, 0), (0, 1, 0), (3, 0, 0), (4, 0, 0), (3, 1, 0)),
        ((0, 1, 2), (3, 4, 5)),
    )

    return {
        "schema_version": 1,
        "seed": 20260915,
        "resolution_sweep": resolution_cases,
        "boundary_case": {
            "disconnected_distance_is_infinite": not isfinite(dijkstra(disconnected, [0])[0][5]),
            "note": "A pair of disconnected triangles exercises the no-path boundary condition."
        },
        "heat_case": {
            "source_is_global_maximum": heat[source] == max(heat),
            "near_before_far": ordering[nearby] < ordering[far],
        },
        "laplacian_case": {
            "max_interior_affine_residual": round(max(abs(laplacian[index]) for index in interior), 14),
        },
        "noise_case": {
            "relative_graph_distance_change": round(abs(noisy_distance - smooth_distance) / smooth_distance, 12),
            "noise_amplitude": 0.015,
        },
        "curvature_profile_case": extrema,
    }


def main() -> int:
    report = run()
    if not all(case["upper_bound_holds"] for case in report["resolution_sweep"]):
        raise SystemExit("edge-graph upper-bound contract failed")
    if not report["heat_case"]["source_is_global_maximum"] or not report["heat_case"]["near_before_far"]:
        raise SystemExit("heat diffusion ordering contract failed")
    if report["laplacian_case"]["max_interior_affine_residual"] > 1e-10:
        raise SystemExit("cotangent Laplacian affine-field contract failed")
    if report["noise_case"]["relative_graph_distance_change"] > 0.03:
        raise SystemExit("noise stability contract failed")
    if report["curvature_profile_case"] != {"ridges": [2, 7], "valleys": [5]}:
        raise SystemExit("curvature extrema contract failed")
    output = ROOT / "expected" / "volume07_validation.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
