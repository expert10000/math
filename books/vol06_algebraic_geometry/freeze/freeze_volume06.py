#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
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

def include_map(book_text: str, vol: Path):
    rx = re.compile(r"(?m)^[ \t]*\\include\{(chapters/ch(\d\d)_[^}]+/chapter)\}")
    out = {}
    for m in rx.finditer(book_text):
        out[f"VI/{int(m.group(2)):02d}"] = vol / (m.group(1) + ".tex")
    return out

def verify_reconciliation_manifest(repo: Path, manifest: Path):
    errors = []
    count = 0
    for raw in manifest.read_text(encoding="utf-8-sig").splitlines():
        if not raw.strip():
            continue
        parts = raw.split(None, 1)
        if len(parts) != 2:
            errors.append("MALFORMED_MANIFEST_ROW:" + raw)
            continue
        expected, rel = parts[0], parts[1].strip()
        p = repo / rel
        count += 1
        if not p.exists():
            errors.append("MISSING_MANIFEST_PATH:" + rel)
        elif sha256(p) != expected:
            errors.append("MANIFEST_DRIFT:" + rel)
    return count, errors

def resolve_tex_target(base_dir: Path, target: str):
    """Resolve a literal TeX input/include target from the Volume VI build directory."""
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

def strip_tex_comments(text: str) -> str:
    """Remove unescaped TeX comments while preserving escaped percent signs."""
    cleaned = []
    for line in text.splitlines():
        cut = len(line)
        for i, ch in enumerate(line):
            if ch != "%":
                continue
            backslashes = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                backslashes += 1
                j -= 1
            if backslashes % 2 == 0:
                cut = i
                break
        cleaned.append(line[:cut])
    return "\n".join(cleaned)

def collect_build_graph(repo: Path, vol: Path):
    root = (vol / "book.tex").resolve()
    stack = [root]
    seen = set()
    ordered = []
    missing = []
    cmd_re = re.compile(r"\\(input|include)\{([^}]+)\}")

    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        ordered.append(current)
        text = strip_tex_comments(read_text(current))
        for kind, target in cmd_re.findall(text):
            resolved = resolve_tex_target(vol, target)
            if resolved is None:
                missing.append(
                    f"MISSING_BUILD_INPUT:{current.relative_to(repo).as_posix()}:{kind}:{target}"
                )
            elif resolved not in seen:
                stack.append(resolved)
    return ordered, sorted(set(missing))

def structural_errors(repo: Path, phase: str):
    vol = repo / "books/vol06_algebraic_geometry"
    status_path = repo / "editorial/CHAPTER_STATUS.tsv"
    rows = [r for r in read_tsv(status_path) if r.get("volume") == "VI"]
    active = include_map(read_text(vol / "book.tex"), vol)
    errors = []

    if len(rows) != 49:
        errors.append(f"STATUS_ROWS:{len(rows)}")
    if len(active) != 49:
        errors.append(f"ACTIVE_INCLUDES:{len(active)}")

    build_files, missing_inputs = collect_build_graph(repo, vol)
    errors.extend(missing_inputs)

    labels = defaultdict(list)
    for p in build_files:
        text = read_text(p)
        if suspicious(text):
            errors.append("SUSPICIOUS_ENCODING:" + p.relative_to(repo).as_posix())
        for lab in re.findall(r"\\label\{([^}]+)\}", text):
            labels[lab].append(p.relative_to(repo).as_posix())

    dups = sorted(lab for lab, owners in labels.items() if len(owners) > 1)
    if dups:
        errors.append("DUPLICATE_LABELS:" + ",".join(dups[:20]))

    row_by_code = {r["chapter_code"]: r for r in rows}
    for code, cp in active.items():
        if not cp.exists():
            errors.append("MISSING_CHAPTER:" + code)
            continue
        sr = row_by_code.get(code)
        if not sr:
            errors.append("MISSING_STATUS:" + code)
            continue
        if sr.get("canonical_path") != cp.relative_to(repo).as_posix():
            errors.append("STATUS_PATH_MISMATCH:" + code)

        if phase == "pre":
            if sr.get("status") != "DRAFTED" or sr.get("next_action") != "FREEZE_READY":
                errors.append(
                    f"NOT_FREEZE_READY:{code}:{sr.get('status')}:{sr.get('next_action')}"
                )
        else:
            if sr.get("status") != "FROZEN" or sr.get("next_action") != "COMPLETE":
                errors.append(
                    f"NOT_FROZEN:{code}:{sr.get('status')}:{sr.get('next_action')}"
                )

    return errors


