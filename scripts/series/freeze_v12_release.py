#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, shutil, subprocess
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

def sha256(path: Path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):
            h.update(b)
    return h.hexdigest()

def tree_hash(files,repo):
    h=hashlib.sha256()
    for p in sorted(files,key=lambda p:p.relative_to(repo).as_posix()):
        rel=p.relative_to(repo).as_posix()
        h.update(rel.encode("utf-8"));h.update(b"\0");h.update(bytes.fromhex(sha256(p)))
    return h.hexdigest()

def write_tsv(path,rows,fields):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader();w.writerows(rows)

def git_head(repo):
    cp=subprocess.run(["git","-C",str(repo),"rev-parse","HEAD"],capture_output=True,text=True)
    return cp.stdout.strip() if cp.returncode==0 else ""

def verify_sums(rc):
    p=rc/"SHA256SUMS.txt"
    if not p.exists(): raise RuntimeError("Missing RC SHA256SUMS.txt")
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        digest,rel=line.split("  ",1)
        if sha256(rc/rel)!=digest:
            raise RuntimeError("RC hash mismatch: "+rel)

def refresh_sums(root):
    lines=[]
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.name!="SHA256SUMS.txt":
            lines.append(f"{sha256(p)}  {p.relative_to(root).as_posix()}")
    (root/"SHA256SUMS.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")
    for line in lines:
        digest,rel=line.split("  ",1)
        if sha256(root/rel)!=digest: raise RuntimeError("Final hash mismatch: "+rel)
    return lines

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    reports=repo/"reports/series"
    rc=repo/"release/theory_of_mathematics_i_viii_v1.2-rc1"
    final=repo/"release/theory_of_mathematics_i_viii_v1.2"

    reproof=json.loads((reports/"V12_RC1_RESIDUAL_REPROOF.json").read_text(encoding="utf-8"))
    triage=json.loads((reports/"V12_RC1_RESIDUAL_LAYOUT_TRIAGE.json").read_text(encoding="utf-8"))
    if reproof.get("status")!="PASS":
        raise SystemExit("Residual reproof is not PASS.")
    if int(reproof.get("overfull_ge_20pt_after_residual_fixes",99))!=0:
        raise SystemExit("Cannot freeze: >=20pt residual queue is not zero.")
    if int(reproof.get("rendered_pages",0))!=int(reproof.get("pdf_pages",0)):
        raise SystemExit("Cannot freeze: not every PDF page rendered.")
    if int(triage.get("low_text_pages_reviewed",0))!=int(triage.get("low_text_pages_classified_intentional",0)):
        raise SystemExit("Cannot freeze: low-text structural classification incomplete.")
    if not rc.exists():
        raise SystemExit("v1.2-rc1 directory is missing.")
    verify_sums(rc)
    if final.exists():
        raise SystemExit("Final v1.2 release directory already exists.")

    shutil.copytree(rc,final)

    # Current source baselines: every volume .tex file plus the shared LaTeX layer.
    shared=[
        repo/"shared/preamble.tex",
        repo/"shared/macros.tex",
        repo/"shared/theorem_styles.tex",
        repo/"shared/notation.tex",
    ]
    rows=[]
    pdf_manifest={r["volume"]:r for r in csv.DictReader(
        (final/"manifests/PDFS.tsv").open("r",encoding="utf-8-sig",newline=""),delimiter="\t"
    )}
    for v,n,title,dirname in VOLS:
        root=repo/"books"/dirname
        files=[p for p in root.rglob("*.tex") if p.is_file()]+[p for p in shared if p.exists()]
        rows.append({
            "volume":v,
            "number":n,
            "title":title,
            "source_tex_files":len(files),
            "source_tree_sha256":tree_hash(files,repo),
            "pdf_pages":pdf_manifest[v]["pages"],
            "pdf_sha256":pdf_manifest[v]["sha256"],
        })
    write_tsv(
        final/"manifests/FINAL_SOURCE_BASELINES.tsv",
        rows,
        ["volume","number","title","source_tex_files","source_tree_sha256","pdf_pages","pdf_sha256"],
    )

    meta_path=final/"RELEASE.json"
    meta=json.loads(meta_path.read_text(encoding="utf-8"))
    meta["release"]="Theory of Mathematics I–VIII v1.2"
    meta["tag"]="theory-of-mathematics-i-viii-v1.2"
    meta["source_commit_at_freeze"]=git_head(repo)
    meta["automated_rendered_reproof"]={
        "status":"PASS",
        "pdf_pages":int(reproof.get("pdf_pages",0)),
        "rendered_pages":int(reproof.get("rendered_pages",0)),
        "overfull_ge_20pt":0,
        "low_text_pages_classified_intentional":int(triage.get("low_text_pages_classified_intentional",0)),
    }
    meta["freeze_authorization"]={
        "authorized":True,
        "basis":"explicit user authorization after automated rendered reproof and residual layout triage",
        "human_visual_page_by_page_proof_recorded":False,
    }
    meta["human_rendered_proof_required"]=False
    meta["final_release_frozen"]=True
    meta["release_decision"]="FROZEN_V1.2"
    meta["final_source_baselines"]=rows
    meta_path.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    notes=final/"RELEASE_NOTES.md"
    notes.write_text(
        notes.read_text(encoding="utf-8")
        + "\n## v1.2 final freeze\n\n"
        + "- Automated rendered reproof: **PASS** for every release page.\n"
        + "- Residual >=20pt overfull queue: **0**.\n"
        + "- Low-text candidates: classified as intentional structural/frontmatter pages.\n"
        + "- Final freeze authorization: explicit user approval after the automated proof gates.\n"
        + "- A separate human page-by-page visual proof was **not** recorded; the release metadata states this explicitly.\n"
        + "- Release decision: **FROZEN_V1.2**.\n",
        encoding="utf-8",
    )

    lines=refresh_sums(final)
    aggregate=hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()

    obj={
        "schema":1,
        "status":"PASS",
        "release":"v1.2",
        "volumes":8,
        "chapters":256,
        "pdfs":8,
        "pdf_pages":int(reproof.get("pdf_pages",0)),
        "rendered_pages":int(reproof.get("rendered_pages",0)),
        "overfull_ge_20pt":0,
        "low_text_pages_classified_intentional":int(triage.get("low_text_pages_classified_intentional",0)),
        "final_release_dir":final.relative_to(repo).as_posix(),
        "final_release_frozen":True,
        "release_decision":"FROZEN_V1.2",
        "human_visual_page_by_page_proof_recorded":False,
        "freeze_authorization":"explicit user authorization",
        "final_release_files_hashed":len(lines),
        "final_release_aggregate_sha256":aggregate,
        "source_baselines":rows,
        "blocking":[],
    }
    (reports/"V12_RELEASE_FREEZE.json").write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (reports/"V12_RELEASE_FREEZE.md").write_text(
        "# Theory of Mathematics I–VIII — v1.2 release freeze\n\n"
        "**Status:** PASS / FROZEN_V1.2\n\n"
        f"- Volumes: **8**; chapters: **256**.\n"
        f"- PDF/rendered pages: **{obj['pdf_pages']} / {obj['rendered_pages']}**.\n"
        "- >=20pt overfull boxes: **0**.\n"
        f"- Intentional structural/frontmatter low-text pages: **{obj['low_text_pages_classified_intentional']}**.\n"
        f"- Final release aggregate SHA-256: `{aggregate}`.\n"
        "- Human page-by-page visual proof recorded: **No**; freeze is based on automated rendered proof plus explicit user authorization.\n",
        encoding="utf-8",
    )

    # Refresh the generic dashboard to current source/PDF state.
    dash=repo/"scripts/series/generate_release_dashboard.py"
    if dash.exists():
        cp=subprocess.run(["python",str(dash),"--repo",str(repo)],capture_output=True,text=True,errors="replace")
        if cp.returncode!=0:
            raise RuntimeError("Release dashboard refresh failed:\n"+cp.stdout+cp.stderr)

    release=repo/"release"
    primary=[
        reports/"V12_RELEASE_FREEZE.json",
        reports/"V12_RC1_RESIDUAL_REPROOF.json",
        release/"SERIES_MASTER_MANIFEST.tsv",
        release/"SERIES_RELEASE_READINESS.json",
        final/"RELEASE.json",
        final/"SHA256SUMS.txt",
    ]
    (release/"SERIES_MASTER_MANIFEST.sha256").write_text(
        "\n".join(f"{sha256(p)}  {p.relative_to(repo).as_posix()}" for p in primary)+"\n",
        encoding="utf-8",
    )

    print(json.dumps(obj,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
