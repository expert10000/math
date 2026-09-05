#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
from collections import Counter

VOL=Path("books/vol02_real_analysis/chapters")
REPORT=Path("reports/series")
BLOCK=re.compile(r"\n?% BEGIN VOL02-EXPANSION ([^\n]+)\n.*?% END VOL02-EXPANSION \1\n?",re.S)
LABEL=re.compile(r"\\label\{([^}]+)\}")
EXAMPLE_BLOCK=re.compile(r"% BEGIN VOL02-EXPANSION (II\d\d-example-\d\d)\n(.*?)% END VOL02-EXPANSION \1",re.S)

def strip(t): return BLOCK.sub("",t)
def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()
def cnt(t,e): return len(re.findall(rf"\\begin\{{{e}\}}",t))
def files(repo): return sorted((repo/VOL).glob("ch*/chapter.tex"))

def preceding_section(text,pos):
    ms=list(re.finditer(r"\\section\{([^}]+)\}",text[:pos]))
    return ms[-1].group(1) if ms else ""

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--write",action="store_true")
    a=ap.parse_args(); repo=Path(a.repo).resolve()

    baseline=repo/REPORT/"VOLUME02_EXAMPLE_EXERCISE_BASELINE.json"
    blockers=[]; rows=[]; all_labels=[]
    if not baseline.exists():
        blockers.append("MISSING_COMMIT1_BASELINE")
        base={}
    else:
        base=json.loads(baseline.read_text(encoding="utf-8"))

    fs=files(repo)
    if len(fs)!=25: blockers.append(f"CHAPTER_COUNT:{len(fs)}!=25")

    cat_patterns={
      "standard":r"\\subsection\*\{Standard computations\}",
      "proof":r"\\subsection\*\{Proofs\}",
      "counterexample":r"\\subsection\*\{(?:Counterexamples|Counterexamples and hypothesis testing)\}",
      "application":r"\\subsection\*\{(?:Applications|Applications and investigations)\}",
      "challenge":r"\\subsection\*\{(?:Challenges|Challenge problems)\}",
    }

    for i,p in enumerate(fs,1):
        code=f"II/{i:02d}"; t=p.read_text(encoding="utf-8-sig")
        c={e:cnt(t,e) for e in ["example","exercise","hint","problem","solution"]}
        labels=LABEL.findall(t); all_labels += [(x,code) for x in labels]
        exblocks=list(EXAMPLE_BLOCK.finditer(t))
        placed=[]
        for b in exblocks:
            sec=preceding_section(t,b.start()); placed.append(sec)
            if sec.strip().lower()=="worked examples":
                blockers.append(f"{code}:EXPANSION_EXAMPLE_IN_COLLECTED_SECTION:{b.group(1)}")
        if len(exblocks)!=3: blockers.append(f"{code}:EXPANSION_EXAMPLES:{len(exblocks)}!=3")
        if c["example"]<6: blockers.append(f"{code}:EXAMPLES:{c['example']}<6")
        if c["exercise"]<24: blockers.append(f"{code}:EXERCISES:{c['exercise']}<24")
        if c["exercise"]!=c["hint"]: blockers.append(f"{code}:EXERCISE_HINT_MISMATCH")
        if c["solution"]<c["exercise"]+c["problem"]: blockers.append(f"{code}:SOLUTION_COVERAGE")
        for cat,pat in cat_patterns.items():
            if not re.search(pat,t): blockers.append(f"{code}:MISSING_GRADED_CATEGORY:{cat}")

        old=next((x for x in base.get("chapters",[]) if x.get("chapter")==code),None)
        protected=sha(strip(t))
        if old and old.get("protected_sha256")!=protected:
            blockers.append(f"{code}:PROTECTED_TEXT_CHANGED")
        if old and c["example"]<old.get("examples",0):
            blockers.append(f"{code}:EXAMPLE_COUNT_DECREASE")
        if old and c["exercise"]<old.get("exercises",0):
            blockers.append(f"{code}:EXERCISE_COUNT_DECREASE")

        rows.append({"chapter":code,**c,"expansion_examples":len(exblocks),
                     "placed_after":" | ".join(placed),"protected_sha256":protected})

    counts=Counter(x for x,_ in all_labels)
    for label,n in counts.items():
        if n>1: blockers.append(f"DUPLICATE_LABEL:{label}")

    status="PASS" if not blockers else "FAIL"
    result={"status":status,"chapters":rows,"blocking":blockers}
    print(json.dumps({"status":status,"blocking":blockers},indent=2))

    if a.write:
        out=repo/REPORT; out.mkdir(parents=True,exist_ok=True)
        (out/"VOLUME02_EXAMPLE_EXERCISE_BALANCE_AUDIT.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
        md=["# Volume II worked-example placement and graded-exercise balance","",
            f"**Result:** {status}","",
            "| Chapter | Examples | Exercises | Hints | Problems | Solutions | Expansion examples |",
            "|---|---:|---:|---:|---:|---:|---:|"]
        for r in rows:
            md.append(f"| {r['chapter']} | {r['example']} | {r['exercise']} | {r['hint']} | {r['problem']} | {r['solution']} | {r['expansion_examples']} |")
        md += ["","## Placement evidence",""]
        for r in rows: md.append(f"- **{r['chapter']}**: {r['placed_after']}")
        md += ["","## Blocking findings",""]
        md += [f"- {b}" for b in blockers] if blockers else ["None."]
        (out/"VOLUME02_EXAMPLE_EXERCISE_BALANCE_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    raise SystemExit(0 if status=="PASS" else 12)

if __name__=="__main__": main()
