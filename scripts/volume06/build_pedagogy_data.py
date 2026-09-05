#!/usr/bin/env python3
import argparse,importlib.util,pprint
from pathlib import Path
from pedagogy_specs_vi01_vi32 import SPECS
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--start",type=int,required=True); ap.add_argument("--end",type=int,required=True); ap.add_argument("--out",required=True); a=ap.parse_args()
    out={}
    for n in range(a.start,a.end+1):
        s=SPECS[n]; code=f"VI/{n:02d}"
        examples=[{"title":t,"body":b} for t,b in s["examples"]]
        standard=[{"title":t,"prompt":p,"hint":"Use "+s["focus"]+".","solution":ans} for t,p,ans in s["std"]]
        proofs=[{"title":t,"prompt":"Prove: "+claim,"hint":"Work directly from "+s["focus"]+".","solution":sketch} for t,claim,sketch in s["proofs"]]
        tests=[{"title":t,"prompt":p,"hint":"Test the claim on a concrete affine or local model before generalizing.","solution":ans} for t,p,ans in s["tests"]]
        apps=[{"title":t,"prompt":p,"hint":"Translate the question into "+s["focus"]+".","solution":ans} for t,p,ans in s["apps"]]
        challenges=[
          {"title":"Synthesis challenge","prompt":f"Combine the main algebraic and geometric viewpoints of {s['title']} in one explicit argument, using at least one localization, quotient, stalk, fiber, or prime-ideal calculation when appropriate.","hint":"Start from one of the worked examples, then reformulate it using the chapter's structural correspondence.","solution":f"A complete solution identifies the concrete model from {s['title']}, translates it through {s['focus']}, and checks the correspondence in both algebraic and geometric language."},
          {"title":"Hypothesis challenge","prompt":f"Choose one structural statement from {s['title']}, remove one essential hypothesis, and construct or explain a counterexample.","hint":"Use one of the three hypothesis tests above as a starting point and sharpen it to the theorem under discussion.","solution":"The solution must name the removed hypothesis, identify the proof step that fails, and exhibit a concrete ring, scheme, sheaf, or morphism where the conclusion no longer holds."}
        ]
        assert len(examples)==3 and len(standard)==5 and len(proofs)==4 and len(tests)==3 and len(apps)==2 and len(challenges)==2
        out[code]={"examples":examples,"exercises":{"standard":standard,"proof":proofs,"test":tests,"application":apps,"challenge":challenges}}
    Path(a.out).write_text("DATA = "+pprint.pformat(out,width=150,sort_dicts=True)+"\n",encoding="utf-8")
    print(f"Wrote pedagogy data for {len(out)} chapters to {a.out}")
if __name__=="__main__": raise SystemExit(main())
