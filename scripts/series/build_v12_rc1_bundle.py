#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, shutil, subprocess
from collections import Counter
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

EVIDENCE = [
    "reports/series/SERIES_PEDAGOGY_FREEZE.json",
    "reports/series/SERIES_PEDAGOGY_FREEZE.md",
    "reports/series/SERIES_PEDAGOGY_COUNTS.tsv",
    "reports/series/SERIES_PEDAGOGY_HASHES.tsv",
    "reports/series/SERIES_PEDAGOGY_CROSS_VOLUME.json",
    "reports/series/SERIES_PEDAGOGY_CROSS_VOLUME.md",
    "reports/series/SERIES_PEDAGOGY_RELEASE_HASHES.tsv",
    "reports/series/POST_PEDAGOGY_RENDER_PAGE_PROOF.tsv",
    "reports/series/POST_PEDAGOGY_RENDER_LAYOUT_WARNINGS.tsv",
    "reports/series/POST_PEDAGOGY_RENDER_VOLUME_PROOF.tsv",
    "reports/series/POST_PEDAGOGY_RENDER_AUDIT.json",
    "reports/series/POST_PEDAGOGY_RENDER_AUDIT.md",
    "reports/series/POST_PEDAGOGY_BUILD_I_VIII.tsv",
    "reports/series/POST_PEDAGOGY_PDF_INVENTORY.tsv",
    "reports/series/POST_PEDAGOGY_BUILD_HARMONIZATION.json",
    "reports/series/POST_PEDAGOGY_BUILD_HARMONIZATION.md",
    "reports/series/POST_PEDAGOGY_REPROOF_PAGE_PROOF.tsv",
    "reports/series/POST_PEDAGOGY_REPROOF_LAYOUT_WARNINGS.tsv",
    "reports/series/POST_PEDAGOGY_REPROOF_VOLUME_PROOF.tsv",
    "reports/series/POST_PEDAGOGY_REPROOF_AUDIT.json",
    "reports/series/POST_PEDAGOGY_REPROOF_AUDIT.md",
    "reports/series/BUILD_I_VIII.tsv",
    "reports/series/PDF_INVENTORY.tsv",
    "reports/series/GLOBAL_SERIES_RECONCILIATION.json",
    "reports/series/GLOBAL_SERIES_RECONCILIATION.md",
    "reports/series/DOSSIER_INDEX_SUMMARY.json",
    "reports/series/CROSS_VOLUME_NAVIGATION_SUMMARY.json",
]

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def read_tsv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def write_tsv(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

def copy(src: Path, dst: Path):
    if not src.exists():
        raise RuntimeError(f"Missing release evidence: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

def git_head(repo: Path) -> str:
    cp = subprocess.run(["git","rev-parse","HEAD"], cwd=repo, capture_output=True, text=True, errors="replace")
    return cp.stdout.strip() if cp.returncode == 0 else ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--release-name", default="theory_of_mathematics_i_viii_v1.2-rc1")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports/series"

    freeze = read_json(reports / "SERIES_PEDAGOGY_FREEZE.json")
    initial = read_json(reports / "POST_PEDAGOGY_RENDER_AUDIT.json")
    reproof = read_json(reports / "POST_PEDAGOGY_REPROOF_AUDIT.json")
    harmon = read_json(reports / "POST_PEDAGOGY_BUILD_HARMONIZATION.json")
    cross = read_json(reports / "SERIES_PEDAGOGY_CROSS_VOLUME.json")
    if freeze.get("status") != "PASS":
        raise SystemExit("Series pedagogy freeze is not PASS")
    if initial.get("status") != "PASS":
        raise SystemExit("Initial post-pedagogy rendered audit is not PASS")
    if reproof.get("status") != "PASS":
        raise SystemExit("Post-harmonization rendered reproof is not PASS")
    if harmon.get("status") != "PASS":
        raise SystemExit("Post-pedagogy build harmonization is not PASS")
    if cross.get("status") != "PASS":
        raise SystemExit("Cross-volume pedagogy reconciliation is not PASS")

    pdfinv = {r["volume"]: r for r in read_tsv(reports / "POST_PEDAGOGY_PDF_INVENTORY.tsv")}
    build = {r["volume"]: r for r in read_tsv(reports / "POST_PEDAGOGY_BUILD_I_VIII.tsv")}
    if len(pdfinv) != 8 or len(build) != 8:
        raise SystemExit("Post-pedagogy build/PDF inventory is incomplete")
    if any(r.get("status") != "PASS" for r in build.values()):
        raise SystemExit("One or more post-pedagogy build rows are not PASS")

    out = repo / "release" / args.release_name
    if out.exists():
        raise SystemExit(f"Release directory already exists: {out}")
    (out / "pdfs").mkdir(parents=True)
    (out / "evidence").mkdir(parents=True)
    (out / "manifests").mkdir(parents=True)

    freeze_pdf = {r["volume"]: r for r in freeze.get("pdfs", [])}
    pdf_rows = []
    source_rows = []
    for volume, number, title, dirname in VOLS:
        src = repo / "books" / dirname / "book.pdf"
        if not src.exists():
            raise SystemExit(f"Missing canonical PDF for {volume}")
        inv = pdfinv[volume]
        digest = sha256(src)
        if digest != inv["sha256"]:
            raise SystemExit(f"{volume} PDF hash drifted after rendered reproof")
        dst = out / "pdfs" / f"volume{number:02d}_{dirname.removeprefix(f'vol{number:02d}_')}.pdf"
        shutil.copy2(src, dst)
        pdf_rows.append({
            "volume": volume,
            "number": number,
            "title": title,
            "pages": inv["pages"],
            "bytes": src.stat().st_size,
            "sha256": digest,
            "release_pdf": dst.relative_to(out).as_posix(),
        })

        fr = freeze_pdf.get(volume, {})
        book_sha = fr.get("book_tex_sha256","")
        ledger_sha = fr.get("volume_hash_ledger_sha256","")
        recon_sha = fr.get("volume_reconciliation_sha256","")
        aggregate = sha_text("\0".join([book_sha, ledger_sha, recon_sha]))
        source_rows.append({
            "volume": volume,
            "number": number,
            "title": title,
            "chapters": fr.get("chapters",""),
            "book_tex_sha256": book_sha,
            "volume_hash_ledger_sha256": ledger_sha,
            "volume_reconciliation_sha256": recon_sha,
            "source_aggregate_sha256": aggregate,
        })

    write_tsv(out / "manifests/PDFS.tsv", pdf_rows,
              ["volume","number","title","pages","bytes","sha256","release_pdf"])
    write_tsv(out / "manifests/SOURCE_BASELINES.tsv", source_rows,
              ["volume","number","title","chapters","book_tex_sha256","volume_hash_ledger_sha256",
               "volume_reconciliation_sha256","source_aggregate_sha256"])

    for rel in EVIDENCE:
        srcp = repo / rel
        copy(srcp, out / "evidence" / srcp.name)

    source_commit = git_head(repo)
    review = {
        "initial_low_text": int(initial.get("low_text_review_candidates",0)),
        "initial_overfull": int(initial.get("overfull_boxes",0)),
        "initial_overfull_ge_20pt": int(initial.get("overfull_ge_20pt",0)),
        "reproof_low_text": int(reproof.get("low_text_review_candidates",0)),
        "reproof_overfull": int(reproof.get("overfull_boxes",0)),
        "reproof_overfull_ge_20pt": int(reproof.get("overfull_ge_20pt",0)),
    }
    release_meta = {
        "schema": 2,
        "release": "Theory of Mathematics I–VIII v1.2 RC1",
        "tag": "theory-of-mathematics-i-viii-v1.2-rc1",
        "source_commit_before_rc_commit": source_commit,
        "volumes": 8,
        "chapters": 256,
        "pedagogy_integration": {
            "status": freeze.get("status"),
            "series_totals": freeze.get("series_totals"),
            "aggregate_release_sha256": freeze.get("evidence_hashes",{}).get("aggregate_release_sha256"),
        },
        "post_pedagogy_initial_render_audit": initial,
        "post_pedagogy_build_harmonization": {
            "status": harmon.get("status"),
            "stale_pdf_inventory_rows_repaired": harmon.get("stale_pdf_inventory_rows_repaired"),
            "stale_build_inventory_rows_repaired": harmon.get("stale_build_inventory_rows_repaired"),
        },
        "post_pedagogy_rendered_reproof": reproof,
        "review_queue": review,
        "pdfs": pdf_rows,
        "source_baselines": source_rows,
        "evidence_sources": EVIDENCE,
        "automated_rc_status": "PASS",
        "human_rendered_proof_required": True,
        "final_release_frozen": False,
        "release_decision": "PENDING_HUMAN_RENDERED_REPROOF",
    }
    (out / "RELEASE.json").write_text(
        json.dumps(release_meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    notes = [
        "# Theory of Mathematics I–VIII — v1.2 RC1",
        "",
        "This release candidate is the first whole-series candidate built after the",
        "worked-example and graded-exercise pedagogy expansion across all eight volumes.",
        "",
        "## Automated gates passed",
        "",
        "- Whole-series pedagogy integration freeze: **PASS**.",
        "- Post-pedagogy initial rendered audit: **PASS**.",
        "- Harmonized clean rebuild of all eight canonical `book.tex` targets: **PASS**.",
        "- Post-harmonization full-page rendered reproof: **PASS**.",
        "- Cross-volume pedagogy reconciliation: **PASS**.",
        "",
        "## Pedagogy corpus",
        "",
        f"- Chapters: **{freeze.get('chapters')}**.",
        f"- Composed worked examples: **{freeze.get('series_totals',{}).get('examples')}**.",
        f"- Composed exercises: **{freeze.get('series_totals',{}).get('exercises')}**.",
        f"- Composed hints: **{freeze.get('series_totals',{}).get('hints')}**.",
        f"- Composed solutions: **{freeze.get('series_totals',{}).get('solutions')}**.",
        "",
        "## Human rendered-proof queue",
        "",
        f"- Low-text page candidates after rebuild: **{review['reproof_low_text']}**.",
        f"- Overfull boxes after rebuild: **{review['reproof_overfull']}**.",
        f"- Overfull boxes >=20pt after rebuild: **{review['reproof_overfull_ge_20pt']}**.",
        "",
        "These candidates are not automatically defects: title pages, part pages, deliberate",
        "blank pages, diagrams, and mathematically unavoidable long displays may be legitimate.",
        "",
        "## Release status",
        "",
        "**PENDING_HUMAN_RENDERED_REPROOF**",
        "",
        "The final v1.2 release freeze is deliberately not part of this commit. Promote this",
        "candidate only after the targeted human/rendered inspection queue has been reviewed",
        "and any confirmed release blockers have been corrected.",
        "",
    ]
    (out / "RELEASE_NOTES.md").write_text("\n".join(notes), encoding="utf-8")

    # Hash everything in the RC directory except the manifest itself.
    lines = []
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.name != "SHA256SUMS.txt":
            lines.append(f"{sha256(p)}  {p.relative_to(out).as_posix()}")
    (out / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    for line in lines:
        digest, rel = line.split("  ", 1)
        if sha256(out / rel) != digest:
            raise SystemExit("RC hash verification failed: " + rel)

    # Refresh the top-level series release dashboard to the post-pedagogy RC state.
    manifest_rows = []
    for volume, number, title, dirname in VOLS:
        fr = freeze_pdf[volume]
        inv = pdfinv[volume]
        srow = next(r for r in source_rows if r["volume"] == volume)
        manifest_rows.append({
            "volume": volume,
            "title": title,
            "chapters": fr["chapters"],
            "planned": 0,
            "drafted": 0,
            "frozen": fr["chapters"],
            "complete": fr["chapters"],
            "book_wrapper": "YES",
            "build_status": "PASS",
            "pdf_pages": inv["pages"],
            "pdf_sha256": inv["sha256"],
            "source_baseline_sha256": srow["source_aggregate_sha256"],
            "missing_canonical_paths": 0,
            "encoding_findings": 0,
            "missing_cross_refs": 0,
            "readiness": "RC_PENDING_HUMAN_PROOF",
            "unresolved": "targeted rendered-proof queue pending",
        })
    manifest_fields = [
        "volume","title","chapters","planned","drafted","frozen","complete","book_wrapper",
        "build_status","pdf_pages","pdf_sha256","source_baseline_sha256","missing_canonical_paths",
        "encoding_findings","missing_cross_refs","readiness","unresolved"
    ]
    release_root = repo / "release"
    write_tsv(release_root / "SERIES_MASTER_MANIFEST.tsv", manifest_rows, manifest_fields)

    readiness = {
        "schema": 2,
        "candidate": "v1.2-rc1",
        "status": "RC_PENDING_HUMAN_PROOF",
        "volumes": manifest_rows,
        "automated_gates": {
            "pedagogy_freeze": freeze.get("status"),
            "initial_render_audit": initial.get("status"),
            "harmonized_build": harmon.get("status"),
            "rendered_reproof": reproof.get("status"),
        },
        "human_rendered_proof_required": True,
        "final_release_frozen": False,
        "release_dir": out.relative_to(repo).as_posix(),
    }
    (release_root / "SERIES_RELEASE_READINESS.json").write_text(
        json.dumps(readiness, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    dashboard = [
        "# Theory of Mathematics I–VIII — Release Dashboard",
        "",
        "**Current candidate:** v1.2-rc1 — **PENDING HUMAN RENDERED PROOF**",
        "",
        "| Volume | Chapters | Build | PDF pages | RC readiness |",
        "|---|---:|---|---:|---|",
    ]
    for r in manifest_rows:
        dashboard.append(
            f"| {r['volume']} — {r['title']} | {r['chapters']} | {r['build_status']} | "
            f"{r['pdf_pages']} | **{r['readiness']}** |"
        )
    dashboard += [
        "",
        "## Post-pedagogy gates",
        "",
        "- Whole-series pedagogy freeze: **PASS**.",
        "- Initial full-page rendered audit: **PASS**.",
        "- Harmonized clean rebuild I–VIII: **PASS**.",
        "- Full-page rendered reproof after rebuild: **PASS**.",
        "",
        "## Remaining gate",
        "",
        "Targeted human inspection of the low-text and layout-warning queues.",
        "The final v1.2 freeze remains a separate commit.",
        "",
    ]
    (release_root / "SERIES_RELEASE_DASHBOARD.md").write_text("\n".join(dashboard), encoding="utf-8")

    primary = [
        repo / "reports/series/SERIES_PEDAGOGY_FREEZE.json",
        repo / "reports/series/POST_PEDAGOGY_REPROOF_AUDIT.json",
        repo / "reports/series/POST_PEDAGOGY_BUILD_I_VIII.tsv",
        repo / "reports/series/POST_PEDAGOGY_PDF_INVENTORY.tsv",
        release_root / "SERIES_MASTER_MANIFEST.tsv",
        release_root / "SERIES_RELEASE_READINESS.json",
        out / "RELEASE.json",
        out / "SHA256SUMS.txt",
    ]
    master_lines = [f"{sha256(p)}  {p.relative_to(repo).as_posix()}" for p in primary]
    (release_root / "SERIES_MASTER_MANIFEST.sha256").write_text(
        "\n".join(master_lines) + "\n", encoding="utf-8"
    )

    rc_aggregate = sha_text("\n".join(lines))
    summary = {
        "schema": 1,
        "status": "PASS",
        "candidate": "v1.2-rc1",
        "release_dir": out.relative_to(repo).as_posix(),
        "volumes": 8,
        "chapters": 256,
        "pdfs": 8,
        "pdf_pages": sum(int(r["pages"]) for r in pdf_rows),
        "release_files_hashed": len(lines),
        "rc_aggregate_sha256": rc_aggregate,
        "human_rendered_proof_required": True,
        "final_release_frozen": False,
        "release_decision": "PENDING_HUMAN_RENDERED_REPROOF",
    }
    (reports / "V12_RC1_SUMMARY.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (reports / "V12_RC1_SUMMARY.md").write_text(
        "\n".join([
            "# Theory of Mathematics I–VIII — v1.2 RC1 summary",
            "",
            "**Automated RC preparation:** PASS",
            "",
            f"- Volumes: **{summary['volumes']}**",
            f"- Chapters: **{summary['chapters']}**",
            f"- PDFs: **{summary['pdfs']}**",
            f"- PDF pages: **{summary['pdf_pages']}**",
            f"- RC aggregate SHA-256: `{summary['rc_aggregate_sha256']}`",
            "",
            "**Release decision:** PENDING_HUMAN_RENDERED_REPROOF",
            "",
            "The final v1.2 release freeze remains separate.",
            "",
        ]), encoding="utf-8"
    )

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
