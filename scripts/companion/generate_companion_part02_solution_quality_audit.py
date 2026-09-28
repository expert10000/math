#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ALLOWED = ("A_STRONG", "B_POLISH", "C_REWRITE", "D_BLOCKING")

KNOWN_GATES = {
    # Important mathematical/source corrections from the Part II completion pass.
    "CP-II-0315": [
        ("SIGN_CORRECTION", ("-D_i u",)),
    ],
    "CP-II-0494": [
        ("DOMAIN_CORRECTION", ("does not define a map",)),
        ("UNBOUNDED_BASIS_TEST", (r"\|Te_N\|_\infty=N",)),
    ],
    "CP-II-0451": [
        ("H1_SCALING_CORRECTION", ("2\\pi n",)),
    ],
    "CP-II-0484": [
        ("DISJOINT_COMPACTS_CORRECTION", ("1/3", "2/3")),
    ],
    "CP-II-0519": [
        ("NORM_ORDER_CORRECTION", (r"\|z\|_\infty", r"\|z\|_2", r"\|z\|_1")),
    ],
    "CP-II-0521": [
        ("FRACTIONAL_THRESHOLD", ("1/2",)),
    ],
    "CP-II-0561": [
        ("2ADIC_COUNTEREXAMPLE", ("ultrametric",)),
    ],
}

FRAGMENT_PATTERNS = re.compile(
    r"\b(?:"
    r"source fragment|source excerpt|"
    r"missing context|cannot reconstruct|not enough information|"
    r"source does not include|"
    r"formula (?:is|was) omitted|"
    r"definition (?:is|was) omitted|"
    r"statement (?:is|was) omitted"
    r")\b",
    re.I,
)
WEAK_PHRASES = re.compile(
    r"\b(immediate|standard|clearly|obvious|similarly|routine|"
    r"follows directly|by a standard argument)\b",
    re.I,
)
SOURCE_NOTE = re.compile(
    r"\b(Source correction|Source-boundary note|Source restoration|"
    r"migrated source|source statement|source fragment)\b",
    re.I,
)
SECTIONISH = re.compile(
    r"\\(?:section|subsection|subsubsection)\*?\{|"
    r"\bExercise\s+\d+(?:\.\d+)?\b|"
    r"\bProblem\s+\d+\b",
    re.I,
)


def words(tex: str) -> int:
    s = re.sub(r"%.*", " ", tex)
    s = re.sub(r"\\[A-Za-z@]+(?:\*|\b)?", " ", s)
    s = re.sub(r"[{}$\\[\]_~^&]", " ", s)
    return len([x for x in re.split(r"\s+", s) if x])


def math_density(tex: str) -> int:
    return (
        len(re.findall(r"\\\[", tex))
        + len(re.findall(r"\\begin\{(?:align|aligned|equation|cases)", tex))
        + len(re.findall(r"\$[^$]+\$", tex))
    )


def title_present(problem: str) -> bool:
    # Canonical title: a bold heading near the start, before substantial prose.
    head = problem[:900]
    return bool(re.search(r"\\textbf\{[^}]{4,100}\}", head))


def named_sections(solution: str) -> tuple[bool, bool, bool]:
    theory = bool(re.search(r"\\textbf\{Theory\b|\\textit\{Theory\b", solution, re.I))
    examples = bool(re.search(r"\\textbf\{Examples?\b|\\textit\{Examples?\b", solution, re.I))
    extensions = bool(re.search(r"\\textbf\{Extensions?\b|\\textit\{Extensions?\b", solution, re.I))
    return theory, examples, extensions


def problem_solution_pairs(tex: str):
    starts = list(re.finditer(r"\\begin\{problem\}\[(CP-II-\d{4})\]", tex))
    for i, m in enumerate(starts):
        pid = m.group(1)
        a = m.start()
        b = starts[i + 1].start() if i + 1 < len(starts) else len(tex)
        window = tex[a:b]
        pm = re.search(
            r"\\begin\{problem\}\[" + re.escape(pid) + r"\](.*?)\\end\{problem\}",
            window,
            re.S,
        )
        sols = list(re.finditer(r"\\begin\{solution\}(.*?)\\end\{solution\}", window, re.S))
        problem = pm.group(1).strip() if pm else ""
        solution = sols[0].group(1).strip() if len(sols) == 1 else ""
        yield pid, problem, solution, len(sols), window


