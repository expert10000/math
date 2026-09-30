#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

TARGETS = {"CP-II-0129", "CP-II-0212", "CP-II-0454"}
R1_TARGETS = {
    "CP-II-0086","CP-II-0108","CP-II-0127","CP-II-0249",
    "CP-II-0303","CP-II-0310","CP-II-0322","CP-II-0395",
    "CP-II-0434","CP-II-0508","CP-II-0523","CP-II-0544",
    "CP-II-0545","CP-II-0547","CP-II-0551","CP-II-0569",
}
EXPECTED_PROVENANCE = {
    "CP-II-0129": "SOURCE_BACKED",
    "CP-II-0212": "CANONICAL_AUTHORED",
    "CP-II-0454": "SOURCE_BACKED",
}


def window(text: str, pid: str) -> str:
    starts = list(re.finditer(r"\\begin\{problem\}\[(CP-II-\d{4})\]", text))
    i = next((i for i, m in enumerate(starts) if m.group(1) == pid), None)
    if i is None:
        raise ValueError(pid)
    a = starts[i].start()
    b = starts[i + 1].start() if i + 1 < len(starts) else len(text)
    return text[a:b]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve()

    base = repo / "books" / "companion_problems_solutions"
    chapter = base / "chapters" / "part02_volume_ii" / "chapter.tex"
    audit = base / "metadata" / "PART_II_SOLUTION_QUALITY_AUDIT.tsv"
    prov = base / "metadata" / "PART_II_C_REWRITE_R2_PROVENANCE.tsv"

    errors: list[str] = []
    for p in (chapter, audit, prov):
        if not p.exists():
            errors.append(f"missing required file: {p}")

    if errors:
        print("COMPANION PART II C_REWRITE R2 VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    text = chapter.read_text(encoding="utf-8")

    sigs = {
        "CP-II-0129": (
            "Takagi Function",
            r"u_n=\frac{\lfloor2^n x\rfloor}{2^n}",
            "dyadic intervals",
            "nowhere differentiable",
        ),
        "CP-II-0212": (
            r"f\in\mathcal S(\mathbb R^n)",
            "Np>n",
            r"D^\alpha f\in L^p",
        ),
        "CP-II-0454": (
            "Takagi Function",
            r"u_n=\frac{\lfloor2^n x\rfloor}{2^n}",
            "successive differences",
            "nowhere differentiable",
        ),
    }

    for pid in TARGETS:
        try:
            w = window(text, pid)
        except ValueError:
            errors.append(f"{pid}: missing")
            continue

        if re.search(r"\\begin\{(?:enumerate|itemize|description)\*?\}", w):
            errors.append(f"{pid}: legacy list environment survived")
        if re.search(r"(^|\s)\\item(?:\[|\s|$)", w, re.M):
            errors.append(f"{pid}: legacy item survived")

        wn = re.sub(r"\s+", "", w.lower())
        for sig in sigs[pid]:
            sn = re.sub(r"\s+", "", sig.lower())
            if sn not in wn:
                errors.append(f"{pid}: signature missing: {sig}")

    with audit.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    by = {r.get("companion_problem_id", ""): r for r in rows}

    if len(rows) != 570:
        errors.append(f"audit rows: expected 570, got {len(rows)}")

    for pid in sorted(TARGETS):
        row = by.get(pid)
        if not row:
            errors.append(f"{pid}: missing audit row")
            continue
        if row.get("quality_status") != "A_STRONG":
            errors.append(
                f"{pid}: expected A_STRONG, got {row.get('quality_status')}"
            )
        if row.get("priority") != "P3":
            errors.append(f"{pid}: expected P3, got {row.get('priority')}")
        if row.get("solution_provenance") != EXPECTED_PROVENANCE[pid]:
            errors.append(
                f"{pid}: provenance expected {EXPECTED_PROVENANCE[pid]}, "
                f"got {row.get('solution_provenance')}"
            )

    for pid in sorted(R1_TARGETS):
        row = by.get(pid)
        if row and row.get("quality_status") != "A_STRONG":
            errors.append(
                f"{pid}: previous R1 target regressed to "
                f"{row.get('quality_status')}"
            )

    counts = Counter(r.get("quality_status", "") for r in rows)
    if counts.get("C_REWRITE", 0) != 0:
        errors.append(
            f"C_REWRITE queue is not empty in final audit: "
            f"{counts.get('C_REWRITE',0)}"
        )
    if counts.get("D_BLOCKING", 0) != 0:
        errors.append(
            f"D_BLOCKING: expected 0, got {counts.get('D_BLOCKING',0)}"
        )

    # Historical pre-R2 backup, if retained, proves only the intended
    # three R2 transitions. Later editorial batches legitimately changed many
    # non-target rows, so their old statuses must not be frozen here.
    backup = audit.with_name(audit.name + ".before_part02_c_rewrite_r2.bak")
    if backup.exists():
        with backup.open("r", encoding="utf-8-sig", newline="") as f:
            brows = list(csv.DictReader(f, delimiter="\t"))
        bby = {r.get("companion_problem_id", ""): r for r in brows}
        if len(brows) != 570:
            errors.append(
                f"pre-R2 backup audit rows: expected 570, got {len(brows)}"
            )

        for pid in sorted(TARGETS):
            old = bby.get(pid)
            row = by.get(pid)

            if old is None:
                errors.append(f"{pid}: missing from pre-R2 backup audit")
                continue

            if old.get("quality_status") != "C_REWRITE":
                errors.append(
                    f"{pid}: pre-R2 status expected C_REWRITE, got "
                    f"{old.get('quality_status')}"
                )

            if row is None:
                errors.append(f"{pid}: missing current audit row")
            elif row.get("quality_status") != "A_STRONG":
                errors.append(
                    f"{pid}: current status expected A_STRONG, got "
                    f"{row.get('quality_status')}"
                )

    with prov.open("r", encoding="utf-8-sig", newline="") as f:
        prows = list(csv.DictReader(f, delimiter="\t"))
    pids = {r.get("companion_problem_id", "") for r in prows}
    if pids != TARGETS:
        errors.append(f"R2 provenance IDs mismatch: {sorted(pids)}")

    if errors:
        print("COMPANION PART II C_REWRITE R2 VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    print("COMPANION PART II C_REWRITE R2 VALIDATION PASSED")
    print("  thematic section: Calculus")
    print("  repaired C_REWRITE rows: 3")
    print("  all 3 R2 targets: A_STRONG / P3")
    print(f"  A_STRONG: {counts.get('A_STRONG',0)}")
    print(f"  B_POLISH: {counts.get('B_POLISH',0)}")
    print(f"  C_REWRITE: {counts.get('C_REWRITE',0)}")
    print(f"  D_BLOCKING: {counts.get('D_BLOCKING',0)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



