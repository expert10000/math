#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

GOALS = {'II/01': ['compute suprema and infima of explicitly described subsets of \\(\\mathbb R\\) and justify that the proposed bounds are sharp;',
           'use the least-upper-bound property to prove existence statements rather than merely estimate candidate values;',
           'apply the Archimedean property to produce integers or reciprocals satisfying a prescribed inequality;',
           'prove density of rational or irrational numbers between two given reals by constructing the required element;',
           'derive triangle and reverse-triangle inequalities in concrete absolute-value problems;',
           'construct examples that distinguish maxima from suprema and expose the failure of completeness in \\(\\mathbb Q\\);'],
 'II/02': ['compute norms and distances in Euclidean and normed spaces and verify the norm axioms in concrete examples;',
           'compare two norms by proving explicit upper and lower inequalities between them;',
           'describe open balls in several norms and explain how their geometry differs;',
           'use the triangle and reverse-triangle inequalities to bound perturbations and distances;',
           'decide whether a proposed formula defines a norm and identify the failed axiom when it does not;',
           'translate coordinate estimates into norm estimates using finite-dimensional norm equivalence;'],
 'II/03': ['determine whether a sequence converges and prove the claimed limit with an explicit \\(\\varepsilon\\)-\\(N\\) argument;',
           'test whether a sequence is Cauchy and use completeness to infer convergence when appropriate;',
           'construct subsequences with prescribed limiting behavior;',
           'apply monotone convergence and squeeze arguments to concrete sequences;',
           'distinguish convergence, boundedness, Cauchy behavior, and existence of convergent subsequences by counterexample;',
           'estimate convergence rates sufficiently sharply to choose an \\(N\\) for a prescribed tolerance;'],
 'II/04': ['decide whether a set is open, closed, both, or neither from the definitions;',
           'compute interiors, closures, boundaries, and limit-point sets for explicit subsets of metric spaces;',
           'prove that arbitrary unions of open sets and finite intersections of open sets are open;',
           'use complements to convert statements about open sets into statements about closed sets;',
           'construct neighborhood or sequence arguments showing that a point lies in a closure or boundary;',
           'produce counterexamples showing why infinite intersections of open sets or infinite unions of closed sets need not preserve '
           'type;'],
 'II/05': ['verify continuity at a point using \\(\\varepsilon\\)-\\(\\delta\\), sequential, and inverse-image criteria;',
           'prove continuity of compositions and algebraic combinations from structural properties rather than coordinate expansion alone;',
           'compute Lipschitz constants for explicit maps and use them to obtain continuity estimates;',
           'distinguish continuity from uniform continuity by constructing or analyzing counterexamples;',
           'identify which topological properties are preserved under continuous maps in the situations treated in the chapter;',
           'translate metric estimates into neighborhood statements and back again;'],
 'II/06': ['prove compactness using finite-subcover, sequential, or Heine--Borel criteria in the setting where each applies;',
           'extract convergent subsequences from bounded sequences in Euclidean space;',
           'use compactness to prove attainment of maxima and minima of continuous functions;',
           'show that continuous images of compact sets are compact and use this to obtain boundedness or closedness conclusions;',
           'construct open covers or sequences that demonstrate failure of compactness;',
           'distinguish compactness from closedness and boundedness outside finite-dimensional Euclidean settings;'],
 'II/07': ['decide whether an explicitly described set is connected or path connected;',
           'construct explicit paths joining two points when path connectedness holds;',
           'use separation arguments or continuous images to prove connectedness;',
           'prove that intervals in \\(\\mathbb R\\) are connected and apply the result to intermediate-value arguments;',
           'construct examples showing that connectedness and path connectedness are not equivalent in complete generality;',
           'identify connected components or path components in elementary examples;'],
 'II/08': ['compute Fréchet derivatives and Jacobian matrices of maps between finite-dimensional normed spaces;',
           'verify differentiability from a linear approximation estimate rather than from partial derivatives alone;',
           'apply the multivariable chain rule to compositions and coordinate changes;',
           'compute directional derivatives and distinguish their existence from full differentiability;',
           'use derivative bounds to obtain local error estimates;',
           'construct examples where partial or directional derivatives exist but differentiability fails;'],
 'II/09': ['verify the hypotheses of the inverse function theorem by computing the derivative and checking its invertibility at a '
           'specified point;',
           'distinguish local invertibility from global injectivity and construct examples where the former holds without the latter;',
           'compute the derivative of a local inverse from \\(D(f^{-1})(f(a))=Df(a)^{-1}\\);',
           'identify which variables can be solved for in \\(F(x,y)=0\\) by checking the appropriate derivative block;',
           'derive and evaluate the implicit-derivative formula \\(Dg=-D_yF^{-1}D_xF\\) in concrete systems;',
           'analyze failure cases where a singular derivative or rank loss prevents the theorem from applying, without concluding more '
           'than the hypotheses justify;'],
 'II/10': ['compute upper and lower sums for explicit partitions and bounded functions;',
           'prove Riemann integrability by controlling \\(U(f,P)-L(f,P)\\);',
           'evaluate elementary Riemann integrals from partitions, antiderivatives, or comparison arguments;',
           'show that monotone or continuous functions on compact intervals are Riemann integrable;',
           'construct bounded functions that fail to be Riemann integrable and identify the obstruction;',
           'use additivity and comparison properties of the integral to derive estimates;'],
 'II/11': ['distinguish pointwise from uniform convergence using definitions and explicit examples;',
           'prove uniform convergence by estimating \\(\\sup_x|f_n(x)-f(x)|\\);',
           'use uniform convergence to pass continuity from \\(f_n\\) to the limit;',
           'construct examples where pointwise convergence does not preserve continuity or bounded error control;',
           'apply the uniform Cauchy criterion to sequences of functions;',
           'determine whether convergence is uniform on a whole domain or only on restricted subsets;'],
 'II/12': ['verify hypotheses that justify interchanging a limit with an integral or derivative;',
           'prove convergence of derivatives by combining uniform convergence of derivatives with convergence at one base point;',
           'construct examples showing that pointwise convergence alone does not justify differentiating or integrating termwise;',
           'estimate remainders uniformly enough to pass a limit through an operation;',
           'distinguish sufficient hypotheses for integral interchange from those needed for derivative interchange;',
           'use a theorem only after checking its domain, regularity, and convergence assumptions explicitly;'],
 'II/13': ['test convergence of numerical and function series using comparison, ratio, root, or uniform criteria;',
           'apply the Weierstrass M-test to prove uniform and absolute convergence of a function series;',
           'justify termwise integration or differentiation of a series when the required uniform hypotheses hold;',
           'determine the interval or region of convergence of a power series;',
           'estimate tails of convergent series sufficiently to meet a prescribed error tolerance;',
           'construct examples separating pointwise, uniform, absolute, and conditional convergence;'],
 'II/14': ['compute Fourier coefficients of elementary periodic functions;',
           'use symmetry to predict vanishing sine or cosine coefficients before integration;',
           'determine pointwise convergence values at continuity points and jump discontinuities under the stated hypotheses;',
           'apply Parseval-type identities in concrete coefficient computations;',
           'estimate partial sums or tails from coefficient information;',
           'distinguish convergence of a Fourier series from convergence of an arbitrary trigonometric series;'],
 'II/15': ['analyze continuity and differentiability of classical pathological examples such as Takagi- or Weierstrass-type functions;',
           'prove nowhere-differentiability or failure of regularity by isolating a scale-dependent oscillation;',
           'distinguish uniform convergence of a defining series from differentiability of its sum;',
           'estimate moduli of continuity for explicit pathological constructions;',
           'construct sequences of scales that expose incompatible difference quotients;',
           'explain which regularity theorem fails and which hypothesis is missing in a given counterexample;'],
 'II/16': ['verify that a self-map is a contraction by finding a constant \\(q<1\\);',
           'prove existence and uniqueness of a fixed point by applying the contraction mapping theorem with all hypotheses checked;',
           'derive quantitative error bounds for Picard iteration;',
           'choose a closed invariant subset on which a proposed iteration is actually contractive;',
           'compare different fixed-point iterations by their contraction constants;',
           'construct examples showing why completeness or the strict contraction condition cannot simply be omitted;'],
 'II/17': ['state and apply Brouwer-type fixed-point conclusions in finite-dimensional compact convex settings;',
           'verify compactness, convexity, and self-map hypotheses before invoking a fixed-point theorem;',
           'construct elementary one-dimensional or planar fixed-point arguments from continuity;',
           'distinguish Brouwer-type existence results from contraction-based uniqueness results;',
           'analyze examples where a fixed point exists but is not unique;',
           'identify which hypothesis fails in a fixed-point counterexample involving noncompact or nonconvex domains;'],
 'II/18': ['rewrite an integral equation as a fixed-point problem on a function space;',
           'estimate the associated integral operator in a sup or other relevant norm;',
           'verify conditions under which the integral operator is a contraction or maps a bounded set into itself;',
           'solve elementary separable or explicitly integrable integral equations;',
           'derive successive-approximation schemes and estimate their errors;',
           'distinguish existence, uniqueness, and stability conclusions for an integral equation;'],
 'II/19': ['convert a first-order ODE into an equivalent integral equation;',
           'verify local Lipschitz conditions in the dependent variable for concrete right-hand sides;',
           'apply Picard iteration to obtain successive approximations;',
           'derive local existence and uniqueness from contraction estimates on a suitable rectangle or ball;',
           'identify blow-up, nonuniqueness, or loss-of-Lipschitz examples where the standard theorem does not apply;',
           'estimate how the solution changes under perturbations of initial data or the right-hand side in elementary settings;'],
 'II/20': ['construct Lagrange and Newton interpolating polynomials from given data;',
           'prove uniqueness of the degree-at-most-\\(n\\) interpolant from the root-counting argument;',
           'compute divided differences and update a Newton interpolant when a new node is added;',
           'derive or apply the interpolation remainder formula to bound the error;',
           'compare equally spaced and Chebyshev-type node choices through the node polynomial;',
           'translate interpolation into a Vandermonde linear system and explain why distinct nodes are essential;'],
 'II/21': ['construct explicit polynomial approximants to continuous functions in the settings developed in the chapter;',
           'apply a polynomial approximation theorem only after checking compactness and continuity hypotheses;',
           'estimate approximation error using modulus-of-continuity or constructive bounds when available;',
           'distinguish interpolation from uniform approximation;',
           'prove density statements by reducing them to the appropriate approximation theorem;',
           'construct examples showing why smoothness can improve approximation rates without being necessary for mere density;'],
 'II/22': ['formulate the minimax approximation problem in the sup norm;',
           'compute simple best approximants by balancing extreme errors;',
           'use Chebyshev polynomials to control the maximum size of monic polynomials on an interval;',
           'compare interpolation error with best-uniform-approximation error;',
           'identify equioscillation patterns in explicit low-degree examples;',
           'derive error lower bounds that certify optimality of a candidate minimax approximant;'],
 'II/23': ['state the alternation criterion with the correct number and ordering of alternating extrema;',
           'use an alternation pattern to certify that a polynomial approximant is minimax;',
           'construct a perturbation argument showing that insufficient alternation cannot be optimal;',
           'identify the error function and its extreme points in explicit approximation problems;',
           "distinguish necessary from sufficient parts of the alternation principle under the chapter's hypotheses;",
           'apply the principle to low-degree examples without solving a larger optimization problem directly;'],
 'II/24': ['derive elementary quadrature rules by integrating an interpolating polynomial;',
           'compute degrees of exactness for given quadrature formulas;',
           'estimate quadrature errors from derivative bounds and remainder formulas;',
           'compare midpoint, trapezoidal, and Simpson-type rules on explicit integrands;',
           'construct composite rules and track how local error accumulates globally;',
           'choose a mesh size that achieves a prescribed error tolerance from an available error estimate;'],
 'II/25': ['compute finite and infinite continued-fraction convergents from recurrence relations;',
           'recover a continued-fraction expansion from the Euclidean algorithm in rational examples;',
           'prove basic determinant identities for consecutive convergents;',
           'use convergents to obtain rational approximations and quantify their error in elementary cases;',
           'compare continued-fraction approximants with simpler decimal or truncation approximations;',
           'identify which approximation statements require irrationality, infinite expansion, or additional hypotheses;']}