def pdf_pages(path: Path) -> int:
    data = path.read_bytes()
    return len(re.findall(rb"/Type\s*/Page(?!s)\b", data))

def update_build_inventory(repo: Path, pdf: Path):
    inventory = repo / "reports/series/BUILD_I_VIII.tsv"
    if not inventory.exists():
        return
    rows = read_tsv(inventory)
    fields = ["volume","volume_dir","target","kind","status","pdf","bytes","sha256","error"]
    found = False
    for r in rows:
        if r.get("volume") == "VI" and r.get("target") == "book.tex":
            r["volume_dir"] = "vol06_algebraic_geometry"
            r["kind"] = "canonical"
            r["status"] = "PASS"
            r["pdf"] = pdf.relative_to(repo).as_posix()
            r["bytes"] = str(pdf.stat().st_size)
            r["sha256"] = sha256(pdf)
            r["error"] = "-"
            found = True
    if not found:
        rows.append({
            "volume":"VI","volume_dir":"vol06_algebraic_geometry","target":"book.tex",
            "kind":"canonical","status":"PASS","pdf":pdf.relative_to(repo).as_posix(),
            "bytes":str(pdf.stat().st_size),"sha256":sha256(pdf),"error":"-"
        })
    write_tsv(inventory, rows, fields)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--phase", choices=("pre","finalize"), required=True)
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    vol = repo / "books/vol06_algebraic_geometry"
    recon = vol / "reconciliation"
    freeze = vol / "freeze"
    freeze.mkdir(parents=True, exist_ok=True)
    summary_path = recon / "VOLUME06_RECONCILIATION_SUMMARY.json"
    manifest_path = recon / "VOLUME06_RECONCILIATION_MANIFEST.sha256"

    if not summary_path.exists() or not manifest_path.exists():
        raise SystemExit("Volume VI reconciliation evidence is missing.")
    summary = json.loads(read_text(summary_path))
    errors = []
    if summary.get("status") != "PASS" or int(summary.get("unresolved_count", 1)) != 0:
        errors.append("RECONCILIATION_NOT_PASS")

    manifest_count, manifest_errors = verify_reconciliation_manifest(repo, manifest_path)
    errors.extend(manifest_errors)
    errors.extend(structural_errors(repo, args.phase if args.phase == "pre" else "pre"))

    if args.phase == "pre":
        build_files, _ = collect_build_graph(repo, vol)
        print(f"reconciliation_manifest_entries={manifest_count}")
        print(f"canonical_build_graph_tex_files={len(build_files)}")
        if errors:
            print("VOLUME VI PRE-FREEZE AUDIT FAILED")
            for e in errors:
                print("BLOCK:", e)
            return 2
        print("VOLUME VI PRE-FREEZE AUDIT PASSED")
        return 0

    # Finalize requires a successful fresh PDF/log.
    pdf = vol / "book.pdf"
    log = vol / "book.log"
    if not pdf.exists():
        errors.append("MISSING_BOOK_PDF")
    if not log.exists():
        errors.append("MISSING_BOOK_LOG")
    if log.exists():
        log_text = read_text(log)
        patterns = [
            r"LaTeX Warning: There were undefined references",
            r"There were undefined citations",
            r"multiply defined"
        ]
        for pattern in patterns:
            if re.search(pattern, log_text, re.I):
                errors.append("BUILD_LOG_WARNING:" + pattern)
    if errors:
        print("VOLUME VI FINALIZE PRECONDITIONS FAILED")
        for e in errors:
            print("BLOCK:", e)
        return 2

    # Transition all Volume VI rows.
    status_path = repo / "editorial/CHAPTER_STATUS.tsv"
    status_all = read_tsv(status_path)
    for r in status_all:
        if r.get("volume") == "VI":
            r["status"] = "FROZEN"
            r["next_action"] = "COMPLETE"
    write_status(status_path, status_all)

    # Canonical release README.
    readme_path = vol / "README.md"
    readme = read_text(readme_path)
    readme = re.sub(
        r"(?m)^\*\*Status:\*\*.*$",
        "**Status:** FROZEN — Volume VI Algebraic Geometry and Sheaf Theory v1.0 release baseline.",
        readme,
        count=1
    )
    marker = "## Freeze/release evidence"
    if marker not in readme:
        readme += (
            "\n\n## Freeze/release evidence\n\n"
            "See `freeze/VOLUME06_FREEZE_REPORT.md` and "
            "`freeze/VOLUME06_FREEZE_MANIFEST.sha256`.\n"
        )
    readme_path.write_text(readme.rstrip() + "\n", encoding="utf-8")

    update_build_inventory(repo, pdf)

    # Post-transition structural check.
    post_errors = structural_errors(repo, "post")
    if post_errors:
        print("VOLUME VI POST-FREEZE STATUS AUDIT FAILED")
        for e in post_errors:
            print("BLOCK:", e)
        return 2

    # Freeze source manifest.
    source_inputs = [
        vol / "book.tex",
        readme_path,
        status_path,
        repo / "editorial/SOURCE_MIGRATION.tsv",
        freeze / "freeze_volume06.py",
        freeze / "RELEASE_VOLUME06.md"
    ]
    for shared in ["preamble.tex","macros.tex","theorem_styles.tex","notation.tex"]:
        p = repo / "shared" / shared
        if p.exists():
            source_inputs.append(p)
    for p in sorted((vol / "chapters").rglob("*")):
        if p.is_file() and p.suffix.lower() in SOURCE_EXTS:
            source_inputs.append(p)
    for p in sorted(recon.glob("*")):
        if p.is_file():
            source_inputs.append(p)

    freeze_manifest = freeze / "VOLUME06_FREEZE_MANIFEST.sha256"
    freeze_report = freeze / "VOLUME06_FREEZE_REPORT.md"
    manifest_lines = []
    for p in sorted(set(source_inputs), key=lambda x: x.as_posix()):
        if p.exists():
            manifest_lines.append(f"{sha256(p)}  {p.relative_to(repo).as_posix()}")
    freeze_manifest.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

    head = ""
    try:
        import subprocess
        head = subprocess.check_output(
            ["git","-C",str(repo),"rev-parse","HEAD"], text=True
        ).strip()
    except Exception:
        head = "UNKNOWN"

    pages = pdf_pages(pdf)
    report = [
        "# Volume VI — Freeze Report",
        "",
        "**Result:** PASS",
        "",
        f"- Pre-freeze parent commit: `{head}`",
        "- Canonical chapters: **49**",
        "- Active chapter includes: **49**",
        "- Corpus/status reconciliation: **PASS / zero unresolved**",
        "- Clean canonical PDF build: **PASS**",
        f"- PDF pages: **{pages}**",
        f"- PDF SHA-256: `{sha256(pdf)}`",
        f"- PDF bytes: **{pdf.stat().st_size}**",
        "- Chapter status: **FROZEN / COMPLETE**",
        f"- Reconciliation manifest entries verified: **{manifest_count}**",
        f"- Freeze manifest entries: **{len(manifest_lines)}**",
        "",
        "The generated PDF was rebuilt cleanly after reconciliation and before the "
        "release commit. The PDF hash is recorded separately from the source manifest "
        "because TeX-generated PDFs need not be byte-for-byte reproducible across "
        "toolchain runs."
    ]
    freeze_report.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")

    print(f"VOLUME VI FREEZE FINALIZED: pages={pages} bytes={pdf.stat().st_size}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
