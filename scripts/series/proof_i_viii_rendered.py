#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re,shutil,struct,subprocess,tempfile
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

def write_tsv(path,rows,fields):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader();w.writerows(rows)

def pdf_pages(path):
    data=Path(path).read_bytes()
    return len(re.findall(rb"/Type\s*/Page(?!s)\b",data))

def png_info(path):
    data=Path(path).read_bytes()[:32]
    if len(data)<24 or data[:8]!=b"\x89PNG\r\n\x1a\n":
        return 0,0
    return struct.unpack(">II",data[16:24])

def run(cmd,cwd=None):
    cp=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,errors="replace")
    if cp.returncode!=0:
        raise RuntimeError("Command failed: "+" ".join(map(str,cmd))+"\n"+cp.stdout[-3000:]+"\n"+cp.stderr[-3000:])
    return cp

def render_pdf(pdf,outdir,prefix,dpi):
    pdftoppm=shutil.which("pdftoppm")
    mutool=shutil.which("mutool")
    gs=shutil.which("gswin64c") or shutil.which("gswin32c") or shutil.which("gs")
    if pdftoppm:
        run([pdftoppm,"-png","-gray","-r",str(dpi),str(pdf),str(outdir/prefix)])
        files=sorted(outdir.glob(prefix+"-*.png"))
        return "pdftoppm",files
    if mutool:
        pattern=str(outdir/(prefix+"-%04d.png"))
        run([mutool,"draw","-q","-r",str(dpi),"-o",pattern,str(pdf)])
        files=sorted(outdir.glob(prefix+"-*.png"))
        return "mutool",files
    if gs:
        pattern=str(outdir/(prefix+"-%04d.png"))
        run([gs,"-dSAFER","-dBATCH","-dNOPAUSE","-sDEVICE=pnggray",
             f"-r{dpi}",f"-sOutputFile={pattern}",str(pdf)])
        files=sorted(outdir.glob(prefix+"-*.png"))
        return Path(gs).name,files
    raise RuntimeError("No page renderer found. Provide pdftoppm, mutool, or Ghostscript on PATH.")

def extract_text_pages(pdf,outdir,prefix):
    pdftotext=shutil.which("pdftotext")
    if not pdftotext:
        return "NOT_AVAILABLE",[]
    target=outdir/(prefix+".txt")
    run([pdftotext,"-layout",str(pdf),str(target)])
    text=target.read_text(encoding="utf-8",errors="replace")
    parts=text.split("\f")
    if parts and parts[-1]=="":
        parts=parts[:-1]
    return "pdftotext",parts