METHODS = {'II/01': ['To prove a candidate supremum, show first that it is an upper bound and then that every smaller number fails to be one.',
           'Use the Archimedean property to choose an integer large enough that its reciprocal lies below the prescribed tolerance.',
           'Rewrite the absolute-value inequality as a pair of ordinary inequalities before solving for the variable.',
           'Apply the reverse triangle inequality to compare two absolute values without expanding cases.',
           'For incompleteness, use a bounded rational set whose real least upper bound is irrational.',
           'Induct on the number of elements: adjoining one new element reduces the maximum question to comparing two numbers.',
           'If \\(A\\subseteq B\\), start from an arbitrary upper bound of \\(B\\) and ask what it says about \\(A\\).',
           'If the distance were positive, choose \\(\\varepsilon\\) strictly smaller than that distance and contradict the hypothesis.'],
 'II/02': ['Write out the norm axioms one at a time; homogeneity and the triangle inequality are usually the decisive tests.',
           'Compute the distance from the norm definition before trying to visualize the geometry.',
           'Describe the unit ball by solving the inequality \\(\\|x\\|<1\\) in coordinates.',
           'Use the triangle inequality twice to obtain a reverse-triangle estimate for the difference of norms.',
           'In finite dimensions, compare each coordinate with the norm and then sum the coordinate bounds.',
           'To disprove a norm, test zero definiteness with a nonzero vector before attempting harder inequalities.',
           'Normalize a nonzero vector to reduce a general estimate to the unit sphere.',
           'Track constants explicitly when proving norm equivalence; the direction of each inequality matters.'],
 'II/03': ['For an \\(\\varepsilon\\)-\\(N\\) proof, solve the desired inequality for \\(n\\) before choosing \\(N\\).',
           'To show Cauchy behavior, estimate \\(|a_n-a_m|\\) uniformly for all \\(m,n\\) beyond the same index.',
           'If monotonicity and boundedness are available, identify the bound and invoke monotone convergence rather than guessing from '
           'numerics.',
           'Choose a subsequence by selecting indices where the sequence enters successively smaller neighborhoods of the proposed limit.',
           'Use the squeeze theorem only after producing upper and lower comparison sequences with the same limit.',
           'A convergent sequence is bounded; use this as a quick necessary-condition test for a proposed example.',
           'To separate convergence from Cauchy behavior, pay attention to whether the ambient space is complete.',
           'For an oscillating sequence, inspect even and odd subsequences before deciding whether a global limit exists.'],
 'II/04': ['Use the metric-ball definition directly: for each point of the set, find a radius whose ball stays inside.',
           'To prove closedness, work with the complement or show that every convergent sequence from the set has its limit in the set.',
           'A point is in the closure exactly when every ball around it meets the set; test this neighborhood condition.',
           'For a boundary point, show that every sufficiently small ball meets both the set and its complement.',
           'Arbitrary unions preserve openness because one containing open set already supplies the needed neighborhood.',
           'Finite intersections preserve openness by taking the minimum of finitely many available radii.',
           'For an infinite-intersection counterexample, let the open sets shrink toward a boundary point.',
           'Compute interior, closure, and boundary separately; do not infer one from a sketch alone.'],
 'II/05': ['For \\(\\varepsilon\\)-\\(\\delta\\) continuity, isolate \\(d(f(x),f(a))\\) and bound it by a constant times \\(d(x,a)\\) when '
           'possible.',
           'For sequential continuity, start with an arbitrary sequence \\(x_n\\to a\\) and push the convergence through the map.',
           'To prove uniform continuity, the chosen \\(\\delta\\) must depend only on \\(\\varepsilon\\), not on the base point.',
           'A Lipschitz estimate \\(d(f(x),f(y))\\le Ld(x,y)\\) immediately gives a uniform-continuity modulus.',
           "For composition, feed the outer map's \\(\\varepsilon\\)-requirement into the inner map's continuity estimate.",
           'To disprove uniform continuity, construct pairs whose inputs become arbitrarily close while their outputs stay separated.',
           'Use inverse images of open sets when the topology is easier to understand than direct metric estimates.',
           'On compact domains, combine continuity with compactness when a global estimate is needed.'],
 'II/06': ['In \\(\\mathbb R^n\\), check closedness and boundedness first; Heine--Borel then converts them to compactness.',
           'For sequential compactness, begin with an arbitrary sequence and construct a convergent subsequence.',
           'To show a continuous function attains a maximum, apply compactness to its image or to a maximizing sequence.',
           'A continuous image of a compact set is compact; use this before trying to prove boundedness directly.',
           'To disprove compactness, give either an open cover with no finite subcover or a sequence with no convergent subsequence.',
           'Closed subsets of compact spaces are compact; isolate the ambient compact set if one is available.',
           'Compact subsets of metric spaces are closed; separate a point outside the set using a positive distance argument.',
           'Do not use Heine--Borel outside finite-dimensional Euclidean space without checking that the theorem still applies.'],
 'II/07': ['To prove path connectedness, write an explicit continuous path \\(\\gamma:[0,1]\\to X\\) joining arbitrary endpoints.',
           'Path connectedness implies connectedness, so use a path construction if it is easier than a separation argument.',
           'To prove disconnectedness, exhibit two disjoint nonempty relatively open sets whose union is the whole set.',
           'Continuous images of connected sets are connected; map an interval onto the set when possible.',
           'An interval cannot be separated because an assumed gap would contradict the least-upper-bound property.',
           'For intermediate-value arguments, apply connectedness to the continuous image and use that connected subsets of \\(\\mathbb '
           'R\\) are intervals.',
           'To identify components, find maximal connected subsets rather than merely visually separate clusters.',
           'For a non-path-connected example, test whether every attempted path would force passage through a missing limit point.'],
 'II/08': ['Propose the derivative linear map first, then divide the remainder by \\(\\|h\\|\\) and show the quotient tends to zero.',
           'The Jacobian matrix represents the Fréchet derivative in standard coordinates; compute partial derivatives only after fixing '
           'the point.',
           'For the chain rule, compose the derivative maps in the same order as the functions.',
           'A directional derivative examines one line only; full differentiability requires one linear map to control all directions '
           'simultaneously.',
           'Use a norm estimate on the remainder term rather than checking coordinate limits separately.',
           'To disprove differentiability, compare the function along two paths or show the candidate linear approximation leaves a '
           'first-order remainder.',
           'For a scalar-valued function, identify the derivative with the gradient only after choosing the Euclidean inner product.',
           'If partial derivatives are continuous near the point, invoke the standard sufficient differentiability theorem instead of '
           'rebuilding the proof.'],
 'II/09': ['Compute \\(Df(a)\\) first and check whether it is an isomorphism; in coordinates this is the nonzero-Jacobian-determinant '
           'test.',
           'Differentiate \\(f^{-1}\\circ f=\\mathrm{id}\\) at the base point and solve the resulting linear identity for \\(D(f^{-1})\\).',
           'For \\(F(x,y)=0\\), compute the derivative only with respect to the variables you want to solve for and check that block for '
           'invertibility.',
           'After verifying \\(D_yF\\) is invertible, differentiate \\(F(x,g(x))=0\\) and solve the linear equation for \\(Dg\\).',
           'A nonsingular derivative gives only local invertibility; test global injectivity separately, for example by looking for '
           'periodicity or symmetry.',
           'If the derivative is singular, conclude only that the theorem does not apply; then inspect the equation directly before '
           'claiming nonexistence or nonuniqueness.',
           'For a regular level set, check surjectivity of the full derivative and identify which coordinate block can be used to graph '
           'the set locally.',
           'To connect the theorem with contraction mapping, normalize the derivative to the identity and estimate the nonlinear remainder '
           'on a sufficiently small ball.'],
 'II/10': ['Write the upper and lower sums from the suprema and infima on each subinterval; keep the partition lengths explicit.',
           'To prove integrability, aim directly at \\(U(f,P)-L(f,P)<\\varepsilon\\) rather than at the value of the integral.',
           'For a monotone function, bound the oscillation on each subinterval by endpoint differences and sum the resulting telescoping '
           'estimate.',
           'For a continuous function on a compact interval, use uniform continuity to make every subinterval oscillation small.',
           'Use additivity over adjacent intervals to reduce a complicated integral to simpler pieces.',
           'Comparison follows from comparing upper or lower sums term by term.',
           'To show nonintegrability, prove that every partition leaves a fixed positive gap between upper and lower sums.',
           'For a tagged Riemann-sum computation, separate the mesh-size estimate from the sample-point choice.'],
 'II/11': ['Pointwise convergence fixes \\(x\\) first; uniform convergence requires one index that works simultaneously for every \\(x\\).',
           'Compute or estimate \\(\\sup_x|f_n(x)-f(x)|\\); convergence of this supremum to zero is the direct uniform test.',
           'To disprove uniform convergence, choose points \\(x_n\\) depending on \\(n\\) where the error stays bounded away from zero.',
           'Uniform limits of continuous functions are continuous; if the proposed limit is discontinuous, uniform convergence is '
           'impossible.',
           'Use the uniform Cauchy criterion when the candidate limit is difficult to identify explicitly.',
           'Restricting the domain can turn nonuniform convergence into uniform convergence; inspect where the bad points accumulate.',
           'For monotone sequences of functions, do not infer uniform convergence without an additional theorem such as Dini under its '
           'hypotheses.',
           'Keep endpoint behavior separate from interior behavior when the convergence deteriorates near a boundary.'],
 'II/12': ['For interchanging limit and integral, identify a theorem whose hypotheses give uniform or dominated control before passing the '
           'limit.',
           'For derivative interchange, check uniform convergence of the derivative sequence and convergence at one base point.',
           'Integrate the derivative convergence from a fixed base point to reconstruct convergence of the functions.',
           'To build a counterexample, look for pointwise convergence with spikes or rapidly changing slopes that defeat uniform control.',
           'Estimate the remainder uniformly in the variable before moving a limit through an operation.',
           'Termwise differentiation is stronger than termwise integration; check the derivative hypotheses separately.',
           "Write the theorem's hypotheses next to the sequence at hand and verify each one explicitly.",
           'If only pointwise convergence is known, avoid exchanging operations until an additional bound or compactness argument supplies '
           'control.'],
 'II/13': ['For the M-test, dominate the absolute value of each term by a numerical sequence whose sum is known to converge.',
           'To find a power-series radius, apply the ratio or root test to the coefficient sequence and then inspect endpoints separately.',
           'For termwise integration, uniform convergence on the interval is the key safe route in this chapter.',
           'For termwise differentiation, control the derivative series uniformly and anchor the original series at one point.',
           'Estimate a series tail by comparison with a geometric or integral bound rather than summing many terms explicitly.',
           'Absolute convergence implies ordinary convergence, but the converse can fail; test signs and absolute values separately.',
           'To disprove uniform convergence, locate points where the tail does not become uniformly small.',
           'Use the Cauchy criterion for series when no closed-form sum is available.'],
 'II/14': ['Exploit parity first: even functions kill sine coefficients and odd functions kill cosine coefficients.',
           'Compute Fourier coefficients from their defining integrals over one period and simplify symmetry before integrating.',
           'At a jump, the standard convergence theorem gives the midpoint of the one-sided limits rather than either side value.',
           'Parseval converts an \\(L^2\\) norm into a sum of squared coefficients; verify normalization constants before applying it.',
           'Integrate by parts to obtain coefficient decay when the function has additional smoothness.',
           'Compare a trigonometric polynomial with a partial Fourier sum by matching coefficients.',
           'Check the period and normalization convention before copying any coefficient formula.',
           'For tail estimates, use coefficient decay or an \\(\\ell^2\\) identity rather than pointwise term estimates alone.'],
 'II/15': ['Isolate one scale of the construction where the oscillation is comparable to the increment under consideration.',
           'For a nowhere-differentiability argument, choose increments adapted to the series frequencies so one term dominates the '
           'difference quotient.',
           'Uniform convergence of the defining series proves continuity, not differentiability; analyze difference quotients separately.',
           'Split the series into low-frequency and high-frequency parts and estimate the two pieces differently.',
           'Use the modulus of continuity to record how oscillation changes with scale.',
           'To refute differentiability, produce two sequences of increments whose difference quotients cannot approach the same finite '
           'limit.',
           'Check whether termwise differentiation would require a derivative series that actually converges.',
           'Do not rely on a plot: convert visible oscillation into an explicit inequality at a chosen sequence of scales.'],
 'II/16': ['Compute a Lipschitz bound for \\(T\\) and verify the constant is strictly below one on the chosen domain.',
           'Check that the domain is complete and that \\(T\\) maps it into itself before invoking the contraction theorem.',
           'Use \\(d(x_n,x_*)\\le q^n d(x_0,x_*)\\) or the a posteriori geometric-tail estimate to quantify iteration error.',
           'If the global map is not contractive, restrict to a closed invariant subset where a sharper derivative or Lipschitz bound '
           'holds.',
           'Uniqueness follows by applying the contraction inequality to two hypothetical fixed points.',
           'To compare iterations, the smaller contraction factor gives the faster geometric asymptotic rate.',
           'If \\(q=1\\), the theorem no longer gives convergence or uniqueness; inspect a simple isometry as a counterexample.',
           'Completeness is used to ensure the Cauchy iterate sequence has a limit inside the space.'],
 'II/17': ['Check compactness, convexity, and continuity/self-map conditions explicitly before invoking Brouwer.',
           'In one dimension, apply the intermediate value theorem to \\(f(x)-x\\).',
           'Brouwer yields existence, not uniqueness; look for multiple fixed points before asserting more.',
           'To show convexity, verify that every segment \\((1-t)x+ty\\) stays in the set.',
           'For a noncompact counterexample, try a translation that moves every point while still mapping the space into itself.',
           'For a nonconvex domain, construct a rotation or swap that avoids fixed points.',
           'Compare with contraction mapping: a contraction supplies metric shrinkage and uniqueness, while Brouwer does not.',
           'When reducing to a finite-dimensional ball, make sure the map really sends the ball back into itself.'],
 'II/18': ['Move every term except the unknown function to one side and define an operator \\(Tu\\) whose fixed points solve the equation.',
           'Estimate \\(\\|Tu-Tv\\|_\\infty\\) by pulling \\(\\|u-v\\|_\\infty\\) outside the integral.',
           'Bound the integral kernel uniformly to obtain a contraction constant.',
           'Before iterating, check that the operator maps the selected closed ball or function class into itself.',
           'Picard iteration starts from any convenient initial function and repeatedly applies the integral operator.',
           'For an explicit kernel, differentiate the integral equation only when regularity justifies doing so.',
           'Existence and uniqueness are separate conclusions; identify exactly which estimate supplies each one.',
           'Use a geometric-series bound on successive differences to estimate the error after finitely many iterations.'],
 'II/19': ['Integrate the ODE from the initial time to rewrite it as \\(y(t)=y_0+\\int f(s,y(s))\\,ds\\).',
           'Estimate the derivative of \\(f\\) with respect to \\(y\\) on the chosen rectangle to obtain a local Lipschitz constant.',
           'Choose the time interval short enough that the Picard operator maps the function ball into itself and becomes a contraction.',
           'Compute the first few Picard iterates directly from the integral equation rather than differentiating them afterward.',
           'If uniqueness fails, look for a right-hand side that is continuous but not locally Lipschitz in \\(y\\).',
           'To detect finite-time blow-up, solve or compare with a scalar equation whose growth can be integrated explicitly.',
           'For stability, subtract the two integral equations and estimate the difference before applying a Grönwall-type bound if '
           'available.',
           'Keep the existence interval local unless you have an a priori bound preventing escape from the rectangle.'],
 'II/20': ['For two nodes, write the unique affine function through them before invoking any general interpolation machinery.',
           'A degree-at-most-\\(n\\) polynomial is determined by \\(n+1\\) distinct values because the difference of two candidates would '
           'have too many roots.',
           'Distinct nodes make the Vandermonde determinant nonzero; repeated nodes require extra derivative data instead.',
           'For a Lagrange basis polynomial, inspect its factors at each node to obtain the Kronecker-delta values.',
           'The node polynomial has one linear factor for each interpolation node; count those factors to get its degree.',
           'Uniqueness is a root-counting argument: a nonzero polynomial cannot have more roots than its degree.',
           'Interpolation is exact at the nodes but may oscillate badly between them; inspect the remainder and the node placement.',
           'Newton form is incremental because adding one node appends one new product term without changing the previous coefficients.'],
 'II/21': ['Separate existence of a polynomial approximant from construction of a specific interpolant; these are different problems.',
           'Check continuity on a compact interval before invoking the uniform polynomial approximation theorem.',
           'Use the modulus of continuity to convert closeness of nearby arguments into a uniform function-value estimate.',
           'If a constructive approximant is given, estimate its error directly in the sup norm.',
           'Density means every \\(\\varepsilon>0\\) admits some polynomial approximant; do not confuse this with convergence of one fixed '
           'sequence unless specified.',
           'Compare the approximating polynomial with the target on the whole interval, not only at selected nodes.',
           'Additional smoothness can improve rates, but uniform approximability of continuous functions does not require '
           'differentiability.',
           'To disprove an overstrong claim, choose a continuous function with limited smoothness and test the asserted rate rather than '
           'the existence theorem.'],
 'II/22': ['Write the error function \\(e=f-p\\) and locate its largest positive and negative values before adjusting the approximant.',
           'For a constant best approximant, balance the maximum positive and negative errors.',
           'Chebyshev polynomials are extremal because they oscillate with equal magnitude; scale them to the required leading '
           'coefficient.',
           "To certify optimality, derive a lower bound on every competitor's maximum error and show the candidate attains it.",
           'Interpolation need not be minimax; compare its sup error with an equioscillating competitor.',
           'Normalize the interval to \\([-1,1]\\) before applying standard Chebyshev formulas.',
           'Count alternating extreme points in the error curve; insufficient alternation suggests the approximation can still be '
           'improved.',
           'Use symmetry of the target function to reduce the possible form of a best approximating polynomial.'],
 'II/23': ['Form the error \\(e=f-p\\) and list its ordered extreme points with their signs.',
           "For degree \\(n\\), look for at least \\(n+2\\) alternating extreme errors under the theorem's hypotheses.",
           'To prove optimality, suppose a better approximant exists and examine the sign changes of the difference of the two '
           'approximants.',
           'Too many sign changes force a low-degree polynomial difference to have too many zeros.',
           'If alternation is missing, perturb the candidate in a direction that lowers the largest errors without enlarging the others.',
           'Keep the extrema ordered along the interval; alternation is not merely a count of positive and negative values.',
           'Use symmetry to predict where alternating extrema should occur in low-degree examples.',
           'Check that the error magnitudes at the alternating points are equal before invoking the certification theorem.'],
 'II/24': ['Derive the quadrature weights by integrating the interpolating basis polynomials, not by memorizing the rule.',
           'Test degree of exactness on monomials \\(1,x,x^2,\\ldots\\) until the first failure.',
           'For an error estimate, insert the derivative bound into the interpolation or Peano-type remainder formula.',
           'Exploit symmetry of the rule and interval to eliminate odd terms when possible.',
           'For a composite rule, apply the local error bound on each subinterval and then sum the contributions.',
           'Express the mesh width \\(h\\) in terms of the number of panels before solving the tolerance inequality.',
           'Compare rules at the same step size using their order and the size of the relevant derivative.',
           "Check whether the formula's node/weight pattern requires an even number of subintervals, as in composite Simpson-type rules."],
 'II/25': ['Generate convergents recursively from numerator and denominator recurrences rather than expanding nested fractions from '
           'scratch.',
           'For a rational number, apply the Euclidean algorithm; the quotients are the finite continued-fraction coefficients.',
           'Use the determinant identity for consecutive convergents to control their difference and relative primeness.',
           'Write the error between the irrational number and a convergent in terms of the next tail of the continued fraction.',
           'Consecutive convergents alternate around the target in the standard simple continued-fraction setting; check parity.',
           'Compare denominators before comparing approximation quality: continued fractions optimize error relative to denominator size.',
           'A rational continued fraction terminates; an irrational simple continued fraction does not.',
           'When proving a best-approximation statement, state the denominator restriction explicitly before comparing competitors.']}

