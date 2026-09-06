#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, re, shutil, struct, subprocess, tempfile
from pathlib import Path

VOLS = [
    ("I",1,"Linear Algebra","vol01_linear_algebra"),
    ("II",2,"Real Analysis and Topological Foundations","vol02_real_analysis"),
    ("III",3,"Measure, Fourier Analysis, Distributions and PDE","vol03_fourier_distributions_pde"),
    ("IV",4,"Complex Analysis and Riemann Surfaces","vol04_complex_analysis"),
    ("V",5,"Commutative Algebra and Homological Methods","vol05_commutative_algebra"),
    ("VI",6,"Algebraic Geometry and Sheaf Theory","vol06_algebraic_geometry"),
    ("VII",7,"Differential, Riemannian and Hyperbolic Geometry","vol07_differential_geometry"),
    ("VIII",8,"Algebraic Topology","vol08_algebraic_topology"),
]

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def read_tsv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def write_tsv(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

def run(cmd, cwd=None):
    cp = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, errors="replace")
    if cp.returncode != 0:
        raise RuntimeError(
            "Command failed: " + " ".join(map(str, cmd)) + "\n"
            + cp.stdout[-3000:] + "\n" + cp.stderr[-3000:]
        )
    return cp

def numeric_page_sort(path: Path):
    m = re.search(r"(\d+)(?=\.png$)", path.name)
    return int(m.group(1)) if m else 10**9

def render_pdf(pdf: Path, outdir: Path, prefix: str, dpi: int):
    pdftoppm = shutil.which("pdftoppm")
    mutool = shutil.which("mutool")
    gs = shutil.which("gswin64c") or shutil.which("gswin32c") or shutil.which("gs")
    if pdftoppm:
        run([pdftoppm, "-png", "-gray", "-r", str(dpi), str(pdf), str(outdir / prefix)])
        files = sorted(outdir.glob(prefix + "-*.png"), key=numeric_page_sort)
        return "pdftoppm", files
    if mutool:
        pattern = str(outdir / (prefix + "-%04d.png"))
        run([mutool, "draw", "-q", "-r", str(dpi), "-o", pattern, str(pdf)])
        files = sorted(outdir.glob(prefix + "-*.png"), key=numeric_page_sort)
        return "mutool", files
    if gs:
        pattern = str(outdir / (prefix + "-%04d.png"))
        run([gs, "-dSAFER", "-dBATCH", "-dNOPAUSE", "-sDEVICE=pnggray",
             f"-r{dpi}", f"-sOutputFile={pattern}", str(pdf)])
        files = sorted(outdir.glob(prefix + "-*.png"), key=numeric_page_sort)
        return Path(gs).name, files
    raise RuntimeError("No page renderer found. Provide pdftoppm, mutool, or Ghostscript on PATH.")

def extract_text_pages(pdf: Path, outdir: Path, prefix: str):
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        return "NOT_AVAILABLE", []
    target = outdir / (prefix + ".txt")
    run([pdftotext, "-layout", str(pdf), str(target)])
    text = target.read_text(encoding="utf-8", errors="replace")
    parts = text.split("\f")
    if parts and parts[-1] == "":
        parts = parts[:-1]
    return "pdftotext", parts

def png_info(path: Path):
    data = path.read_bytes()[:32]
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return 0, 0
    return struct.unpack(">II", data[16:24])

def expected_from_freeze(repo: Path):
    p = repo / "reports/series/SERIES_PEDAGOGY_FREEZE.json"
    if not p.exists():
        raise RuntimeError("Missing SERIES_PEDAGOGY_FREEZE.json")
    data = json.loads(p.read_text(encoding="utf-8"))
    if data.get("status") != "PASS" or int(data.get("volumes", 0)) != 8 or int(data.get("chapters", 0)) != 256:
        raise RuntimeError("Series pedagogy freeze is not PASS for 8 volumes / 256 chapters")
    rows = {}
    for r in data.get("pdfs", []):
        rows[r["volume"]] = {
            "pages": int(r["pdf_pages"]),
            "sha256": r["pdf_sha256"],
            "bytes": int(r["pdf_bytes"]),
            "source": "SERIES_PEDAGOGY_FREEZE.json",
        }
    if len(rows) != 8:
        raise RuntimeError(f"Series pedagogy freeze contains {len(rows)} PDF rows, expected 8")
    return rows

