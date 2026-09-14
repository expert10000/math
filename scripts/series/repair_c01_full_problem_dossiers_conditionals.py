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
    paths = [
        x.strip()
        for x in git(repo, "ls-files", "books/**/*.tex").stdout.splitlines()
        if x.strip()
    ]

    repaired: list[str] = []
    suspicious: list[str] = []

    for rel in paths:
        path = repo / rel
        if not path.is_file():
            continue

        current = path.read_text(encoding="utf-8-sig")
        old = parent_text(repo, rel)
        if old is None:
            continue

        old_open = old.count(OPEN)
        cur_open = current.count(OPEN)
        if old_open == 0 or cur_open == 0:
            continue

        old_close = old.count(CLOSE)
        cur_close = current.count(CLOSE)

        # C01's provenance cleanup accidentally removed the final \fi in a
        # family of problem files. Repair only when the parent version proves
        # that a closing \fi existed and the current version lost it.
        missing = old_close - cur_close

        if (
            missing > 0
            and old_open == cur_open
            and old.rstrip().endswith(CLOSE)
            and not current.rstrip().endswith(CLOSE)
        ):
            # In the affected family the missing closure(s) are at EOF.
            fixed = current.rstrip() + "\n" + ("\n".join([CLOSE] * missing)) + "\n"
            path.write_text(fixed, encoding="utf-8", newline="\n")
            repaired.append(rel)
            print(f"  REPAIR {rel}: restored {missing} closing \\\\fi token(s)")
        elif old_open == cur_open and old_close > cur_close:
            suspicious.append(
                f"{rel}: parent had {old_close} \\\\fi, current has {cur_close}; "
                "not repaired automatically because the missing closure is not proven to be at EOF"
            )

    print(f"C01 conditional repair: {len(repaired)} file(s) repaired.")

    if suspicious:
        print("C01 CONDITIONAL REPAIR NEEDS REVIEW:")
        for item in suspicious:
            print("  " + item)
        return 2

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
