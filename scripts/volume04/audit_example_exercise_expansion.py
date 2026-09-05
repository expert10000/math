#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter
from pathlib import Path

VOL = Path("books/vol04_complex_analysis/chapters")
REPORT = Path("reports/series")
BLOCK = re.compile(r"% BEGIN VOL04-EXPANSION ([^\n]+)\n.*?% END VOL04-EXPANSION \1\n?", re.S)
LABEL = re.compile(r"\\label\{([^}]+)\}")
EXAMPLE_BLOCK = re.compile(r"% BEGIN VOL04-EXPANSION (IV\d\d-example-\d\d)\n(.*?)% END VOL04-EXPANSION \1", re.S)
EXERCISE_BLOCK = re.compile(r"% BEGIN VOL04-EXPANSION (IV\d\d-exercises-01)\n(.*?)% END VOL04-EXPANSION \1", re.S)

def strip_expansions(text: str) -> str:
    return BLOCK.sub("", text)

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def count_env(text: str, env: str) -> int:
    return len(re.findall(rf"\\begin\{{{env}\}}", text))

def chapter_files(repo: Path):
    return sorted((repo / VOL).glob("ch*/chapter.tex"))

def baseline_row(base: dict, code: str):
    return next((x for x in base.get("chapters", []) if x.get("chapter") == code), None)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--snapshot", action="store_true")
    ap.add_argument("--stage", type=int, default=1, choices=[1, 2, 3])
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    out = repo / REPORT
    baseline_path = out / "VOLUME04_EXAMPLE_EXERCISE_BASELINE.json"
    base = json.loads(baseline_path.read_text(encoding="utf-8")) if baseline_path.exists() else {}
    blockers: list[str] = []
    rows: list[dict] = []
    all_labels: list[str] = []
    files = chapter_files(repo)
    if len(files) != 31:
        blockers.append(f"CHAPTER_COUNT:{len(files)}!=31")
    if args.stage > 1 and not base:
        blockers.append("MISSING_COMMIT1_BASELINE")

    for i, path in enumerate(files, 1):
        code = f"IV/{i:02d}"
        text = path.read_text(encoding="utf-8-sig")
        labels = LABEL.findall(text)
        all_labels.extend(labels)
        exblocks = list(EXAMPLE_BLOCK.finditer(text))
        exercise_blocks = list(EXERCISE_BLOCK.finditer(text))
        row = {
            "chapter": code,
            "path": path.relative_to(repo).as_posix(),
            "examples": count_env(text, "example"),
            "exercises": count_env(text, "exercise"),
            "hints": count_env(text, "hint"),
            "problems": count_env(text, "problem"),
            "solutions": count_env(text, "solution"),
            "labels": len(labels),
            "protected_sha256": sha256(strip_expansions(text)),
            "expansion_examples": len(exblocks),
            "expansion_exercise_blocks": len(exercise_blocks),
            "expansion_exercises": sum(count_env(m.group(2), "exercise") for m in exercise_blocks),
            "expansion_hints": sum(count_env(m.group(2), "hint") for m in exercise_blocks),
            "expansion_solutions": sum(count_env(m.group(2), "solution") for m in exercise_blocks),
        }
        rows.append(row)
        if row["exercises"] != row["hints"]:
            blockers.append(f"{code}:EXERCISE_HINT_MISMATCH:{row['exercises']}!={row['hints']}")
        if row["solutions"] < row["exercises"] + row["problems"]:
            blockers.append(f"{code}:SOLUTION_COVERAGE")

        old = baseline_row(base, code)
        if old and old.get("protected_sha256") != row["protected_sha256"]:
            blockers.append(f"{code}:PROTECTED_TEXT_CHANGED")

        enriched = (args.stage >= 2 and i <= 11) or (args.stage >= 3 and 12 <= i <= 18)
        if enriched:
            if not old:
                blockers.append(f"{code}:MISSING_BASELINE_ROW")
            else:
                expected_examples = old["examples"] + 3
                expected_exercises = old["exercises"] + 16
                expected_hints = old["hints"] + 16
                expected_solutions = old["solutions"] + 16
                if row["examples"] != expected_examples:
                    blockers.append(f"{code}:EXAMPLES:{row['examples']}!={expected_examples}")
                if row["exercises"] != expected_exercises:
                    blockers.append(f"{code}:EXERCISES:{row['exercises']}!={expected_exercises}")
                if row["hints"] != expected_hints:
                    blockers.append(f"{code}:HINTS:{row['hints']}!={expected_hints}")
                if row["solutions"] != expected_solutions:
                    blockers.append(f"{code}:SOLUTIONS:{row['solutions']}!={expected_solutions}")
            if row["expansion_examples"] != 3:
                blockers.append(f"{code}:EXPANSION_EXAMPLES:{row['expansion_examples']}!=3")
            if row["expansion_exercise_blocks"] != 1:
                blockers.append(f"{code}:EXPANSION_EXERCISE_BLOCKS:{row['expansion_exercise_blocks']}!=1")
            if row["expansion_exercises"] != 16:
                blockers.append(f"{code}:EXPANSION_EXERCISES:{row['expansion_exercises']}!=16")
            if row["expansion_hints"] != 16:
                blockers.append(f"{code}:EXPANSION_HINTS:{row['expansion_hints']}!=16")
            if row["expansion_solutions"] != 16:
                blockers.append(f"{code}:EXPANSION_SOLUTIONS:{row['expansion_solutions']}!=16")
        elif args.stage >= 2 and 19 <= i <= 31:
            # Later chapters remain protected and untouched in this package.
            if row["expansion_examples"] or row["expansion_exercise_blocks"]:
                blockers.append(f"{code}:UNEXPECTED_EARLY_EXPANSION")

    for lab, n in Counter(all_labels).items():
        if n > 1:
            blockers.append(f"DUPLICATE_LABEL:{lab}")

    status = "PASS" if not blockers else "FAIL"
    result = {"status": status, "stage": args.stage, "chapters": rows, "blocking": blockers}

    if not args.check_only:
        out.mkdir(parents=True, exist_ok=True)
        if args.snapshot:
            if any(r["expansion_examples"] or r["expansion_exercise_blocks"] for r in rows):
                blockers.append("SNAPSHOT_REFUSED:EXPANSION_MARKERS_ALREADY_PRESENT")
                status = "FAIL"
                result["status"] = status
                result["blocking"] = blockers
            else:
                baseline_path.write_text(
                    json.dumps({"schema": 1, "volume": "IV", "chapters": rows}, indent=2) + "\n",
                    encoding="utf-8",
                )
        (out / "VOLUME04_EXAMPLE_EXERCISE_AUDIT.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md = [
            "# Volume IV worked-example and graded-exercise audit", "",
            f"**Result:** {status}", "",
            f"**Stage:** {args.stage}", "",
            "| Chapter | Examples | Exercises | Hints | Problems | Solutions | New examples | New exercises |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for r in rows:
            md.append(
                f"| {r['chapter']} | {r['examples']} | {r['exercises']} | {r['hints']} | "
                f"{r['problems']} | {r['solutions']} | {r['expansion_examples']} | {r['expansion_exercises']} |"
            )
        md += ["", "## Blocking findings", ""] + ([f"- {b}" for b in blockers] if blockers else ["None."])
        (out / "VOLUME04_EXAMPLE_EXERCISE_AUDIT.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps({"status": status, "stage": args.stage, "blocking": blockers}, indent=2))
    return 0 if status == "PASS" else 9

if __name__ == "__main__":
    raise SystemExit(main())
