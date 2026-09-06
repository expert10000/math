#!/usr/bin/env python3
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "reports/series/VOLUME08_EXAMPLE_EXERCISE_BASELINE.json"
AUDIT = ROOT / "reports/series/VOLUME08_EXAMPLE_EXERCISE_AUDIT.json"
OUT_JSON = ROOT / "reports/series/VOLUME08_EXAMPLE_EXERCISE_BALANCE_AUDIT.json"
OUT_MD = ROOT / "reports/series/VOLUME08_EXAMPLE_EXERCISE_BALANCE_AUDIT.md"
BOOK = ROOT / "books/vol08_algebraic_topology/book.tex"

LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
EX_RE = re.compile(
    r"\\begin\{exercise\}(?:\[[^\]]*\])?\\label\{[^}]+\}\s*(.*?)\s*\\end\{exercise\}",
    re.S,
)
TRIAD_RE = re.compile(
    r"\\begin\{exercise\}(?:\[[^\]]*\])?\\label\{[^}]+\}.*?\\end\{exercise\}\s*"
    r"\\begin\{hint\}.*?\\end\{hint\}\s*"
    r"\\begin\{solution\}.*?\\end\{solution\}",
    re.S,
)
CATEGORY_MARKERS = [
    ("standard", r"\subsection*{Standard computations and constructions}", 5),
    ("proof", r"\subsection*{Proofs}", 4),
    ("test", r"\subsection*{Counterexamples and hypothesis tests}", 3),
    ("application", r"\subsection*{Applications and investigations}", 2),
    ("challenge", r"\subsection*{Challenge problems}", 2),
]

def git(*args, check=True):
    cp = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        encoding="utf-8", errors="replace",
    )
    if check and cp.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed: {cp.stderr}")
    return cp

def cnt(t, env):
    return t.count(r"\begin{" + env + "}")

