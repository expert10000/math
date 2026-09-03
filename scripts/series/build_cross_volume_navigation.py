#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from collections import defaultdict
from pathlib import Path

VOLUME_TITLES={
"I":"Linear Algebra",
"II":"Real Analysis and Topological Foundations",
"III":"Measure, Fourier Analysis, Distributions and PDE",
"IV":"Complex Analysis and Riemann Surfaces",
"V":"Commutative Algebra and Homological Methods",
"VI":"Algebraic Geometry and Sheaf Theory",
"VII":"Differential, Riemannian and Hyperbolic Geometry",
"VIII":"Algebraic Topology",
}

# Curated mathematical bridges. These are editorial navigation edges, not
# formal prerequisite assertions. They point readers toward the strongest
# conceptual continuations across the frozen volumes.
BRIDGES=[
("I/03","VII/04","FOUNDATION","Bases and dimension become the local linear language of tangent spaces."),
("I/05","VII/03","FOUNDATION","Linear maps provide the model for derivatives of smooth maps."),
("I/09","VII/07","FOUNDATION","Direct sums and linear algebra prepare the fiberwise algebra of vector bundles."),
("I/14","VII/08","FOUNDATION","Orthogonality and bases support frame-bundle and metric constructions."),
("II/04","VII/01","FOUNDATION","Open and closed sets supply the local topological language of manifolds."),
("II/05","VII/01","FOUNDATION","Metric-space continuity prepares the topology underlying manifolds."),
("II/08","VII/03","FOUNDATION","Several-variable differentiability is the analytic model for smooth maps."),
("II/09","VII/06","FOUNDATION","Inverse and implicit function principles drive submanifold constructions."),
("II/06","VIII/02","SEE_ALSO","Compactness interacts strongly with homotopy equivalence and global topology."),
("III/15","III/16","INTERNAL_BRIDGE","Test-function spaces feed directly into distributions; retained here to mark the analysis chain."),
("III/20","VII/40","SEE_ALSO","Weak derivatives and PDE methods connect to geometric heat methods."),
("IV/15","IV/22","INTERNAL_BRIDGE","Analytic continuation motivates Riemann surfaces."),
("IV/23","VIII/10","CONTINUATION","Covering maps and monodromy pass from complex analysis to topological covering theory."),
("IV/27","VII/07","SEE_ALSO","Complex tori are geometric examples of quotient and bundle constructions."),
("IV/31","VI/43","CONTINUATION","Elliptic curves as Riemann surfaces meet plane cubic algebraic geometry."),
("V/02","VI/06","FOUNDATION","Prime ideals become geometric points."),
("V/02","VI/07","FOUNDATION","Prime ideals organize the spectrum of a ring."),
("V/05","VI/08","FOUNDATION","Multiplicative systems underlie basic open localizations."),
("V/06","VI/08","FOUNDATION","Localization of rings gives the coordinate rings of basic opens."),
("V/08","VI/11","FOUNDATION","Localization at primes produces local rings and residue fields."),
("V/09","VI/16","FOUNDATION","Exact sequences of modules prepare exact sequences of sheaves."),
("V/10","VI/23","FOUNDATION","Tensor products underlie fiber products and base-change algebra."),
("V/11","VI/24","FOUNDATION","Module base change precedes geometric base change."),
("V/13","VII/07","CONTINUATION","Projective modules are algebraic counterparts of vector-bundle behavior."),
("V/14","VI/24","FOUNDATION","Flatness is a key exactness condition in base change."),
("V/15","VI/26","FOUNDATION","Noetherian algebra controls finite-type and Noetherian morphisms."),
("V/16","VI/21","FOUNDATION","Module support foreshadows the loci on which geometric objects live."),
("V/19","VI/27","FOUNDATION","Integral dependence feeds integral schemes and function fields."),
("V/20","VI/28","FOUNDATION","Integral closure is the algebra behind normalization."),
("V/22","VIII/16","CONTINUATION","Chain complexes reappear as the algebraic engine of homology."),
("V/23","VIII/26","SEE_ALSO","Resolutions supply the algebra behind derived coefficient constructions."),
("V/26","VIII/27","SEE_ALSO","Tor is the algebraic correction term behind Künneth phenomena."),
("V/27","VI/48","CONTINUATION","Ext and derived exactness prepare sheaf-cohomological exact sequences."),
("V/28","VI/49","CONTINUATION","Derived-functor language leads naturally toward cohomological vanishing."),
("VII/01","VIII/01","CONTINUATION","Manifolds become spaces on which homotopies of maps are studied."),
("VII/07","VIII/30","CONTINUATION","Vector bundles continue into clutching constructions."),
("VII/10","VIII/33","CONTINUATION","Orientation and integration prepare Poincaré duality."),
("VII/09","VIII/28","SEE_ALSO","Differential forms provide a geometric model for cohomological thinking."),
("VIII/16","VIII/17","INTERNAL_BRIDGE","Chain complexes feed directly into homology."),
]

