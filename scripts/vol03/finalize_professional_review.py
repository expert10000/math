#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path
BASE="9b5a9df81037a845af81982efc95dcd6139ab53a"
PARENT="c714fb71a1dea249d200735059ee22d3dd859085"

def load(p:Path)->dict: return json.loads(p.read_text(encoding="utf-8-sig"))

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); a=ap.parse_args(); repo=Path(a.repo).resolve(); reports=repo/"reports/vol03"; builddir=repo/"build/vol03-review"; blocking=[]
    math=load(reports/"VOL03_REMAINING_MATH_REPAIRS.json"); prereq=load(reports/"VOL03_PREREQUISITE_AUDIT.json"); hints=load(reports/"VOL03_HINT_THEOREM_AUDIT.json"); gates=load(builddir/"gates.json")
    if math.get("status")!="PASS" or math.get("chapters_reviewed")!=28: blocking.append("mathematical review evidence is not PASS/28")
    if prereq.get("status")!="PASS": blocking.append("prerequisite/notation audit is not PASS")
    if hints.get("status")!="PASS" or hints.get("hints_reviewed")!=672: blocking.append("hint/theorem audit is not PASS/672")
    if gates.get("status")!="PASS": blocking.append("current-source reconciliation/build aggregate is not PASS")
    rows=gates.get("gates",[]); structural=next((g for g in rows if g.get("name","").startswith("bundle structural")),None); build=next((g for g in rows if "LaTeX build" in g.get("name","")),None)
    if not structural: blocking.append("structural gate missing")
    if not build: blocking.append("build gate missing")
    counts=structural.get("totals",{}) if structural else {}
    expected={"problem":336,"exercise":672,"hint":672,"solution":1008}
    if structural and structural.get("chapters")!=28: blocking.append("structural chapter count is not 28")
    for k,v in expected.items():
        if counts.get(k)!=v: blocking.append(f"{k}: expected {v}, found {counts.get(k)}")
    pdf=(repo/build["pdf"]) if build and build.get("pdf") else None
    if not pdf or not pdf.is_file(): pdf_hash=None; pdf_bytes=None; blocking.append("post-review PDF missing")
    else:
        data=pdf.read_bytes(); pdf_hash=hashlib.sha256(data).hexdigest(); pdf_bytes=len(data)
    if build and build.get("pdf_sha256") and build.get("pdf_sha256")!=pdf_hash: blocking.append("PDF hash differs from build gate")
    overfull=build.get("overfull_boxes",[]) if build else []
    if any(float(x)>=20 for x in overfull): blocking.append("overfull box >=20pt remains")
    freeze=subprocess.run(["git","diff","--name-only",BASE,"--","books/vol03_fourier_distributions_pde/freeze"],cwd=repo,capture_output=True,text=True)
    freeze_changed=[x for x in freeze.stdout.splitlines() if x.strip()]
    if freeze_changed: blocking.append("historical Volume III freeze changed")
    build_report={"schema":1,"status":"PASS" if build and build.get("status")=="PASS" and pdf_hash and not any("PDF" in x or "overfull" in x or "build" in x for x in blocking) else "FAIL","review_parent":PARENT,"command":build.get("command") if build else None,"exit_codes":build.get("exit_codes") if build else None,"pages":build.get("pages") if build else None,"pdf_bytes":pdf_bytes,"pdf_sha256":pdf_hash,"overfull_boxes":overfull,"significant_overfull_threshold_pt":20,"source_counts":{"chapters":structural.get("chapters") if structural else None,"problems":counts.get("problem"),"exercises":counts.get("exercise"),"hints":counts.get("hint"),"solutions":counts.get("solution")},"historical_freeze_rewritten":bool(freeze_changed)}
    (reports/"VOL03_BUILD_AFTER_PRO_REVIEW.json").write_text(json.dumps(build_report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    status="PASS" if not blocking and build_report["status"]=="PASS" else "FAIL"
    final={"schema":1,"status":status,"professional_review_base":BASE,"commit3_parent":PARENT,"scope":"Volume III III/01-III/28 professional review","mathematical_repairs":math.get("status"),"prerequisite_notation_audit":prereq.get("status"),"exercise_hint_theorem_audit":hints.get("status"),"hints_reviewed":hints.get("hints_reviewed"),"theorems_classified":hints.get("theorems_classified"),"build":build_report,"historical_v1_freeze_preserved":not freeze_changed,"blocking":blocking}
    (reports/"VOL03_PROFESSIONAL_REVIEW_FINAL.json").write_text(json.dumps(final,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume III — professional review final","",f"**Status:** {status}","",f"- Mathematical repairs: **{math.get('status')}**",f"- Prerequisite/notation audit: **{prereq.get('status')}**",f"- 672-hint/theorem audit: **{hints.get('status')}**",f"- Hints reviewed: **{hints.get('hints_reviewed')}/672**",f"- Clean build: **{build_report['status']}**",f"- PDF pages: **{build_report.get('pages')}**",f"- PDF bytes: **{build_report.get('pdf_bytes')}**",f"- PDF SHA-256: `{build_report.get('pdf_sha256')}`","","The historical v1.0 freeze is preserved; the current 672/672/1008 source inventory is recorded only under reports/vol03.","","## Blocking findings","",*( ["None."] if not blocking else [f"- {x}" for x in blocking])]
    (reports/"VOL03_PROFESSIONAL_REVIEW_FINAL.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(final,indent=2,ensure_ascii=False)); return 0 if status=="PASS" else 5

if __name__=="__main__": raise SystemExit(main())
