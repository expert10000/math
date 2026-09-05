#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, re
from pathlib import Path
from collections import Counter

VOL=Path("books/vol01_linear_algebra/chapters")
REPORT=Path("reports/series")
BLOCK=re.compile(r"\n?% BEGIN VOL01-EXPANSION ([^\n]+)\n.*?% END VOL01-EXPANSION \1\n?",re.S)
LABEL=re.compile(r"\\label\{([^}]+)\}")
EXAMPLE_BLOCK=re.compile(r"% BEGIN VOL01-EXPANSION (I\d\d-example-\d\d)\n(.*?)% END VOL01-EXPANSION \1",re.S)

def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()
def strip_blocks(t): return BLOCK.sub("",t)
def count(t,env): return len(re.findall(rf"\\begin\{{{env}\}}",t))
def files(repo): return sorted((repo/VOL).glob("ch*/chapter.tex"))

def preceding_section(text,pos):
    ms=list(re.finditer(r"\\section\{([^}]+)\}",text[:pos]))
    return ms[-1].group(1) if ms else ""

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--write",action="store_true")
    a=ap.parse_args(); repo=Path(a.repo).resolve()

    baseline=repo/REPORT/"VOLUME01_EXAMPLE_EXERCISE_BASELINE.json"
    blockers=[]; warnings=[]; rows=[]; all_labels=[]
    base=json.loads(baseline.read_text(encoding="utf-8")) if baseline.exists() else {}
    if not base: blockers.append("MISSING_COMMIT1_BASELINE")

    chapter_files=files(repo)
    if len(chapter_files)!=18: blockers.append(f"CHAPTER_COUNT:{len(chapter_files)}!=18")

    for i,p in enumerate(chapter_files,1):
        code=f"I/{i:02d}"
        t=p.read_text(encoding="utf-8-sig")
        c={e:count(t,e) for e in ["example","exercise","hint","solution","problem"]}
        labels=LABEL.findall(t); all_labels.extend((x,code) for x in labels)
        exblocks=list(EXAMPLE_BLOCK.finditer(t))
        placed=[]
        for b in exblocks:
            sec=preceding_section(t,b.start())
            placed.append(sec)
            if sec.strip().lower()=="worked examples":
                blockers.append(f"{code}:EXPANSION_EXAMPLE_IN_COLLECTED_WORKED_SECTION:{b.group(1)}")
        if len(exblocks)!=3:
            blockers.append(f"{code}:EXPANSION_EXAMPLES:{len(exblocks)}!=3")
        if c["example"]<6: blockers.append(f"{code}:EXAMPLES:{c['example']}<6")
        if c["exercise"]<24: blockers.append(f"{code}:EXERCISES:{c['exercise']}<24")
        if c["exercise"]!=c["hint"]: blockers.append(f"{code}:EXERCISE_HINT:{c['exercise']}!={c['hint']}")
        if c["solution"]<c["exercise"]+c["problem"]:
            blockers.append(f"{code}:SOLUTION_COVERAGE:{c['solution']}<{c['exercise']+c['problem']}")

        # Supplementary category structure: exact headings created by the expansion packages.
        cat_checks={
          "standard":r"\\subsection\*\{Standard computations\}",
          "proof":r"\\subsection\*\{Proofs\}",
          "counterexample":r"\\subsection\*\{(?:Counterexamples|Counterexamples and hypothesis testing)\}",
          "application":r"\\subsection\*\{(?:Applications|Applications and investigations)\}",
          "challenge":r"\\subsection\*\{(?:Challenges|Challenge problems)\}",
        }
        for cat,pat in cat_checks.items():
            if not re.search(pat,t):
                blockers.append(f"{code}:MISSING_GRADED_CATEGORY:{cat}")

        old=next((x for x in base.get("chapters",[]) if x.get("chapter")==code),None)
        protected_sha=sha(strip_blocks(t))
        if old and old.get("protected_sha256")!=protected_sha:
            blockers.append(f"{code}:PROTECTED_TEXT_CHANGED")
        if old and c["example"]<old.get("examples",0):
            blockers.append(f"{code}:EXAMPLE_COUNT_DECREASE")
        if old and c["exercise"]<old.get("exercises",0):
            blockers.append(f"{code}:EXERCISE_COUNT_DECREASE")

        rows.append({
          "chapter":code,"examples":c["example"],"exercises":c["exercise"],
          "hints":c["hint"],"problems":c["problem"],"solutions":c["solution"],
          "expansion_examples":len(exblocks),"placed_after":" | ".join(placed),
          "protected_sha256":protected_sha
        })

    counts=Counter(x for x,_ in all_labels)
    for label,n in sorted(counts.items()):
        if n>1:
            where=[c for x,c in all_labels if x==label]
            blockers.append(f"DUPLICATE_LABEL:{label}:{','.join(where)}")

    status="PASS" if not blockers else "FAIL"
    result={"status":status,"chapters":rows,"blocking":blockers,"warnings":warnings}
    print(json.dumps({"status":status,"blocking":blockers},indent=2))

    if a.write:
        outdir=repo/REPORT; outdir.mkdir(parents=True,exist_ok=True)
        (outdir/"VOLUME01_EXAMPLE_EXERCISE_BALANCE_AUDIT.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
        md=["# Volume I worked-example placement and graded-exercise balance","",
            f"**Result:** {status}","",
            "| Chapter | Examples | Exercises | Hints | Problems | Solutions | Expansion examples |",
            "|---|---:|---:|---:|---:|---:|---:|"]
        for r in rows:
            md.append(f"| {r['chapter']} | {r['examples']} | {r['exercises']} | {r['hints']} | {r['problems']} | {r['solutions']} | {r['expansion_examples']} |")
        md += ["","## Placement evidence",""]
        for r in rows:
            md.append(f"- **{r['chapter']}**: {r['placed_after']}")
        md += ["","## Blocking findings",""]
        md += [f"- {x}" for x in blockers] if blockers else ["None."]
        (outdir/"VOLUME01_EXAMPLE_EXERCISE_BALANCE_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")

    raise SystemExit(0 if status=="PASS" else 12)
if __name__=="__main__": main()