GENERIC_HINT_FRAGMENTS = (
    "identify the definition or structural theorem",
    "use the chapter method",
    "use the central definitions",
)

TRIAD = re.compile(
    r"(\\begin\{exercise\}\\label\{(?P<label>exr:ii(?P<ch>\d{2})-(?P<idx>\d{2}))\}(?P<exercise>.*?)\\end\{exercise\}\s*)"
    r"(\\begin\{hint\}(?P<hint>.*?)\\end\{hint\}\s*)"
    r"(\\begin\{solution\}(?P<solution>.*?)\\end\{solution\})",
    re.S,
)

def read_status(repo: Path):
    with (repo/"editorial/CHAPTER_STATUS.tsv").open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def paths_for_volume(repo: Path):
    result={}
    for row in read_status(repo):
        code=(row.get("chapter_code") or "").strip()
        if code in GOALS:
            if row.get("status")!="FROZEN" or row.get("next_action")!="COMPLETE":
                raise RuntimeError(f"{code}: expected FROZEN/COMPLETE")
            result[code]=repo/row["canonical_path"]
    missing=sorted(set(GOALS)-set(result))
    if missing:
        raise RuntimeError(f"missing Volume II chapters: {missing}")
    return result

def replace_goals(text: str, code: str) -> str:
    block=[
        r"\section*{Learning goals}",
        "After this chapter, the reader should be able to:",
        r"\begin{itemize}",
    ]
    block += [rf"\item {g}" for g in GOALS[code]]
    block += [r"\end{itemize}", ""]
    replacement="\n".join(block)
    pattern=re.compile(
        r"\\section\*\{Learning goals\}.*?(?=\\section\*\{Conceptual roadmap\})",
        re.S
    )
    if not pattern.search(text):
        raise RuntimeError(f"{code}: learning-goals block not found")
    return pattern.sub(lambda m: replacement,text,count=1)