VOLUME_EDGES=[
("I","II","Linear algebra supplies the finite-dimensional language used throughout analysis."),
("I","VII","Linear algebra becomes the local model for tangent, cotangent, frame, and bundle geometry."),
("II","III","Real analysis develops into measure, Fourier, distribution, and PDE methods."),
("II","VII","Multivariable analysis and topology support smooth-manifold theory."),
("IV","VIII","Coverings, monodromy, degree, and surfaces connect complex analysis to topology."),
("IV","VI","Riemann surfaces and elliptic curves meet algebraic curves and projective geometry."),
("V","VI","Commutative algebra is the principal algebraic foundation of schemes and sheaves."),
("V","VIII","Chain complexes, Tor, Ext, and derived methods connect to homological topology."),
("VII","VIII","Manifolds, bundles, orientation, and intersection phenomena feed algebraic topology."),
]

def read_tsv(path):
    with Path(path).open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def write_tsv(path,rows,fields):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader();w.writerows(rows)

def replace_section(path,heading,body):
    p=Path(path);text=p.read_text(encoding="utf-8-sig",errors="replace")
    block=heading+"\n\n"+body.rstrip()+"\n"
    rx=re.compile(r"(?ms)^"+re.escape(heading)+r"\n.*?(?=^## |\Z)")
    if rx.search(text):
        text=rx.sub(block,text)
    else:
        text=text.rstrip()+"\n\n"+block
    p.write_text(text.rstrip()+"\n",encoding="utf-8")

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve()
    status=read_tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    by_code={r["chapter_code"]:r for r in status}
    blockers=[];rows=[]
    for source,target,kind,note in BRIDGES:
        if source not in by_code:blockers.append("MISSING_SOURCE_CODE:"+source);continue
        if target not in by_code:blockers.append("MISSING_TARGET_CODE:"+target);continue
        s=by_code[source];t=by_code[target]
        rows.append({
            "source_volume":s["volume"],"source_code":source,"source_title":s["chapter_title"],
            "target_volume":t["volume"],"target_code":target,"target_title":t["chapter_title"],
            "bridge_kind":kind,"rationale":note
        })
    if len({(r["source_code"],r["target_code"]) for r in rows})!=len(rows):
        blockers.append("DUPLICATE_CHAPTER_BRIDGE")

    reports=repo/"reports/series";reports.mkdir(parents=True,exist_ok=True)
    write_tsv(reports/"CROSS_VOLUME_CHAPTER_BRIDGES.tsv",rows,[
        "source_volume","source_code","source_title","target_volume","target_code","target_title","bridge_kind","rationale"
    ])
    vedges=[]
    for a,b,note in VOLUME_EDGES:
        if a not in VOLUME_TITLES or b not in VOLUME_TITLES:
            blockers.append(f"UNKNOWN_VOLUME_EDGE:{a}->{b}");continue
        vedges.append({"source_volume":a,"source_title":VOLUME_TITLES[a],"target_volume":b,"target_title":VOLUME_TITLES[b],"rationale":note})
    write_tsv(reports/"CROSS_VOLUME_DEPENDENCY_MAP.tsv",vedges,[
        "source_volume","source_title","target_volume","target_title","rationale"
    ])

    outgoing=defaultdict(list);incoming=defaultdict(list)
    for r in rows:
        if r["source_volume"]!=r["target_volume"]:
            outgoing[r["source_volume"]].append(r)
            incoming[r["target_volume"]].append(r)

    # Per-volume sidecars.
    for v,title in VOLUME_TITLES.items():
        sr=[r for r in status if r["volume"]==v]
        if not sr:
            blockers.append("MISSING_VOLUME_STATUS:"+v);continue
        vol_dir=(repo/sr[0]["canonical_path"]).parents[2]
        lines=[
            f"# Volume {v} — Mathematical Navigation","",
            "This sidecar adds cross-volume prerequisites, continuations, and see-also links without changing the frozen theorem/chapter text.","",
            "## Comes from",""
        ]
        inc=incoming.get(v,[])
        if inc:
            for r in inc:
                lines.append(f"- **{r['source_code']} — {r['source_title']}** → **{r['target_code']} — {r['target_title']}** — {r['rationale']}")
        else:lines.append("No curated incoming cross-volume bridge.")
        lines += ["","## Leads to",""]
        out=outgoing.get(v,[])
        if out:
            for r in out:
                lines.append(f"- **{r['source_code']} — {r['source_title']}** → **{r['target_code']} — {r['target_title']}** — {r['rationale']}")
        else:lines.append("No curated outgoing cross-volume bridge.")
        lines += ["","## Reading principle","",
                  "These links are editorial navigation, not formal logical dependencies. They identify especially useful conceptual transitions in the frozen 256-chapter series.",""]
        (vol_dir/"MATHEMATICAL_NAVIGATION.md").write_text("\n".join(lines),encoding="utf-8")
        replace_section(
            vol_dir/"LANDING.md",
            "## Mathematical navigation",
            "See `MATHEMATICAL_NAVIGATION.md` for curated prerequisites, continuations, and cross-volume bridges."
        )

    nav=[
        "# Theory of Mathematics I–VIII — Mathematical Navigation","",
        "This map supplements the canonical chapter/status navigation with mathematical dependencies and continuations.",
        "It does not alter the frozen chapter texts.","",
        "## Volume-level dependency map",""
    ]
    for r in vedges:
        nav.append(f"- **{r['source_volume']} — {r['source_title']}** → **{r['target_volume']} — {r['target_title']}**: {r['rationale']}")
    nav += ["","## Curated chapter bridges",""]
    for r in rows:
        if r["source_volume"]==r["target_volume"]: continue
        nav.append(
            f"- `{r['source_code']}` **{r['source_title']}** → `{r['target_code']}` **{r['target_title']}** "
            f"({r['bridge_kind']}): {r['rationale']}"
        )
    nav += ["","## Use","",
            "Start from a chapter you know, follow `FOUNDATION` edges backward for prerequisites, and `CONTINUATION` or `SEE_ALSO` edges forward for the next natural subject.",""]
    (repo/"books/CROSS_VOLUME_MATHEMATICAL_NAVIGATION.md").write_text("\n".join(nav),encoding="utf-8")
    replace_section(
        repo/"books/SERIES_NAVIGATION.md",
        "## Mathematical dependency map",
        "See `CROSS_VOLUME_MATHEMATICAL_NAVIGATION.md` and `../reports/series/CROSS_VOLUME_CHAPTER_BRIDGES.tsv` for curated mathematical prerequisites and continuations."
    )

    summary={
        "status":"PASS" if not blockers else "FAIL",
        "volume_edges":len(vedges),"chapter_bridges":len(rows),
        "cross_volume_chapter_bridges":sum(r["source_volume"]!=r["target_volume"] for r in rows),
        "volume_navigation_sidecars":len(VOLUME_TITLES),
        "blocking":blockers
    }
    (reports/"CROSS_VOLUME_NAVIGATION_SUMMARY.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blockers else 3

if __name__=="__main__":
    raise SystemExit(main())
