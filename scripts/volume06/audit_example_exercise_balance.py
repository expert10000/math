#!/usr/bin/env python3
import argparse,json,re,subprocess
from collections import Counter
from pathlib import Path
from expansion_common import SECTION,TERMINAL_SECTION

VOL=Path("books/vol06_algebraic_geometry/chapters"); REPORT=Path("reports/series")
EX=re.compile(r"% BEGIN VOL06-EXPANSION (VI\d\d-example-\d\d)\n(.*?)% END VOL06-EXPANSION \1",re.S)
XB=re.compile(r"% BEGIN VOL06-EXPANSION (VI\d\d-exercises-01)\n(.*?)% END VOL06-EXPANSION \1",re.S)
LAB=re.compile(r"\\label\{([^}]+)\}")
def cnt(t,e): return len(re.findall(rf"\\begin\{{{e}\}}",t))

def preceding_section(text,pos):
    ms=list(SECTION.finditer(text[:pos]))
    return ms[-1].group(1).strip() if ms else "(chapter introduction)"

def first_terminal(text):
    for m in SECTION.finditer(text):
        if TERMINAL_SECTION.match(m.group(1).strip()): return m.start()
    return len(text)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
    repo=Path(a.repo).resolve(); blockers=[]; rows=[]; labels=[]
    cats=[("standard","Standard computations",5),("proof","Proofs",4),("test","Counterexamples and hypothesis tests",3),("application","Applications and investigations",2),("challenge","Challenge problems",2)]
    fs=sorted((repo/VOL).glob("ch*/chapter.tex"))
    if len(fs)!=49: blockers.append(f"CHAPTER_COUNT:{len(fs)}!=49")
    for i,p in enumerate(fs,1):
        code=f"VI/{i:02d}"; t=p.read_text(encoding="utf-8-sig"); labels+=LAB.findall(t)
        ebs=list(EX.finditer(t)); xbs=list(XB.finditer(t)); term=first_terminal(t)
        placed=[preceding_section(t,b.start()) for b in ebs]
        if len(ebs)!=3: blockers.append(f"{code}:EXPANSION_EXAMPLES:{len(ebs)}!=3")
        if any(b.start()>=term for b in ebs): blockers.append(f"{code}:EXAMPLE_AFTER_TERMINAL_SECTION")
        if len(xbs)!=1: blockers.append(f"{code}:EXERCISE_BLOCKS:{len(xbs)}!=1")
        body=xbs[0].group(2) if xbs else ""
        total=cnt(body,"exercise")
        if total!=16 or cnt(body,"hint")!=16 or cnt(body,"solution")!=16: blockers.append(f"{code}:TRIAD_COUNTS")
        catcounts={}
        for key,heading,expected in cats:
            m=re.search(rf"\\subsection\*\{{{re.escape(heading)}\}}(.*?)(?=\\subsection\*\{{|$)",body,re.S)
            c=cnt(m.group(1),"exercise") if m else 0; catcounts[key]=c
            if c!=expected: blockers.append(f"{code}:{key.upper()}:{c}!={expected}")
        rows.append({"chapter":code,"placed_after":placed,"categories":catcounts,"new_examples":len(ebs),"new_exercises":total})

    for lab,n in Counter(labels).items():
        if n>1: blockers.append(f"DUPLICATE_LABEL:{lab}")

    tracked=subprocess.run(["git","-C",str(repo),"ls-files","scripts/volume06"],stdout=subprocess.PIPE,text=True,encoding="utf-8",errors="replace").stdout.splitlines()
    tracked_cache=[x for x in tracked if "/__pycache__/" in x or x.endswith(".pyc")]
    if tracked_cache: blockers += [f"TRACKED_PYTHON_CACHE:{x}" for x in tracked_cache]
    gi=repo/"scripts"/"volume06"/".gitignore"
    if not gi.exists(): blockers.append("MISSING_VOLUME06_GITIGNORE")
    else:
        g=gi.read_text(encoding="utf-8")
        if "__pycache__/" not in g or "*.pyc" not in g: blockers.append("INCOMPLETE_VOLUME06_GITIGNORE")

    status="PASS" if not blockers else "FAIL"
    result={"status":status,"chapters":rows,"tracked_python_cache":tracked_cache,"blocking":blockers}
    print(json.dumps({"status":status,"tracked_python_cache":tracked_cache,"blocking":blockers},indent=2))
    if a.write:
        out=repo/REPORT; out.mkdir(parents=True,exist_ok=True)
        (out/"VOLUME06_EXAMPLE_EXERCISE_BALANCE_AUDIT.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
        md=["# Volume VI worked-example placement and graded-exercise balance","",f"**Result:** {status}","",
            "| Chapter | New examples | New exercises | 5/4/3/2/2 |","|---|---:|---:|---|"]
        for r in rows:
            c=r["categories"]; md.append(f"| {r['chapter']} | {r['new_examples']} | {r['new_exercises']} | {c['standard']}/{c['proof']}/{c['test']}/{c['application']}/{c['challenge']} |")
        md += ["","## Placement evidence",""]
        for r in rows: md.append(f"- **{r['chapter']}**: {' | '.join(r['placed_after'])}")
        md += ["","## Python-cache hygiene","",f"- tracked cache files: **{len(tracked_cache)}**","","## Blocking findings",""]
        md += [f"- {b}" for b in blockers] if blockers else ["None."]
        (out/"VOLUME06_EXAMPLE_EXERCISE_BALANCE_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    return 0 if status=="PASS" else 12
if __name__=="__main__":
    raise SystemExit(main())