def clean_hint(h: str) -> str:
    h=re.sub(r"%.*","",h)
    h=re.sub(r"\\[a-zA-Z]+\{([^{}]*)\}",r"\1",h)
    h=re.sub(r"\s+"," ",h).strip()
    return h

def useful_seed(seed: str) -> bool:
    s=seed.lower().strip(" .:;!?")
    if not s or s in {"yes","no","definition","theorem","formula","compute directly"}:
        return False
    return not any(frag in s for frag in GENERIC_HINT_FRAGMENTS)

def compose_hint(code: str, idx: int, old_hint: str) -> str:
    method=METHODS[code][idx-1]
    seed=clean_hint(old_hint)
    if useful_seed(seed):
        if seed[-1] not in ".!?":
            seed += "."
        return seed + " " + method
    return method

def replace_hints(text: str, code: str) -> tuple[str,int]:
    count=0
    chnum=int(code.split("/")[1])
    def repl(m):
        nonlocal count
        if int(m.group("ch"))!=chnum:
            return m.group(0)
        idx=int(m.group("idx"))
        hint=compose_hint(code,idx,m.group("hint"))
        count += 1
        return (
            m.group(1)
            + "\\begin{hint}\n"
            + hint
            + "\n\\end{hint}\n"
            + m.group(8)
        )
    out=TRIAD.sub(repl,text)
    return out,count

def apply(repo: Path, mode: str, start: int, end: int):
    paths=paths_for_volume(repo)
    summary=[]
    for n in range(start,end+1):
        code=f"II/{n:02d}"
        p=paths[code]
        text=p.read_text(encoding="utf-8-sig")
        before=text
        hints=0
        if mode in ("goals","all"):
            text=replace_goals(text,code)
        if mode in ("hints","all"):
            text,hints=replace_hints(text,code)
            if hints!=8:
                raise RuntimeError(f"{code}: expected 8 exercise hints, replaced {hints}")
        if text!=before:
            p.write_text(text.rstrip()+"\n",encoding="utf-8")
        summary.append({"chapter_code":code,"changed":text!=before,"hints_replaced":hints})
    print(json.dumps(summary,indent=2,ensure_ascii=False))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--mode",choices=("goals","hints","all"),required=True)
    ap.add_argument("--start",type=int,default=1)
    ap.add_argument("--end",type=int,default=25)
    args=ap.parse_args()
    apply(Path(args.repo).resolve(),args.mode,args.start,args.end)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
