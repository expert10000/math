#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

STATUS_FIELDS = [
    "volume","chapter_code","chapter_title","status","legacy_source_status",
    "mapped_rule_count","canonical_path","next_action"
]
MOJIBAKE = ("Ã","Â","â€","â€“","â€”","Ä‚","Ă","Äą","Ë","Ĺ","Å","Â¬","Â©","Â¶")
SOURCE_EXTS = {".tex",".svg",".png",".jpg",".jpeg",".pdf"}

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")

def read_tsv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def safe(value) -> str:
    if value is None:
        return "-"
    s = str(value)
    return s if s != "" else "-"

def write_tsv(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["\t".join(fields)]
    for row in rows:
        lines.append("\t".join(safe(row.get(f, "-")) for f in fields))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def write_status(path: Path, rows):
    lines = ["\t".join(STATUS_FIELDS)]
    for row in rows:
        lines.append("\t".join(str(row.get(f, "")) for f in STATUS_FIELDS))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def suspicious(text: str) -> int:
    return sum(text.count(token) for token in MOJIBAKE) + text.count("\ufffd")

def resolve_legacy_source(repo: Path, source_file: str) -> Path:
    direct = repo / source_file
    if direct.exists():
        return direct
    return repo / "chapters/tex" / source_file

def include_map(book_text: str, vol: Path):
    rx = re.compile(r"(?m)^[ \t]*\\include\{(chapters/ch(\d\d)_[^}]+/chapter)\}")
    out = {}
    for m in rx.finditer(book_text):
        code = f"VI/{int(m.group(2)):02d}"
        out[code] = vol / (m.group(1) + ".tex")
    return out

def tex_inputs_missing(vol: Path, text: str):
    missing = []
    for target in re.findall(r"\\input\{([^}]+)\}", text):
        if not target.startswith("chapters/"):
            continue
        base = vol / target
        candidates = [base, Path(str(base) + ".tex")]
        if not any(p.exists() for p in candidates):
            missing.append(target)
    return sorted(set(missing))

def resolve_tex_target(base_dir: Path, target: str):
    r"""Resolve a TeX \input/\include target using the volume working directory."""
    target = target.strip()
    if not target or target.startswith("|"):
        return None
    p = base_dir / target
    candidates = [p]
    if p.suffix == "":
        candidates.append(Path(str(p) + ".tex"))
    for cand in candidates:
        if cand.exists() and cand.is_file():
            return cand.resolve()
    return None

def collect_build_graph(repo: Path, vol: Path):
    """Traverse only TeX files actually reachable from Volume VI book.tex."""
    root = (vol / "book.tex").resolve()
    stack = [root]
    seen = set()
    ordered = []
    edge_rows = []
    cmd_re = re.compile(r"\\(input|include)\{([^}]+)\}")

    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        ordered.append(current)
        text = read_text(current)
        for kind, target in cmd_re.findall(text):
            resolved = resolve_tex_target(vol, target)
            edge_rows.append({
                "source_path": current.relative_to(repo).as_posix(),
                "command": kind,
                "target": target,
                "resolved_path": resolved.relative_to(repo).as_posix() if resolved else "-",
                "classification": "RESOLVED" if resolved else "MISSING_INPUT"
            })
            if resolved and resolved not in seen:
                stack.append(resolved)

    return ordered, edge_rows

def collect_build_labels(repo: Path, build_files):
    labels = defaultdict(list)
    for p in build_files:
        text = read_text(p)
        for label in re.findall(r"\\label\{([^}]+)\}", text):
            labels[label].append(p.relative_to(repo).as_posix())
    return labels

def collect_build_refs(repo: Path, build_files, labels):
    rows = []
    missing = []
    rx = re.compile(r"\\(ref|eqref|autoref|pageref|cref|Cref)\{([^}]+)\}")
    for p in build_files:
        text = read_text(p)
        for kind, payload in rx.findall(text):
            for label in [x.strip() for x in payload.split(",") if x.strip()]:
                owners = labels.get(label, [])
                classification = "RESOLVED" if owners else "MISSING_LABEL"
                rows.append({
                    "source_path": p.relative_to(repo).as_posix(),
                    "ref_kind": kind,
                    "label": label,
                    "target_paths": ";".join(owners) if owners else "-",
                    "classification": classification
                })
                if not owners:
                    missing.append(f"MISSING_REF:{p.relative_to(repo).as_posix()}:{label}")
    return rows, missing

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--apply-status", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    vol = repo / "books/vol06_algebraic_geometry"
    recon = vol / "reconciliation"
    recon.mkdir(parents=True, exist_ok=True)
    status_path = repo / "editorial/CHAPTER_STATUS.tsv"
    source_path = repo / "editorial/SOURCE_MIGRATION.tsv"
    book_path = vol / "book.tex"
    readme_path = vol / "README.md"

    status_all = read_tsv(status_path)
    vi_rows = [r for r in status_all if r.get("volume") == "VI"]
    book_text = read_text(book_path)
    active = include_map(book_text, vol)
    source_rows = read_tsv(source_path)
    vi_source = [r for r in source_rows if re.fullmatch(r"VI/\d{2}", r.get("destination",""))]

    source_by_dest = defaultdict(list)
    for r in vi_source:
        source_by_dest[r["destination"]].append(r)

    build_files, build_edges = collect_build_graph(repo, vol)
    build_labels = collect_build_labels(repo, build_files)
    duplicate_vi_labels = sorted(label for label, owners in build_labels.items() if len(owners) > 1)
    duplicate_label_rows = [
        {
            "label": label,
            "owner_count": len(build_labels[label]),
            "owner_paths": ";".join(build_labels[label])
        }
        for label in duplicate_vi_labels
    ]
    ref_rows, missing_refs = collect_build_refs(repo, build_files, build_labels)

    chapter_rows = []
    source_recon_rows = []
    blockers = []
    per_code_blockers = defaultdict(list)

    if len(vi_rows) != 49:
        blockers.append(f"STATUS_ROWS:{len(vi_rows)} expected 49")
    if len(active) != 49:
        blockers.append(f"ACTIVE_INCLUDES:{len(active)} expected 49")
    if duplicate_vi_labels:
        blockers.append(f"DUPLICATE_LABELS:{len(duplicate_vi_labels)}")
    blockers.extend(missing_refs)

    # Existing series build evidence is a useful freeze-readiness gate.
    build_inventory = repo / "reports/series/BUILD_I_VIII.tsv"
    build_pass = False
    if build_inventory.exists():
        for r in read_tsv(build_inventory):
            if r.get("volume") == "VI" and r.get("target") == "book.tex" and r.get("status") == "PASS":
                build_pass = True
                break
    if not build_pass:
        blockers.append("NO_CURRENT_PASS_BUILD_INVENTORY_FOR_VOLUME_VI")

    row_by_code = {r["chapter_code"]: r for r in vi_rows}
    for n in range(1, 50):
        code = f"VI/{n:02d}"
        sr = row_by_code.get(code)
        cp = active.get(code)
        local = []

        if sr is None:
            local.append("MISSING_STATUS_ROW")
        if cp is None:
            local.append("MISSING_ACTIVE_INCLUDE")
        if cp is not None and not cp.exists():
            local.append("MISSING_CANONICAL_FILE")

        text = read_text(cp) if cp and cp.exists() else ""
        size = cp.stat().st_size if cp and cp.exists() else 0
        sections = len(re.findall(r"(?m)^[ \t]*\\section(?:\*?)\{", text))
        labels = len(re.findall(r"\\label\{[^}]+\}", text))
        problems = len(re.findall(r"\\begin\{problem\}", text, re.I))
        exercises = len(re.findall(r"\\begin\{exercise\}", text, re.I))
        hints = len(re.findall(r"\\begin\{hint\}", text, re.I))
        solutions = len(re.findall(r"\\begin\{solution\}", text, re.I))
        theorem_like = len(re.findall(
            r"\\begin\{(?:definition|theorem|lemma|proposition|corollary|example)\}",
            text, re.I
        ))
        figure_inputs = len(re.findall(r"\\input\{chapters/[^}]*figures/[^}]+\}", text))
        missing_inputs = tex_inputs_missing(vol, text) if text else []

        if cp and cp.exists():
            if size < 2000:
                local.append(f"CONTENT_TOO_SMALL:{size}")
            if not re.search(r"\\chapter(?:\[[^\]]+\])?\{", text) and "\\chapter{" not in text:
                local.append("MISSING_CHAPTER_COMMAND")
            if labels == 0:
                local.append("NO_LABELS")
            if sections < 2:
                local.append(f"TOO_FEW_SECTIONS:{sections}")
            if suspicious(text):
                local.append("SUSPICIOUS_ENCODING")
            if missing_inputs:
                local.append("MISSING_INPUTS:" + ",".join(missing_inputs[:8]))

        rules = source_by_dest.get(code, [])
        legacy_missing = []
        for rule in rules:
            legacy_file = resolve_legacy_source(repo, rule.get("source_file",""))
            exists = legacy_file.exists()
            if not exists:
                legacy_missing.append(rule.get("source_file",""))
            source_recon_rows.append({
                "chapter_code": code,
                "source_file": rule.get("source_file",""),
                "source_block_id": rule.get("source_block_id",""),
                "block_kind": rule.get("block_kind",""),
                "source_selector": rule.get("source_selector",""),
                "action": rule.get("action",""),
                "precedence": rule.get("precedence",""),
                "audit_status": rule.get("audit_status",""),
                "legacy_source_exists": "YES" if exists else "NO",
                "canonical_target": cp.relative_to(repo).as_posix() if cp and cp.exists() else "-",
                "resolution": "RESOLVED_TO_ACTIVE_CANONICAL_CHAPTER" if exists and cp and cp.exists() else "BLOCKED"
            })
        if legacy_missing:
            local.append("MISSING_LEGACY_SOURCE:" + ",".join(sorted(set(legacy_missing))[:8]))

        declared_path = sr.get("canonical_path","") if sr else ""
        active_rel = cp.relative_to(repo).as_posix() if cp else ""
        old_mapped = sr.get("mapped_rule_count","0") if sr else "0"
        actual_mapped = len(rules)

        pedagogy = "NONE"
        if problems + exercises > 0:
            if solutions >= problems + exercises:
                pedagogy = "FULL_SOLUTION_COUNT"
            elif solutions > 0 or hints > 0:
                pedagogy = "MIXED_HINT_SOLUTION_LAYER"
            else:
                pedagogy = "UNSOLVED_EXERCISE_LAYER"

        per_code_blockers[code].extend(local)
        chapter_rows.append({
            "chapter_code": code,
            "canonical_path": active_rel or declared_path or "-",
            "file_exists": "YES" if cp and cp.exists() else "NO",
            "bytes": size,
            "sections": sections,
            "labels": labels,
            "theorem_like": theorem_like,
            "problems": problems,
            "exercises": exercises,
            "hints": hints,
            "solutions": solutions,
            "pedagogy_layer": pedagogy,
            "figure_inputs": figure_inputs,
            "mapped_rules_declared": old_mapped,
            "mapped_rules_actual": actual_mapped,
            "chapter_blockers": ";".join(local) if local else "-"
        })

    for code, local in per_code_blockers.items():
        for item in local:
            blockers.append(f"{code}:{item}")

    blockers = sorted(set(blockers))
    result = "PASS" if not blockers else "FAIL"

    # Status ledger is reconciled to the authoritative book include and source map.
    if args.apply_status:
        for r in status_all:
            if r.get("volume") != "VI":
                continue
            code = r["chapter_code"]
            cp = active.get(code)
            if cp and cp.exists():
                r["canonical_path"] = cp.relative_to(repo).as_posix()
                r["mapped_rule_count"] = str(len(source_by_dest.get(code, [])))
                r["status"] = "DRAFTED"
                r["next_action"] = "FREEZE_READY" if result == "PASS" else (
                    "RECONCILE_BLOCKERS" if per_code_blockers.get(code) else "FREEZE_READY"
                )
        write_status(status_path, status_all)

        readme = read_text(readme_path)
        if result == "PASS":
            new_status = "**Status:** All 49 canonical chapters reconciled; freeze/release ready."
        else:
            new_status = "**Status:** All 49 canonical chapters present; reconciliation blockers remain."
        readme = re.sub(r"(?m)^\*\*Status:\*\*.*$", new_status, readme, count=1)
        readme_path.write_text(readme.rstrip() + "\n", encoding="utf-8")

    write_tsv(
        recon / "VOLUME06_CHAPTER_AUDIT.tsv",
        chapter_rows,
        ["chapter_code","canonical_path","file_exists","bytes","sections","labels","theorem_like",
         "problems","exercises","hints","solutions","pedagogy_layer","figure_inputs",
         "mapped_rules_declared","mapped_rules_actual","chapter_blockers"]
    )
    write_tsv(
        recon / "VOLUME06_SOURCE_RULE_RECONCILIATION.tsv",
        source_recon_rows,
        ["chapter_code","source_file","source_block_id","block_kind","source_selector","action",
         "precedence","audit_status","legacy_source_exists","canonical_target","resolution"]
    )
    write_tsv(
        recon / "VOLUME06_REFERENCE_AUDIT.tsv",
        ref_rows,
        ["source_path","ref_kind","label","target_paths","classification"]
    )
    write_tsv(
        recon / "VOLUME06_BUILD_GRAPH.tsv",
        build_edges,
        ["source_path","command","target","resolved_path","classification"]
    )
    write_tsv(
        recon / "VOLUME06_DUPLICATE_LABELS.tsv",
        duplicate_label_rows,
        ["label","owner_count","owner_paths"]
    )

    summary = {
        "status": result,
        "canonical_chapters": len(chapter_rows),
        "active_includes": len(active),
        "status_rows": len(vi_rows),
        "source_rules": len(vi_source),
        "build_graph_tex_files": len(build_files),
        "duplicate_labels": len(duplicate_vi_labels),
        "duplicate_label_examples": duplicate_vi_labels[:20],
        "missing_references": len(missing_refs),
        "build_inventory_pass": build_pass,
        "unresolved_count": len(blockers),
        "unresolved": blockers
    }
    (recon / "VOLUME06_RECONCILIATION_SUMMARY.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    report = [
        "# Volume VI — Canonical Corpus Reconciliation",
        "",
        f"**Result:** {result}",
        "",
        f"- Canonical chapter targets audited: **{len(chapter_rows)}**",
        f"- Active `book.tex` includes: **{len(active)}**",
        f"- Volume VI status rows: **{len(vi_rows)}**",
        f"- Exact SOURCE_MIGRATION rules routed to VI/01–VI/49: **{len(vi_source)}**",
        f"- TeX files in the actual canonical build graph: **{len(build_files)}**",
        f"- Duplicate labels in that build graph: **{len(duplicate_vi_labels)}**",
        f"- Missing references from Volume VI canonical TeX: **{len(missing_refs)}**",
        f"- Existing canonical build inventory: **{'PASS' if build_pass else 'MISSING/FAIL'}**",
        f"- Unresolved blockers: **{len(blockers)}**",
        "",
        "## Status reconciliation",
        "",
        "The 49 active `book.tex` includes are authoritative for canonical chapter paths. "
        "Mapped-rule counts are re-derived from `editorial/SOURCE_MIGRATION.tsv`. "
        "When this audit passes, all 49 rows are normalized to `DRAFTED / FREEZE_READY` "
        "before the separate freeze commit.",
        "",
        "## Pedagogical-layer policy",
        "",
        "Problem, exercise, hint, and solution counts are recorded per chapter. "
        "They are evidence, not an artificial uniform-count requirement: Volume VI contains "
        "chapter-specific solved dossiers and exercise layers built at different stages. "
        "The freeze gate instead requires complete canonical files, source-map accountability, "
        "resolved labels/references, intact figure inputs, clean encoding, and a successful build.",
        "",
        "## Unresolved blockers",
        ""
    ]
    report += [f"- {b}" for b in blockers] if blockers else ["None."]
    (recon / "VOLUME06_RECONCILIATION_REPORT.md").write_text(
        "\n".join(report).rstrip() + "\n", encoding="utf-8"
    )

    # Source-evidence manifest deliberately excludes README/CHAPTER_STATUS because the freeze
    # transition changes those metadata files. It protects the mathematical source corpus.
    manifest_inputs = [
        book_path,
        source_path,
        recon / "reconcile_volume06.py",
        recon / "RECONCILIATION_POLICY.md",
        recon / "VOLUME06_CHAPTER_AUDIT.tsv",
        recon / "VOLUME06_SOURCE_RULE_RECONCILIATION.tsv",
        recon / "VOLUME06_REFERENCE_AUDIT.tsv",
        recon / "VOLUME06_BUILD_GRAPH.tsv",
        recon / "VOLUME06_DUPLICATE_LABELS.tsv",
        recon / "VOLUME06_RECONCILIATION_SUMMARY.json",
        recon / "VOLUME06_RECONCILIATION_REPORT.md"
    ]
    for p in sorted((vol / "chapters").rglob("*")):
        if p.is_file() and p.suffix.lower() in SOURCE_EXTS:
            manifest_inputs.append(p)
    manifest_lines = []
    for p in sorted(set(manifest_inputs), key=lambda x: x.as_posix()):
        if p.exists():
            manifest_lines.append(f"{sha256(p)}  {p.relative_to(repo).as_posix()}")
    (recon / "VOLUME06_RECONCILIATION_MANIFEST.sha256").write_text(
        "\n".join(manifest_lines) + "\n", encoding="utf-8"
    )

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
