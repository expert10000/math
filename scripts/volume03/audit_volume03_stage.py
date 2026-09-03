#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path

def tsv(p):
    with Path(p).open("r",encoding="utf-8-sig",newline="") as f:
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
                if bs%2==0:cut=i;break
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
        for t in rx.findall(text):
            q=p.parent/t
            if q.suffix=="":q=q.with_suffix(".tex")
            stack.append(q)
    return sorted(seen)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--developed-through",type=int,required=True)
    ap.add_argument("--batch-start",type=int,required=True)
    ap.add_argument("--batch-end",type=int,required=True)
    args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol03_fourier_distributions_pde"
    status=tsv(repo/"editorial/CHAPTER_STATUS.tsv");src=tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    blockers=[];labels=[];total_p=total_e=total_h=total_s=0
    rows=[]
    for n in range(1,29):
        code=f"III/{n:02d}";sr=next((r for r in status if r.get("chapter_code")==code),None)
        if not sr:
            blockers.append(f"MISSING_STATUS:{code}");continue
        p=repo/sr["canonical_path"]
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
                blockers.append(f"PAIRING:{code}:problems={pr}:exercises={ex}:hints={hi}:solutions={so}")
            if sr.get("status")!="DRAFTED":
                blockers.append(f"STATUS:{code}:{sr.get('status')}")
        else:
            if not scaffold:blockers.append(f"EXPECTED_SCAFFOLD:{code}")
        rows.append({"chapter_code":code,"problems":pr,"exercises":ex,"hints":hi,"solutions":so,
                     "scaffold":"YES" if scaffold else "NO","status":sr.get("status","")})
        total_p+=pr;total_e+=ex;total_h+=hi;total_s+=so

    build=graph(vol/"book.tex")
    for p in build:
        text=strip_comments(p.read_text(encoding="utf-8-sig"))
        labels += re.findall(r"\\label\{([^}]+)\}",text)
    dup=sorted({x for x in labels if labels.count(x)>1})
    if dup:blockers.append("DUPLICATE_LABELS:"+",".join(dup[:20]))

    includes=len(re.findall(r"\\include\{chapters/",(vol/"book.tex").read_text(encoding="utf-8-sig")))
    if includes!=28:blockers.append(f"BOOK_INCLUDES:{includes}")

    tag=f"III{args.batch_start:02d}_III{args.batch_end:02d}"
    prov_path=vol/"reconstruction"/f"VOLUME03_{tag}_DOSSIER_PROVENANCE.tsv"
    acc_path=vol/"reconstruction"/f"VOLUME03_{tag}_SOURCE_RULE_ACCOUNTING.tsv"
    if not prov_path.exists():blockers.append(f"MISSING_PROVENANCE:{tag}");prov=[]
    else:prov=tsv(prov_path)
    if not acc_path.exists():blockers.append(f"MISSING_ACCOUNTING:{tag}");acc=[]
    else:acc=tsv(acc_path)
    expected_chapters=args.batch_end-args.batch_start+1
    if len(prov)!=12*expected_chapters:
        blockers.append(f"PROVENANCE_ROWS:{len(prov)}")
    batch_rules=[r for r in src if r.get("destination","").startswith("III/") and args.batch_start<=int(r["destination"].split("/")[1])<=args.batch_end]
    if len(acc)!=len(batch_rules):
        blockers.append(f"SOURCE_ACCOUNTING_ROWS:{len(acc)}:expected={len(batch_rules)}")
    unresolved=[r for r in acc if r.get("disposition","").startswith("UNRESOLVED")]
    if unresolved:blockers.append(f"UNRESOLVED_SOURCE_RULES:{len(unresolved)}")
    missing_sources=[r for r in acc if r.get("source_exists")!="YES"]
    if missing_sources:blockers.append(f"MISSING_SOURCE_FILES:{len(missing_sources)}")

    # mapped_rule_count must agree with live source map for all Volume III rows.
    for sr in status:
        code=sr.get("chapter_code","")
        if re.fullmatch(r"III/\d{2}",code):
            expected=sum(1 for r in src if r.get("destination")==code)
            try:actual=int(sr.get("mapped_rule_count") or 0)
            except:actual=-1
            if actual!=expected:blockers.append(f"MAPPED_RULE_COUNT:{code}:{actual}!={expected}")

    summary={
        "status":"PASS" if not blockers else "FAIL",
        "developed_through":args.developed_through,
        "book_includes":includes,
        "developed_chapters":args.developed_through,
        "solved_dossiers":total_p,
        "exercises":total_e,
        "hints":total_h,
        "solutions":total_s,
        "batch_source_rules":len(batch_rules),
        "batch_provenance_rows":len(prov),
        "batch_corpus_guided":sum(r.get("origin")=="CORPUS_GUIDED" for r in prov),
        "batch_fresh":sum(r.get("origin")=="FRESH_CANONICAL" for r in prov),
        "duplicate_labels":len(dup),
        "unresolved_count":len(blockers),
        "unresolved":blockers
    }
    out=vol/"reconstruction"
    (out/f"VOLUME03_{tag}_AUDIT.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume III Stage Audit","",f"**Result:** {summary['status']}","",
        f"- Developed through: **III/{args.developed_through:02d}**",
        f"- Active book includes: **{includes} / 28**",
        f"- Embedded solved dossiers: **{total_p}**",
        f"- Exercises / hints / total solutions: **{total_e} / {total_h} / {total_s}**",
        f"- Batch source rules accounted: **{len(acc)} / {len(batch_rules)}**",
        f"- Batch corpus-guided dossiers: **{summary['batch_corpus_guided']}**",
        f"- Batch fresh canonical dossiers: **{summary['batch_fresh']}**",
        f"- Duplicate labels: **{len(dup)}**","",
        "## Blockers",""]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (out/f"VOLUME03_{tag}_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blockers else 3

if __name__=="__main__":
    raise SystemExit(main())
