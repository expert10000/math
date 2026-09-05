#!/usr/bin/env python3
import argparse,hashlib,json,re
from collections import Counter
from pathlib import Path
VOL=Path("books/vol05_commutative_algebra/chapters"); REPORT=Path("reports/series")
BLOCK=re.compile(r"% BEGIN VOL05-EXPANSION ([^\n]+)\n.*?% END VOL05-EXPANSION \1\n?",re.S)
LAB=re.compile(r"\\label\{([^}]+)\}"); EB=re.compile(r"% BEGIN VOL05-EXPANSION (V\d\d-example-\d\d)\n(.*?)% END VOL05-EXPANSION \1",re.S); XB=re.compile(r"% BEGIN VOL05-EXPANSION (V\d\d-exercises-01)\n(.*?)% END VOL05-EXPANSION \1",re.S)
def strip(t): return BLOCK.sub("",t)
def sha(t): return hashlib.sha256(t.encode()).hexdigest()
def cnt(t,e): return len(re.findall(rf"\\begin\{{{e}\}}",t))
def row0(base,code): return next((x for x in base.get("chapters",[]) if x["chapter"]==code),None)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); ap.add_argument("--snapshot",action="store_true"); ap.add_argument("--stage",type=int,choices=[1,2,3],default=1); ap.add_argument("--check-only",action="store_true"); a=ap.parse_args()
    repo=Path(a.repo).resolve(); out=repo/REPORT; bp=out/"VOLUME05_EXAMPLE_EXERCISE_BASELINE.json"; base=json.loads(bp.read_text()) if bp.exists() else {}; blockers=[]; rows=[]; labels=[]
    fs=sorted((repo/VOL).glob("ch*/chapter.tex"))
    if len(fs)!=28: blockers.append(f"CHAPTER_COUNT:{len(fs)}!=28")
    if a.stage>1 and not base: blockers.append("MISSING_COMMIT1_BASELINE")
    for i,p in enumerate(fs,1):
        code=f"V/{i:02d}"; t=p.read_text(encoding="utf-8-sig"); labs=LAB.findall(t); labels+=labs; ebs=list(EB.finditer(t)); xbs=list(XB.finditer(t))
        r={"chapter":code,"path":p.relative_to(repo).as_posix(),"examples":cnt(t,"example"),"exercises":cnt(t,"exercise"),"hints":cnt(t,"hint"),"problems":cnt(t,"problem"),"solutions":cnt(t,"solution"),"labels":len(labs),"protected_sha256":sha(strip(t)),"expansion_examples":len(ebs),"expansion_exercise_blocks":len(xbs),"expansion_exercises":sum(cnt(x.group(2),"exercise") for x in xbs),"expansion_hints":sum(cnt(x.group(2),"hint") for x in xbs),"expansion_solutions":sum(cnt(x.group(2),"solution") for x in xbs)}
        rows.append(r)
        if r["exercises"]!=r["hints"]: blockers.append(f"{code}:EXERCISE_HINT_MISMATCH")
        if r["solutions"]<r["exercises"]+r["problems"]: blockers.append(f"{code}:SOLUTION_COVERAGE")
        old=row0(base,code)
        if old and old["protected_sha256"]!=r["protected_sha256"]: blockers.append(f"{code}:PROTECTED_TEXT_CHANGED")
        enriched=(a.stage>=2 and i<=8) or (a.stage>=3 and 9<=i<=14)
        if enriched:
            if not old: blockers.append(f"{code}:MISSING_BASELINE")
            else:
                for key,delta in [("examples",3),("exercises",16),("hints",16),("solutions",16)]:
                    if r[key]!=old[key]+delta: blockers.append(f"{code}:{key.upper()}:{r[key]}!={old[key]+delta}")
            if r["expansion_examples"]!=3 or r["expansion_exercise_blocks"]!=1 or r["expansion_exercises"]!=16 or r["expansion_hints"]!=16 or r["expansion_solutions"]!=16: blockers.append(f"{code}:EXPANSION_COUNTS")
        elif a.stage>=2 and (i>14 or (a.stage==2 and i>8)):
            if r["expansion_examples"] or r["expansion_exercise_blocks"]: blockers.append(f"{code}:UNEXPECTED_EARLY_EXPANSION")
    for lab,n in Counter(labels).items():
        if n>1: blockers.append(f"DUPLICATE_LABEL:{lab}")
    status="PASS" if not blockers else "FAIL"; result={"status":status,"stage":a.stage,"chapters":rows,"blocking":blockers}
    if not a.check_only:
        out.mkdir(parents=True,exist_ok=True)
        if a.snapshot:
            if any(r["expansion_examples"] or r["expansion_exercise_blocks"] for r in rows): blockers.append("SNAPSHOT_REFUSED"); status="FAIL"
            else: bp.write_text(json.dumps({"schema":1,"volume":"V","chapters":rows},indent=2)+"\n")
        result["status"]=status; result["blocking"]=blockers
        (out/"VOLUME05_EXAMPLE_EXERCISE_AUDIT.json").write_text(json.dumps(result,indent=2)+"\n")
        md=["# Volume V worked-example and graded-exercise audit","",f"**Result:** {status}","",f"**Stage:** {a.stage}","","| Chapter | Examples | Exercises | Hints | Problems | Solutions | New examples | New exercises |","|---|---:|---:|---:|---:|---:|---:|---:|"]
        for r in rows: md.append(f"| {r['chapter']} | {r['examples']} | {r['exercises']} | {r['hints']} | {r['problems']} | {r['solutions']} | {r['expansion_examples']} | {r['expansion_exercises']} |")
        md += ["","## Blocking findings",""]+([f"- {b}" for b in blockers] if blockers else ["None."])
        (out/"VOLUME05_EXAMPLE_EXERCISE_AUDIT.md").write_text("\n".join(md)+"\n")
    print(json.dumps({"status":status,"stage":a.stage,"blocking":blockers},indent=2)); return 0 if status=="PASS" else 9
if __name__=="__main__": raise SystemExit(main())
