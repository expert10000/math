#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,shutil
from pathlib import Path

VOLS=[
("I",1,"Linear Algebra","vol01_linear_algebra"),
("II",2,"Real Analysis and Topological Foundations","vol02_real_analysis"),
("III",3,"Measure, Fourier Analysis, Distributions and PDE","vol03_fourier_distributions_pde"),
("IV",4,"Complex Analysis and Riemann Surfaces","vol04_complex_analysis"),
("V",5,"Commutative Algebra and Homological Methods","vol05_commutative_algebra"),
("VI",6,"Algebraic Geometry and Sheaf Theory","vol06_algebraic_geometry"),
("VII",7,"Differential, Riemannian and Hyperbolic Geometry","vol07_differential_geometry"),
("VIII",8,"Algebraic Topology","vol08_algebraic_topology"),
]

def read_tsv(path):
    with Path(path).open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):
            h.update(b)
    return h.hexdigest()

def write_tsv(path,rows,fields):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader();w.writerows(rows)

def copy(src,dst):
    src=Path(src);dst=Path(dst)
    if not src.exists():return False
    dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst);return True

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--release-name",default="theory_of_mathematics_i_viii_v1.1-rc1")
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    reports=repo/"reports/series"
    proof=json.loads((reports/"RENDERED_I_VIII_PROOF.json").read_text(encoding="utf-8"))
    dossier=json.loads((reports/"DOSSIER_INDEX_SUMMARY.json").read_text(encoding="utf-8"))
    nav=json.loads((reports/"CROSS_VOLUME_NAVIGATION_SUMMARY.json").read_text(encoding="utf-8"))
    recon=json.loads((reports/"GLOBAL_SERIES_RECONCILIATION.json").read_text(encoding="utf-8"))
    if proof.get("status")!="PASS":raise SystemExit("Rendered proof is not PASS")
    if dossier.get("status")!="PASS":raise SystemExit("Dossier index is not PASS")
    if nav.get("status")!="PASS":raise SystemExit("Navigation audit is not PASS")
    if recon.get("status")!="PASS":raise SystemExit("Global reconciliation is not PASS")

    out=repo/"release"/args.release_name
    if out.exists():shutil.rmtree(out)
    (out/"pdfs").mkdir(parents=True)
    (out/"evidence").mkdir(parents=True)
    (out/"manifests").mkdir(parents=True)

    pdfinv={r["volume"]:r for r in read_tsv(reports/"PDF_INVENTORY.tsv")}
    pdf_rows=[]
    for v,n,title,dirname in VOLS:
        src=repo/"books"/dirname/"book.pdf"
        if not src.exists():raise SystemExit(f"Missing PDF for {v}")
        dst=out/"pdfs"/f"volume{n:02d}_{dirname.removeprefix(f'vol{n:02d}_')}.pdf"
        shutil.copy2(src,dst)
        inv=pdfinv.get(v,{})
        pdf_rows.append({
            "volume":v,"number":n,"title":title,
            "pages":inv.get("pages",""),"bytes":src.stat().st_size,
            "sha256":sha(src),"release_pdf":dst.relative_to(out).as_posix()
        })
    write_tsv(out/"manifests/PDFS.tsv",pdf_rows,["volume","number","title","pages","bytes","sha256","release_pdf"])

    chapter_manifest=repo/"release/theory_of_mathematics_i_viii_v1.0/manifests/CHAPTERS.tsv"
    if chapter_manifest.exists():
        copy(chapter_manifest,out/"manifests/CHAPTERS_v1.0_source_baseline.tsv")

    evidence=[
        "reports/series/DOSSIER_INDEX.tsv",
        "reports/series/DOSSIER_PROVENANCE_ATLAS.tsv",
        "reports/series/DOSSIER_INDEX_SUMMARY.json",
        "reports/series/DOSSIER_INDEX.md",
        "reports/series/CROSS_VOLUME_DEPENDENCY_MAP.tsv",
        "reports/series/CROSS_VOLUME_CHAPTER_BRIDGES.tsv",
        "reports/series/CROSS_VOLUME_NAVIGATION_SUMMARY.json",
        "books/CROSS_VOLUME_MATHEMATICAL_NAVIGATION.md",
        "reports/series/RENDERED_PAGE_PROOF.tsv",
        "reports/series/RENDERED_VOLUME_PROOF.tsv",
        "reports/series/LATEX_LAYOUT_WARNINGS.tsv",
        "reports/series/RENDERED_I_VIII_PROOF.json",
        "reports/series/RENDERED_I_VIII_PROOF.md",
        "reports/series/GLOBAL_SERIES_RECONCILIATION.json",
        "reports/series/GLOBAL_SERIES_RECONCILIATION.md",
        "reports/series/BUILD_I_VIII.tsv",
        "reports/series/PDF_INVENTORY.tsv",
    ]
    copied=[]
    for rel in evidence:
        if copy(repo/rel,out/"evidence"/Path(rel).name):
            copied.append(rel)
    for v,n,title,dirname in VOLS:
        navfile=repo/"books"/dirname/"MATHEMATICAL_NAVIGATION.md"
        if navfile.exists():
            copy(navfile,out/"evidence"/"volume_navigation"/f"volume{n:02d}.md")
            copied.append(navfile.relative_to(repo).as_posix())

    notes=[
        "# Theory of Mathematics I–VIII — v1.1 RC1","",
        "This release candidate is a post-v1.0 editorial/proofing layer. The frozen mathematical chapter corpus remains unchanged.",
        "",
        "## Added after v1.0","",
        f"- Canonical problem/dossier index: **{dossier.get('canonical_problem_entries')}** `problem` entries.",
        f"- Additional indexed `challenge` entries: **{dossier.get('canonical_challenge_entries')}**.",
        f"- Curated cross-volume chapter bridges: **{nav.get('cross_volume_chapter_bridges')}**.",
        f"- Rendered proof pages: **{proof.get('rendered_pages')} / {proof.get('pdf_pages')}**.",
        f"- Low-text pages queued for human review: **{proof.get('low_text_review_candidates')}**.",
        f"- LaTeX overfull boxes queued for review: **{proof.get('overfull_boxes')}**, including **{proof.get('overfull_ge_20pt')}** >=20pt.",
        "",
        "## Release-candidate status","",
        "- Global corpus reconciliation remains PASS.",
        "- Eight canonical volume PDFs are included.",
        "- Every PDF page was successfully rasterized in the automated rendered proof.",
        "- Candidate visual issues are recorded as a targeted human-proof queue rather than silently rewritten.",
        "",
        "## Next gate","",
        "Perform the targeted human visual review of pages flagged in `evidence/RENDERED_PAGE_PROOF.tsv` and `evidence/LATEX_LAYOUT_WARNINGS.tsv`. Apply only confirmed errata before promoting v1.1 RC1 to v1.1.",
        ""
    ]
    (out/"RELEASE_NOTES.md").write_text("\n".join(notes),encoding="utf-8")

    meta={
        "schema":1,"release":"Theory of Mathematics I–VIII v1.1 RC1",
        "tag":"theory-of-mathematics-i-viii-v1.1-rc1",
        "volumes":8,"chapters":256,
        "mathematical_corpus":"unchanged from v1.0 frozen baseline",
        "dossier_index":dossier,
        "cross_volume_navigation":nav,
        "rendered_proof":proof,
        "pdfs":pdf_rows,"evidence_sources":copied,
    }
    (out/"RELEASE.json").write_text(json.dumps(meta,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    lines=[]
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.name!="SHA256SUMS.txt":
            lines.append(f"{sha(p)}  {p.relative_to(out).as_posix()}")
    (out/"SHA256SUMS.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")
    for line in lines:
        digest,rel=line.split("  ",1)
        if sha(out/rel)!=digest:raise SystemExit("Hash verification failed: "+rel)

    summary={"status":"PASS","release_dir":out.relative_to(repo).as_posix(),"pdfs":len(pdf_rows),"evidence_files":len(copied),"sha256_entries":len(lines)}
    print(json.dumps(summary,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
