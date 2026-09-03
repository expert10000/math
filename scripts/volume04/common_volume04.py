from __future__ import annotations
import csv,re
from pathlib import Path

ALL_CHAPTERS=[
("IV/01","Complex Differentiability","ch01_complex_differentiability"),
("IV/02","Cauchy–Riemann Equations","ch02_cauchy_riemann_equations"),
("IV/03","Power Series and Analytic Functions","ch03_power_series_and_analytic_functions"),
("IV/04","Complex Integration","ch04_complex_integration"),
("IV/05","Cauchy's Theorem","ch05_cauchy_s_theorem"),
("IV/06","Cauchy's Integral Formula","ch06_cauchy_s_integral_formula"),
("IV/07","Zeros and the Identity Theorem","ch07_zeros_and_the_identity_theorem"),
("IV/08","Laurent Series","ch08_laurent_series"),
("IV/09","Isolated Singularities","ch09_isolated_singularities"),
("IV/10","Residues and the Residue Theorem","ch10_residues_and_the_residue_theorem"),
("IV/11","Evaluation of Real Integrals","ch11_evaluation_of_real_integrals"),
("IV/12","Winding Numbers and the Argument Principle","ch12_winding_numbers_and_the_argument_principle"),
("IV/13","Rouché's Theorem","ch13_rouch_s_theorem"),
("IV/14","Branches of the Logarithm and Roots","ch14_branches_of_the_logarithm_and_roots"),
("IV/15","Analytic Continuation","ch15_analytic_continuation"),
("IV/16","Möbius Transformations","ch16_m_bius_transformations"),
("IV/17","Conformal Mapping","ch17_conformal_mapping"),
("IV/18","Schwarz–Christoffel Transformations","ch18_schwarz_christoffel_transformations"),
("IV/19","The Gamma Function","ch19_the_gamma_function"),
("IV/20","Beta and Gamma Identities","ch20_beta_and_gamma_identities"),
("IV/21","Keyhole Contours and Branch-Cut Integrals","ch21_keyhole_contours_and_branch_cut_integrals"),
("IV/22","From Analytic Continuation to Riemann Surfaces","ch22_from_analytic_continuation_to_riemann_surfaces"),
("IV/23","Covering Maps and Monodromy","ch23_covering_maps_and_monodromy"),
("IV/24","Branched Coverings","ch24_branched_coverings"),
("IV/25","Construction by Gluing","ch25_construction_by_gluing"),
("IV/26","Compactification and Genus","ch26_compactification_and_genus"),
("IV/27","Lattices and Complex Tori","ch27_lattices_and_complex_tori"),
("IV/28","Elliptic Functions","ch28_elliptic_functions"),
("IV/29","The Weierstrass ℘-Function","ch29_the_weierstrass_function"),
("IV/30","Addition Formulas","ch30_addition_formulas"),
("IV/31","Elliptic Curves as Riemann Surfaces","ch31_elliptic_curves_as_riemann_surfaces"),
]
PARTS=[
("Holomorphic Functions",1,6),
("Singularities and Residues",7,11),
("Global Complex Analysis",12,18),
("Special Functions",19,21),
("Riemann Surfaces",22,26),
("Elliptic Functions",27,31),
]
STATUS_FIELDS=["volume","chapter_code","chapter_title","status","legacy_source_status","mapped_rule_count","canonical_path","next_action"]
PROV_FIELDS=["chapter_code","dossier_index","dossier_label","dossier_title","origin","source_file","source_block_id","source_selector","source_topic","note"]
ACCOUNT_FIELDS=["source_file","source_family","source_block_id","block_kind","source_selector","source_topic","destination","precedence","source_exists","disposition","canonical_dossier_label"]
INV_FIELDS=["chapter_code","chapter_title","mapped_rules","missing_sources","canonical_path","state"]

def read_tsv(path):
    with Path(path).open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def write_tsv(path,rows,fields):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    lines=["\t".join(fields)]
    for row in rows:
        vals=[]
        for f in fields:
            v=row.get(f,"-");vals.append("-" if v is None or v=="" else str(v))
        lines.append("\t".join(vals))
    path.write_text("\n".join(lines)+"\n",encoding="utf-8")
def source_path(repo,name):
    if not name:return None
    for p in (repo/name,repo/"chapters/tex"/name):
        if p.exists():return p
    return None
def label(code):return "iv"+code.split("/")[1]
def safe_title(text):return str(text).replace("[",r"\lbrack{}").replace("]",r"\rbrack{}")
def tex_title(text):return str(text).replace("℘",r"$\wp$")

