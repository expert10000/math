#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import re
from collections import Counter
from pathlib import Path

THEME_ORDER = [
    "Measure and Integration",
    "Fourier Analysis",
    "Distribution Theory",
    "Sobolev and PDE Methods",
]

THEME_CORRESPONDENCE = {
    "Measure and Integration": "III/01--III/08",
    "Fourier Analysis": "III/09--III/14",
    "Distribution Theory": "III/15--III/19",
    "Sobolev and PDE Methods": "III/20--III/28",
}

EXPECTED_IDS = [f"CP-III-{i:04d}" for i in range(1, 26)]


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def replace_braced_command(text: str, command: str, prefix: str, suffix: str) -> str:
    for starred in (True, False):
        token = "\\" + command + ("*" if starred else "") + "{"
        out = []
        pos = 0
        while True:
            start = text.find(token, pos)
            if start < 0:
                out.append(text[pos:])
                break
            out.append(text[pos:start])
            i = start + len(token)
            depth = 1
            while i < len(text) and depth:
                ch = text[i]
                escaped = i > 0 and text[i - 1] == "\\"
                if ch == "{" and not escaped:
                    depth += 1
                elif ch == "}" and not escaped:
                    depth -= 1
                i += 1
            if depth:
                out.append(text[start:])
                break
            body = text[start + len(token):i - 1]
            out.append(prefix + body + suffix)
            pos = i
        text = "".join(out)
    return text


def normalize_probheaders(text: str) -> str:
    token = r"\probheader{"
    out = []
    pos = 0
    while True:
        start = text.find(token, pos)
        if start < 0:
            out.append(text[pos:])
            break
        out.append(text[pos:start])
        i = start + len(token)
        depth = 1
        while i < len(text) and depth:
            ch = text[i]
            escaped = i > 0 and text[i - 1] == "\\"
            if ch == "{" and not escaped:
                depth += 1
            elif ch == "}" and not escaped:
                depth -= 1
            i += 1
        if depth:
            out.append(text[start:])
            break
        body = text[start + len(token):i - 1]
        out.append(r"\par\medskip\noindent\textbf{" + body + r"}\quad")
        pos = i
    return "".join(out)


def extract_source_figures(text: str) -> tuple[str, list[str], int]:
    labels = []
    count = 0
    pattern = re.compile(r"\\begin\{figure\*?\}.*?\\end\{figure\*?\}", re.S)

    def repl(match):
        nonlocal count
        count += 1
        block = match.group(0)
        labels.extend(re.findall(r"\\label\{(fig:[^}]+)\}", block))
        return "\n"

    return pattern.sub(repl, text), sorted(set(labels)), count


def strip_outer_environment(text: str, env: str) -> str:
    pat = re.compile(
        rf"^\s*\\begin\{{{re.escape(env)}\}}(?:\[[^\]]*\])?\s*(.*?)\s*"
        rf"\\end\{{{re.escape(env)}\}}\s*$",
        re.S,
    )
    m = pat.match(text)
    return m.group(1) if m else text


def remove_initial_solution_heading(text: str) -> str:
    # Remove only an initial wrapper heading; internal pedagogical headings remain,
    # but will be normalized by clean_body().
    patterns = [
        r"^\s*\\paragraph\*?\{\s*Solution(?:[^{}]*)\}\s*",
        r"^\s*\\subparagraph\*?\{\s*Solution(?:[^{}]*)\}\s*",
        r"^\s*\\subsection\*?\{\s*Solution(?:[^{}]*)\}\s*",
        r"^\s*\\section\*?\{\s*Solution(?:[^{}]*)\}\s*",
        r"^\s*\\subsection\*?\{[^{}]*Theory and Solutions[^{}]*\}\s*",
        r"^\s*Solution(?:\s*\([^)]*\)|\s+to\s+\([^)]*\))?\s*[.:]\s*",
    ]
    for pat in patterns:
        new, n = re.subn(pat, "", text, count=1, flags=re.I | re.S)
        if n:
            return new
    return text


