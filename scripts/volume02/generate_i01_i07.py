#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,re,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from vol02_i01_i07_data import CHAPTERS, DATA

PARTS=[
("Metric Foundations",1,7),
("Calculus",8,10),
("Sequences of Functions",11,15),
("Fixed Points and Differential Equations",16,19),
("Approximation",20,25),
]
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
            value=r.get(k,"-")
            vals.append("-" if value is None or value=="" else str(value))
        lines.append("\t".join(vals))
    p.write_text("\n".join(lines)+"\n",encoding="utf-8")

def source_path(repo,name):
    if not name:return None
    for p in (repo/name,repo/"chapters/tex"/name):
        if p.exists():return p
    return None

def guides(repo,source_rows,code):
    out=[]
    for r in source_rows:
        if r.get("destination")!=code:continue
        try:prec=int(r.get("precedence") or "0")
        except:prec=0
        if prec<90:continue
        if r.get("source_selector","").strip()=="*":continue
        if r.get("block_kind") in ("ANY_UNMATCHED_BLOCK","ENTIRE_FILE"):continue
        if not source_path(repo,r.get("source_file","")):continue
        out.append((prec,r))
    out.sort(key=lambda z:(-z[0],z[1].get("source_file",""),z[1].get("source_block_id","")))
    result=[];seen=set()
    for _,r in out:
        key=(r.get("source_file",""),r.get("source_block_id",""))
        if key not in seen:
            seen.add(key);result.append(r)
    return result

def label(code):
    return "ii"+code.split("/")[1]

def render(code,title,data):
    lab=label(code)
    out=[rf"\chapter{{{title}}}",rf"\label{{ch:{lab}}}","",data["intro"],"",
         r"\section*{Learning goals}",
         "The reader should be able to use the chapter's definitions in proofs, recognize the decisive hypotheses, and move between concrete metric examples and invariant topological statements.",
         "",r"\section*{Conceptual roadmap}",r"\[",
         r"\boxed{\text{definition}\;\longrightarrow\;\text{estimate}\;\longrightarrow\;\text{structural theorem}\;\longrightarrow\;\text{application}.}",
         r"\]",""]
    for name,body in data["sections"]:
        out += [rf"\section{{{name}}}",body,""]
    out += [r"\section{Core structural results}",""]
    for i,(name,statement,proof) in enumerate(data["theorems"],1):
        out += [rf"\begin{{theorem}}[{name}]\label{{thm:{lab}-{i:02d}}}",statement,
                r"\begin{proof}",proof,r"\end{proof}",r"\end{theorem}",""]
    out += [r"\section{Worked examples}",""]
    for i,(name,problem,solution) in enumerate(data["dossiers"][:4],1):
        out += [rf"\begin{{example}}[{name}]\label{{ex:{lab}-worked-{i:02d}}}",
                problem+" "+solution,r"\end{example}",""]
    out += [r"\section{Solved dossiers}",
            "Each dossier is a substantial solved problem. Corpus mappings guide topic choice where explicit retained source blocks exist; otherwise the dossier is a fresh canonical completion.",""]
    for i,(name,problem,solution) in enumerate(data["dossiers"],1):
        out += [rf"\begin{{problem}}[{name}]\label{{prob:{lab}-dossier-{i:02d}}}",problem,r"\end{problem}",
                r"\begin{solution}",solution,r"\end{solution}",""]
    out += [r"\section{Exercises with complete solutions}",
            "The shorter exercise layer is kept separate from the dossiers.",""]
    for i,(problem,hint,solution) in enumerate(data["exercises"],1):
        out += [rf"\begin{{exercise}}\label{{exr:{lab}-{i:02d}}}",problem,r"\end{exercise}",
                r"\begin{hint}",hint,r"\end{hint}",
                r"\begin{solution}",solution,r"\end{solution}",""]
    out += [r"\section*{Chapter summary}",
            "The central definitions, estimates, and structural theorems of this chapter will be used repeatedly in the remaining analysis volume.",""]
    return "\n".join(out)

def stub(code,title):
    return "\n".join([rf"\chapter{{{title}}}",rf"\label{{ch:{label(code)}}}","",
        r"\section*{Reconstruction scaffold}",
        "This canonical chapter path is active and buildable. Full reconstruction is reserved for a later Volume II commit.",""])

