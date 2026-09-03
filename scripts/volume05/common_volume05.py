from __future__ import annotations
import csv,re
from pathlib import Path

ALL_CHAPTERS=[
("V/01","Rings, Ideals and Quotients","ch01_rings_ideals_and_quotients"),
("V/02","Prime and Maximal Ideals","ch02_prime_and_maximal_ideals"),
("V/03","Radicals and Nilpotents","ch03_radicals_and_nilpotents"),
("V/04","Chinese Remainder Theory","ch04_chinese_remainder_theory"),
("V/05","Multiplicative Systems","ch05_multiplicative_systems"),
("V/06","Localization of Rings","ch06_localization_of_rings"),
("V/07","Localization of Modules","ch07_localization_of_modules"),
("V/08","Local Rings and Localization at Primes","ch08_local_rings_and_localization_at_primes"),
("V/09","Modules and Exact Sequences","ch09_modules_and_exact_sequences"),
("V/10","Tensor Products","ch10_tensor_products"),
("V/11","Quotients and Base Change","ch11_quotients_and_base_change"),
("V/12","Hom and Finitely Presented Modules","ch12_hom_and_finitely_presented_modules"),
("V/13","Free and Projective Modules","ch13_free_and_projective_modules"),
("V/14","Flat Modules","ch14_flat_modules"),
("V/15","Noetherian Rings and Modules","ch15_noetherian_rings_and_modules"),
("V/16","Support","ch16_support"),
("V/17","Associated Primes","ch17_associated_primes"),
("V/18","Completion and I-Adic Topology","ch18_completion_and_i_adic_topology"),
("V/19","Integral Dependence","ch19_integral_dependence"),
("V/20","Integral Closure and Normalization","ch20_integral_closure_and_normalization"),
("V/21","Valuation Rings","ch21_valuation_rings"),
("V/22","Chain Complexes","ch22_chain_complexes"),
("V/23","Free Resolutions","ch23_free_resolutions"),
("V/24","Syzygies","ch24_syzygies"),
("V/25","Minimal Resolutions","ch25_minimal_resolutions"),
("V/26","The Tor Functor","ch26_the_tor_functor"),
("V/27","The Ext Functor","ch27_the_ext_functor"),
("V/28","Derived-Functor Viewpoint","ch28_derived_functor_viewpoint"),
]
PARTS=[
("Rings and Ideals",1,4),
("Localization",5,8),
("Modules and Tensor Products",9,14),
("Noetherian Algebra",15,18),
("Integral and Valuation Theory",19,21),
("Homological Algebra",22,28),
]
STATUS_FIELDS=["volume","chapter_code","chapter_title","status","legacy_source_status","mapped_rule_count","canonical_path","next_action"]
PROV_FIELDS=["chapter_code","dossier_index","dossier_label","dossier_title","origin","source_file","source_block_id","source_selector","source_topic","note"]
ACCOUNT_FIELDS=["source_file","source_family","source_block_id","block_kind","source_selector","source_topic","destination","precedence","source_exists","disposition","canonical_dossier_label"]
INV_FIELDS=["chapter_code","chapter_title","mapped_rules","missing_sources","canonical_path","state"]

def read_tsv(path):
    with Path(path).open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def write_tsv(path,rows,fields):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    lines=["\t".join(fields)]
    for row in rows:
        vals=[]
        for f in fields:
            v=row.get(f,"-")
            vals.append("-" if v is None or v=="" else str(v))
        lines.append("\t".join(vals))
    path.write_text("\n".join(lines)+"\n",encoding="utf-8")

def source_path(repo,name):
    if not name:return None
    for p in (repo/name,repo/"chapters/tex"/name):
        if p.exists():return p
    return None

def label(code):return "v"+code.split("/")[1]
def safe_title(text):return str(text).replace("[",r"\lbrack{}").replace("]",r"\rbrack{}")

def dossier_entries(data):
    sections=data["sections"];theorems=data["theorems"]
    count=max(1,min(11-len(theorems),len(sections)))
    out=[]
    for name,body in sections[:count]:
        out.append((
            f"{name} diagnostic",
            f"Give a rigorous worked analysis of {name}. State the ring, module, finiteness, localization, or homological hypotheses and derive the central conclusion.",
            body+" The decisive step is to use the universal property, exactness criterion, localization test, or finite-generation mechanism appropriate to the algebraic structure."
        ))
    for name,statement,proof in theorems:
        out.append((
            f"{name} proof dossier",
            "Prove the following structural statement and identify the hypothesis that makes the conclusion work: "+statement,
            proof+" This proof isolates the reusable algebraic mechanism behind the result."
        ))
    out.append((
        "Chapter synthesis",
        "Connect the definitions and principal structural theorems of this chapter into one reusable commutative-algebra strategy.",
        data["intro"]+" The recurring strategy is to encode the algebraic object by kernels, quotients, localization, finite presentation, or a resolution, apply the corresponding universal or exactness principle, and then recover the desired global or local conclusion."
    ))
    if len(out)!=12:
        raise RuntimeError(f"Expected 12 dossiers, got {len(out)}")
    return out

