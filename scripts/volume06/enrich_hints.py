#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path

GUIDANCE = {'VI/07': 'Use the prime-ideal viewpoint: translate the statement into containment or specialization in the spectrum, then check it on '
          'basic Zariski neighborhoods.',
 'VI/08': 'Reduce the question to localization at the chosen element and the basic-open correspondence; track exactly which powers become '
          'invertible.',
 'VI/09': 'Separate generic-point behavior from closed-point behavior by comparing prime ideals, closures, and specialization relations.',
 'VI/10': 'Pass to the nilradical or the reduced quotient and ask which geometric data survives after nilpotents are removed.',
 'VI/13': 'Work stalkwise when equality, injectivity, surjectivity, or local behavior is at issue, and use the sheaf gluing axiom only '
          'after local compatibility is clear.',
 'VI/15': 'Compute kernels stalkwise, but remember that sheaf images generally require sheafification of the presheaf image before '
          'exactness can be read correctly.',
 'VI/16': 'Test exactness on stalks; for a connecting or lifting question, identify the local preimages first and then measure the '
          'obstruction to gluing them.',
 'VI/17': 'On a basic open, identify sections with the corresponding localization and compare restriction maps with further localization.',
 'VI/39': 'At a codimension-one point, use the local order of vanishing to compute the coefficient of the prime divisor and then assemble '
          'the divisor globally.',
 'VI/40': 'Choose local meromorphic equations on an open cover and compare their ratios on overlaps; Cartier data is multiplicative gluing '
          'data modulo units.',
 'VI/42': 'Move between invertible sheaves, transition functions, and Cartier divisors, and check tensor product by multiplying the '
          'corresponding cocycles.',
 'VI/43': 'Use the cubic equation together with the chosen point or tangent line, then interpret intersections with multiplicity rather '
          'than as distinct points only.',
 'VI/44': 'Write the rational map and its base locus explicitly, then follow exceptional curves and inverse images on the open sets where '
          'the map is defined.',
 'VI/45': 'Use the Rees-algebra or affine-chart description of the blow-up and track the exceptional divisor through the chart '
          'coordinates.',
 'VI/46': 'Exploit surjectivity of restriction maps: extend the required local section one open set at a time and use that extension to '
          'kill the cocycle or obstruction.',
 'VI/47': 'Write the Cech differential on the relevant overlaps and decide whether the given cocycle is a coboundary by constructing '
          'compatible local data.',
 'VI/48': 'Choose local lifts in the short exact sequence, subtract them on overlaps, and identify the resulting cocycle as the connecting '
          'cohomology class.',
 'VI/49': 'Reduce to the affine or acyclic case covered by the vanishing theorem, then verify that the sheaf and cover satisfy the exact '
          'hypotheses before concluding higher cohomology vanishes.'}
MARKER = "% PEDAGOGY-ENRICHED-VI"

def read_status(repo: Path):
    with (repo/"editorial/CHAPTER_STATUS.tsv").open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def strip_comments(text: str) -> str:
    out=[]
    for line in text.splitlines():
        cut=None
        for i,ch in enumerate(line):
            if ch=="%":
                bs=0;j=i-1
                while j>=0 and line[j]=="\\": bs+=1;j-=1
                if bs%2==0:
                    cut=i;break
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)

def resolve_tex_target(current: Path, target: str, roots):
    raw=Path(target);cands=[]
    if raw.is_absolute(): cands.append(raw)
    else:
        cands.append(current.parent/raw)
        for base in roots:cands.append(Path(base)/raw)
    expanded=[]
    for q in cands:
        expanded.append(q)
        if q.suffix=="":expanded.append(q.with_suffix(".tex"))
    for q in expanded:
        try: qq=q.resolve()
        except Exception: qq=q
        if qq.exists() and qq.is_file(): return qq
    return None

def tex_graph(root: Path, roots):
    root=root.resolve(); roots=[Path(x).resolve() for x in roots]
    seen=set(); stack=[root]
    rx=re.compile(r"\\(?:input|include)\{([^}]+)\}")
    while stack:
        p=stack.pop()
        if p in seen or not p.exists():continue
        seen.add(p)
        text=strip_comments(p.read_text(encoding="utf-8-sig",errors="replace"))
        for target in rx.findall(text):
            q=resolve_tex_target(p,target,roots)
            if q is not None and q not in seen:stack.append(q)
    return sorted(seen,key=lambda x:x.as_posix())

def chapter_paths(repo: Path):
    out={}
    for r in read_status(repo):
        code=(r.get("chapter_code") or "").strip()
        if code.startswith("VI/"):
            if r.get("status")!="FROZEN" or r.get("next_action")!="COMPLETE":
                raise RuntimeError(f"{code}: expected FROZEN/COMPLETE")
            out[code]=repo/r["canonical_path"]
    if len(out)!=49:raise RuntimeError(f"expected 49 Volume VI chapters, found {len(out)}")
    return out

HINT_RX=re.compile(r"\\begin\{hint\}(?P<body>.*?)\\end\{hint\}",re.S)

def enrich_file(path: Path, suffix: str):
    text=path.read_text(encoding="utf-8-sig")
    changed=0
    def repl(m):
        nonlocal changed
        body=m.group("body")
        if MARKER in body:
            return m.group(0)
        cleaned=body.strip()
        newbody="\n"+MARKER+"\n"+cleaned
        if cleaned and cleaned[-1] not in ".!?":newbody += "."
        newbody += " "+suffix+"\n"
        changed+=1
        return "\\begin{hint}"+newbody+"\\end{hint}"
    out=HINT_RX.sub(repl,text)
    if out!=text:path.write_text(out.rstrip()+"\n",encoding="utf-8")
    return changed

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--start",type=int,required=True)
    ap.add_argument("--end",type=int,required=True)
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    volroot=repo/"books/vol06_algebraic_geometry"
    cps=chapter_paths(repo)
    changed=0; touched=[]; active_hints=0
    for n in range(args.start,args.end+1):
        code=f"VI/{n:02d}"; cp=cps[code]
        graph=tex_graph(cp,[volroot,repo])
        hint_files=[p for p in graph if "\\begin{hint}" in p.read_text(encoding="utf-8-sig",errors="replace")]
        count=sum(len(HINT_RX.findall(p.read_text(encoding="utf-8-sig",errors="replace"))) for p in hint_files)
        active_hints += count
        if count and code not in GUIDANCE:
            raise RuntimeError(f"{code} has {count} hints but no chapter-specific guidance")
        for p in hint_files:
            nchanged=enrich_file(p,GUIDANCE[code])
            if nchanged:
                changed+=nchanged
                touched.append(p.relative_to(repo).as_posix())
    print(json.dumps({
        "range":f"VI/{args.start:02d}-VI/{args.end:02d}",
        "active_hints_in_range":active_hints,
        "newly_enriched":changed,
        "touched_files":sorted(set(touched)),
    },indent=2))
    return 0

if __name__=="__main__":raise SystemExit(main())