def book():
    slug={c:s for c,t,s in CHAPTERS}
    out=[r"\documentclass[11pt,a4paper,oneside,openany]{book}",
         r"\input{../../shared/preamble.tex}",r"\input{../../shared/macros.tex}",
         r"\input{../../shared/theorem_styles.tex}",r"\input{../../shared/notation.tex}","",
         r"\title{Theory of Mathematics\\[0.5em]\Large Volume II: Real Analysis and Topological Foundations}",
         r"\author{}",r"\date{}",
         r"\hypersetup{pdftitle={Theory of Mathematics — Volume II: Real Analysis and Topological Foundations},pdfsubject={Canonical reconstructed mathematics series}}",
         r"\begin{document}",r"\pagenumbering{gobble}",r"\maketitle",r"\clearpage",
         r"\frontmatter",r"\tableofcontents",r"\mainmatter",""]
    for part,a,b in PARTS:
        out.append(rf"\part{{{part}}}")
        for n in range(a,b+1):
            code=f"II/{n:02d}"
            out.append(rf"\include{{chapters/{slug[code]}/chapter}}")
        out.append("")
    out += [r"\backmatter",r"\end{document}",""]
    return "\n".join(out)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol02_real_analysis"
    status=read_tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    src=read_tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    (vol/"book.tex").write_text(book(),encoding="utf-8")
    inventory=[];provenance=[]
    for code,title,slug in CHAPTERS:
        p=vol/"chapters"/slug/"chapter.tex";p.parent.mkdir(parents=True,exist_ok=True)
        if code in DATA:
            p.write_text(render(code,title,DATA[code]).rstrip()+"\n",encoding="utf-8")
        elif not p.exists():
            p.write_text(stub(code,title).rstrip()+"\n",encoding="utf-8")
        # Canonical text files end with exactly one newline and no blank EOF line.
        current=p.read_text(encoding="utf-8-sig")
        p.write_text(current.rstrip()+"\n",encoding="utf-8")
        rules=[r for r in src if r.get("destination")==code]
        missing=sum(1 for r in rules if r.get("source_file") and not source_path(repo,r.get("source_file","")))
        inventory.append({"chapter_code":code,"chapter_title":title,"mapped_rules":len(rules),
            "missing_sources":missing,"canonical_path":p.relative_to(repo).as_posix(),
            "state":"DEVELOPED" if code in DATA else "SCAFFOLD"})
        if code in DATA:
            gs=guides(repo,src,code)
            for i,(dtitle,_,_) in enumerate(DATA[code]["dossiers"],1):
                r=gs[i-1] if i<=len(gs) else None
                provenance.append({
                    "chapter_code":code,"dossier_index":i,"dossier_label":f"prob:{label(code)}-dossier-{i:02d}",
                    "dossier_title":dtitle,"origin":"CORPUS_GUIDED" if r else "DEVISED_TO_COMPLETE_COVERAGE",
                    "source_file":r.get("source_file","-") if r else "-",
                    "source_block_id":r.get("source_block_id","-") if r else "-",
                    "source_selector":r.get("source_selector","-") if r else "-",
                    "source_topic":r.get("source_title_or_pattern","-") if r else "-",
                    "note":"Mapped source used for topic guidance; canonical problem and solution newly written." if r else "Fresh canonical problem added to complete coverage."
                })
    write_tsv(vol/"reconstruction/VOLUME02_SOURCE_INVENTORY.tsv",inventory,
        ["chapter_code","chapter_title","mapped_rules","missing_sources","canonical_path","state"])
    write_tsv(vol/"reconstruction/VOLUME02_I01_I07_DOSSIER_PROVENANCE.tsv",provenance,
        ["chapter_code","dossier_index","dossier_label","dossier_title","origin","source_file","source_block_id","source_selector","source_topic","note"])
    for r in status:
        code=r.get("chapter_code","")
        if code.startswith("II/"):
            rules=[x for x in src if x.get("destination")==code]
            r["mapped_rule_count"]=str(len(rules))
            if code in DATA:
                r["status"]="DRAFTED";r["next_action"]="REVIEW_AND_INTEGRATE"
    lines=["\t".join(FIELDS)]
    for r in status:lines.append("\t".join(str(r.get(k,"")) for k in FIELDS))
    (repo/"editorial/CHAPTER_STATUS.tsv").write_text("\n".join(lines)+"\n",encoding="utf-8")
    readme=vol/"README.md";txt=readme.read_text(encoding="utf-8-sig")
    txt=re.sub(r"(?m)^\*\*Status:\*\*.*$","**Status:** Canonical reconstruction underway; II/01–II/07 developed with solved dossiers.",txt,count=1)
    readme.write_text(txt.rstrip()+"\n",encoding="utf-8")
    print("Generated canonical Volume II wrapper and II/01-II/07.")
    print("Solved dossiers: 84; short exercises: 56.")
    return 0
if __name__=="__main__":raise SystemExit(main())
