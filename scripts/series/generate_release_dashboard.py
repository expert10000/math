#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,re
from collections import Counter
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
def read_tsv(p):
    if not p.exists(): return []
    with p.open("r",encoding="utf-8-sig",newline="") as f: return list(csv.DictReader(f,delimiter="\t"))
def hfile(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()
def tree_hash(paths,repo):
    h=hashlib.sha256()
    for p in sorted(set(paths),key=lambda x:x.as_posix()):
        if not p.exists() or not p.is_file(): continue
        rel=p.relative_to(repo).as_posix()
        h.update(rel.encode()); h.update(b"\0"); h.update(bytes.fromhex(hfile(p)))
    return h.hexdigest()
def write_tsv(p,rows,fields):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader();w.writerows(rows)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); args=ap.parse_args()
    repo=Path(args.repo).resolve()
    status=read_tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    build={r["volume"]:r for r in read_tsv(repo/"reports/series/BUILD_I_VIII.tsv") if r.get("target")=="book.tex"}
    pdf={r["volume"]:r for r in read_tsv(repo/"reports/series/PDF_INVENTORY.tsv")}
    enc=read_tsv(repo/"reports/series/GLOBAL_ENCODING_AUDIT.tsv")
    paths=read_tsv(repo/"reports/series/GLOBAL_CANONICAL_PATH_AUDIT.tsv")
    xrefs=read_tsv(repo/"books/CROSS_VOLUME_REFERENCE_AUDIT.tsv")

    rows=[]; unresolved=[]
    for v,n,title,dirname in VOLS:
        vd=repo/"books"/dirname
        sr=[r for r in status if r["volume"]==v]
        st=Counter(r["status"] for r in sr); nx=Counter(r["next_action"] for r in sr)
        br=build.get(v,{})
        pr=pdf.get(v,{})
        book=vd/"book.tex"
        source_files=[book,vd/"README.md",vd/"LANDING.md"]
        source_files += [repo/r["canonical_path"] for r in sr if (repo/r["canonical_path"]).exists()]
        source_hash=tree_hash(source_files,repo)
        missing_paths=sum(1 for r in sr if not (repo/r["canonical_path"]).exists())
        encoding_findings=sum(1 for r in enc if (r.get("path","").startswith(f"books/{dirname}/")))
        missing_refs=sum(1 for r in xrefs if r.get("source_volume")==v and r.get("classification")=="MISSING_LABEL")
        build_status=br.get("status","NO_WRAPPER" if not book.exists() else "NOT_RUN")
        pages=pr.get("pages","")
        pdf_hash=pr.get("sha256","")
        # Readiness classification.
        if not book.exists():
            readiness="ARCHITECTURE_ONLY"
        elif build_status=="FAIL":
            readiness="BLOCKED_BUILD"
        elif st.get("FROZEN",0)==len(sr) and nx.get("COMPLETE",0)==len(sr) and pr.get("exists")=="YES":
            readiness="RELEASED"
        elif build_status=="PASS":
            readiness="BUILDABLE_DRAFT"
        else:
            readiness="NEEDS_BUILD"
        blockers=[]
        if missing_refs: blockers.append(f"{missing_refs} missing labels")
        if encoding_findings: blockers.append(f"{encoding_findings} encoding findings")
        if build_status=="FAIL": blockers.append("canonical build failed")
        if missing_paths and book.exists(): blockers.append(f"{missing_paths} canonical paths missing")
        if readiness=="ARCHITECTURE_ONLY": blockers.append("canonical wrapper not yet created")
        rows.append({
          "volume":v,"title":title,"chapters":len(sr),"planned":st.get("PLANNED",0),
          "drafted":st.get("DRAFTED",0),"frozen":st.get("FROZEN",0),"complete":nx.get("COMPLETE",0),
          "book_wrapper":"YES" if book.exists() else "NO","build_status":build_status,
          "pdf_pages":pages,"pdf_sha256":pdf_hash,"source_baseline_sha256":source_hash,
          "missing_canonical_paths":missing_paths,"encoding_findings":encoding_findings,
          "missing_cross_refs":missing_refs,"readiness":readiness,
          "unresolved":"; ".join(blockers) if blockers else "-"
        })
        for b in blockers: unresolved.append({"volume":v,"item":b,"readiness":readiness})

    release=repo/"release"; release.mkdir(parents=True,exist_ok=True)
    fields=["volume","title","chapters","planned","drafted","frozen","complete","book_wrapper","build_status",
            "pdf_pages","pdf_sha256","source_baseline_sha256","missing_canonical_paths","encoding_findings",
            "missing_cross_refs","readiness","unresolved"]
    write_tsv(release/"SERIES_MASTER_MANIFEST.tsv",rows,fields)

    # Manifest hash file over primary series evidence and source baselines.
    evidence=[
      repo/"editorial/CONTENT_ATLAS.md",repo/"editorial/CHAPTER_STATUS.tsv",
      repo/"editorial/SOURCE_MIGRATION.tsv",repo/"reports/series/GLOBAL_I_VIII_AUDIT.json",
      repo/"reports/series/BUILD_I_VIII.tsv",repo/"reports/series/PDF_INVENTORY.tsv",
      repo/"books/SERIES_NAVIGATION.md",repo/"books/CROSS_VOLUME_REFERENCE_AUDIT.tsv",
      release/"SERIES_MASTER_MANIFEST.tsv",
    ]
    lines=[]
    for p in evidence:
        if p.exists(): lines.append(f"{hfile(p)}  {p.relative_to(repo).as_posix()}")
    (release/"SERIES_MASTER_MANIFEST.sha256").write_text("\n".join(lines).rstrip()+"\n",encoding="utf-8")

    obj={"schema":1,"volumes":rows,"unresolved_corpus_items":unresolved}
    (release/"SERIES_RELEASE_READINESS.json").write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    md=["# Theory of Mathematics I–VIII — Release Dashboard","",
        "Generated from canonical status, build, navigation, reference, encoding, and PDF inventories.","",
        "| Volume | Chapters | Status | Build | PDF pages | Readiness | Unresolved |",
        "|---|---:|---|---|---:|---|---|"]
    for r in rows:
        status_summary=f"{r['planned']}P/{r['drafted']}D/{r['frozen']}F"
        md.append(f"| {r['volume']} — {r['title']} | {r['chapters']} | {status_summary} | {r['build_status']} | "
                  f"{r['pdf_pages'] or '—'} | **{r['readiness']}** | "
                  f"{'—' if r['unresolved']=='-' else r['unresolved']} |")
    md += ["","## Readiness semantics","",
           "- **RELEASED** — all chapter rows FROZEN/COMPLETE, canonical build PDF present.",
           "- **BUILDABLE_DRAFT** — canonical wrapper builds, but chapter corpus is not fully frozen.",
           "- **NEEDS_BUILD** — wrapper exists but no successful current series build inventory.",
           "- **BLOCKED_BUILD** — canonical wrapper build failed.",
           "- **ARCHITECTURE_ONLY** — chapter architecture/status exists, but canonical `book.tex` has not yet been created.",
           "","## Source and PDF baselines",""]
    for r in rows:
        md.append(f"- Volume {r['volume']}: source `{r['source_baseline_sha256']}`"
                  + (f"; PDF `{r['pdf_sha256']}` ({r['pdf_pages']} pages)" if r["pdf_sha256"] else "; no canonical PDF baseline"))
    md += ["","## Unresolved corpus items",""]
    if unresolved:
        for u in unresolved: md.append(f"- Volume {u['volume']}: {u['item']} ({u['readiness']})")
    else: md.append("None.")
    (release/"SERIES_RELEASE_DASHBOARD.md").write_text("\n".join(md).rstrip()+"\n",encoding="utf-8")

    # Compact machine-readable per-volume source baseline.
    print(json.dumps({"volumes":len(rows),"released":sum(r["readiness"]=="RELEASED" for r in rows),
                      "unresolved_items":len(unresolved)},indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
