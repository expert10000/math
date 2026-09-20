#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

VOLUME = "II"
PART = "02"

THEME_ORDER = [
    ("Metric and Topological Foundations", "II/01--II/07"),
    ("Calculus", "II/08--II/10"),
    ("Sequences of Functions", "II/11--II/15"),
    ("Fixed Points and Differential Equations", "II/16--II/19"),
    ("Approximation", "II/20--II/25"),
]

MIGRATION_FIELDS = [
    "companion_problem_id","semantic_unit_id","representative_problem_id","thematic_section",
    "related_chapters","atlas_editorial_status","source_problem_ids","statement_source_file",
    "statement_line_range","statement_status","solution_status","primary_solution_id",
    "primary_solution_source_file","primary_solution_line_range","distinct_solution_variants",
    "alternate_solution_ids","figure_requirement","figure_status","migration_status","notes"
]

PROBLEM_ENVS = "problem|exercise|example|question|task|challenge"
SOLUTION_ENVS = "solution|answer|proofsolution"
HINT_ENVS = "hint|hints"

def read_tsv(path: Path) -> tuple[list[str], list[dict[str,str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        return list(r.fieldnames or []), [dict(x) for x in r]

def write_tsv(path: Path, fields: list[str], rows: Iterable[dict[str,object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})

def safe_read(path: Path) -> str:
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")

def parse_range(value: str) -> tuple[int,int] | None:
    m = re.fullmatch(r"L?(\d+)-L?(\d+)", (value or "").strip())
    if not m:
        return None
    a,b = int(m.group(1)), int(m.group(2))
    return (a,b) if a <= b else (b,a)

def extract_range(source_root: Path, rel: str, line_range: str) -> str:
    rr = parse_range(line_range)
    if not rel or not rr:
        return ""
    p = source_root / Path(rel)
    if not p.exists():
        return ""
    lines = safe_read(p).splitlines()
    a,b = rr
    if a < 1 or a > len(lines):
        return ""
    b = min(b, len(lines))
    return "\n".join(lines[a-1:b])

def strip_comments(text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in text.splitlines())

def strip_balanced_environment(text: str, env_pattern: str) -> str:
    # Imported files use ordinary non-nested solution/hint wrappers in the problem spans.
    return re.sub(
        rf"\\begin\{{(?:{env_pattern})\*?\}}(?:\[[^\]]*\])?.*?\\end\{{(?:{env_pattern})\*?\}}",
        "\n",
        text,
        flags=re.I | re.S,
    )

def extract_problem_heading_content(text: str) -> tuple[str,str]:
    # Recover a mathematical statement embedded directly in a heading such as:
    # \section{Problem 4: Prove that ...}
    pat = re.compile(
        r"\\(?:chapter|section|subsection|subsubsection|paragraph)\*?\s*\{"
        r"\s*(?:Problem|Exercise|Example|Question|Task|Challenge)"
        r"(?:\s+[A-Za-z0-9][A-Za-z0-9.()_/\-]*)?\s*(?:[:.\-]\s*)?"
        r"(?P<body>[^{}]*)\}",
        re.I,
    )
    m = pat.search(text)
    if not m:
        return text, ""
    body = (m.group("body") or "").strip()
    text = text[:m.start()] + "\n" + text[m.end():]
    return text, body

def strip_presentation_commands(text: str) -> str:
    text = re.sub(r"\\documentclass(?:\[[^\]]*\])?\{[^}]*\}", " ", text, flags=re.I)
    text = re.sub(r"\\usepackage(?:\[[^\]]*\])?\{[^}]*\}", " ", text, flags=re.I)
    text = re.sub(r"\\(?:begin|end)\{document\}", " ", text, flags=re.I)
    text = re.sub(r"\\label\{[^}]+\}", " ", text)
    text = re.sub(r"\\(?:chapter|section|subsection|subsubsection|paragraph)\*?\{[^{}]*\}", " ", text)
    text = re.sub(rf"\\begin\{{(?:{PROBLEM_ENVS})\*?\}}(?:\[[^\]]*\])?", " ", text, flags=re.I)
    text = re.sub(rf"\\end\{{(?:{PROBLEM_ENVS})\*?\}}", " ", text, flags=re.I)
    text = re.sub(
        r"(?im)^\s*(?:\\textbf\{)?(?:Problem|Exercise|Example|Question|Task|Challenge)"
        r"(?:\s+[A-Za-z0-9][A-Za-z0-9.()_/\-]*)?\}?\s*[:.]\s*",
        "",
        text,
    )
    return text

def strip_figure_code(text: str) -> str:
    text = re.sub(r"\\begin\{figure\*?\}.*?\\end\{figure\*?\}", "\n", text, flags=re.I | re.S)
    text = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", "\n", text, flags=re.I | re.S)
    text = re.sub(r"\\includegraphics(?:\[[^\]]*\])?\{[^}]+\}", " ", text, flags=re.I)
    text = re.sub(r"\\includesvg(?:\[[^\]]*\])?\{[^}]+\}", " ", text, flags=re.I)
    return text

def tidy(text: str) -> str:
    lines = [x.rstrip() for x in text.splitlines()]
    out = []
    blank = False
    for line in lines:
        if not line.strip():
            if not blank and out:
                out.append("")
            blank = True
        else:
            out.append(line)
            blank = False
    return "\n".join(out).strip()

def strip_standalone_group_braces(text: str) -> str:
    """Remove legacy presentation-group lines containing only ``{`` or ``}``.

    The imported corpus contains formatting constructs that open/close TeX groups
    on separate lines around reader-facing content. Once the corresponding style
    command is stripped, those braces become syntactically dangerous residue.
    Removing *only* lines that consist of a bare grouping brace is conservative:
    braces inside mathematical expressions and command arguments are untouched.
    """
    kept = [
        line
        for line in (text or "").splitlines()
        if not re.fullmatch(r"\s*[{}]\s*", line)
    ]
    return tidy("\n".join(kept))


def normalize_legacy_lists(text: str) -> str:
    r"""Flatten imported legacy lists into reader-facing paragraphs.

    Reconciled source spans frequently begin or end in the middle of
    ``itemize``, ``enumerate``, or ``description`` environments. Preserving
    those environments therefore requires reconstructing presentation context
    that is outside the mathematical statement.

    For the Companion migration we instead preserve the *content*:
      * every list begin/end wrapper is removed;
      * ``\item[label]`` becomes a labeled paragraph;
      * unlabeled ``\item`` becomes a bullet paragraph;
      * nested list wrappers are flattened the same way.

    This is intentionally presentation-only normalization. Mathematical TeX
    inside item bodies is left untouched.
    """
    s = text or ""

    # Remove list wrappers anywhere on a line, including common optional args.
    s = re.sub(
        r"\\begin\{(?:itemize|enumerate|description)\*?\}(?:\[[^\]]*\])?",
        " ",
        s,
        flags=re.I,
    )
    s = re.sub(
        r"\\end\{(?:itemize|enumerate|description)\*?\}",
        " ",
        s,
        flags=re.I,
    )

    out: list[str] = []
    for line in s.splitlines():
        # Whole-line item with an optional explicit label.
        m = re.match(
            r"^(?P<indent>\s*)\\item(?:\[(?P<label>[^\]]+)\])?\s*(?P<body>.*)$",
            line,
        )
        if m:
            indent = m.group("indent")
            label = (m.group("label") or "").strip()
            body = m.group("body").strip()
            if label:
                out.append(f"{indent}\\par\\noindent {label}\\quad {body}".rstrip())
            else:
                out.append(
                    f"{indent}\\par\\noindent\\textbullet\\quad {body}".rstrip()
                )
            continue

        # Defensive handling for an item token embedded after other stripped
        # presentation syntax on the same line.
        line = re.sub(
            r"\\item\[([^\]]+)\]\s*",
            lambda m: r"\par\noindent " + m.group(1).strip() + r"\quad ",
            line,
        )
        line = re.sub(
            r"\\item\b\s*",
            r"\\par\\noindent\\textbullet\\quad ",
            line,
        )

        out.append(line)

    return tidy("\n".join(out))

def is_nonsemantic_wrapper_residue(text: str) -> bool:
    """Return True when cleanup leaves only grouping/punctuation residue."""
    s = (text or "").strip()
    if not s:
        return True
    residue = re.sub(r"""[\s{}\[\]().,;:!?~`'"+\-=\/|&%]+""", "", s)
    return residue == ""

def strip_unmatched_closing_braces(text: str) -> str:
    r"""Drop only unescaped ``}`` tokens that would make local brace depth negative.

    This targets legacy presentation-group residue such as::

        } $\boxed{\cos(2\pi/n)}$.

    Balanced braces used by TeX commands and mathematics are preserved. Escaped
    braces ``\{`` and ``\}`` are treated as literal symbols and do not affect
    grouping depth.
    """
    s = text or ""
    out: list[str] = []
    depth = 0
    i = 0

    while i < len(s):
        ch = s[i]

        # Preserve escaped characters verbatim. In particular, \{ and \}
        # are literal delimiters rather than TeX grouping braces.
        if ch == "\\":
            out.append(ch)
            if i + 1 < len(s):
                out.append(s[i + 1])
                i += 2
                continue
            i += 1
            continue

        if ch == "{":
            depth += 1
            out.append(ch)
            i += 1
            continue

        if ch == "}":
            if depth > 0:
                depth -= 1
                out.append(ch)
            # depth == 0 => orphan closer from stripped legacy presentation;
            # drop only this one token.
            i += 1
            continue

        out.append(ch)
        i += 1

    return tidy("".join(out))

def normalize_legacy_operator_macros(text: str) -> str:
    r"""Normalize confirmed legacy macros/control characters not in shared macros.

    Confirmed cases:
    - ``\tr``: legacy matrix-trace shorthand -> ``\operatorname{tr}``;
    - ``\gap``: legacy horizontal-spacing shorthand -> ``\quad``;
    - NUL characters: remove control-byte residue that TeX reports as ``^^@``.
    """
    s = text or ""

    # Control-byte residue is never mathematical content.
    s = s.replace("\x00", "")

    # Semantic operator normalization.
    s = re.sub(r"\\tr\b", r"\\operatorname{tr}", s)

    # Obsolete AMS shorthand; canonical series notation uses \\mathbb.
    s = re.sub(r"\\Bbb\b", r"\\mathbb", s)

    # Legacy spacing shorthand. Preserve the intended visual separation without
    # extending the global series macro contract.
    s = re.sub(r"\\gap\b", r"\\quad", s)

    return s

def clean_statement(raw: str) -> str:
    if not raw:
        return ""
    raw = strip_comments(raw)
    # Remove embedded solutions/hints before stripping outer problem wrappers.
    raw = strip_balanced_environment(raw, SOLUTION_ENVS)
    raw = strip_balanced_environment(raw, HINT_ENVS)
    # Heading-delimited solution/hint material: truncate at the first explicit heading.
    raw = re.split(
        r"\\(?:section|subsection|subsubsection|paragraph)\*?\s*\{\s*(?:Solution|Answer|Hint|Hints)\b",
        raw,
        maxsplit=1,
        flags=re.I,
    )[0]
    raw, heading_body = extract_problem_heading_content(raw)
    raw = strip_presentation_commands(raw)
    raw = strip_figure_code(raw)
    raw = tidy(raw)
    if heading_body:
        heading_body = tidy(strip_figure_code(strip_presentation_commands(heading_body)))
        raw = (heading_body + ("\n\n" + raw if raw else "")).strip()

    # Remove only brace-only presentation-group lines. Mathematical braces inside
    # formulas/commands are preserved.
    raw = strip_standalone_group_braces(raw)
    raw = normalize_legacy_lists(raw)
    raw = normalize_legacy_operator_macros(raw)
    raw = strip_unmatched_closing_braces(raw)

    # Canonical companion output owns proof termination; legacy source
    # QED markers must not survive even when encountered in problem/body text.
    raw = re.sub(r"[ \\t]*\\qedhere\b[ \\t]*", "", raw)
    raw = re.sub(r"[ \\t]*\\qed\b[ \\t]*", "", raw)
    return raw

def clean_solution(raw: str) -> str:
    if not raw:
        return ""
    raw = strip_comments(raw)
    raw = strip_balanced_environment(raw, HINT_ENVS)
    raw = re.sub(rf"\\begin\{{(?:{SOLUTION_ENVS})\*?\}}(?:\[[^\]]*\])?", " ", raw, flags=re.I)
    raw = re.sub(rf"\\end\{{(?:{SOLUTION_ENVS})\*?\}}", " ", raw, flags=re.I)
    # Canonical Companion solutions are already proof-like. Strip imported
    # presentation headings such as \\paragraph{Solution.}.
    raw = re.sub(
        r"\\(?:chapter|section|subsection|subsubsection|paragraph)\*?\s*"
        r"\{\s*(?:Solution|Answer|Proof)\s*[.:;!?-]?\s*\}",
        " ",
        raw,
        flags=re.I,
    )
    raw = re.sub(
        r"(?im)^\s*(?:\\textbf\{\s*)?"
        r"(?:Solution|Answer|Proof)\s*[.:;!?-]?\s*\}?\s*",
        "",
        raw,
    )

    # The canonical proof-like solution environment supplies its own QED mark.
    raw = re.sub(r"[ \\t]*\\qedhere\b[ \\t]*", "", raw)
    raw = re.sub(r"[ \\t]*\\qed\b[ \\t]*", "", raw)
    raw = re.sub(r"\\label\{[^}]+\}", " ", raw)
    raw = strip_figure_code(raw)
    raw = re.sub(r"\\(?:begin|end)\{document\}", " ", raw, flags=re.I)
    cleaned = tidy(raw)

    # Normalize legacy presentation groups instead of discarding an otherwise
    # valid mathematical solution just because it contains a bare brace line.
    cleaned = strip_standalone_group_braces(cleaned)
    cleaned = normalize_legacy_lists(cleaned)
    cleaned = normalize_legacy_operator_macros(cleaned)
    cleaned = strip_unmatched_closing_braces(cleaned)

    # If nothing mathematical remains after normalization, treat the source
    # solution as not safely recoverable.
    if is_nonsemantic_wrapper_residue(cleaned):
        return ""

    return cleaned

def tex_escape_heading(s: str) -> str:
    # Theme strings are controlled, but keep this safe for later reuse.
    return s.replace("&", r"\&").replace("%", r"\%").replace("#", r"\#").replace("_", r"\_")

def choose_primary_solution(
    member_ids: set[str],
    links: list[dict[str,str]],
    source_root: Path,
) -> tuple[dict[str,str] | None, str, list[str], int]:
    candidates = []
    for row in links:
        if row.get("solution_kind","").upper() != "SOLUTION":
            continue
        if row.get("linked_problem_id","") not in member_ids:
            continue
        raw = extract_range(source_root, row.get("solution_source_file",""), row.get("solution_line_range",""))
        cleaned = clean_solution(raw)
        if not cleaned:
            continue
        h = row.get("solution_text_hash","") or ("TEXT:" + re.sub(r"\s+"," ",cleaned).strip())
        candidates.append((row, cleaned, h))

    if not candidates:
        return None, "", [], 0

    by_hash: dict[str,list[tuple[dict[str,str],str,str]]] = defaultdict(list)
    for x in candidates:
        by_hash[x[2]].append(x)

    # Prefer a resolved/high-confidence row and then a shorter source path as a stable tie-break.
    rank = {"HIGH":3,"MEDIUM":2,"REVIEW":1,"":0}
    unique = []
    for h, group in by_hash.items():
        group.sort(
            key=lambda x: (
                rank.get(x[0].get("reconciliation_confidence","").upper(),0),
                "RESOLVED" in x[0].get("reconciliation_status","").upper(),
                -len(x[0].get("solution_source_file","")),
                x[0].get("solution_id",""),
            ),
            reverse=True,
        )
        unique.append(group[0])
    unique.sort(
        key=lambda x: (
            rank.get(x[0].get("reconciliation_confidence","").upper(),0),
            "RESOLVED" in x[0].get("reconciliation_status","").upper(),
            -len(x[1]),
            x[0].get("solution_id",""),
        ),
        reverse=True,
    )
    primary = unique[0]
    alternate_ids = [x[0].get("solution_id","") for x in unique[1:]]
    return primary[0], primary[1], alternate_ids, len(unique)

def main() -> int:
    ap = argparse.ArgumentParser(description="Migrate Companion Part II problem corpus.")
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    args = ap.parse_args()
    repo = args.repo.resolve()

    inv = repo/"imports"/"problem_inventory"
    base = repo/"books"/"companion_problems_solutions"
    source_root = repo/"imports"/"ALL_TEX_AND_FIGURES"/"tex"

    atlas_path = base/"metadata"/"COMPANION_PROBLEM_ATLAS.tsv"
    ledger_path = inv/"PROBLEM_LEDGER.tsv"
    links_path = inv/"PROBLEM_SOLUTION_LINKS.tsv"
    chapter_path = base/"chapters"/"part02_volume_ii"/"chapter.tex"
    migration_path = base/"metadata"/"PART_II_MIGRATION.tsv"
    summary_path = base/"metadata"/"PART_II_MIGRATION_SUMMARY.md"

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

    part = [r for r in atlas if r.get("related_volume","") == VOLUME]
    if not part:
        print("ERROR: no Volume II rows in Companion atlas")
        return 2

    ledger_by_id = {r.get("problem_id",""):r for r in ledger}
    links_list = list(links)

    by_theme: dict[str,list[dict]] = defaultdict(list)
    migration_rows = []
    rendered = 0
    with_solution = 0
    holds = 0
    multi_solution = 0

    for ar in sorted(part, key=lambda r: r.get("companion_problem_id","")):
        cp = ar.get("companion_problem_id","")
        sid = ar.get("semantic_unit_id","")
        rep = ar.get("representative_problem_id","")
        lr = ledger_by_id.get(rep, {})
        source_file = lr.get("source_file","")
        source_range = lr.get("source_line_range","")
        raw_statement = extract_range(source_root, source_file, source_range)
        statement = clean_statement(raw_statement)

        member_ids = {x for x in ar.get("source_problem_ids","").split(";") if x}
        if rep:
            member_ids.add(rep)

        primary_row, solution, alternate_ids, distinct_variants = choose_primary_solution(member_ids, links_list, source_root)
        if distinct_variants > 1:
            multi_solution += 1

        theme = ar.get("thematic_section","") or "Metric and Topological Foundations"
        related = ar.get("related_chapters","") or dict(THEME_ORDER).get(theme,"II/01--II/25")

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
            by_theme[theme].append({
                "cp":cp,
                "statement":statement,
                "solution":solution,
                "related":related,
                "atlas_editorial_status":ar.get("editorial_status",""),
            })

        if solution:
            sol_status = "MIGRATED_PRIMARY_SOLUTION"
            if distinct_variants > 1:
                sol_status = "MIGRATED_PRIMARY_SOLUTION;ALTERNATE_VARIANTS_RETAINED_IN_PROVENANCE"
        elif ar.get("has_solution","").upper() == "YES":
            sol_status = "SOLUTION_EXPECTED_BUT_NOT_SAFELY_RECOVERED"
        else:
            sol_status = "NO_RECONCILED_SOLUTION"

        migration_rows.append({
            "companion_problem_id":cp,
            "semantic_unit_id":sid,
            "representative_problem_id":rep,
            "thematic_section":theme,
            "related_chapters":related,
            "atlas_editorial_status":ar.get("editorial_status",""),
            "source_problem_ids":ar.get("source_problem_ids",""),
            "statement_source_file":source_file,
            "statement_line_range":source_range,
            "statement_status":statement_status,
            "solution_status":sol_status,
            "primary_solution_id":primary_row.get("solution_id","") if primary_row else "",
            "primary_solution_source_file":primary_row.get("solution_source_file","") if primary_row else "",
            "primary_solution_line_range":primary_row.get("solution_line_range","") if primary_row else "",
            "distinct_solution_variants":distinct_variants,
            "alternate_solution_ids":";".join(alternate_ids),
            "figure_requirement":ar.get("figure_requirement",""),
            "figure_status":ar.get("figure_status",""),
            "migration_status":migration_status,
            "notes":"Reader-facing provenance suppressed; exact source lineage retained here.",
        })

    # Reader-facing chapter.
    out = [
        r"\chapter{Problems Related to Volume II}",
        r"\label{ch:companion-ii}",
        "",
        r"\paragraph{Main-text correspondence.}",
        r"This Part accompanies \emph{Volume II: Real Analysis and Topological Foundations}. Problems are grouped by",
        r"mathematical theme rather than by reproducing the chapter sequence of the main text.",
        r"Each section gives the corresponding main-text chapter range for further reading.",
        "",
    ]

    theme_ranges = dict(THEME_ORDER)
    known_themes = {x[0] for x in THEME_ORDER}
    ordered_themes = [x[0] for x in THEME_ORDER] + sorted(k for k in by_theme if k not in known_themes)

    for theme in ordered_themes:
        items = by_theme.get(theme, [])
        if not items:
            continue
        related = theme_ranges.get(theme) or items[0]["related"]
        out += [
            rf"\section{{{tex_escape_heading(theme)}}}",
            "",
            rf"\paragraph{{Related material.}} Volume II, Chapters \texttt{{{related}}}.",
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
            r"preserved in the Part I migration ledger and are not silently replaced or reconstructed.",
            "",
        ]

    chapter_path.write_text("\n".join(out).rstrip()+"\n", encoding="utf-8")
    write_tsv(migration_path, MIGRATION_FIELDS, migration_rows)

    by_theme_counts = Counter(r["thematic_section"] for r in migration_rows if r["migration_status"]=="MIGRATED_TO_COMPANION")
    review_count = sum(1 for r in migration_rows if r["atlas_editorial_status"]=="PLACEMENT_REVIEW_REQUIRED")
    expected_solution = sum(1 for r in part if r.get("has_solution","").upper()=="YES")
    missing_expected = sum(1 for r in migration_rows if r["solution_status"]=="SOLUTION_EXPECTED_BUT_NOT_SAFELY_RECOVERED")

    summary = [
        "# Companion Part II migration — Volume II problem corpus",
        "",
        "This pass materializes the Volume II semantic atlas rows as reader-facing Companion problems.",
        "Source provenance, classification confidence, and alternate solution variants remain in the migration ledger rather than the mathematical prose.",
        "",
        "## Coverage",
        "",
        f"- Part II atlas units: **{len(part)}**",
        f"- Reader-facing problems migrated: **{rendered}**",
        f"- Editorial holds with no safely recoverable statement: **{holds}**",
        f"- Problems with a migrated primary solution: **{with_solution}**",
        f"- Atlas rows marked as having a reconciled solution: **{expected_solution}**",
        f"- Expected solutions not safely recovered in this pass: **{missing_expected}**",
        f"- Problems with multiple distinct solution variants retained in provenance: **{multi_solution}**",
        f"- Atlas placement-review rows included in Part II: **{review_count}**",
        "",
        "## Reader-facing thematic sections",
        "",
    ]
    for theme, related in THEME_ORDER:
        summary.append(f"- {theme} ({related}): **{by_theme_counts.get(theme,0)}** problems")
    summary += [
        "",
        "## Visual layer",
        "",
        "No new plots or diagrams are introduced in this migration commit.",
        "Existing/source visual requirements remain recorded in `COMPANION_PROBLEM_ATLAS.tsv` and `PART_II_MIGRATION.tsv` for the later visual-enrichment pass.",
        "",
        "## Integrity rule",
        "",
        "Every Part I atlas unit has exactly one migration-ledger row and therefore one explicit disposition.",
        "No missing statement or solution is fabricated.",
        "",
    ]
    summary_path.write_text("\n".join(summary), encoding="utf-8")

    print("COMPANION PART II MIGRATION BUILT")
    print(f"  atlas units: {len(part)}")
    print(f"  migrated problems: {rendered}")
    print(f"  editorial holds: {holds}")
    print(f"  migrated solutions: {with_solution}")
    print(f"  expected solutions not recovered: {missing_expected}")
    print(f"  multiple solution variants: {multi_solution}")
    for theme, _ in THEME_ORDER:
        print(f"  {theme}: {by_theme_counts.get(theme,0)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
