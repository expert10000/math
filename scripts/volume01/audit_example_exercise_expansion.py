#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

BASE="75876454d6a79790125df79dc88a5a2875bf5a94"
VOL=Path("books/vol01_linear_algebra/chapters")
REPORT=Path("reports/series")
BLOCK=re.compile(r"\n?% BEGIN VOL01-EXPANSION ([^\n]+)\n.*?% END VOL01-EXPANSION \1\n?",re.S)

def strip_blocks(t): return BLOCK.sub("",t)
def counts(t):
    return {
      "examples":len(re.findall(r"\\begin\{example\}",t)),
      "exercises":len(re.findall(r"\\begin\{exercise\}",t)),
      "hints":len(re.findall(r"\\begin\{hint\}",t)),
      "solutions":len(re.findall(r"\\begin\{solution\}",t)),
      "problems":len(re.findall(r"\\begin\{problem\}",t)),
    }
def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()
def chapter_files(repo): return sorted((repo/VOL).glob("ch*/chapter.tex"))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--snapshot",action="store_true")
    ap.add_argument("--check-only",action="store_true")
    ap.add_argument("--stage",type=int,default=1)
    a=ap.parse_args(); repo=Path(a.repo).resolve()
    report_dir=repo/REPORT
    if not a.check_only:
        report_dir.mkdir(parents=True,exist_ok=True)
    baseline=report_dir/"VOLUME01_EXAMPLE_EXERCISE_BASELINE.json"

    rows=[]; blockers=[]
    files=chapter_files(repo)
    if len(files)!=18: blockers.append(f"CHAPTER_FILES:{len(files)}!=18")
    base_data=json.loads(baseline.read_text(encoding="utf-8")) if baseline.exists() else {}

    for i,p in enumerate(files,1):
        t=p.read_text(encoding="utf-8-sig")
        protected=strip_blocks(t); c=counts(t)
        code=f"I/{i:02d}"
        row={"chapter":code,"path":str(p.relative_to(repo)).replace("\\","/"),
             **c,"protected_sha256":sha(protected),
             "expansion_blocks":len(re.findall(r"% BEGIN VOL01-EXPANSION ",t))}
        rows.append(row)
        if c["exercises"]!=c["hints"]:
            blockers.append(f"{code}:EXERCISE_HINT_MISMATCH:{c['exercises']}!={c['hints']}")
        if c["solutions"] < c["exercises"]+c["problems"]:
            blockers.append(f"{code}:TOO_FEW_SOLUTIONS")
        if not a.snapshot and base_data:
            old=next((x for x in base_data["chapters"] if x["chapter"]==code),None)
            if old and old["protected_sha256"]!=row["protected_sha256"]:
                blockers.append(f"{code}:PROTECTED_TEXT_CHANGED")
            if old and c["examples"]<old["examples"]:
                blockers.append(f"{code}:EXAMPLE_COUNT_DECREASED")
            if old and c["exercises"]<old["exercises"]:
                blockers.append(f"{code}:EXERCISE_COUNT_DECREASED")

    if a.stage>=2:
        for r in rows[:6]:
            if r["examples"]<6: blockers.append(f"{r['chapter']}:EXAMPLES:{r['examples']}<6")
            if r["exercises"]<24: blockers.append(f"{r['chapter']}:EXERCISES:{r['exercises']}<24")
    if a.stage>=3:
        for r in rows[6:12]:
            if r["examples"]<6: blockers.append(f"{r['chapter']}:EXAMPLES:{r['examples']}<6")
            if r["exercises"]<24: blockers.append(f"{r['chapter']}:EXERCISES:{r['exercises']}<24")

    status="PASS" if not blockers else "FAIL"
    out={"status":status,"stage":a.stage,"chapters":rows,"blocking":blockers}

    if a.snapshot and not a.check_only:
        baseline.write_text(json.dumps({"schema":1,"base_commit":BASE,"chapters":rows},indent=2)+"\n",encoding="utf-8")
    if not a.check_only:
        (report_dir/"VOLUME01_EXAMPLE_EXERCISE_AUDIT.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
        md=["# Volume I worked-example and graded-exercise audit","",f"**Result:** {status}","",
            "| Chapter | Examples | Exercises | Hints | Expansion blocks |",
            "|---|---:|---:|---:|---:|"]
        for r in rows:
            md.append(f"| {r['chapter']} | {r['examples']} | {r['exercises']} | {r['hints']} | {r['expansion_blocks']} |")
        md += ["","## Blocking findings",""]
        md += [f"- {x}" for x in blockers] if blockers else ["None."]
        (report_dir/"VOLUME01_EXAMPLE_EXERCISE_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")

    print(json.dumps({"status":status,"stage":a.stage,"blocking":blockers},indent=2))
    raise SystemExit(0 if not blockers else 9)
if __name__=="__main__": main()
