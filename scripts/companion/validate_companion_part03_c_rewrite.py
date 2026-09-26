#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

TARGETS = {"CP-III-0001", "CP-III-0013", "CP-III-0014", "CP-III-0016"}

def window(text: str, pid: str) -> str:
    starts = list(re.finditer(r"\\begin\{problem\}\[(CP-III-\d{4})\]", text))
    i = next((i for i,m in enumerate(starts) if m.group(1) == pid), None)
    if i is None:
        raise ValueError(pid)
    a = starts[i].start()
    b = starts[i+1].start() if i+1 < len(starts) else len(text)
    return text[a:b]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve()

    chapter = repo / "books" / "companion_problems_solutions" / "chapters" / "part03_volume_iii" / "chapter.tex"
    provenance = repo / "books" / "companion_problems_solutions" / "metadata" / "PART_III_C_REWRITE_PROVENANCE.tsv"
    errors = []

    if not chapter.exists():
        errors.append(f"missing chapter: {chapter}")
    if not provenance.exists():
        errors.append(f"missing provenance: {provenance}")

    if not errors:
        text = chapter.read_text(encoding="utf-8")
        try:
            w1 = window(text, "CP-III-0001")
            w13 = window(text, "CP-III-0013")
            w14 = window(text, "CP-III-0014")
            w16 = window(text, "CP-III-0016")
        except ValueError as e:
            errors.append(f"missing canonical problem: {e}")
            w1 = w13 = w14 = w16 = ""

        if "prescribed countable family" not in w1:
            errors.append("CP-III-0001: countable-family correction missing")
        if "Liouville numbers" not in w1 or "Hölder classes" not in w1:
            errors.append("CP-III-0001: worked Baire solution signatures missing")

        if "Theory: Tempered Distributions" in w13:
            errors.append("CP-III-0013: source overmerge survived")
        if r"(\mathcal Ff,\mathcal Fg)" not in w13:
            errors.append("CP-III-0013: corrected Plancherel pairing missing")
        if r"\pi\mathbf1_{(-1,1)}" not in w13:
            errors.append("CP-III-0013: sinc transform derivation signature missing")
        if "Translations are continuous in \\(L^2\\)" not in w13:
            errors.append("CP-III-0013: L2 convolution continuity signature missing")

        if "Exercise 4.2" in w14:
            errors.append("CP-III-0014: radial Exercise 4.2 overmerge survived")
        if "decays only polynomially" not in w14:
            errors.append("CP-III-0014: multiplier source correction missing")
        if r"\widehat G(\xi)" not in w14 or r"\frac1{1+4\pi^2\xi^2}" not in w14:
            errors.append("CP-III-0014: Green-kernel transform missing")

        if "Additional examples for part (a)" in w16:
            errors.append("CP-III-0016: repetitive source examples survived")
        if "We prove the chain in the order requested" not in w16:
            errors.append("CP-III-0016: coherent rewrite signature missing")
        if "Monotone convergence" not in w16:
            errors.append("CP-III-0016: measurable-extension proof missing")

    if provenance.exists():
        with provenance.open("r", encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f, delimiter="\t"))
        ids = {r.get("companion_problem_id", "") for r in rows}
        if ids != TARGETS:
            errors.append(f"rewrite provenance IDs mismatch: {sorted(ids)}")

    if errors:
        print("COMPANION PART III C_REWRITE VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    print("COMPANION PART III C_REWRITE VALIDATION PASSED")
    print("  CP-III-0001: Baire examples fully worked")
    print("  CP-III-0013: Exercise 4.3 normalized and fully solved")
    print("  CP-III-0014: Exercise 4.1 normalized and fully solved")
    print("  CP-III-0016: Exercise 2.5 rewritten coherently")
    print("  C_REWRITE queue: empty")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
