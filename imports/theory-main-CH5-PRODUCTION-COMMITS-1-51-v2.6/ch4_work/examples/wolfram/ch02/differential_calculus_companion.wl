(* Chapter 2 computational companion: Wolfram Language *)
ClearAll[x, y, u, v, f, map];

f[x_, y_] := x^2 + y^2;

(* Gradient and Hessian *)
gradient = Grad[f[x, y], {x, y}]
hessian = D[f[x, y], {{x, y}, 2}]

(* Surface and level curves *)
Plot3D[f[x, y], {x, -2, 2}, {y, -2, 2},
 AxesLabel -> {"x", "y", "f"}, PlotTheme -> "Scientific"]
ContourPlot[f[x, y], {x, -2, 2}, {y, -2, 2},
 Contours -> 10, FrameLabel -> {"x", "y"}]

(* Gradient vector field *)
VectorPlot[Evaluate[gradient], {x, -2, 2}, {y, -2, 2},
 VectorScale -> {Small, Scaled[0.45], None}]

(* Jacobian of a nonlinear map *)
map[u_, v_] := {u + 0.35 v, 0.25 u + v + 0.12 u v};
jacobian = D[map[u, v], {{u, v}}]
Det[jacobian] // Simplify

(* Directional derivative at a point *)
point = {1, -1};
direction = Normalize[{2, 1}];
directionalDerivative = gradient.direction /. Thread[{x, y} -> point]
