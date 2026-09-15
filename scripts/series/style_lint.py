#!/usr/bin/env python3
"""Run the conservative final copy-edit lint on canonical chapter sources.

This is intentionally a style guard, not a prose generator: it rejects a small
set of low-information transition phrases and TeX hygiene defects without
rewriting mathematical content or inferring theorem hypotheses.
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


LOW_INFORMATION = {
    "we_now_prove": re.compile(r"\bwe now prove\b", re.I),
    "we_now_show": re.compile(r"\bwe now show\b", re.I),
    "we_now_turn": re.compile(r"\bwe now turn\b", re.I),
    "we_now_consider": re.compile(r"\bwe now consider\b", re.I),
    "we_are_now_ready": re.compile(r"\bwe are now ready\b", re.I),
    "it_is_clear_that": re.compile(r"\bit is clear that\b", re.I),
    "obviously": re.compile(r"\bobviously\b", re.I),
}


def chapter_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def report_tsv(rows: list[dict[str, str]]) -> str:
    from io import StringIO
    output = StringIO(newline="")
    fields = ["check", "status", "count", "detail"]
    writer = csv.DictWriter(output, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def rendered_report(rows: list[dict[str, str]], chapters: int, tex_files: int) -> str:
    lines = [
        "# Final Copy-Edit and Clarity Audit", "",
        "The C11 lint operates only on canonical chapter sources listed in `editorial/CHAPTER_STATUS.tsv`.",
        "It is deliberately conservative: it catches mechanical style regressions but does not try to alter mathematical claims, hypotheses, or notation.",
        "", f"- Canonical chapter entries checked: **{chapters}**", f"- Canonical TeX files checked: **{tex_files}**", "",
        "| Check | Status | Count |", "|---|---|---:|",
    ]
    lines.extend(f"| {row['check']} | {row['status']} | {row['count']} |" for row in rows)
    lines += ["", "## Interpretation", "", "A `PASS` means no blocker for that narrow check. The accompanying copy-edit policy requires a human review of terminology, theorem naming, notation introduction, paragraph dependency, and display integration; those judgments are intentionally not automated.", ""]
    return "\n".join(lines)


def write_or_check(path: Path, content: str, check: bool, stale: list[str], repo: Path) -> None:
    content = content.rstrip() + "\n"
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            stale.append(path.relative_to(repo).as_posix())
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--check", action="store_true", help="verify that committed reports match the source")
    args = parser.parse_args()
    repo = args.repo.resolve()
    chapters = chapter_rows(repo / "editorial/CHAPTER_STATUS.tsv")
    findings: dict[str, list[str]] = {name: [] for name in LOW_INFORMATION}
    trailing, tabs, missing = [], [], []
    for chapter in chapters:
        path = repo / chapter["canonical_path"]
        if not path.exists():
            missing.append(chapter["chapter_code"])
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8-sig", errors="replace").splitlines(), 1):
            if line.rstrip() != line:
                trailing.append(f"{chapter['chapter_code']}:{number}")
            if "\t" in line:
                tabs.append(f"{chapter['chapter_code']}:{number}")
            if line.lstrip().startswith("%"):
                continue
            for name, pattern in LOW_INFORMATION.items():
                if pattern.search(line):
                    findings[name].append(f"{chapter['chapter_code']}:{number}")

    checks = [("chapter_ledger_count", [] if len(chapters) == 256 else [str(len(chapters))]), ("missing_canonical_sources", missing), ("trailing_whitespace", trailing), ("tab_characters", tabs)]
    checks.extend((name, values) for name, values in findings.items())
    rows = [{"check": name, "status": "PASS" if not values else "FAIL", "count": str(len(values)), "detail": "; ".join(values[:8]) or "-"} for name, values in checks]
    stale: list[str] = []
    report_dir = repo / "reports/series"
    write_or_check(report_dir / "COPYEDIT_STYLE_AUDIT.tsv", report_tsv(rows), args.check, stale, repo)
    write_or_check(report_dir / "COPYEDIT_STYLE_AUDIT.md", rendered_report(rows, len(chapters), len(chapters) - len(missing)), args.check, stale, repo)
    failures = [row["check"] for row in rows if row["status"] != "PASS"]
    if stale:
        failures.extend(f"OUT_OF_DATE:{path}" for path in stale)
    print(f"Copy-edit lint checked {len(chapters)} canonical chapters.")
    if failures:
        print("FAIL: " + ", ".join(failures))
        return 3
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
