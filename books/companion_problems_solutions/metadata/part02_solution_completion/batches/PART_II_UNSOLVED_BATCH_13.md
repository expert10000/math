# Part II missing-solution batch 13

- problems: **20**
- IDs: CP-II-0263, CP-II-0266, CP-II-0270, CP-II-0272, CP-II-0274, CP-II-0275, CP-II-0277, CP-II-0284, CP-II-0285, CP-II-0287, CP-II-0288, CP-II-0290, CP-II-0292, CP-II-0294, CP-II-0295, CP-II-0296, CP-II-0302, CP-II-0306, CP-II-0307, CP-II-0308

## CP-II-0263

- chapter line: 15978

```tex
\label{prob:cp-ii-0263}
\par\noindent\textbullet\quad Choose an orthonormal sequence $(e_i)_{i\ge1}\subset H$.
		Then for every $y\in H$,
		$\langle y,e_i\rangle\to0$ by BesselĂ˘â‚¬â„˘s inequality,
		hence $e_i\rightharpoonup0$.
		However $\|e_i\|=1$ for all $i$,
		so $e_i\nrightarrow0$ in norm.
```

## CP-II-0266

- chapter line: 16020

```tex
\label{prob:cp-ii-0266}
— Smooth Approximation of a Periodic $L^p$ Function

Let $f\in L^p_{\mathrm{loc}}(\mathbb{R}^n)$ be periodic.
Define the cubes
\[
Q = \{x : |x_j|<1\}, \qquad q = \{x : |x_j|<\tfrac12\}.
\]

\bigskip
\noindent\textbf{(a) Construction of $h_\varepsilon$}

Choose $\chi\in C_c^\infty(\mathbb{R}^n)$ with
$\chi\equiv 1$ on $q$ and $\operatorname{supp}\chi \subset Q$.
Set $g := f\chi$. Then $\operatorname{supp}g \subset Q$ and $g=f$ on $q$.

Since $C_c^\infty$ is dense in $L^p$, choose $h_\varepsilon\in C^\infty$ with
$\operatorname{supp}h_\varepsilon\subset Q$ and
\[
\|g - h_\varepsilon\|_{L^p(\mathbb{R}^n)} < \varepsilon.
\]
But $f1_q = g$, so
\[
\|f1_q - h_\varepsilon\|_{L^p(\mathbb{R}^n)} < \varepsilon.
\]

\bigskip
Define
\[
f_\varepsilon(x) := \sum_{g\in\mathbb{Z}^n} h_\varepsilon(x-g)
= \sum_{g\in\mathbb{Z}^n} \tau_g h_\varepsilon(x).
\]

\bigskip
\noindent\textbf{(b) $f_\varepsilon$ is smooth and periodic}

Since $\operatorname{supp}h_\varepsilon\subset Q$, at each $x$ only finitely many terms are nonzero.
Thus $f_\varepsilon\in C^\infty(\mathbb{R}^n)$.

For periodicity:
\[
f_\varepsilon(x+k)
= \sum_{g} h_\varepsilon(x+k-g)
= \sum_{h} h_\varepsilon(x-h)
= f_\varepsilon(x),
\]
after substituting $h=g-k$.
Thus $f_\varepsilon$ is $\mathbb{Z}^n$-periodic.

\bigskip
\noindent\textbf{(c) Estimate on $q$}

If $x\in q$ and $h_\varepsilon(x-g)\neq 0$, then $x-g\in Q$, so $g$ lies in the finite set
\[
G = \{g\in\mathbb{Z}^n : (Q+g)\cap q \neq \emptyset\}.
\]
Thus
\[
f_\varepsilon(x) = \sum_{g\in G} h_\varepsilon(x-g).
\]

Since $f$ is periodic,
\[
f(x-g)=f(x),
\]
and by translation invariance,
\[
\|f1_q - h_\varepsilon(\cdot - g)\|_{L^p(\mathbb{R}^n)} < \varepsilon,
\quad g\in G.
\]

On $q$,
\[
f(x)-f_\varepsilon(x)
= \sum_{g\in G} \bigl(f(x) - h_\varepsilon(x-g)\bigr),
\]
so
\[
\|f - f_\varepsilon\|_{L^p(q)}
\le \sum_{g\in G} \|f - h_\varepsilon(\cdot-g)\|_{L^p(q)}
\le (\#G)\varepsilon.
\]

Let $c_n := \#G$. Then
\[
\|f - f_\varepsilon\|_{L^p(q)} < c_n \varepsilon.
\]
```

