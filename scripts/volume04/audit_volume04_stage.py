#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path
def tsv(p):
    with Path(p).open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def strip_comments(text):
    out=[]
    for line in text.splitlines():
        cut=None
        for i,ch in enumerate(line):
            if ch=="%":
                bs=0;j=i-1
                while j>=0 and line[j]=="\\":bs+=1;j-=1
                if bs%2==0:cut=i;break
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)
def graph(root):
    seen=set();stack=[root];rx=re.compile(r"\\(?:input|include)\{([^}]+)\}")
    while stack:
        p=stack.pop().resolve()
        if p in seen or not p.exists():continue
        seen.add(p);text=strip_comments(p.read_text(encoding="utf-8-sig"))
        for t in rx.findall(text):
            q=p.parent/t
            if q.suffix=="":q=q.with_suffix(".tex")
            stack.append(q)
    return sorted(seen)
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);ap.add_argument("--developed-through",type=int,required=True);ap.add_argument("--batch-start",type=int,required=True);ap.add_argument("--batch-end",type=int,required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol04_complex_analysis";block=[];status=tsv(repo/"editorial/CHAPTER_STATUS.tsv");src=tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    probs=exs=hints=sols=0
    for n in range(1,32):
        code=f"IV/{n:02d}";sr=next((r for r in status if r.get("chapter_code")==code),None)
        if not sr:block.append(f"MISSING_STATUS:{code}");continue
        p=repo/sr["canonical_path"]
        if not p.exists():block.append(f"MISSING_CHAPTER:{code}");continue
        text=p.read_text(encoding="utf-8-sig");scaffold="Reconstruction scaffold" in text
        pr=len(re.findall(r"\\begin\{problem\}",text));ex=len(re.findall(r"\\begin\{exercise\}",text));hi=len(re.findall(r"\\begin\{hint\}",text));so=len(re.findall(r"\\begin\{solution\}",text))
        if n<=args.developed_through:
            if scaffold:block.append(f"UNEXPECTED_SCAFFOLD:{code}")
            if (pr,ex,hi,so)!=(12,8,8,20):block.append(f"PAIRING:{code}:{pr}/{ex}/{hi}/{so}")
            if sr.get("status")!="DRAFTED":block.append(f"STATUS:{code}:{sr.get('status')}")
        elif not scaffold:block.append(f"EXPECTED_SCAFFOLD:{code}")
        expected=sum(1 for r in src if r.get("destination")==code)
        try:actual=int(sr.get("mapped_rule_count") or 0)
        except:actual=-1
        if actual!=expected:block.append(f"MAPPED_RULE_COUNT:{code}:{actual}!={expected}")
        probs+=pr;exs+=ex;hints+=hi;sols+=so
    build=graph(vol/"book.tex");labels=[];refs=[]
    for p in build:
        text=strip_comments(p.read_text(encoding="utf-8-sig"));labels+=re.findall(r"\\label\{([^}]+)\}",text);refs+=re.findall(r"\\(?:ref|eqref|autoref|pageref|cref|Cref)\{([^}]+)\}",text)
    dups=sorted({x for x in labels if labels.count(x)>1})
    if dups:block.append("DUPLICATE_LABELS:"+",".join(dups[:20]))
    missingrefs=sorted({x for x in refs if x not in set(labels)})
    if missingrefs:block.append("MISSING_REFS:"+",".join(missingrefs[:20]))
    includes=len(re.findall(r"\\include\{chapters/",(vol/"book.tex").read_text(encoding="utf-8-sig")))
    if includes!=31:block.append(f"BOOK_INCLUDES:{includes}")
    tag=f"IV{args.batch_start:02d}_IV{args.batch_end:02d}";rec=vol/"reconstruction"
    pp=rec/f"VOLUME04_{tag}_DOSSIER_PROVENANCE.tsv";aa=rec/f"VOLUME04_{tag}_SOURCE_RULE_ACCOUNTING.tsv"
    prov=tsv(pp) if pp.exists() else [];acc=tsv(aa) if aa.exists() else []
    if not pp.exists():block.append(f"MISSING_PROVENANCE:{tag}")
    if not aa.exists():block.append(f"MISSING_ACCOUNTING:{tag}")
    expected_ch=args.batch_end-args.batch_start+1
    if len(prov)!=12*expected_ch:block.append(f"PROVENANCE_ROWS:{len(prov)}")
    rules=[r for r in src if re.fullmatch(r"IV/\d{2}",r.get("destination","")) and args.batch_start<=int(r["destination"].split("/")[1])<=args.batch_end]
    if len(acc)!=len(rules):block.append(f"ACCOUNTING_ROWS:{len(acc)}!={len(rules)}")
    if any(r.get("source_exists")!="YES" for r in acc):block.append("MISSING_BATCH_SOURCE_FILES")
    if any(r.get("disposition","").startswith("UNRESOLVED") for r in acc):block.append("UNRESOLVED_SOURCE_RULES")
    if (repo/"scripts/volume04/__pycache__").exists():block.append("PYTHON_CACHE_PRESENT")
    summary={"status":"PASS" if not block else "FAIL","developed_through":args.developed_through,"book_includes":includes,
             "solved_dossiers":probs,"exercises":exs,"hints":hints,"solutions":sols,"batch_source_rules":len(rules),
             "batch_provenance_rows":len(prov),"batch_corpus_guided":sum(r.get("origin")=="CORPUS_GUIDED" for r in prov),
             "duplicate_labels":len(dups),"missing_refs":len(missingrefs),"unresolved_count":len(block),"unresolved":block}
    (rec/f"VOLUME04_{tag}_AUDIT.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume IV Stage Audit","",f"**Result:** {summary['status']}","",f"- Developed through: **IV/{args.developed_through:02d}**",
        f"- Active includes: **{includes} / 31**",f"- Embedded solved dossiers: **{probs}**",
        f"- Exercises / hints / solutions: **{exs} / {hints} / {sols}**",
        f"- Batch source rules accounted: **{len(acc)} / {len(rules)}**",f"- Duplicate labels: **{len(dups)}**",f"- Missing refs: **{len(missingrefs)}**","",
        "## Blockers",""]
    md += [f"- {b}" for b in block] if block else ["None."]
    (rec/f"VOLUME04_{tag}_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False));return 0 if not block else 3
if __name__=="__main__":raise SystemExit(main())
