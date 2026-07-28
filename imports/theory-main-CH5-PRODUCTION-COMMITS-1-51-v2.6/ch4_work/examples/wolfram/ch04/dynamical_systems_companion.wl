Clear["Global`*"];
DSolveValue[{y'[t] == -2 y[t], y[0] == 1}, y[t], t]
sol=NDSolveValue[{x'[t]==v[t],v'[t]==x[t]-x[t]^3-.2v[t],x[0]==.2,v[0]==.8},{x,v},{t,0,30}];