## CP-II-0270

- chapter line: 16217

```tex
\label{prob:cp-ii-0270}
\par\noindent (b)\quad Show $\mathbf 1_I\in\overline{\mathrm{Span}}\{\psi_{n,k}\}$ for every finite interval $I$ (closure in $L^2$).
```

## CP-II-0272

- chapter line: 16222

```tex
\label{prob:cp-ii-0272}
(b,c)

	\setcounter{enumi}{1}
	\par\noindent\textbullet\quad Along $te_2=(0,t)$,
	\[
	D_1 f(0,t)=t \;\;\Rightarrow\;\;\frac{D_1 f(0,t)-D_1 f(0,0)}{t}=1.
	\]
	Along $te_1=(t,0)$,
	\[
	D_2 f(t,0)=-t \;\;\Rightarrow\;\;\frac{D_2 f(t,0)-D_2 f(0,0)}{t}=-1.
	\]

	\par\noindent\textbullet\quad Hence
	\[
	D_2D_1 f(0)=1, \quad D_1D_2 f(0)=-1.
	\]
	So both exist, but are not equal.
```

## CP-II-0274

- chapter line: 16316

```tex
\label{prob:cp-ii-0274}
\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad Show that the inner product has the following properties for all $x,y,z\in\mathbb{R}^n$ and $a\in\mathbb{R}$:
\[
\langle x,y\rangle=\langle y,x\rangle,\qquad
\langle x+y,z\rangle=\langle x,z\rangle+\langle y,z\rangle,\qquad
\langle ax,y\rangle=a\langle x,y\rangle.
\]
\textit{Solution.} These follow from the Euclidean inner product $\langle x,y\rangle=\sum_{i=1}^n x_i y_i$.

\par\noindent\textbullet\quad For $t\in\mathbb{R}$ and $x,y\in\mathbb{R}^n$ show
\[
\|x+ty\|^2=\|x\|^2+2t\langle x,y\rangle+t^2\|y\|^2\ge 0.
\]
\textit{Solution.} Expand $\langle x+ty,x+ty\rangle$.

\par\noindent\textbullet\quad Deduce Cauchy--Schwarz: $|\langle x,y\rangle|\le \|x\|\,\|y\|$.\\
\textit{Solution.} View $\|x+ty\|^2$ as a quadratic in $t$ and use non-positivity of its discriminant.
Equality iff $x,y$ are linearly dependent.

\par\noindent\textbullet\quad Deduce the triangle inequality $\|x+y\|\le \|x\|+\|y\|$.

\par\noindent\textbullet\quad Show the reverse triangle inequality $|\|x\|-\|y\||\le \|x-y\|$.

\par\noindent\textbullet\quad Suppose $x=(x^1,\dots,x^n)^t$.

\renewcommand\labelenumii{(\roman{enumii})}
\par\noindent\textbullet\quad $\displaystyle \max_{k}|x^k|\le \|x\|$.
\par\noindent\textbullet\quad $\displaystyle \|x\|\le \sqrt{n}\,\max_{k}|x^k|$.

\textit{Solution.} Immediate from $\|x\|^2=\sum (x^i)^2$.
```

## CP-II-0275

- chapter line: 16350

```tex
\label{prob:cp-ii-0275}
\par\noindent\textbullet\quad Show that if $t \ge s$, then
	\[
	\|f\|_{H^{s}(\mathbb{R}^n)} \le \|f\|_{H^{t}(\mathbb{R}^n)}.
	\]
	Deduce that
	\[
	\|f\|_{L^2(\mathbb{R}^n)}
	\le \frac{1}{(2\pi)^{n/2}}\|f\|_{H^{s}(\mathbb{R}^n)}.
	\]
	\emph{Hint: Use Parseval's formula.}
```

## CP-II-0277

- chapter line: 16418

```tex
\label{prob:cp-ii-0277}
\par\noindent\textbullet\quad Show that \((3)\) admits a unique solution $u$ such that
	\[
	u \in C^0([0,T];H^2(\mathbb{R}^n)) \cap C^1((0,T);L^2(\mathbb{R}^n)),
	\]
	whose spatial Fourier–Plancherel transform is given by
	\[
	\widehat{u}(t,\xi) = \widehat{u_0}(\xi)\, e^{-it|\xi|^2}.
	\]
```

