from __future__ import annotations
import importlib.util,re
from pathlib import Path
VOLUME=Path("books/vol06_algebraic_geometry/chapters")
SECTION=re.compile(r"(?m)^\\section\*?\{([^}]+)\}(?:\s*\\label\{[^}]+\})?\s*(?:%[^\n]*)?$")
TERMINAL_SECTION = re.compile(
    r"^(?:"
    r"problems?(?:\b|:)|"
    r"exercises?(?:\b|:)|"
    r"solutions?(?:\b|:)|"
    r"hints?(?:\b|:)|"
    r"worked examples?(?:\b|:)|"
    r"solved problems?(?:\b|:)|"
    r"problem bank(?:\b|:)|"
    r"exercise bank(?:\b|:)|"
    r"legacy problems?(?:\b|:)|"
    r"chapter summary(?:\b|:)|"
    r"references?(?:\b|:)|"
    r"bibliography(?:\b|:)"
    r")",
    re.I,
)
CATEGORIES=[("standard","Standard computations",5),("proof","Proofs",4),("test","Counterexamples and hypothesis tests",3),("application","Applications and investigations",2),("challenge","Challenge problems",2)]
CHAPTER_PATHS={1: 'ch01_algebraic_sets',
 2: 'ch02_zariski_topology',
 3: 'ch03_coordinate_rings',
 4: 'ch04_morphisms_affine_algebraic_sets',
 5: 'ch05_irreducibility_components',
 6: 'ch06_prime_ideals_geometric_points',
 7: 'ch07_spectrum_of_a_ring',
 8: 'ch08_basic_open_sets',
 9: 'ch09_generic_closed_points',
 10: 'ch10_reduced_nonreduced_geometry',
 11: 'ch11_local_rings_residue_fields',
 12: 'ch12_presheaves',
 13: 'ch13_sheaves_stalks',
 14: 'ch14_sheafification',
 15: 'ch15_kernels_images_quotients',
 16: 'ch16_exact_sequences_sheaves',
 17: 'ch17_structure_sheaf',
 18: 'ch18_affine_schemes',
 19: 'ch19_morphisms_affine_schemes',
 20: 'ch20_gluing_affine_schemes',
 21: 'ch21_schemes_and_points',
 22: 'ch22_open_closed_subschemes',
 23: 'ch23_fiber_products',
 24: 'ch24_base_change',
 25: 'ch25_fibers_geometric_fibers',
 26: 'ch26_finite_type_noetherian_morphisms',
 27: 'ch27_integral_schemes_function_fields',
 28: 'ch28_normalization',
 29: 'ch29_krull_dimension',
 30: 'ch30_dimension_of_schemes',
 31: 'ch31_codimension',
 32: 'ch32_tangent_spaces_and_local_geometry',
 33: 'ch33_o_x_modules_quasicoherent',
 34: 'ch34_graded_rings',
 35: 'ch35_proj',
 36: 'ch36_projective_space',
 37: 'ch37_projective_schemes',
 38: 'ch38_projective_morphisms_and_closed_embeddings',
 39: 'ch39_weil_divisors',
 40: 'ch40_cartier_divisors',
 41: 'ch41_divisor_class_groups',
 42: 'ch42_line_bundles_and_picard_groups',
 43: 'ch43_plane_cubics',
 44: 'ch44_cremona_transformations',
 45: 'ch45_blow_ups',
 46: 'ch46_flabby_sheaves',
 47: 'ch47_ech_cohomology',
 48: 'ch48_exact_sequences_and_cohomology',
 49: 'ch49_basic_vanishing_results'}
