#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ATLAS_FIELDS = [
    "companion_problem_id","semantic_unit_id","representative_problem_id","companion_part",
    "thematic_section","related_volume","related_chapters","related_sections","source_files",
    "source_problem_ids","has_solution","problem_type","difficulty","figure_requirement",
    "figure_type","figure_status","migration_status","editorial_status","notes"
]

REVIEW_FIELDS = [
    "semantic_unit_id","representative_problem_id","suggested_volume","suggested_thematic_section",
    "related_chapters","confidence","score_margin","source_files","problem_type",
    "classification_basis","review_reason"
]

SUMMARY_ORDER = ["I","II","III","IV","V","VI","VII","VIII"]

@dataclass(frozen=True)
class Theme:
    name: str
    chapters: str
    terms: tuple[tuple[str, int], ...]

@dataclass(frozen=True)
class VolumeProfile:
    roman: str
    part: str
    title: str
    file_hints: tuple[tuple[str, int], ...]
    terms: tuple[tuple[str, int], ...]
    themes: tuple[Theme, ...]

def t(*pairs: tuple[str, int]) -> tuple[tuple[str, int], ...]:
    return tuple(pairs)

PROFILES = (
    VolumeProfile(
        "I","01","Linear Algebra",
        t(("linear-algebra",18),("linear_algebra",18),("matrix",4)),
        t(("vector space",8),("linear map",8),("linear transformation",8),("basis",5),("dimension",4),
          ("matrix",5),("determinant",7),("trace",5),("eigenvalue",8),("eigenvector",8),
          ("minimal polynomial",9),("jordan",9),("inner product",8),("orthogonal",7),
          ("unitary",7),("spectral theorem",10),("quadratic form",8),("singular value",10)),
        (
            Theme("Vector Spaces","I/01--I/06",
                  t(("vector space",8),("linear combination",7),("subspace",7),("span",6),
                    ("linear independence",8),("basis",7),("dimension",6),("linear map",5),
                    ("kernel",6),("image",5),("isomorphism",5))),
            Theme("Matrices and Operators","I/07--I/12",
                  t(("matrix",8),("determinant",9),("trace",7),("eigenvalue",9),("eigenvector",9),
                    ("invariant subspace",8),("triangular",8),("diagonal",8),("minimal polynomial",9),
                    ("jordan",9),("canonical form",8))),
            Theme("Euclidean and Hilbert-Space Geometry","I/13--I/18",
                  t(("inner product",9),("orthogonal",9),("gram-schmidt",10),("projection",7),
                    ("unitary",8),("spectral theorem",10),("quadratic form",9),("singular value",10),
                    ("svd",10))),
        ),
    ),
    VolumeProfile(
        "II","02","Real Analysis and Topological Foundations",
        t(("theory-of-analysis",14),("real-analysis",16),("analysis-functions",12),("analysis-topology",12)),
        t(("real number",6),("metric space",8),("open set",4),("closed set",4),("compact",7),
          ("connected",6),("continuity",5),("differentiable",6),("derivative",4),("riemann integral",8),
          ("uniform convergence",9),("fixed point",8),("ordinary differential",8),("interpolation",8),
          ("chebyshev",9),("continued fraction",9)),
        (
            Theme("Metric and Topological Foundations","II/01--II/07",
                  t(("complete",5),("cauchy sequence",8),("metric space",9),("normed space",8),
                    ("open set",6),("closed set",6),("compact",8),("connected",8),("topological space",8))),
            Theme("Calculus","II/08--II/10",
                  t(("differentiable",8),("derivative",6),("jacobian",8),("inverse function",10),
                    ("implicit function",10),("riemann integral",9))),
            Theme("Sequences of Functions","II/11--II/15",
                  t(("pointwise convergence",9),("uniform convergence",10),("series of functions",9),
                    ("trigonometric series",8),("nowhere differentiable",10))),
            Theme("Fixed Points and Differential Equations","II/16--II/19",
                  t(("contraction",9),("fixed point",10),("brouwer",10),("integral equation",9),
                    ("ordinary differential",10),("ode",7),("existence theorem",5))),
            Theme("Approximation","II/20--II/25",
                  t(("interpolation",10),("polynomial approximation",10),("chebyshev",10),
                    ("minimax",10),("alternation",9),("quadrature",9),("continued fraction",10))),
        ),
    ),
    VolumeProfile(
        "III","03","Measure, Fourier Analysis, Distributions and PDE",
        t(("fourier",14),("distribution",12),("pde",14),("measure",10),("sobolev",14)),
        t(("sigma-algebra",9),("measure",7),("measurable",8),("lebesgue",10),("fubini",9),
          ("holder",6),("minkowski",7),("fourier",10),("convolution",8),("schwartz",9),
          ("distribution",9),("tempered",9),("weak derivative",10),("sobolev",10),
          ("green function",9),("fundamental solution",8),("elliptic",8),("sturm-liouville",9),
          ("laplace equation",8),("heat equation",8),("wave equation",8)),
        (
            Theme("Measure and Integration","III/01--III/08",
                  t(("sigma-algebra",10),("measure",9),("measurable",9),("lebesgue",10),("fubini",10),
                    ("lp ",6),("l^p",7),("holder",7),("minkowski",8),("egorov",10),("vitali",10))),
            Theme("Fourier Analysis","III/09--III/14",
                  t(("fourier series",10),("convolution",9),("approximate identity",9),
                    ("fourier transform",10),("gaussian",5),("plancherel",10),("schwartz",9))),
            Theme("Distribution Theory","III/15--III/19",
                  t(("test function",9),("distribution",10),("distributional derivative",10),
                    ("delta distribution",9),("tempered distribution",10))),
            Theme("Sobolev and PDE Methods","III/20--III/28",
                  t(("weak derivative",10),("sobolev",10),("boundary-value",8),("boundary value",8),
                    ("fundamental solution",9),("green function",10),("sturm-liouville",10),
                    ("elliptic",10),("maximum principle",9),("pde",8),("helmholtz",9))),
        ),
    ),
    VolumeProfile(
        "IV","04","Complex Analysis and Riemann Surfaces",
        t(("complex-analysis",18),("complex_analysis",18),("riemann-surface",16),("elliptic-function",16)),
        t(("holomorphic",10),("cauchy-riemann",10),("complex integral",8),("contour",7),
          ("laurent",10),("residue",10),("rouche",10),("argument principle",9),("conformal",9),
          ("mobius",8),("analytic continuation",9),("riemann surface",10),("monodromy",8),
          ("gamma function",8),("elliptic function",10),("weierstrass",9)),
        (
            Theme("Holomorphic Functions","IV/01--IV/06",
                  t(("holomorphic",10),("cauchy-riemann",10),("power series",7),("complex integration",9),
                    ("cauchy theorem",10),("cauchy integral",10))),
            Theme("Singularities and Residues","IV/07--IV/11",
                  t(("zero",3),("identity theorem",9),("laurent",10),("singularity",9),
                    ("residue",10),("real integral",5))),
            Theme("Global Complex Analysis","IV/12--IV/18",
                  t(("winding number",9),("argument principle",10),("rouche",10),("branch",5),
                    ("logarithm",4),("analytic continuation",10),("mobius",10),("conformal",10),
                    ("schwarz-christoffel",10))),
            Theme("Special Functions","IV/19--IV/21",
                  t(("gamma function",10),("beta function",10),("keyhole",10),("branch cut",8))),
            Theme("Riemann Surfaces","IV/22--IV/26",
                  t(("riemann surface",10),("covering map",7),("monodromy",10),("branched covering",10),
                    ("gluing",6),("genus",6))),
            Theme("Elliptic Functions","IV/27--IV/31",
                  t(("lattice",5),("complex torus",10),("elliptic function",10),("weierstrass",10),
                    ("addition formula",7),("elliptic curve",8))),
        ),
    ),
    VolumeProfile(
        "V","05","Commutative Algebra and Homological Methods",
        t(("commutative-algebra",20),("commutative_algebra",20),("homological-algebra",12)),
        t(("commutative ring",8),("ideal",4),("prime ideal",7),("maximal ideal",7),("radical",6),
          ("localization",9),("module",5),("tensor product",8),("noetherian",9),("associated prime",9),
          ("integral dependence",9),("integral closure",8),("valuation ring",9),("free resolution",10),
          ("syzygy",10),("tor ",8),("ext ",8),("projective module",8),("flat module",8)),
        (
            Theme("Rings and Ideals","V/01--V/04",
                  t(("ring",5),("ideal",8),("quotient ring",8),("prime ideal",9),("maximal ideal",9),
                    ("radical",8),("nilpotent",8),("chinese remainder",10))),
            Theme("Localization","V/05--V/08",
                  t(("multiplicative system",10),("localization",10),("local ring",9),("localize",9))),
            Theme("Modules and Tensor Products","V/09--V/14",
                  t(("module",7),("exact sequence",5),("tensor product",10),("base change",5),
                    ("hom ",5),("finitely presented",9),("projective module",9),("flat module",9))),
            Theme("Noetherian Algebra","V/15--V/18",
                  t(("noetherian",10),("support",6),("associated prime",10),("completion",8),("adic",8))),
            Theme("Integral and Valuation Theory","V/19--V/21",
                  t(("integral dependence",10),("integral closure",10),("normalization",7),
                    ("valuation ring",10),("valuation",8))),
            Theme("Homological Algebra","V/22--V/28",
                  t(("chain complex",7),("free resolution",10),("resolution",8),("syzygy",10),
                    ("minimal resolution",10),("tor ",10),("ext ",10),("derived functor",10))),
        ),
    ),
    VolumeProfile(
        "VI","06","Algebraic Geometry and Sheaf Theory",
        t(("algebraic-geometry",22),("algebraic_geometry",22),("scheme",8),("sheaf",7)),
        t(("algebraic set",10),("zariski",10),("coordinate ring",9),("spec",8),("spectrum of",8),
          ("scheme",10),("sheaf",9),("stalk",8),("structure sheaf",10),("fiber product",9),
          ("base change",7),("geometric fiber",9),("krull dimension",9),("tangent space",5),
          ("proj",9),("projective space",7),("divisor",9),("picard",9),("blow-up",10),("blowup",10),
          ("cech cohomology",9)),
        (
            Theme("Classical Affine Geometry","VI/01--VI/05",
                  t(("algebraic set",10),("zariski",8),("coordinate ring",10),("affine algebraic",9),
                    ("irreducible",5),("component",4))),
            Theme("Prime Spectra","VI/06--VI/11",
                  t(("prime ideal",6),("spectrum",9),("spec",9),("basic open",9),("generic point",9),
                    ("closed point",8),("nonreduced",9),("residue field",8),("local ring",6))),
            Theme("Sheaves","VI/12--VI/17",
                  t(("presheaf",10),("sheafification",10),("sheaf",9),("stalk",9),
                    ("exact sequence of sheaves",10),("structure sheaf",10))),
            Theme("Affine and General Schemes","VI/18--VI/22",
                  t(("affine scheme",10),("morphism of affine schemes",10),("scheme",8),
                    ("gluing affine",10),("open subscheme",9),("closed subscheme",9))),
            Theme("Morphisms and Families","VI/23--VI/28",
                  t(("fiber product",10),("base change",9),("geometric fiber",10),("fiber",6),
                    ("finite type",9),("function field",8),("normalization",8))),
            Theme("Dimension","VI/29--VI/32",
                  t(("krull dimension",10),("dimension of",7),("codimension",10),("tangent space",9),
                    ("local geometry",8))),
            Theme("Modules and Projective Geometry","VI/33--VI/38",
                  t(("quasi-coherent",10),("graded ring",9),("proj",10),("projective space",9),
                    ("projective scheme",10),("closed embedding",8))),
            Theme("Divisors and Birational Geometry","VI/39--VI/45",
                  t(("weil divisor",10),("cartier divisor",10),("divisor",8),("class group",9),
                    ("line bundle",7),("picard",10),("plane cubic",9),("cremona",10),("blow-up",10),
                    ("blowup",10))),
            Theme("Sheaf Cohomology","VI/46--VI/49",
                  t(("flabby",10),("cech",10),("sheaf cohomology",10),("cohomology of sheaves",10),
                    ("vanishing",5))),
        ),
    ),
    VolumeProfile(
        "VII","07","Differential, Riemannian and Hyperbolic Geometry",
        t(("differential-geometry",22),("differential_geometry",22),("theory-of-geometry",11)),
        t(("smooth manifold",10),("tangent space",7),("cotangent",9),("differential form",9),
          ("stokes",8),("regular curve",8),("curvature",6),("torsion",7),("regular surface",8),
          ("gauss map",9),("shape operator",9),("riemannian",10),("levi-civita",10),("geodesic",9),
          ("parallel transport",9),("ricci",9),("weyl curvature",9),("lorentzian",10),
          ("hyperbolic plane",10),("poincare metric",9),("fuchsian",10),("kleinian",10),
          ("mesh geodesic",10),("discrete laplacian",10),("heat method",10)),
        (
            Theme("Smooth Manifolds","VII/01--VII/06",
                  t(("topological manifold",8),("smooth manifold",10),("smooth structure",10),
                    ("atlas",6),("diffeomorphism",8),("tangent space",8),("cotangent",8),("submanifold",8))),
            Theme("Bundles and Forms","VII/07--VII/11",
                  t(("vector bundle",7),("principal bundle",9),("frame bundle",9),("differential form",10),
                    ("orientation",7),("stokes",10))),
            Theme("Curves and Surfaces","VII/12--VII/19",
                  t(("regular curve",10),("frenet",10),("curvature",7),("torsion",9),("regular surface",10),
                    ("fundamental form",10),("gauss map",10),("shape operator",10),("minimal surface",10),
                    ("ruled surface",9),("developable",9))),
            Theme("Riemannian Geometry","VII/20--VII/28",
                  t(("riemannian",10),("connection",6),("levi-civita",10),("geodesic",9),
                    ("parallel transport",10),("holonomy",9),("riemann curvature",10),("ricci",10),
                    ("scalar curvature",9),("weyl",9))),
            Theme("Lorentzian Geometry","VII/29--VII/30",
                  t(("lorentzian",10),("indefinite metric",10),("timelike",8),("spacelike",8))),
            Theme("Hyperbolic Geometry","VII/31--VII/37",
                  t(("hyperbolic",10),("poincare",8),("psl(2",8),("fuchsian",10),("kleinian",10),
                    ("hyperbolic three",10))),
            Theme("Computational Geometry","VII/38--VII/42",
                  t(("mesh",8),("discrete geodesic",10),("graph geodesic",10),("heat method",10),
                    ("discrete laplacian",10),("ridge",8),("valley",8))),
        ),
    ),
    VolumeProfile(
        "VIII","08","Algebraic Topology",
        t(("algebraic-topology",22),("algebraic_topology",22),("topology-",8)),
        t(("homotopy",10),("cw complex",10),("fundamental group",10),("covering space",9),
          ("deck transformation",9),("simplicial",8),("singular homology",10),("cellular homology",10),
          ("relative homology",9),("chain homotopy",9),("universal coefficient",10),("kunneth",10),
          ("cohomology",8),("cup product",10),("clutching",10),("thom class",10),("euler class",9),
          ("poincare duality",10),("intersection form",9),("lefschetz",10)),
        (
            Theme("Homotopy","VIII/01--VIII/04",
                  t(("homotopy",10),("homotopy equivalence",10),("contractible",9),("degree of",8),
                    ("antipodal",9))),
            Theme("CW Complexes","VIII/05--VIII/08",
                  t(("cell attachment",10),("cw complex",10),("mapping cone",9),("attaching map",9))),
            Theme("Fundamental Groups and Coverings","VIII/09--VIII/14",
                  t(("fundamental group",10),("covering space",10),("lifting",8),("deck transformation",10),
                    ("group action",7),("su(2)",8),("so(3)",8),("free group",8),("covering graph",9))),
            Theme("Homology","VIII/15--VIII/21",
                  t(("simplicial complex",9),("chain complex",6),("singular homology",10),
                    ("cellular homology",10),("relative homology",10),("euler characteristic",10))),
            Theme("Homological Machinery","VIII/22--VIII/27",
                  t(("chain homotopy",10),("chain contraction",10),("mapping cone of chain",10),
                    ("homology with coefficients",10),("universal coefficient",10),("kunneth",10))),
            Theme("Cohomology, Bundles and Manifolds","VIII/28--VIII/35",
                  t(("cohomology",9),("cup product",10),("clutching",10),("thom class",10),
                    ("euler class",10),("poincare duality",10),("intersection form",10),("lefschetz",10))),
        ),
    ),
)

