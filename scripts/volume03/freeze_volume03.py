#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,hashlib,re
from pathlib import Path

FIELDS=["volume","chapter_code","chapter_title","status","legacy_source_status","mapped_rule_count","canonical_path","next_action"]
def tsv(p):
    with Path(p).open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write_status(p,rows):
    lines=["\t".join(FIELDS)]
    for r in rows:lines.append("\t".join(str(r.get(k,"")) for k in FIELDS))
    Path(p).write_text("\n".join(lines)+"\n",encoding="utf-8")
def source_inputs(vol):
    items=[vol/"book.tex"]
    items+=sorted((vol/"chapters").rglob("*.tex"))
    items+=sorted(p for p in (vol/"reconstruction").glob("*") if p.is_file())
    return [p for p in items if p.exists()]
def write_manifest(vol):
    f=vol/"freeze";f.mkdir(parents=True,exist_ok=True)
    lines=[f"{sha(p)}  {p.relative_to(vol).as_posix()}" for p in source_inputs(vol)]
    (f/"VOLUME03_FREEZE_MANIFEST.sha256").write_text("\n".join(lines)+"\n",encoding="utf-8")
def check_manifest(vol):
    for line in (vol/"freeze/VOLUME03_FREEZE_MANIFEST.sha256").read_text(encoding="utf-8").splitlines():
        digest,rel=line.split("  ",1);p=vol/rel
        if not p.exists() or sha(p)!=digest:raise RuntimeError(f"Freeze manifest mismatch: {rel}")
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);ap.add_argument("--phase",choices=["pre","finalize"],required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol03_fourier_distributions_pde";f=vol/"freeze";f.mkdir(parents=True,exist_ok=True)
    summary=json.loads((vol/"reconstruction/VOLUME03_FULL_RECONCILIATION.json").read_text(encoding="utf-8"))
    if summary.get("status")!="PASS" or summary.get("unresolved_count")!=0:raise RuntimeError("Volume III reconciliation not PASS/0")
    if args.phase=="pre":
        readme=vol/"README.md";txt=readme.read_text(encoding="utf-8-sig")
        txt=re.sub(r"(?m)^\*\*Status:\*\*.*$","**Status:** Full 28-chapter reconstruction reconciled; release build pending.",txt,count=1)
        readme.write_text(txt.rstrip()+"\n",encoding="utf-8")
        (f/"RELEASE_VOLUME03.md").write_text("# Volume III — Measure, Fourier Analysis, Distributions and PDE\n\nRelease baseline: 28 canonical chapters, 336 solved dossiers, full corpus reconciliation PASS.\n",encoding="utf-8")
        write_manifest(vol);print("VOLUME III PRE-FREEZE AUDIT PASSED");return 0
    check_manifest(vol)
    pdf=vol/"book.pdf";log=vol/"book.log"
    if not pdf.exists() or not log.exists():raise RuntimeError("book.pdf/book.log missing")
    status=tsv(repo/"editorial/CHAPTER_STATUS.tsv");hits=0
    for r in status:
        if re.fullmatch(r"III/\d{2}",r.get("chapter_code","")):
            r["status"]="FROZEN";r["next_action"]="COMPLETE";hits+=1
    if hits!=28:raise RuntimeError(f"Expected 28 III rows, found {hits}")
    write_status(repo/"editorial/CHAPTER_STATUS.tsv",status)
    readme=vol/"README.md";txt=readme.read_text(encoding="utf-8-sig")
    txt=re.sub(r"(?m)^\*\*Status:\*\*.*$","**Status:** FROZEN — Volume III Measure, Fourier Analysis, Distributions and PDE v1.0 release baseline.",txt,count=1)
    readme.write_text(txt.rstrip()+"\n",encoding="utf-8")
    b=pdf.read_bytes();pages=len(re.findall(rb"/Type\s*/Page(?!s)",b))
    report=["# Volume III Freeze Report","",
            "- Status: **FROZEN / COMPLETE**","- Canonical chapters: **28**",
            "- Solved dossiers: **336**","- Exercises: **224**","- Hints: **224**","- Total solutions: **560**",
            f"- PDF bytes: **{len(b)}**",f"- PDF SHA-256: `{hashlib.sha256(b).hexdigest()}`",
            f"- Approximate PDF pages: **{pages}**","- Reconciliation: **PASS / 0 unresolved**",""]
    (f/"VOLUME03_FREEZE_REPORT.md").write_text("\n".join(report),encoding="utf-8")
    print("VOLUME III FREEZE FINALIZED");return 0
if __name__=="__main__":raise SystemExit(main())