def code_for(n): return f"VI/{n:02d}"
def compact(code): return code.replace("/","")
def path_for(repo,n): return repo/VOLUME/CHAPTER_PATHS[n]/"chapter.tex"
def load_data(path):
    spec=importlib.util.spec_from_file_location("vol06_pedagogy_data",path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod.DATA
def render_example(code,i,item):
    tag=f"{compact(code)}-example-{i:02d}"; lab=f"ex:{compact(code).lower()}-expand-{i:02d}"
    return f"% BEGIN VOL06-EXPANSION {tag}\n\\begin{{example}}[{item['title']}]\\label{{{lab}}}\n{item['body'].strip()}\n\\end{{example}}\n% END VOL06-EXPANSION {tag}\n"
def render_exercises(code,groups):
    tag=f"{compact(code)}-exercises-01"; out=[f"% BEGIN VOL06-EXPANSION {tag}","\\section{Graded supplementary exercises}","These exercises extend the protected chapter with computations, proofs, hypothesis tests, applications, and challenges.",""]; serial=0
    for key,heading,expected in CATEGORIES:
        items=groups.get(key,[])
        if len(items)!=expected: raise RuntimeError(f"{code}:{key} expected {expected}, got {len(items)}")
        out += [f"\\subsection*{{{heading}}}",""]
        for item in items:
            serial+=1; lab=f"exr:{compact(code).lower()}-expand-{serial:02d}"
            out += [f"\\begin{{exercise}}[{item['title']}]\\label{{{lab}}}",item["prompt"].strip(),"\\end{exercise}",
                    "\\begin{hint}",item["hint"].strip(),"\\end{hint}",
                    "\\begin{solution}",item["solution"].strip(),"\\end{solution}",""]
    if serial!=16: raise RuntimeError(f"{code}: expected 16 exercises")
    out += [f"% END VOL06-EXPANSION {tag}",""]; return "\n".join(out)
def render_all_blocks(code,d): return [render_example(code,i,x) for i,x in enumerate(d["examples"],1)]+[render_exercises(code,d["exercises"])]
def concept_sections(text):
    ms=list(SECTION.finditer(text)); out=[]
    for m in ms:
        title=m.group(1).strip()
        low=title.lower()
        # Skip chapter front-matter headings, but keep conceptual starred sections.
        if low in {"purpose and learning goals","learning goals","chapter roadmap"}:
            continue
        # Stop only at genuine terminal pedagogy/reference sections.
        # Conceptual headings such as "The universal problem" remain valid.
        if TERMINAL_SECTION.match(title):
            break
        out.append(m)
    return out
def expand_chapter(original,code,d):
    tags=[f"{compact(code)}-example-{i:02d}" for i in range(1,4)]+[f"{compact(code)}-exercises-01"]
    present=[x for x in tags if f"% BEGIN VOL06-EXPANSION {x}" in original]
    if present:
        if len(present)==4: return original
        raise RuntimeError(f"{code}: partial expansion markers: {present}")
    if not original.endswith("\n"): raise RuntimeError(f"{code}: protected chapter must end with newline")
    concept=concept_sections(original)
    if not concept:
        raise RuntimeError(f"{code}: no conceptual section boundary available")
    # Find the first genuine terminal pedagogy/reference section, if any.
    all_sections=list(SECTION.finditer(original))
    terminal_start=len(original)
    for m in all_sections:
        if TERMINAL_SECTION.match(m.group(1).strip()):
            terminal_start=m.start()
            break
    # Normal chapters: spread examples across conceptual development.
    # Sparse chapters: keep all examples safely inside the conceptual region,
    # immediately before the terminal material rather than aborting.
    k=len(concept)
    if k>=3:
        afters=[max(1,k//4),max(1,k//2),max(1,(3*k)//4)]
        afters=[min(a,k-1) if k>1 else 1 for a in afters]
        positions=[concept[a].start() if a<k else terminal_start for a in afters]
    elif k==2:
        positions=[concept[1].start(),terminal_start,terminal_start]
    else:
        positions=[terminal_start,terminal_start,terminal_start]
    inserts=[]
    for i,(item,pos) in enumerate(zip(d["examples"],positions),1):
        inserts.append((pos,i,render_example(code,i,item)))
    text=original
    # reverse position and reverse index so final same-position order is 1,2,3
    for pos,i,block in sorted(inserts,key=lambda x:(x[0],x[1]),reverse=True): text=text[:pos]+block+text[pos:]
    return text+render_exercises(code,d["exercises"])