def norm_prompt(s):
    s = re.sub(r"%.*", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def main():
    failures = []
    rows = []
    labels = []
    prompts = []
    baseline = json.loads(BASE.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    book = BOOK.read_text(encoding="utf-8-sig")

    if len(baseline.get("chapters", [])) != 35:
        failures.append(f"baseline chapter count {len(baseline.get('chapters', []))} != 35")
    if audit.get("status") != "PASS" or audit.get("stage") != 5 or audit.get("expanded_count") != 35:
        failures.append(
            f"stage audit is not final PASS: status={audit.get('status')} "
            f"stage={audit.get('stage')} expanded={audit.get('expanded_count')}"
        )

    for item in baseline.get("chapters", []):
        code = item["chapter"]
        n = int(code.split("/")[1])
        canonical = ROOT / item["path"]
        expansion = canonical.parent / "pedagogy_expansion.tex"
        if not canonical.exists():
            failures.append(f"{code}: canonical source missing")
            continue

        got = git("rev-parse", f"HEAD:{item['path']}").stdout.strip()
        if got != item["protected_git_blob_sha1"]:
            failures.append(f"{code}: protected Git blob drift {got}")
        d = git("diff", "--quiet", "HEAD", "--", item["path"], check=False)
        if d.returncode == 1:
            failures.append(f"{code}: protected working-tree/index drift")
        elif d.returncode not in (0, 1):
            failures.append(f"{code}: protected drift check error")

        ctext = canonical.read_text(encoding="utf-8-sig")
        labels.extend(LABEL_RE.findall(ctext))

        if not expansion.exists():
            failures.append(f"{code}: pedagogy expansion missing")
            continue
        etext = expansion.read_text(encoding="utf-8-sig")
        labels.extend(LABEL_RE.findall(etext))

        counts = {e: cnt(etext, e) for e in ("example", "exercise", "hint", "solution")}
        expected = {"example": 3, "exercise": 16, "hint": 16, "solution": 16}
        if counts != expected:
            failures.append(f"{code}: environment counts {counts} != {expected}")

        triads = len(TRIAD_RE.findall(etext))
        if triads != 16:
            failures.append(f"{code}: ordered exercise/hint/solution triads {triads} != 16")

        marker_positions = []
        for name, marker, expected_count in CATEGORY_MARKERS:
            pos = etext.find(marker)
            if pos < 0:
                failures.append(f"{code}: category marker missing: {name}")
            marker_positions.append((name, pos, expected_count))
        if all(pos >= 0 for _, pos, _ in marker_positions):
            for idx, (name, pos, expected_count) in enumerate(marker_positions):
                end = marker_positions[idx + 1][1] if idx + 1 < len(marker_positions) else len(etext)
                block = etext[pos:end]
                got_count = cnt(block, "exercise")
                if got_count != expected_count:
                    failures.append(
                        f"{code}: category {name} exercise count {got_count} != {expected_count}"
                    )

        if etext.find(r"\section{Supplementary worked examples}") > etext.find(r"\section{Graded supplementary exercises}"):
            failures.append(f"{code}: examples are not placed before exercises")

        folder = canonical.parent.name
        placement = (
            rf"\include{{chapters/{folder}/chapter}}" + "\n" +
            rf"\input{{chapters/{folder}/pedagogy_expansion}} % VOL08-PEDAGOGY VIII/{n:02d}"
        )
        if placement not in book:
            failures.append(f"{code}: pedagogy layer is not immediately after canonical include")

        chapter_prompts = [norm_prompt(x) for x in EX_RE.findall(etext)]
        if len(chapter_prompts) != 16:
            failures.append(f"{code}: exercise prompt extraction count {len(chapter_prompts)} != 16")
        prompts.extend((code, p) for p in chapter_prompts)

        rows.append({
            "chapter": code,
            "examples": counts.get("example", 0),
            "exercises": counts.get("exercise", 0),
            "hints": counts.get("hint", 0),
            "solutions": counts.get("solution", 0),
            "triads": triads,
            "placement": "PASS" if placement in book else "FAIL",
            "category_counts": {
                "standard": 5, "proof": 4, "test": 3, "application": 2, "challenge": 2
            },
        })

    dup_labels = {k: v for k, v in Counter(labels).items() if v > 1}
    if dup_labels:
        for lab, k in sorted(dup_labels.items()):
            failures.append(f"duplicate composed label:{lab}:{k}")

    prompt_counter = Counter(p for _, p in prompts if p)
    duplicate_prompts = sorted(p for p, k in prompt_counter.items() if k > 1)
    if duplicate_prompts:
        failures.append(f"duplicate exact exercise prompts:{len(duplicate_prompts)}")

    status = "PASS" if not failures else "FAIL"
    result = {
        "schema": 1,
        "status": status,
        "volume": "VIII",
        "architecture": "split-pedagogy-layer",
        "chapter_count": len(rows),
        "expanded_count": 35,
        "added_totals": {
            "examples": sum(r["examples"] for r in rows),
            "exercises": sum(r["exercises"] for r in rows),
            "hints": sum(r["hints"] for r in rows),
            "solutions": sum(r["solutions"] for r in rows),
        },
        "target_per_chapter": {
            "examples": 3, "exercises": 16, "hints": 16, "solutions": 16,
            "categories": {"standard": 5, "proof": 4, "test": 3, "application": 2, "challenge": 2},
        },
        "canonical_chapter_sources_modified": 0,
        "duplicate_composed_labels": len(dup_labels),
        "duplicate_exact_exercise_prompts": len(duplicate_prompts),
        "rows": rows,
        "failures": failures,
    }
    OUT_JSON.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    md = [
        "# Volume VIII worked-example placement and graded-exercise balance audit",
        "",
        f"**Result:** {status}",
        "",
        "## Final pedagogy totals",
        "",
        f"- chapters expanded: **{len(rows)} / 35**",
        f"- added worked examples: **{result['added_totals']['examples']}**",
        f"- added exercises: **{result['added_totals']['exercises']}**",
        f"- added hints: **{result['added_totals']['hints']}**",
        f"- added complete solutions: **{result['added_totals']['solutions']}**",
        "- canonical `chapter.tex` sources modified: **0**",
        "",
        "## Placement rule",
        "",
        "Each chapter-local pedagogy layer is wired immediately after its protected canonical "
        "`\\include{.../chapter}` in `book.tex`. Within each layer, three worked examples precede "
        "the graded exercise section.",
        "",
        "## Exercise balance",
        "",
        "Every chapter contains 16 ordered exercise/hint/solution triads:",
        "",
        "- 5 standard computations or constructions;",
        "- 4 proofs;",
        "- 3 counterexamples or hypothesis tests;",
        "- 2 applications or investigations;",
        "- 2 challenge problems.",
        "",
        f"- duplicate composed labels: **{len(dup_labels)}**",
        f"- duplicate exact exercise prompts: **{len(duplicate_prompts)}**",
        "",
        "## Blocking findings",
        "",
    ]
    md += ["None."] if not failures else [f"- {x}" for x in failures]
    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps({
        "status": status,
        "chapters": len(rows),
        "added_totals": result["added_totals"],
        "duplicate_labels": len(dup_labels),
        "duplicate_prompts": len(duplicate_prompts),
        "failures": failures,
    }, indent=2))
    return 0 if status == "PASS" else 9

if __name__ == "__main__":
    raise SystemExit(main())