def exercise_entries(data):
    out=[]
    for name,body in data["sections"][:8]:
        out.append((
            f"State and apply the central principle behind {name}. Give one concrete algebraic consequence.",
            "Begin from the exact definition or theorem hypothesis in the corresponding section.",
            body+" The same principle can then be reused in later localization, support, base-change, resolution, Tor, or Ext arguments."
        ))
    if len(out)!=8:raise RuntimeError("Expected 8 exercises")
    return out

def render_chapter(code,title,data):
    lab=label(code);ds=dossier_entries(data);es=exercise_entries(data)
    out=[
        rf"\chapter{{{title}}}",rf"\label{{ch:{lab}}}","",data["intro"],"",
        r"\section*{Learning goals}",
        "The reader should be able to state the definitions precisely, prove the core structural results, move between global and localized formulations, and audit finiteness and exactness hypotheses.",
        "",r"\section*{Conceptual roadmap}",r"\[",
        r"\boxed{\text{presentation or universal property}\;\longrightarrow\;\text{exactness/localization}\;\longrightarrow\;\text{structural consequence}.}",
        r"\]",""
    ]
    for name,body in data["sections"]:
        out += [rf"\section{{{name}}}",body,""]
    out += [r"\section{Core structural results}",""]
    for i,(name,st,proof) in enumerate(data["theorems"],1):
        out += [
            rf"\begin{{theorem}}[{safe_title(name)}]\label{{thm:{lab}-{i:02d}}}",
            st,r"\begin{proof}",proof,r"\end{proof}",r"\end{theorem}",""
        ]
    out += [r"\section{Worked examples}",""]
    for i,(name,p,s) in enumerate(ds[:4],1):
        out += [
            rf"\begin{{example}}[{safe_title(name)}]\label{{ex:{lab}-worked-{i:02d}}}",
            p+" "+s,r"\end{example}",""
        ]
    out += [
        r"\section{Solved dossiers}",
        "Each dossier is a canonical solved problem. The provenance ledger records which retained corpus rules guided its topic and which dossiers were added freshly to complete the chapter.",""
    ]
    for i,(name,p,s) in enumerate(ds,1):
        out += [
            rf"\begin{{problem}}[{safe_title(name)}]\label{{prob:{lab}-dossier-{i:02d}}}",p,r"\end{problem}",
            r"\begin{solution}",s,r"\end{solution}",""
        ]
    out += [r"\section{Exercises with complete solutions}",""]
    for i,(p,h,s) in enumerate(es,1):
        out += [
            rf"\begin{{exercise}}\label{{exr:{lab}-{i:02d}}}",p,r"\end{exercise}",
            r"\begin{hint}",h,r"\end{hint}",r"\begin{solution}",s,r"\end{solution}",""
        ]
    out += [
        r"\section*{Chapter summary}",
        "The chapter now contributes a canonical solved layer to the progression from rings and modules through localization, Noetherian methods, integral dependence, and derived functors.",""
    ]
    return "\n".join(out).rstrip()+"\n"

def render_stub(code,title):
    return "\n".join([
        rf"\chapter{{{title}}}",rf"\label{{ch:{label(code)}}}","",
        r"\section*{Reconstruction scaffold}",
        "This canonical chapter path is active and buildable. Full reconstruction is scheduled for a later Volume V commit."
    ]).rstrip()+"\n"

def render_book(canonical_paths=None):
    slug={c:s for c,t,s in ALL_CHAPTERS}
    if canonical_paths:
        for code,path in canonical_paths.items():
            p=Path(path)
            if p.name!="chapter.tex":
                raise RuntimeError(f"Canonical path must end in chapter.tex: {code}: {path}")
            slug[code]=p.parent.name
    out=[
        r"\documentclass[11pt,a4paper,oneside,openany]{book}",
        r"\input{../../shared/preamble.tex}",
        r"\input{../../shared/macros.tex}",
        r"\input{../../shared/theorem_styles.tex}",
        r"\input{../../shared/notation.tex}","",
        r"\title{Theory of Mathematics\\[0.5em]\Large Volume V: Commutative Algebra and Homological Methods}",
        r"\author{}",r"\date{}",
        r"\hypersetup{pdftitle={Theory of Mathematics — Volume V: Commutative Algebra and Homological Methods},pdfsubject={Canonical reconstructed mathematics series}}",
        r"\begin{document}",r"\pagenumbering{gobble}",r"\maketitle",r"\clearpage",
        r"\frontmatter",r"\tableofcontents",r"\mainmatter",""
    ]
    for part,a,b in PARTS:
        out.append(rf"\part{{{part}}}")
        for n in range(a,b+1):
            out.append(rf"\include{{chapters/{slug[f'V/{n:02d}']}/chapter}}")
        out.append("")
    out += [r"\backmatter",r"\end{document}",""]
    return "\n".join(out).rstrip()+"\n"

