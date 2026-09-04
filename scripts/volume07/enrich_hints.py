#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path

GUIDANCE={'VII/01': 'Check the three manifold requirements separately: local Euclidean structure, Hausdorff separation, and second countability each '
           'rule out a different pathology.',
 'VII/02': 'Write the chart transition map explicitly and test smoothness on the overlap; compatibility is a statement about coordinates, not '
           'about the picture alone.',
 'VII/03': 'Move the map into local coordinates, differentiate there, and then check that the conclusion is independent of the chosen charts.',
 'VII/04': 'Represent tangent vectors by curve velocities or derivations and use the chart differential only as a coordinate model of the '
           'intrinsic tangent space.',
 'VII/05': 'Pair covectors with tangent vectors and track pullback by composition with the differential; duality reverses the direction of '
           'maps.',
 'VII/06': 'Use a rank or regular-value criterion for submanifolds, and use product charts to separate the factors before computing dimensions.',
 'VII/07': 'Choose a local trivialization, write transition functions on overlaps, and check the cocycle condition before making a global '
           'bundle claim.',
 'VII/08': 'Use the group action on fibers explicitly and distinguish a principal bundle from its associated vector or frame bundle.',
 'VII/09': 'Compute forms in local coordinates, use antisymmetry before expanding, and apply pullback or exterior derivative through their '
           'defining algebraic rules.',
 'VII/10': 'Track orientation through ordered bases or coordinate Jacobians, then reduce integration to positively oriented charts and a '
           'partition of unity when needed.',
 'VII/11': 'Identify the oriented boundary first, then compare the exterior derivative integral in the interior with the induced boundary '
           'integral and its sign convention.',
 'VII/12': 'Parametrize by an allowed regular parameter, compute speed and arc length, and separate geometric quantities from artifacts of '
           'reparametrization.',
 'VII/13': 'Normalize the tangent, differentiate the moving frame, and use the Frenet equations only where curvature is nonzero and the frame '
           'is defined.',
 'VII/14': 'Work in a regular surface chart or level-set description and verify rank before using tangent-plane or local-coordinate formulas.',
 'VII/15': 'Compute the first fundamental form from tangent inner products and the second from the normal derivative; keep intrinsic and '
           'extrinsic data distinct.',
 'VII/16': 'Differentiate the unit normal to obtain the shape operator, then use its eigenvectors and eigenvalues to read principal directions '
           'and curvatures.',
 'VII/17': 'Diagonalize the shape operator at the point when possible; Gaussian curvature is the product and mean curvature is the averaged '
           'trace of its principal curvatures.',
 'VII/18': 'Write the ruling explicitly and test Gaussian curvature or tangent-plane variation to distinguish ruled surfaces from developable '
           'ones.',
 'VII/19': 'Use the mean-curvature equation or first variation as the decisive condition, and check boundary or parametrization hypotheses '
           'before invoking a minimal-surface formula.',
 'VII/20': 'Write the metric tensor in local coordinates, use positive definiteness, and compute lengths or angles through the metric rather '
           'than the ambient coordinates.',
 'VII/21': 'Apply the connection rules to vector fields, then separate coordinate coefficients from the invariant covariant derivative being '
           'represented.',
 'VII/22': 'Use metric compatibility together with zero torsion to determine the Levi-Civita connection; in coordinates this becomes the '
           'Christoffel-symbol formula.',
 'VII/23': 'Write the geodesic equation from the Levi-Civita connection and distinguish affine parametrization from merely tracing the same '
           'unparametrized curve.',
 'VII/24': 'Solve the parallel-transport equation along the chosen curve and use metric compatibility to check preservation of inner products.',
 'VII/25': 'Generate holonomy by parallel transport around loops and compare the result under homotopy or curvature information rather than '
           'treating it as a local coordinate effect.',
 'VII/26': 'Use the commutator definition of curvature, then exploit tensor symmetries and a well-chosen frame before expanding components.',
 'VII/27': 'Contract the Riemann tensor in the correct indices to obtain Ricci curvature, then contract once more with the metric for scalar '
           'curvature.',
 'VII/28': 'Separate the trace-free Weyl part from the Ricci and scalar contributions, paying attention to the dimension where the Weyl tensor '
           'becomes nontrivial.',
 'VII/29': 'Track the metric signature as part of the structure and classify tangent vectors by the sign of their squared norm before using '
           'causal terminology.',
 'VII/30': 'Compare the same connection and curvature constructions under positive-definite and Lorentzian signatures, noting where causal '
           'cones replace ordinary metric spheres.',
 'VII/31': 'Choose one hyperbolic model, write its metric and geodesics explicitly, then use the standard model transformations to translate '
           'the result to another model.',
 'VII/32': 'Use the conformal factor of the Poincare metric to compute lengths and geodesics, and verify invariance under the appropriate '
           'fractional-linear transformations.',
 'VII/33': 'Represent the transformation by a real two-by-two matrix up to scalar and use its action on the boundary to classify or verify a '
           'hyperbolic isometry.',
 'VII/34': 'Classify an isometry from its fixed points and translation data, then connect the algebraic type with its geometric action on the '
           'hyperbolic plane.',
 'VII/35': 'Check discreteness through the group action and fundamental-domain geometry, then separate orbit structure from the topology of the '
           'quotient surface.',
 'VII/36': 'Use the upper-half-space or ball model in three dimensions and the complex fractional-linear action to connect boundary Mobius '
           'geometry with interior isometries.',
 'VII/37': 'Study the limit set on the ideal boundary and the discontinuity domain separately; the boundary dynamics organize the quotient '
           'geometry.',
 'VII/38': 'Translate the smooth geodesic objective into the discrete representation being used and distinguish graph shortest paths from '
           'surface geodesics.',
 'VII/39': 'For graph methods, identify the sampled edge metric; for exact mesh geodesics, track unfolding or continuous face crossings rather '
           'than restricting motion to edges.',
 'VII/40': 'Follow the heat-method pipeline in order: diffuse briefly, normalize the gradient field, then solve the Poisson equation and remove '
           'the additive constant.',
 'VII/41': 'Write the chosen discrete Laplacian and mass matrix explicitly, then check symmetry, nullspace, and consistency before interpreting '
           'eigenvalues or diffusion.',
 'VII/42': 'Compute principal curvature directions and directional derivatives, then apply the ridge or valley sign and extremum conditions '
           'along the relevant curvature line.'}
