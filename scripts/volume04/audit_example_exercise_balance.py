#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter
from pathlib import Path

VOL=Path("books/vol04_complex_analysis/chapters")
REPORT=Path("reports/series")
BLOCK=re.compile(r"% BEGIN VOL04-EXPANSION ([^\n]+)\n.*?% END VOL04-EXPANSION \1\n?",re.S)
LABEL=re.compile(r"\\label\{([^}]+)\}")
EXAMPLE_BLOCK=re.compile(r"% BEGIN VOL04-EXPANSION (IV\d\d-example-\d\d)\n(.*?)% END VOL04-EXPANSION \1",re.S)
EXERCISE_BLOCK=re.compile(r"% BEGIN VOL04-EXPANSION (IV\d\d-exercises-01)\n(.*?)% END VOL04-EXPANSION \1",re.S)
SECTION=re.compile(r"\\section\{([^}]+)\}")
CATS=[
    ("Standard computations",5),
    ("Proofs",4),
    ("Counterexamples and hypothesis tests",3),
    ("Applications and investigations",2),
    ("Challenge problems",2),
]

def sha(t:str)->str: return hashlib.sha256(t.encode("utf-8")).hexdigest()
def strip(t:str)->str: return BLOCK.sub("",t)
def cnt(t:str,e:str)->int: return len(re.findall(rf"\\begin\{{{e}\}}",t))
def preceding_section(text:str,pos:int)->str:
    ms=list(SECTION.finditer(text[:pos])); return ms[-1].group(1) if ms else ""
def cat_counts(block:str)->dict[str,int]:
    out={}; marks=[]
    for name,_ in CATS:
        m=re.search(rf"\\subsection\*\{{{re.escape(name)}\}}",block)
        if m: marks.append((m.start(),name,m.end()))
    marks.sort()
    for j,(start,name,end) in enumerate(marks):
        stop=marks[j+1][0] if j+1<len(marks) else len(block)
        out[name]=cnt(block[end:stop],"exercise")
    return out

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); ap.add_argument("--write",action="store_true")
    a=ap.parse_args(); repo=Path(a.repo).resolve(); out=repo/REPORT
    base_path=out/"VOLUME04_EXAMPLE_EXERCISE_BASELINE.json"
    base=json.loads(base_path.read_text(encoding="utf-8")) if base_path.exists() else {}
    blockers=[]; rows=[]; all_labels=[]
    if not base: blockers.append("MISSING_COMMIT1_BASELINE")
    files=sorted((repo/VOL).glob("ch*/chapter.tex"))
    if len(files)!=31: blockers.append(f"CHAPTER_COUNT:{len(files)}!=31")
    for i,p in enumerate(files,1):
        code=f"IV/{i:02d}"; t=p.read_text(encoding="utf-8-sig")
        labels=LABEL.findall(t); all_labels+=labels
        exblocks=list(EXAMPLE_BLOCK.finditer(t)); eb=list(EXERCISE_BLOCK.finditer(t))
        placements=[preceding_section(t,m.start()) for m in exblocks]
        if len(exblocks)!=3: blockers.append(f"{code}:EXPANSION_EXAMPLES:{len(exblocks)}!=3")
        for tag,sec in zip([m.group(1) for m in exblocks],placements):
            if not sec or sec in {"Worked examples","Solved dossiers","Exercises with complete solutions","Graded supplementary exercises","Core structural results"}:
                blockers.append(f"{code}:BAD_EXAMPLE_PLACEMENT:{tag}:{sec or 'NONE'}")
        if len(eb)!=1: blockers.append(f"{code}:EXPANSION_EXERCISE_BLOCKS:{len(eb)}!=1")
        cats=cat_counts(eb[0].group(2)) if len(eb)==1 else {}
        for name,n in CATS:
            if cats.get(name)!=n: blockers.append(f"{code}:CATEGORY:{name}:{cats.get(name)}!={n}")
        counts={e:cnt(t,e) for e in ["example","exercise","hint","problem","solution"]}
        if counts["exercise"]!=counts["hint"]: blockers.append(f"{code}:EXERCISE_HINT_MISMATCH")
        if counts["solution"]<counts["exercise"]+counts["problem"]: blockers.append(f"{code}:SOLUTION_COVERAGE")
        old=next((x for x in base.get("chapters",[]) if x.get("chapter")==code),None)
        protected=sha(strip(t))
        if not old: blockers.append(f"{code}:MISSING_BASELINE_ROW")
        else:
            if old.get("protected_sha256")!=protected: blockers.append(f"{code}:PROTECTED_TEXT_CHANGED")
            expected={"example":old["examples"]+3,"exercise":old["exercises"]+16,"hint":old["hints"]+16,"solution":old["solutions"]+16}
            for k,v in expected.items():
                if counts[k]!=v: blockers.append(f"{code}:{k.upper()}:{counts[k]}!={v}")
        rows.append({"chapter":code,**counts,"placements":placements,"categories":cats,"protected_sha256":protected})
    for lab,n in Counter(all_labels).items():
        if n>1: blockers.append(f"DUPLICATE_LABEL:{lab}")
    status="PASS" if not blockers else "FAIL"; result={"status":status,"chapters":rows,"blocking":blockers}
    print(json.dumps({"status":status,"blocking":blockers},indent=2))
    if a.write:
        out.mkdir(parents=True,exist_ok=True)
        (out/"VOLUME04_EXAMPLE_EXERCISE_BALANCE_AUDIT.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
        md=["# Volume IV worked-example placement and graded-exercise balance","",f"**Result:** {status}","",
            "| Chapter | Examples | Exercises | Hints | Problems | Solutions | Placement sections |",
            "|---|---:|---:|---:|---:|---:|---|"]
        for r in rows:
            md.append(f"| {r['chapter']} | {r['example']} | {r['exercise']} | {r['hint']} | {r['problem']} | {r['solution']} | {'; '.join(r['placements'])} |")
        md += ["","## Required graded balance","","Every chapter: 5 standard computations, 4 proofs, 3 counterexamples or hypothesis tests, 2 applications or investigations, 2 challenges.","","## Blocking findings",""]
        md += [f"- {b}" for b in blockers] if blockers else ["None."]
        (out/"VOLUME04_EXAMPLE_EXERCISE_BALANCE_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    return 0 if status=="PASS" else 12
if __name__=="__main__": raise SystemExit(main())
