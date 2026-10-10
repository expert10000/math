#!/usr/bin/env python3
"""GA-03f.6 read-only release gate; optionally writes a diagnostic TSV.

Never edits chapters, imported inventory, or existing audit ledgers.
Exit 0 = structural+mathematical gates passed (provenance remains separate).
"""
import argparse, csv, re, sys
from pathlib import Path

ROOT_CH = Path("books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex")
ROOT_AUD = Path("reports/companion/global_audit")
EXPECTED = {
    "V/10": ["CP-V-0018", "CP-V-0095"],
    "V/11": ["CP-V-0022", "CP-V-0096"],
    "V/12": ["CP-V-0023", "CP-V-0105"],
    "V/13": ["CP-V-0020", "CP-V-0021", "CP-V-0025", "CP-V-0058"],
    "V/14": ["CP-V-0019", "CP-V-0106"],
    "V/26": ["CP-V-0047", "CP-V-0048"],
    "V/27": ["CP-V-0045", "CP-V-0113"],
    "V/28": ["CP-V-0044", "CP-V-0114"],
}
def readtsv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def run(repo):
    checks = []
    def check(code, ok, detail):
        checks.append((code, "PASS" if ok else "FAIL", str(detail)))
    chapter = repo / ROOT_CH
    if not chapter.is_file():
        print("ERROR: missing chapter", chapter)
        return [("CHAPTER", "FAIL", "chapter absent")]
    source = chapter.read_text(encoding="utf-8")
    sections = list(re.finditer(r'\\section\*\{(V/\d{2})\s+---\s+[^}]*\}', source))
    bysec = {}
    for i,m in enumerate(sections):
        stop = sections[i+1].start() if i+1<len(sections) else len(source)
        bysec[m.group(1)] = source[m.end():stop]
    allids=[]
    for sec, want in EXPECTED.items():
        block=bysec.get(sec,"")
        found=re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]',block)
        solutions=len(re.findall(r'\\begin\{solution\}',block))
        check("STRUCT_"+sec, set(found)==set(want) and len(found)==len(want) and solutions==len(want),
              f"problems={len(found)}, solutions={solutions}, IDs={','.join(found)}")
        allids+=found
    check("UNIQUE_IDS",len(allids)==18 and len(set(allids))==18,f"IDs={len(allids)}, unique={len(set(allids))}")
    def problem(pid):
        a=source.find(r'\begin{problem}['+pid+']')
        if a < 0: return ""
        b=source.find(r'\end{solution}',a)
        return source[a:b] if b>=0 else ""
    p18=problem("CP-V-0018")
    check("CP0018_CRT",
          ("f(0)=g(0)" in p18 or "f(0) = g(0)" in p18)
          and "and the two factors generate comaximal ideals" not in p18,
          "fiber-product explanation present; invalid CRT claim absent")
    p96=problem("CP-V-0096")
    check("CP0096_BASE_CHANGE",r'\xrightarrow{\cdot f}' in p96 and
          r'\operatorname{coker}' in p96 and
          "for \\(f=0\\)" in p96,
          "multiplication-by-f exact presentation, cokernel, f=0 case")
    aud=repo/ROOT_AUD
    cov=aud/"GA03F_INVENTORY_COVERAGE.tsv"
    if cov.is_file():
        rows=readtsv(cov)
        check("COVERAGE_LEDGER",len(rows)==18 and
              {r.get("companion_problem_id") for r in rows}==set(allids),
              f"rows={len(rows)}")
    else:check("COVERAGE_LEDGER",False,"missing")
    quality=aud/"GA03F_MATHEMATICAL_QUALITY.tsv"
    if quality.is_file():
        rows=readtsv(quality)
        ids={r.get("problem_id") for r in rows}
        p18status=next((r.get("mathematical_status") for r in rows if r.get("problem_id")=="CP-V-0018"),"")
        check("QUALITY_LEDGER",len(rows)==18 and ids==set(allids) and
              p18status=="PREVIOUSLY_CORRECTED_REVIEWED",
              f"rows={len(rows)}, CP-V-0018 status={p18status}")
    else:check("QUALITY_LEDGER",False,"missing")
    candidates=aud/"GA03F_SOURCE_CANDIDATES.tsv"
    evidence=aud/"GA03F_EVIDENCE_REVIEW.tsv"
    for name,path in [("CANDIDATES",candidates),("EVIDENCE",evidence)]:
        if path.is_file():
            rows=readtsv(path)
            check(name, bool(rows),f"rows={len(rows)}")
        else: check(name,False,"missing")
    # Not a failure of mathematical gate: editorial provenance may still be unresolved.
    print("GA-03f.6 RELEASE GATE")
    for name,status,detail in checks:
        print(f"  {status:4} {name}: {detail}")
    print("  NOTE: source equivalence is not proven by candidate scores.")
    return checks

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--repo",type=Path,default=Path("."))
    parser.add_argument("--apply",action="store_true",help="write new GA03F_RELEASE_GATE.tsv only")
    a=parser.parse_args()
    checks=run(a.repo.resolve())
    failures=[x for x in checks if x[1]!="PASS"]
    if a.apply:
        out=a.repo.resolve()/ROOT_AUD/"GA03F_RELEASE_GATE.tsv"
        out.parent.mkdir(parents=True,exist_ok=True)
        with out.open("w",encoding="utf-8",newline="") as f:
            w=csv.writer(f,delimiter="\t")
            w.writerow(["check","status","detail"])
            w.writerows(checks)
        print("WROTE:",out)
    print(f"GA-03f.6: {len(checks)-len(failures)}/{len(checks)} checks passed")
    if failures: sys.exit(1)

if __name__=="__main__":main()
