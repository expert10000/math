#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

BANNED = [
"explain and use",
"Identify the definition or structural theorem in this chapter that directly controls the question, then reduce the calculation to that statement.",
]
MEASURABLE = {
"apply","assemble","associate","build","change","check","choose","classify","compare","compute","construct",
"convert","decide","decompose","derive","describe","detect","determine","diagonalize","distinguish",
"explain","extend","extract","find","form","identify","interpret","perform","prove","read","recognize",
"recover","reduce","relate","rewrite","show","solve","test","track","transform","translate","unitarily","use","verify","write",
}

def read_status(repo: Path):
    path = repo / "editorial" / "CHAPTER_STATUS.tsv"
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--require-goals", action="store_true")
    ap.add_argument("--require-hints-through", type=int, default=0)
    ap.add_argument("--require-full", action="store_true")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    rows = [r for r in read_status(repo) if r.get("volume") == "I"]
    blockers=[]
    report=[]
    all_hints=[]
    total_goals=0
    total_hints=0
    banned_hits=0

    if len(rows)!=18:
        blockers.append(f"STATUS_ROWS:{len(rows)}!=18")

    for r in rows:
        code=r["chapter_code"]
        n=int(code.split("/")[1])
        p=repo/r["canonical_path"]
        if not p.exists():
            blockers.append(f"MISSING:{code}")
            continue
        text=p.read_text(encoding="utf-8-sig")
        m=re.search(
            r"\\section\*\{Learning goals\}(.*?)(?=\\section\*\{Conceptual roadmap\})",
            text,re.S
        )
        goals=[]
        if m:
            goals=[re.sub(r"\s+"," ",x).strip().rstrip(";") for x in re.findall(r"\\item\s+(.*?);",m.group(1),re.S)]
        total_goals+=len(goals)
        measurable=0
        for g in goals:
            first=re.sub(r"\\\([^)]*\\\)","",g).strip().split()
            if first and first[0].lower() in MEASURABLE:
                measurable+=1

        hints=[re.sub(r"\s+"," ",x).strip() for x in re.findall(r"\\begin\{hint\}(.*?)\\end\{hint\}",text,re.S)]
        total_hints+=len(hints)
        all_hints.extend(hints)
        local_banned=sum(sum(b.lower() in h.lower() for b in BANNED) for h in hints)
        banned_hits+=local_banned

        if args.require_goals or args.require_full:
            if len(goals)!=6:
                blockers.append(f"{code}:GOALS:{len(goals)}!=6")
            if measurable!=len(goals):
                blockers.append(f"{code}:NONMEASURABLE_GOALS:{len(goals)-measurable}")
            if "explain and use" in m.group(1).lower() if m else False:
                blockers.append(f"{code}:GENERIC_GOAL_PHRASE")

        if n <= args.require_hints_through or args.require_full:
            if len(hints)!=8:
                blockers.append(f"{code}:HINTS:{len(hints)}!=8")
            if local_banned:
                blockers.append(f"{code}:GENERIC_HINTS:{local_banned}")
            for i,h in enumerate(hints,1):
                if len(h)<25:
                    blockers.append(f"{code}:HINT_{i:02d}_TOO_SHORT:{len(h)}")
                if len(h)>420:
                    blockers.append(f"{code}:HINT_{i:02d}_TOO_LONG:{len(h)}")

        report.append({
            "chapter_code":code,
            "chapter_title":r["chapter_title"],
            "goals":len(goals),
            "measurable_goals":measurable,
            "hints":len(hints),
            "generic_hint_hits":local_banned,
        })

    dup_hints={h:n for h,n in Counter(all_hints).items() if n>1}
    if args.require_full:
        if total_goals!=108:
            blockers.append(f"TOTAL_GOALS:{total_goals}!=108")
        if total_hints!=144:
            blockers.append(f"TOTAL_HINTS:{total_hints}!=144")
        if banned_hits:
            blockers.append(f"TOTAL_GENERIC_HINT_HITS:{banned_hits}")
        if dup_hints:
            blockers.append(f"DUPLICATE_HINT_TEXTS:{len(dup_hints)}")

    outdir=repo/"reports/series"
    outdir.mkdir(parents=True,exist_ok=True)
    fields=["chapter_code","chapter_title","goals","measurable_goals","hints","generic_hint_hits"]
    with (outdir/"VOLUME01_PEDAGOGY_AUDIT.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n")
        w.writeheader();w.writerows(report)

    summary={
        "status":"PASS" if not blockers else "FAIL",
        "chapters":len(rows),
        "learning_outcomes":total_goals,
        "hints":total_hints,
        "generic_hint_hits":banned_hits,
        "duplicate_hint_texts":len(dup_hints),
        "required_hints_through":18 if args.require_full else args.require_hints_through,
        "blocking":blockers,
    }
    (outdir/"VOLUME01_PEDAGOGY_AUDIT.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=[
        "# Volume I Pedagogy Audit","",
        f"**Result:** {summary['status']}","",
        f"- Chapters: **{summary['chapters']} / 18**",
        f"- Learning outcomes: **{summary['learning_outcomes']}**",
        f"- Exercise hints: **{summary['hints']}**",
        f"- Generic hint hits: **{summary['generic_hint_hits']}**",
        f"- Duplicate hint texts: **{summary['duplicate_hint_texts']}**","",
        "## Blocking findings",""
    ]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (outdir/"VOLUME01_PEDAGOGY_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")

    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blockers else 3

if __name__=="__main__":
    raise SystemExit(main())
