#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,re
from collections import defaultdict
from pathlib import Path

MOJIBAKE=("Ã","Â","â€","â€“","â€”","Ä‚","Ă","Äą","Ë","Ĺ","Å","Â¬","Â©","Â¶")
FIELDS=["volume","chapter_code","chapter_title","status","legacy_source_status","mapped_rule_count","canonical_path","next_action"]

def read(p):return p.read_text(encoding="utf-8-sig",errors="replace")
def tsv(p):
    with p.open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def write_tsv(p,rows,fields):
    lines=["\t".join(fields)]
    for r in rows:lines.append("\t".join(str(r.get(f,"-") or "-") for f in fields))
    p.write_text("\n".join(lines)+"\n",encoding="utf-8")
def write_status(p,rows):
    lines=["\t".join(FIELDS)]
    for r in rows:lines.append("\t".join(str(r.get(f,"")) for f in FIELDS))
    p.write_text("\n".join(lines)+"\n",encoding="utf-8")
def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):h.update(b)
    return h.hexdigest()
def strip_comments(text):
    out=[]
    for line in text.splitlines():
        cut=len(line)
        for i,c in enumerate(line):
            if c!="%":continue
            bs=0;j=i-1
            while j>=0 and line[j]=="\\":bs+=1;j-=1
            if bs%2==0:cut=i;break
        out.append(line[:cut])
    return "\n".join(out)
def resolve(vol,target):
    p=vol/target
    for q in (p,Path(str(p)+".tex")):
        if q.exists():return q.resolve()
    return None
def graph(repo,vol):
    stack=[(vol/"book.tex").resolve()];seen=set();files=[];missing=[]
    rx=re.compile(r"\\(input|include)\{([^}]+)\}")
    while stack:
        p=stack.pop()
        if p in seen:continue
        seen.add(p);files.append(p)
        for kind,target in rx.findall(strip_comments(read(p))):
            q=resolve(vol,target)
            if q is None:missing.append(f"{p.relative_to(repo)}:{target}")
            elif q not in seen:stack.append(q)
    return files,missing
