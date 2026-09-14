#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

OPEN = r"\ifdefined\FullProblemDossiers"
CLOSE = r"\fi"

def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=check,
    )

def parent_text(repo: Path, rel: str) -> str | None:
    p = git(repo, "show", f"HEAD^:{rel}", check=False)
    if p.returncode != 0:
        return None
    return p.stdout

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()

    failures: list[str] = []
    checked = 0

    for rel in git(repo, "ls-files", "books/**/*.tex").stdout.splitlines():
        rel = rel.strip()
        if not rel:
            continue
        path = repo / rel
        if not path.is_file():
            continue

        cur = path.read_text(encoding="utf-8-sig")
        old = parent_text(repo, rel)
        if old is None or OPEN not in old:
            continue

        checked += 1
        if old.count(OPEN) == cur.count(OPEN) and old.count(CLOSE) > cur.count(CLOSE):
            failures.append(
                f"{rel}: lost closing conditional(s): "
                f"parent fi={old.count(CLOSE)}, current fi={cur.count(CLOSE)}"
            )

        # The known problem-file pattern must not leave a FullProblemDossiers
        # conditional open through EOF.
        last_open = cur.rfind(OPEN)
        if last_open >= 0 and cur.find(CLOSE, last_open) < 0:
            failures.append(f"{rel}: {OPEN} has no later \\\\fi")

    if failures:
        print("FULL-PROBLEM-DOSSIER CONDITIONAL QA FAIL")
        for f in failures:
            print("  " + f)
        return 1

    print(f"FULL-PROBLEM-DOSSIER CONDITIONAL QA PASS — {checked} parent/current TeX files checked.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
