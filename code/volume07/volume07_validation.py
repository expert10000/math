"""Small deterministic reference implementations for Volume VII validation."""
from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from math import hypot, inf, sqrt
from typing import Iterable

Point = tuple[float, float, float]


@dataclass(frozen=True)
class Mesh:
    vertices: tuple[Point, ...]
    triangles: tuple[tuple[int, int, int], ...]


def subtract(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def dot(a: Point, b: Point) -> float:
    return sum(x * y for x, y in zip(a, b))


def cross(a: Point, b: Point) -> Point:
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def norm(a: Point) -> float:
    return sqrt(dot(a, a))


def distance(a: Point, b: Point) -> float:
    return norm(subtract(a, b))


def rectangular_mesh(n: int, noise: float = 0.0) -> Mesh:
    """Return a unit-square mesh with a deterministic bounded height perturbation."""
    if n < 2:
        raise ValueError("n must be at least 2")
    vertices: list[Point] = []
    for y in range(n + 1):
        for x in range(n + 1):
            z = noise * ((x * 17 + y * 31) % 7 - 3) / 3
            vertices.append((x / n, y / n, z))
    triangles: list[tuple[int, int, int]] = []
    for y in range(n):
        for x in range(n):
            a = y * (n + 1) + x
            b, c, d = a + 1, a + n + 1, a + n + 2
            triangles.extend(((a, b, d), (a, d, c)))
    return Mesh(tuple(vertices), tuple(triangles))


def vertex(mesh: Mesh, n: int, x: int, y: int) -> int:
    return y * (n + 1) + x


def weighted_edges(mesh: Mesh) -> dict[int, dict[int, float]]:
    graph: dict[int, dict[int, float]] = {i: {} for i in range(len(mesh.vertices))}
    for triangle in mesh.triangles:
        for a, b in ((triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[2], triangle[0])):
            weight = distance(mesh.vertices[a], mesh.vertices[b])
            graph[a][b] = graph[b][a] = weight
    return graph


def dijkstra(mesh: Mesh, sources: Iterable[int]) -> tuple[list[float], list[int | None]]:
    graph = weighted_edges(mesh)
    distances = [inf] * len(mesh.vertices)
    parent: list[int | None] = [None] * len(mesh.vertices)
    queue: list[tuple[float, int]] = []
    for source in sorted(set(sources)):
        distances[source] = 0.0
        heappush(queue, (0.0, source))
    while queue:
        current, node = heappop(queue)
        if current != distances[node]:
            continue
        for neighbor, weight in graph[node].items():
            candidate = current + weight
            if candidate < distances[neighbor] - 1e-15:
                distances[neighbor] = candidate
                parent[neighbor] = node
                heappush(queue, (candidate, neighbor))
    return distances, parent


def recover_path(parent: list[int | None], target: int) -> list[int]:
    path = [target]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    return list(reversed(path))


def cotangent_laplacian(mesh: Mesh, values: list[float]) -> list[float]:
    """Return the positive cotangent stiffness operator without mass scaling."""
    if len(values) != len(mesh.vertices):
        raise ValueError("one value per vertex is required")
    weights: dict[tuple[int, int], float] = {}
    for i, j, k in mesh.triangles:
        for a, b, opposite in ((i, j, k), (j, k, i), (k, i, j)):
            u, v = subtract(mesh.vertices[a], mesh.vertices[opposite]), subtract(mesh.vertices[b], mesh.vertices[opposite])
            area2 = norm(cross(u, v))
            if area2 <= 1e-15:
                raise ValueError("degenerate triangle")
            edge = tuple(sorted((a, b)))
            weights[edge] = weights.get(edge, 0.0) + dot(u, v) / area2 / 2
    result = [0.0] * len(mesh.vertices)
    for (a, b), weight in weights.items():
        delta = weight * (values[a] - values[b])
        result[a] += delta
        result[b] -= delta
    return result


def heat_diffusion(mesh: Mesh, source: int, time_step: float = 0.04, steps: int = 16) -> list[float]:
    """Explicit graph heat diffusion with a scale-safe timestep for test meshes."""
    graph = weighted_edges(mesh)
    value = [0.0] * len(mesh.vertices)
    value[source] = 1.0
    degree = max(len(neighbors) for neighbors in graph.values())
    alpha = min(time_step, 0.9 / degree)
    for _ in range(steps):
        next_value = value.copy()
        for node, neighbors in graph.items():
            next_value[node] += alpha * sum(value[other] - value[node] for other in neighbors)
        value = next_value
    return value


def heat_distance_ordering(heat: list[float]) -> list[float]:
    peak = max(heat)
    return [-__import__("math").log(max(value, 1e-300) / peak) for value in heat]


def profile_extrema(samples: list[float]) -> dict[str, list[int]]:
    """Classify strict local extrema; endpoints are intentionally excluded."""
    ridges, valleys = [], []
    for index in range(1, len(samples) - 1):
        left, current, right = samples[index - 1], samples[index], samples[index + 1]
        if current > left and current > right:
            ridges.append(index)
        if current < left and current < right:
            valleys.append(index)
    return {"ridges": ridges, "valleys": valleys}


def flat_reference(a: Point, b: Point) -> float:
    """Exact intrinsic distance for two points on the planar reference mesh."""
    return hypot(a[0] - b[0], a[1] - b[1])


def bounded_noise_profile(seed: int = 20260915) -> list[float]:
    # A deterministic low-amplitude perturbation preserves the two intended extrema.
    base = [0.0, 0.4, 1.0, 0.45, -0.1, -0.8, -0.15, 0.25, 0.0]
    offsets = [((seed >> (index % 16)) & 3) - 1.5 for index in range(len(base))]
    return [value + 0.015 * offset for value, offset in zip(base, offsets)]
