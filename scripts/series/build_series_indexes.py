#!/usr/bin/env python3
"""Build the reproducible series indexes from canonical sources.

The chapter ledger is the authority for chapter identity.  The source TeX is
the authority for named mathematical statements.  This deliberately avoids a
second hand-maintained list of chapters, theorem names, or cross-volume links.
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path


STATEMENT_RX = re.compile(
    r"\\begin\{(theorem|proposition|lemma|corollary|definition)\}"
    r"(?:\[([^\]]+)\])?\s*(?:\\label\{([^}]+)\})?",
    re.MULTILINE,
)
REFERENCE_RX = re.compile(
    r"\b(?:in|see)\s+(?:the\s+)?(previous|next|later)\s+chapter\b"
    r"|\b(as shown above|as discussed previously)\b",
    re.IGNORECASE,
)

SUBJECTS = {
    "Linear algebra": ("linear", "matrix", "vector", "eigen", "determinant", "spectral", "quadratic"),
    "Analysis and PDE": ("metric", "compact", "measure", "fourier", "distribution", "pde", "sobolev", "integral", "approximation"),
    "Complex analysis": ("holomorphic", "cauchy", "residue", "riemann surface", "elliptic", "mobius", "covering"),
    "Commutative algebra": ("ring", "ideal", "module", "localization", "homological", "tor", "ext", "derived"),
    "Algebraic geometry": ("scheme", "morphism", "sheaf", "projective", "divisor", "blow", "variety", "cohomology"),
    "Differential geometry": ("manifold", "curvature", "geodesic", "riemannian", "hyperbolic", "mesh", "laplacian", "bundle"),
    "Algebraic topology": ("homotopy", "homology", "cohomology", "topolog", "fundamental group", "fibration", "duality"),
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def tsv(rows: list[dict[str, str]], fields: list[str]) -> str:
    from io import StringIO
    output = StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def escaped(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().replace("|", "\\|")


def notation_macros(text: str) -> list[tuple[str, str, str]]:
    """Read one-line providecommand definitions, including nested TeX braces."""
    macros = []
    for line in text.splitlines():
        match = re.match(r"\s*\\providecommand\{\\([A-Za-z]+)\}(.*)$", line)
        if not match:
            continue
        command, tail = match.groups()
        tail = tail.strip()
        arity = "0"
        if tail.startswith("["):
            arity, _, tail = tail[1:].partition("]")
            tail = tail.strip()
        if not tail.startswith("{"):
            continue
        depth = 0
        for index, character in enumerate(tail):
            if character == "{":
                depth += 1
            elif character == "}":
                depth -= 1
                if depth == 0:
                    macros.append((command, arity, tail[1:index]))
                    break
    return macros


def relative(repo: Path, path: Path) -> str:
    return path.relative_to(repo).as_posix()


def statement_rows(repo: Path, chapters: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[str]]:
    rows, failures = [], []
    labels: dict[str, str] = {}
    for chapter in chapters:
        source = repo / chapter["canonical_path"]
        if not source.exists():
            failures.append(f"MISSING_CHAPTER_SOURCE:{chapter['chapter_code']}")
            continue
        source_text = source.read_text(encoding="utf-8-sig", errors="replace")
        for match in STATEMENT_RX.finditer(source_text):
            kind, name, label = match.groups()
            if not name:
                continue  # Anonymous statements do not belong in a name index.
            if label and label in labels:
                failures.append(f"DUPLICATE_STATEMENT_LABEL:{label}:{labels[label]}:{chapter['chapter_code']}")
            elif label:
                labels[label] = chapter["chapter_code"]
            rows.append({
                "name": escaped(name), "kind": kind, "volume": chapter["volume"],
                "chapter_code": chapter["chapter_code"], "chapter_title": chapter["chapter_title"],
                "label": label or "UNLABELLED", "source_path": chapter["canonical_path"],
            })
    return sorted(rows, key=lambda row: (row["name"].casefold(), row["chapter_code"], row["kind"])), failures


def audit_directional_references(repo: Path, chapters: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[str]]:
    by_volume: dict[str, list[dict[str, str]]] = defaultdict(list)
    for chapter in chapters:
        by_volume[chapter["volume"]].append(chapter)
    positions = {}
    for volume, rows in by_volume.items():
        rows.sort(key=lambda row: int(row["chapter_code"].split("/")[1]))
        positions.update({row["chapter_code"]: (rows, index) for index, row in enumerate(rows)})

    audit, failures = [], []
    for chapter in chapters:
        source = repo / chapter["canonical_path"]
        if not source.exists():
            continue
        for line_number, line in enumerate(source.read_text(encoding="utf-8-sig", errors="replace").splitlines(), 1):
            for match in REFERENCE_RX.finditer(line):
                phrase = match.group(0)
                direction = (match.group(1) or "local").lower()
                target = ""
                if direction in {"next", "previous"}:
                    rows, index = positions[chapter["chapter_code"]]
                    target_index = index + (1 if direction == "next" else -1)
                    if 0 <= target_index < len(rows):
                        target = rows[target_index]["chapter_code"]
                        status = "RESOLVED_SEQUENCE"
                    else:
                        status = "MISSING_SEQUENCE_TARGET"
                        failures.append(f"{status}:{chapter['chapter_code']}:{line_number}")
                elif direction == "later":
                    status = "DIRECTIONAL_REFERENCE_REVIEW"
                else:
                    status = "LOCAL_CONTEXT"
                audit.append({
                    "source_code": chapter["chapter_code"], "source_path": chapter["canonical_path"],
                    "line": str(line_number), "phrase": phrase, "target_code": target, "status": status,
                })
    return audit, failures


def write_or_check(path: Path, content: str, check: bool, mismatches: list[str]) -> None:
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            mismatches.append(relative(path.parents[2] if "reports" in path.parts else path.parents[1], path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--check", action="store_true", help="fail when generated outputs are not current")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    chapters = read_tsv(repo / "editorial/CHAPTER_STATUS.tsv")
    failures, mismatches = [], []
    if len(chapters) != 256:
        failures.append(f"UNEXPECTED_CHAPTER_COUNT:{len(chapters)}")

    theorem_rows, theorem_failures = statement_rows(repo, chapters)
    failures.extend(theorem_failures)
    audit_rows, audit_failures = audit_directional_references(repo, chapters)
    failures.extend(audit_failures)
    bridge_path = repo / "reports/series/CROSS_VOLUME_CHAPTER_BRIDGES.tsv"
    bridges = read_tsv(bridge_path) if bridge_path.exists() else []
    if not bridges:
        failures.append("MISSING_CROSS_VOLUME_BRIDGES")

    notation = [
        "# Series Notation Index", "",
        "Generated from `shared/notation.tex`. This records only series-wide macros; chapter-local notation remains defined at its point of use.",
        "", "| Command | Arguments | Expansion |", "|---|---:|---|",
    ]
    for command, arity, body in notation_macros((repo / "shared/notation.tex").read_text(encoding="utf-8")):
        notation.append(f"| `\\{command}` | {arity} | `{body}` |")
    notation += ["", "## Editorial conventions", "", "- `X, Y, Z`: spaces, schemes, or varieties", "- `A, B, R, S`: rings", "- `M, N`: modules", "- `\\mathfrak p, \\mathfrak q`: prime ideals", "- `\\mathfrak m`: maximal ideals", "- `\\mathcal F, \\mathcal G`: sheaves", ""]

    theorem = ["# Series Theorem and Named Statement Index", "", "Generated from named `theorem`, `proposition`, `lemma`, `corollary`, and `definition` environments in canonical chapter sources.", "", "| Name | Kind | Chapter | Label |", "|---|---|---|---|"]
    for row in theorem_rows:
        theorem.append(f"| {row['name']} | {row['kind']} | {row['chapter_code']} — {row['chapter_title']} | `{row['label']}` |")
    theorem.append("")

    subject = ["# Series Subject Index", "", "Generated by matching the canonical chapter titles against the controlled subject vocabulary in `scripts/series/build_series_indexes.py`.", ""]
    for name, words in SUBJECTS.items():
        matches = [row for row in chapters if any(word in row["chapter_title"].casefold() for word in words)]
        subject += [f"## {name}", ""]
        subject.extend(f"- **{row['chapter_code']} — {row['chapter_title']}**" for row in matches)
        subject.append("")

    cross = ["# Cross-Volume Index", "", "Generated from the curated bridge ledger. These are reading-navigation links, not formal dependency claims.", "", "The fuller rationale appears in `CROSS_VOLUME_MATHEMATICAL_NAVIGATION.md`.", ""]
    for row in bridges:
        if row["source_volume"] != row["target_volume"]:
            cross.append(f"- **{row['source_code']} — {row['source_title']}** → **{row['target_code']} — {row['target_title']}** ({row['bridge_kind']}): {row['rationale']}")
    cross.append("")

    audit = ["# Directional Reference Audit", "", "This audit checks the high-risk directional phrases `previous chapter`, `next chapter`, `later chapter`, `as shown above`, and `as discussed previously` in canonical chapter sources.", "", "`RESOLVED_SEQUENCE` is checked against the canonical chapter ledger. `LOCAL_CONTEXT` is intra-chapter wording, not a cross-volume navigation claim. `DIRECTIONAL_REFERENCE_REVIEW` requires an editorial decision before calling it a stale reference.", "", f"- Chapter ledger entries: **{len(chapters)}**", f"- Named statements indexed: **{len(theorem_rows)}**", f"- Directional phrases found: **{len(audit_rows)}**", ""]

    outputs = {
        repo / "books/NOTATION_INDEX.md": "\n".join(notation),
        repo / "books/THEOREM_INDEX.md": "\n".join(theorem),
        repo / "books/SUBJECT_INDEX.md": "\n".join(subject),
        repo / "books/CROSS_VOLUME_INDEX.md": "\n".join(cross),
        repo / "reports/series/STALE_REFERENCE_AUDIT.md": "\n".join(audit),
        repo / "reports/series/THEOREM_INDEX.tsv": tsv(theorem_rows, ["name", "kind", "volume", "chapter_code", "chapter_title", "label", "source_path"]),
        repo / "reports/series/STALE_REFERENCE_AUDIT.tsv": tsv(audit_rows, ["source_code", "source_path", "line", "phrase", "target_code", "status"]),
    }
    for path, content in outputs.items():
        write_or_check(path, content.rstrip() + "\n", args.check, mismatches)

    if mismatches:
        failures.extend(f"OUT_OF_DATE:{path}" for path in mismatches)
    print(f"Indexed {len(chapters)} chapters, {len(theorem_rows)} named statements, {len(bridges)} curated bridges, and {len(audit_rows)} directional references.")
    if failures:
        print("FAIL: " + ", ".join(failures))
        return 3
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
