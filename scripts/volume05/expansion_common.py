from __future__ import annotations
import importlib.util,re
from pathlib import Path
VOLUME=Path("books/vol05_commutative_algebra/chapters")
SECTION=re.compile(r"(?m)^\\section\{([^}]+)\}\s*$"); CORE="Core structural results"
CATEGORIES=[("standard","Standard computations",5),("proof","Proofs",4),("test","Counterexamples and hypothesis tests",3),("application","Applications and investigations",2),("challenge","Challenge problems",2)]
CHAPTER_PATHS={1:"ch01_rings_ideals_and_quotients",2:"ch02_prime_and_maximal_ideals",3:"ch03_radicals_and_nilpotents",4:"ch04_chinese_remainder_theory",5:"ch05_multiplicative_systems",6:"ch06_localization_of_rings",7:"ch07_localization_of_modules",8:"ch08_local_rings_and_localization_at_primes",9:"ch09_modules_and_exact_sequences",10:"ch10_tensor_products",11:"ch11_quotients_and_base_change",12:"ch12_hom_and_finitely_presented_modules",13:"ch13_free_and_projective_modules",14:"ch14_flat_modules",15:"ch15_noetherian_rings_and_modules",16:"ch16_support",17:"ch17_associated_primes",18:"ch18_completion_and_i_adic_topology",19:"ch19_integral_dependence",20:"ch20_integral_closure_and_normalization",21:"ch21_valuation_rings",22:"ch22_chain_complexes",23:"ch23_free_resolutions",24:"ch24_syzygies",25:"ch25_minimal_resolutions",26:"ch26_the_tor_functor",27:"ch27_the_ext_functor",28:"ch28_derived_functor_viewpoint"}
def code_for(n): return f"V/{n:02d}"
def compact(code): return code.replace("/","")
def path_for(repo,n): return repo/VOLUME/CHAPTER_PATHS[n]/"chapter.tex"
def load_data(path):
    spec=importlib.util.spec_from_file_location("pedagogy_data",path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod.DATA
def render_example(code,i,item):
    tag=f"{compact(code)}-example-{i:02d}"; lab=f"ex:{compact(code).lower()}-expand-{i:02d}"
    return f"% BEGIN VOL05-EXPANSION {tag}\n\\begin{{example}}[{item['title']}]\\label{{{lab}}}\n{item['body'].strip()}\n\\end{{example}}\n% END VOL05-EXPANSION {tag}\n"
def render_exercises(code,groups):
    tag=f"{compact(code)}-exercises-01"; out=[f"% BEGIN VOL05-EXPANSION {tag}","\\section{Graded supplementary exercises}","These exercises extend the protected chapter with a balanced set of computations, proofs, hypothesis tests, applications, and challenges.",""]; serial=0
    for key,heading,expected in CATEGORIES:
        items=groups.get(key,[])
        if len(items)!=expected: raise RuntimeError(f"{code}:{key} expected {expected}, got {len(items)}")
        out += [f"\\subsection*{{{heading}}}",""]
        for item in items:
            serial+=1; lab=f"exr:{compact(code).lower()}-expand-{serial:02d}"
            out += [f"\\begin{{exercise}}[{item['title']}]\\label{{{lab}}}",item["prompt"].strip(),"\\end{exercise}","\\begin{hint}",item["hint"].strip(),"\\end{hint}","\\begin{solution}",item["solution"].strip(),"\\end{solution}",""]
    if serial!=16: raise RuntimeError(f"{code}: expected 16 exercises")
    out += [f"% END VOL05-EXPANSION {tag}",""]; return "\n".join(out)
def render_all_blocks(code,d): return [render_example(code,i,x) for i,x in enumerate(d["examples"],1)]+[render_exercises(code,d["exercises"])]
def expand_chapter(original,code,d):
    tags=[f"{compact(code)}-example-{i:02d}" for i in range(1,4)]+[f"{compact(code)}-exercises-01"]
    present=[x for x in tags if f"% BEGIN VOL05-EXPANSION {x}" in original]
    if present:
        if len(present)==4: return original
        raise RuntimeError(f"{code}: partial expansion markers: {present}")
    ms=list(SECTION.finditer(original)); core=next((m for m in ms if m.group(1)==CORE),None)
    if core is None: raise RuntimeError(f"{code}: missing core section")
    concept=[m for m in ms if m.start()<core.start()]
    if len(concept)<8: raise RuntimeError(f"{code}: expected at least 8 concept sections")
    inserts=[]
    for i,item in enumerate(d["examples"],1):
        after=int(item["after_section"]); pos=concept[after].start() if after<len(concept) else core.start(); inserts.append((pos,render_example(code,i,item)))
    text=original
    for pos,block in sorted(inserts,reverse=True): text=text[:pos]+block+text[pos:]
    return text+render_exercises(code,d["exercises"])