def classify(pid: str, problem: str, solution: str, sol_count: int):
    pw = words(problem)
    sw = words(solution)
    md = math_density(solution)
    title = title_present(problem)
    weak_count = len(WEAK_PHRASES.findall(solution))
    fragment = bool(FRAGMENT_PATTERNS.search(problem + "\n" + solution))
    source_note = bool(SOURCE_NOTE.search(problem + "\n" + solution))
    sectionish = len(SECTIONISH.findall(problem))
    theory, examples, extensions = named_sections(solution)

    flags: list[str] = []
    blockers: list[str] = []

    if sol_count != 1:
        blockers.append(f"paired_solution_count={sol_count}")
    if not solution.strip():
        blockers.append("empty_solution")
    if sw < 35 and pw >= 80:
        blockers.append("solution_extremely_short")

    # Known mathematical regression gates.
    for gate_name, required_groups in KNOWN_GATES.get(pid, []):
        for group in required_groups:
            if group not in solution:
                blockers.append(f"known_gate_missing:{gate_name}:{group}")

    # The old CP-II-0315 solution may contain the wrong sign while still
    # mentioning D_i. Detect a common wrong formulation explicitly.
    if pid == "CP-II-0315":
        compact = re.sub(r"\s+", " ", solution)
        if "converges to D_i u" in compact and "converges to -D_i u" not in compact:
            blockers.append("known_gate_wrong_sign:CP-II-0315")

    if blockers:
        status = "D_BLOCKING"
        priority = "P0"
    else:
        overmerge = (
            sectionish >= 3
            or pw > 1800
            or (pw > 1000 and sw < max(120, int(0.18 * pw)))
        )
        terse = (
            sw < 110
            or (pw > 500 and sw < 160)
            or (pw > 900 and sw < int(0.22 * pw))
        )
        weak_proof = weak_count >= 4 and sw < 260
        if overmerge or fragment or (terse and pw > 250):
            status = "C_REWRITE"
            priority = "P1"
        elif terse or weak_proof or not title:
            status = "B_POLISH"
            priority = "P2"
        else:
            status = "A_STRONG"
            priority = "P3"

    if not title:
        flags.append("MISSING_DESCRIPTIVE_TITLE")
    if sw < 110:
        flags.append("TERSE_SOLUTION")
    if pw > 1000:
        flags.append("LONG_PROBLEM_BODY")
    if sectionish >= 3:
        flags.append("POSSIBLE_OVERMERGE")
    if fragment:
        flags.append("FRAGMENT_OR_SOURCE_GAP")
    if source_note:
        flags.append("SOURCE_CORRECTION_PRESENT")
    if weak_count >= 4:
        flags.append("MANY_SHORTCUT_PHRASES")
    if md == 0 and sw > 90:
        flags.append("LOW_MATH_DENSITY")

    theory_needed = "YES" if pw >= 260 or status in {"C_REWRITE", "D_BLOCKING"} else "OPTIONAL"
    examples_recommended = "YES" if status in {"B_POLISH", "C_REWRITE"} and sw < 260 else "OPTIONAL"
    extensions_recommended = "OPTIONAL"

    reasons: list[str] = []
    if blockers:
        reasons.extend(blockers)
    if status == "C_REWRITE":
        if fragment:
            reasons.append("source/statement fragment needs coherent reconstruction")
        if sectionish >= 3 or pw > 1800:
            reasons.append("problem boundary appears overmerged or mini-chapter sized")
        if terse:
            reasons.append("solution too short relative to task")
    if status == "B_POLISH":
        if not title:
            reasons.append("needs descriptive problem name")
        if terse:
            reasons.append("solution needs expansion")
        if source_note:
            reasons.append("source correction/restoration should be editorially normalized")
        if weak_proof:
            reasons.append("too many shortcut phrases replace proof detail")
    if status == "A_STRONG":
        reasons.append("substantial solution with no deterministic blocker/rewrite trigger")

    action = {
        "A_STRONG": "Retain; copy-edit into the Part III six-part convention where useful.",
        "B_POLISH": "Polish to the Part III convention: title, exact statement, focused theory if needed, fuller worked steps, and useful examples/extensions.",
        "C_REWRITE": "Reconstruct the canonical problem boundary if necessary and rewrite the solution as a matched worked argument.",
        "D_BLOCKING": "Repair correctness/pairing/source defect before any editorial polish.",
    }[status]

    return {
        "quality_status": status,
        "priority": priority,
        "problem_words": pw,
        "solution_words": sw,
        "math_density": md,
        "title_present": "YES" if title else "NO",
        "theory_needed": theory_needed,
        "examples_recommended": examples_recommended,
        "extensions_recommended": extensions_recommended,
        "flags": ";".join(flags),
        "finding": "; ".join(reasons),
        "required_action": action,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve()

    base = repo / "books" / "companion_problems_solutions"
    chapter = base / "chapters" / "part02_volume_ii" / "chapter.tex"
    ledger = base / "metadata" / "PART_II_MIGRATION.tsv"
    out_tsv = base / "metadata" / "PART_II_SOLUTION_QUALITY_AUDIT.tsv"
    out_md = base / "metadata" / "PART_II_SOLUTION_QUALITY_AUDIT.md"

    if not chapter.exists():
        raise SystemExit(f"missing chapter: {chapter}")
    if not ledger.exists():
        raise SystemExit(f"missing migration ledger: {ledger}")

    tex = chapter.read_text(encoding="utf-8")
    with ledger.open("r", encoding="utf-8-sig", newline="") as f:
        migration = list(csv.DictReader(f, delimiter="\t"))

    provenance = {}
    for r in migration:
        pid = r.get("companion_problem_id", "")
        solution_status = (r.get("solution_status") or "").strip()
        provenance[pid] = (
            "SOURCE_BACKED"
            if solution_status.startswith("MIGRATED_PRIMARY_SOLUTION")
            else "CANONICAL_AUTHORED"
        )

    rows = []
    for pid, problem, solution, sol_count, window in problem_solution_pairs(tex):
        c = classify(pid, problem, solution, sol_count)
        rows.append({
            "companion_problem_id": pid,
            "solution_provenance": provenance.get(pid, "UNKNOWN"),
            **c,
        })

    fields = [
        "companion_problem_id",
        "solution_provenance",
        "quality_status",
        "priority",
        "problem_words",
        "solution_words",
        "math_density",
        "title_present",
        "theory_needed",
        "examples_recommended",
        "extensions_recommended",
        "flags",
        "finding",
        "required_action",
    ]
    with out_tsv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    counts = Counter(r["quality_status"] for r in rows)
    pcounts = Counter(r["priority"] for r in rows)
    prov = Counter(r["solution_provenance"] for r in rows)

    if prov.get("SOURCE_BACKED", 0) != 165:
        raise RuntimeError(
            f"Part II provenance mismatch: expected 165 source-backed rows, "
            f"got {prov.get('SOURCE_BACKED', 0)}"
        )
    if prov.get("CANONICAL_AUTHORED", 0) != 405:
        raise RuntimeError(
            f"Part II provenance mismatch: expected 405 canonical-authored rows, "
            f"got {prov.get('CANONICAL_AUTHORED', 0)}"
        )

    queue = defaultdict(list)
    for r in rows:
        queue[r["quality_status"]].append(r["companion_problem_id"])

    lines = [
        "# Companion Part II solution-quality audit",
        "",
        "This is the first full 570-pair editorial triage against",
        "`COMPANION_SOLUTION_EDITORIAL_STANDARD.md`.",
        "",
        "The audit is deliberately separate from solution coverage. It does not modify",
        "the Part II mathematics.",
        "",
        "## Coverage",
        "",
        f"- audited problem/solution pairs: **{len(rows)}**",
        f"- source-backed provenance rows: **{prov.get('SOURCE_BACKED',0)}**",
        f"- canonical-authored provenance rows: **{prov.get('CANONICAL_AUTHORED',0)}**",
        "",
        "## Quality result",
        "",
        f"- `A_STRONG`: **{counts.get('A_STRONG',0)}**",
        f"- `B_POLISH`: **{counts.get('B_POLISH',0)}**",
        f"- `C_REWRITE`: **{counts.get('C_REWRITE',0)}**",
        f"- `D_BLOCKING`: **{counts.get('D_BLOCKING',0)}**",
        "",
        "## Priority queues",
        "",
        f"- `P0`: **{pcounts.get('P0',0)}**",
        f"- `P1`: **{pcounts.get('P1',0)}**",
        f"- `P2`: **{pcounts.get('P2',0)}**",
        f"- `P3`: **{pcounts.get('P3',0)}**",
        "",
        "## Interpretation",
        "",
        "This audit is a deterministic editorial triage. `D_BLOCKING` includes exact",
        "pairing failures and selected known mathematical regression gates from the",
        "Part II completion pass. `C_REWRITE` captures large overmerges, fragments,",
        "and solutions that are too short for the task. `B_POLISH` captures pairs",
        "that are basically usable but do not yet meet the Part III editorial",
        "convention.",
        "",
        "The rewrite/polish passes should still read the exact current problem and",
        "solution before changing mathematics; the audit is a queue, not a substitute",
        "for mathematical review.",
        "",
    ]

    for status in ("D_BLOCKING", "C_REWRITE", "B_POLISH"):
        ids = queue.get(status, [])
        lines += [f"## {status} queue", ""]
        if not ids:
            lines.append("None.")
        else:
            # Compact line wrapping.
            chunk = []
            for pid in ids:
                chunk.append(f"`{pid}`")
                if len(chunk) == 10:
                    lines.append(", ".join(chunk))
                    chunk = []
            if chunk:
                lines.append(", ".join(chunk))
        lines.append("")

    out_md.write_text("\n".join(lines), encoding="utf-8")

    print("COMPANION PART II SOLUTION-QUALITY AUDIT GENERATED")
    print(f"  audited pairs: {len(rows)}")
    print(f"  source-backed: {prov.get('SOURCE_BACKED',0)}")
    print(f"  canonical-authored: {prov.get('CANONICAL_AUTHORED',0)}")
    print(f"  A_STRONG: {counts.get('A_STRONG',0)}")
    print(f"  B_POLISH: {counts.get('B_POLISH',0)}")
    print(f"  C_REWRITE: {counts.get('C_REWRITE',0)}")
    print(f"  D_BLOCKING: {counts.get('D_BLOCKING',0)}")
    print(f"  P0/P1/P2/P3: {pcounts.get('P0',0)}/{pcounts.get('P1',0)}/{pcounts.get('P2',0)}/{pcounts.get('P3',0)}")
    print("  TSV:", out_tsv)
    print("  MD:", out_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
