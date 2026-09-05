from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
from collections import Counter
VOL=Path("books/vol03_fourier_distributions_pde/chapters"); REPORT=Path("reports/series")
BLOCK=re.compile(r"\n?% BEGIN VOL03-EXPANSION ([^\n]+)\n.*?% END VOL03-EXPANSION \1\n?",re.S)
LABEL=re.compile(r"\\label\{([^}]+)\}")
def strip(t): return BLOCK.sub("",t)
def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()
def cnt(t,e): return len(re.findall(rf"\\begin\{{{e}\}}",t))
def files(repo): return sorted((repo/VOL).glob("ch*/chapter.tex"))
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True)
    ap.add_argument("--snapshot",action="store_true"); ap.add_argument("--check-only",action="store_true")
    ap.add_argument("--stage",type=int,default=1)
    a=ap.parse_args(); repo=Path(a.repo).resolve(); out=repo/REPORT
    if not a.check_only: out.mkdir(parents=True,exist_ok=True)
    baseline=out/"VOLUME03_EXAMPLE_EXERCISE_BASELINE.json"
    base=json.loads(baseline.read_text(encoding="utf-8")) if baseline.exists() else {}
    fs=files(repo); blockers=[]; rows=[]; labels=[]
    if len(fs)!=28: blockers.append(f"CHAPTER_COUNT:{len(fs)}!=28")
    for i,p in enumerate(fs,1):
        code=f"III/{i:02d}"; t=p.read_text(encoding="utf-8-sig")
        row={"chapter":code,"path":str(p.relative_to(repo)).replace("\\","/"),
             "examples":cnt(t,"example"),"exercises":cnt(t,"exercise"),"hints":cnt(t,"hint"),
             "problems":cnt(t,"problem"),"solutions":cnt(t,"solution"),"labels":len(LABEL.findall(t)),
             "protected_sha256":sha(strip(t)),
             "expansion_examples":len(re.findall(r"% BEGIN VOL03-EXPANSION III\d\d-example-",t))}
        rows.append(row); labels+=LABEL.findall(t)
        if row["exercises"]!=row["hints"]: blockers.append(f"{code}:EXERCISE_HINT_MISMATCH")
        if row["solutions"]<row["exercises"]+row["problems"]: blockers.append(f"{code}:SOLUTION_COVERAGE")
        if not a.snapshot and base:
            old=next((x for x in base.get("chapters",[]) if x["chapter"]==code),None)
            if old and old["protected_sha256"]!=row["protected_sha256"]: blockers.append(f"{code}:PROTECTED_TEXT_CHANGED")
            if old and row["examples"]<old["examples"]: blockers.append(f"{code}:EXAMPLE_COUNT_DECREASE")
            if old and row["exercises"]<old["exercises"]: blockers.append(f"{code}:EXERCISE_COUNT_DECREASE")
    if a.stage>=2:
        for r in rows[:8]:
            if r["examples"]<7: blockers.append(f"{r['chapter']}:EXAMPLES:{r['examples']}<7")
            if r["exercises"]<24: blockers.append(f"{r['chapter']}:EXERCISES:{r['exercises']}<24")
            if r["expansion_examples"]!=3: blockers.append(f"{r['chapter']}:EXPANSION_EXAMPLES:{r['expansion_examples']}!=3")
    if a.stage>=3:
        for r in rows[8:14]:
            if r["examples"]<7: blockers.append(f"{r['chapter']}:EXAMPLES:{r['examples']}<7")
            if r["exercises"]<24: blockers.append(f"{r['chapter']}:EXERCISES:{r['exercises']}<24")
            if r["expansion_examples"]!=3: blockers.append(f"{r['chapter']}:EXPANSION_EXAMPLES:{r['expansion_examples']}!=3")
    for lab,n in Counter(labels).items():
        if n>1: blockers.append(f"DUPLICATE_LABEL:{lab}")
    status="PASS" if not blockers else "FAIL"; result={"status":status,"stage":a.stage,"chapters":rows,"blocking":blockers}
    if a.snapshot and not a.check_only:
        baseline.write_text(json.dumps({"schema":1,"chapters":rows},indent=2)+"\n",encoding="utf-8")
    if not a.check_only:
        (out/"VOLUME03_EXAMPLE_EXERCISE_AUDIT.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
        md=["# Volume III worked-example and graded-exercise audit","",f"**Result:** {status}","",
            "| Chapter | Examples | Exercises | Hints | Problems | Solutions | New examples |",
            "|---|---:|---:|---:|---:|---:|---:|"]
        for r in rows: md.append(f"| {r['chapter']} | {r['examples']} | {r['exercises']} | {r['hints']} | {r['problems']} | {r['solutions']} | {r['expansion_examples']} |")
        md+=["","## Blocking findings",""]+([f"- {b}" for b in blockers] if blockers else ["None."])
        (out/"VOLUME03_EXAMPLE_EXERCISE_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps({"status":status,"stage":a.stage,"blocking":blockers},indent=2))
    raise SystemExit(0 if status=="PASS" else 9)
if __name__=="__main__": main()