def log_warnings(log,volume):
    if not log.exists(): return [],["MISSING_LOG:"+volume]
    text=log.read_text(encoding="utf-8-sig",errors="replace")
    blockers=[]
    for needle in (
        "LaTeX Warning: There were undefined references",
        "There were undefined citations",
        "multiply defined",
    ):
        if needle.lower() in text.lower():
            blockers.append(f"{volume}:{needle}")
    rows=[]
    rx=re.compile(r"Overfull \\hbox \(([-+]?[0-9.]+)pt too wide\).*?(?:at lines? ([0-9]+)(?:--([0-9]+))?)?",re.I)
    for m in rx.finditer(text):
        rows.append({
            "volume":volume,
            "overfull_pt":m.group(1),
            "line_start":m.group(2) or "",
            "line_end":m.group(3) or m.group(2) or "",
            "severity":"HIGH" if float(m.group(1))>=20 else ("MEDIUM" if float(m.group(1))>=10 else "LOW")
        })
    return rows,blockers

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--dpi",type=int,default=18)
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    reports=repo/"reports/series";reports.mkdir(parents=True,exist_ok=True)
    pdfinv={r["volume"]:r for r in read_tsv(reports/"PDF_INVENTORY.tsv")}
    blockers=[];page_rows=[];layout_rows=[];volume_rows=[]
    renderer_used=set();text_tools=set()
    total_pages=0;rendered_pages=0;blank_candidates=0

    with tempfile.TemporaryDirectory(prefix="math_i_viii_renderproof_") as td:
        temp=Path(td)
        for v,n,title,dirname in VOLS:
            vol=repo/"books"/dirname
            pdf=vol/"book.pdf"
            if not pdf.exists():
                blockers.append(f"{v}:MISSING_PDF");continue
            inv=pdfinv.get(v,{})
            try:
                inv_pages=int(inv.get("pages") or 0) if inv else 0
            except ValueError:
                inv_pages=0
            byte_pages=pdf_pages(pdf)
            expected=inv_pages or byte_pages
            if expected<=0:
                pdfinfo=shutil.which("pdfinfo")
                if pdfinfo:
                    info=run([pdfinfo,str(pdf)]).stdout
                    m=re.search(r"(?m)^Pages:\s+(\d+)\s*$",info)
                    expected=int(m.group(1)) if m else 0
            if expected<=0:
                blockers.append(f"{v}:UNABLE_TO_DETERMINE_PAGE_COUNT")
                continue
            # Byte-level page counting is only a fallback because modern PDFs
            # can store page-tree objects in compressed object streams.
            out=temp/f"v{n:02d}";out.mkdir()
            try:
                renderer,images=render_pdf(pdf,out,f"v{n:02d}",args.dpi)
            except Exception as exc:
                blockers.append(f"{v}:RENDER_FAILED:{exc}")
                continue
            renderer_used.add(renderer)
            text_tool,text_pages=extract_text_pages(pdf,out,f"v{n:02d}")
            text_tools.add(text_tool)
            if len(images)!=expected:
                blockers.append(f"{v}:RENDERED_PAGES:{len(images)}!={expected}")
            if text_pages and len(text_pages) not in (expected,expected+1):
                blockers.append(f"{v}:TEXT_PAGE_COUNT:{len(text_pages)}!={expected}")

            vol_blank=0
            for i,img in enumerate(images,1):
                w,h=png_info(img);size=img.stat().st_size
                chars=""
                if i<=len(text_pages):
                    chars=len(re.sub(r"\s+","",text_pages[i-1]))
                classification="RENDERED_OK"
                if size<100 or w<=0 or h<=0:
                    classification="RENDER_INVALID"
                    blockers.append(f"{v}:PAGE_{i}:INVALID_RENDER")
                elif chars!="" and chars<20:
                    classification="LOW_TEXT_REVIEW"
                    vol_blank+=1;blank_candidates+=1
                page_rows.append({
                    "volume":v,"page":i,"raster_width":w,"raster_height":h,
                    "raster_bytes":size,"text_chars":chars,
                    "classification":classification
                })
            total_pages+=expected;rendered_pages+=len(images)

            lw,lb=log_warnings(vol/"book.log",v)
            layout_rows+=lw;blockers+=lb
            volume_rows.append({
                "volume":v,"title":title,"pdf_pages":expected,"rendered_pages":len(images),
                "renderer":renderer,"text_extractor":text_tool,
                "low_text_review_pages":vol_blank,
                "overfull_boxes":len(lw),
                "overfull_ge_20pt":sum(float(r["overfull_pt"])>=20 for r in lw),
                "status":"PASS" if len(images)==expected and not lb else "FAIL"
            })

    write_tsv(reports/"RENDERED_PAGE_PROOF.tsv",page_rows,[
        "volume","page","raster_width","raster_height","raster_bytes","text_chars","classification"
    ])
    write_tsv(reports/"LATEX_LAYOUT_WARNINGS.tsv",layout_rows,[
        "volume","overfull_pt","line_start","line_end","severity"
    ])
    write_tsv(reports/"RENDERED_VOLUME_PROOF.tsv",volume_rows,[
        "volume","title","pdf_pages","rendered_pages","renderer","text_extractor",
        "low_text_review_pages","overfull_boxes","overfull_ge_20pt","status"
    ])

    if len(volume_rows)!=8:
        blockers.append(f"VOLUME_PROOF_ROWS:{len(volume_rows)}!=8")
    if rendered_pages!=total_pages:
        blockers.append(f"TOTAL_RENDERED_PAGES:{rendered_pages}!={total_pages}")

    summary={
        "status":"PASS" if not blockers else "FAIL",
        "volumes":len(volume_rows),
        "pdf_pages":total_pages,
        "rendered_pages":rendered_pages,
        "renderers":sorted(renderer_used),
        "text_extractors":sorted(text_tools),
        "low_text_review_candidates":blank_candidates,
        "overfull_boxes":len(layout_rows),
        "overfull_ge_20pt":sum(float(r["overfull_pt"])>=20 for r in layout_rows),
        "blocking":blockers,
    }
    (reports/"RENDERED_I_VIII_PROOF.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=[
        "# Theory of Mathematics I–VIII — Rendered Release Proof","",
        f"**Automated proof result:** {summary['status']}","",
        f"- Volumes rendered: **{summary['volumes']} / 8**",
        f"- PDF pages: **{total_pages}**",
        f"- Pages rasterized: **{rendered_pages}**",
        f"- Renderer(s): **{', '.join(summary['renderers']) or 'none'}**",
        f"- Low-text pages flagged for human review: **{blank_candidates}**",
        f"- Overfull boxes recorded from LaTeX logs: **{len(layout_rows)}**",
        f"- Overfull boxes >=20pt: **{summary['overfull_ge_20pt']}**","",
        "## Scope","",
        "Every canonical PDF page is rasterized at low proofing resolution. The raster proof verifies that every page is renderable and produces a nonempty image.",
        "Text extraction, when available, flags low-text pages as review candidates rather than failures because title, part, and intentionally blank pages can be legitimate.",
        "LaTeX overfull boxes are inventoried for targeted visual inspection; only broken rendering or canonical undefined-reference/citation/multiply-defined warnings are blocking.",
        "",
        "## Human proof queue","",
        "Use `RENDERED_PAGE_PROOF.tsv` for low-text page candidates and `LATEX_LAYOUT_WARNINGS.tsv` for wide-box candidates. These are the targeted pages for the next manual visual pass.","",
        "## Blocking findings",""
    ]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (reports/"RENDERED_I_VIII_PROOF.md").write_text("\n".join(md)+"\n",encoding="utf-8")

    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blockers else 5

if __name__=="__main__":
    raise SystemExit(main())
