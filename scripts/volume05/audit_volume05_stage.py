#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path

def tsv(path):
    with Path(path).open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def strip_comments(text):
    out=[]
    for line in text.splitlines():
        cut=None
        for i,ch in enumerate(line):
            if ch=="%":
                bs=0;j=i-1
                while j>=0 and line[j]=="\\":
                    bs+=1;j-=1
                if bs%2==0:
                    cut=i;break
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)

def graph(root):
    seen=set();stack=[root]
    rx=re.compile(r"\\(?:input|include)\{([^}]+)\}")
    while stack:
        p=stack.pop().resolve()
        if p in seen or not p.exists():continue
        seen.add(p)
        text=strip_comments(p.read_text(encoding="utf-8-sig"))
        for target in rx.findall(text):
            q=p.parent/target
            if q.suffix=="":
                q=q.with_suffix(".tex")
            stack.append(q)
    return sorted(seen)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--developed-through",type=int,required=True)
    ap.add_argument("--batch-start",type=int,required=True)
    ap.add_argument("--batch-end",type=int,required=True)
    args=ap.parse_args()

    repo=Path(args.repo).resolve()
    vol=repo/"books/vol05_commutative_algebra"
    status=tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    src=tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    blockers=[]
    problems=exercises=hints=solutions=0

    for n in range(1,29):
        code=f"V/{n:02d}"
        row=next((r for r in status if r.get("chapter_code")==code),None)
        if not row:
            blockers.append(f"MISSING_STATUS:{code}");continue
        p=repo/row.get("canonical_path","")
        if not p.exists():
            blockers.append(f"MISSING_CHAPTER:{code}");continue
        text=p.read_text(encoding="utf-8-sig")
        scaffold="Reconstruction scaffold" in text
        pr=len(re.findall(r"\\begin\{problem\}",text))
        ex=len(re.findall(r"\\begin\{exercise\}",text))
        hi=len(re.findall(r"\\begin\{hint\}",text))
        so=len(re.findall(r"\\begin\{solution\}",text))
        if n<=args.developed_through:
            if scaffold:blockers.append(f"UNEXPECTED_SCAFFOLD:{code}")
            if (pr,ex,hi,so)!=(12,8,8,20):
                blockers.append(f"PAIRING:{code}:{pr}/{ex}/{hi}/{so}")
            if row.get("status")!="DRAFTED":
                blockers.append(f"STATUS:{code}:{row.get('status')}")
        elif not scaffold:
            blockers.append(f"EXPECTED_SCAFFOLD:{code}")

        live=sum(1 for r in src if r.get("destination")==code)
        try:ledger=int(row.get("mapped_rule_count") or 0)
        except:ledger=-1
        if live!=ledger:
            blockers.append(f"MAPPED_RULE_COUNT:{code}:{ledger}!={live}")
        problems+=pr;exercises+=ex;hints+=hi;solutions+=so

    book=vol/"book.tex"
    includes=len(re.findall(r"\\include\{chapters/",book.read_text(encoding="utf-8-sig")))
    if includes!=28:
        blockers.append(f"BOOK_INCLUDES:{includes}")

    build=graph(book);labels=[];refs=[]
    for p in build:
        text=strip_comments(p.read_text(encoding="utf-8-sig"))
        labels+=re.findall(r"\\label\{([^}]+)\}",text)
        refs+=re.findall(r"\\(?:ref|eqref|autoref|pageref|cref|Cref)\{([^}]+)\}",text)
    dups=sorted({x for x in labels if labels.count(x)>1})
    missingrefs=sorted({x for x in refs if x not in set(labels)})
    if dups:blockers.append("DUPLICATE_LABELS:"+",".join(dups[:30]))
    if missingrefs:blockers.append("MISSING_REFS:"+",".join(missingrefs[:30]))

    tag=f"V{args.batch_start:02d}_V{args.batch_end:02d}"
    rec=vol/"reconstruction"
    pp=rec/f"VOLUME05_{tag}_DOSSIER_PROVENANCE.tsv"
    aa=rec/f"VOLUME05_{tag}_SOURCE_RULE_ACCOUNTING.tsv"
    prov=tsv(pp) if pp.exists() else []
    acc=tsv(aa) if aa.exists() else []
    if not pp.exists():blockers.append(f"MISSING_PROVENANCE:{tag}")
    if not aa.exists():blockers.append(f"MISSING_ACCOUNTING:{tag}")
    expected_ch=args.batch_end-args.batch_start+1
    if len(prov)!=12*expected_ch:
        blockers.append(f"PROVENANCE_ROWS:{len(prov)}")
    rules=[
        r for r in src
        if re.fullmatch(r"V/\d{2}",r.get("destination",""))
        and args.batch_start<=int(r["destination"].split("/")[1])<=args.batch_end
    ]
    if len(acc)!=len(rules):
        blockers.append(f"ACCOUNTING_ROWS:{len(acc)}!={len(rules)}")
    if any(r.get("source_exists")!="YES" for r in acc):
        blockers.append("MISSING_BATCH_SOURCE_FILES")
    if any(r.get("disposition","").startswith("UNRESOLVED") for r in acc):
        blockers.append("UNRESOLVED_SOURCE_RULES")
    if (repo/"scripts/volume05/__pycache__").exists():
        blockers.append("PYTHON_CACHE_PRESENT")

    summary={
        "status":"PASS" if not blockers else "FAIL",
        "developed_through":args.developed_through,
        "book_includes":includes,
        "solved_dossiers":problems,
        "exercises":exercises,
        "hints":hints,
        "solutions":solutions,
        "batch_source_rules":len(rules),
        "batch_provenance_rows":len(prov),
        "batch_corpus_guided":sum(r.get("origin")=="CORPUS_GUIDED" for r in prov),
        "duplicate_labels":len(dups),
        "missing_refs":len(missingrefs),
        "unresolved_count":len(blockers),
        "unresolved":blockers
    }
    (rec/f"VOLUME05_{tag}_AUDIT.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=[
        "# Volume V Stage Audit","",f"**Result:** {summary['status']}","",
        f"- Developed through: **V/{args.developed_through:02d}**",
        f"- Active includes: **{includes} / 28**",
        f"- Embedded solved dossiers: **{problems}**",
        f"- Exercises / hints / solutions: **{exercises} / {hints} / {solutions}**",
        f"- Batch source rules accounted: **{len(acc)} / {len(rules)}**",
        f"- Duplicate labels: **{len(dups)}**",
        f"- Missing refs: **{len(missingrefs)}**","",
        "## Blockers",""
    ]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (rec/f"VOLUME05_{tag}_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blockers else 3

if __name__=="__main__":
    raise SystemExit(main())
