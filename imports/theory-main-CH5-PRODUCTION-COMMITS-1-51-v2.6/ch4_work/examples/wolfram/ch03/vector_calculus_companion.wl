(* Chapter 3 vector-calculus companion *)
Clear[x,y,z];
f = {-y,x,0};
Print["Divergence: ", Div[f,{x,y,z}]];
Print["Curl: ", Curl[f,{x,y,z}]];
Print["Laplacian of Gaussian: ", Laplacian[Exp[-(x^2+y^2+z^2)],{x,y,z}]//Simplify];
(* Stokes check on a disk of radius R *)
Print["Stokes surface result: ", Integrate[2 r,{r,0,R},{theta,0,2 Pi}]];
(* Gauss check for F={x,y,z} in a ball *)
Print["Gauss volume result: ", Integrate[3 r^2 Sin[theta],{r,0,R},{theta,0,Pi},{phi,0,2 Pi}]];
