#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

VOLUMES = [
    ("I","vol01_linear_algebra","Linear Algebra",
     "Readers beginning a rigorous university-level mathematics sequence.",
     "High-school algebra and symbolic manipulation; no prior abstract linear algebra is assumed.",
     "Vector spaces, linear maps, matrices, canonical forms, inner products, spectral structure, quadratic forms, and singular-value decomposition."),
    ("II","vol02_real_analysis","Real Analysis and Topological Foundations",
     "Readers moving from computational calculus to proof-based analysis.",
     "Volume I-level mathematical maturity, single-variable calculus, and elementary set theory.",
     "Completeness, Euclidean and normed spaces, topology, continuity, differentiation, integration, sequences, series, and foundational real analysis."),
    ("III","vol03_fourier_distributions_pde","Measure, Fourier Analysis, Distributions and PDE",
     "Readers developing modern analytic tools for harmonic analysis and partial differential equations.",
     "Volumes I-II or equivalent linear algebra, real analysis, topology, and integration.",
     "Measure and integration, Fourier methods, distributions, weak formulations, and partial differential equations."),
    ("IV","vol04_complex_analysis","Complex Analysis and Riemann Surfaces",
     "Readers studying one-complex-variable analysis through Riemann surfaces.",
     "Volumes I-II or equivalent real analysis, multivariable calculus, and basic topology.",
     "Holomorphic functions, contour integration, residues, analytic continuation, conformal mapping, Riemann surfaces, elliptic functions, and complex tori."),
    ("V","vol05_commutative_algebra","Commutative Algebra and Homological Methods",
     "Readers preparing for algebraic geometry and homological algebra.",
     "Volume I or equivalent linear algebra; elementary group, ring, and field theory is helpful.",
     "Rings, ideals, localization, modules, Noetherian methods, dimension, exact sequences, complexes, Ext, Tor, and homological tools."),
    ("VI","vol06_algebraic_geometry","Algebraic Geometry and Sheaf Theory",
     "Readers developing scheme-theoretic algebraic geometry and sheaf methods.",
     "Volume V or equivalent commutative algebra; topology and category-theoretic language are helpful.",
     "Affine algebraic geometry, schemes, morphisms, sheaves, divisors, dimension, fiber products, base change, cohomological structures, and geometric applications."),
    ("VII","vol07_differential_geometry","Differential, Riemannian and Hyperbolic Geometry",
     "Readers studying smooth, metric, global, hyperbolic, and computational geometry.",
     "Volumes I-II or equivalent linear algebra, multivariable analysis, and topology; computational chapters also use numerical linear algebra.",
     "Smooth manifolds, bundles, forms, curves and surfaces, Riemannian and Lorentzian geometry, hyperbolic geometry, and computational geometry."),
    ("VIII","vol08_algebraic_topology","Algebraic Topology",
     "Readers developing algebraic invariants of topological spaces and bundles.",
     "Point-set topology, linear algebra, and comfort with groups and quotient constructions; Volume VII gives useful geometric motivation.",
     "Fundamental groups, coverings, homology, exact sequences, cohomology, products, bundles, Thom classes, duality, intersection theory, and Lefschetz theory."),
]

VERSION = "1.3+"
DATE = "14 September 2026"

def tex_escape(s: str) -> str:
    table = {"&":r"\&","%":r"\%","$":r"\$","#":r"\#","_":r"\_","{":r"\{","}":r"\}"}
    return "".join(table.get(c,c) for c in s)

def note(roman,title,audience,prereq,scope,author,affiliation,orcid):
    if author:
        auth = r"\textbf{Author/editor.} " + tex_escape(author)
        extras = []
        if affiliation:
            extras.append(tex_escape(affiliation))
        if orcid:
            extras.append(r"\texttt{" + tex_escape(orcid) + "}")
        if extras:
            auth += r"\\ " + r" \quad ".join(extras)
    else:
        auth = (r"\textbf{Authorship status.} Individual authorship is not asserted by the current "
                r"repository metadata. A verified author/editor name must be supplied before an "
                r"externally distributed edition claims personal authorship.")

    return rf"""\chapter*{{Publication, Scope, and Source Note}}
\phantomsection
\addcontentsline{{toc}}{{chapter}}{{Publication, Scope, and Source Note}}

\section*{{Edition}}
\textbf{{Series:}} \emph{{Theory of Mathematics}}\\
\textbf{{Volume {roman}:}} \emph{{{title}}}\\
\textbf{{Working edition:}} {VERSION}\\
\textbf{{Metadata date:}} {DATE}

{auth}

\section*{{Audience and prerequisites}}
\textbf{{Audience.}} {audience}

\textbf{{Prerequisites.}} {prereq}

\section*{{Scope}}
{scope}

\section*{{Rights and citation status}}
The repository license is the authoritative rights statement. If that license is
not yet finalized, no broader permission should be inferred from the presence of
the source files. Recommended citation metadata, release identifiers, and
archival identifiers must agree with the exact released source revision.

\section*{{Source and provenance policy}}
Reader-facing chapters present mathematics directly. Source lineage, migration
history, and editorial reconciliation belong in the repository's formal
provenance and audit records. Historical or scholarly attribution that matters
to the mathematics belongs in bibliographic notes and references.

The series policy is recorded in
\texttt{{editorial/SOURCE\_AND\_PROVENANCE\_POLICY.md}}.
"""

