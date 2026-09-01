#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, re
from collections import Counter, defaultdict
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
def read(p): return p.read_text(encoding="utf-8-sig",errors="replace")
def read_status(p):
    with p.open("r",encoding="utf-8-sig",newline="") as f: return list(csv.DictReader(f,delimiter="\t"))
def write_tsv(p,rows,fields):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()
def pdf_pages(p):
    # Pure-Python fallback suitable for TeX-generated PDFs: count leaf /Page objects,
    # excluding the /Pages tree object.
    data=p.read_bytes()
    return len(re.findall(rb"/Type\s*/Page(?!s)\b",data))
def parse_book_metadata(p):
    if not p.exists(): return {"title":"","pdftitle":"","includes":0,"parts":0}
    t=read(p)
    title=re.search(r"\\title\{(.*?)\}",t,re.S)
    pdf=re.search(r"pdftitle\s*=\s*\{([^}]*)\}",t,re.S)
    return {
      "title":re.sub(r"\s+"," ",title.group(1)).strip() if title else "",
      "pdftitle":re.sub(r"\s+"," ",pdf.group(1)).strip() if pdf else "",
      "includes":len(re.findall(r"(?m)^[ \t]*\\include\{",t)),
      "parts":len(re.findall(r"(?m)^[ \t]*\\part\{",t)),
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--build-inventory",default="")
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    status=read_status(repo/"editorial/CHAPTER_STATUS.tsv")
    books=repo/"books"; reports=repo/"reports/series"; reports.mkdir(parents=True,exist_ok=True)

    build_rows={}
    if args.build_inventory:
        bp=Path(args.build_inventory)
        if bp.exists():
            with bp.open("r",encoding="utf-8-sig",newline="") as f:
                for r in csv.DictReader(f,delimiter="\t"): build_rows[r["volume"]]=r

    metadata_rows=[]; pdf_rows=[]; all_labels={}; refs=[]
    label_owner={}
    existing_chapter_files=[]
    for v,n,title,dirname in VOLS:
        vd=books/dirname
        rows=[r for r in status if r["volume"]==v]
        st=Counter(r["status"] for r in rows); nx=Counter(r["next_action"] for r in rows)
        book=vd/"book.tex"; md=parse_book_metadata(book)
        pdf=vd/"book.pdf"
        pdf_info={"volume":v,"pdf_path":"N/A","exists":"NO","pages":"N/A","bytes":"N/A","sha256":"N/A"}
        if pdf.exists():
            pdf_info={"volume":v,"pdf_path":pdf.relative_to(repo).as_posix(),"exists":"YES",
                      "pages":pdf_pages(pdf),"bytes":pdf.stat().st_size,"sha256":sha(pdf)}
        pdf_rows.append(pdf_info)
        metadata_rows.append({
          "volume":v,"number":n,"title":title,"directory":dirname,
          "chapter_rows":len(rows),"planned":st.get("PLANNED",0),"drafted":st.get("DRAFTED",0),
          "frozen":st.get("FROZEN",0),"complete":nx.get("COMPLETE",0),
          "book_tex":"YES" if book.exists() else "NO",
          "active_includes":md["includes"],"parts":md["parts"],
          "latex_title":md["title"],"pdf_title":md["pdftitle"],
          "build_status":build_rows.get(v,{}).get("status","NOT_RUN" if book.exists() else "NO_WRAPPER"),
          "pdf_pages":pdf_info["pages"],"pdf_sha256":pdf_info["sha256"]
        })

        # Volume landing page.
        lines=[
          f"# Volume {v} — {title}","",
          f"**Canonical directory:** `{dirname}`",
          f"**Chapter architecture:** {len(rows)} chapters",
          f"**Canonical wrapper:** {'`book.tex`' if book.exists() else 'not yet created'}",
          f"**Status:** {st.get('PLANNED',0)} planned / {st.get('DRAFTED',0)} drafted / {st.get('FROZEN',0)} frozen.",
          "",
          "## Canonical chapter navigation",""
        ]
        for r in rows:
            exists=(repo/r["canonical_path"]).exists()
            marker="✓" if exists else "○"
            lines.append(f"- {marker} **{r['chapter_code']} — {r['chapter_title']}** — `{r['status']}` / `{r['next_action']}`")
        lines += ["","## Build state",""]
        if book.exists():
            br=build_rows.get(v,{})
            lines.append(f"- Canonical wrapper exists with **{md['includes']} active includes** and **{md['parts']} parts**.")
            lines.append(f"- Latest series-build status: **{br.get('status','NOT_RUN')}**.")
            if pdf.exists():
                lines.append(f"- Current canonical PDF: **{pdf_info['pages']} pages**, SHA-256 `{pdf_info['sha256']}`.")
        else:
            lines.append("- This volume remains at architecture/reconstruction stage; `BUILD_ALL` does not fabricate an empty wrapper.")
        (vd/"LANDING.md").write_text("\n".join(lines).rstrip()+"\n",encoding="utf-8")

        # Cross-reference scan over existing canonical chapter files.
        for r in rows:
            cp=repo/r["canonical_path"]
            if not cp.exists(): continue
            existing_chapter_files.append(cp)
            text=read(cp)
            for lab in re.findall(r"\\label\{([^}]+)\}",text):
                label_owner.setdefault(lab,v)
            for kind,lab in re.findall(r"\\(ref|eqref|autoref)\{([^}]+)\}",text):
                refs.append((v,cp.relative_to(repo).as_posix(),kind,lab))

    # Second pass for ref ownership.
    ref_rows=[]
    for v,path,kind,lab in refs:
        owner=label_owner.get(lab,"")
        cls="MISSING_LABEL" if not owner else ("CROSS_VOLUME" if owner!=v else "INTRA_VOLUME")
        ref_rows.append({"source_volume":v,"source_path":path,"ref_kind":kind,
                         "label":lab,"target_volume":owner,"classification":cls})
    write_tsv(books/"CROSS_VOLUME_REFERENCE_AUDIT.tsv",ref_rows,
              ["source_volume","source_path","ref_kind","label","target_volume","classification"])
    write_tsv(books/"VOLUME_METADATA_AUDIT.tsv",metadata_rows,
              ["volume","number","title","directory","chapter_rows","planned","drafted","frozen","complete",
               "book_tex","active_includes","parts","latex_title","pdf_title","build_status","pdf_pages","pdf_sha256"])
    write_tsv(reports/"PDF_INVENTORY.tsv",pdf_rows,
              ["volume","pdf_path","exists","pages","bytes","sha256"])

    # Series navigation.
    nav=["# Theory of Mathematics — Volumes I–VIII","",
         "Canonical navigation generated from `editorial/CHAPTER_STATUS.tsv`.","",
         "## Volume navigation",""]
    for row in metadata_rows:
        nav.append(
          f"- **Volume {row['volume']} — {row['title']}** → `{row['directory']}/LANDING.md` "
          f"({row['chapter_rows']} chapters; {row['book_tex']=='YES' and 'buildable wrapper present' or 'architecture stage'})"
        )
    nav += ["","## Buildability rule","",
            "The series build compiles canonical `book.tex` wrappers that actually exist. "
            "A missing wrapper is recorded as `NO_WRAPPER`, not treated as a LaTeX failure and never auto-generated.",
            "","## Cross-volume reference audit","",
            f"- Cross-volume references found: **{sum(r['classification']=='CROSS_VOLUME' for r in ref_rows)}**",
            f"- Missing referenced labels found: **{sum(r['classification']=='MISSING_LABEL' for r in ref_rows)}**",
            "",
            "See `CROSS_VOLUME_REFERENCE_AUDIT.tsv` for instance-level evidence."]
    (books/"SERIES_NAVIGATION.md").write_text("\n".join(nav).rstrip()+"\n",encoding="utf-8")

    print(f"Generated navigation for {len(metadata_rows)} volumes; "
          f"{sum(r['book_tex']=='YES' for r in metadata_rows)} canonical wrappers present.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