## CP-II-0284

- chapter line: 16553

```tex
\label{prob:cp-ii-0284}
\par\noindent\textbullet\quad If a real polynomial vanishes on an infinite subset of $[0,1]$ with a limit point in $[0,1]$,
	then it is identically zero (identity theorem for polynomials).
```

## CP-II-0285

- chapter line: 16559

```tex
\label{prob:cp-ii-0285}
\par\noindent\textbullet\quad \textbf{Linear rate.}
	For $\delta_n=\frac{1}{n+1}$, one has
	$\gamma_j=\frac{1}{j}-\frac{1}{j+1}=\frac{1}{j(j+1)}$ and
	\[
	f(x)=\sum_{j\ge1}\frac{1}{j(j+1)}\,T_{3j}(x),
	\qquad E_n(f)\ge\frac{1}{n+1}.
	\]
```

## CP-II-0287

- chapter line: 16570

```tex
\label{prob:cp-ii-0287}
\par\noindent\textbullet\quad The Hölder conjugate exponent $q$ of $p$ is defined by
	\[
	\frac{1}{p} + \frac{1}{q} = 1,
	\qquad 1 < p < \infty.
	\]
```

## CP-II-0288

- chapter line: 16579

```tex
\label{prob:cp-ii-0288}
\par\noindent\textbullet\quad \emph{Totally bounded}: for every $\varepsilon>0$, there exist $x_1,\dots,x_N\in X$ such that
	\[
	X \subset \bigcup_{i=1}^N B(x_i,\varepsilon).
	\]
```

## CP-II-0290

- chapter line: 16652

```tex
\label{prob:cp-ii-0290}
\par\noindent\textbullet\quad \textbf{Homogeneity:} $\|\alpha p\|_{I}=\sup_{t\in I}|\alpha||p(t)|=|\alpha|\,\|p\|_{I}$.
```

## CP-II-0292

- chapter line: 16657

```tex
\label{prob:cp-ii-0292}
\par\noindent\textbullet\quad all integrals reduce to finite sums;
```

## CP-II-0294

- chapter line: 16662

```tex
\label{prob:cp-ii-0294}
State whether the sequence $(f_i)_{i=0}^\infty$ of functions converges pointwise and/or uniformly.

\renewcommand\labelenumi{(\alph{enumi})}

\par\noindent\textbullet\quad $f_i:\mathbb{R}\to\mathbb{R}$, \; $f_i(x)=e^{x}+\dfrac{1}{i+1}$.

\textit{Solution.} For each $x$, $f_i(x)\to e^x$. Moreover
\[
\sup_{x\in\mathbb{R}} |f_i(x)-e^x|=\sup_{x\in\mathbb{R}}\frac{1}{i+1}=\frac{1}{i+1}\xrightarrow{i\to\infty}0,
\]
so $f_i\to e^x$ \emph{uniformly} on $\mathbb{R}$.

\par\noindent\textbullet\quad $f_i:\mathbb{R}\to\mathbb{R}$, \; $f_i(x)=x+2^{-i}x^2$.

\textit{Solution.} For fixed $x$, $f_i(x)\to x$. However
\[
\sup_{x\in\mathbb{R}} |f_i(x)-x|=\sup_{x\in\mathbb{R}} 2^{-i}x^2=+\infty \quad \text{for every fixed } i,
\]
hence the convergence is \emph{not} uniform on $\mathbb{R}$.
(Nonetheless, on any bounded interval $[-M,M]$ the convergence is uniform since
$\sup_{|x|\le M} |f_i(x)-x|=2^{-i}M^2\to 0$.)

\par\noindent\textbullet\quad $f_i:[0,1]\to\mathbb{R}$ given by
\[
f_i(x)=
\begin{cases}
2^i x, & 0\le x<2^{-i},\\[2pt]
2-2^i x, & 2^{-i}\le x<2^{-(i-1)},\\[2pt]
0, & x\ge 2^{-(i-1)}.
\end{cases}
\]
\textit{Solution.} For every $x\in[0,1]$, $f_i(x)\to 0$ (as in Exercise 3.1). But
$\sup_{x\in[0,1]} f_i(x)=1$ for all $i$, so the convergence is \emph{not} uniform on $[0,1]$.
(On $[\delta,1]$ with $\delta>0$, the convergence is uniform.)
```

