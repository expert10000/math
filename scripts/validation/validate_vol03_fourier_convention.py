#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
VOL = ROOT / "books/vol03_fourier_distributions_pde"

required = {
    VOL / "frontmatter/fourier_conventions.tex": [
        r"e^{-2\pi i x\cdot\xi}",
        r"2\pi i\xi_j",
        r"4\pi^2|\xi|^2",
        r"e^{-4\pi^2t|\xi|^2}",
    ],
    VOL / "chapters/ch11_the_fourier_transform/chapter.tex": [
        r"e^{-2\pi i",
        r"2\pi i\xi",
    ],
    VOL / "chapters/ch12_the_gaussian_and_transform_calculus/chapter.tex": [
        r"e^{-\pi",
        r"4\pi",
    ],
    VOL / "chapters/ch19_fourier_transform_of_distributions/chapter.tex": [
        r"\widehat{\delta_0}",
        r"2\pi i",
    ],
    VOL / "chapters/ch28_spectral_and_transform_methods_for_pde/chapter.tex": [
        r"4\pi^2",
        r"e^{-4\pi^2",
    ],
}

errors = []
book = (VOL / "book.tex").read_text(encoding="utf-8-sig")
if r"\input{frontmatter/fourier_conventions.tex}" not in book:
    errors.append("book.tex does not include the global Fourier convention page")

for path, needles in required.items():
    text = path.read_text(encoding="utf-8-sig")
    for needle in needles:
        if needle not in text:
            errors.append(f"{path.relative_to(ROOT)} missing {needle}")

front = (VOL / "frontmatter/fourier_conventions.tex").read_text(encoding="utf-8-sig")
if r"e^{-i x\cdot\xi}" in front:
    errors.append("global page contains incompatible no-2pi transform convention")

if errors:
    print("\n".join("ERROR: " + e for e in errors))
    sys.exit(1)
print("Volume III Fourier convention audit: PASS")
