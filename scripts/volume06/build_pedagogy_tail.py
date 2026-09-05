#!/usr/bin/env python3
import argparse,pprint
from pathlib import Path
from pedagogy_specs_vi33_vi49 import SPECS

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--start",type=int,required=True)
    ap.add_argument("--end",type=int,required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    data={}
    for n in range(a.start,a.end+1):
        s=SPECS[n]; code=f"VI/{n:02d}"
        data[code]={
          "examples":[{"title":t,"body":b} for t,b in s["examples"]],
          "exercises":{
            "standard":[{"title":t,"prompt":p,"hint":"Use "+s["focus"]+".","solution":ans} for t,p,ans in s["std"]],
            "proof":[{"title":t,"prompt":"Prove: "+p,"hint":"Work from "+s["focus"]+" and state the hypotheses explicitly.","solution":ans} for t,p,ans in s["proofs"]],
            "test":[{"title":t,"prompt":p,"hint":"Test the claim on a concrete projective, divisor, blow-up, or sheaf model before generalizing.","solution":ans} for t,p,ans in s["tests"]],
            "application":[{"title":t,"prompt":p,"hint":"Translate the question into "+s["focus"]+".","solution":ans} for t,p,ans in s["apps"]],
            "challenge":[
              {"title":"Synthesis challenge",
               "prompt":f"Connect two central viewpoints of {s['title']} in one explicit calculation or proof.",
               "hint":"Start from one worked example and reformulate it using the chapter's structural correspondence.",
               "solution":f"A complete solution makes one concrete computation in {s['title']} and then translates it through {s['focus']}, checking both descriptions agree."},
              {"title":"Hypothesis challenge",
               "prompt":f"Choose one theorem-level statement from {s['title']}, remove one essential hypothesis, and give a concrete failure.",
               "hint":"Use one of the hypothesis tests above as the seed counterexample.",
               "solution":"Name the removed hypothesis, identify the proof step that fails, and exhibit a concrete ring, scheme, divisor, sheaf, or morphism where the conclusion is false."}
            ],
          },
        }
        counts=data[code]["exercises"]
        expected={"standard":5,"proof":4,"test":3,"application":2,"challenge":2}
        for k,v in expected.items():
            if len(counts[k])!=v: raise RuntimeError(f"{code}:{k}:{len(counts[k])}!={v}")
        if len(data[code]["examples"])!=3: raise RuntimeError(f"{code}:examples")
    Path(a.out).write_text("DATA = "+pprint.pformat(data,width=150,sort_dicts=True)+"\n",encoding="utf-8")
    print(f"Wrote pedagogy data for {len(data)} chapters to {a.out}")
if __name__=="__main__":
    raise SystemExit(main())