def source_exists(repo,name):
    for p in (repo/name,repo/"chapters/tex"/name):
        if p.exists():return p
    return None

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol01_linear_algebra";out=vol/"reconciliation";out.mkdir(exist_ok=True)
    status_all=tsv(repo/"editorial/CHAPTER_STATUS.tsv");rows=[r for r in status_all if r.get("volume")=="I"]
    src=tsv(repo/"editorial/SOURCE_MIGRATION.tsv");rules=[r for r in src if re.fullmatch(r"I/\d{2}",r.get("destination",""))]
    build,missing_inputs=graph(repo,vol)
    blockers=list(missing_inputs)

    labels=defaultdict(list);refs=[];stub_files=[];pair_rows=[]
    for p in build:
        text=read(p)
        rel=p.relative_to(repo).as_posix()
        if "Reconstruction scaffold" in text:stub_files.append(rel)
        if sum(text.count(x) for x in MOJIBAKE)+text.count("\ufffd"):blockers.append("ENCODING:"+rel)
        for lab in re.findall(r"\\label\{([^}]+)\}",text):labels[lab].append(rel)
        for kind,payload in re.findall(r"\\(ref|eqref|autoref|pageref|cref|Cref)\{([^}]+)\}",text):
            for lab in [x.strip() for x in payload.split(",") if x.strip()]:refs.append((rel,kind,lab))
        if "/chapters/" in rel and rel.endswith("/chapter.tex"):
            ex=len(re.findall(r"\\begin\{exercise\}",text,re.I))
            sol=len(re.findall(r"\\begin\{solution\}",text,re.I))
            hints=len(re.findall(r"\\begin\{hint\}",text,re.I))
            pair_rows.append({"path":rel,"exercises":ex,"hints":hints,"solutions":sol,
                              "paired":"YES" if ex==hints==sol and ex>0 else "NO"})
            if not (ex==hints==sol and ex>0):blockers.append(f"PAIRING:{rel}:{ex}/{hints}/{sol}")
    dups=sorted(k for k,v in labels.items() if len(v)>1)
    if dups:blockers.append("DUPLICATE_LABELS:"+",".join(dups[:20]))
    for rel,kind,lab in refs:
        if lab not in labels:blockers.append(f"MISSING_REF:{rel}:{lab}")
    if stub_files:blockers.extend("STUB:"+p for p in stub_files)
    if len(rows)!=18:blockers.append(f"STATUS_ROWS:{len(rows)}")
    if len([p for p in build if "/chapters/" in p.as_posix() and p.name=="chapter.tex"])!=18:
        blockers.append("ACTIVE_CHAPTER_GRAPH_NOT_18")

    rule_rows=[];missing_sources=0
    for r in rules:
        p=source_exists(repo,r.get("source_file",""))
        if not p:missing_sources+=1
        rule_rows.append({
          "chapter_code":r.get("destination",""),"source_file":r.get("source_file",""),
          "source_block_id":r.get("source_block_id",""),"block_kind":r.get("block_kind",""),
          "source_selector":r.get("source_selector",""),"source_title_or_pattern":r.get("source_title_or_pattern",""),
          "action":r.get("action",""),"precedence":r.get("precedence",""),
          "legacy_source_exists":"YES" if p else "NO",
          "canonical_target":next((x.get("canonical_path","") for x in rows if x.get("chapter_code")==r.get("destination")),"-"),
          "disposition":"ROUTED_TO_CANONICAL_CHAPTER" if p else "BLOCKED_MISSING_SOURCE"
        })
    if missing_sources:blockers.append(f"MISSING_LEGACY_SOURCES:{missing_sources}")

    blockers=sorted(set(blockers));status="PASS" if not blockers else "FAIL"
    if status=="PASS":
        for r in status_all:
            if r.get("volume")=="I":
                r["status"]="DRAFTED";r["next_action"]="FREEZE_READY"
        write_status(repo/"editorial/CHAPTER_STATUS.tsv",status_all)
        readme=vol/"README.md";txt=read(readme)
        txt=re.sub(r"(?m)^\*\*Status:\*\*.*$","**Status:** All 18 canonical chapters reconstructed and reconciled; freeze/release ready.",txt,count=1)
        readme.write_text(txt.rstrip()+"\n",encoding="utf-8")

    write_tsv(out/"VOLUME01_SOURCE_RULE_RECONCILIATION.tsv",rule_rows,[
      "chapter_code","source_file","source_block_id","block_kind","source_selector","source_title_or_pattern",
      "action","precedence","legacy_source_exists","canonical_target","disposition"])
    write_tsv(out/"VOLUME01_EXERCISE_PAIRING.tsv",pair_rows,["path","exercises","hints","solutions","paired"])
    summary={"status":status,"canonical_build_graph_tex_files":len(build),"status_rows":len(rows),
             "source_rules":len(rules),"missing_source_rules":missing_sources,"duplicate_labels":len(dups),
             "stub_files":len(stub_files),"unresolved_count":len(blockers),"unresolved":blockers}
    (out/"VOLUME01_RECONCILIATION_SUMMARY.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    rep=["# Volume I — Reconciliation Report","",f"**Result:** {status}","",
         f"- Canonical chapters: **18**",f"- Build-graph TeX files: **{len(build)}**",
         f"- Routed legacy/source rules: **{len(rules)}**",f"- Missing routed source files: **{missing_sources}**",
         f"- Duplicate build-graph labels: **{len(dups)}**",f"- Remaining scaffolds: **{len(stub_files)}**",
         f"- Unresolved blockers: **{len(blockers)}**","","## Unresolved blockers",""]
    rep += [f"- {x}" for x in blockers] if blockers else ["None."]
    (out/"VOLUME01_RECONCILIATION_REPORT.md").write_text("\n".join(rep)+"\n",encoding="utf-8")

    manifest_inputs=[vol/"book.tex",repo/"editorial/SOURCE_MIGRATION.tsv",out/"reconcile_volume01.py",
                     out/"VOLUME01_SOURCE_RULE_RECONCILIATION.tsv",out/"VOLUME01_EXERCISE_PAIRING.tsv",
                     out/"VOLUME01_RECONCILIATION_SUMMARY.json",out/"VOLUME01_RECONCILIATION_REPORT.md"]
    manifest_inputs += [p for p in build if p.is_file() and str(p).startswith(str(vol))]
    lines=[]
    for p in sorted(set(manifest_inputs),key=lambda x:x.as_posix()):
        lines.append(f"{sha(p)}  {p.relative_to(repo).as_posix()}")
    (out/"VOLUME01_RECONCILIATION_MANIFEST.sha256").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if status=="PASS" else 3
if __name__=="__main__":raise SystemExit(main())
