(* Chapter 1 computational companion: Wolfram Language *)
a = {4, 3}; b = {5, 1};
projection = (a.b)/(b.b) b;
Graphics[{Arrow[{{0, 0}, a}], Arrow[{{0, 0}, b}],
  Dashed, Line[{projection, a}], Arrow[{{0, 0}, projection}]}, Axes -> True]

rotation[theta_] := {{Cos[theta], -Sin[theta]}, {Sin[theta], Cos[theta]}};
Table[rotation[theta].{3, 1}, {theta, 0, Pi/2, Pi/6}]

A = {{1.5, .7}, {.3, 1.2}};
A.# & /@ {{0, 0}, {1, 0}, {1, 1}, {0, 1}}

Orthogonalize[{{3, 1}, {2, 3}}, Method -> "GramSchmidt"]
