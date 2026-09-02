#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,re,subprocess
from collections import defaultdict
from pathlib import Path
FIELDS=["volume","chapter_code","chapter_title","status","legacy_source_status","mapped_rule_count","canonical_path","next_action"]
def read(p):return p.read_text(encoding="utf-8-sig",errors="replace")
def tsv(p):
    with p.open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def write_status(p,rows):
    lines=["\t".join(FIELDS)]
    for r in rows:lines.append("\t".join(str(r.get(f,"")) for f in FIELDS))
    p.write_text("\n".join(lines)+"\n",encoding="utf-8")
def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):h.update(b)
    return h.hexdigest()
def verify_manifest(repo,p):
    errors=[];count=0
    for line in read(p).splitlines():
        if not line.strip():continue
        expected,rel=line.split(None,1);q=repo/rel.strip();count+=1
        if not q.exists():errors.append("MISSING:"+rel.strip())
        elif sha(q)!=expected:errors.append("DRIFT:"+rel.strip())
    return count,errors
def pdf_pages(p):return len(re.findall(rb"/Type\s*/Page(?!s)\b",p.read_bytes()))
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);ap.add_argument("--phase",choices=("pre","finalize"),required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol01_linear_algebra";recon=vol/"reconciliation";freeze=vol/"freeze";freeze.mkdir(exist_ok=True)
    summ=json.loads(read(recon/"VOLUME01_RECONCILIATION_SUMMARY.json"))
    errors=[]
    if summ.get("status")!="PASS" or summ.get("unresolved_count")!=0:errors.append("RECONCILIATION_NOT_PASS")
    count,errs=verify_manifest(repo,recon/"VOLUME01_RECONCILIATION_MANIFEST.sha256");errors+=errs
    rows=[r for r in tsv(repo/"editorial/CHAPTER_STATUS.tsv") if r.get("volume")=="I"]
    if len(rows)!=18:errors.append("STATUS_ROWS")
    if args.phase=="pre":
        for r in rows:
            if r.get("status")!="DRAFTED" or r.get("next_action")!="FREEZE_READY":errors.append("NOT_FREEZE_READY:"+r.get("chapter_code",""))
        print(f"reconciliation_manifest_entries={count}")
        if errors:
            print("VOLUME I PRE-FREEZE AUDIT FAILED")
            for e in errors:print("BLOCK:",e)
            return 2
        print("VOLUME I PRE-FREEZE AUDIT PASSED");return 0

    pdf=vol/"book.pdf";log=vol/"book.log"
    if not pdf.exists():errors.append("MISSING_PDF")
    if not log.exists():errors.append("MISSING_LOG")
    if log.exists():
        txt=read(log)
        for pat in ("LaTeX Warning: There were undefined references","There were undefined citations","multiply defined"):
            if pat.lower() in txt.lower():errors.append("BUILD_LOG:"+pat)
    if errors:
        for e in errors:print("BLOCK:",e)
        return 2
    allrows=tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    for r in allrows:
        if r.get("volume")=="I":r["status"]="FROZEN";r["next_action"]="COMPLETE"
    write_status(repo/"editorial/CHAPTER_STATUS.tsv",allrows)
    readme=vol/"README.md";txt=read(readme)
    txt=re.sub(r"(?m)^\*\*Status:\*\*.*$","**Status:** FROZEN — Volume I Linear Algebra v1.0 release baseline.",txt,count=1)
    if "## Freeze/release evidence" not in txt:txt += "\n\n## Freeze/release evidence\n\nSee `freeze/VOLUME01_FREEZE_REPORT.md` and `freeze/VOLUME01_FREEZE_MANIFEST.sha256`.\n"
    readme.write_text(txt.rstrip()+"\n",encoding="utf-8")
    inputs=[vol/"book.tex",readme,repo/"editorial/CHAPTER_STATUS.tsv",repo/"editorial/SOURCE_MIGRATION.tsv",freeze/"freeze_volume01.py",freeze/"RELEASE_VOLUME01.md"]
    inputs += list((vol/"chapters").rglob("*.tex"))+list(recon.glob("*"))
    dossier_dir=vol/"dossiers"
    if dossier_dir.exists():
        inputs += [p for p in dossier_dir.glob("*") if p.is_file()]
    lines=[f"{sha(p)}  {p.relative_to(repo).as_posix()}" for p in sorted(set(inputs),key=lambda x:x.as_posix()) if p.exists()]
    (freeze/"VOLUME01_FREEZE_MANIFEST.sha256").write_text("\n".join(lines)+"\n",encoding="utf-8")
    head=subprocess.check_output(["git","-C",str(repo),"rev-parse","HEAD"],text=True).strip()
    rep=["# Volume I — Freeze Report","","**Result:** PASS","",f"- Pre-freeze parent commit: `{head}`","- Canonical chapters: **18**",
         "- Corpus reconciliation: **PASS / zero unresolved**","- Clean canonical PDF build: **PASS**",f"- PDF pages: **{pdf_pages(pdf)}**",
         f"- PDF SHA-256: `{sha(pdf)}`",f"- PDF bytes: **{pdf.stat().st_size}**","- Chapter status: **FROZEN / COMPLETE**",
         f"- Freeze manifest entries: **{len(lines)}**"]
    (freeze/"VOLUME01_FREEZE_REPORT.md").write_text("\n".join(rep)+"\n",encoding="utf-8")
    print(f"VOLUME I FREEZE FINALIZED: pages={pdf_pages(pdf)} bytes={pdf.stat().st_size}")
    return 0
if __name__=="__main__":raise SystemExit(main())
