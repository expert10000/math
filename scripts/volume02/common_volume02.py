from __future__ import annotations
import csv,re
from pathlib import Path

FIELDS=["volume","chapter_code","chapter_title","status","legacy_source_status","mapped_rule_count","canonical_path","next_action"]

def read_tsv(p):
    with p.open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def write_tsv(p,rows,fields):
    p.parent.mkdir(parents=True,exist_ok=True)
    lines=["\t".join(fields)]
    for r in rows:
        vals=[]
        for k in fields:
            v=r.get(k,"-")
            vals.append("-" if v is None or v=="" else str(v))
        lines.append("\t".join(vals))
    p.write_text("\n".join(lines)+"\n",encoding="utf-8")

def source_path(repo,name):
    if not name:return None
    for p in (repo/name,repo/"chapters/tex"/name):
        if p.exists():return p
    return None

def explicit_guides(repo,source_rows,code):
    found=[]
    for r in source_rows:
        if r.get("destination")!=code:continue
        try:prec=int(r.get("precedence") or "0")
        except:prec=0
        if prec<90:continue
        if r.get("source_selector","").strip()=="*":continue
        if r.get("block_kind") in ("ANY_UNMATCHED_BLOCK","ENTIRE_FILE"):continue
        if not source_path(repo,r.get("source_file","")):continue
        found.append((prec,r))
    found.sort(key=lambda z:(-z[0],z[1].get("source_file",""),z[1].get("source_block_id","")))
    out=[];seen=set()
    for _,r in found:
        key=(r.get("source_file",""),r.get("source_block_id",""))
        if key not in seen:
            seen.add(key);out.append(r)
    return out

def label(code):
    return "ii"+code.split("/")[1]

def optional_title(text):
    # LaTeX optional arguments terminate at a literal closing square bracket.
    # Replace square-bracket glyphs inside titles by control sequences so
    # mathematical intervals and continued fractions remain safe.
    return str(text).replace("[", r"\lbrack{}").replace("]", r"\rbrack{}")

def render(code,title,data):
    lab=label(code)
    out=[rf"\chapter{{{title}}}",rf"\label{{ch:{lab}}}","",data["intro"],"",
         r"\section*{Learning goals}",
         "The reader should be able to use the central definitions, prove the structural results, diagnose the role of each hypothesis, and solve representative analytic problems.",
         "",r"\section*{Conceptual roadmap}",r"\[",
         r"\boxed{\text{definition}\;\longrightarrow\;\text{estimate}\;\longrightarrow\;\text{theorem}\;\longrightarrow\;\text{application}.}",
         r"\]",""]
    for name,body in data["sections"]:
        out += [rf"\section{{{name}}}",body,""]
    out += [r"\section{Core structural results}",""]
    for i,(name,statement,proof) in enumerate(data["theorems"],1):
        safe_name=optional_title(name)
        out += [rf"\begin{{theorem}}[{safe_name}]\label{{thm:{lab}-{i:02d}}}",statement,
                r"\begin{proof}",proof,r"\end{proof}",r"\end{theorem}",""]
    out += [r"\section{Worked examples}",""]
    for i,(name,problem,solution) in enumerate(data["dossiers"][:4],1):
        safe_name=optional_title(name)
        out += [rf"\begin{{example}}[{safe_name}]\label{{ex:{lab}-worked-{i:02d}}}",
                problem+" "+solution,r"\end{example}",""]
    out += [r"\section{Solved dossiers}",
            "The dossiers are longer solved problems. Legacy mappings guide topic selection where explicit retained source blocks exist; otherwise fresh canonical problems complete the chapter.",""]
    for i,(name,problem,solution) in enumerate(data["dossiers"],1):
        safe_name=optional_title(name)
        out += [rf"\begin{{problem}}[{safe_name}]\label{{prob:{lab}-dossier-{i:02d}}}",problem,r"\end{problem}",
                r"\begin{solution}",solution,r"\end{solution}",""]
    out += [r"\section{Exercises with complete solutions}",""]
    for i,(problem,hint,solution) in enumerate(data["exercises"],1):
        out += [rf"\begin{{exercise}}\label{{exr:{lab}-{i:02d}}}",problem,r"\end{exercise}",
                r"\begin{hint}",hint,r"\end{hint}",r"\begin{solution}",solution,r"\end{solution}",""]
    out += [r"\section*{Chapter summary}",
            "The chapter's tools now form part of the canonical Volume II analysis toolkit and will be used in later approximation, fixed-point, and convergence arguments.",""]
    return "\n".join(out).rstrip()+"\n"

def update_status(repo,developed_codes,complete=False):
    status=read_tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    src=read_tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    for r in status:
        code=r.get("chapter_code","")
        if code.startswith("II/"):
            r["mapped_rule_count"]=str(sum(1 for s in src if s.get("destination")==code))
            if code in developed_codes:
                r["status"]="FROZEN" if complete else "DRAFTED"
                r["next_action"]="COMPLETE" if complete else "REVIEW_AND_INTEGRATE"
    lines=["\t".join(FIELDS)]
    for r in status:
        lines.append("\t".join(str(r.get(k,"")) for k in FIELDS))
    (repo/"editorial/CHAPTER_STATUS.tsv").write_text("\n".join(lines)+"\n",encoding="utf-8")

def provenance_rows(repo,source_rows,data):
    rows=[]
    for code,content in data.items():
        gs=explicit_guides(repo,source_rows,code)
        for i,(title,_,_) in enumerate(content["dossiers"],1):
            r=gs[i-1] if i<=len(gs) else None
            rows.append({
                "chapter_code":code,"dossier_index":i,
                "dossier_label":f"prob:{label(code)}-dossier-{i:02d}",
                "dossier_title":title,
                "origin":"CORPUS_GUIDED" if r else "FRESH_CANONICAL",
                "source_file":r.get("source_file","-") if r else "-",
                "source_block_id":r.get("source_block_id","-") if r else "-",
                "source_selector":r.get("source_selector","-") if r else "-",
                "source_topic":r.get("source_title_or_pattern","-") if r else "-",
                "note":"Mapped source used for topic guidance; canonical problem and solution newly written." if r else "Fresh canonical problem."
            })
    return rows

PROV_FIELDS=["chapter_code","dossier_index","dossier_label","dossier_title","origin","source_file","source_block_id","source_selector","source_topic","note"]