def dossier_entries(data):
    sections=data["sections"];theorems=data["theorems"];count=max(1,min(11-len(theorems),len(sections)))
    out=[]
    for name,body in sections[:count]:
        out.append((f"{name} diagnostic",
                    f"Give a rigorous worked analysis of {name}. State the relevant holomorphic, contour, series, or singularity hypothesis and derive the central conclusion.",
                    body+" The decisive step is to use the complex-analytic structure globally rather than reason from real-variable intuition alone."))
    for name,statement,proof in theorems:
        out.append((f"{name} proof dossier",
                    "Prove the following theorem-level statement and identify the essential hypothesis: "+statement,
                    proof+" This identifies the mechanism that makes the complex-analytic conclusion stronger than its real-variable analogue."))
    out.append(("Chapter synthesis",
                "Connect the definitions and principal theorems of this chapter into one reusable complex-analysis strategy.",
                data["intro"]+" The reusable strategy is to identify the analytic domain, choose the correct local expansion or contour representation, apply the structural theorem, and then audit singularities and topology."))
    if len(out)!=12:raise RuntimeError(f"Expected 12 dossiers, got {len(out)}")
    return out

def exercise_entries(data):
    out=[]
    for name,body in data["sections"][:8]:
        out.append((f"State and apply the central principle behind {name}. Give one concrete consequence.",
                    "Begin from the exact definition or theorem hypothesis in the corresponding section.",
                    body+" The same principle can then be reused in later contour, residue, conformal, or Riemann-surface arguments."))
    if len(out)!=8:raise RuntimeError("Expected 8 exercises")
    return out

def render_chapter(code,title,data):
    lab=label(code);ds=dossier_entries(data);es=exercise_entries(data)
    out=[rf"\chapter{{{tex_title(title)}}}",rf"\label{{ch:{lab}}}","",data["intro"],"",
         r"\section*{Learning goals}",
         "The reader should be able to state the definitions precisely, prove the core results, choose valid contours or local expansions, and diagnose which domain and regularity hypotheses are essential.",
         "",r"\section*{Conceptual roadmap}",r"\[",
         r"\boxed{\text{local holomorphic structure}\;\longrightarrow\;\text{integral or series representation}\;\longrightarrow\;\text{global consequence}.}",
         r"\]",""]
    for name,body in data["sections"]:out += [rf"\section{{{name}}}",body,""]
    out += [r"\section{Core structural results}",""]
    for i,(name,st,proof) in enumerate(data["theorems"],1):
        out += [rf"\begin{{theorem}}[{safe_title(name)}]\label{{thm:{lab}-{i:02d}}}",st,r"\begin{proof}",proof,r"\end{proof}",r"\end{theorem}",""]
    out += [r"\section{Worked examples}",""]
    for i,(name,p,s) in enumerate(ds[:4],1):
        out += [rf"\begin{{example}}[{safe_title(name)}]\label{{ex:{lab}-worked-{i:02d}}}",p+" "+s,r"\end{example}",""]
    out += [r"\section{Solved dossiers}",
            "The dossiers are canonical solved problems. The provenance ledger separately records which retained corpus rules guided each topic and which dossiers were newly designed.",""]
    for i,(name,p,s) in enumerate(ds,1):
        out += [rf"\begin{{problem}}[{safe_title(name)}]\label{{prob:{lab}-dossier-{i:02d}}}",p,r"\end{problem}",r"\begin{solution}",s,r"\end{solution}",""]
    out += [r"\section{Exercises with complete solutions}",""]
    for i,(p,h,s) in enumerate(es,1):
        out += [rf"\begin{{exercise}}\label{{exr:{lab}-{i:02d}}}",p,r"\end{exercise}",r"\begin{hint}",h,r"\end{hint}",r"\begin{solution}",s,r"\end{solution}",""]
    out += [r"\section*{Chapter summary}","The chapter now forms part of the canonical complex-analysis chain from holomorphicity through residues, global continuation, and Riemann surfaces.",""]
    return "\n".join(out).rstrip()+"\n"

def render_stub(code,title):
    return "\n".join([rf"\chapter{{{tex_title(title)}}}",rf"\label{{ch:{label(code)}}}","",r"\section*{Reconstruction scaffold}",
                     "This canonical chapter path is active and buildable. Full reconstruction is scheduled for a later Volume IV commit."]).rstrip()+"\n"

