#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

TARGETS = {
    "CP-II-0061": "SOURCE_BACKED",
    "CP-II-0083": "SOURCE_BACKED",
    "CP-II-0305": "SOURCE_BACKED",
    "CP-II-0315": "CANONICAL_AUTHORED",
}


def problem_window(text: str, pid: str) -> str:
    starts = list(re.finditer(r"\\begin\{problem\}\[(CP-II-\d{4})\]", text))
    idx = next((i for i, m in enumerate(starts) if m.group(1) == pid), None)
    if idx is None:
        raise ValueError(f"{pid}: problem not found")
    a = starts[idx].start()
    b = starts[idx + 1].start() if idx + 1 < len(starts) else len(text)
    return text[a:b]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve()

    base = repo / "books" / "companion_problems_solutions"
    chapter = base / "chapters" / "part02_volume_ii" / "chapter.tex"
    audit = base / "metadata" / "PART_II_SOLUTION_QUALITY_AUDIT.tsv"
    provenance = base / "metadata" / "PART_II_BLOCKING_REPAIR_PROVENANCE.tsv"

    errors: list[str] = []
    for p in (chapter, audit, provenance):
        if not p.exists():
            errors.append(f"missing required file: {p}")

    if errors:
        print("COMPANION PART II BLOCKING-REPAIR VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    text = chapter.read_text(encoding="utf-8")

    try:
        w61 = problem_window(text, "CP-II-0061")
        w83 = problem_window(text, "CP-II-0083")
        w305 = problem_window(text, "CP-II-0305")
        w315 = problem_window(text, "CP-II-0315")
    except ValueError as e:
        errors.append(str(e))
        w61 = w83 = w305 = w315 = ""

    if r"s<-\frac n2" not in w61:
        errors.append("CP-II-0061: Dirac Sobolev threshold missing")
    if r"\mathcal S" not in w61 or r"\mathcal S'" not in w61:
        errors.append("CP-II-0061: Sobolev/Schwartz inclusion proof missing")

    if r"D_y^\alpha\psi(y)" not in w83:
        errors.append("CP-II-0083: slice derivative formula missing")
    if r"T_{f_j}" not in w83 or r"\sigma(\mathcal D',\mathcal D)" not in w83:
        errors.append("CP-II-0083: weak-* approximation proof missing")

    if "Dirichlet function" not in w305:
        errors.append("CP-II-0305: source-background correction missing")
    if "D(f)" not in w305 or r"\int_A f(x,y)\,dx\,dy=0" not in w305:
        errors.append("CP-II-0305: Riemann-integrability proof signature missing")

    if r"-D_i u" not in w315:
        errors.append("CP-II-0315: corrected negative derivative limit missing")
   
    if r"\phi(he_i)-\phi(0)" not in w315:
        errors.append("CP-II-0315: Dirac sign check missing")

    with audit.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    by_id = {r.get("companion_problem_id", ""): r for r in rows}

    blockers = [
        r.get("companion_problem_id", "")
        for r in rows
        if r.get("quality_status") == "D_BLOCKING"
    ]
    if blockers:
        errors.append(f"D_BLOCKING queue is not empty: {blockers}")

    for pid, expected_prov in TARGETS.items():
        row = by_id.get(pid)
        if row is None:
            errors.append(f"{pid}: missing audit row")
            continue
        if row.get("quality_status") != "A_STRONG":
            errors.append(
                f"{pid}: expected A_STRONG after repair, got "
                f"{row.get('quality_status')}"
            )
        if row.get("priority") != "P3":
            errors.append(
                f"{pid}: expected P3 after repair, got {row.get('priority')}"
            )
        if row.get("solution_provenance") != expected_prov:
            errors.append(
                f"{pid}: provenance expected {expected_prov}, got "
                f"{row.get('solution_provenance')}"
            )

    with provenance.open("r", encoding="utf-8-sig", newline="") as f:
        prows = list(csv.DictReader(f, delimiter="\t"))
    pids = {r.get("companion_problem_id", "") for r in prows}
    if pids != set(TARGETS):
        errors.append(f"repair provenance IDs mismatch: {sorted(pids)}")

    if errors:
        print("COMPANION PART II BLOCKING-REPAIR VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    print("COMPANION PART II BLOCKING-REPAIR VALIDATION PASSED")
    print("  CP-II-0061: full Sobolev exercise solution")
    print("  CP-II-0083: full distribution-slice solution")
    print("  CP-II-0305: corrected Riemann-integrability argument")
    print("  CP-II-0315: corrected translation-difference sign")
    print("  D_BLOCKING queue: empty")
    print("  four repaired targets: A_STRONG / P3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
