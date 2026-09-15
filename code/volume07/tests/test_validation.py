from __future__ import annotations

import sys
import unittest
import json
from math import inf
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "experiments"))
from volume07_validation import (  # noqa: E402
    Mesh, cotangent_laplacian, dijkstra, flat_reference, heat_diffusion,
    heat_distance_ordering, profile_extrema, rectangular_mesh, vertex,
)
from run_validation import run  # noqa: E402


class VolumeVIIValidationTests(unittest.TestCase):
    def test_graph_distance_is_an_upper_bound_on_flat_reference(self) -> None:
        mesh = rectangular_mesh(8)
        source, target = vertex(mesh, 8, 0, 0), vertex(mesh, 8, 8, 4)
        graph_distance = dijkstra(mesh, [source])[0][target]
        self.assertGreaterEqual(graph_distance + 1e-12, flat_reference(mesh.vertices[source], mesh.vertices[target]))

    def test_disconnected_query_is_infinite(self) -> None:
        mesh = Mesh(((0, 0, 0), (1, 0, 0), (5, 0, 0), (6, 0, 0)), ((0, 1, 1), (2, 3, 3)))
        self.assertEqual(dijkstra(mesh, [0])[0][3], inf)

    def test_affine_field_has_zero_interior_cotangent_residual(self) -> None:
        mesh = rectangular_mesh(6)
        values = [point[0] - 3 * point[1] for point in mesh.vertices]
        residual = cotangent_laplacian(mesh, values)
        interior = [vertex(mesh, 6, x, y) for x in range(1, 6) for y in range(1, 6)]
        self.assertLess(max(abs(residual[index]) for index in interior), 1e-10)

    def test_heat_ordering_separates_near_and_far_vertices(self) -> None:
        mesh = rectangular_mesh(8)
        source = vertex(mesh, 8, 0, 0)
        order = heat_distance_ordering(heat_diffusion(mesh, source))
        self.assertEqual(order[source], 0.0)
        self.assertLess(order[vertex(mesh, 8, 1, 0)], order[vertex(mesh, 8, 8, 8)])

    def test_profile_extrema_are_deterministic(self) -> None:
        self.assertEqual(profile_extrema([0.0, 1.0, 0.0, -1.0, 0.0]), {"ridges": [1], "valleys": [3]})

    def test_expected_validation_report_is_current(self) -> None:
        expected = json.loads((ROOT / "expected" / "volume07_validation.json").read_text(encoding="utf-8"))
        self.assertEqual(run(), expected)


if __name__ == "__main__":
    unittest.main()
