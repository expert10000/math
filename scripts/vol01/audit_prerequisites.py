#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,re,shutil,subprocess
from pathlib import Path

VOLDIR="books/vol01_linear_algebra"
CH = {
  1:"ch01_scalars_vectors_and_linear_combinations",
  2:"ch02_subspaces_span_and_linear_independence",
  3:"ch03_bases_and_dimension",
  4:"ch04_coordinates_and_change_of_basis",
  14:"ch14_gram_schmidt_and_orthogonal_projection",
}

def text(repo,n):
    return (repo/VOLDIR/"chapters"/CH[n]/"chapter.tex").read_text(encoding="utf-8-sig",errors="replace")

def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def run(cmd,cwd=None):
    cp=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,errors="replace")
    if cp.returncode!=0:
        raise RuntimeError("Command failed: "+" ".join(map(str,cmd))+"\n"+cp.stdout[-3000:]+"\n"+cp.stderr[-3000:])
    return cp

def write_tsv(path,rows,fields):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n")
        w.writeheader(); w.writerows(rows)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); ap.add_argument("--build",action="store_true")
    args=ap.parse_args(); repo=Path(args.repo).resolve(); reports=repo/"reports/vol01"; reports.mkdir(parents=True,exist_ok=True)
    c1,c2,c3,c4,c14=[text(repo,n) for n in (1,2,3,4,14)]
    blocking=[]

    if "2-3x+5x^2" in c1: blocking.append("I01 wrong polynomial target still present")
    if "2-3x-5x^2" not in c1 or "b-c=-5" not in c1:
        blocking.append("I01 corrected polynomial/equation missing")

    if "% VOL01-DEPENDENCY-PREVIEW-I01" not in c1:
        blocking.append("I01 preview-terminology marker missing")
    if "The vectors $u,v$ are independent, so" in c1:
        blocking.append("I01 proof still relies on pre-Ch2 independence")

    for needle in ("\\begin{vmatrix}","Set the \\(2\\times2\\) determinant to zero.","Two planar vectors are dependent exactly when the determinant"):
        if needle in c2: blocking.append("I02 hidden determinant prerequisite: "+needle)

    for needle in ("The trace map","Rank-nullity gives","nonzero linear functional and hence surjective"):
        if needle in c3: blocking.append("I03 hidden later prerequisite: "+needle)
    if "Chapter~8 will call the diagonal sum" not in c3 or "Chapter~6 later gives a rank--nullity argument" not in c3:
        blocking.append("I03 explicit preview cross-references missing")

    required_markers=[
      "% VOL01-DEPENDENCY-PREVIEW-I04-MAPS",
      "% VOL01-DEPENDENCY-PREVIEW-I04-LINEAR-MAPS",
      "% VOL01-DEPENDENCY-PREVIEW-I04-DUAL",
    ]
    for m in required_markers:
        if m not in c4: blocking.append("I04 preview marker missing: "+m)
    banned=[
      "The determinant confirms validity",
      "The determinant of the basis matrix is",
      "The determinant is $-1$",
      "Vectors and linear maps do not change when the basis changes",
      "Linear functionals transform by the inverse transpose",
      "derive the similarity relation between matrices of the same operator",
      "For an operator matrix, insert identity changes of coordinates",
    ]
    for needle in banned:
        if needle in c4: blocking.append("I04 hidden prerequisite remains: "+needle)
    if "\\begin{vmatrix}" in c4 or "\\det" in c4:
        blocking.append("I04 formal determinant computation remains before Ch8")

    for line in c14.splitlines():
        if "pseudoinverse" in line.lower():
            if "Preview" not in line or "Chapter~18" not in line:
                blocking.append("I14 pseudoinverse occurrence is not explicitly previewed")

    rows=[
      {"concept":"span; dependence; independence","introduced":"I/02","early_use":"I/01","policy":"chapter-wide preview + direct coefficient proofs","status":"PASS" if "% VOL01-DEPENDENCY-PREVIEW-I01" in c1 else "FAIL"},
      {"concept":"basis; dimension","introduced":"I/03","early_use":"I/01","policy":"chapter-wide preview; no later theorem used as premise","status":"PASS" if "% VOL01-DEPENDENCY-PREVIEW-I01" in c1 else "FAIL"},
      {"concept":"linear maps; isomorphisms","introduced":"I/05","early_use":"I/04","policy":"explicit local preview; coordinate map proved directly bijective and combination-preserving","status":"PASS" if "% VOL01-DEPENDENCY-PREVIEW-I04-MAPS" in c4 else "FAIL"},
      {"concept":"rank-nullity; kernels","introduced":"I/06","early_use":"I/03","policy":"formal use removed; later method mentioned only as preview","status":"PASS" if "Rank-nullity gives" not in c3 else "FAIL"},
      {"concept":"determinant; trace","introduced":"I/08","early_use":"I/02-I/04","policy":"formal tests removed; Chapter 8 references are previews only","status":"PASS" if not any(x in c2+c4 for x in ("\\begin{vmatrix}","The determinant confirms validity","The determinant of the basis matrix is")) else "FAIL"},
      {"concept":"dual coordinates; covectors","introduced":"after linear-map formalism","early_use":"I/04","policy":"optional self-contained preview; not used as prerequisite","status":"PASS" if "% VOL01-DEPENDENCY-PREVIEW-I04-DUAL" in c4 else "FAIL"},
      {"concept":"pseudoinverse","introduced":"I/18","early_use":"I/14","policy":"explicit Chapter 18 preview","status":"PASS" if "Chapter~18 introduces the pseudoinverse" in c14 else "FAIL"},
    ]
    write_tsv(reports/"VOL01_PREREQUISITE_GRAPH.tsv",rows,["concept","introduced","early_use","policy","status"])

    build_obj={"status":"NOT_RUN"}
    if args.build:
        latexmk=shutil.which("latexmk")
        if not latexmk:
            blocking.append("latexmk not found on PATH")
        else:
            vol=repo/VOLDIR
            try:
                run([latexmk,"-C","book.tex"],cwd=vol)
                run([latexmk,"-pdf","-interaction=nonstopmode","-halt-on-error","book.tex"],cwd=vol)
                pdf=vol/"book.pdf"; log=vol/"book.log"
                if not pdf.exists() or not log.exists():
                    raise RuntimeError("book.pdf/book.log missing after build")
                ltxt=log.read_text(encoding="utf-8-sig",errors="replace")
                hard=[
                  "LaTeX Warning: There were undefined references",
                  "There were undefined citations",
                  "multiply defined",
                  "Undefined control sequence",
                  "Fatal error occurred",
                  "Emergency stop",
                ]
                hits=[x for x in hard if x.lower() in ltxt.lower()]
                if hits: blocking.extend("BUILD:"+x for x in hits)
                pages=0
                pdfinfo=shutil.which("pdfinfo")
                if pdfinfo:
                    out=run([pdfinfo,str(pdf)]).stdout
                    m=re.search(r"(?m)^Pages:\s+(\d+)\s*$",out)
                    pages=int(m.group(1)) if m else 0
                if pages<=0:
                    data=pdf.read_bytes()
                    pages=len(re.findall(rb"/Type\s*/Page(?!s)\b",data))
                build_obj={
                  "schema":1,
                  "status":"PASS" if not hits and pages>0 else "FAIL",
                  "pdf":"books/vol01_linear_algebra/book.pdf",
                  "pages":pages,
                  "bytes":pdf.stat().st_size,
                  "sha256":sha(pdf),
                  "blocking":hits,
                }
            except Exception as exc:
                build_obj={"schema":1,"status":"FAIL","error":str(exc)}
                blocking.append("Volume I build failed: "+str(exc))

    (reports/"VOL01_RELEASE_BLOCKER_BUILD.json").write_text(json.dumps(build_obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    audit={
      "schema":1,
      "status":"PASS" if not blocking and (not args.build or build_obj.get("status")=="PASS") else "FAIL",
      "scope":"Volume I release-blocking mathematical correctness and prerequisite order",
      "chapters_checked":[1,2,3,4,14],
      "dependency_graph_rows":len(rows),
      "problem_i01_dossier_03_corrected":"2-3x-5x^2" in c1 and "b-c=-5" in c1,
      "build":build_obj,
      "blocking":blocking,
    }
    (reports/"VOL01_PREREQUISITE_AUDIT.json").write_text(json.dumps(audit,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=[
      "# Volume I — prerequisite and release-blocker audit","",
      f"**Status:** {audit['status']}","",
      "## Gates","",
      f"- Polynomial dossier correction: {'PASS' if audit['problem_i01_dossier_03_corrected'] else 'FAIL'}",
      f"- Dependency graph rows: **{len(rows)}**",
      f"- Volume I clean build: **{build_obj.get('status')}**",
      "",
      "## Policy","",
      "A concept used before its formal introduction must either be eliminated from the proof/solution or explicitly marked as a preview. Preview material may not be used as an unstated premise.",
      "",
      "## Blocking findings","",
    ]
    md += ["None."] if not blocking else [f"- {b}" for b in blocking]
    (reports/"VOL01_PREREQUISITE_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(audit,indent=2,ensure_ascii=False))
    return 0 if audit["status"]=="PASS" else 5

if __name__=="__main__":
    raise SystemExit(main())
