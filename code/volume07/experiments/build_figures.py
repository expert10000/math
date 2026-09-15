#!/usr/bin/env python3
"""Regenerate a compact SVG visualizing the deterministic ridge/valley profile."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from volume07_validation import bounded_noise_profile, profile_extrema  # noqa: E402


def main() -> int:
    values = bounded_noise_profile()
    extrema = profile_extrema(values)
    points = " ".join(f"{20 + 55 * i},{155 - 100 * value:.3f}" for i, value in enumerate(values))
    markers = []
    for kind, color in (("ridges", "#b42318"), ("valleys", "#1d4ed8")):
        for index in extrema[kind]:
            markers.append(f'<circle cx="{20 + 55 * index}" cy="{155 - 100 * values[index]:.3f}" r="5" fill="{color}"/>')
    svg = "\n".join((
        '<svg xmlns="http://www.w3.org/2000/svg" width="480" height="190" viewBox="0 0 480 190">',
        '<rect width="480" height="190" fill="white"/>',
        '<path d="M20 155H460 M20 25V155" stroke="#475569" fill="none"/>',
        f'<polyline points="{points}" fill="none" stroke="#0f766e" stroke-width="3"/>',
        *markers,
        '<text x="22" y="18" font-family="sans-serif" font-size="14">Deterministic curvature-profile extrema</text>',
        '<text x="330" y="178" font-family="sans-serif" font-size="12">sample index</text>',
        '</svg>',
    )) + "\n"
    output = ROOT / "figures" / "curvature_profile_extrema.svg"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(svg, encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
