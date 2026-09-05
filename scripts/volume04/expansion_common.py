from __future__ import annotations
import importlib.util, re
from pathlib import Path

VOLUME = Path("books/vol04_complex_analysis/chapters")
SECTION = re.compile(r"(?m)^\\section\{([^}]+)\}\s*$")
CORE = "Core structural results"
CATEGORIES = [
    ("standard", "Standard computations", 5),
    ("proof", "Proofs", 4),
    ("test", "Counterexamples and hypothesis tests", 3),
    ("application", "Applications and investigations", 2),
    ("challenge", "Challenge problems", 2),
]

CHAPTER_PATHS = {
  1:"ch01_complex_differentiability", 2:"ch02_cauchy_riemann_equations",
  3:"ch03_power_series_and_analytic_functions", 4:"ch04_complex_integration",
  5:"ch05_cauchy_s_theorem", 6:"ch06_cauchy_s_integral_formula",
  7:"ch07_zeros_and_the_identity_theorem", 8:"ch08_laurent_series",
  9:"ch09_isolated_singularities", 10:"ch10_residues_and_the_residue_theorem",
  11:"ch11_evaluation_of_real_integrals", 12:"ch12_winding_numbers_and_the_argument_principle",
  13:"ch13_rouch_s_theorem", 14:"ch14_branches_of_the_logarithm_and_roots",
  15:"ch15_analytic_continuation", 16:"ch16_m_bius_transformations",
  17:"ch17_conformal_mapping", 18:"ch18_schwarz_christoffel_transformations",
  19:"ch19_the_gamma_function", 20:"ch20_beta_and_gamma_identities",
  21:"ch21_keyhole_contours_and_branch_cut_integrals",
  22:"ch22_from_analytic_continuation_to_riemann_surfaces",
  23:"ch23_covering_maps_and_monodromy", 24:"ch24_branched_coverings",
  25:"ch25_construction_by_gluing", 26:"ch26_compactification_and_genus",
  27:"ch27_lattices_and_complex_tori", 28:"ch28_elliptic_functions",
  29:"ch29_the_weierstrass_function", 30:"ch30_addition_formulas",
  31:"ch31_elliptic_curves_as_riemann_surfaces",
}

def code_for(n: int) -> str:
    return f"IV/{n:02d}"

def compact(code: str) -> str:
    return code.replace("/", "")

def path_for(repo: Path, n: int) -> Path:
    return repo / VOLUME / CHAPTER_PATHS[n] / "chapter.tex"

def load_data(path: Path) -> dict:
    spec = importlib.util.spec_from_file_location("vol04_expansion_data", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import data file: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.DATA

def render_example(code: str, index: int, item: dict) -> str:
    tag = f"{compact(code)}-example-{index:02d}"
    label = f"ex:{compact(code).lower()}-expand-{index:02d}"
    return (
        f"% BEGIN VOL04-EXPANSION {tag}\n"
        f"\\begin{{example}}[{item['title']}]\\label{{{label}}}\n"
        f"{item['body'].strip()}\n"
        f"\\end{{example}}\n"
        f"% END VOL04-EXPANSION {tag}\n"
    )

def render_exercises(code: str, groups: dict) -> str:
    tag = f"{compact(code)}-exercises-01"
    parts = [
        f"% BEGIN VOL04-EXPANSION {tag}",
        "\\section{Graded supplementary exercises}",
        "These exercises extend the protected chapter with a balanced set of computations, proofs, hypothesis tests, applications, and challenges.",
        "",
    ]
    serial = 0
    for key, heading, expected in CATEGORIES:
        items = groups.get(key, [])
        if len(items) != expected:
            raise RuntimeError(f"{code}:{key} expected {expected} items, got {len(items)}")
        parts.append(f"\\subsection*{{{heading}}}")
        parts.append("")
        for item in items:
            serial += 1
            label = f"exr:{compact(code).lower()}-expand-{serial:02d}"
            parts.extend([
                f"\\begin{{exercise}}[{item['title']}]\\label{{{label}}}",
                item["prompt"].strip(),
                "\\end{exercise}",
                "\\begin{hint}", item["hint"].strip(), "\\end{hint}",
                "\\begin{solution}", item["solution"].strip(), "\\end{solution}", "",
            ])
    if serial != 16:
        raise RuntimeError(f"{code}: expected 16 exercises, rendered {serial}")
    parts.append(f"% END VOL04-EXPANSION {tag}")
    parts.append("")
    return "\n".join(parts)

def render_all_blocks(code: str, chapter_data: dict) -> list[str]:
    return [render_example(code, i, x) for i, x in enumerate(chapter_data["examples"], 1)] + [render_exercises(code, chapter_data["exercises"])]

def insert_examples(text: str, code: str, chapter_data: dict) -> str:
    matches = [m for m in SECTION.finditer(text) if m.group(1) != CORE]
    core = next((m for m in SECTION.finditer(text) if m.group(1) == CORE), None)
    if core is None:
        raise RuntimeError(f"{code}: missing '{CORE}' section")
    concept = [m for m in matches if m.start() < core.start()]
    if len(concept) < 8:
        raise RuntimeError(f"{code}: expected at least 8 concept sections before core results, got {len(concept)}")
    inserts: list[tuple[int, str]] = []
    examples = chapter_data.get("examples", [])
    if len(examples) != 3:
        raise RuntimeError(f"{code}: expected exactly 3 examples, got {len(examples)}")
    for idx, item in enumerate(examples, 1):
        after = int(item["after_section"])
        if not 1 <= after <= len(concept):
            raise RuntimeError(f"{code}: invalid after_section={after}")
        target = concept[after - 1]
        # Insert before the next section; if this is the last concept section, insert before Core.
        pos = concept[after].start() if after < len(concept) else core.start()
        inserts.append((pos, render_example(code, idx, item)))
    for pos, block in sorted(inserts, reverse=True):
        text = text[:pos] + block + text[pos:]
    return text

def expand_chapter(original: str, code: str, chapter_data: dict) -> str:
    expected_tags = [f"{compact(code)}-example-{i:02d}" for i in range(1,4)] + [f"{compact(code)}-exercises-01"]
    present = [tag for tag in expected_tags if f"% BEGIN VOL04-EXPANSION {tag}" in original]
    if present:
        if len(present) == len(expected_tags):
            return original
        raise RuntimeError(f"{code}: partial expansion markers present: {present}")
    text = insert_examples(original, code, chapter_data)
    exercise_block = render_exercises(code, chapter_data["exercises"])
    # Keep the original bytes reconstructible: append the marked block without altering original text.
    return text + exercise_block