def clean_body(text: str) -> str:
    text = text.replace("\ufeff", "")
    text = re.sub(r"[ \t]*\\qedhere\b[ \t]*", "", text)
    text = re.sub(r"[ \t]*\\qed\b[ \t]*", "", text)
    text = re.sub(r"(?m)^[ \t]*\\sep[ \t]*$", "", text)
    text = re.sub(r"(?m)^[ \t]*\\tighthrule[ \t]*$", "", text)
    text = text.replace(r"\begin{spacy}", "").replace(r"\end{spacy}", "")
    text = re.sub(
        r"\\begin\{statement\}",
        r"\\par\\medskip\\noindent\\textbf{Statement.}\\ ",
        text,
    )
    text = re.sub(r"\\end\{statement\}", r"\\par", text)
    text = normalize_probheaders(text)

    # Canonical problem/solution bodies should not contain sectioning commands.
    for command, spacing in (
        ("section", r"\par\medskip\noindent\textbf{"),
        ("subsection", r"\par\medskip\noindent\textbf{"),
        ("subsubsection", r"\par\smallskip\noindent\textbf{"),
        ("paragraph", r"\par\smallskip\noindent\textbf{"),
        ("subparagraph", r"\par\smallskip\noindent\textbf{"),
    ):
        text = replace_braced_command(text, command, spacing, r"}\quad")

    # Only a bullet at the very start is a migration wrapper artifact.
    text = re.sub(
        r"^\s*(?:\\par\s*)?(?:\\noindent\s*)?\\textbullet(?:\s*\\quad)?\s*",
        "",
        text,
        count=1,
    )
    text = re.sub(r"^\s*\(\*\)\s*", "", text, count=1)
    text = re.sub(r"^\s*\\(?:bigskip|medskip|smallskip)\s*", "", text)
    text = re.sub(r"\s*\\(?:bigskip|medskip|smallskip)\s*$", "", text)

    lines = [line.rstrip() for line in text.splitlines()]
    out = []
    blanks = 0
    for line in lines:
        if not line.strip():
            blanks += 1
            if blanks <= 2:
                out.append("")
        else:
            blanks = 0
            out.append(line)
    return "\n".join(out).strip()


def remove_source_heading(text: str) -> str:
    lines = text.splitlines()
    if not lines:
        return text
    patterns = [
        r"^\s*\\(?:sub)*section\*?\{(?:Problem|Exercise)[^}]*\}\s*$",
        r"^\s*\\(?:sub)*paragraph\*?\{(?:Problem|Exercise)[^}]*\}\s*$",
        r"^\s*\\textbf\{(?:Problem|Exercise)[^}]*\}\s*$",
        r"^\s*(?:Problem|Exercise)\s+\d+(?:\.\d+)*\s*(?:[-—:][^\n]*)?\s*$",
    ]
    if any(re.match(p, lines[0], re.I) for p in patterns):
        return "\n".join(lines[1:]).lstrip()
    return text


def read_range(path: Path, start: int, end: int) -> str:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if start < 1 or end < start or end > len(lines):
        raise RuntimeError(
            f"Invalid range {path}: L{start}-L{end}; source has {len(lines)} lines"
        )
    return "\n".join(lines[start - 1:end]) + "\n"


