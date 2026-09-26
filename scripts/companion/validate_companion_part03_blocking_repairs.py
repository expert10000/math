#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


def problem_window(text: str, pid: str) -> str:
    starts = list(re.finditer(r"\\begin\{problem\}\[(CP-III-\d{4})\]", text))
    idx = next((i for i, m in enumerate(starts) if m.group(1) == pid), None)
    if idx is None:
        raise ValueError(f"{pid}: not found")
    a = starts[idx].start()
    b = starts[idx + 1].start() if idx + 1 < len(starts) else len(text)
    return text[a:b]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve()

    chapter = (
        repo / "books" / "companion_problems_solutions" / "chapters"
        / "part03_volume_iii" / "chapter.tex"
    )
    provenance = (
        repo / "books" / "companion_problems_solutions" / "metadata"
        / "PART_III_BLOCKING_REPAIR_PROVENANCE.tsv"
    )
    errors: list[str] = []

    for p in (chapter, provenance):
        if not p.exists():
            errors.append(f"missing required file: {p}")
    if errors:
        print("COMPANION PART III BLOCKING-REPAIR VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    text = chapter.read_text(encoding="utf-8")

    try:
        w6 = problem_window(text, "CP-III-0006")
        w23 = problem_window(text, "CP-III-0023")
    except ValueError as e:
        errors.append(str(e))
        w6 = w23 = ""

    if "Exercise 5.10" in w6 or "Heat equation: energy estimate" in w6:
        errors.append("CP-III-0006: overmerged later source sections survived")
    if r"\bigcap_{s\in\mathbb R}H^s" in w6 or r"\bigcap_{s\in\mathbb{R}} H^s" in w6:
        errors.append("CP-III-0006: false Schwartz/Sobolev identity survived")
    if r"\|D^\alpha f\|_{H^s}" not in w6:
        errors.append("CP-III-0006: derivative estimate signature missing")
    if "source exercise item" not in w6:
        errors.append("CP-III-0006: source-boundary note missing")

    if r"\mu_j\cdot\lambda_k=\delta_{jk}" not in w23:
        errors.append("CP-III-0023: algebraic dual-basis signature missing")
    if r"\lambda_j^*\cdot\lambda_k" not in w23 or r"2\pi\delta_{jk}" not in w23:
        errors.append("CP-III-0023: corrected 2pi Fourier dual-basis relation missing")
    if "Periodicity lets us shift each summand back to the fixed cell" not in w23:
        errors.append("CP-III-0023: corrected mean-value proof missing")
    if "every \\(\\Lambda\\)-periodic distribution is tempered" not in w23:
        errors.append("CP-III-0023: temperedness proof signature missing")
    if r"\mathcal F^{-1}\delta_\xi" not in w23 or r"\frac1{(2\pi)^n}e_\xi" not in w23:
        errors.append("CP-III-0023: explicit Fourier inversion normalization missing")

    with provenance.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    ids = {r.get("companion_problem_id", "") for r in rows}
    if ids != {"CP-III-0006", "CP-III-0023"}:
        errors.append(f"repair provenance IDs mismatch: {sorted(ids)}")

    if errors:
        print("COMPANION PART III BLOCKING-REPAIR VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    print("COMPANION PART III BLOCKING-REPAIR VALIDATION PASSED")
    print("  CP-III-0006: source-boundary overmerge repaired")
    print("  CP-III-0023: mean-value proof repaired")
    print("  CP-III-0023: 2pi Fourier dual normalization repaired")
    print("  CP-III-0023: periodic-distribution temperedness established")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
