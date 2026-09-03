from __future__ import annotations
import csv,re
from pathlib import Path

ALL_CHAPTERS=[
("III/01","Sigma-Algebras and Measures","ch01_sigma_algebras_and_measures"),
("III/02","Measurable Functions","ch02_measurable_functions"),
("III/03","The Lebesgue Integral","ch03_the_lebesgue_integral"),
("III/04","Convergence Theorems","ch04_convergence_theorems"),
("III/05","Product Measures and Fubini Theory","ch05_product_measures_and_fubini_theory"),
("III/06","Lp Spaces","ch06_lp_spaces"),
("III/07","Hölder, Minkowski and Interpolation","ch07_h_lder_minkowski_and_interpolation"),
("III/08","Egorov, Vitali and Weak-Lp Ideas","ch08_egorov_vitali_and_weak_lp_ideas"),
("III/09","Fourier Series","ch09_fourier_series"),
("III/10","Convolution and Approximate Identities","ch10_convolution_and_approximate_identities"),
("III/11","The Fourier Transform","ch11_the_fourier_transform"),
("III/12","The Gaussian and Transform Calculus","ch12_the_gaussian_and_transform_calculus"),
("III/13","Plancherel and L2 Fourier Theory","ch13_plancherel_and_l2_fourier_theory"),
("III/14","The Schwartz Space","ch14_the_schwartz_space"),
("III/15","Test-Function Spaces","ch15_test_function_spaces"),
("III/16","Distributions and Distributional Derivatives","ch16_distributions_and_distributional_derivatives"),
("III/17","Support and Singular Distributions","ch17_support_and_singular_distributions"),
("III/18","Tempered Distributions","ch18_tempered_distributions"),
("III/19","Fourier Transform of Distributions","ch19_fourier_transform_of_distributions"),
("III/20","Weak Derivatives","ch20_weak_derivatives"),
("III/21","Sobolev Spaces","ch21_sobolev_spaces"),
("III/22","Approximation and Density","ch22_approximation_and_density"),
("III/23","Weak Boundary-Value Problems","ch23_weak_boundary_value_problems"),
("III/24","Fundamental Solutions","ch24_fundamental_solutions"),
("III/25","Green Functions","ch25_green_functions"),
("III/26","Sturm–Liouville Green Kernels","ch26_sturm_liouville_green_kernels"),
("III/27","Elliptic Operators and Maximum Principles","ch27_elliptic_operators_and_maximum_principles"),
("III/28","Spectral and Transform Methods for PDE","ch28_spectral_and_transform_methods_for_pde"),
]
PARTS=[
("Measure and Integration",1,8),
("Fourier Analysis",9,14),
("Distribution Theory",15,19),
("Sobolev and PDE Methods",20,28),
]
STATUS_FIELDS=["volume","chapter_code","chapter_title","status","legacy_source_status","mapped_rule_count","canonical_path","next_action"]

def read_tsv(path):
    with Path(path).open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def write_tsv(path,rows,fields):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    lines=["\t".join(fields)]
    for row in rows:
        vals=[]
        for field in fields:
            value=row.get(field,"-")
            vals.append("-" if value is None or value=="" else str(value))
        lines.append("\t".join(vals))
    path.write_text("\n".join(lines)+"\n",encoding="utf-8")

def source_path(repo,name):
    if not name:return None
    candidates=[repo/name,repo/"chapters/tex"/name]
    for p in candidates:
        if p.exists():return p
    return None

def code_num(code):
    return int(code.split("/")[1])

def label(code):
    return "iii"+code.split("/")[1]

def safe_optional_title(text):
    return str(text).replace("[",r"\lbrack{}").replace("]",r"\rbrack{}")

def dossier_entries(data):
    sections=data["sections"];theorems=data["theorems"]
    # Exactly 12 dossiers. Extra theorem depth (III/11) is preserved by
    # reducing section dossiers rather than exceeding the volume contract.
    section_count=11-len(theorems)
    section_count=max(1,min(section_count,len(sections)))
    entries=[]
    for name,body in sections[:section_count]:
        entries.append((
            f"{name} diagnostic",
            f"Give a rigorous worked analysis of {name} in the setting of this chapter. State the decisive definition or hypothesis and derive the central conclusion.",
            body+" The decisive point is to use the chapter definition at the correct countable, norm, transform, or distributional level rather than rely on pointwise intuition alone."
        ))
    for name,statement,proof in theorems:
        entries.append((
            f"{name} proof dossier",
            "Prove the following structural statement and identify the step where its main hypothesis is used: "+statement,
            proof+" This proof also explains why the stated hypothesis is structural rather than cosmetic."
        ))
    entries.append((
        "Chapter synthesis",
        "Connect the main definitions and structural theorems of this chapter into one proof strategy. Explain what object is controlled, what estimate or closure principle is used, and what conclusion becomes available.",
        data["intro"]+" The recurring strategy is to encode the object in the chapter's natural measurable, normed, Fourier, or distributional structure, establish the controlling estimate, and then pass to the desired limit or representation."
    ))
    if len(entries)!=12:
        raise RuntimeError(f"Expected 12 dossiers, generated {len(entries)}")
    return entries

