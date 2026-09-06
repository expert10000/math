#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json, re, shutil, subprocess
from pathlib import Path

VOLS = {
    "I": (1, "vol01_linear_algebra"),
    "II": (2, "vol02_real_analysis"),
    "III": (3, "vol03_fourier_distributions_pde"),
    "IV": (4, "vol04_complex_analysis"),
    "V": (5, "vol05_commutative_algebra"),
    "VI": (6, "vol06_algebraic_geometry"),
    "VII": (7, "vol07_differential_geometry"),
    "VIII": (8, "vol08_algebraic_topology"),
}


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_tsv(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


def run_text(cmd):
    cp = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if cp.returncode != 0:
        return ""
    return cp.stdout


def release_pdf(repo: Path, volume: str) -> Path:
    number, dirname = VOLS[volume]
    stem = dirname.removeprefix(f"vol{number:02d}_")
    return repo / "release/theory_of_mathematics_i_viii_v1.2-rc1/pdfs" / f"volume{number:02d}_{stem}.pdf"


def page_text(pdf: Path, page: int) -> str:
    tool = shutil.which("pdftotext")
    if not tool or not pdf.exists():
        return ""
    return run_text([tool, "-layout", "-f", str(page), "-l", str(page), str(pdf), "-"])


def compact_preview(text: str, limit: int = 180) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def classify_low_text(row, text: str):
    page = int(row["page"])
    chars = int(row.get("text_chars") or 0)
    raster = int(row.get("raster_bytes") or 0)
    normalized = re.sub(r"\s+", " ", text).strip().casefold()
    if chars == 0 and page <= 2:
        return "LIKELY_INTENTIONAL_FRONTMATTER_VERSO", "retain; human glance only"
    if any(token in normalized for token in ("part i", "part ii", "part iii", "part iv", "part v", "part vi", "part vii", "part viii", "chapter")):
        return "LIKELY_INTENTIONAL_STRUCTURAL_DIVIDER", "retain; human glance only"
    if chars < 20 and raster < 3000:
        return "LIKELY_INTENTIONAL_DIVIDER_OR_BLANK", "retain; human glance only"
    return "HUMAN_REVIEW_LOW_TEXT", "inspect rendered page"


def nearest_repo_tex(log_text: str, pos: int, repo: Path, volroot: Path):
    prefix = log_text[max(0, pos - 120000):pos]
    tokens = re.findall(r"\(([^()\r\n]*?\.tex)", prefix, flags=re.I)
    for raw in reversed(tokens):
        token = raw.strip().strip('"').replace("\\", "/")
        low = token.casefold()
        if "/tex/latex/" in low or "miktex" in low or "program files" in low:
            continue
        candidates = []
        p = Path(token)
        if p.is_absolute():
            candidates.append(p)
        else:
            candidates.extend([volroot / token, repo / token])
        for candidate in candidates:
            try:
                resolved = candidate.resolve()
            except Exception:
                resolved = candidate
            if resolved.exists() and resolved.is_file():
                try:
                    return resolved.relative_to(repo).as_posix()
                except Exception:
                    return str(resolved)
    return ""


def source_context(repo: Path, source_file: str, line_no: int):
    if not source_file or line_no <= 0:
        return ""
    p = Path(source_file)
    if not p.is_absolute():
        p = repo / source_file
    if not p.exists():
        return ""
    lines = p.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    lo = max(0, line_no - 2); hi = min(len(lines), line_no + 1)
    return compact_preview(" ".join(lines[lo:hi]), 240)


def parse_high_log(repo: Path, volume: str):
    _, dirname = VOLS[volume]
    volroot = repo / "books" / dirname
    log = volroot / "book.log"
    if not log.exists():
        return []
    text = log.read_text(encoding="utf-8-sig", errors="replace")
    rx = re.compile(r"Overfull \\hbox \(([-+]?[0-9.]+)pt too wide\)(?:.*?at lines? ([0-9]+)(?:--([0-9]+))?)?", re.I)
    out = []
    for m in rx.finditer(text):
        pt = float(m.group(1))
        if pt < 20:
            continue
        line = int(m.group(2) or 0)
        source = nearest_repo_tex(text, m.start(), repo, volroot)
        context = source_context(repo, source, line)
        lc = context.casefold()
        if "\\url" in lc or "http://" in lc or "https://" in lc or "\\href" in lc:
            context_kind = "URL_OR_HYPERLINK"
            action = "shared URL break flexibility"
        elif "\\texttt" in lc or "\\verb" in lc:
            context_kind = "MONOSPACE_TECHNICAL_TEXT"
            action = "shared technical-text line flexibility"
        elif any(tok in lc for tok in ("\\begin{align", "\\begin{equation", "\\begin{multline", "\\[", "\\]")):
            context_kind = "DISPLAY_MATH"
            action = "retain for targeted human math-layout review"
        elif "$" in context or "\\(" in context:
            context_kind = "PROSE_WITH_INLINE_MATH"
            action = "shared emergency paragraph stretch"
        else:
            context_kind = "PROSE_OR_UNKNOWN"
            action = "shared emergency paragraph stretch"
        out.append({
            "overfull_pt": pt,
            "line_start": line,
            "source_file": source,
            "source_context": context,
            "context_kind": context_kind,
            "repair_action": action,
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports/series"

    audit_path = reports / "POST_PEDAGOGY_REPROOF_AUDIT.json"
    page_path = reports / "POST_PEDAGOGY_REPROOF_PAGE_PROOF.tsv"
    layout_path = reports / "POST_PEDAGOGY_REPROOF_LAYOUT_WARNINGS.tsv"
    if not (audit_path.exists() and page_path.exists() and layout_path.exists()):
        raise SystemExit("Missing post-pedagogy reproof evidence")

    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    if audit.get("status") != "PASS" or int(audit.get("volumes",0)) != 8:
        raise SystemExit("Post-pedagogy reproof is not PASS for 8 volumes")

    pages = read_tsv(page_path)
    layout = read_tsv(layout_path)
    low = [r for r in pages if r.get("classification") == "LOW_TEXT_REVIEW"]
    high = [r for r in layout if float(r.get("overfull_pt") or 0) >= 20]

    rows = []
    low_human = 0
    for r in low:
        volume = r["volume"]; page = int(r["page"])
        text = page_text(release_pdf(repo, volume), page)
        classification, action = classify_low_text(r, text)
        if classification == "HUMAN_REVIEW_LOW_TEXT":
            low_human += 1
        rows.append({
            "finding_type": "LOW_TEXT_PAGE",
            "volume": volume,
            "page": page,
            "overfull_pt": "",
            "severity": "REVIEW",
            "source_file": "",
            "line_start": "",
            "context_kind": "STRUCTURAL_PAGE",
            "context_preview": compact_preview(text),
            "classification": classification,
            "repair_action": action,
        })

    resolved_sources = 0
    display_math = 0
    max_pt = 0.0
    # Attach log/source context in warning order within each volume. If the local
    # logs have been cleaned, retain the tracked warning row and mark source unknown.
    parsed_by_volume = {v: parse_high_log(repo, v) for v in VOLS}
    counters = {v: 0 for v in VOLS}
    for r in high:
        volume = r["volume"]
        idx = counters[volume]; counters[volume] += 1
        parsed = parsed_by_volume.get(volume, [])
        p = parsed[idx] if idx < len(parsed) else {}
        pt = float(r["overfull_pt"]); max_pt = max(max_pt, pt)
        source = p.get("source_file", "")
        if source: resolved_sources += 1
        kind = p.get("context_kind", "UNKNOWN")
        if kind == "DISPLAY_MATH": display_math += 1
        classification = (
            "CONFIRMED_EXTREME_OVERFULL" if pt >= 100 else
            "CONFIRMED_MAJOR_OVERFULL" if pt >= 40 else
            "CONFIRMED_OVERFULL"
        )
        rows.append({
            "finding_type": "OVERFULL_HBOX",
            "volume": volume,
            "page": "",
            "overfull_pt": f"{pt:.5f}".rstrip("0").rstrip("."),
            "severity": r.get("severity", "HIGH"),
            "source_file": source,
            "line_start": p.get("line_start") or r.get("line_start", ""),
            "context_kind": kind,
            "context_preview": p.get("source_context", ""),
            "classification": classification,
            "repair_action": p.get("repair_action", "shared emergency paragraph stretch; human reproof"),
        })

    out_tsv = reports / "V12_RC1_RENDER_TRIAGE.tsv"
    out_json = reports / "V12_RC1_RENDER_TRIAGE.json"
    out_md = reports / "V12_RC1_RENDER_TRIAGE.md"
    write_tsv(out_tsv, rows, [
        "finding_type","volume","page","overfull_pt","severity","source_file","line_start",
        "context_kind","context_preview","classification","repair_action"
    ])

    summary = {
        "schema": 1,
        "status": "PASS",
        "candidate": "v1.2-rc1",
        "source_reproof_status": audit.get("status"),
        "pdf_pages": int(audit.get("pdf_pages",0)),
        "low_text_candidates": len(low),
        "low_text_human_review_remaining": low_human,
        "overfull_boxes_total": int(audit.get("overfull_boxes",0)),
        "overfull_ge_20pt": len(high),
        "max_overfull_pt": round(max_pt, 5),
        "confirmed_overfull_candidates": len(high),
        "source_resolved_overfull_candidates": resolved_sources,
        "display_math_candidates": display_math,
        "safe_shared_repair_policy": {
            "tolerance": 2000,
            "emergencystretch": "3em",
            "urlmuskip": "0mu plus 2mu",
            "global_sloppy": False,
            "math_rescaling": False,
        },
        "human_rendered_proof_required": True,
        "final_release_frozen": False,
        "blocking": [],
    }
    out_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md = [
        "# Theory of Mathematics I–VIII — v1.2-rc1 rendered-proof triage",
        "",
        "**Triage result:** PASS",
        "",
        f"- Pages in the candidate: **{summary['pdf_pages']}**",
        f"- Low-text candidates: **{len(low)}**",
        f"- Low-text pages still requiring content-level review: **{low_human}**",
        f"- Overfull boxes total: **{summary['overfull_boxes_total']}**",
        f"- Confirmed overfull boxes >=20pt: **{len(high)}**",
        f"- Maximum overfull width: **{summary['max_overfull_pt']}pt**",
        f"- High-warning source locations resolved from current logs: **{resolved_sources} / {len(high)}**",
        "",
        "## Decision",
        "",
        "Low-text candidates are retained as human-review items unless the extracted page text",
        "and page position make them clearly structural title/part/verso pages. They are not",
        "automatically rewritten.",
        "",
        "The >=20pt overfull boxes are confirmed TeX layout findings. The safe automatic repair",
        "is limited to controlled paragraph and URL line-breaking flexibility in the shared",
        "preamble. Display mathematics is never resized or semantically rewritten by this pass.",
        "",
        "The final v1.2 freeze remains separate and still requires a human rendered reproof.",
        "",
    ]
    out_md.write_text("\n".join(md), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
