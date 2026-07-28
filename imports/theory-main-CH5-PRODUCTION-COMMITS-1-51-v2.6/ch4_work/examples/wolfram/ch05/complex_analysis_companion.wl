(* Chapter 5 complex-analysis companion *)
roots[n_] := Exp[2 Pi I Range[0, n - 1]/n];
Print[Max[Abs[roots[8]^8 - 1]]];
Graphics[{Circle[], PointSize[.02], Point[ReIm /@ roots[8]]}, Axes -> True]
ComplexPlot[z^3 - 1, {z, -1.7 - 1.4 I, 1.7 + 1.4 I}, PlotLegends -> Automatic]
ParametricPlot[Evaluate@Table[ReIm[(t + I c)^2], {c, -1.2, 1.2, .3}], {t, -1.2, 1.2}, AspectRatio -> 1]
NIntegrate[1/z, {z, 1, I, -1, -I, 1}]