PROFILE_BY_ROMAN = {p.roman: p for p in PROFILES}

def read_tsv(path: Path) -> tuple[list[str], list[dict[str,str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        return list(r.fieldnames or []), [dict(x) for x in r]

def write_tsv(path: Path, fields: list[str], rows: Iterable[dict[str,object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})

def safe_read(path: Path) -> str:
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            pass
    return path.read_text(encoding="utf-8", errors="replace")

def parse_range(value: str) -> tuple[int,int] | None:
    m = re.fullmatch(r"L?(\d+)-L?(\d+)", (value or "").strip())
    if not m:
        return None
    a,b = int(m.group(1)), int(m.group(2))
    return (a,b) if a <= b else (b,a)

def extract_statement_text(source_root: Path, ledger_row: dict[str,str]) -> str:
    rel = ledger_row.get("source_file","")
    line_range = parse_range(ledger_row.get("source_line_range",""))
    if not rel or not line_range:
        return ""
    path = source_root / Path(rel)
    if not path.exists():
        return ""
    lines = safe_read(path).splitlines()
    a,b = line_range
    if a < 1 or a > len(lines):
        return ""
    b = min(b, len(lines))
    text = "\n".join(lines[a-1:b])
    # Classification needs the statement and its immediate mathematical vocabulary,
    # but long embedded solutions can dominate keyword counts. Cap the sample.
    return text[:12000]

def norm_text(s: str) -> str:
    s = s.lower()
    replacements = {
        "\\\\": " ",
        "{": " ", "}": " ", "$": " ", "_": " ", "^": " ",
        "–": "-", "—": "-", "é": "e", "ö": "o", "ü": "u",
        "č": "c", "ć": "c", "š": "s",
    }
    for a,b in replacements.items():
        s = s.replace(a,b)
    s = re.sub(r"\s+", " ", s)
    return s

def score_terms(text: str, terms: tuple[tuple[str,int],...]) -> tuple[int,list[str]]:
    total = 0
    hits: list[str] = []
    for term, weight in terms:
        n = text.count(term)
        if n:
            # Repeated occurrences help, but cap each term so a long solution cannot dominate.
            total += weight * min(n, 3)
            hits.append(term)
    return total, hits

def classify_volume(source_files: str, statement: str) -> tuple[VolumeProfile,int,int,str]:
    src = norm_text(source_files)
    txt = norm_text(statement)
    scored = []
    for p in PROFILES:
        fs, fh = score_terms(src, p.file_hints)
        ts, th = score_terms(txt, p.terms)
        # Source-family identity is valuable provenance evidence but mathematical text
        # remains the dominant signal for generic or cross-disciplinary filenames.
        score = fs + ts
        scored.append((score,p,fh,th))
    scored.sort(key=lambda x: (x[0], x[1].roman), reverse=True)
    best = scored[0]
    second = scored[1]
    basis_parts = []
    if best[2]:
        basis_parts.append("source:" + ",".join(best[2][:4]))
    if best[3]:
        basis_parts.append("text:" + ",".join(best[3][:8]))
    return best[1], best[0], second[0], "; ".join(basis_parts) or "weak lexical evidence"

def classify_theme(profile: VolumeProfile, statement: str, source_files: str) -> tuple[Theme,int,int,str]:
    txt = norm_text(statement + " " + source_files)
    scored = []
    for theme in profile.themes:
        score, hits = score_terms(txt, theme.terms)
        scored.append((score,theme,hits))
    scored.sort(key=lambda x: (x[0], x[1].name), reverse=True)
    best = scored[0]
    second_score = scored[1][0] if len(scored) > 1 else 0
    basis = "theme:" + ",".join(best[2][:8]) if best[2] else "theme:fallback-to-volume-region"
    return best[1], best[0], second_score, basis

def confidence(best: int, second: int, source_files: str, profile: VolumeProfile, theme_score: int) -> tuple[str,str]:
    margin = best - second
    src = norm_text(source_files)
    strong_file = any(h in src and w >= 14 for h,w in profile.file_hints)
    if best >= 18 and margin >= 8 and (strong_file or theme_score >= 8):
        return "HIGH", str(margin)
    if best >= 10 and margin >= 4:
        return "MEDIUM", str(margin)
    return "LOW", str(margin)

def figure_hint(statement: str, has_figures: str) -> tuple[str,str,str]:
    txt = norm_text(statement)
    if (has_figures or "").upper() == "YES":
        return "YES","SOURCE_FIGURE","SOURCE_PRESENT_REVIEW_LATER"
    if any(x in txt for x in (
        "plot ","graph of","sketch ","draw ","diagram","curve ","surface ","contour",
        "geodesic","mobius","riemann surface","algebraic set","scheme","covering space",
        "cw complex","vector field","phase portrait","fundamental domain"
    )):
        return "CANDIDATE","TO_BE_DETERMINED","PENDING_VISUAL_AUDIT"
    return "NO","","PENDING_VISUAL_AUDIT"

def main() -> int:
    ap = argparse.ArgumentParser(description="Build the Companion semantic problem placement atlas.")
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    args = ap.parse_args()
    repo = args.repo.resolve()
    inv = repo / "imports" / "problem_inventory"
    base = repo / "books" / "companion_problems_solutions"
    source_root = repo / "imports" / "ALL_TEX_AND_FIGURES" / "tex"

    sem_path = inv / "SEMANTIC_PROBLEM_UNITS.tsv"
    ledger_path = inv / "PROBLEM_LEDGER.tsv"
    atlas_path = base / "metadata" / "COMPANION_PROBLEM_ATLAS.tsv"
    review_path = base / "metadata" / "COMPANION_PLACEMENT_REVIEW.tsv"
    summary_path = base / "metadata" / "COMPANION_ATLAS_SUMMARY.md"

    for p in (sem_path, ledger_path, atlas_path):
        if not p.exists():
            print(f"ERROR: missing required file: {p}")
            return 2
    if not source_root.exists():
        print(f"ERROR: missing source corpus: {source_root}")
        return 2

    _, sem_rows = read_tsv(sem_path)
    _, ledger = read_tsv(ledger_path)
    ledger_by_id = {r.get("problem_id",""): r for r in ledger}

    if not sem_rows:
        print("ERROR: SEMANTIC_PROBLEM_UNITS.tsv is empty")
        return 2

    classified = []
    review = []
    prelim = []

    for sem in sem_rows:
        sid = sem.get("semantic_problem_id") or sem.get("semantic_unit_id") or ""
        rep = sem.get("representative_problem_id","")
        lr = ledger_by_id.get(rep, {})
        statement = extract_statement_text(source_root, lr)
        source_files = sem.get("source_files","") or lr.get("source_file","")
        profile, best, second, basis = classify_volume(source_files, statement)
        theme, tbest, tsecond, tbasis = classify_theme(profile, statement, source_files)
        conf, margin = confidence(best, second, source_files, profile, tbest)
        fig_req, fig_type, fig_status = figure_hint(statement, lr.get("has_figures",""))
        problem_type = sem.get("problem_types","") or lr.get("problem_type","")
        has_solution = sem.get("solution_availability","") or lr.get("has_solution","")
        source_problem_ids = sem.get("member_problem_ids","") or rep

        prelim.append({
            "semantic_unit_id": sid,
            "representative_problem_id": rep,
            "profile": profile,
            "theme": theme,
            "confidence": conf,
            "margin": margin,
            "source_files": source_files,
            "source_problem_ids": source_problem_ids,
            "has_solution": has_solution,
            "problem_type": problem_type,
            "figure_requirement": fig_req,
            "figure_type": fig_type,
            "figure_status": fig_status,
            "basis": basis + ("; " + tbasis if tbasis else ""),
            "statement_missing": not bool(statement.strip()),
            "volume_score": best,
            "second_score": second,
            "theme_score": tbest,
        })

    # Stable IDs inside each Part: frozen semantic corpus + sorted semantic IDs.
    grouped: dict[str,list[dict]] = defaultdict(list)
    for x in prelim:
        grouped[x["profile"].roman].append(x)
    for roman in grouped:
        grouped[roman].sort(key=lambda x: x["semantic_unit_id"])

    id_by_sid = {}
    for roman in SUMMARY_ORDER:
        for idx, x in enumerate(grouped.get(roman, []), 1):
            id_by_sid[x["semantic_unit_id"]] = f"CP-{roman}-{idx:04d}"

    for x in sorted(prelim, key=lambda z: (SUMMARY_ORDER.index(z["profile"].roman), z["semantic_unit_id"])):
        p = x["profile"]
        th = x["theme"]
        editorial = "READY_FOR_COMPANION_MIGRATION"
        reasons = []
        if x["confidence"] == "LOW":
            editorial = "PLACEMENT_REVIEW_REQUIRED"
            reasons.append("low volume-classification confidence")
        if x["statement_missing"]:
            editorial = "PLACEMENT_REVIEW_REQUIRED"
            reasons.append("representative statement text unavailable")
        if x["theme_score"] == 0:
            if editorial == "READY_FOR_COMPANION_MIGRATION":
                editorial = "PLACEMENT_REVIEW_REQUIRED"
            reasons.append("thematic section chosen only from broad volume fallback")

        row = {
            "companion_problem_id": id_by_sid[x["semantic_unit_id"]],
            "semantic_unit_id": x["semantic_unit_id"],
            "representative_problem_id": x["representative_problem_id"],
            "companion_part": p.part,
            "thematic_section": th.name,
            "related_volume": p.roman,
            "related_chapters": th.chapters,
            "related_sections": "",
            "source_files": x["source_files"],
            "source_problem_ids": x["source_problem_ids"],
            "has_solution": x["has_solution"],
            "problem_type": x["problem_type"],
            "difficulty": "",
            "figure_requirement": x["figure_requirement"],
            "figure_type": x["figure_type"],
            "figure_status": x["figure_status"],
            "migration_status": "ATLAS_CLASSIFIED",
            "editorial_status": editorial,
            "notes": f"classification={x['confidence']}; margin={x['margin']}; {x['basis']}",
        }
        classified.append(row)

        if editorial == "PLACEMENT_REVIEW_REQUIRED":
            review.append({
                "semantic_unit_id": x["semantic_unit_id"],
                "representative_problem_id": x["representative_problem_id"],
                "suggested_volume": p.roman,
                "suggested_thematic_section": th.name,
                "related_chapters": th.chapters,
                "confidence": x["confidence"],
                "score_margin": x["margin"],
                "source_files": x["source_files"],
                "problem_type": x["problem_type"],
                "classification_basis": x["basis"],
                "review_reason": "; ".join(reasons),
            })

    write_tsv(atlas_path, ATLAS_FIELDS, classified)
    write_tsv(review_path, REVIEW_FIELDS, review)

    by_volume = Counter(r["related_volume"] for r in classified)
    by_conf = Counter(re.search(r"classification=([A-Z]+)", r["notes"]).group(1) for r in classified)
    solved = sum(1 for r in classified if r["has_solution"].upper() == "YES")
    fig_candidates = sum(1 for r in classified if r["figure_requirement"] in {"YES","CANDIDATE"})

    lines = [
        "# Companion semantic problem placement atlas",
        "",
        "This atlas places every reconciled semantic problem unit into one Companion Part and one broad thematic section.",
        "It is an intermediate staging classification, not a final decision to insert the problem into a specific main-volume chapter.",
        "",
        "## Coverage",
        "",
        f"- Semantic units classified: **{len(classified)}**",
        f"- Units with reconciled solutions: **{solved}**",
        f"- Placement-review rows: **{len(review)}**",
        f"- Existing/source or candidate visual rows: **{fig_candidates}**",
        "",
        "## By Companion Part / related Volume",
        "",
    ]
    for roman in SUMMARY_ORDER:
        p = PROFILE_BY_ROMAN[roman]
        lines.append(f"- Part {p.part} / Volume {roman} — {p.title}: **{by_volume.get(roman,0)}**")
    lines += ["", "## Classification confidence", ""]
    for k in ("HIGH","MEDIUM","LOW"):
        lines.append(f"- {k}: **{by_conf.get(k,0)}**")
    lines += [
        "",
        "## Interpretation",
        "",
        "- `READY_FOR_COMPANION_MIGRATION` means the broad Part/thematic placement is strong enough to begin reader-facing migration.",
        "- `PLACEMENT_REVIEW_REQUIRED` does not discard the problem; it records a proposed placement that should be checked during migration.",
        "- `related_chapters` is intentionally a chapter range or thematic region. Exact main-book integration is deferred until after the Companion is complete.",
        "- Figure status is only a first-pass signal. A dedicated visual audit follows mathematical migration.",
        "",
    ]
    summary_path.write_text("\n".join(lines), encoding="utf-8")

    print("COMPANION SEMANTIC ATLAS BUILT")
    print(f"  semantic units: {len(classified)}")
    print(f"  solved units: {solved}")
    print(f"  placement review: {len(review)}")
    for roman in SUMMARY_ORDER:
        print(f"  Volume {roman}: {by_volume.get(roman,0)}")
    print(f"  output: {atlas_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