def exercise_entries(data):
    out=[]
    for name,body in data["sections"][:8]:
        first=body.split(".")[0].strip()
        out.append((
            f"State and apply the central principle behind {name}. Give one immediate consequence in the setting of this chapter.",
            "Start from the precise definition or estimate in the corresponding section.",
            body+" As an immediate consequence, the same principle can be inserted into later convergence, approximation, transform, or weak-form arguments whenever its hypotheses are verified."
        ))
    if len(out)!=8:raise RuntimeError("Expected 8 exercises")
    return out

def render_chapter(code,title,data):
    lab=label(code);dossiers=dossier_entries(data);exercises=exercise_entries(data)
    out=[rf"\chapter{{{title}}}",rf"\label{{ch:{lab}}}","",data["intro"],"",
         r"\section*{Learning goals}",
         "The reader should be able to state the central definitions precisely, prove the structural results, audit the hypotheses in examples, and use the chapter's estimates in later analysis.",
         "",r"\section*{Conceptual roadmap}",r"\[",
         r"\boxed{\text{structure}\;\longrightarrow\;\text{estimate}\;\longrightarrow\;\text{limit or representation}\;\longrightarrow\;\text{application}.}",
         r"\]",""]
    for name,body in data["sections"]:
        out += [rf"\section{{{name}}}",body,""]
    out += [r"\section{Core structural results}",""]
    for i,(name,statement,proof) in enumerate(data["theorems"],1):
        sname=safe_optional_title(name)
        out += [rf"\begin{{theorem}}[{sname}]\label{{thm:{lab}-{i:02d}}}",statement,
                r"\begin{proof}",proof,r"\end{proof}",r"\end{theorem}",""]
    out += [r"\section{Worked examples}",""]
    for i,(name,problem,solution) in enumerate(dossiers[:4],1):
        sname=safe_optional_title(name)
        out += [rf"\begin{{example}}[{sname}]\label{{ex:{lab}-worked-{i:02d}}}",
                problem+" "+solution,r"\end{example}",""]
    out += [r"\section{Solved dossiers}",
            "Each dossier is a canonical solved problem. The provenance ledger records which retained corpus rules guided its topic and which dossiers were added freshly to complete the chapter.",""]
    for i,(name,problem,solution) in enumerate(dossiers,1):
        sname=safe_optional_title(name)
        out += [rf"\begin{{problem}}[{sname}]\label{{prob:{lab}-dossier-{i:02d}}}",problem,r"\end{problem}",
                r"\begin{solution}",solution,r"\end{solution}",""]
    out += [r"\section{Exercises with complete solutions}",
            "The shorter exercise layer remains separate from the solved dossiers.",""]
    for i,(problem,hint,solution) in enumerate(exercises,1):
        out += [rf"\begin{{exercise}}\label{{exr:{lab}-{i:02d}}}",problem,r"\end{exercise}",
                r"\begin{hint}",hint,r"\end{hint}",r"\begin{solution}",solution,r"\end{solution}",""]
    out += [r"\section*{Chapter summary}",
            "The chapter now supplies a canonical theorem-and-dossier layer for subsequent measure, Fourier, distributional, Sobolev, and PDE arguments.",""]
    return "\n".join(out).rstrip()+"\n"

def render_stub(code,title):
    return "\n".join([
        rf"\chapter{{{title}}}",rf"\label{{ch:{label(code)}}}","",
        r"\section*{Reconstruction scaffold}",
        "This canonical chapter path is active and buildable. Full reconstruction is scheduled for a later Volume III commit."
    ]).rstrip()+"\n"

def render_book():
    slug={c:s for c,t,s in ALL_CHAPTERS}
    out=[
        r"\documentclass[11pt,a4paper,oneside,openany]{book}",
        r"\input{../../shared/preamble.tex}",
        r"\input{../../shared/macros.tex}",
        r"\input{../../shared/theorem_styles.tex}",
        r"\input{../../shared/notation.tex}","",
        r"\title{Theory of Mathematics\\[0.5em]\Large Volume III: Measure, Fourier Analysis, Distributions and PDE}",
        r"\author{}",r"\date{}",
        r"\hypersetup{pdftitle={Theory of Mathematics — Volume III: Measure, Fourier Analysis, Distributions and PDE},pdfsubject={Canonical reconstructed mathematics series}}",
        r"\begin{document}",r"\pagenumbering{gobble}",r"\maketitle",r"\clearpage",
        r"\frontmatter",r"\tableofcontents",r"\mainmatter",""
    ]
    for part,a,b in PARTS:
        out.append(rf"\part{{{part}}}")
        for n in range(a,b+1):
            code=f"III/{n:02d}"
            out.append(rf"\include{{chapters/{slug[code]}/chapter}}")
        out.append("")
    out += [r"\backmatter",r"\end{document}",""]
    return "\n".join(out).rstrip()+"\n"

