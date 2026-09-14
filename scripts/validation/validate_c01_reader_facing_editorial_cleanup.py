#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

EXCLUDED_PATH_MARKERS = (
    "legacy_problem_audit",
    "source_migration",
    "provenance",
)

def excluded(path: Path) -> bool:
    s = path.as_posix().lower()
    return any(marker in s for marker in EXCLUDED_PATH_MARKERS)

def strip_comment(line: str) -> str:
    for i, ch in enumerate(line):
        if ch == "%":
            nbs = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                nbs += 1
                j -= 1
            if nbs % 2 == 0:
                return line[:i]
    return line

def strip_nonrendered(line: str) -> str:
    line = re.sub(r"\\label\{[^}]*\}", "", line)
    return line

BANNED = [
    ("legacy", re.compile(r"\blegacy\b", re.I)),
    ("corpus", re.compile(r"\bcorpus\b", re.I)),
    ("dossier", re.compile(r"\bdossiers?\b", re.I)),
    ("reader-facing provenance", re.compile(r"\bprovenance\b", re.I)),
    ("protected chapter", re.compile(r"\bprotected chapter\b", re.I)),
    ("source audit", re.compile(r"\bsource audit\b", re.I)),
    ("migration map", re.compile(r"\bmigration map\b", re.I)),
    ("post-volume audit", re.compile(r"\bpost-VIII/35\b", re.I)),
    ("reconstruction invariant", re.compile(r"\breconstruction invariant\b", re.I)),
    ("retained corpus rules", re.compile(r"\bretained corpus rules?\b", re.I)),
]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    files = [
        p for p in sorted((repo / "books").glob("vol*/**/*.tex"))
        if not excluded(p)
    ]

    failures = []
    for path in files:
        rel = path.relative_to(repo).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            visible = strip_nonrendered(strip_comment(line))
            for label, rx in BANNED:
                if rx.search(visible):
                    failures.append(f"{rel}:{lineno}: {label}: {visible.strip()}")

    if failures:
        print("C01 QA FAIL — reader-facing workflow residue remains:")
        for f in failures:
            print("  " + f)
        return 1

    print(f"C01 QA PASS — {len(files)} reader-facing TeX files checked.")
    print("No legacy/corpus/dossier/provenance workflow vocabulary remains in rendered book sources.")
    print("Formal audit, source-migration, and provenance records remain preserved outside the reader-facing gate.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
