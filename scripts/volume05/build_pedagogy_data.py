#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, pprint
from pathlib import Path
from pedagogy_specs import SPECS

def load(path):
    spec=importlib.util.spec_from_file_location("base_volume05_data",path)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod.DATA

def t(title,prompt,hint,solution):
    return {"title":title,"prompt":prompt,"hint":hint,"solution":solution}

def build_one(code,base,spec):
    examples=[{"after_section":a,"title":b,"body":c} for a,b,c in spec["examples"]]
    standard=[t(title,prompt,"Use "+spec["focus"]+".",answer) for title,prompt,answer in spec["calc"]]
    proofs=[]
    for title,statement,proof in base["theorems"][:3]:
        proofs.append(t(title+" proof","Prove: "+statement,"Start from the chapter theorem hypotheses and identify the decisive algebraic map or containment.",proof))
    thnames=[x[0] for x in base["theorems"][:2]]
    proofs.append(t("Structural synthesis",
        f"Prove a short corollary by combining {thnames[0]} with {thnames[1]}. State every hypothesis you use.",
        "Apply the first theorem to move to its structural description, then use the second theorem on that description.",
        f"A valid synthesis first invokes {thnames[0]} and then applies {thnames[1]}; the conclusion follows after checking the shared hypotheses."))
    tests=[t(title,"Test the claim: "+claim,"Try a smallest standard ring or module from this chapter.",answer) for title,claim,answer in spec["tests"]]
    apps=[t(title,prompt,"Translate the situation into "+spec["focus"]+".",answer) for title,prompt,answer in spec["apps"]]
    sections=base["sections"]
    challenges=[
      t("Local-global synthesis",
        f"Connect the chapter ideas '{sections[0][0]}' and '{sections[-1][0]}' in one rigorous argument.",
        "State the relevant map, ideal, module, or universal property before drawing the conclusion.",
        f"The argument begins with {sections[0][1]} It then uses the later viewpoint: {sections[-1][1]} The bridge is supplied by the structural theorems proved in the chapter."),
      t("Hypothesis audit",
        f"Choose one theorem from the chapter and explain precisely what can fail if one key hypothesis is removed.",
        "Use one of the explicit counterexamples in the graded set and compare it with the theorem statement.",
        f"The theorem hypotheses are essential because the chapter's quotient, localization, exactness, or finiteness mechanism can fail outside them. A correct answer identifies the dropped hypothesis and exhibits a concrete failure.")
    ]
    return {"examples":examples,"exercises":{"standard":standard,"proof":proofs,"test":tests,"application":apps,"challenge":challenges}}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--base",required=True); ap.add_argument("--start",type=int,required=True); ap.add_argument("--end",type=int,required=True); ap.add_argument("--out",required=True)
    a=ap.parse_args(); base=load(Path(a.base).resolve()); data={}
    for n in range(a.start,a.end+1):
        code=f"V/{n:02d}"
        if code not in base: raise RuntimeError(f"{code} missing from base data")
        if code not in SPECS: raise RuntimeError(f"{code} missing from pedagogy specs")
        data[code]=build_one(code,base[code],SPECS[code])
    Path(a.out).write_text("DATA = "+pprint.pformat(data,width=130,sort_dicts=True)+"\n",encoding="utf-8")
    print(f"Wrote pedagogy data for {len(data)} chapter(s): {a.out}")
if __name__=="__main__": raise SystemExit(main())
