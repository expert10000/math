#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,re,shutil,subprocess,tempfile
from collections import Counter
from pathlib import Path

VOL=Path("books/vol04_complex_analysis/chapters"); REPORT=Path("reports/series")
LABEL=re.compile(r"\\label\{([^}]+)\}")
BLOCK=re.compile(r"% BEGIN VOL04-EXPANSION ([^\n]+)\n.*?% END VOL04-EXPANSION \1\n?",re.S)
def hfile(p:Path)->str:
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
def sha_text(t:str)->str: return hashlib.sha256(t.encode("utf-8")).hexdigest()
def cnt(t:str,e:str)->int: return len(re.findall(rf"\\begin\{{{e}\}}",t))
def build_pdf(repo:Path):
    exe=shutil.which("pdflatex")
    if not exe: raise RuntimeError("pdflatex not found")
    vol=repo/"books/vol04_complex_analysis"; book=vol/"book.tex"
    if not book.exists(): raise RuntimeError(f"missing {book}")
    td=tempfile.TemporaryDirectory(prefix="vol04_reconcile_"); out=Path(td.name)
    stdout=""
    for _ in range(3):
        p=subprocess.run([exe,"-interaction=nonstopmode","-halt-on-error",f"-output-directory={out}",book.name],cwd=vol,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdout=p.stdout
        if p.returncode!=0: break
    return td,out/"book.pdf",out/"book.log",stdout

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); a=ap.parse_args(); repo=Path(a.repo).resolve(); out=repo/REPORT; out.mkdir(parents=True,exist_ok=True)
    base_path=out/"VOLUME04_EXAMPLE_EXERCISE_BASELINE.json"; base=json.loads(base_path.read_text(encoding="utf-8")) if base_path.exists() else {}
    blockers=[]; rows=[]; hashes=[]; labels=[]
    if not base: blockers.append("MISSING_COMMIT1_BASELINE")
    for required in ["VOLUME04_EXAMPLE_EXERCISE_AUDIT.json","VOLUME04_EXAMPLE_EXERCISE_BALANCE_AUDIT.json"]:
        p=out/required
        if not p.exists(): blockers.append(f"MISSING_REPORT:{required}")
        else:
            try:
                if json.loads(p.read_text(encoding="utf-8")).get("status")!="PASS": blockers.append(f"REPORT_NOT_PASS:{required}")
            except Exception: blockers.append(f"REPORT_UNREADABLE:{required}")
    files=sorted((repo/VOL).glob("ch*/chapter.tex"))
    if len(files)!=31: blockers.append(f"CHAPTER_COUNT:{len(files)}!=31")
    for i,p in enumerate(files,1):
        code=f"IV/{i:02d}"; t=p.read_text(encoding="utf-8-sig"); labs=LABEL.findall(t); labels+=labs
        row={"chapter":code,"examples":cnt(t,"example"),"exercises":cnt(t,"exercise"),"hints":cnt(t,"hint"),"problems":cnt(t,"problem"),"solutions":cnt(t,"solution"),"labels":len(labs)}
        rows.append(row); hashes.append({"chapter":code,"path":p.relative_to(repo).as_posix(),"sha256":hfile(p)})
        old=next((x for x in base.get("chapters",[]) if x.get("chapter")==code),None)
        if old:
            protected=sha_text(BLOCK.sub("",t))
            if protected!=old.get("protected_sha256"): blockers.append(f"{code}:PROTECTED_TEXT_CHANGED")
            exp={"examples":old["examples"]+3,"exercises":old["exercises"]+16,"hints":old["hints"]+16,"solutions":old["solutions"]+16}
            for k,v in exp.items():
                if row[k]!=v: blockers.append(f"{code}:{k.upper()}:{row[k]}!={v}")
        else: blockers.append(f"{code}:MISSING_BASELINE_ROW")
        if row["exercises"]!=row["hints"]: blockers.append(f"{code}:EXERCISE_HINT_MISMATCH")
        if row["solutions"]<row["exercises"]+row["problems"]: blockers.append(f"{code}:SOLUTION_COVERAGE")
    for lab,n in Counter(labels).items():
        if n>1: blockers.append(f"DUPLICATE_LABEL:{lab}")

    td=None; pdfinfo={"path":"temporary build/book.pdf","bytes":None,"sha256":None}; logtext=""
    try:
        td,pdf,log,stdout=build_pdf(repo)
        logtext=log.read_text(encoding="utf-8",errors="replace") if log.exists() else stdout
        if not pdf.exists(): blockers.append("PDF_MISSING")
        else: pdfinfo={"path":"temporary build/book.pdf","bytes":pdf.stat().st_size,"sha256":hfile(pdf)}
        for pat in ["Fatal error occurred","Emergency stop","! LaTeX Error","Undefined control sequence","!  ==> Fatal error"]:
            if pat in logtext: blockers.append(f"TEX_FATAL:{pat}")
        if "There were undefined references" in logtext: blockers.append("UNDEFINED_REFERENCES")
        if "Rerun to get cross-references right" in logtext: blockers.append("RERUN_WARNING_AFTER_THREE_PASSES")
    except Exception as e:
        blockers.append(f"BUILD_EXCEPTION:{type(e).__name__}:{e}")

    totals={k:sum(r[k] for r in rows) for k in ["examples","exercises","hints","problems","solutions","labels"]}
    status="PASS" if not blockers else "FAIL"; result={"status":status,"chapters":rows,"totals":totals,"pdf":pdfinfo,"blocking":blockers}
    (out/"VOLUME04_EXAMPLE_EXERCISE_RECONCILIATION.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    with (out/"VOLUME04_EXAMPLE_EXERCISE_COUNTS.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["chapter","examples","exercises","hints","problems","solutions","labels"],delimiter="\t"); w.writeheader(); w.writerows(rows)
    with (out/"VOLUME04_EXAMPLE_EXERCISE_HASHES.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["chapter","path","sha256"],delimiter="\t"); w.writeheader(); w.writerows(hashes)
    md=["# Volume IV pedagogy reconciliation after example/exercise expansion","",f"**Result:** {status}","","## Totals",""]
    for k,v in totals.items(): md.append(f"- {k}: **{v}**")
    md += ["","## Canonical compile evidence","",f"- temporary PDF bytes: `{pdfinfo['bytes']}`",f"- temporary PDF SHA-256: `{pdfinfo['sha256']}`","","## Invariants","","- all 31 chapters match their Commit-1 protected SHA after stripping VOL04 expansion blocks","- every chapter has exactly three expansion examples and sixteen graded triads","- placement/balance audit is PASS","- three-pass Volume IV compile has no fatal or unresolved-reference blockers","","## Blocking findings",""]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (out/"VOLUME04_EXAMPLE_EXERCISE_RECONCILIATION.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    if td is not None: td.cleanup()
    print(json.dumps({"status":status,"totals":totals,"pdf":pdfinfo,"blocking":blockers},indent=2))
    return 0 if status=="PASS" else 13
if __name__=="__main__": raise SystemExit(main())
