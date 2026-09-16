#!/usr/bin/env python3
"""Build the imported/dossier problem ledger from the consolidated TeX corpus.

The scanner is intentionally conservative: it discovers problem-like objects and
records provenance. It does NOT decide canonical placement or modify book files.

Default source root:
  imports/ALL_TEX_AND_FIGURES/tex/

Generated outputs:
  imports/problem_inventory/SOURCE_FILES.tsv
  imports/problem_inventory/RAW_PROBLEM_ITEMS.tsv
  imports/problem_inventory/REJECTED_STRUCTURAL_ITEMS.tsv
  imports/problem_inventory/DETACHED_SOLUTION_ITEMS.tsv
  imports/problem_inventory/PROBLEM_LEDGER.tsv
  imports/problem_inventory/PROBLEM_SOLUTION_LINKS.tsv
  imports/problem_inventory/DUPLICATE_GROUPS.tsv
  imports/problem_inventory/INVENTORY_SUMMARY.md
  imports/problem_inventory/orphan_solutions.md
  imports/problem_inventory/orphan_problems.md
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, Optional

TRACKED_ENVS = {
    "problem": "PROBLEM",
    "exercise": "EXERCISE",
    "example": "WORKED_EXAMPLE",
    "question": "QUESTION",
    "task": "TASK",
    "challenge": "CHALLENGE",
}
SOLUTION_ENVS = {"solution", "answer", "proofsolution"}
HINT_ENVS = {"hint", "hints"}
THEOREM_ENVS = {"theorem", "proposition", "lemma", "corollary"}
PROBLEM_SECTION_RE = re.compile(
    r"\b(problems?|exercises?|problem\s+sets?|dossiers?|challenges?|questions?)\b",
    re.IGNORECASE,
)
SECTION_RE = re.compile(
    r"\\(?P<kind>chapter|section|subsection|subsubsection|paragraph)\*?\s*\{(?P<title>[^{}]{0,500})\}"
)
BEGIN_ENV_RE = re.compile(r"\\begin\{(?P<env>[A-Za-z*]+)\}(?:\[(?P<opt>[^\]]*)\])?")
END_ENV_TMPL = r"\\end\{%s\}"
PLAIN_PROBLEM_RE = re.compile(
    r"^\s*(?:\\(?:textbf|bfseries)\s*\{?\s*)?"
    r"(?P<kind>Problem|Exercise|Example|Challenge|Question|Task)"
    r"(?:\s+(?P<num>[A-Za-z0-9][A-Za-z0-9.()_\-/]*))?\s*[:.]\s*(?P<rest>.*)$",
    re.IGNORECASE,
)
PLAIN_SOLUTION_RE = re.compile(r"^\s*(?:\\textbf\{)?(?P<kind>Solution|Answer)\}?\s*[:.]", re.IGNORECASE)
PLAIN_HINT_RE = re.compile(r"^\s*(?:\\textbf\{)?Hint\}?\s*[:.]", re.IGNORECASE)
ITEM_RE = re.compile(r"^\s*\\item(?:\[(?P<label>[^\]]+)\])?\s*(?P<rest>.*)$")
FIGURE_RE = re.compile(
    r"\\includegraphics(?:\[[^\]]*\])?\{(?P<g>[^}]+)\}|"
    r"\\input\{(?P<i>[^}]*?(?:tikz|figure|fig)[^}]*)\}|"
    r"\\begin\{tikzpicture\}",
    re.IGNORECASE,
)
NUMBERISH_RE = re.compile(r"(?:Problem|Exercise|Example|Question|Task|Challenge)?\s*([A-Za-z]*\d+(?:[.\-]\d+)*[A-Za-z]?)", re.I)
COMMENT_RE = re.compile(r"(?<!\\)%.*$")

SECTION_LEVEL = {"chapter": 0, "section": 1, "subsection": 2, "subsubsection": 3, "paragraph": 4}


@dataclass
class Candidate:
    source_path: Path
    source_collection: str
    detected_type: str
    start_line: int
    end_line: int
    source_number: str = ""
    source_heading: str = ""
    title: str = ""
    confidence: str = "MEDIUM"
    raw_text: str = ""
    statement_hash: str = ""
    has_hint: bool = False
    has_solution: bool = False
    solution_location: str = ""
    figure_references: str = ""
    problem_id: str = ""
    source_id: str = ""
    duplicate_group: str = ""


@dataclass
class DetachedSolution:
    source_path: Path
    start_line: int
    end_line: int
    source_number: str
    kind: str
    solution_id: str = ""
    linked_problem_id: str = ""


def strip_tex_comment(line: str) -> str:
    return COMMENT_RE.sub("", line)


def normalize_statement(text: str) -> str:
    # Remove comments and solution/hint material from the fingerprint input.
    text = re.sub(r"\\begin\{(?:solution|answer|proofsolution|hint|hints)\}.*?\\end\{(?:solution|answer|proofsolution|hint|hints)\}", " ", text, flags=re.I | re.S)
    text = re.split(r"(?im)^\s*(?:\\textbf\{)?(?:Solution|Answer|Hint)\}?\s*[:.]", text, maxsplit=1)[0]
    lines = [strip_tex_comment(x) for x in text.splitlines()]
    text = "\n".join(lines)
    text = re.sub(r"\\label\{[^}]+\}", " ", text)
    # Remove presentation wrappers so the same mathematical statement can hash
    # identically across problem/exercise/example formatting variants.
    text = re.sub(r"\\begin\{(?:problem|exercise|example|question|task|challenge)\*?\}(?:\[[^\]]*\])?", " ", text, flags=re.I)
    text = re.sub(r"\\end\{(?:problem|exercise|example|question|task|challenge)\*?\}", " ", text, flags=re.I)
    text = re.sub(r"\\(?:section|subsection|subsubsection|paragraph)\*?\{\s*(?:Problem|Exercise|Example|Question|Task|Challenge)[^}]*\}", " ", text, flags=re.I)
    text = re.sub(r"^\s*\\item(?:\[[^\]]+\])?\s*", "", text, flags=re.I)
    text = re.sub(r"^\s*(?:\\textbf\{)?(?:Problem|Exercise|Example|Question|Task|Challenge)(?:\s+[A-Za-z0-9][A-Za-z0-9.()_\-/]*)?\}?\s*[:.]\s*", "", text, flags=re.I)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def statement_hash(text: str) -> str:
    norm = normalize_statement(text)
    return hashlib.sha256(norm.encode("utf-8", errors="replace")).hexdigest() if norm else ""


def candidate_statement_hash(c: "Candidate") -> str:
    """Hash actual statement content, with one safe recovery path.

    A heading such as ``\\section{Problem 4: Prove ...}`` is itself the statement,
    but normalize_statement intentionally removes presentation headings.  For
    heading-based candidates only, recover the extracted heading remainder.

    Empty environment wrappers / empty ``Problem 4.`` markers are deliberately
    left hashless and later quarantined from the semantic ledger.
    """
    h = statement_hash(c.raw_text)
    if h:
        return h
    first = next((strip_tex_comment(x).strip() for x in c.raw_text.splitlines() if strip_tex_comment(x).strip()), "")
    if first and SECTION_RE.search(first) and c.title.strip():
        return statement_hash(c.title)
    return ""


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def safe_read(path: Path) -> str:
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def collection_code(collection: str) -> str:
    return {"Downloads": "DL", "MATH-ALLS-2": "M2", "MATH_ALLS-3": "M3"}.get(collection, "OT")


def make_source_id(collection: str, rel_path: str) -> str:
    digest = hashlib.sha1(rel_path.replace("\\", "/").encode("utf-8")).hexdigest()[:10].upper()
    return f"IMP-{collection_code(collection)}-{digest}"


def collection_from_path(source_root: Path, path: Path) -> str:
    rel = path.relative_to(source_root)
    return rel.parts[0] if rel.parts else "UNKNOWN"


def get_sections(lines: list[str]) -> list[tuple[int, str, int]]:
    out: list[tuple[int, str, int]] = []
    for i, line in enumerate(lines, 1):
        for m in SECTION_RE.finditer(strip_tex_comment(line)):
            out.append((i, m.group("title").strip(), SECTION_LEVEL[m.group("kind")]))
    return out


def nearest_heading(sections: list[tuple[int, str, int]], line_no: int) -> str:
    heading = ""
    for ln, title, _lvl in sections:
        if ln <= line_no:
            heading = title
        else:
            break
    return heading


def heading_scope_end(sections: list[tuple[int, str, int]], idx: int, total_lines: int) -> int:
    line_no, _title, level = sections[idx]
    for j in range(idx + 1, len(sections)):
        ln2, _t2, lvl2 = sections[j]
        if lvl2 <= level:
            return ln2 - 1
    return total_lines


def extract_env_candidates(text: str, lines: list[str], path: Path, collection: str, sections: list[tuple[int, str, int]]) -> list[Candidate]:
    candidates: list[Candidate] = []
    for m in BEGIN_ENV_RE.finditer(text):
        env_raw = m.group("env")
        env = env_raw.rstrip("*").lower()
        if env not in TRACKED_ENVS:
            continue
        end_re = re.compile(END_ENV_TMPL % re.escape(env_raw), re.I)
        em = end_re.search(text, m.end())
        if not em:
            end_pos = len(text)
            confidence = "LOW"
        else:
            end_pos = em.end()
            confidence = "HIGH"
        start = line_of(text, m.start())
        end = line_of(text, end_pos)
        raw = text[m.start():end_pos]
        opt = (m.group("opt") or "").strip()
        num = ""
        if opt:
            nm = NUMBERISH_RE.search(opt)
            if nm:
                num = nm.group(1)
        candidates.append(Candidate(
            source_path=path,
            source_collection=collection,
            detected_type=TRACKED_ENVS[env],
            start_line=start,
            end_line=end,
            source_number=num,
            source_heading=nearest_heading(sections, start),
            title=opt,
            confidence=confidence,
            raw_text=raw,
        ))
    return candidates


def range_overlaps(a0: int, a1: int, b0: int, b1: int) -> bool:
    return max(a0, b0) <= min(a1, b1)


def already_covered(candidates: list[Candidate], start: int, end: int) -> bool:
    return any(range_overlaps(c.start_line, c.end_line, start, end) for c in candidates)


def extract_plain_and_heading_candidates(lines: list[str], path: Path, collection: str, sections: list[tuple[int, str, int]], existing: list[Candidate]) -> list[Candidate]:
    starts: list[tuple[int, str, str, str, str]] = []  # line, kind, num, title, confidence
    for i, line in enumerate(lines, 1):
        clean = strip_tex_comment(line)
        pm = PLAIN_PROBLEM_RE.match(clean)
        if pm:
            starts.append((i, pm.group("kind").upper(), pm.group("num") or "", (pm.group("rest") or "").strip(), "MEDIUM"))
            continue
        sm = SECTION_RE.search(clean)
        if sm:
            title = sm.group("title").strip()
            # Require a word boundary after the singular kind so plural structural
            # headings such as ``Examples`` are not misread as ``Example s``.
            mm = re.match(r"\s*(Problem|Exercise|Example|Challenge|Question|Task)\b(?:\s+([A-Za-z0-9][A-Za-z0-9.()_\-/]*))?\s*[:.\-]?\s*(.*)$", title, re.I)
            if mm and not PROBLEM_SECTION_RE.fullmatch(title.strip()):
                starts.append((i, mm.group(1).upper(), mm.group(2) or "", mm.group(3).strip(), "MEDIUM"))
    starts.sort()
    out: list[Candidate] = []
    boundary_lines = sorted({s[0] for s in starts} | {x[0] for x in sections})
    for idx, (start, kind, num, title, conf) in enumerate(starts):
        if already_covered(existing + out, start, start):
            continue

        # Numbered section-style problems often use a nested ``Exact statement``
        # subsection followed by a ``Solution`` subsection.  Treat the whole
        # statement region as one problem instead of truncating at the first
        # nested heading.  Stop before Solution/Answer/Hint or before the next
        # numbered problem at the same-or-higher structural level.
        section_here = next(((ln, stitle, lvl) for ln, stitle, lvl in sections if ln == start), None)
        if section_here is not None:
            _ln0, _stitle0, level0 = section_here
            end = len(lines)
            for ln2, title2, lvl2 in sections:
                if ln2 <= start:
                    continue
                if re.match(r"\s*(Solution|Answer|Hint|Hints)\b", title2, re.I):
                    end = ln2 - 1
                    break
                numbered2 = re.match(
                    r"\s*(Problem|Exercise|Example|Challenge|Question|Task)\b(?:\s+[A-Za-z0-9][A-Za-z0-9.()_\-/]*)?",
                    title2,
                    re.I,
                )
                if numbered2 and lvl2 <= level0:
                    end = ln2 - 1
                    break
                if lvl2 < level0:
                    end = ln2 - 1
                    break
        else:
            next_lines = [ln for ln in boundary_lines if ln > start]
            end = (next_lines[0] - 1) if next_lines else len(lines)

        end = max(start, end)
        raw = "\n".join(lines[start - 1:end])
        out.append(Candidate(
            source_path=path,
            source_collection=collection,
            detected_type="WORKED_EXAMPLE" if kind == "EXAMPLE" else kind,
            start_line=start,
            end_line=end,
            source_number=num,
            source_heading=nearest_heading(sections, start),
            title=title,
            confidence=conf,
            raw_text=raw,
        ))
    return out


def extract_problem_section_items(lines: list[str], path: Path, collection: str, sections: list[tuple[int, str, int]], existing: list[Candidate]) -> list[Candidate]:
    out: list[Candidate] = []
    for si, (sec_line, title, _level) in enumerate(sections):
        if not PROBLEM_SECTION_RE.search(title):
            continue
        scope_end = heading_scope_end(sections, si, len(lines))
        item_lines: list[tuple[int, str, str]] = []
        env_depth = 0
        for ln in range(sec_line + 1, scope_end + 1):
            clean = strip_tex_comment(lines[ln - 1])
            env_depth += len(re.findall(r"\\begin\{(?:enumerate|itemize|description)\}", clean))
            im = ITEM_RE.match(clean)
            if im and env_depth > 0:
                item_lines.append((ln, (im.group("label") or "").strip(), (im.group("rest") or "").strip()))
            env_depth -= len(re.findall(r"\\end\{(?:enumerate|itemize|description)\}", clean))
            env_depth = max(0, env_depth)
        for j, (start, label, rest) in enumerate(item_lines):
            end = item_lines[j + 1][0] - 1 if j + 1 < len(item_lines) else scope_end
            if already_covered(existing + out, start, end):
                continue
            num = ""
            if label:
                nm = NUMBERISH_RE.search(label)
                num = nm.group(1) if nm else label
            raw = "\n".join(lines[start - 1:end])
            out.append(Candidate(
                source_path=path,
                source_collection=collection,
                detected_type="EXERCISE_ITEM" if "exercise" in title.lower() else "PROBLEM_ITEM",
                start_line=start,
                end_line=end,
                source_number=num,
                source_heading=title,
                title=rest[:240],
                confidence="MEDIUM",
                raw_text=raw,
            ))

        # Theorem-like exercise candidates inside a problem/exercise section, when not inside items.
        scope_text = "\n".join(lines[sec_line:scope_end])
        offset_line = sec_line + 1
        for m in BEGIN_ENV_RE.finditer(scope_text):
            env_raw = m.group("env")
            env = env_raw.rstrip("*").lower()
            if env not in THEOREM_ENVS:
                continue
            start = offset_line + scope_text.count("\n", 0, m.start())
            end_re = re.compile(END_ENV_TMPL % re.escape(env_raw), re.I)
            em = end_re.search(scope_text, m.end())
            end = (offset_line + scope_text.count("\n", 0, em.end())) if em else scope_end
            if already_covered(existing + out, start, end):
                continue
            raw = "\n".join(lines[start - 1:end])
            out.append(Candidate(
                source_path=path,
                source_collection=collection,
                detected_type="PROOF_EXERCISE_CANDIDATE",
                start_line=start,
                end_line=end,
                source_heading=title,
                confidence="LOW",
                raw_text=raw,
            ))
    return out


def numbered_problem_heading_before(sections: list[tuple[int, str, int]], line_no: int) -> tuple[str, str]:
    """Return (kind, number) from the nearest numbered problem/exercise heading.

    This is primarily for legacy solution sections such as::

        \\subsection*{Exercise 4.1}
        \\begin{solution}

    The heading is provenance for the solution, not a statement-bearing problem.
    """
    for ln, title, _lvl in reversed(sections):
        if ln >= line_no:
            continue
        m = re.match(
            r"\s*(Problem|Exercise|Example|Challenge|Question|Task)\s*([A-Za-z0-9.()_\-/]+)\s*[:.\-]?\s*(.*)$",
            title,
            re.I,
        )
        if m:
            return m.group(1).upper(), m.group(2)
        # Stop at the first intervening section heading.  A remote heading from a
        # different section must not donate its numbering to this solution.
        break
    return "", ""


def parent_numbered_problem_heading(
    sections: list[tuple[int, str, int]], line_no: int
) -> tuple[str, str]:
    r"""Find the nearest enclosing numbered problem/exercise section.

    Legacy dossiers often use::

        \section{Problem 1}
        \subsection*{Exact statement}
        ...
        \subsection*{Solution}

    For the Solution subsection, the immediately preceding heading is
    ``Exact statement`` rather than ``Problem 1``.  Walk upward through the
    heading hierarchy and recover the numbered parent.
    """
    current_level = None
    for ln, _title, lvl in sections:
        if ln == line_no:
            current_level = lvl
            break
    if current_level is None:
        current_level = 99
    for ln, title, lvl in reversed(sections):
        if ln >= line_no:
            continue
        if lvl >= current_level:
            continue
        m = re.match(
            r"\s*(Problem|Exercise|Example|Challenge|Question|Task)\b(?:\s+([A-Za-z0-9][A-Za-z0-9.()_\-/]*))?",
            title,
            re.I,
        )
        if m:
            return m.group(1).upper(), m.group(2) or ""
        # Once we encounter a non-numbered parent at a higher structural level,
        # the solution is not enclosed by a numbered problem heading.
        if lvl < current_level:
            current_level = lvl
    return "", ""


def is_detached_solution_heading_candidate(c: Candidate) -> bool:
    """True when a hashless numbered problem heading only wraps solution/hint material."""
    if c.statement_hash:
        return False
    first = next(
        (strip_tex_comment(x).strip() for x in c.raw_text.splitlines() if strip_tex_comment(x).strip()),
        "",
    )
    if not SECTION_RE.search(first):
        return False
    return bool(re.search(r"\\begin\{(?:solution|answer|proofsolution|hint|hints)\}", c.raw_text, re.I))


def detect_detached_solution_blocks(text: str, lines: list[str], path: Path, sections: list[tuple[int, str, int]]) -> list[DetachedSolution]:
    sols: list[DetachedSolution] = []
    for m in BEGIN_ENV_RE.finditer(text):
        env_raw = m.group("env")
        env = env_raw.rstrip("*").lower()
        if env not in SOLUTION_ENVS and env not in HINT_ENVS:
            continue
        end_re = re.compile(END_ENV_TMPL % re.escape(env_raw), re.I)
        em = end_re.search(text, m.end())
        end_pos = em.end() if em else len(text)
        start = line_of(text, m.start())
        end = line_of(text, end_pos)
        opt = (m.group("opt") or "").strip()
        nm = NUMBERISH_RE.search(opt) if opt else None
        source_num = nm.group(1) if nm else ""
        if not source_num:
            _heading_kind, source_num = numbered_problem_heading_before(sections, start)
        if not source_num:
            _parent_kind, source_num = parent_numbered_problem_heading(sections, start)
        sols.append(DetachedSolution(path, start, end, source_num, "HINT" if env in HINT_ENVS else "SOLUTION"))
    # Heading-delimited solutions/hints (common in long legacy dossiers):
    # ``\subsection*{Solution}`` followed by ordinary prose, often with nested
    # subsubsections and no solution environment.
    for si, (sec_line, sec_title, _sec_level) in enumerate(sections):
        mt = re.match(r"\s*(Solution|Answer|Hint|Hints)\b(?:\s+(?:to|for)\s+)?(.*)$", sec_title, re.I)
        if not mt:
            continue
        scope_end = heading_scope_end(sections, si, len(lines))
        if any(range_overlaps(sec_line, scope_end, x.start_line, x.end_line) for x in sols):
            continue
        tail = (mt.group(2) or "").strip()
        nm = NUMBERISH_RE.search(tail) if tail else None
        source_num = nm.group(1) if nm else ""
        if not source_num:
            _pkind, source_num = parent_numbered_problem_heading(sections, sec_line)
        kind = "HINT" if mt.group(1).lower().startswith("hint") else "SOLUTION"
        sols.append(DetachedSolution(path, sec_line, scope_end, source_num, kind))

    for i, line in enumerate(lines, 1):
        clean = strip_tex_comment(line)
        sm = PLAIN_SOLUTION_RE.match(clean)
        hm = PLAIN_HINT_RE.match(clean)
        if not sm and not hm:
            continue
        if any(s.start_line <= i <= s.end_line for s in sols):
            continue
        next_mark = len(lines)
        for j in range(i + 1, len(lines) + 1):
            c2 = strip_tex_comment(lines[j - 1])
            if PLAIN_PROBLEM_RE.match(c2) or PLAIN_SOLUTION_RE.match(c2) or PLAIN_HINT_RE.match(c2) or SECTION_RE.search(c2):
                next_mark = j - 1
                break
        prefix = clean[:120]
        nm = NUMBERISH_RE.search(prefix)
        source_num = nm.group(1) if nm else ""
        if not source_num:
            _heading_kind, source_num = numbered_problem_heading_before(sections, i)
        if not source_num:
            _parent_kind, source_num = parent_numbered_problem_heading(sections, i)
        sols.append(DetachedSolution(path, i, max(i, next_mark), source_num, "HINT" if hm else "SOLUTION"))
    sols.sort(key=lambda s: (s.start_line, s.end_line))
    return sols


def attach_metadata(candidates: list[Candidate], detached: list[DetachedSolution]) -> None:
    candidates.sort(key=lambda c: (c.start_line, c.end_line))
    for i, c in enumerate(candidates):
        c.statement_hash = candidate_statement_hash(c)
        figs = []
        for fm in FIGURE_RE.finditer(c.raw_text):
            figs.append(fm.group("g") or fm.group("i") or "tikzpicture")
        c.figure_references = ";".join(dict.fromkeys(figs))
        if re.search(r"\\begin\{(?:hint|hints)\}|^\s*(?:\\textbf\{)?Hint\}?\s*[:.]", c.raw_text, re.I | re.M):
            c.has_hint = True
        if re.search(r"\\begin\{(?:solution|answer|proofsolution)\}|^\s*(?:\\textbf\{)?(?:Solution|Answer)\}?\s*[:.]", c.raw_text, re.I | re.M):
            c.has_solution = True
            c.solution_location = f"L{c.start_line}-L{c.end_line}"



def dedupe_candidates(candidates: list[Candidate]) -> list[Candidate]:
    # Keep one candidate when multiple detectors identify the same/near-identical span.
    rank = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
    kept: list[Candidate] = []
    for c in sorted(candidates, key=lambda x: (x.start_line, -rank.get(x.confidence, 0), x.end_line)):
        dupe_idx: Optional[int] = None
        for k, e in enumerate(kept):
            if c.start_line == e.start_line or (
                range_overlaps(c.start_line, c.end_line, e.start_line, e.end_line)
                and min(c.end_line - c.start_line + 1, e.end_line - e.start_line + 1) / max(c.end_line - c.start_line + 1, e.end_line - e.start_line + 1) > 0.75
            ):
                dupe_idx = k
                break
        if dupe_idx is None:
            kept.append(c)
        else:
            e = kept[dupe_idx]
            if rank.get(c.confidence, 0) > rank.get(e.confidence, 0):
                kept[dupe_idx] = c
    return sorted(kept, key=lambda x: (x.start_line, x.end_line))


def scan_file(source_root: Path, path: Path) -> tuple[list[Candidate], list[DetachedSolution]]:
    text = safe_read(path)
    lines = text.splitlines()
    collection = collection_from_path(source_root, path)
    sections = get_sections(lines)
    cands = extract_env_candidates(text, lines, path, collection, sections)
    cands.extend(extract_plain_and_heading_candidates(lines, path, collection, sections, cands))
    cands.extend(extract_problem_section_items(lines, path, collection, sections, cands))
    cands = dedupe_candidates(cands)
    detached = detect_detached_solution_blocks(text, lines, path, sections)
    attach_metadata(cands, detached)
    return cands, detached


def tsv_write(path: Path, fieldnames: list[str], rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def clean_cell(value: object) -> object:
    if isinstance(value, bool):
        return "YES" if value else "NO"
    if value is None:
        return ""
    return value


def build(repo: Path, source_root: Path, out_dir: Path) -> dict[str, int]:
    tex_files = sorted(p for p in source_root.rglob("*.tex") if p.is_file())
    if not tex_files:
        raise SystemExit(f"No .tex files found under {source_root}")

    source_rows = []
    all_discovered: list[Candidate] = []
    all_candidates: list[Candidate] = []
    rejected_structural: list[Candidate] = []
    detached_solution_markers: list[Candidate] = []
    all_solutions: list[DetachedSolution] = []

    for p in tex_files:
        rel = p.relative_to(source_root).as_posix()
        collection = collection_from_path(source_root, p)
        sid = make_source_id(collection, rel)
        raw_bytes = p.read_bytes()
        source_rows.append({
            "source_id": sid,
            "source_collection": collection,
            "source_file": rel,
            "repo_path": p.relative_to(repo).as_posix(),
            "sha256": hashlib.sha256(raw_bytes).hexdigest(),
            "size_bytes": len(raw_bytes),
        })
        cands, sols = scan_file(source_root, p)
        for idx, c in enumerate(cands, 1):
            c.source_id = sid
            c.problem_id = f"{sid}-P{idx:03d}"
        for idx, s in enumerate(sols, 1):
            s.solution_id = f"{sid}-S{idx:03d}"
        # Keep stable IDs for every structural detection.  Only genuine
        # statement-bearing candidates enter the semantic PROBLEM_LEDGER.
        # Hashless numbered headings that introduce solution/hint blocks are
        # detached-solution markers, not rejected problems.
        valid_cands = [c for c in cands if c.statement_hash]
        detached_markers = [c for c in cands if is_detached_solution_heading_candidate(c)]
        detached_marker_ids = {c.problem_id for c in detached_markers}
        rejected_cands = [c for c in cands if not c.statement_hash and c.problem_id not in detached_marker_ids]

        # Link detached solution/hint blocks conservatively:
        #   1) containing statement-bearing candidate;
        #   2) exact same-file problem number;
        #   3) very-near preceding unnumbered statement (legacy inline style).
        # A solution-only file with Exercise 4.1 headings remains orphaned for
        # the later cross-file/numbering reconciliation pass rather than being
        # attached to an unrelated preceding example.
        for sol in sols:
            containing = [c for c in valid_cands if c.start_line <= sol.start_line <= c.end_line]
            if containing:
                sol.linked_problem_id = min(containing, key=lambda c: c.end_line - c.start_line).problem_id
                continue
            if sol.source_number:
                exact = [c for c in valid_cands if c.source_number and c.source_number == sol.source_number]
                if exact:
                    before = [c for c in exact if c.start_line <= sol.start_line]
                    chosen = before[-1] if before else exact[0]
                    sol.linked_problem_id = chosen.problem_id
                continue
            preceding = [c for c in valid_cands if c.end_line < sol.start_line and sol.start_line - c.end_line <= 3]
            if preceding:
                sol.linked_problem_id = preceding[-1].problem_id

        for c in valid_cands:
            linked = [sol for sol in sols if sol.linked_problem_id == c.problem_id]
            if linked:
                c.has_hint = c.has_hint or any(sol.kind == "HINT" for sol in linked)
                linked_solution = next((sol for sol in linked if sol.kind == "SOLUTION"), None)
                if linked_solution:
                    c.has_solution = True
                    c.solution_location = f"L{linked_solution.start_line}-L{linked_solution.end_line}"

        all_discovered.extend(cands)
        all_candidates.extend(valid_cands)
        detached_solution_markers.extend(detached_markers)
        rejected_structural.extend(rejected_cands)
        all_solutions.extend(sols)

    # Exact duplicate groups by normalized statement hash.
    by_hash: dict[str, list[Candidate]] = defaultdict(list)
    for c in all_candidates:
        if c.statement_hash:
            by_hash[c.statement_hash].append(c)
    duplicate_groups = []
    dup_counter = 0
    for h, group in sorted(by_hash.items()):
        if len(group) < 2:
            continue
        dup_counter += 1
        gid = f"DUP-{dup_counter:05d}"
        for c in group:
            c.duplicate_group = gid
        duplicate_groups.append({
            "duplicate_group": gid,
            "statement_hash": h,
            "member_count": len(group),
            "problem_ids": ";".join(c.problem_id for c in group),
            "source_files": ";".join(sorted({c.source_path.relative_to(source_root).as_posix() for c in group})),
            "review_status": "NEEDS_EDITORIAL_REVIEW",
        })

    source_fields = ["source_id", "source_collection", "source_file", "repo_path", "sha256", "size_bytes"]
    tsv_write(out_dir / "SOURCE_FILES.tsv", source_fields, source_rows)

    raw_fields = [
        "problem_id", "source_id", "source_collection", "source_file", "start_line", "end_line",
        "source_number", "source_heading", "detected_type", "statement_text_hash", "has_hint",
        "has_solution", "solution_location", "figure_references", "confidence",
    ]
    raw_rows = []
    for c in all_discovered:
        raw_rows.append({
            "problem_id": c.problem_id,
            "source_id": c.source_id,
            "source_collection": c.source_collection,
            "source_file": c.source_path.relative_to(source_root).as_posix(),
            "start_line": c.start_line,
            "end_line": c.end_line,
            "source_number": c.source_number,
            "source_heading": c.source_heading,
            "detected_type": c.detected_type,
            "statement_text_hash": c.statement_hash,
            "has_hint": clean_cell(c.has_hint),
            "has_solution": clean_cell(c.has_solution),
            "solution_location": c.solution_location,
            "figure_references": c.figure_references,
            "confidence": c.confidence,
        })
    tsv_write(out_dir / "RAW_PROBLEM_ITEMS.tsv", raw_fields, raw_rows)

    rejected_fields = [
        "problem_id", "source_id", "source_collection", "source_file", "source_line_range",
        "source_problem_number", "source_heading", "detected_type", "confidence", "rejection_reason",
    ]
    rejected_rows = []
    for c in rejected_structural:
        rejected_rows.append({
            "problem_id": c.problem_id,
            "source_id": c.source_id,
            "source_collection": c.source_collection,
            "source_file": c.source_path.relative_to(source_root).as_posix(),
            "source_line_range": f"L{c.start_line}-L{c.end_line}",
            "source_problem_number": c.source_number,
            "source_heading": c.source_heading or c.title,
            "detected_type": c.detected_type,
            "confidence": c.confidence,
            "rejection_reason": "EMPTY_NORMALIZED_STATEMENT; structural marker retained for audit",
        })
    tsv_write(out_dir / "REJECTED_STRUCTURAL_ITEMS.tsv", rejected_fields, rejected_rows)

    detached_marker_fields = [
        "problem_id", "source_id", "source_collection", "source_file", "source_line_range",
        "source_problem_number", "source_heading", "detected_type", "confidence",
        "linked_solution_ids", "classification_reason",
    ]
    detached_marker_rows = []
    solutions_by_file_number: dict[tuple[str, str], list[DetachedSolution]] = defaultdict(list)
    for sol in all_solutions:
        rel = sol.source_path.relative_to(source_root).as_posix()
        solutions_by_file_number[(rel, sol.source_number)].append(sol)
    for c in detached_solution_markers:
        rel = c.source_path.relative_to(source_root).as_posix()
        matching = solutions_by_file_number.get((rel, c.source_number), []) if c.source_number else []
        detached_marker_rows.append({
            "problem_id": c.problem_id,
            "source_id": c.source_id,
            "source_collection": c.source_collection,
            "source_file": rel,
            "source_line_range": f"L{c.start_line}-L{c.end_line}",
            "source_problem_number": c.source_number,
            "source_heading": c.source_heading or c.title,
            "detected_type": c.detected_type,
            "confidence": c.confidence,
            "linked_solution_ids": ";".join(sol.solution_id for sol in matching),
            "classification_reason": "SOLUTION_ONLY_HEADING; retain for detached-solution reconciliation",
        })
    tsv_write(out_dir / "DETACHED_SOLUTION_ITEMS.tsv", detached_marker_fields, detached_marker_rows)

    ledger_fields = [
        "problem_id", "source_id", "source_collection", "source_file", "source_location",
        "source_line_range", "source_problem_number", "source_heading", "problem_type",
        "primary_subject", "secondary_subject", "keywords", "has_hint", "has_solution",
        "solution_id", "has_figures", "companion_files", "source_build_status", "statement_hash",
        "duplicate_group", "canonical_match_type", "canonical_problem_id", "canonical_volume",
        "canonical_chapter", "target_volume", "target_chapter", "target_section", "mapping_confidence",
        "migration_status", "migration_commit", "review_status", "notes",
    ]
    solution_by_problem = defaultdict(list)
    for s in all_solutions:
        if s.linked_problem_id:
            solution_by_problem[s.linked_problem_id].append(s)

    ledger_rows = []
    for c in all_candidates:
        linked = solution_by_problem.get(c.problem_id, [])
        sol_ids = [s.solution_id for s in linked if s.kind == "SOLUTION"]
        ledger_rows.append({
            "problem_id": c.problem_id,
            "source_id": c.source_id,
            "source_collection": c.source_collection,
            "source_file": c.source_path.relative_to(source_root).as_posix(),
            "source_location": f"{c.source_path.relative_to(repo).as_posix()}:L{c.start_line}-L{c.end_line}",
            "source_line_range": f"L{c.start_line}-L{c.end_line}",
            "source_problem_number": c.source_number,
            "source_heading": c.source_heading or c.title,
            "problem_type": c.detected_type,
            "primary_subject": "UNCLASSIFIED",
            "secondary_subject": "",
            "keywords": "",
            "has_hint": clean_cell(c.has_hint),
            "has_solution": clean_cell(c.has_solution),
            "solution_id": ";".join(sol_ids),
            "has_figures": "YES" if c.figure_references else "NO",
            "companion_files": c.figure_references,
            "source_build_status": "UNKNOWN",
            "statement_hash": c.statement_hash,
            "duplicate_group": c.duplicate_group,
            "canonical_match_type": "UNREVIEWED",
            "canonical_problem_id": "",
            "canonical_volume": "",
            "canonical_chapter": "",
            "target_volume": "UNCLASSIFIED",
            "target_chapter": "UNCLASSIFIED",
            "target_section": "",
            "mapping_confidence": "UNREVIEWED",
            "migration_status": "UNREVIEWED",
            "migration_commit": "",
            "review_status": "NEEDS_EDITORIAL_REVIEW",
            "notes": "auto-discovered; semantic/canonical reconciliation pending",
        })
    tsv_write(out_dir / "PROBLEM_LEDGER.tsv", ledger_fields, ledger_rows)

    link_fields = ["solution_id", "source_id", "solution_source_file", "solution_line_range", "solution_kind", "source_problem_number", "linked_problem_id", "link_status"]
    link_rows = []
    for s in all_solutions:
        rel = s.source_path.relative_to(source_root).as_posix()
        sid = make_source_id(collection_from_path(source_root, s.source_path), rel)
        link_rows.append({
            "solution_id": s.solution_id,
            "source_id": sid,
            "solution_source_file": rel,
            "solution_line_range": f"L{s.start_line}-L{s.end_line}",
            "solution_kind": s.kind,
            "source_problem_number": s.source_number,
            "linked_problem_id": s.linked_problem_id,
            "link_status": "LINKED_SAME_FILE" if s.linked_problem_id else ("ORPHAN_NUMBERED_SOLUTION" if s.source_number else "ORPHAN_NEEDS_REVIEW"),
        })
    tsv_write(out_dir / "PROBLEM_SOLUTION_LINKS.tsv", link_fields, link_rows)

    dup_fields = ["duplicate_group", "statement_hash", "member_count", "problem_ids", "source_files", "review_status"]
    tsv_write(out_dir / "DUPLICATE_GROUPS.tsv", dup_fields, duplicate_groups)

    orphan_solutions = [r for r in link_rows if not r["linked_problem_id"]]
    orphan_problems = [r for r in ledger_rows if r["has_solution"] == "NO"]

    with (out_dir / "orphan_solutions.md").open("w", encoding="utf-8") as f:
        f.write("# Orphan imported solutions/hints\n\n")
        if not orphan_solutions:
            f.write("None detected by the structural pass.\n")
        else:
            for r in orphan_solutions:
                f.write(f"- `{r['solution_id']}` — `{r['solution_source_file']}` {r['solution_line_range']} ({r['solution_kind']})\n")

    with (out_dir / "orphan_problems.md").open("w", encoding="utf-8") as f:
        f.write("# Imported problem-like items without detected solution\n\n")
        if not orphan_problems:
            f.write("None detected by the structural pass.\n")
        else:
            for r in orphan_problems:
                f.write(f"- `{r['problem_id']}` — `{r['source_file']}` {r['source_line_range']} ({r['problem_type']})\n")

    type_counts = Counter(c.detected_type for c in all_candidates)
    coll_counts = Counter(c.source_collection for c in all_candidates)
    summary_lines = [
        "# Imported problem inventory — structural discovery pass",
        "",
        "> This inventory is discovery/provenance data. It does not modify canonical book content and does not yet assert canonical placement.",
        "",
        "## Counts",
        "",
        f"- Source TeX files scanned: **{len(tex_files)}**",
        f"- Structural problem-like detections: **{len(all_discovered)}**",
        f"- Statement-bearing ledger problems: **{len(all_candidates)}**",
        f"- Empty structural markers quarantined: **{len(rejected_structural)}**",
        f"- Detached solution-heading markers: **{len(detached_solution_markers)}**",
        f"- Solution/hint blocks detected: **{len(all_solutions)}**",
        f"- Exact duplicate groups: **{len(duplicate_groups)}**",
        f"- Orphan solution/hint blocks needing review: **{len(orphan_solutions)}**",
        f"- Problem-like objects without a detected solution: **{len(orphan_problems)}**",
        "",
        "## By source collection",
        "",
    ]
    for k, v in sorted(coll_counts.items()):
        summary_lines.append(f"- {k}: **{v}**")
    summary_lines += ["", "## By detected type", ""]
    for k, v in sorted(type_counts.items()):
        summary_lines.append(f"- {k}: **{v}**")
    summary_lines += [
        "",
        "## Next reconciliation pass",
        "",
        "1. Review LOW-confidence `PROOF_EXERCISE_CANDIDATE` rows.",
        "2. Reconcile detached solution files and numbering mismatches.",
        "3. Classify mathematical subject from actual statement content.",
        "4. Assign Volume/chapter/section.",
        "5. Compare statement hashes/fingerprints against canonical problem index.",
        "6. Replace `UNREVIEWED`/`UNCLASSIFIED` fields with explicit dispositions.",
        "",
    ]
    (out_dir / "INVENTORY_SUMMARY.md").write_text("\n".join(summary_lines), encoding="utf-8")

    return {
        "sources": len(tex_files),
        "structural_detections": len(all_discovered),
        "problems": len(all_candidates),
        "rejected_structural": len(rejected_structural),
        "detached_solution_markers": len(detached_solution_markers),
        "solution_blocks": len(all_solutions),
        "duplicate_groups": len(duplicate_groups),
        "orphan_solutions": len(orphan_solutions),
        "unsolved": len(orphan_problems),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, default=Path.cwd(), help="Repository root (default: cwd)")
    ap.add_argument("--source-root", type=Path, default=None, help="Override consolidated TeX source root")
    ap.add_argument("--out", type=Path, default=None, help="Override output directory")
    args = ap.parse_args()

    repo = args.repo.resolve()
    source_root = (args.source_root.resolve() if args.source_root else repo / "imports" / "ALL_TEX_AND_FIGURES" / "tex")
    out_dir = (args.out.resolve() if args.out else repo / "imports" / "problem_inventory")

    if not source_root.exists():
        print(f"ERROR: source root not found: {source_root}", file=sys.stderr)
        return 2

    counts = build(repo, source_root, out_dir)
    print("Imported problem ledger generated")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    print(f"  output: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
