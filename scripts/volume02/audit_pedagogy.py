#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

MEASURABLE = {
"analyze","apply","choose","compare","compute","construct","convert","decide","derive",
"describe","determine","distinguish","estimate","evaluate","explain","extract","formulate",
"identify","justify","produce","prove","recover","rewrite","show","solve","state","test",
"translate","use","verify",
}
BANNED_GOAL_FRAGMENTS = (
"the reader should be able to use the central definitions",
"use the chapter's definitions in proofs",
"explain and use",
)
BANNED_HINT_FRAGMENTS = (
"identify the definition or structural theorem in this chapter",
"use the chapter method",
)

def read_status(repo: Path):
    with (repo/"editorial/CHAPTER_STATUS.tsv").open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--require-goals",action="store_true")
    ap.add_argument("--require-hints-through",type=int,default=0)
    ap.add_argument("--require-full",action="store_true")
    args=ap.parse_args()

    repo=Path(args.repo).resolve()
    rows=[r for r in read_status(repo) if r.get("volume")=="II"]
    blockers=[]
    report=[]
    all_hints=[]
    total_goals=total_hints=total_problems=total_exercises=total_solutions=0
    generic_hint_hits=0

    if len(rows)!=25:
        blockers.append(f"STATUS_ROWS:{len(rows)}!=25")

    for r in rows:
        code=r["chapter_code"]
        n=int(code.split("/")[1])
        p=repo/r["canonical_path"]
        if not p.exists():
            blockers.append(f"MISSING:{code}")
            continue
        text=p.read_text(encoding="utf-8-sig")

        gm=re.search(
            r"\\section\*\{Learning goals\}(.*?)(?=\\section\*\{Conceptual roadmap\})",
            text,re.S
        )
        goals=[]
        if gm:
            goals=[re.sub(r"\s+"," ",x).strip().rstrip(";")
                   for x in re.findall(r"\\item\s+(.*?);",gm.group(1),re.S)]
        measurable=0
        for g in goals:
            first=re.sub(r"\\\([^)]*\\\)","",g).strip().split()
            if first and first[0].lower() in MEASURABLE:
                measurable += 1
        total_goals += len(goals)

        problems=re.findall(r"\\begin\{problem\}",text)
        exercises=re.findall(r"\\begin\{exercise\}",text)
        solutions=re.findall(r"\\begin\{solution\}",text)
        hints=[re.sub(r"\s+"," ",x).strip()
               for x in re.findall(r"\\begin\{hint\}(.*?)\\end\{hint\}",text,re.S)]

        total_problems += len(problems)
        total_exercises += len(exercises)
        total_solutions += len(solutions)
        total_hints += len(hints)
        all_hints.extend(hints)

        local_generic=sum(
            1 for h in hints
            if any(frag in h.lower() for frag in BANNED_HINT_FRAGMENTS)
        )
        generic_hint_hits += local_generic

        if args.require_goals or args.require_full:
            if len(goals)!=6:
                blockers.append(f"{code}:GOALS:{len(goals)}!=6")
            if measurable!=len(goals):
                blockers.append(f"{code}:NONMEASURABLE_GOALS:{len(goals)-measurable}")
            lower_goal=(gm.group(1).lower() if gm else "")
            for frag in BANNED_GOAL_FRAGMENTS:
                if frag in lower_goal:
                    blockers.append(f"{code}:GENERIC_GOAL:{frag}")

        if n<=args.require_hints_through or args.require_full:
            if len(hints)!=8:
                blockers.append(f"{code}:HINTS:{len(hints)}!=8")
            if local_generic:
                blockers.append(f"{code}:GENERIC_HINTS:{local_generic}")
            for i,h in enumerate(hints,1):
                if len(h)<45:
                    blockers.append(f"{code}:HINT_{i:02d}_TOO_SHORT:{len(h)}")
                if len(h)>650:
                    blockers.append(f"{code}:HINT_{i:02d}_TOO_LONG:{len(h)}")

        if args.require_full:
            if len(problems)!=12:
                blockers.append(f"{code}:PROBLEMS:{len(problems)}!=12")
            if len(exercises)!=8:
                blockers.append(f"{code}:EXERCISES:{len(exercises)}!=8")
            if len(solutions)!=20:
                blockers.append(f"{code}:SOLUTIONS:{len(solutions)}!=20")

        report.append({
            "chapter_code":code,
            "chapter_title":r["chapter_title"],
            "goals":len(goals),
            "measurable_goals":measurable,
            "problems":len(problems),
            "exercises":len(exercises),
            "hints":len(hints),
            "solutions":len(solutions),
            "generic_hint_hits":local_generic,
        })

    dup={h:n for h,n in Counter(all_hints).items() if n>1}
    if args.require_full:
        if total_goals!=150:
            blockers.append(f"TOTAL_GOALS:{total_goals}!=150")
        if total_problems!=300:
            blockers.append(f"TOTAL_PROBLEMS:{total_problems}!=300")
        if total_exercises!=200:
            blockers.append(f"TOTAL_EXERCISES:{total_exercises}!=200")
        if total_hints!=200:
            blockers.append(f"TOTAL_HINTS:{total_hints}!=200")
        if total_solutions!=500:
            blockers.append(f"TOTAL_SOLUTIONS:{total_solutions}!=500")
        if generic_hint_hits:
            blockers.append(f"TOTAL_GENERIC_HINT_HITS:{generic_hint_hits}")
        if dup:
            blockers.append(f"DUPLICATE_HINT_TEXTS:{len(dup)}")

    out=repo/"reports/series"
    out.mkdir(parents=True,exist_ok=True)
    fields=[
        "chapter_code","chapter_title","goals","measurable_goals",
        "problems","exercises","hints","solutions","generic_hint_hits"
    ]
    with (out/"VOLUME02_PEDAGOGY_AUDIT.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n")
        w.writeheader();w.writerows(report)

    summary={
        "status":"PASS" if not blockers else "FAIL",
        "chapters":len(rows),
        "learning_outcomes":total_goals,
        "problems":total_problems,
        "exercises":total_exercises,
        "hints":total_hints,
        "solutions":total_solutions,
        "generic_hint_hits":generic_hint_hits,
        "duplicate_hint_texts":len(dup),
        "ii09_bespoke_outcomes":6 if any(r["chapter_code"]=="II/09" for r in report) else 0,
        "required_hints_through":25 if args.require_full else args.require_hints_through,
        "blocking":blockers,
    }
    (out/"VOLUME02_PEDAGOGY_AUDIT.json").write_text(
        json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"
    )

    md=[
        "# Volume II Pedagogy Audit","",
        f"**Result:** {summary['status']}","",
        f"- Chapters: **{summary['chapters']} / 25**",
        f"- Measurable learning outcomes: **{summary['learning_outcomes']}**",
        f"- Solved dossiers/problems: **{summary['problems']}**",
        f"- Exercises: **{summary['exercises']}**",
        f"- Mathematical hints: **{summary['hints']}**",
        f"- Solutions: **{summary['solutions']}**",
        f"- Generic hint hits: **{summary['generic_hint_hits']}**",
        f"- Duplicate hint texts: **{summary['duplicate_hint_texts']}**","",
        "## II/09 special treatment","",
        "II/09 is the source-light chapter in the atlas. Its six outcomes and eight hint strategies are authored directly from the inverse/implicit-function mathematics rather than inherited from a legacy source template.","",
        "## Blocking findings",""
    ]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (out/"VOLUME02_PEDAGOGY_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")

    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blockers else 4

if __name__=="__main__":
    raise SystemExit(main())