## CP-II-0295

- chapter line: 16700

```tex
\label{prob:cp-ii-0295}
\par\noindent\textbullet\quad $f(x,y)=x+y$ is Lipschitz in both variables and continuous.
```

## CP-II-0296

- chapter line: 16705

```tex
\label{prob:cp-ii-0296}
Quickies on norms

Two norms $\|\cdot\|,\|\cdot\|'$ on $V$ are Lipschitz equivalent iff there exist $r,R>0$ with
	$B_r\subseteq B_1'\subseteq B_R$, where $B_\rho=\{x:\|x\|<\rho\}$, $B'_\rho=\{x:\|x\|'<\rho\}$.
	Indeed, $c\|x\|\le \|x\|'\le C\|x\|$ implies the inclusions with $r=1/C$, $R=1/c$;
	conversely the inclusions give $\|x\|'\le (1/r)\|x\|$ and $\|x\|\le R\|x\|'$.

	The bounds $c\|x\|\le \|x\|'\le C\|x\|$ imply
	$\|x_n-x\|\to0 \Leftrightarrow \|x_n-x\|'\to0$. Conversely, if this fails, one can find
	$\|x_k\|=1$ with $\|x_k\|'\to\infty$; then $y_k=x_k/k$ satisfies $y_k\to0$ in $\|\cdot\|$
	but not in $\|\cdot\|'$.

	It is a norm. If $\varphi$ is not continuous, there are $x_k$ with $\|x_k\|=1$ and
	$|\varphi(x_k)|\to\infty$, hence $\|x_k\|_\varphi\to\infty$, so no inequality
	$\|x\|_\varphi\le C\|x\|$ holds; thus $\|\cdot\|_\varphi$ is not Lipschitz equivalent to $\|\cdot\|$.

	If every norm on $V$ is Lipschitz equivalent to $\|\cdot\|$, then $V$ must be finite-dimensional.
	Otherwise there exists a discontinuous linear functional $\varphi$ on $V$, and by (c) the norm
	$\|x\|+|\varphi(x)|$ would not be equivalent to $\|\cdot\|$.

	\bigskip
```

## CP-II-0302

- chapter line: 16730

```tex
\label{prob:cp-ii-0302}
\par\noindent\textbullet\quad If $(S_n)$ bounded and $x^n$ monotone $\downarrow 0$, then $\sum a_n x^n$ converges (Dirichlet).
```

## CP-II-0306

- chapter line: 16735

```tex
\label{prob:cp-ii-0306}
\par\noindent\textbullet\quad \textbf{Practical diagnostics.}
	Sampling only at $\{x_k\}$ detects the worst-case error and guides adaptive refinement.
```

## CP-II-0307

- chapter line: 16741

```tex
\label{prob:cp-ii-0307}
Which of the following subsets of $\mathbb{R}^n$ is open?

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad $\mathbb{R}^n$: \textbf{Yes}.
\par\noindent\textbullet\quad $\varnothing$: \textbf{Yes}.
\par\noindent\textbullet\quad $\{x\in\mathbb{R}^n:x^1>0\}$: \textbf{Yes}.
\par\noindent\textbullet\quad $\{x\in\mathbb{R}^n:x^i\in[0,1]\}$: \textbf{No}.
\par\noindent\textbullet\quad $\mathbb{Q}^n$: \textbf{No}.
```

## CP-II-0308

- chapter line: 16753

```tex
\label{prob:cp-ii-0308}
Let $(x_i)$ and $(y_i)$ in $\mathbb{R}^n$ satisfy $x_i\to x$, $y_i\to y$.

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad $x_i+y_i\to x+y$. \textit{Proof.} $\|(x_i+y_i)-(x+y)\|\le \|x_i-x\|+\|y_i-y\|\to 0$.
\par\noindent\textbullet\quad $\langle x_i,y_i\rangle\to \langle x,y\rangle$; in particular $\|x_i\|\to \|x\|$.\\
\textit{Proof.} Expand $\langle x_i,y_i\rangle-\langle x,y\rangle$ and use Cauchy--Schwarz.
\par\noindent\textbullet\quad If $a_i\to a$ in $\mathbb{R}$, then $a_i x_i\to ax$.\\
\textit{Proof.} $a_ix_i-ax=(a_i-a)(x_i-x)+(a_i-a)x+a(x_i-x)$.
```
