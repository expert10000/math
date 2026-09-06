#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess
from pathlib import Path

VI = "books/vol06_algebraic_geometry/chapters/ch41_divisor_class_groups/chapter.tex"
VI_WRONG = "books/vol06_algebraic_geometry/chapters/ch41_divisor_class_groups/figures/figure_07.tex"
VII = "books/vol07_differential_geometry/chapters/ch10_orientation_and_integration/chapter.tex"
VIII = "books/vol08_algebraic_topology/chapters/ch35_lefschetz_theory/chapter.tex"
TARGETS=[VI,VII,VIII]

VI_OLD=r'''\[
\boxed{
A_x\text{ UFD}
\Longrightarrow
\Cl(A)=\langle[L]\rangle,
\qquad
\operatorname{div}(x)=2L
\Longrightarrow
2[L]=0,
\qquad
L\text{ nonprincipal}
\Longrightarrow
\Cl(A)=\mathbb Z/2.
}
\]'''
VI_NEW=r'''\[
\boxed{\begin{aligned}
A_x\text{ UFD}
&\Longrightarrow \Cl(A)=\langle[L]\rangle,\\
\operatorname{div}(x)=2L
&\Longrightarrow 2[L]=0,\\
L\text{ nonprincipal}
&\Longrightarrow \Cl(A)=\mathbb Z/2.
\end{aligned}}
\]'''

VII_OLD=r'''\[
\boxed{\text{orientation}=\text{coherent sign of frames},\qquad
\int_M\omega=\text{coordinate integrals glued by a partition of unity}.}
\]'''
VII_NEW=r'''\[
\boxed{\begin{aligned}
\text{orientation}
  &=\text{coherent sign of frames},\\
\int_M\omega
  &=\text{coordinate integrals glued by a partition of unity}.
\end{aligned}}
\]'''

VIII_OLD=r'''\[
\text{homology}
\to
\text{cohomology}
\to
\text{cup/cap products}
\to
\text{Thom and Euler classes}
\to
\text{Poincaré duality}
\to
\text{intersection}
\to
\text{fixed-point theory}.
\]'''
VIII_NEW=r'''\[
\begin{aligned}
\text{homology}
&\to \text{cohomology}
\to \text{cup/cap products}
\to \text{Thom and Euler classes}\\
&\to \text{Poincaré duality}
\to \text{intersection}
\to \text{fixed-point theory}.
\end{aligned}
\]'''

REPL={VI:(VI_OLD,VI_NEW),VII:(VII_OLD,VII_NEW),VIII:(VIII_OLD,VIII_NEW)}

def sha256(p:Path):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def restore_wrong(repo:Path):
    cp=subprocess.run(["git","show",f"HEAD:{VI_WRONG}"],cwd=repo,capture_output=True)
    if cp.returncode!=0:
        raise RuntimeError("Cannot read HEAD version of "+VI_WRONG)
    (repo/VI_WRONG).write_bytes(cp.stdout)

def apply_changes(repo:Path):
    restore_wrong(repo)
    result={}
    for rel,(old,new) in REPL.items():
        p=repo/rel
        text=p.read_text(encoding="utf-8-sig")
        if old in text:
            text=text.replace(old,new,1)
            p.write_text(text,encoding="utf-8",newline="\n")
        elif new not in text:
            raise SystemExit("Expected layout construct not found: "+rel)
        result[rel]=sha256(p)
    return result

def severe(log:Path):
    text=log.read_text(encoding="utf-8-sig",errors="replace")
    pts=[float(x) for x in re.findall(r"Overfull \\hbox \(([-+]?[0-9.]+)pt too wide\)",text,re.I)]
    high=[x for x in pts if x>=20.0]
    return len(high),max(pts or [0.0])

def verify(repo:Path):
    reports=repo/"reports/series"
    tri=json.loads((reports/"V12_RC1_RESIDUAL_LAYOUT_TRIAGE.json").read_text(encoding="utf-8"))
    if tri.get("status")!="PASS" or int(tri.get("residual_ge_20pt",0))!=3:
        raise SystemExit("Corrected residual triage is not PASS.")
    rows={}; blockers=[]
    dirs={"VI":"vol06_algebraic_geometry","VII":"vol07_differential_geometry","VIII":"vol08_algebraic_topology"}
    for v,d in dirs.items():
        log=repo/"books"/d/"book.log"
        if not log.exists():
            blockers.append(v+":MISSING_LOG"); continue
        n,m=severe(log)
        rows[v]={"overfull_ge_20pt":n,"max_overfull_pt":m}
        if n: blockers.append(f"{v}:RESIDUAL_GE20={n}:MAX={m:.5f}")
    obj={
        "schema":2,"status":"PASS" if not blockers else "FAIL","candidate":"v1.2-rc1",
        "scope":"Corrected three local residual layout repairs",
        "before_overfull_ge_20pt":3,
        "after_affected_volume_overfull_ge_20pt":sum(r["overfull_ge_20pt"] for r in rows.values()),
        "affected_volume_logs":rows,
        "source_sha256":{rel:sha256(repo/rel) for rel in TARGETS},
        "restored_false_positive_source":VI_WRONG,
        "mathematical_content_changed":False,"repair_kind":"layout-only local reflow","blocking":blockers,
    }
    (reports/"V12_RC1_RESIDUAL_LAYOUT_REPAIR.json").write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# v1.2 RC1 corrected residual layout repair","",f"**Status:** {obj['status']}","",
        "- Original VI figure attribution corrected; `figure_07.tex` restored to its committed state.",
        "- Mathematical assertions/theorems/problems changed: **No**.",
        "- >=20pt findings before: **3**.",
        f"- >=20pt findings in VI/VII/VIII after repair: **{obj['after_affected_volume_overfull_ge_20pt']}**.","",
        "## Actual repaired sources",""]
    for rel in TARGETS: md.append(f"- `{rel}` — `{obj['source_sha256'][rel]}`")
    if blockers: md += ["","## Blocking findings",""]+[f"- {x}" for x in blockers]
    (reports/"V12_RC1_RESIDUAL_LAYOUT_REPAIR.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(obj,indent=2,ensure_ascii=False))
    return 0 if not blockers else 5

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    mode=ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--apply",action="store_true"); mode.add_argument("--verify",action="store_true")
    args=ap.parse_args(); repo=Path(args.repo).resolve()
    if args.apply:
        print(json.dumps({"status":"APPLIED","source_sha256":apply_changes(repo)},indent=2))
        return 0
    return verify(repo)

if __name__=="__main__":
    raise SystemExit(main())
