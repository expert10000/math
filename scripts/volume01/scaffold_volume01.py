#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path

CHAPTERS=[('I/01', 'Scalars, Vectors and Linear Combinations', 'ch01_scalars_vectors_and_linear_combinations'), ('I/02', 'Subspaces, Span and Linear Independence', 'ch02_subspaces_span_and_linear_independence'), ('I/03', 'Bases and Dimension', 'ch03_bases_and_dimension'), ('I/04', 'Coordinates and Change of Basis', 'ch04_coordinates_and_change_of_basis'), ('I/05', 'Linear Transformations', 'ch05_linear_transformations'), ('I/06', 'Kernels, Images and Isomorphisms', 'ch06_kernels_images_and_isomorphisms'), ('I/07', 'Matrix Representation of Linear Maps', 'ch07_matrix_representation_of_linear_maps'), ('I/08', 'Determinants and Trace', 'ch08_determinants_and_trace'), ('I/09', 'Eigenvalues and Eigenvectors', 'ch09_eigenvalues_and_eigenvectors'), ('I/10', 'Invariant Subspaces and Triangularization', 'ch10_invariant_subspaces_and_triangularization'), ('I/11', 'Diagonalization and Minimal Polynomials', 'ch11_diagonalization_and_minimal_polynomials'), ('I/12', 'Canonical Forms', 'ch12_canonical_forms'), ('I/13', 'Inner Products and Orthogonality', 'ch13_inner_products_and_orthogonality'), ('I/14', 'Gram–Schmidt and Orthogonal Projection', 'ch14_gram_schmidt_and_orthogonal_projection'), ('I/15', 'Orthogonal and Unitary Operators', 'ch15_orthogonal_and_unitary_operators'), ('I/16', 'The Spectral Theorem', 'ch16_the_spectral_theorem'), ('I/17', 'Quadratic Forms', 'ch17_quadratic_forms'), ('I/18', 'Singular-Value Decomposition', 'ch18_singular_value_decomposition')]
FIELDS=["volume","chapter_code","chapter_title","status","legacy_source_status","mapped_rule_count","canonical_path","next_action"]

def read_tsv(p):
    with p.open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))

def write_tsv(p,rows,fields):
    lines=["\t".join(fields)]
    for r in rows:
        lines.append("\t".join(str(r.get(k,"-") or "-") for k in fields))
    p.write_text("\n".join(lines)+"\n",encoding="utf-8")

def write_status(p,rows):
    lines=["\t".join(FIELDS)]
    for r in rows:lines.append("\t".join(str(r.get(k,"")) for k in FIELDS))
    p.write_text("\n".join(lines)+"\n",encoding="utf-8")