def update_book(path: Path, author: str):
    raw = path.read_text(encoding="utf-8-sig")
    new = re.sub(r"\\date\{\}", rf"\\date{{Version {VERSION} --- {DATE}}}", raw, count=1)
    if author:
        new = re.sub(r"\\author\{\}", r"\author{" + tex_escape(author) + "}", new, count=1)
        new = new.replace("pdfauthor={}", "pdfauthor={" + tex_escape(author) + "}")
    new = new.replace(
        "pdfsubject={Canonical reconstructed mathematics series}",
        "pdfsubject={Theory of Mathematics scholarly educational series}",
    )
    marker = r"\input{frontmatter/publication-and-scope.tex}"
    if marker not in new:
        if r"\tableofcontents" in new:
            new = new.replace(r"\tableofcontents", r"\tableofcontents" + "\n" + marker, 1)
        elif r"\frontmatter" in new:
            new = new.replace(r"\frontmatter", r"\frontmatter" + "\n" + marker, 1)
        else:
            raise RuntimeError(f"No insertion point in {path}")
    path.write_text(new, encoding="utf-8", newline="\n")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--author", default="")
    ap.add_argument("--affiliation", default="")
    ap.add_argument("--orcid", default="")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()

    for roman,d,title,audience,prereq,scope in VOLUMES:
        vdir = repo/"books"/d
        front = vdir/"frontmatter"
        front.mkdir(parents=True, exist_ok=True)
        (front/"publication-and-scope.tex").write_text(
            note(roman,title,audience,prereq,scope,a.author.strip(),a.affiliation.strip(),a.orcid.strip()),
            encoding="utf-8", newline="\n"
        )
        update_book(vdir/"book.tex", a.author.strip())

    editorial = repo/"editorial"
    editorial.mkdir(parents=True, exist_ok=True)

    author = a.author.strip() or "UNASSERTED — supply verified author/editor identity before external publication"
    aff = a.affiliation.strip() or "UNASSERTED"
    orcid = a.orcid.strip() or "UNASSERTED"

    metadata = f"""series_title: "Theory of Mathematics"
working_version: "{VERSION}"
metadata_date: "2026-09-14"
repository: "https://github.com/expert10000/math"
author: "{author}"
affiliation: "{aff}"
orcid: "{orcid}"
authorship_policy: "Never infer personal authorship from repository ownership or commit history."
rights_source: "LICENSE.md"
license_status: "Use LICENSE.md as authoritative; do not infer permissions not stated there."
citation_status: "Version-specific citation/DOI metadata is finalized only at archival release."
volumes: 8
"""
    (editorial/"PUBLICATION_METADATA.yml").write_text(metadata, encoding="utf-8", newline="\n")

    policy = """# Source and provenance policy

## Principle
Published mathematical exposition and repository source-tracking serve different purposes.

## Formal lineage
Lineage is preserved in editorial, audit, reconciliation, source-migration, and release records.

## Originality and permissions
A source record establishes lineage, not permission. Copyright/license status must be checked independently for externally sourced text, figures, problems, tables, or substantial adaptations.

## Bibliographic attribution
Historical and primary-source attribution belongs in bibliographic notes and maintained reference records, not repository-workflow prose inside exercises.

## Authorship
Personal authorship must be explicitly verified. Repository ownership or commit authorship must never be silently converted into a personal authorship claim.

## Release rule
Every external release must bind exact source revision, verified author/editor metadata, rights/license statement, bibliography/provenance policy, release version/date, and checksums/archive identifier where available.
"""
    (editorial/"SOURCE_AND_PROVENANCE_POLICY.md").write_text(policy, encoding="utf-8", newline="\n")

    gate = """# C02 publication metadata gate

C02 establishes reader-facing edition/scope notes for Volumes I–VIII and a series-level publication/provenance policy.

The gate intentionally does not invent a personal author. If verified metadata is supplied to `APPLY_C02.ps1`, it is propagated to title/PDF metadata. Otherwise the front matter explicitly records personal authorship as unasserted.
"""
    (editorial/"C02_PUBLICATION_METADATA.md").write_text(gate, encoding="utf-8", newline="\n")

    docs = repo/"docs"
    docs.mkdir(parents=True, exist_ok=True)
    pub = """# Publication and citation

The canonical scholarly series is **Theory of Mathematics**, Volumes I–VIII.

For working builds, cite the repository revision (commit SHA), volume title, and working version. Version-specific DOI/archive identifiers are added only when an archival release is deposited.

Author/editor identity must come from verified publication metadata; do not infer it from the GitHub account name.

Rights and reuse are governed by `LICENSE.md`.
Source-lineage policy is governed by `editorial/SOURCE_AND_PROVENANCE_POLICY.md`.
"""
    (docs/"PUBLICATION_AND_CITATION.md").write_text(pub, encoding="utf-8", newline="\n")

    print("C02 applied to all eight canonical volumes.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