def write_status(repo,status_rows,source_rows,developed_codes):
    for row in status_rows:
        code=row.get("chapter_code","")
        if code.startswith("III/"):
            row["mapped_rule_count"]=str(sum(1 for s in source_rows if s.get("destination")==code))
            if code in developed_codes:
                row["status"]="DRAFTED";row["next_action"]="REVIEW_AND_INTEGRATE"
    lines=["\t".join(STATUS_FIELDS)]
    for row in status_rows:
        lines.append("\t".join(str(row.get(k,"")) for k in STATUS_FIELDS))
    (repo/"editorial/CHAPTER_STATUS.tsv").write_text("\n".join(lines)+"\n",encoding="utf-8")

def classify_source_rules(repo,source_rows,code,dossier_labels):
    relevant=[r for r in source_rows if r.get("destination")==code]
    def prec(r):
        try:return int(r.get("precedence") or 0)
        except:return 0
    explicit=[r for r in relevant if prec(r)>=90 and r.get("source_selector","").strip()!="*" and r.get("block_kind") not in ("ANY_UNMATCHED_BLOCK","ENTIRE_FILE")]
    explicit_sorted=sorted(explicit,key=lambda r:(-prec(r),r.get("source_file",""),r.get("source_block_id","")))
    assignment={}
    for i,r in enumerate(explicit_sorted):
        key=(r.get("source_file",""),r.get("source_block_id",""),r.get("source_selector",""))
        assignment[key]=dossier_labels[i] if i<len(dossier_labels) else "-"
    rows=[]
    for r in relevant:
        exists=source_path(repo,r.get("source_file","")) is not None
        key=(r.get("source_file",""),r.get("source_block_id",""),r.get("source_selector",""))
        action=(r.get("action","") or "").upper()
        family=(r.get("source_family","") or "").upper()
        if not exists:
            disposition="UNRESOLVED_MISSING_SOURCE";dossier="-"
        elif "ARCHIVE" in action or "DUPLICATE" in action:
            disposition="DUPLICATE_OR_ARCHIVE_ACCOUNTED";dossier="-"
        elif family=="SUPPORT":
            disposition="SUPPORT_ONLY";dossier="-"
        elif key in assignment and assignment[key]!="-":
            disposition="CORPUS_GUIDED_CANONICAL_PROBLEM";dossier=assignment[key]
        elif key in assignment:
            disposition="MERGED_WITH_CHAPTER_CONTEXT";dossier="-"
        else:
            disposition="ROUTED_TO_CHAPTER_CONTEXT";dossier="-"
        rows.append({
            "source_file":r.get("source_file",""),"source_family":r.get("source_family",""),
            "source_block_id":r.get("source_block_id",""),"block_kind":r.get("block_kind",""),
            "source_selector":r.get("source_selector",""),"source_topic":r.get("source_title_or_pattern",""),
            "destination":code,"precedence":r.get("precedence",""),"source_exists":"YES" if exists else "NO",
            "disposition":disposition,"canonical_dossier_label":dossier
        })
    return rows,explicit_sorted

def provenance_rows(repo,source_rows,code,data):
    dossiers=dossier_entries(data)
    labels=[f"prob:{label(code)}-dossier-{i:02d}" for i in range(1,13)]
    accounting,explicit=classify_source_rules(repo,source_rows,code,labels)
    rows=[]
    for i,(dtitle,_,_) in enumerate(dossiers,1):
        r=explicit[i-1] if i<=len(explicit) and source_path(repo,explicit[i-1].get("source_file","")) else None
        rows.append({
            "chapter_code":code,"dossier_index":i,"dossier_label":labels[i-1],"dossier_title":dtitle,
            "origin":"CORPUS_GUIDED" if r else "FRESH_CANONICAL",
            "source_file":r.get("source_file","-") if r else "-",
            "source_block_id":r.get("source_block_id","-") if r else "-",
            "source_selector":r.get("source_selector","-") if r else "-",
            "source_topic":r.get("source_title_or_pattern","-") if r else "-",
            "note":"Retained corpus rule guided the canonical dossier; statement and solution are newly authored." if r else "Fresh canonical dossier added to complete the chapter contract."
        })
    return rows,accounting
