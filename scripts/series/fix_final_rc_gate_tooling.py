#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    n = text.count(old)
    if n == 0:
        # Idempotence: already fixed is acceptable.
        if new in text:
            print(f"{label}: already fixed")
            return
        raise SystemExit(f"{label}: expected source pattern not found in {path}")
    if n != 1:
        raise SystemExit(f"{label}: expected one source pattern, found {n} in {path}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print(f"{label}: fixed")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()

    p = repo / "scripts/series/audit_reviewed_freezes_i_viii.py"
    old = '''    for raw in manifest.read_text(encoding="utf-8-sig").splitlines():\n        if not raw.strip():\n            continue\n        parts = raw.split(None, 1)\n'''
    new = '''    for raw in manifest.read_text(encoding="utf-8-sig").splitlines():\n        line = raw.strip()\n        if not line or line.startswith("#"):\n            continue\n        parts = line.split(None, 1)\n'''
    replace_once(p, old, new, "freeze manifest comment support")

    canonical_count = '''        includes=len(re.findall(r"(?m)^[ \\t]*\\\\include\\{chapters/ch\\d\\d_[^}]+/chapter\\}",text))\n'''

    p = repo / "scripts/series/verify_series_build.py"
    old = '''        includes=len(re.findall(r"(?m)^[ \\t]*\\\\include\\{",text))\n'''
    replace_once(p, old, canonical_count, "verify canonical chapter include count")

    p = repo / "scripts/series/reconcile_i_viii_release.py"
    old = '''        includes=len(re.findall(r"(?m)^[ \\t]*\\\\include\\{",read_text(book))) if book.exists() else 0\n'''
    new = '''        includes=len(re.findall(r"(?m)^[ \\t]*\\\\include\\{chapters/ch\\d\\d_[^}]+/chapter\\}",read_text(book))) if book.exists() else 0\n'''
    replace_once(p, old, new, "reconciliation canonical chapter include count")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
