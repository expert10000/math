#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

# Reuse the canonical, already-tested statement/solution normalization from Part II.
from migrate_companion_part02 import (
    MIGRATION_FIELDS,
    read_tsv,
    write_tsv,
    extract_range,
    clean_statement,
    choose_primary_solution,
    tex_escape_heading,
)

VOLUME = "IV"
PART = "04"

THEME_ORDER = [
    ("Holomorphic Functions", "IV/01--IV/06"),
    ("Singularities and Residues", "IV/07--IV/11"),
    ("Global Complex Analysis", "IV/12--IV/18"),
    ("Special Functions", "IV/19--IV/21"),
    ("Riemann Surfaces", "IV/22--IV/26"),
    ("Elliptic Functions", "IV/27--IV/31"),
]

def read_manifest(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = [dict(r) for r in csv.DictReader(f, delimiter="\t")]
    return {
        r.get("companion_problem_id", ""): r
        for r in rows
        if r.get("companion_problem_id")
    }

def rel_for_input(path_value: str) -> str:
    # chapter.tex is included from books/companion_problems_solutions/book.tex,
    # so figure input paths are relative to the Companion book root.
    s = (path_value or "").strip().replace("\\", "/")
    if s.startswith("books/companion_problems_solutions/"):
        s = s[len("books/companion_problems_solutions/"):]
    return s

def main() -> int:
    ap = argparse.ArgumentParser(description="Migrate Companion Part IV problem corpus.")
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    ap.add_argument(
        "--no-designed-figures",
        action="store_true",
        help="Do not insert staged designed Part IV TikZ figures."
    )
    args = ap.parse_args()
    repo = args.repo.resolve()

    inv = repo / "imports" / "problem_inventory"
    base = repo / "books" / "companion_problems_solutions"
    source_root = repo / "imports" / "ALL_TEX_AND_FIGURES" / "tex"

    atlas_path = base / "metadata" / "COMPANION_PROBLEM_ATLAS.tsv"
    ledger_path = inv / "PROBLEM_LEDGER.tsv"
    links_path = inv / "PROBLEM_SOLUTION_LINKS.tsv"
    chapter_path = base / "chapters" / "part04_volume_iv" / "chapter.tex"
    migration_path = base / "metadata" / "PART_IV_MIGRATION.tsv"
    summary_path = base / "metadata" / "PART_IV_MIGRATION_SUMMARY.md"
    designed_manifest_path = base / "metadata" / "PART_IV_CANDIDATE_FIGURE_MANIFEST.tsv"
    source_figure_audit_path = base / "metadata" / "PART_IV_FIGURE_AUDIT.tsv"

    for p in (atlas_path, ledger_path, links_path):
        if not p.exists():
            print(f"ERROR: missing required input: {p}")
            return 2
    if not source_root.exists():
        print(f"ERROR: source corpus missing: {source_root}")
        return 2

    _, atlas = read_tsv(atlas_path)
    _, ledger = read_tsv(ledger_path)
    _, links = read_tsv(links_path)
    designed = read_manifest(designed_manifest_path)

    part = [r for r in atlas if r.get("related_volume", "") == VOLUME]
    if not part:
        print("ERROR: no Volume IV rows in Companion atlas")
        return 2

    ledger_by_id = {r.get("problem_id", ""): r for r in ledger}
    links_list = list(links)

    by_theme: dict[str, list[dict]] = defaultdict(list)
    migration_rows = []
    rendered = 0
    with_solution = 0
    holds = 0
    multi_solution = 0
    designed_placed = 0
    designed_missing = 0

    theme_ranges = dict(THEME_ORDER)

    for ar in sorted(part, key=lambda r: r.get("companion_problem_id", "")):
        cp = ar.get("companion_problem_id", "")
        sid = ar.get("semantic_unit_id", "")
        rep = ar.get("representative_problem_id", "")
        lr = ledger_by_id.get(rep, {})

        source_file = lr.get("source_file", "")
        source_range = lr.get("source_line_range", "")
        raw_statement = extract_range(source_root, source_file, source_range)
        statement = clean_statement(raw_statement)

        member_ids = {x for x in ar.get("source_problem_ids", "").split(";") if x}
        if rep:
            member_ids.add(rep)

        primary_row, solution, alternate_ids, distinct_variants = choose_primary_solution(
            member_ids, links_list, source_root
        )
        if distinct_variants > 1:
            multi_solution += 1

        theme = ar.get("thematic_section", "") or "Holomorphic Functions"
        related = ar.get("related_chapters", "") or theme_ranges.get(theme, "IV/01--IV/31")

        figure_input = ""
        manifest_row = designed.get(cp)
        if manifest_row and not args.no_designed_figures:
            rel = rel_for_input(manifest_row.get("file", ""))
            target = base / rel
            if rel and target.exists():
                figure_input = rel
            else:
                designed_missing += 1

        if not statement:
            statement_status = "EDITORIAL_HOLD_EMPTY_STATEMENT"
            migration_status = "EDITORIAL_HOLD"
            holds += 1
        else:
            statement_status = "MIGRATED"
            migration_status = "MIGRATED_TO_COMPANION"
            rendered += 1
            if solution:
                with_solution += 1
            if figure_input:
                designed_placed += 1
            by_theme[theme].append({
                "cp": cp,
                "statement": statement,
                "solution": solution,
                "related": related,
                "figure_input": figure_input,
            })

        if solution:
            sol_status = "MIGRATED_PRIMARY_SOLUTION"
            if distinct_variants > 1:
                sol_status += ";ALTERNATE_VARIANTS_RETAINED_IN_PROVENANCE"
        elif ar.get("has_solution", "").upper() == "YES":
            sol_status = "SOLUTION_EXPECTED_BUT_NOT_SAFELY_RECOVERED"
        else:
            sol_status = "NO_RECONCILED_SOLUTION"

        notes = ["Reader-facing provenance suppressed; exact source lineage retained here."]
        if manifest_row:
            notes.append(
                "Designed figure: "
                + (manifest_row.get("file", "") or "manifest row present")
            )

        migration_rows.append({
            "companion_problem_id": cp,
            "semantic_unit_id": sid,
            "representative_problem_id": rep,
            "thematic_section": theme,
            "related_chapters": related,
            "atlas_editorial_status": ar.get("editorial_status", ""),
            "source_problem_ids": ar.get("source_problem_ids", ""),
            "statement_source_file": source_file,
            "statement_line_range": source_range,
            "statement_status": statement_status,
            "solution_status": sol_status,
            "primary_solution_id": primary_row.get("solution_id", "") if primary_row else "",
            "primary_solution_source_file": primary_row.get("solution_source_file", "") if primary_row else "",
            "primary_solution_line_range": primary_row.get("solution_line_range", "") if primary_row else "",
            "distinct_solution_variants": distinct_variants,
            "alternate_solution_ids": ";".join(alternate_ids),
            "figure_requirement": ar.get("figure_requirement", ""),
            "figure_status": ar.get("figure_status", ""),
            "migration_status": migration_status,
            "notes": " ".join(notes),
        })

    out = [
        r"\chapter{Problems Related to Volume IV}",
        r"\label{ch:companion-iv}",
        "",
        r"\par\medskip\noindent\textbf{Main-text correspondence.}\quad",
        r"This Part accompanies \emph{Volume IV: Complex Analysis and Riemann Surfaces}.",
        r"Problems are grouped by mathematical theme rather than by reproducing the main-text chapter sequence.",
        r"Each section gives the corresponding chapter range for further reading.",
        "",
    ]

    known_themes = {x[0] for x in THEME_ORDER}
    ordered_themes = [x[0] for x in THEME_ORDER] + sorted(
        k for k in by_theme if k not in known_themes
    )

    for theme in ordered_themes:
        items = by_theme.get(theme, [])
        if not items:
            continue
        related = theme_ranges.get(theme) or items[0]["related"]
        out += [
            rf"\section{{{tex_escape_heading(theme)}}}",
            "",
            rf"\par\medskip\noindent\textbf{{Related material.}}\quad Volume IV, Chapters \texttt{{{related}}}.",
            "",
        ]

        for item in items:
            label = item["cp"].lower()
            out += [
                rf"\begin{{problem}}[{item['cp']}]",
                rf"\label{{prob:{label}}}",
                item["statement"],
                r"\end{problem}",
                "",
            ]

            if item["figure_input"]:
                out += [
                    rf"\input{{{item['figure_input']}}}",
                    "",
                ]

            if item["solution"]:
                out += [
                    r"\begin{solution}",
                    item["solution"],
                    r"\end{solution}",
                    "",
                ]

    if holds:
        out += [
            r"\section*{Editorially held source items}",
            r"\addcontentsline{toc}{section}{Editorially held source items}",
            "",
            r"A small number of reconciled source records could not be rendered safely because the",
            r"representative source span contains no recoverable mathematical statement. They remain",
            r"preserved in the Part IV migration ledger and are not silently replaced or reconstructed.",
            "",
        ]

    chapter_path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    write_tsv(migration_path, MIGRATION_FIELDS, migration_rows)

    by_theme_counts = Counter(
        r["thematic_section"]
        for r in migration_rows
        if r["migration_status"] == "MIGRATED_TO_COMPANION"
    )
    expected_solution = sum(
        1 for r in part if r.get("has_solution", "").upper() == "YES"
    )
    missing_expected = sum(
        1
        for r in migration_rows
        if r["solution_status"] == "SOLUTION_EXPECTED_BUT_NOT_SAFELY_RECOVERED"
    )
    review_count = sum(
        1
        for r in migration_rows
        if r["atlas_editorial_status"] == "PLACEMENT_REVIEW_REQUIRED"
    )

    source_audit_present = source_figure_audit_path.exists()
    source_visual_note = (
        "Source-backed Part IV visual assets remain staged in `figures/part04/` and are "
        "tracked in `PART_IV_FIGURE_AUDIT.tsv`. They are intentionally not auto-inserted "
        "by this migration pass because raw multi-image groups require caption/placement review."
        if source_audit_present
        else "No `PART_IV_FIGURE_AUDIT.tsv` was present at migration time."
    )

    summary = [
        "# Companion Part IV migration — Volume IV problem corpus",
        "",
        "This pass materializes the Volume IV semantic atlas rows as reader-facing Companion problems.",
        "Source provenance, classification confidence, and alternate solution variants remain in the migration ledger rather than the mathematical prose.",
        "",
        "## Coverage",
        "",
        f"- Part IV atlas units: **{len(part)}**",
        f"- Reader-facing problems migrated: **{rendered}**",
        f"- Editorial holds with no safely recoverable statement: **{holds}**",
        f"- Problems with a migrated primary solution: **{with_solution}**",
        f"- Atlas rows marked as having a reconciled solution: **{expected_solution}**",
        f"- Expected solutions not safely recovered in this pass: **{missing_expected}**",
        f"- Problems with multiple distinct solution variants retained in provenance: **{multi_solution}**",
        f"- Atlas placement-review rows included in Part IV: **{review_count}**",
        "",
        "## Reader-facing thematic sections",
        "",
    ]
    for theme, related in THEME_ORDER:
        summary.append(
            f"- {theme} ({related}): **{by_theme_counts.get(theme, 0)}** problems"
        )

    summary += [
        "",
        "## Visual layer",
        "",
        f"- Designed Part IV TikZ figures placed automatically: **{designed_placed}**",
        f"- Designed manifest rows missing a staged file: **{designed_missing}**",
        f"- Designed manifest available: **{'YES' if designed_manifest_path.exists() else 'NO'}**",
        "",
        source_visual_note,
        "",
        "## Integrity rule",
        "",
        "Every Part IV atlas unit has exactly one migration-ledger row and therefore one explicit disposition.",
        "No missing statement or solution is fabricated.",
        "",
    ]
    summary_path.write_text("\n".join(summary), encoding="utf-8")

    print("COMPANION PART IV MIGRATION BUILT")
    print(f"  atlas units: {len(part)}")
    print(f"  migrated problems: {rendered}")
    print(f"  editorial holds: {holds}")
    print(f"  migrated solutions: {with_solution}")
    print(f"  expected solutions not recovered: {missing_expected}")
    print(f"  multiple solution variants: {multi_solution}")
    print(f"  designed figures placed: {designed_placed}")
    print(f"  designed figure files missing: {designed_missing}")
    for theme, _ in THEME_ORDER:
        print(f"  {theme}: {by_theme_counts.get(theme, 0)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