def expected_from_inventory(repo: Path, rel: str):
    p = repo / rel
    if not p.exists():
        raise RuntimeError(f"Missing expected inventory: {rel}")
    rows = {}
    for r in read_tsv(p):
        rows[r["volume"]] = {
            "pages": int(r["pages"]),
            "sha256": r["sha256"],
            "bytes": int(r["bytes"]),
            "source": rel,
        }
    if len(rows) != 8:
        raise RuntimeError(f"{rel} contains {len(rows)} rows, expected 8")
    return rows

def log_findings(log: Path, volume: str):
    layout = []
    blockers = []
    if not log.exists():
        return layout, [f"{volume}:MISSING_LOG"]
    text = log.read_text(encoding="utf-8-sig", errors="replace")
    hard = [
        "LaTeX Warning: There were undefined references",
        "There were undefined citations",
        "multiply defined",
        "Undefined control sequence",
        "Fatal error occurred",
        "Emergency stop",
    ]
    for needle in hard:
        if needle.lower() in text.lower():
            blockers.append(f"{volume}:LOG:{needle}")

    patterns = [
        (r"Overfull \\hbox \(([-+]?[0-9.]+)pt too wide\)(?:.*?at lines? ([0-9]+)(?:--([0-9]+))?)?", "HBOX"),
        (r"Overfull \\vbox \(([-+]?[0-9.]+)pt too high\)(?:.*?at lines? ([0-9]+)(?:--([0-9]+))?)?", "VBOX"),
    ]
    for rx, kind in patterns:
        for m in re.finditer(rx, text, flags=re.I):
            pt = float(m.group(1))
            layout.append({
                "volume": volume,
                "kind": kind,
                "overfull_pt": f"{pt:.5f}".rstrip("0").rstrip("."),
                "line_start": m.group(2) or "",
                "line_end": m.group(3) or m.group(2) or "",
                "severity": "HIGH" if pt >= 20 else ("MEDIUM" if pt >= 10 else "LOW"),
            })
    return layout, blockers

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--label", default="POST_PEDAGOGY_RENDER")
    ap.add_argument("--dpi", type=int, default=24)
    ap.add_argument("--inventory", default="")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    reports = repo / "reports/series"
    reports.mkdir(parents=True, exist_ok=True)
    label = re.sub(r"[^A-Z0-9_]+", "_", args.label.upper()).strip("_")
    if not label:
        raise SystemExit("Invalid output label")

    try:
        expected = expected_from_inventory(repo, args.inventory) if args.inventory else expected_from_freeze(repo)
    except Exception as exc:
        print(json.dumps({"status": "ENGINE_FAIL", "error": str(exc)}, indent=2))
        return 2

    blockers = []
    page_rows = []
    layout_rows = []
    volume_rows = []
    renderers = set()
    text_tools = set()
    total_pages = 0
    total_rendered = 0
    low_text = 0

    with tempfile.TemporaryDirectory(prefix="math_post_pedagogy_render_") as td:
        temp = Path(td)
        for volume, number, title, dirname in VOLS:
            local_blockers = []
            vol = repo / "books" / dirname
            pdf = vol / "book.pdf"
            log = vol / "book.log"
            exp = expected.get(volume)
            if exp is None:
                local_blockers.append(f"{volume}:EXPECTED_ROW_MISSING")
                blockers += local_blockers
                continue
            if not pdf.exists():
                local_blockers.append(f"{volume}:MISSING_PDF")
                blockers += local_blockers
                continue

            current_sha = sha256(pdf)
            if current_sha != exp["sha256"]:
                local_blockers.append(f"{volume}:PDF_SHA256:{current_sha}!={exp['sha256']}")
            if pdf.stat().st_size != exp["bytes"]:
                # Byte drift is implied by SHA drift but recorded separately for diagnostics.
                local_blockers.append(f"{volume}:PDF_BYTES:{pdf.stat().st_size}!={exp['bytes']}")

            out = temp / f"v{number:02d}"
            out.mkdir()
            try:
                renderer, images = render_pdf(pdf, out, f"v{number:02d}", args.dpi)
            except Exception as exc:
                local_blockers.append(f"{volume}:RENDER_FAILED:{exc}")
                blockers += local_blockers
                continue
            renderers.add(renderer)

            text_tool, text_pages = extract_text_pages(pdf, out, f"v{number:02d}")
            text_tools.add(text_tool)
            expected_pages = int(exp["pages"])
            if len(images) != expected_pages:
                local_blockers.append(f"{volume}:RENDERED_PAGES:{len(images)}!={expected_pages}")
            if text_pages and len(text_pages) not in (expected_pages, expected_pages + 1):
                local_blockers.append(f"{volume}:TEXT_PAGES:{len(text_pages)}!={expected_pages}")

            vol_low_text = 0
            for i, img in enumerate(images, 1):
                width, height = png_info(img)
                size = img.stat().st_size
                chars = ""
                if i <= len(text_pages):
                    chars = len(re.sub(r"\s+", "", text_pages[i-1]))
                classification = "RENDERED_OK"
                if size < 100 or width <= 0 or height <= 0:
                    classification = "RENDER_INVALID"
                    local_blockers.append(f"{volume}:PAGE_{i}:INVALID_RENDER")
                elif chars != "" and chars < 20:
                    classification = "LOW_TEXT_REVIEW"
                    vol_low_text += 1
                    low_text += 1
                page_rows.append({
                    "volume": volume,
                    "page": i,
                    "raster_width": width,
                    "raster_height": height,
                    "raster_bytes": size,
                    "text_chars": chars,
                    "classification": classification,
                })

            lw, lb = log_findings(log, volume)
            layout_rows += lw
            local_blockers += lb
            blockers += local_blockers
            total_pages += expected_pages
            total_rendered += len(images)
            volume_rows.append({
                "volume": volume,
                "title": title,
                "expected_source": exp["source"],
                "expected_pages": expected_pages,
                "rendered_pages": len(images),
                "pdf_bytes": pdf.stat().st_size,
                "pdf_sha256": current_sha,
                "renderer": renderer,
                "text_extractor": text_tool,
                "low_text_review_pages": vol_low_text,
                "overfull_boxes": len(lw),
                "overfull_ge_20pt": sum(float(r["overfull_pt"]) >= 20 for r in lw),
                "status": "PASS" if not local_blockers else "FAIL",
            })

    if len(volume_rows) != 8:
        blockers.append(f"VOLUME_ROWS:{len(volume_rows)}!=8")
    if total_rendered != total_pages:
        blockers.append(f"TOTAL_RENDERED:{total_rendered}!={total_pages}")

    summary = {
        "schema": 1,
        "status": "PASS" if not blockers else "FAIL",
        "label": label,
        "volumes": len(volume_rows),
        "pdf_pages": total_pages,
        "rendered_pages": total_rendered,
        "renderers": sorted(renderers),
        "text_extractors": sorted(text_tools),
        "low_text_review_candidates": low_text,
        "overfull_boxes": len(layout_rows),
        "overfull_ge_20pt": sum(float(r["overfull_pt"]) >= 20 for r in layout_rows),
        "blocking": blockers,
        "human_rendered_review_required": True,
    }

    write_tsv(reports / f"{label}_PAGE_PROOF.tsv", page_rows, [
        "volume","page","raster_width","raster_height","raster_bytes","text_chars","classification"
    ])
    write_tsv(reports / f"{label}_LAYOUT_WARNINGS.tsv", layout_rows, [
        "volume","kind","overfull_pt","line_start","line_end","severity"
    ])
    write_tsv(reports / f"{label}_VOLUME_PROOF.tsv", volume_rows, [
        "volume","title","expected_source","expected_pages","rendered_pages","pdf_bytes","pdf_sha256",
        "renderer","text_extractor","low_text_review_pages","overfull_boxes","overfull_ge_20pt","status"
    ])
    (reports / f"{label}_AUDIT.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    md = [
        f"# I–VIII post-pedagogy rendered QA — {label}",
        "",
        f"**Automated result:** {summary['status']}",
        "",
        f"- Volumes: **{summary['volumes']} / 8**",
        f"- Expected PDF pages: **{summary['pdf_pages']}**",
        f"- Rasterized pages: **{summary['rendered_pages']}**",
        f"- Renderers: **{', '.join(summary['renderers']) or 'none'}**",
        f"- Low-text pages queued for human review: **{summary['low_text_review_candidates']}**",
        f"- Overfull boxes inventoried: **{summary['overfull_boxes']}**",
        f"- Overfull boxes >=20pt: **{summary['overfull_ge_20pt']}**",
        "",
        "## Policy",
        "",
        "Low-text pages and overfull boxes are review candidates, not automatic release blockers.",
        "Broken page rendering, PDF/hash drift against the selected expected inventory, and",
        "undefined-reference/citation/multiply-defined or fatal LaTeX log findings are blocking.",
        "",
        "The final v1.2 release remains gated on a separate human rendered-proof freeze.",
        "",
        "## Blocking findings",
        "",
    ]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (reports / f"{label}_AUDIT.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    # Findings are persisted even when FAIL; the launcher decides whether to continue.
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
