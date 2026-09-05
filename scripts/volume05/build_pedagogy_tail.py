#!/usr/bin/env python3
import argparse,importlib.util,pprint
from pathlib import Path
from pedagogy_specs_v15_v28 import SPECS
def load(path):
    spec=importlib.util.spec_from_file_location("base_data",path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod.DATA
def tri(title,prompt,hint,solution): return {"title":title,"prompt":prompt,"hint":hint,"solution":solution}
def build(code,base,s):
    examples=[{"after_section":a,"title":b,"body":c} for a,b,c in s["examples"]]
    std=[tri(t,p,"Use "+s["focus"]+".",ans) for t,p,ans in s["calc"]]
    proofs=[]
    for title,statement,proof in base["theorems"][:3]:
        proofs.append(tri(title+" proof","Prove: "+statement,"Start from the theorem hypotheses and identify the decisive algebraic construction.",proof))
    names=[x[0] for x in base["theorems"][:2]]
    proofs.append(tri("Structural synthesis",f"Prove a corollary that genuinely uses both {names[0]} and {names[1]}.","Apply the first theorem to obtain its structural description, then verify the second theorem's hypotheses.","A correct proof explicitly invokes both results, verifies the common hypotheses, and derives a new consequence rather than merely restating either theorem."))
    tests=[tri(t,"Test the claim: "+p,"Use the smallest concrete ring, module, or resolution that can decide the claim.",ans) for t,p,ans in s["tests"]]
    apps=[tri(t,p,"Translate the question into "+s["focus"]+".",ans) for t,p,ans in s["apps"]]
    sec=base["sections"]
    ch=[
      tri("Local-global synthesis",f"Connect '{sec[0][0]}' with '{sec[-1][0]}' in one rigorous argument.","State the relevant ring map, module map, or complex before applying the structural theorem.",f"The opening idea is: {sec[0][1]} The later viewpoint is: {sec[-1][1]} A complete solution identifies the structural theorem that links these descriptions and checks its hypotheses."),
      tri("Hypothesis audit","Choose one theorem from the chapter, remove one essential hypothesis, and exhibit or explain a concrete failure.","Use one of the chapter's explicit computations or counterexamples as the test case.","The solution must name the removed hypothesis, show exactly which proof step breaks, and give a concrete algebraic object where the claimed conclusion fails.")
    ]
    return {"examples":examples,"exercises":{"standard":std,"proof":proofs,"test":tests,"application":apps,"challenge":ch}}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--base",required=True); ap.add_argument("--start",type=int,required=True); ap.add_argument("--end",type=int,required=True); ap.add_argument("--out",required=True); a=ap.parse_args()
    base=load(Path(a.base).resolve()); out={}
    for n in range(a.start,a.end+1):
        code=f"V/{n:02d}"
        if code not in base: raise RuntimeError(f"{code} missing from base")
        out[code]=build(code,base[code],SPECS[code])
    Path(a.out).write_text("DATA = "+pprint.pformat(out,width=135,sort_dicts=True)+"\n",encoding="utf-8")
    print(f"Wrote {len(out)} chapter(s) to {a.out}")
if __name__=="__main__": raise SystemExit(main())
