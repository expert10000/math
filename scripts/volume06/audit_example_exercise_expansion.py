#!/usr/bin/env python3
import argparse,hashlib,json,re
from collections import Counter
from pathlib import Path

VOL=Path("books/vol06_algebraic_geometry/chapters"); REPORT=Path("reports/series")
BLOCK=re.compile(r"% BEGIN VOL06-EXPANSION ([^\n]+)\n.*?% END VOL06-EXPANSION \1\n?",re.S)
LAB=re.compile(r"\\label\{([^}]+)\}")
EB=re.compile(r"% BEGIN VOL06-EXPANSION (VI\d\d-example-\d\d)\n(.*?)% END VOL06-EXPANSION \1",re.S)
XB=re.compile(r"% BEGIN VOL06-EXPANSION (VI\d\d-exercises-01)\n(.*?)% END VOL06-EXPANSION \1",re.S)

def strip(t): return BLOCK.sub("",t)
def sha(t): return hashlib.sha256(t.encode()).hexdigest()
def cnt(t,e): return len(re.findall(rf"\\begin\{{{e}\}}",t))
def row0(base,code): return next((x for x in base.get("chapters",[]) if x["chapter"]==code),None)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--stage",type=int,choices=[1,2,3,4],default=4)
    ap.add_argument("--check-only",action="store_true")
    a=ap.parse_args()
    repo=Path(a.repo).resolve(); out=repo/REPORT
    bp=out/"VOLUME06_EXAMPLE_EXERCISE_BASELINE.json"
    base=json.loads(bp.read_text(encoding="utf-8")) if bp.exists() else {}
    blockers=[]; observations=[]; rows=[]; labels=[]
    fs=sorted((repo/VOL).glob("ch*/chapter.tex"))
    if len(fs)!=49: blockers.append(f"CHAPTER_COUNT:{len(fs)}!=49")
    if a.stage>1 and not base: blockers.append("MISSING_COMMIT1_BASELINE")

    for i,p in enumerate(fs,1):
        code=f"VI/{i:02d}"; t=p.read_text(encoding="utf-8-sig")
        labs=LAB.findall(t); labels+=labs
        ebs=list(EB.finditer(t)); xbs=list(XB.finditer(t))
        r={"chapter":code,"path":p.relative_to(repo).as_posix(),
           "examples":cnt(t,"example"),"exercises":cnt(t,"exercise"),"hints":cnt(t,"hint"),
           "problems":cnt(t,"problem"),"solutions":cnt(t,"solution"),"labels":len(labs),
           "protected_sha256":sha(strip(t)),"expansion_examples":len(ebs),
           "expansion_exercise_blocks":len(xbs),
           "expansion_exercises":sum(cnt(x.group(2),"exercise") for x in xbs),
           "expansion_hints":sum(cnt(x.group(2),"hint") for x in xbs),
           "expansion_solutions":sum(cnt(x.group(2),"solution") for x in xbs)}
        rows.append(r)
        if r["exercises"]!=r["hints"]:
            observations.append(f"{code}:LEGACY_EXERCISE_HINT_IMBALANCE:{r['exercises']}!={r['hints']}")
        if r["solutions"]<r["exercises"]+r["problems"]:
            observations.append(f"{code}:LEGACY_SOLUTION_COVERAGE:{r['solutions']}<{r['exercises']+r['problems']}")

        old=row0(base,code)
        if old and old["protected_sha256"]!=r["protected_sha256"]:
            blockers.append(f"{code}:PROTECTED_TEXT_CHANGED")

        enriched=(a.stage>=2 and i<=17) or (a.stage>=3 and 18<=i<=32) or (a.stage>=4 and 33<=i<=49)
        if enriched:
            if not old:
                blockers.append(f"{code}:MISSING_BASELINE")
            else:
                for key,delta in [("examples",3),("exercises",16),("hints",16),("solutions",16)]:
                    expected=old[key]+delta
                    if r[key]!=expected:
                        blockers.append(f"{code}:{key.upper()}:{r[key]}!={expected}")
            if r["expansion_examples"]!=3: blockers.append(f"{code}:EXPANSION_EXAMPLES:{r['expansion_examples']}!=3")
            if r["expansion_exercise_blocks"]!=1: blockers.append(f"{code}:EXPANSION_EXERCISE_BLOCKS:{r['expansion_exercise_blocks']}!=1")
            if r["expansion_exercises"]!=16: blockers.append(f"{code}:EXPANSION_EXERCISES:{r['expansion_exercises']}!=16")
            if r["expansion_hints"]!=16: blockers.append(f"{code}:EXPANSION_HINTS:{r['expansion_hints']}!=16")
            if r["expansion_solutions"]!=16: blockers.append(f"{code}:EXPANSION_SOLUTIONS:{r['expansion_solutions']}!=16")
        elif a.stage>=2 and (r["expansion_examples"] or r["expansion_exercise_blocks"]):
            blockers.append(f"{code}:UNEXPECTED_EARLY_EXPANSION")

    for lab,n in Counter(labels).items():
        if n>1: blockers.append(f"DUPLICATE_LABEL:{lab}")

    status="PASS" if not blockers else "FAIL"
    result={"status":status,"stage":a.stage,"chapters":rows,"blocking":blockers,"baseline_observations":observations}
    if not a.check_only:
        out.mkdir(parents=True,exist_ok=True)
        (out/"VOLUME06_EXAMPLE_EXERCISE_AUDIT.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
        md=["# Volume VI worked-example and graded-exercise audit","",f"**Result:** {status}","",f"**Stage:** {a.stage}","",
            "| Chapter | Examples | Exercises | Hints | Problems | Solutions | New examples | New exercises |",
            "|---|---:|---:|---:|---:|---:|---:|---:|"]
        for r in rows:
            md.append(f"| {r['chapter']} | {r['examples']} | {r['exercises']} | {r['hints']} | {r['problems']} | {r['solutions']} | {r['expansion_examples']} | {r['expansion_exercises']} |")
        md += ["","## Blocking findings",""]+([f"- {b}" for b in blockers] if blockers else ["None."])
        md += ["","## Legacy baseline observations (non-blocking)",""]+([f"- {b}" for b in observations] if observations else ["None."])
        (out/"VOLUME06_EXAMPLE_EXERCISE_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps({"status":status,"stage":a.stage,"blocking":blockers,"baseline_observations":observations},indent=2))
    return 0 if status=="PASS" else 9
if __name__=="__main__":
    raise SystemExit(main())
