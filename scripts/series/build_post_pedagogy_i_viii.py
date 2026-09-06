#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, re, shutil, subprocess
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
    if not path.exists():
        return []
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
            + cp.stdout[-5000:] + "\n" + cp.stderr[-5000:]
        )
    return cp

def pdf_pages(pdf: Path, fallback: int = 0):
    pdfinfo = shutil.which("pdfinfo")
    if pdfinfo:
        try:
            out = run([pdfinfo, str(pdf)]).stdout
            m = re.search(r"(?m)^Pages:\s+(\d+)\s*$", out)
            if m:
                return int(m.group(1)), "pdfinfo"
        except Exception:
            pass
    mutool = shutil.which("mutool")
    if mutool:
        try:
            out = run([mutool, "info", str(pdf)]).stdout
            m = re.search(r"(?im)^Pages:\s*(\d+)\s*$", out)
            if m:
                return int(m.group(1)), "mutool"
        except Exception:
            pass
    data = pdf.read_bytes()
    n = len(re.findall(rb"/Type\s*/Page(?!s)\b", data))
    if n > 0:
        return n, "byte-scan"
    if fallback > 0:
        return fallback, "freeze-fallback"
    return 0, "unknown"

def log_blockers(log: Path, volume: str):
    if not log.exists():
        return [f"{volume}:MISSING_LOG"]
    text = log.read_text(encoding="utf-8-sig", errors="replace")
    blockers = []
    for needle in (
        "LaTeX Warning: There were undefined references",
        "There were undefined citations",
        "multiply defined",
        "Undefined control sequence",
        "Fatal error occurred",
        "Emergency stop",
    ):
        if needle.lower() in text.lower():
            blockers.append(f"{volume}:{needle}")
    return blockers

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--no-clean", action="store_true")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports/series"
    reports.mkdir(parents=True, exist_ok=True)

    freeze_path = reports / "SERIES_PEDAGOGY_FREEZE.json"
    if not freeze_path.exists():
        raise SystemExit("Missing SERIES_PEDAGOGY_FREEZE.json")
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    if freeze.get("status") != "PASS":
        raise SystemExit("Series pedagogy freeze is not PASS")
    freeze_pdf = {r["volume"]: r for r in freeze.get("pdfs", [])}

    latexmk = shutil.which("latexmk")
    if not latexmk:
        raise SystemExit("latexmk was not found on PATH")

    old_pdf_rows = {r.get("volume"): r for r in read_tsv(reports / "PDF_INVENTORY.tsv")}
    old_build_rows = {r.get("volume"): r for r in read_tsv(reports / "BUILD_I_VIII.tsv")}

    build_rows = []
    post_build_rows = []
    pdf_rows = []
    blockers = []

    for volume, number, title, dirname in VOLS:
        vol = repo / "books" / dirname
        book = vol / "book.tex"
        pdf = vol / "book.pdf"
        log = vol / "book.log"
        if not book.exists():
            blockers.append(f"{volume}:MISSING_BOOK_TEX")
            continue

        try:
            if not args.no_clean:
                run([latexmk, "-C", "book.tex"], cwd=vol)
            run([latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error", "book.tex"], cwd=vol)
        except Exception as exc:
            blockers.append(f"{volume}:BUILD_FAILED:{exc}")
            continue

        if not pdf.exists():
            blockers.append(f"{volume}:MISSING_PDF_AFTER_BUILD")
            continue
        if not log.exists():
            blockers.append(f"{volume}:MISSING_LOG_AFTER_BUILD")
            continue

        lb = log_blockers(log, volume)
        blockers += lb

        fallback = int(freeze_pdf.get(volume, {}).get("pdf_pages", 0))
        pages, page_method = pdf_pages(pdf, fallback)
        if pages <= 0:
            blockers.append(f"{volume}:PAGE_COUNT_UNAVAILABLE")

        digest = sha256(pdf)
        rel_pdf = pdf.relative_to(repo).as_posix()
        status = "PASS" if not lb and pages > 0 else "FAIL"

        build_rows.append({
            "volume": volume,
            "volume_dir": dirname,
            "target": "book.tex",
            "kind": "canonical",
            "status": status,
            "pdf": rel_pdf,
            "bytes": pdf.stat().st_size,
            "sha256": digest,
            "error": "-" if status == "PASS" else "log/page-count finding",
        })
        post_build_rows.append({
            "volume": volume,
            "number": number,
            "title": title,
            "volume_dir": dirname,
            "target": "book.tex",
            "clean_build": "NO" if args.no_clean else "YES",
            "status": status,
            "pages": pages,
            "page_count_method": page_method,
            "pdf": rel_pdf,
            "bytes": pdf.stat().st_size,
            "sha256": digest,
            "book_tex_sha256": sha256(book),
        })
        pdf_rows.append({
            "volume": volume,
            "pdf_path": rel_pdf,
            "exists": "YES",
            "pages": pages,
            "bytes": pdf.stat().st_size,
            "sha256": digest,
        })

    if len(build_rows) != 8:
        blockers.append(f"BUILD_ROWS:{len(build_rows)}!=8")
    if len(pdf_rows) != 8:
        blockers.append(f"PDF_ROWS:{len(pdf_rows)}!=8")
    if any(r["status"] != "PASS" for r in build_rows):
        blockers.append("ONE_OR_MORE_BUILD_ROWS_FAIL")

    if blockers:
        print(json.dumps({"status":"FAIL","blocking":blockers}, indent=2, ensure_ascii=False))
        return 5

    # Repair the stale generic series build/PDF inventories with the post-pedagogy state.
    write_tsv(reports / "BUILD_I_VIII.tsv", build_rows,
              ["volume","volume_dir","target","kind","status","pdf","bytes","sha256","error"])
    write_tsv(reports / "PDF_INVENTORY.tsv", pdf_rows,
              ["volume","pdf_path","exists","pages","bytes","sha256"])
    write_tsv(reports / "POST_PEDAGOGY_BUILD_I_VIII.tsv", post_build_rows,
              ["volume","number","title","volume_dir","target","clean_build","status","pages",
               "page_count_method","pdf","bytes","sha256","book_tex_sha256"])
    write_tsv(reports / "POST_PEDAGOGY_PDF_INVENTORY.tsv", pdf_rows,
              ["volume","pdf_path","exists","pages","bytes","sha256"])

    stale_pdf_rows = 0
    stale_build_rows = 0
    comparison = []
    for row in pdf_rows:
        v = row["volume"]
        old = old_pdf_rows.get(v, {})
        stale = (str(old.get("pages","")) != str(row["pages"])
                 or old.get("sha256","") != row["sha256"]
                 or str(old.get("bytes","")) != str(row["bytes"]))
        stale_pdf_rows += int(stale)
        ob = old_build_rows.get(v, {})
        bstale = ob.get("sha256","") != row["sha256"] or str(ob.get("bytes","")) != str(row["bytes"])
        stale_build_rows += int(bstale)
        comparison.append({
            "volume": v,
            "old_pages": old.get("pages",""),
            "new_pages": row["pages"],
            "old_sha256": old.get("sha256",""),
            "new_sha256": row["sha256"],
            "pdf_inventory_refreshed": "YES" if stale else "NO",
            "build_inventory_refreshed": "YES" if bstale else "NO",
        })

    summary = {
        "schema": 1,
        "status": "PASS",
        "scope": "Post-pedagogy clean build harmonization for Volumes I-VIII",
        "volumes": 8,
        "clean_builds": not args.no_clean,
        "stale_pdf_inventory_rows_repaired": stale_pdf_rows,
        "stale_build_inventory_rows_repaired": stale_build_rows,
        "canonical_tex_sources_modified": 0,
        "comparison": comparison,
        "blocking": [],
    }
    (reports / "POST_PEDAGOGY_BUILD_HARMONIZATION.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    md = [
        "# I–VIII post-pedagogy build harmonization",
        "",
        "**Result:** PASS",
        "",
        "- One canonical clean-build contract was applied to all eight `book.tex` targets.",
        "- No manuscript or canonical TeX source is modified by this script.",
        f"- Stale generic PDF inventory rows refreshed: **{stale_pdf_rows} / 8**.",
        f"- Stale generic build inventory rows refreshed: **{stale_build_rows} / 8**.",
        "",
        "This repairs release-evidence drift introduced because the older generic build/PDF",
        "inventories predated the completed pedagogy expansion.",
        "",
    ]
    (reports / "POST_PEDAGOGY_BUILD_HARMONIZATION.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