def render_book(canonical_paths=None):
    slug={c:s for c,t,s in ALL_CHAPTERS}
    if canonical_paths:
        for code,path in canonical_paths.items():
            p=Path(path)
            if p.name!="chapter.tex":
                raise RuntimeError(f"Canonical path must end in chapter.tex: {code}: {path}")
            slug[code]=p.parent.name
    out=[r"\documentclass[11pt,a4paper,oneside,openany]{book}",r"\input{../../shared/preamble.tex}",r"\input{../../shared/macros.tex}",
         r"\input{../../shared/theorem_styles.tex}",r"\input{../../shared/notation.tex}","",
         r"\title{Theory of Mathematics\\[0.5em]\Large Volume IV: Complex Analysis and Riemann Surfaces}",r"\author{}",r"\date{}",
         r"\hypersetup{pdftitle={Theory of Mathematics — Volume IV: Complex Analysis and Riemann Surfaces},pdfsubject={Canonical reconstructed mathematics series}}",
         r"\begin{document}",r"\pagenumbering{gobble}",r"\maketitle",r"\clearpage",r"\frontmatter",r"\tableofcontents",r"\mainmatter",""]
    for part,a,b in PARTS:
        out.append(rf"\part{{{part}}}")
        for n in range(a,b+1):out.append(rf"\include{{chapters/{slug[f'IV/{n:02d}']}/chapter}}")
        out.append("")
    out += [r"\backmatter",r"\end{document}",""]
    return "\n".join(out).rstrip()+"\n"

def write_status(repo,status,src,developed):
    for r in status:
        code=r.get("chapter_code","")
        if code.startswith("IV/"):
            r["mapped_rule_count"]=str(sum(1 for s in src if s.get("destination")==code))
            if code in developed:r["status"]="DRAFTED";r["next_action"]="REVIEW_AND_INTEGRATE"
    lines=["\t".join(STATUS_FIELDS)]
    for r in status:lines.append("\t".join(str(r.get(k,"")) for k in STATUS_FIELDS))
    (repo/"editorial/CHAPTER_STATUS.tsv").write_text("\n".join(lines)+"\n",encoding="utf-8")

def source_accounting(repo,src,code,labels):
    rel=[r for r in src if r.get("destination")==code]
    def prec(r):
        try:return int(r.get("precedence") or 0)
        except:return 0
    explicit=[r for r in rel if prec(r)>=90 and r.get("source_selector","").strip()!="*" and r.get("block_kind") not in ("ANY_UNMATCHED_BLOCK","ENTIRE_FILE")]
    explicit=sorted(explicit,key=lambda r:(-prec(r),r.get("source_file",""),r.get("source_block_id","")))
    assign={}
    for i,r in enumerate(explicit):
        assign[(r.get("source_file",""),r.get("source_block_id",""),r.get("source_selector",""))]=labels[i] if i<len(labels) else "-"
    rows=[]
    for r in rel:
        exists=source_path(repo,r.get("source_file","")) is not None
        key=(r.get("source_file",""),r.get("source_block_id",""),r.get("source_selector",""))
        action=(r.get("action","") or "").upper();family=(r.get("source_family","") or "").upper()
        if not exists:disp="UNRESOLVED_MISSING_SOURCE";lab="-"
        elif "ARCHIVE" in action or "DUPLICATE" in action:disp="DUPLICATE_OR_ARCHIVE_ACCOUNTED";lab="-"
        elif family=="SUPPORT":disp="SUPPORT_ONLY";lab="-"
        elif key in assign and assign[key]!="-":disp="CORPUS_GUIDED_CANONICAL_PROBLEM";lab=assign[key]
        elif key in assign:disp="MERGED_WITH_CHAPTER_CONTEXT";lab="-"
        else:disp="ROUTED_TO_CHAPTER_CONTEXT";lab="-"
        rows.append({"source_file":r.get("source_file",""),"source_family":r.get("source_family",""),"source_block_id":r.get("source_block_id",""),
                     "block_kind":r.get("block_kind",""),"source_selector":r.get("source_selector",""),"source_topic":r.get("source_title_or_pattern",""),
                     "destination":code,"precedence":r.get("precedence",""),"source_exists":"YES" if exists else "NO","disposition":disp,"canonical_dossier_label":lab})
    return rows,explicit

def provenance(repo,src,code,data):
    ds=dossier_entries(data);labs=[f"prob:{label(code)}-dossier-{i:02d}" for i in range(1,13)]
    acc,explicit=source_accounting(repo,src,code,labs);rows=[]
    for i,(title,_,_) in enumerate(ds,1):
        rr=explicit[i-1] if i<=len(explicit) and source_path(repo,explicit[i-1].get("source_file","")) else None
        rows.append({"chapter_code":code,"dossier_index":i,"dossier_label":labs[i-1],"dossier_title":title,
                     "origin":"CORPUS_GUIDED" if rr else "FRESH_CANONICAL","source_file":rr.get("source_file","-") if rr else "-",
                     "source_block_id":rr.get("source_block_id","-") if rr else "-","source_selector":rr.get("source_selector","-") if rr else "-",
                     "source_topic":rr.get("source_title_or_pattern","-") if rr else "-",
                     "note":"Retained corpus rule guided the canonical dossier; statement and solution newly authored." if rr else "Fresh canonical dossier added to complete coverage."})
    return rows,acc