def source_exists(repo,name):
    for p in (repo/name,repo/"chapters/tex"/name):
        if p.exists():return p
    return None

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol01_linear_algebra"
    (vol/"chapters").mkdir(parents=True,exist_ok=True)
    parts=[
      ("Vector Spaces",CHAPTERS[:6]),
      ("Matrices and Operators",CHAPTERS[6:12]),
      ("Euclidean and Hilbert-Space Geometry",CHAPTERS[12:])
    ]
    book=[
      r"\documentclass[11pt,a4paper,oneside,openany]{book}",
      r"\input{../../shared/preamble.tex}",
      r"\input{../../shared/macros.tex}",
      r"\input{../../shared/theorem_styles.tex}",
      r"\input{../../shared/notation.tex}",
      "",
      r"\title{Theory of Mathematics\\[0.5em]\Large Volume I: Linear Algebra}",
      r"\author{}",
      r"\date{}",
      r"\hypersetup{pdftitle={Theory of Mathematics — Volume I: Linear Algebra},pdfsubject={Canonical reconstructed mathematics series}}",
      r"\begin{document}",
      r"\pagenumbering{gobble}",
      r"\maketitle",
      r"\clearpage",
      r"\frontmatter",
      r"\tableofcontents",
      r"\mainmatter"
    ]
    for part,items in parts:
        book += ["",f"\\part{{{part}}}"]
        for code,title,slug in items:
            book.append(f"\\include{{chapters/{slug}/chapter}}")
    book += ["",r"\backmatter",r"\end{document}",""]
    (vol/"book.tex").write_text("\n".join(book),encoding="utf-8")

    # Buildable, explicit reconstruction stubs; later batch commits replace them.
    for code,title,slug in CHAPTERS:
        p=vol/"chapters"/slug/"chapter.tex"
        p.parent.mkdir(parents=True,exist_ok=True)
        n=int(code.split("/")[1])
        p.write_text(
          f"\\chapter{{{title}}}\n"
          f"\\label{{ch:i{n:02d}-scaffold}}\n\n"
          "\\section*{Reconstruction scaffold}\n"
          "This canonical chapter path is reserved and buildable. "
          "The staged reconstruction commits replace this scaffold with audited mathematical content.\n",
          encoding="utf-8"
        )

    status_path=repo/"editorial/CHAPTER_STATUS.tsv";rows=read_tsv(status_path)
    src=read_tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    routed=[r for r in src if re.fullmatch(r"I/\d{2}",r.get("destination",""))]
    bydest={}
    for r in routed:bydest.setdefault(r["destination"],[]).append(r)

    inv=[]
    for r in routed:
        p=source_exists(repo,r.get("source_file",""))
        inv.append({
          "chapter_code":r.get("destination",""),
          "source_file":r.get("source_file",""),
          "source_block_id":r.get("source_block_id",""),
          "block_kind":r.get("block_kind",""),
          "source_selector":r.get("source_selector",""),
          "source_title_or_pattern":r.get("source_title_or_pattern",""),
          "action":r.get("action",""),
          "precedence":r.get("precedence",""),
          "audit_status":r.get("audit_status",""),
          "source_exists":"YES" if p else "NO"
        })
    audit=vol/"reconstruction";audit.mkdir(exist_ok=True)
    write_tsv(audit/"VOLUME01_SOURCE_INVENTORY.tsv",inv,[
      "chapter_code","source_file","source_block_id","block_kind","source_selector",
      "source_title_or_pattern","action","precedence","audit_status","source_exists"
    ])
    summary=[]
    for code,title,slug in CHAPTERS:
        rules=bydest.get(code,[])
        summary.append({
          "chapter_code":code,"chapter_title":title,"mapped_rules":len(rules),
          "source_files":len(set(r.get("source_file","") for r in rules)),
          "missing_sources":sum(1 for r in rules if not source_exists(repo,r.get("source_file",""))),
          "canonical_path":f"books/vol01_linear_algebra/chapters/{slug}/chapter.tex"
        })
    write_tsv(audit/"VOLUME01_SOURCE_SUMMARY.tsv",summary,[
      "chapter_code","chapter_title","mapped_rules","source_files","missing_sources","canonical_path"
    ])

    for r in rows:
        if r.get("volume")=="I":
            code=r["chapter_code"];title,slug=next((t,s) for c,t,s in CHAPTERS if c==code)
            r["canonical_path"]=f"books/vol01_linear_algebra/chapters/{slug}/chapter.tex"
            r["mapped_rule_count"]=str(len(bydest.get(code,[])))
            r["next_action"]="RECONSTRUCT_CANONICAL_CHAPTER"
    write_status(status_path,rows)

    readme=vol/"README.md"
    text=readme.read_text(encoding="utf-8-sig")
    text=re.sub(r"(?m)^\*\*Status:\*\*.*$","**Status:** Canonical build scaffold active; I/01–I/18 staged reconstruction underway.",text,count=1)
    readme.write_text(text.rstrip()+"\n",encoding="utf-8")
    print(f"Volume I scaffold: 18 active chapters, {len(routed)} routed source rules")
    return 0
if __name__=="__main__":raise SystemExit(main())