def header_text() -> str:
    return (
        "\\chapter{Problems Related to Volume III}\n"
        "\\label{ch:companion-iii}\n\n"
        "\\paragraph{Main-text correspondence.}\n"
        "This Part accompanies \\emph{Volume III: Measure, Fourier Analysis, "
        "Distributions and PDE}, whose canonical chapter range is "
        "\\texttt{III/01--III/28}. Problems are grouped by mathematical theme "
        "while retaining stable Companion IDs and source provenance.\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--preview", type=Path)
    args = ap.parse_args()

    repo = args.repo.resolve()
    ledger_path = (
        repo / "books" / "companion_problems_solutions" / "metadata"
        / "PART_III_MIGRATION.tsv"
    )
    chapter_path = (
        repo / "books" / "companion_problems_solutions" / "chapters"
        / "part03_volume_iii" / "chapter.tex"
    )
    summary_path = (
        repo / "books" / "companion_problems_solutions" / "metadata"
        / "PART_III_MIGRATION_SUMMARY.md"
    )
    preview_path = args.preview or (
        repo / "reports" / "companion" / "PART_III_GENERATED_PREVIEW_V2.tex"
    )

    with ledger_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows = list(reader)
        fields = list(reader.fieldnames or [])

    rows.sort(key=lambda r: r["companion_problem_id"])
    if [r["companion_problem_id"] for r in rows] != EXPECTED_IDS:
        raise SystemExit("Ledger must contain exactly CP-III-0001..CP-III-0025")

    non_exact = [
        r["companion_problem_id"]
        for r in rows
        if r.get("resolution_status") != "RESOLVED_EXACT_RANGE"
    ]
    if non_exact:
        raise SystemExit("Non-exact rows remain: " + ", ".join(non_exact))

    explicit_solution_rows = [
        r for r in rows if (r.get("has_solution") or "").upper() == "YES"
    ]
    unresolved_solution_ranges = [
        r["companion_problem_id"]
        for r in explicit_solution_rows
        if r.get("solution_resolution_status") != "RESOLVED_EXACT_SOLUTION_RANGE"
    ]
    if unresolved_solution_ranges:
        raise SystemExit(
            "Expected solution rows lack explicit solution ranges: "
            + ", ".join(unresolved_solution_ranges)
        )

    extra_fields = [
        "source_excerpt_sha256",
        "generated_problem_sha256",
        "solution_recovery_status",
        "source_figure_count",
        "source_figure_labels",
        "generated_status",
    ]
    for field in extra_fields:
        if field not in fields:
            fields.append(field)

    by_theme = {theme: [] for theme in THEME_ORDER}
    solution_count = 0
    review_rows = []
    figure_units = []

    for row in rows:
        pid = row["companion_problem_id"]
        source = Path(row["resolved_source_file"])
        expect_solution = (row.get("has_solution") or "").upper() == "YES"

        if expect_solution:
            statement_start = int(row["resolved_statement_start_line"])
            statement_end = int(row["resolved_statement_end_line"])
            solution_start = int(row["resolved_solution_start_line"])
            solution_end = int(row["resolved_solution_end_line"])

            raw_statement = read_range(source, statement_start, statement_end)
            raw_solution = read_range(source, solution_start, solution_end)
            raw_for_hash = raw_statement + "\n<<<SOLUTION>>>\n" + raw_solution
            row["solution_recovery_status"] = "EXPLICIT_RESOLVED_RANGE"
        else:
            statement_start = int(row["resolved_start_line"])
            statement_end = int(row["resolved_end_line"])
            raw_statement = read_range(source, statement_start, statement_end)
            raw_solution = None
            raw_for_hash = raw_statement
            row["solution_recovery_status"] = "NOT_EXPECTED"

        row["source_excerpt_sha256"] = sha256_text(raw_for_hash)

        statement_no_figs, statement_fig_labels, statement_fig_count = extract_source_figures(raw_statement)
        solution_no_figs = None
        solution_fig_labels = []
        solution_fig_count = 0
        if raw_solution is not None:
            solution_no_figs, solution_fig_labels, solution_fig_count = extract_source_figures(raw_solution)

        figure_labels = sorted(set(statement_fig_labels + solution_fig_labels))
        figure_count = statement_fig_count + solution_fig_count
        row["source_figure_count"] = str(figure_count)
        row["source_figure_labels"] = ";".join(figure_labels)

        if figure_count or (row.get("figure_requirement") or "").upper() == "YES":
            figure_units.append(pid)

        statement = clean_body(
            remove_source_heading(
                strip_outer_environment(statement_no_figs, "problem")
            )
        )

        solution = None
        if solution_no_figs is not None:
            solution = remove_initial_solution_heading(solution_no_figs)
            solution = clean_body(strip_outer_environment(solution, "solution"))

        if not statement:
            row["generated_status"] = "REVIEW_REQUIRED_EMPTY_PROBLEM"
            review_rows.append(pid)
        elif expect_solution and not solution:
            row["generated_status"] = "REVIEW_REQUIRED_SOLUTION"
            review_rows.append(pid)
        else:
            row["generated_status"] = "MIGRATED"

        block = [
            f"\\begin{{problem}}[{pid}]",
            f"\\label{{prob:{pid.lower()}}}",
            statement,
            "\\end{problem}",
        ]

        if solution:
            block += ["", "\\begin{solution}", solution, "\\end{solution}"]
            solution_count += 1

        rendered = "\n".join(block).strip() + "\n"
        row["generated_problem_sha256"] = sha256_text(rendered)
        by_theme.setdefault(row["thematic_section"], []).append(rendered)

    parts = [header_text().rstrip(), ""]
    for theme in THEME_ORDER:
        blocks = by_theme.get(theme, [])
        if not blocks:
            continue
        parts += [
            f"\\section{{{theme}}}",
            f"\\noindent\\textit{{Main-text correspondence: {THEME_CORRESPONDENCE[theme]}.}}",
            "",
            "\n".join(blocks).rstrip(),
            "",
        ]

    for theme in sorted(set(by_theme) - set(THEME_ORDER)):
        blocks = by_theme[theme]
        if blocks:
            parts += [f"\\section{{{theme}}}", "", "\n".join(blocks).rstrip(), ""]

    chapter_text = "\n".join(parts).rstrip() + "\n"

    preview_path.parent.mkdir(parents=True, exist_ok=True)
    preview_path.write_text(chapter_text, encoding="utf-8", newline="\n")

    status_counts = Counter(r["generated_status"] for r in rows)
    theme_counts = Counter(r["thematic_section"] for r in rows)
    source_figure_blocks = sum(int(r["source_figure_count"] or 0) for r in rows)

    summary = [
        "# Part III Companion Migration Summary",
        "",
        f"- Canonical units: **{len(rows)}**",
        f"- Recovered solutions: **{solution_count}**",
        f"- Review-required units: **{len(review_rows)}**",
        f"- Source figure blocks detected: **{source_figure_blocks}**",
        f"- Figure-relevant units: **{len(figure_units)}**",
        "",
        "## Generation status",
        "",
    ]
    for key, value in sorted(status_counts.items()):
        summary.append(f"- **{key}: {value}**")
    summary += ["", "## Themes", ""]
    for theme in THEME_ORDER:
        summary.append(f"- **{theme}: {theme_counts.get(theme, 0)}**")
    summary += ["", "## Review-required units", ""]
    summary += [f"- `{x}`" for x in review_rows] if review_rows else ["- none"]
    summary += ["", "## Figure-relevant units", ""]
    summary += [f"- `{x}`" for x in figure_units] if figure_units else ["- none"]

    if args.apply:
        chapter_path.parent.mkdir(parents=True, exist_ok=True)
        chapter_path.write_text(chapter_text, encoding="utf-8", newline="\n")
        with ledger_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=fields,
                delimiter="\t",
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerows(rows)
        summary_path.write_text("\n".join(summary) + "\n", encoding="utf-8")

    print("COMPANION PART III MIGRATION V2")
    print("===============================")
    print("mode:", "APPLY" if args.apply else "PREVIEW")
    print("canonical units:", len(rows))
    print("recovered solutions:", solution_count)
    print("review-required:", len(review_rows))
    print("source figure blocks:", source_figure_blocks)
    print("figure-relevant units:", len(figure_units))
    for key, value in sorted(status_counts.items()):
        print(f"{key}: {value}")
    print("preview:", preview_path)
    if args.apply:
        print("chapter:", chapter_path)
        print("summary:", summary_path)

    if args.apply and review_rows:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
