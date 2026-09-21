#!/usr/bin/env python3
import argparse,csv,re
from pathlib import Path
ROMAN={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII"}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",type=Path,required=True); ap.add_argument("--part",type=int,required=True,choices=range(1,9)); a=ap.parse_args()
    repo=a.repo.resolve(); roman=ROMAN[a.part]; nn=f"{a.part:02d}"
    chapter=repo/"books"/"companion_problems_solutions"/"chapters"/f"part{nn}_volume_{roman.lower()}"/"chapter.tex"
    manifest=repo/"books"/"companion_problems_solutions"/"metadata"/f"PART_{roman}_FIGURES.tsv"
    book=repo/"books"/"companion_problems_solutions"/"book.tex"
    text=chapter.read_text(encoding="utf-8")
    labs=re.findall(r"\\label\{(fig:[^}]+)\}",text)
    refs=re.findall(r"\\(?:ref|autoref|cref|Cref)\{(fig:[^}]+)\}",text)
    graphics=re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}",text)
    errors=[]
    dup=sorted({x for x in labs if labs.count(x)>1})
    if dup: errors.append("duplicate labels: "+", ".join(dup))
    miss=sorted(set(refs)-set(labs))
    if miss: errors.append("unresolved refs: "+", ".join(miss))
    for raw in graphics:
        p=repo/"books"/"companion_problems_solutions"/raw
        if not p.exists(): errors.append("missing asset: "+raw)
    rows=[]
    if manifest.exists():
        with manifest.open("r",encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f,delimiter="\t"))
        review=[r for r in rows if (r.get("status") or "").startswith("REVIEW_REQUIRED")]
        if review: errors.append(f"{len(review)} manifest rows require review")
    elif refs or labs: errors.append("missing manifest")
    if book.exists():
        lof=len(re.findall(r"(?m)^[ \t]*\\listoffigures[ \t]*$",book.read_text(encoding="utf-8")))
        if lof!=1: errors.append(f"expected one listoffigures, found {lof}")
    print(f"PART {roman} FIGURES: refs={len(refs)} labels={len(labs)} graphics={len(graphics)} manifest_rows={len(rows)}")
    if errors:
        print("FAILED"); [print(" -",e) for e in errors]; return 1
    print("PASSED"); return 0
if __name__=="__main__": raise SystemExit(main())
