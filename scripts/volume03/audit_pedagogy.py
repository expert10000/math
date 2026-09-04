#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from collections import Counter
from pathlib import Path

MEASURABLE={
"analyze","apply","build","check","choose","classify","compare","compute","connect","construct","control","define",
"derive","determine","diagonalize","distinguish","embed","estimate","explain","extend","identify",
"interpret","justify","produce","prove","recover","separate","show","solve","track","translate",
"use","verify",
}
BANNED_GOALS=(
"state the central definitions precisely, prove the structural results",
"use the chapter's estimates in later analysis",
"explain and use",
)
BANNED_HINTS=(
"start from the precise definition or estimate in the corresponding section",
"identify the definition or structural theorem",
)

def read_status(repo):
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
    rows=[r for r in read_status(repo) if r.get("volume")=="III"]
    blockers=[]; report=[]; all_hints=[]
    totals={"goals":0,"problems":0,"exercises":0,"hints":0,"solutions":0}
    generic=0
    if len(rows)!=28: blockers.append(f"STATUS_ROWS:{len(rows)}!=28")

    for r in rows:
        code=r["chapter_code"];n=int(code.split("/")[1])
        p=repo/r["canonical_path"]
        if not p.exists():
            blockers.append(f"MISSING:{code}");continue
        text=p.read_text(encoding="utf-8-sig")
        gm=re.search(r"\\section\*\{Learning goals\}(.*?)(?=\\section\*\{Conceptual roadmap\})",text,re.S)
        goals=[]
        if gm:
            goals=[re.sub(r"\s+"," ",x).strip().rstrip(";")
                   for x in re.findall(r"\\item\s+(.*?);",gm.group(1),re.S)]
        measurable=0
        for g in goals:
            first=re.sub(r"\\\([^)]*\\\)","",g).strip().split()
            if first and first[0].lower() in MEASURABLE: measurable+=1

        problems=re.findall(r"\\begin\{problem\}",text)
        exercises=re.findall(r"\\begin\{exercise\}",text)
        hints=[re.sub(r"\s+"," ",x).strip() for x in re.findall(r"\\begin\{hint\}(.*?)\\end\{hint\}",text,re.S)]
        solutions=re.findall(r"\\begin\{solution\}",text)
        totals["goals"]+=len(goals);totals["problems"]+=len(problems)
        totals["exercises"]+=len(exercises);totals["hints"]+=len(hints);totals["solutions"]+=len(solutions)
        all_hints.extend(hints)
        local_generic=sum(1 for h in hints if any(x in h.lower() for x in BANNED_HINTS))
        generic+=local_generic

        if args.require_goals or args.require_full:
            if len(goals)!=6: blockers.append(f"{code}:GOALS:{len(goals)}!=6")
            if measurable!=len(goals): blockers.append(f"{code}:NONMEASURABLE_GOALS:{len(goals)-measurable}")
            lower=gm.group(1).lower() if gm else ""
            for frag in BANNED_GOALS:
                if frag in lower: blockers.append(f"{code}:GENERIC_GOAL:{frag}")

        if n<=args.require_hints_through or args.require_full:
            if len(hints)!=8: blockers.append(f"{code}:HINTS:{len(hints)}!=8")
            if local_generic: blockers.append(f"{code}:GENERIC_HINTS:{local_generic}")
            for i,h in enumerate(hints,1):
                if len(h)<55: blockers.append(f"{code}:HINT_{i:02d}_TOO_SHORT:{len(h)}")
                if len(h)>700: blockers.append(f"{code}:HINT_{i:02d}_TOO_LONG:{len(h)}")

        if args.require_full:
            if len(problems)!=12: blockers.append(f"{code}:PROBLEMS:{len(problems)}!=12")
            if len(exercises)!=8: blockers.append(f"{code}:EXERCISES:{len(exercises)}!=8")
            if len(solutions)!=20: blockers.append(f"{code}:SOLUTIONS:{len(solutions)}!=20")

        report.append({
            "chapter_code":code,"chapter_title":r["chapter_title"],
            "goals":len(goals),"measurable_goals":measurable,
            "problems":len(problems),"exercises":len(exercises),
            "hints":len(hints),"solutions":len(solutions),
            "generic_hint_hits":local_generic,
        })

    dup={h:n for h,n in Counter(all_hints).items() if n>1}
    if args.require_full:
        expected={"goals":168,"problems":336,"exercises":224,"hints":224,"solutions":560}
        for k,v in expected.items():
            if totals[k]!=v: blockers.append(f"TOTAL_{k.upper()}:{totals[k]}!={v}")
        if generic: blockers.append(f"TOTAL_GENERIC_HINT_HITS:{generic}")
        if dup: blockers.append(f"DUPLICATE_HINT_TEXTS:{len(dup)}")

    out=repo/"reports/series";out.mkdir(parents=True,exist_ok=True)
    fields=["chapter_code","chapter_title","goals","measurable_goals","problems","exercises","hints","solutions","generic_hint_hits"]
    with (out/"VOLUME03_PEDAGOGY_AUDIT.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n")
        w.writeheader();w.writerows(report)

    summary={
        "status":"PASS" if not blockers else "FAIL",
        "chapters":len(rows),"learning_outcomes":totals["goals"],
        "problems":totals["problems"],"exercises":totals["exercises"],
        "hints":totals["hints"],"solutions":totals["solutions"],
        "generic_hint_hits":generic,"duplicate_hint_texts":len(dup),
        "distribution_arc_chapters":"III/15-III/20",
        "pde_arc_chapters":"III/23-III/28",
        "required_hints_through":28 if args.require_full else args.require_hints_through,
        "blocking":blockers,
    }
    (out/"VOLUME03_PEDAGOGY_AUDIT.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume III Pedagogy Audit","",f"**Result:** {summary['status']}","",
        f"- Chapters: **{len(rows)} / 28**",
        f"- Measurable learning outcomes: **{totals['goals']}**",
        f"- Solved dossiers/problems: **{totals['problems']}**",
        f"- Exercises / hints / solutions: **{totals['exercises']} / {totals['hints']} / {totals['solutions']}**",
        f"- Generic hint hits: **{generic}**",
        f"- Duplicate hint texts: **{len(dup)}**","",
        "## Special arcs","",
        "- III/15–III/20: test functions, distributions, support, tempered distributions, distributional Fourier transform, weak derivatives.",
        "- III/23–III/28: weak boundary-value problems, fundamental solutions, Green kernels, elliptic maximum principles, spectral/transform PDE methods.","",
        "## Blocking findings",""]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (out/"VOLUME03_PEDAGOGY_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blockers else 5

if __name__=="__main__":
    raise SystemExit(main())