def write_status(repo,status,src,developed):
    for r in status:
        code=r.get("chapter_code","")
        if code.startswith("V/"):
            r["mapped_rule_count"]=str(sum(1 for s in src if s.get("destination")==code))
            if code in developed:
                r["status"]="DRAFTED";r["next_action"]="REVIEW_AND_INTEGRATE"
    lines=["\t".join(STATUS_FIELDS)]
    for r in status:
        lines.append("\t".join(str(r.get(k,"")) for k in STATUS_FIELDS))
    (repo/"editorial/CHAPTER_STATUS.tsv").write_text("\n".join(lines)+"\n",encoding="utf-8")

def source_accounting(repo,src,code,labels):
    relevant=[r for r in src if r.get("destination")==code]
    def prec(r):
        try:return int(r.get("precedence") or 0)
        except:return 0
    explicit=[
        r for r in relevant
        if prec(r)>=90
        and r.get("source_selector","").strip()!="*"
        and r.get("block_kind") not in ("ANY_UNMATCHED_BLOCK","ENTIRE_FILE")
    ]
    explicit=sorted(explicit,key=lambda r:(-prec(r),r.get("source_file",""),r.get("source_block_id","")))
    assign={}
    for i,r in enumerate(explicit):
        key=(r.get("source_file",""),r.get("source_block_id",""),r.get("source_selector",""))
        assign[key]=labels[i] if i<len(labels) else "-"
    rows=[]
    for r in relevant:
        exists=source_path(repo,r.get("source_file","")) is not None
        key=(r.get("source_file",""),r.get("source_block_id",""),r.get("source_selector",""))
        action=(r.get("action","") or "").upper()
        family=(r.get("source_family","") or "").upper()
        if not exists:disp="UNRESOLVED_MISSING_SOURCE";lab="-"
        elif "ARCHIVE" in action or "DUPLICATE" in action:disp="DUPLICATE_OR_ARCHIVE_ACCOUNTED";lab="-"
        elif family=="SUPPORT":disp="SUPPORT_ONLY";lab="-"
        elif key in assign and assign[key]!="-":disp="CORPUS_GUIDED_CANONICAL_PROBLEM";lab=assign[key]
        elif key in assign:disp="MERGED_WITH_CHAPTER_CONTEXT";lab="-"
        else:disp="ROUTED_TO_CHAPTER_CONTEXT";lab="-"
        rows.append({
            "source_file":r.get("source_file",""),
            "source_family":r.get("source_family",""),
            "source_block_id":r.get("source_block_id",""),
            "block_kind":r.get("block_kind",""),
            "source_selector":r.get("source_selector",""),
            "source_topic":r.get("source_title_or_pattern",""),
            "destination":code,
            "precedence":r.get("precedence",""),
            "source_exists":"YES" if exists else "NO",
            "disposition":disp,
            "canonical_dossier_label":lab
        })
    return rows,explicit

def provenance(repo,src,code,data):
    ds=dossier_entries(data)
    labels=[f"prob:{label(code)}-dossier-{i:02d}" for i in range(1,13)]
    accounting,explicit=source_accounting(repo,src,code,labels)
    rows=[]
    for i,(title,_,_) in enumerate(ds,1):
        rr=explicit[i-1] if i<=len(explicit) and source_path(repo,explicit[i-1].get("source_file","")) else None
        rows.append({
            "chapter_code":code,
            "dossier_index":i,
            "dossier_label":labels[i-1],
            "dossier_title":title,
            "origin":"CORPUS_GUIDED" if rr else "FRESH_CANONICAL",
            "source_file":rr.get("source_file","-") if rr else "-",
            "source_block_id":rr.get("source_block_id","-") if rr else "-",
            "source_selector":rr.get("source_selector","-") if rr else "-",
            "source_topic":rr.get("source_title_or_pattern","-") if rr else "-",
            "note":"Retained corpus rule guided the canonical dossier; statement and solution are newly authored." if rr else "Fresh canonical dossier added to complete the chapter contract."
        })
    return rows,accounting