MARKER="% PEDAGOGY-ENRICHED-VII"

def read_status(repo):
    with (repo/"editorial/CHAPTER_STATUS.tsv").open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

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

def resolve_tex_target(current,target,roots):
    raw=Path(target);c=[]
    if raw.is_absolute():c.append(raw)
    else:
        c.append(current.parent/raw)
        for b in roots:c.append(Path(b)/raw)
    expanded=[]
    for q in c:
        expanded.append(q)
        if q.suffix=="":expanded.append(q.with_suffix(".tex"))
    for q in expanded:
        try:qq=q.resolve()
        except Exception:qq=q
        if qq.exists() and qq.is_file():return qq
    return None

def tex_graph(root,roots):
    root=Path(root).resolve();roots=[Path(x).resolve() for x in roots]
    seen=set();stack=[root];rx=re.compile(r"\\(?:input|include)\{([^}]+)\}")
    while stack:
        p=stack.pop()
        if p in seen or not p.exists():continue
        seen.add(p)
        t=strip_comments(p.read_text(encoding="utf-8-sig",errors="replace"))
        for target in rx.findall(t):
            q=resolve_tex_target(p,target,roots)
            if q is not None and q not in seen:stack.append(q)
    return sorted(seen,key=lambda x:x.as_posix())

def chapter_paths(repo):
    out={}
    for r in read_status(repo):
        c=(r.get("chapter_code") or "").strip()
        if c.startswith("VII/"):
            if r.get("status")!="FROZEN" or r.get("next_action")!="COMPLETE":
                raise RuntimeError(f"{c}: expected FROZEN/COMPLETE")
            out[c]=repo/r["canonical_path"]
    if len(out)!=42:raise RuntimeError(f"expected 42 Volume VII chapters, found {len(out)}")
    return out

HINT_RX=re.compile(r"\\begin\{hint\}(?P<body>.*?)\\end\{hint\}",re.S)

def enrich_file(path,suffix):
    text=path.read_text(encoding="utf-8-sig")
    counter={"ordinal":0,"changed":0}
    variants=[
        "Make the controlling geometric criterion explicit before the calculation. ",
        "Work in a convenient local model first, then return to the invariant statement. ",
        "After the main computation, check the hypotheses and geometric interpretation. ",
    ]
    def repl(m):
        counter["ordinal"]+=1
        body=m.group("body")
        if MARKER in body:return m.group(0)
        seed=body.strip()
        prefix=variants[(counter["ordinal"]-1)%3]
        new="\n"+MARKER+"\n"+seed
        if seed and seed[-1] not in ".!?":new+="."
        new+=" "+prefix+suffix+"\n"
        counter["changed"]+=1
        return "\\begin{hint}"+new+"\\end{hint}"
    out=HINT_RX.sub(repl,text)
    if out!=text:path.write_text(out.rstrip()+"\n",encoding="utf-8")
    return counter["changed"]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--start",type=int,required=True)
    ap.add_argument("--end",type=int,required=True)
    a=ap.parse_args();repo=Path(a.repo).resolve()
    cps=chapter_paths(repo);volroot=repo/"books/vol07_differential_geometry"
    total=0;changed=0;touched=[]
    for n in range(a.start,a.end+1):
        code=f"VII/{n:02d}";cp=cps[code]
        graph=tex_graph(cp,[volroot,repo])
        files=[]
        for p in graph:
            t=p.read_text(encoding="utf-8-sig",errors="replace")
            if "\\begin{hint}" in t:files.append(p)
            total+=len(HINT_RX.findall(t))
        if total and code not in GUIDANCE:raise RuntimeError(f"missing guidance for {code}")
        for p in files:
            c=enrich_file(p,GUIDANCE[code])
            if c:changed+=c;touched.append(p.relative_to(repo).as_posix())
    print(json.dumps({
        "range":f"VII/{a.start:02d}-VII/{a.end:02d}",
        "active_hints_in_range":sum(
            len(HINT_RX.findall(p.read_text(encoding="utf-8-sig",errors="replace")))
            for n in range(a.start,a.end+1)
            for p in tex_graph(cps[f"VII/{n:02d}"],[volroot,repo])
        ),
        "newly_enriched":changed,
        "touched_files":sorted(set(touched)),
    },indent=2))
    return 0

if __name__=="__main__":raise SystemExit(main())
