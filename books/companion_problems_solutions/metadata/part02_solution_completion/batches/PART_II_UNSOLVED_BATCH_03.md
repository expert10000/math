# Part II missing-solution batch 03

- problems: **20**
- IDs: CP-II-0282, CP-II-0286, CP-II-0291, CP-II-0293, CP-II-0297, CP-II-0300, CP-II-0303, CP-II-0304, CP-II-0309, CP-II-0310, CP-II-0321, CP-II-0323, CP-II-0326, CP-II-0330, CP-II-0332, CP-II-0333, CP-II-0334, CP-II-0357, CP-II-0365, CP-II-0367

## CP-II-0282

- chapter line: 4379

```tex
\label{prob:cp-ii-0282}
Diagonals and Equality Sets

Let $(X,\tau)$ and $(Y,\rho)$ be topological spaces with $(Y,\rho)$ Hausdorff.

	\par\medskip\noindent\textbf{Statement.}\
		Show that $\Delta=\{(y,y):y\in Y\}\subset Y\times Y$ is closed (product topology).
	\par

	\begin{proof}
		Let $(y_1,y_2)\in (Y\times Y)\setminus\Delta$, so $y_1\ne y_2$. Since $Y$ is Hausdorff, there exist disjoint open sets $U\ni y_1$ and $V\ni y_2$ with $U\cap V=\varnothing$. Then
		\[
		(y_1,y_2)\in U\times V \subset (Y\times Y)\setminus \Delta,
		\]
		because for any $(u,v)\in U\times V$ we cannot have $u=v$ (that would force $u\in U\cap V=\varnothing$). Hence $(Y\times Y)\setminus \Delta$ is open and $\Delta$ is closed.
	\end{proof}

	\begin{remark}
		The converse holds: $Y$ is Hausdorff if and only if $\Delta$ is closed in $Y\times Y$.
	\end{remark}

	\par\medskip\noindent\textbf{Statement.}\
		Let $f,g:X\to Y$ be continuous. Show that $E=\{x\in X:\ f(x)=g(x)\}$ is closed in $X$.
	\par

	\begin{proof}
		Consider $F=(f,g):X\to Y\times Y$, which is continuous in the product topology. Then
		\[
		E=F^{-1}(\Delta).
		\]
		By part (a), $\Delta$ is closed in $Y\times Y$, hence $E$ is the preimage of a closed set under a continuous map and is therefore closed in $X$.
	\end{proof}

		\par\noindent\textbullet\quad If $Y=\mathbb{R}$ and $f,g:X\to\mathbb{R}$ are continuous, then
		\[
		E=\{x:\ f(x)=g(x)\}=(f-g)^{-1}(\{0\}),
		\]
		which is closed since $\{0\}$ is closed and $f-g$ is continuous.
		\par\noindent\textbullet\quad On $X=\mathbb{R}$, $f(x)=x^3-1$ and $g(x)=x-1$ give $E=\{1\}$, a closed set.

	Let $Y=\{a,b\}$ with the indiscrete topology. Then $Y$ is not Hausdorff and $\Delta\subset Y\times Y$ is not closed. Take any space $X$ and a non-closed set $A\subset X$ (e.g.\ $X=\mathbb{R}$, $A=(0,1)$). Define
	\[
	f(x)\equiv a,\qquad
	g(x)=\begin{cases}
		a,& x\in A,\\
		b,& x\notin A.
	\end{cases}
	\]
	Every map into an indiscrete space is continuous, so $f,g$ are continuous. But
	$E=\{x:\ f(x)=g(x)\}=A$, which is not closed. Thus the Hausdorff hypothesis in (b) is essential.

	Let $X$ be a topological space and $\Delta_X=\{(x,x):x\in X\}\subseteq X\times X$ its diagonal.

		\par\noindent\textbullet\quad $X$ is \emph{Hausdorff} $\iff$ $\Delta_X$ is \emph{closed} in $X\times X$.
		\par\noindent\textbullet\quad $X$ has a \emph{$G_\delta$-diagonal} if there exist open sets $U_n\subseteq X\times X$ such that
		\[
		\Delta_X=\bigcap_{n=1}^\infty U_n .
		\]

		\par\noindent\textbullet\quad \textbf{Metric spaces have $G_\delta$-diagonals.}
		If $(X,d)$ is metric, the function $(x,y)\mapsto d(x,y)$ is continuous on $X\times X$, hence
		\[
		\Delta_X=\bigcap_{m=1}^{\infty}\bigl\{(x,y)\in X\times X: d(x,y)<1/m\bigr\}
		\]
		is a $G_\delta$ subset of $X\times X$.
		\par\noindent\textbullet\quad \textbf{First countable Hausdorff $\Rightarrow G_\delta$-diagonal.}
		If $X$ is Hausdorff and for each $x\in X$ there is a countable neighborhood base $\{B_n(x)\}_{n\in\mathbb{N}}$, then
		\[
		U_n=\bigcup_{x\in X} B_n(x)\times B_n(x)\qquad(n\in\mathbb{N})
		\]
		are open in $X\times X$ and $\Delta_X=\bigcap_{n} U_n$.
		\par\noindent\textbullet\quad \textbf{SneiderĂ˘â‚¬â„˘s Theorem (compact case).}
		A compact Hausdorff space $K$ is metrizable if and only if $\Delta_K$ is a $G_\delta$ in $K\times K$.

		\par\noindent\textbullet\quad $\mathbb{R}^n$ with its Euclidean topology: Hausdorff and metric $\Rightarrow$ $\Delta$ is closed and a $G_\delta$.
		\par\noindent\textbullet\quad Any compact metrizable space (e.g.\ the Cantor set, the $n$-torus $(S^1)^n$) has a $G_\delta$-diagonal.
		\par\noindent\textbullet\quad The Niemytzki (Moore) plane: Hausdorff and first countable, hence has a $G_\delta$-diagonal, but is not normal; consequently not metrizable.

		\par\noindent\textbullet\quad For uncountable $I$, the Tikhonoff cube $[0,1]^I$ is compact Hausdorff but not metrizable; hence by Sneider, $\Delta_{[0,1]^I}$ is \emph{not} a $G_\delta$ in $[0,1]^I\times[0,1]^I$.
		\par\noindent\textbullet\quad The indiscrete space on $\{a,b\}$ is not Hausdorff; $\Delta$ is not closed (and not $G_\delta$).
		\par\noindent\textbullet\quad The cofinite topology on an infinite set is $T_1$ but not Hausdorff; $\Delta$ is not closed (hence not $G_\delta$).
```

## CP-II-0286

- chapter line: 4463

```tex
\label{prob:cp-ii-0286}
— Smoothness and bounds for $\widehat f$ with compact support

Let $f\in L^1(\mathbb R^n)$ with $\operatorname{supp}f\subset B_R(0)$ for some $R>0$.
Show that $\widehat f\in C^\infty(\mathbb R^n)$ and that, for every multi-index $\alpha$,
\[
\sup_{\xi\in\mathbb R^n}\big|D_\xi^\alpha \widehat f(\xi)\big|
\;\le\; R^{|\alpha|}\,\|f\|_{L^1}.
\]
```

## CP-II-0291

- chapter line: 4475

```tex
\label{prob:cp-ii-0291}
— Distributions with zero derivative are constants

Suppose \(u\in\mathcal D'(\mathbb R)\) satisfies \(Du=0\). Show that there exists \(\lambda\in\mathbb C\) such that
\[
u[\phi]=\lambda\int_{\mathbb R}\phi(x)\,dx,\qquad\forall\,\phi\in\mathcal D(\mathbb R).
\]
\emph{(Extend the result to \(\mathbb R^n\) for \(n>1\)).}

The hypothesis \(Du=0\) means \(u[\phi']=0\) for all \(\phi\in\mathcal D(\mathbb R)\).
Fix \(\phi_0\in\mathcal D(\mathbb R)\) with \(\int_{\mathbb R}\phi_0=1\). For any \(\phi\in\mathcal D(\mathbb R)\), set \(c_\phi=\int_{\mathbb R}\phi\) and define
\[
\psi(x)=\int_{-\infty}^x\big(\phi(t)-c_\phi\phi_0(t)\big)\,dt.
\]
Then \(\psi\in\mathcal D(\mathbb R)\) and \(\psi'=\phi-c_\phi\phi_0\). Therefore
\[
u[\phi]=u[\psi']+c_\phi\,u[\phi_0]=c_\phi\,u[\phi_0]=\lambda\int_{\mathbb R}\phi,
\]
with \(\lambda:=u[\phi_0]\).

If \(D_j u=0\) for all \(j=1,\dots,n\), then \(u[\partial_j\phi]=0\) for all \(\phi\in\mathcal D(\mathbb R^n)\).
Choose \(\phi_0\in\mathcal D(\mathbb R^n)\) with \(\int\phi_0=1\).

 For any \(\phi\), write \(\phi=\nabla\cdot F+c_\phi\phi_0\) with \(c_\phi=\int\phi\) and \(F\in\mathcal D(\mathbb R^n;\mathbb C^n)\) such that \(\nabla\cdot F=\phi-c_\phi\phi_0\) (possible because the right-hand side has integral \(0\)).

 Then
\[
u[\phi]=u[\nabla\cdot F]+c_\phi\,u[\phi_0]=\lambda\int_{\mathbb R^n}\phi.
\]

If \(u\) is induced by \(f\in L^1_{\mathrm{loc}}(\mathbb R)\), then \(Du=0\) implies \(f' = 0\) in the distributional sense, hence \(f\) is a.e.\ constant and \(u[\phi]=\lambda\int\phi\).
By contrast, \(D\delta\ne0\), since \(D\delta[\phi]=-\phi'(0)\).

Let $X$ be a locally convex space over $\mathbb K$ and let $X'$ denote its continuous dual.
The weak-$^\ast$ topology on $X'$, denoted $\sigma(X',X)$, is the coarsest topology on $X'$ for which every evaluation map
\[
e_x:X'\to\mathbb K,\qquad e_x(f)=f(x)\quad(x\in X),
\]
is continuous. Equivalently, it is the initial topology induced by the family $\{e_x:x\in X\}$.

\bigskip

A net $(f_\alpha)\subset X'$ converges to $f\in X'$ in $\sigma(X',X)$ if and only if
\[
f_\alpha(x)\longrightarrow f(x)\qquad\text{for every }x\in X.
\]

\smallskip

For $x\in X$ and an open set $U\subset\mathbb K$, the sets
\[
e_x^{-1}(U)=\{\,f\in X':\ f(x)\in U\,\}
\]
form a subbasis. A typical $0$-neighborhood is
\[
V(x_1,\dots,x_m;\varepsilon)
=\bigl\{\,f\in X':\ |f(x_j)|<\varepsilon\ \text{for }j=1,\dots,m\,\bigr\}.
\]

\smallskip

If $X$ is normed, the closed unit ball of $X'$ is compact in $\sigma(X',X)$ (Banach--Alaoglu).
If $X$ is separable, the weak-$^\ast$ topology is metrizible on norm-bounded subsets of $X'$.
The weak topology on $X$ is $\sigma(X,X')$, while the weak-$^\ast$ topology on $X'$ is $\sigma(X',X)$.
The canonical embedding $J:X\to X''$ is weak-to-weak-$^\ast$ continuous; it is onto if and only if $X$ is reflexive.

\smallskip

For $X=\ell^1$ and $X'=\ell^\infty$, $\sigma(\ell^\infty,\ell^1)$ is pointwise convergence on $\ell^1$:
$y^{(\alpha)}\to y$ iff $\sum_k y^{(\alpha)}_k x_k\to\sum_k y_k x_k$ for all $x\in\ell^1$.

For $X=C_0(\Omega)$ (locally compact Hausdorff), $X'=M(\Omega)$; the topology $\sigma(M(\Omega),C_0(\Omega))$
is narrow convergence of measures: $\int f\,d\mu_\alpha\to\int f\,d\mu$ for all $f\in C_0(\Omega)$.

For distributions, $\sigma(\mathcal D'(\mathbb R^n),\mathcal D(\mathbb R^n))$ and
$\sigma(\mathcal S'(\mathbb R^n),\mathcal S(\mathbb R^n))$ coincide with test-functionwise convergence.
```

## CP-II-0293

- chapter line: 4554

```tex
\label{prob:cp-ii-0293}
A sequence $(x_i)\subset\mathbb{R}^n$ is Cauchy if $\forall\varepsilon>0\,\exists N:\ i,j\ge N\Rightarrow \|x_i-x_j\|<\varepsilon$.

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad If $x_i\to x$, then $(x_i)$ is Cauchy. \textit{Proof.} Triangle inequality with $\varepsilon/2$.
\par\noindent\textbullet\quad If $(x_i)$ is Cauchy, then it is bounded. \textit{Proof.} Take $\varepsilon=1$.
\par\noindent\textbullet\quad Every Cauchy sequence in $\mathbb{R}^n$ converges. \textit{Proof.} Bounded $\Rightarrow$ has a convergent subsequence; use Cauchy property to pass to the full sequence.

\textbf{Remark.} In $\mathbb{R}$, $\mathbb{R}^n$, and $\mathbb{C}\cong\mathbb{R}^2$, a sequence is convergent iff it is Cauchy (completeness). In incomplete spaces (e.g.\ $\mathbb{Q}$), Cauchy does not imply convergent.
```

## CP-II-0297

- chapter line: 4566

```tex
\label{prob:cp-ii-0297}
\par\noindent\textbullet\quad If one takes $f_n(x)=\mathbf 1_{[0,1]}(x-n)$, it also works;
		all translations of the same shape have $\|f_n\|_1=1$ and no weak limit.

	Let $X$ be a topological space and $F:X\to(-\infty,+\infty]$.
```

## CP-II-0300

- chapter line: 4601

```tex
\label{prob:cp-ii-0300}
Let $K_1 \supset K_2 \supset K_3 \supset \cdots$ be a decreasing sequence of non-empty,
	connected, compact subsets of a Hausdorff space $X$.
	Let
	\[
	K = \bigcap_{n=1}^{\infty} K_n.
	\]

		\par\noindent\textbullet\quad Show that $K$ is non-empty.
		\par\noindent\textbullet\quad Show that $K$ is connected.
		\par\noindent\textbullet\quad Give an example with $X=\mathbb{R}^2$ showing that part (b)
		fails if the $K_n$ are only closed instead of compact.


	\textbf{Theory.}
	In any Hausdorff space, the intersection of a decreasing sequence
	of non-empty compact sets is non-empty (finite intersection property).
	Connectedness is preserved under nested intersections of connected sets.
	Compactness is required for non-emptiness; without it, closed sets
	may shrink or split into disconnected limits.


	\textbf{Solutions.}

	\textit{(a) Non-emptiness.}
	Each $K_n$ is compact and non-empty, $K_{n+1}\subseteq K_n$.
	Thus the family $\{K_n\}$ has the finite intersection property.
	By compactness, $\bigcap_n K_n \neq \varnothing$.

	\medskip

	\textit{(b) Connectedness.}
	Assume $K=A\cup B$ with $A,B$ non-empty and disjoint, open in $K$.
	Then $A=U\cap K$, $B=V\cap K$ for some disjoint open $U,V\subset X$.
	For each $n$, $K_n=(K_n\cap U)\cup(K_n\cap V)$.
	Since $K_n$ is connected, one of these intersections is empty for all $n$.
	Hence one of $A,B$ is empty—contradiction. So $K$ is connected.

	\medskip

	\textit{(c) Failure without compactness.}
	Let $X=\mathbb{R}^2$ and define
	\[
	L_n=\{(x,y):y=\tfrac{1}{n}x,\ x>0\}
	\cup
	\{(x,y):y=-\tfrac{1}{n}x,\ x>0\}.
	\]
	Each $L_n$ is closed in $\mathbb{R}^2$ and connected.
	They form a decreasing sequence, but
	\[
	\bigcap_n L_n = \{(x,0):x>0\},
	\]
	which is disconnected in $\mathbb{R}^2$.
	Thus compactness (not mere closedness) is essential.


	\textbf{Summary.}

	\begin{center}
		\resizebox{\linewidth}{!}{%
		\begin{tabular}{c|l|c|l}
			Part & Statement & Result & Key Idea\\\hline
			(a) & $K$ non-empty & Yes & Nested compact sets $\Rightarrow$ finite intersection property\\
			(b) & $K$ connected & Yes & Intersection preserves connectedness\\
			(c) & Closed instead of compact & No & May lose connectedness (counterexample in $\mathbb{R}^2$)
		\end{tabular}}
	\end{center}

	\par\medskip\noindent\textbf{Problem 8 — Antipodal Points on the Circle (Borsuk–Ulam in 1D)}\par
```

## CP-II-0303

- chapter line: 4712

```tex
\label{prob:cp-ii-0303}
— Compactness and sequential compactness in $C[0,1]$

Let $C[0,1]$ be the metric space consisting of all continuous functions $f:[0,1]\to\mathbb{R}$,
with distance
\[
d(f,g)=\sup_{x\in[0,1]}|f(x)-g(x)|.
\]

\bigskip

Let $h(x)=|f(x)-g(x)|$. Since $h$ is continuous on the compact interval $[0,1]$,
the Extreme Value Theorem ensures that $h$ attains its maximum and minimum values.
Therefore
\[
d(f,g)=\sup_{x\in[0,1]}|f(x)-g(x)|=\max_{x\in[0,1]}|f(x)-g(x)|.
\]

\bigskip

Let
\[
X=\{\, f\in C[0,1] : f([0,1])\subseteq[0,1]\,\}.
\]
Consider the sequence $f_n(x)=x^n$ for $x\in[0,1]$.
Each $f_n$ lies in $X$ because $x^n\in[0,1]$ for $x\in[0,1]$.

For any fixed $x\in[0,1)$, $f_n(x)=x^n\to 0$, while $f_n(1)=1$.
Hence $f_n$ converges pointwise to
\[
f(x)=
\begin{cases}
	0, & 0\le x<1,\\[3pt]
	1, & x=1,
\end{cases}
\]
which is discontinuous at $x=1$.

Since the limit function is not continuous, the convergence cannot be uniform.
No subsequence can converge uniformly either (every subsequence has the same pointwise limit).
Thus $(f_n)$ has no convergent subsequence in $C[0,1]$ under $d(f,g)=\|f-g\|_\infty$.

Therefore $X$ is not sequentially compact.

\bigskip

In metric spaces, compactness $\Leftrightarrow$ sequential compactness,
so $X$ is not compact. Nevertheless, we can give an explicit open cover with no finite subcover.

For each $n\in\mathbb{N}$, define
\[
U_n = \{\, f\in X : f(1) > 1 - \tfrac{1}{n} \,\}.
\]
Each $U_n$ is open in the sup-norm topology.
The collection $\{U_n : n\in\mathbb{N}\}$ covers $X$, since for every $f\in X$,
$f(1)\in[0,1]$ so $f(1)>1-1/n$ for some $n$.

However, no finite subcollection covers $X$.
If $U_{n_1},\dots,U_{n_k}$ are finitely many, let $N=\max\{n_i\}$.
Then the constant function $f(x)\equiv 1-\tfrac{1}{2N}$ lies in $X$ but satisfies
$f(1)=1-\tfrac{1}{2N}<1-\tfrac{1}{N}$, hence $f\notin U_N$.
Thus this cover has no finite subcover.

\bigskip

	\par\noindent\textbullet\quad The sequence $f_n(x)=x^n$ is a classical example in $C[0,1]$ showing failure of compactness.
	\par\noindent\textbullet\quad The family $X$ is bounded and closed but not equicontinuous; by the Arzelà–Ascoli theorem it is not relatively compact.
	\par\noindent\textbullet\quad $C[0,1]$ with $\|\cdot\|_\infty$ is complete but infinite-dimensional, hence non-compact.

\noindent\textbf{Definitions.}
For $S\subset\mathbb{R}$:

	\par\noindent\textbullet\quad The \emph{maximum} $\max S$ is a number $m\in S$ with $s\le m$ for all $s\in S$.
	\par\noindent\textbullet\quad The \emph{supremum} $\sup S$ is the least upper bound: the smallest $\alpha\in\mathbb{R}$ such that $s\le \alpha$ for all $s\in S$.

If $\max S$ exists, then $\sup S=\max S$. The supremum need not belong to $S$.

\smallskip

\noindent\textbf{Examples.}

	\par\noindent\textbullet\quad $S=(0,1)$: $\sup S=1$ but $\max S$ does not exist (1 is not in $S$).
	\par\noindent\textbullet\quad $S=[0,1]$: $\sup S=\max S=1$ (attained).
	\par\noindent\textbullet\quad $S=\{1-\tfrac1n:n\in\mathbb{N}\}$: $\sup S=1$, no maximum (1 is only a limit point).
	\par\noindent\textbullet\quad $S=\{0,1,2,\dots,100\}$: $\sup S=\max S=100$.
	\par\noindent\textbullet\quad $S=(-\infty,0)$: $\sup S=0$, no maximum.

\smallskip

\noindent\textbf{For functions.}
If $f:[a,b]\to\mathbb{R}$ is continuous and $[a,b]$ is compact, then by the Extreme Value Theorem
\[
\sup_{x\in[a,b]} f(x) \;=\; \max_{x\in[a,b]} f(x).
\]
If the domain is not compact, or $f$ is not continuous, the supremum may fail to be attained:

	\par\noindent\textbullet\quad $f(x)=x$ on $(0,1)$: $\sup f=1$ but $f$ has no maximum.
	\par\noindent\textbullet\quad $f(x)=\sin x$ on $\bigl(-\tfrac{\pi}{2},\tfrac{\pi}{2}\bigr)$: $\sup f=1$ but no maximum (endpoints excluded).

\smallskip

\noindent\textbf{Application to $C[0,1]$.}
For $f,g\in C[0,1]$, the function $h(x)=|f(x)-g(x)|$ is continuous on the compact interval $[0,1]$.
Hence
\[
\sup_{x\in[0,1]} |f(x)-g(x)| \;=\; \max_{x\in[0,1]} |f(x)-g(x)|.
\]

\noindent\textbf{Statement.}
Let $K\subset\mathbb{R}^n$ be compact and let $f:K\to\mathbb{R}$ be continuous.
Then there exist points $x_{\min},x_{\max}\in K$ such that
\[
f(x_{\min})=\min_{x\in K} f(x), \qquad f(x_{\max})=\max_{x\in K} f(x).
\]
Equivalently,
\[
\sup_{x\in K} f(x)=\max_{x\in K} f(x), \qquad \inf_{x\in K} f(x)=\min_{x\in K} f(x).
\]

\smallskip

\noindent\textbf{Proof sketch.}
Let $M=\sup_{x\in K} f(x)$. Choose $x_n\in K$ with $f(x_n)\to M$.
By compactness, some subsequence $x_{n_k}\to x^*\in K$.
By continuity, $f(x^*)=\lim_{k\to\infty} f(x_{n_k})=M$, so the supremum is attained.
Apply the same argument to $-f$ to get a minimum.

\smallskip

\noindent\textbf{Why the hypotheses are needed.}

	\par\noindent\textbullet\quad If the domain is not compact, even continuous functions may fail to attain extrema:
	$f(x)=x$ on $(0,1)$ has $\sup=1$ but no maximum.
	\par\noindent\textbullet\quad If $f$ is not continuous, attainment can fail even on compact sets (pathologies exist).

\bigskip

For $f,g\in C[0,1]$,

 set $h(x)=|f(x)-g(x)|$.

Then $h$ is continuous on the compact interval $[0,1]$.
By the EVT,
\[
\sup_{x\in[0,1]} |f(x)-g(x)| \;=\; \max_{x\in[0,1]} |f(x)-g(x)|.
\]
Hence the metric $d(f,g)=\sup_{x\in[0,1]}|f(x)-g(x)|$ is the maximum value of $|f-g|$ on $[0,1]$.

Let $X=\{f\in C[0,1]: 0\le f(x)\le 1 \text{ for all }x\in[0,1]\}$ with the sup norm.

\smallskip

\noindent\textbf{Define the cover.}
For each $n\in\mathbb{N}$ set
\[
U_n=\bigl\{\,f\in X:\ f(1)>1-\tfrac1n\,\bigr\}.
\]

\noindent\emph{$U_n$ is open.}
The evaluation functional $E_1:C[0,1]\to\mathbb{R}$, $E_1(f)=f(1)$, is continuous since
$|E_1(f)-E_1(g)|=|f(1)-g(1)|\le \|f-g\|_\infty$.
Thus $U_n=E_1^{-1}\bigl((1-\tfrac1n,\infty)\bigr)$ is open.

\smallskip

\noindent\emph{$\{U_n\}_{n\in\mathbb{N}}$ covers $X$.}
If $f\in X$ then $f(1)\in[0,1]$, hence there exists $n$ with $1-\tfrac1n<f(1)$, i.e.\ $f\in U_n$.

\smallskip

\noindent\textbf{No finite subcover.}
Given finitely many $U_{n_1},\dots,U_{n_k}$, let $N=\max\{n_1,\dots,n_k\}$ and consider
the constant function $f_N(x)\equiv 1-\tfrac{1}{2N}$.
Then $f_N\in X$ but
\[
f_N(1)=1-\tfrac{1}{2N}\le 1-\tfrac1N,
\]
so $f_N\notin U_N$, hence $f_N$ is not contained in the finite union $U_{n_1}\cup\cdots\cup U_{n_k}$.
Therefore no finite subcollection covers $X$.

\smallskip

Consequently, $X$ is not compact.

For $f:\mathbb{R}\to\mathbb{R}$ and $q\in\mathbb{R}$, the \emph{fiber} (level set) at $q$ is
\[
f^{-1}(q)=\{x\in\mathbb{R}:\ f(x)=q\}.
\]
A \emph{rational fiber} means $q\in\mathbb{Q}$.

\smallskip

\noindent\textbf{Key mechanism (with IVP).}
Assume $f$ has the intermediate value property and that each rational fiber $f^{-1}(q)$ is closed.
Fix $q\in\mathbb{Q}$. Then the sublevel and superlevel sets
\[
U_q=f^{-1}((-\infty,q)),\qquad V_q=f^{-1}((q,\infty))
\]
are open. Indeed, if $x_0\in U_q$ but every neighborhood of $x_0$ contains points with values $\ge q$,
the IVP forces points with value exactly $q$ arbitrarily close to $x_0$, hence $x_0\in\overline{f^{-1}(q)}$.
Since $f^{-1}(q)$ is closed, $x_0\in f^{-1}(q)$, contradicting $f(x_0)<q$.
Thus $U_q$ is open; similarly $V_q$ is open.

\smallskip

For rationals $r<s$,
\[
f^{-1}((r,s))=V_r\cap U_s
\]
is open. Because intervals with rational endpoints form a base of $\mathbb{R}$,
the preimage of every open set is open; hence $f$ is continuous.

\bigskip

\noindent\textbf{Examples.}

	\par\noindent\textbullet\quad \emph{IVP but some rational fiber not closed (discontinuous):}
	$f(x)=\sin(1/x)$ for $x\ne 0$, $f(0)=0$. For $q=\tfrac12$, $f^{-1}(q)$ accumulates at $0$ but does not contain $0$.
	\par\noindent\textbullet\quad \emph{Closed rational fibers but no IVP (discontinuous):}
	$f(x)=\mathbf{1}_{[0,\infty)}(x)$. Fibers at $q=0,1$ are closed; others are empty (closed). Yet $f$ is discontinuous at $0$.
	\par\noindent\textbullet\quad \emph{Continuous:} any continuous $f$ has all fibers $f^{-1}(q)$ closed for every $q\in\mathbb{R}$ and satisfies IVP.
```

## CP-II-0304

- chapter line: 4936

```tex
\label{prob:cp-ii-0304}
(Fourier transform of a compactly supported $L^1$ function)

Suppose $f \in L^{1}(\mathbb{R}^{n})$ with $\operatorname{supp} f \subset B_{R}(0)$ for some $R>0$.

	\par\noindent\textbullet\quad Show that $\widehat{f} \in C^{\infty}(\mathbb{R}^{n})$ and that for any multi–index $\alpha$,
	\[
	\sup_{\xi \in \mathbb{R}^{n}} \left| D^{\alpha} \widehat{f}(\xi) \right|
	\le R^{|\alpha|} \, \|f\|_{L^{1}(\mathbb{R}^{n})}.
	\]

	\par\noindent\textbullet\quad Show that $\widehat{f}$ is real analytic, with an infinite radius of convergence, i.e.
	\[
	\widehat{f}(\xi)
	= \sum_{\alpha} \frac{D^{\alpha} \widehat{f}(0)}{\alpha!} \, \xi^{\alpha}
	\qquad \text{for all } \xi \in \mathbb{R}^{n}.
	\]

	\par\noindent\textbullet\quad Show that if $\widehat{f}(\xi)$ vanishes on an open set, then it must vanish everywhere.
	\hfill\textit{(Hint: use part (i) of Lemma 3.2.)}

You may assume the following version of Taylor's theorem: if $g \in C^{k+1}(B_{r}(0))$, then for $x \in B_{r}(0)$,
\[
g(x)
= \sum_{|\alpha|\le k} D^{\alpha} g(0)\,\frac{x^{\alpha}}{\alpha!}
+ \sum_{|\beta| = k+1} R_{\beta}(x)\,x^{\beta},
\]
where the remainder satisfies
\[
|R_{\beta}(x)|
\le \frac{1}{\beta!}
\max_{|\alpha|=|\beta|}
\max_{y\in B_{r}(0)} |D^{\alpha} g(y)|.
\]

Suppose $f\in L^1(\mathbb{R}^n)$, with $\mathrm{supp}\,f\subset B_R(0)$ for some $R>0$,
and define
\[
\widehat f(\xi):=\int_{\mathbb{R}^n} e^{-2\pi i x\cdot \xi} f(x)\,dx.
\]

We first show that $\widehat f\in C^\infty(\mathbb{R}^n)$ and that, for any
multi-index $\alpha$,
\[
\sup_{\xi\in\mathbb{R}^n}\big|D^\alpha \widehat f(\xi)\big|
\le R^{|\alpha|}\,\|f\|_{L^1(\mathbb{R}^n)}.
\]

\emph{Proof.}
Because $f$ has compact support, for each multi-index $\alpha$ we may differentiate
under the integral sign:
\[
D^\alpha_\xi \widehat f(\xi)
= \int_{\mathbb{R}^n} D^\alpha_\xi\!\big(e^{-2\pi i x\cdot \xi}\big) f(x)\,dx
= \int_{\mathbb{R}^n} (-2\pi i x)^\alpha e^{-2\pi i x\cdot \xi} f(x)\,dx.
\]
Hence
\[
|D^\alpha \widehat f(\xi)|
\le \int_{\mathbb{R}^n} |x^\alpha|\,|f(x)|\,dx.
\]
On the support of $f$ we have $|x_k|\le R$ for each coordinate, so
$|x^\alpha|\le R^{|\alpha|}$. Therefore
\[
|D^\alpha \widehat f(\xi)|
\le R^{|\alpha|} \int_{\mathbb{R}^n}|f(x)|\,dx
= R^{|\alpha|}\,\|f\|_{L^1(\mathbb{R}^n)},
\]
and this upper bound is independent of $\xi$. Thus
\[
\sup_{\xi\in\mathbb{R}^n}|D^\alpha\widehat f(\xi)|
\le R^{|\alpha|}\,\|f\|_{L^1}.
\]
Since each derivative is obtained as an $L^1$–limit under the integral,
$D^\alpha\widehat f$ is continuous, and hence $\widehat f\in C^\infty(\mathbb{R}^n)$.


We show that $\widehat f$ is real analytic with infinite radius of convergence, i.e.
\[
\widehat f(\xi) = \sum_{\alpha} \frac{D^\alpha \widehat f(0)}{\alpha!}\,\xi^\alpha
\qquad\text{for all }\xi\in\mathbb{R}^n.
\]

\emph{Proof.}
Apply the multivariable Taylor theorem to
\[
g(\xi):=\widehat f(\xi)
\]
at the point $0\in\mathbb{R}^n$. For $x\in B_r(0)$ we have
\[
\widehat f(x)
= \sum_{|\alpha|\le k} D^\alpha \widehat f(0)\,\frac{x^\alpha}{\alpha!}
+ \sum_{|\beta|=k+1} R_\beta(x)\,x^\beta,
\]
where each remainder term satisfies
\[
|R_\beta(x)|
\le \frac{1}{\beta!}
\max_{|\gamma|=|\beta|}
\max_{y\in B_r(0)} |D^\gamma \widehat f(y)|.
\]
Using the estimate from part (a) we obtain
\[
|R_\beta(x)|
\le \frac{1}{\beta!}\,R^{|\beta|}\,\|f\|_{L^1}.
\]
Hence, for $|x|<r$,
\[
\begin{aligned}
	\left|\sum_{|\beta|=k+1} R_\beta(x)\,x^\beta\right|
	&\le \sum_{|\beta|=k+1}
	\frac{R^{|\beta|}\|f\|_{L^1}}{\beta!}\,|x|^{|\beta|} \\
	&\le \|f\|_{L^1}
	\sum_{m=k+1}^\infty \frac{(C R|x|)^m}{m!},
\end{aligned}
\]
where $C>0$ depends only on the dimension (via the number of multi-indices of
length $m$). The last sum is the tail of an exponential series and therefore
tends to $0$ as $k\to\infty$, for every $x\in\mathbb{R}^n$ (no restriction on $|x|$).

Letting $k\to\infty$ we conclude that
\[
\widehat f(\xi)
= \sum_{\alpha} \frac{D^\alpha \widehat f(0)}{\alpha!}\,\xi^\alpha
\qquad\text{for all }\xi\in\mathbb{R}^n,
\]
so $\widehat f$ is real analytic with infinite radius of convergence.


Suppose that $\widehat f(\xi)=0$ for all $\xi$ in some nonempty open set
$\Omega\subset\mathbb{R}^n$. Choose $\xi_0\in\Omega$ and let $B_r(\xi_0)\subset\Omega$ be
a ball contained in $\Omega$. On $B_r(\xi_0)$ we have $\widehat f\equiv 0$, and hence,
for every multi-index $\alpha$,
\[
D^\alpha \widehat f(\xi_0)=0.
\]

By part (b), the Taylor expansion of $\widehat f$ at $\xi_0$ has infinite radius of
convergence:
\[
\widehat f(\xi)
= \sum_{\alpha} \frac{D^\alpha \widehat f(\xi_0)}{\alpha!}\,
(\xi-\xi_0)^\alpha
\qquad\text{for all }\xi\in\mathbb{R}^n.
\]
Since all derivatives at $\xi_0$ vanish, every coefficient in this series is zero,
and consequently $\widehat f(\xi)=0$ for all $\xi\in\mathbb{R}^n$.

Thus, if $\widehat f$ vanishes on any nonempty open set, it must vanish identically.


In one dimension, let
\[
f(x) = \mathbf{1}_{[-1,1]}(x).
\]
Then $f\in L^{1}(\mathbb{R})$ and $\mathrm{supp}\,f\subset[-1,1]=B_{1}(0)$, so $R=1$
and $\|f\|_{L^{1}}=2$. With the Fourier transform
\[
\widehat{f}(\xi)
= \int_{\mathbb{R}} e^{-2\pi i x\xi} f(x)\,dx,
\]
we compute
\[
\widehat{f}(\xi)
= \int_{-1}^{1} e^{-2\pi i x\xi}\,dx
= \frac{\sin(2\pi\xi)}{\pi\xi},
\]
where $\widehat{f}(0)$ is defined by continuity, giving $\widehat{f}(0)=2$.

For any $k\in\mathbb{N}$ we have
\[
\widehat{f}^{(k)}(\xi)
= \int_{-1}^{1} (-2\pi i x)^{k} e^{-2\pi i x\xi}\,dx,
\]
so that
\[
\big|\widehat{f}^{(k)}(\xi)\big|
\le \int_{-1}^{1} |2\pi x|^{k}\,dx
\le (2\pi)^{k} \int_{-1}^{1} |x|^{k}\,dx
\le (2\pi)^{k} \cdot 2.
\]
This is of the form
\[
\sup_{\xi\in\mathbb{R}} \big|\widehat{f}^{(k)}(\xi)\big|
\le C^{k} \|f\|_{L^{1}},
\]
and illustrates the bound from part (a) of Exercise~3.7 with $R=1$.

Around $\xi=0$ we expand
\[
e^{-2\pi i x\xi} = \sum_{m=0}^{\infty}
\frac{(-2\pi i x\xi)^{m}}{m!},
\]
and since $|x|\le 1$ on the support of $f$, we may integrate term-by-term:
\[
\widehat{f}(\xi)
= \sum_{m=0}^{\infty} \frac{(-2\pi i \xi)^{m}}{m!}
\int_{-1}^{1} x^{m}\,dx.
\]
The inner integral is
\[
\int_{-1}^{1} x^{m}\,dx
=
\begin{cases}
	0, & m \text{ odd},\\[0.3em]
	\dfrac{2}{m+1}, & m \text{ even},
\end{cases}
\]
so
\[
\widehat{f}(\xi)
= \sum_{k=0}^{\infty}
\frac{(-2\pi i \xi)^{2k}}{(2k)!}\,\frac{2}{2k+1}.
\]
This is a power series in $\xi$ which converges for all $\xi\in\mathbb{R}$, and
precisely recovers $\widehat{f}(\xi)=\sin(2\pi\xi)/(\pi\xi)$. It is a concrete
instance of the statement in part (b) that $\widehat{f}$ is real analytic with
infinite radius of convergence.

Note also that $\widehat{f}(\xi)$ has only isolated zeros (at $\xi=k/2$,
$k\in\mathbb{Z}\setminus\{0\}$), so it does \emph{not} vanish on any nonempty
open interval. This is consistent with part (c): if $\widehat{f}$ vanished on an
open set, analyticity would force all derivatives at a point of that set to be
zero and hence $\widehat{f}\equiv 0$.

Let
\[
f(x)=
\begin{cases}
	e^{-\frac{1}{1-x^{2}}}, & |x|<1,\\[0.3em]
	0, & |x|\ge 1 ,
\end{cases}
\qquad f\in C^\infty_c(\mathbb{R}),\ \mathrm{supp}(f)\subset[-1,1].
\]
Its Fourier transform is
\[
\widehat{f}(\xi)
= \int_{-1}^{1} e^{-2\pi i x\xi}\, e^{-\frac{1}{1-x^{2}}}\,dx,
\]
which does not admit a simple closed form, but it satisfies all conclusions of Exercise~3.7:

	\par\noindent (a)\quad \textbf{Differentiating under the integral.}
	For every integer $k\ge0$,
	\[
	\widehat{f}^{(k)}(\xi)
	= \int_{-1}^{1} (-2\pi i x)^{k} e^{-2\pi i x\xi}\, e^{-\frac{1}{1-x^{2}}}\,dx.
	\]
	Since $|x|\le 1$,
	\[
	\big|\widehat{f}^{(k)}(\xi)\big|
	\le \int_{-1}^{1} |2\pi x|^{k} e^{-\frac{1}{1-x^{2}}}\,dx
	\le C^{k}\,\|f\|_{L^{1}},
	\qquad
	\sup_{\xi\in\mathbb{R}}\big|\widehat{f}^{(k)}(\xi)\big| <\infty.
	\]
	This matches exactly the estimate
	\[
	\sup_{\xi\in\mathbb{R}^{n}} |D^\alpha \widehat{f}(\xi)|
	\le R^{|\alpha|}\,\|f\|_{L^{1}},
	\qquad R=1.
	\]

	\par\noindent (b)\quad \textbf{Real analyticity.}
	Expanding the exponential,
	\[
	e^{-2\pi i x\xi}
	= \sum_{m=0}^{\infty} \frac{(-2\pi i x\xi)^{m}}{m!},
	\]
	and since $|x|\le 1$ on $\operatorname{supp}(f)$, the series converges absolutely for all $\xi$.
	Thus the integral may be computed term-by-term:
	\[
	\widehat{f}(\xi)
	= \sum_{m=0}^{\infty}
	\frac{(-2\pi i\xi)^{m}}{m!}
	\int_{-1}^{1} x^{m}\, e^{-\frac{1}{1-x^{2}}}\,dx.
	\]
	This is a power series in $\xi$ with infinite radius of convergence, exactly as stated in Exercise~3.7(b).

	\par\noindent (c)\quad \textbf{Vanishing on an open set implies $\widehat{f}\equiv 0$.}
	If $\widehat{f}$ vanished on an open interval, real analyticity would force all derivatives
	at a point of that interval to vanish, making all coefficients in the Taylor series zero.
	Hence $\widehat{f}\equiv 0$.
	But
	\[
	\widehat{f}(0)=\int_{-1}^{1} f(x)\,dx >0,
	\]
	so this cannot happen for the bump function.
	This fully matches Exercise~3.7(c).
```

## CP-II-0309

- chapter line: 5227

```tex
\label{prob:cp-ii-0309}
s.

\par\noindent\textbullet\quad If \(\nu=\gamma\) is the Cantor measure, then \(\nu_a=0\) and \(\nu_s=\gamma\).

	Let $X$ be a topological space and $\mu$ a (Borel) measure on $X$.
	We say $\mu$ is \emph{locally finite} if every $x\in X$ has a neighborhood $U$
	with $\mu(U)<\infty$.
	Lebesgue measure on $\mathbb{R}^n$ and counting measure on a discrete space are locally finite.
	A measure that assigns $+\infty$ to every nonempty open set is not locally finite.

	\bigskip

	A Borel measure $\mu$ on a Hausdorff space $X$ is
	\emph{outer regular} if for every Borel set $A$,
	\[
	\mu(A)=\inf\{\mu(U): A\subset U,\ U\text{ open}\},
	\]
	and \emph{inner regular} if for every Borel set $A$,
	\[
	\mu(A)=\sup\{\mu(K): K\subset A,\ K\text{ compact}\}.
	\]
	A \emph{Radon measure} is a Borel measure that is locally finite, outer regular, and inner regular.
	Classical examples include Lebesgue measure on $\mathbb{R}^n$, surface measure on smooth manifolds,
	and counting measure on discrete locally compact spaces.

	\bigskip

	A \emph{topological group} is a group $G$ endowed with a Hausdorff topology such that
	multiplication $(g,h)\mapsto gh$ and inversion $g\mapsto g^{-1}$ are continuous.
	If $G$ is \emph{locally compact}, then there exists a nonzero Radon measure $\eta$
	(Haar measure) such that $\eta(gA)=\eta(A)$ for all Borel $A$ and all $g\in G$.
	Haar measure is unique up to a positive scalar multiple.
	If also $\eta(Ag)=\eta(A)$ for all $g$, then $G$ is \emph{unimodular}
	(e.g.\ all abelian, discrete, and compact groups).
	On $\mathbb{R}^n$, Haar measure coincides with Lebesgue measure.

	\bigskip

	For measures $\mu,\nu$ on $(X,\mathcal{B})$, we write $\nu\perp\mu$ if there exists
	$S\in\mathcal{B}$ with $\mu(S)=0$ and $\nu(X\setminus S)=0$.
	This is the measure-theoretic notion often called ``orthogonality'' of measures.
	Examples: $\delta_x\perp m$ on $\mathbb{R}^n$, and the Cantor measure $\gamma$ on $[0,1]$ satisfies $\gamma\perp m$.

	\bigskip

	On a locally compact Hausdorff space with a Radon reference measure $\mu$ (e.g.\ Haar measure on a group),
	any finite Borel measure $\nu$ decomposes uniquely as $\nu=\nu_a+\nu_s$ with $\nu_a\ll\mu$ and $\nu_s\perp\mu$.
	In particular, on $\mathbb{R}^n$ with $\mu=m$ (Lebesgue), the absolutely continuous part has the
	form $\nu_a=f\,m$ for some $f\in L^1(m)$, while $\nu_s$ is concentrated on an $m$-null set.

	Let $X$ be a topological space. The \emph{Borel $\sigma$-algebra} $\mathcal{B}(X)$
	is the smallest $\sigma$-algebra containing all open sets of $X$.
	Equivalently, $\mathcal{B}(X)$ is generated by the open sets (and hence contains
	all closed sets, $G_\delta$ and $F_\sigma$ sets, and all sets obtained from these
	by countable unions, intersections, and complements).

	\bigskip

	A measure $\mu$ defined on $\mathcal{B}(X)$ is called a \emph{Borel measure}.
	If, in addition, $\mu$ is \emph{locally finite} and both \emph{outer} and \emph{inner regular},
	then $\mu$ is a \emph{Radon measure}.

	\bigskip

	Given a Borel measure $\mu$, its \emph{completion} adds to the $\sigma$-algebra
	all subsets of $\mu$-null sets. Lebesgue measure on $\mathbb{R}^n$ is precisely
	the completion of a Borel measure (often called the Borel--Lebesgue measure).

	\bigskip
```

## CP-II-0310

- chapter line: 5300

```tex
\label{prob:cp-ii-0310}
Slices and a quotient of a product

Let $X,Y$ be topological spaces and endow $X\times Y$ with the product topology.

	\subsection*{(a) For each $y\in Y$, $X\times\{y\}\cong X$}
	Define
	\[
	i_y:X\to X\times\{y\},\quad i_y(x)=(x,y),
	\qquad
	p_y:X\times\{y\}\to X,\quad p_y(x,y)=x.
	\]
	Then $i_y$ is continuous (product of $\mathrm{id}_X$ with the constant map $y$),
	$p_y$ is the restriction of the continuous projection $\pi_X$, and
	\[
	p_y\circ i_y=\mathrm{id}_X,\qquad i_y\circ p_y=\mathrm{id}_{X\times\{y\}}.
	\]
	Hence $i_y$ is a homeomorphism $X\cong X\times\{y\}$.

	Define $(x,y)\sim(x',y')$ iff $x=x'$. Let $q:X\times Y\to (X\times Y)/\!\sim$ be the quotient map and
	$\pi_X:X\times Y\to X$ the first projection. Since $\pi_X$ is continuous and constant on $\sim$-classes,
	the universal property yields a unique continuous
	\[
	\tilde\pi:(X\times Y)/\!\sim \longrightarrow X \quad\text{such that}\quad \tilde\pi\circ q=\pi_X.
	\]

	Fix $y_0\in Y$ and define $s:X\to (X\times Y)/\!\sim$ by $s(x)=q(x,y_0)$.
	Then $s$ is continuous (it equals $q\circ i_{y_0}$).

	For $x\in X$, $\tilde\pi\circ s(x)=\tilde\pi(q(x,y_0))=\pi_X(x,y_0)=x$.
	For any $(x,y)\in X\times Y$ we have $(x,y)\sim(x,y_0)$, hence
	\[
	s\circ\tilde\pi\big(q(x,y)\big)=s(x)=q(x,y_0)=q(x,y).
	\]
	Thus $s=(\tilde\pi)^{-1}$ and $\tilde\pi$ is a homeomorphism.
	Therefore $(X\times Y)/\!\sim\ \cong X$.

	\begin{tikzcd}
		X\times Y \arrow[d, "q"'] \arrow[dr, "\pi_X"] & \\
		Q \arrow[r, "\tilde{\pi}"'] & X
	\end{tikzcd}

\medskip

\begin{tikzcd}
		X \arrow[r, "i_{y_0}"] \arrow[rr, bend right=20, "\mathrm{id}_X"'] &
		X\times Y \arrow[r, "q"] \arrow[dr, "\pi_X"'] &
		Q \arrow[d, "\tilde{\pi}"] \arrow[loop right, "s\circ\tilde{\pi}"'] \\
		& & X
	\end{tikzcd}

		\par\noindent\textbullet\quad $X=\mathbb{R}$, $Y=[0,1]$. For any $t\in[0,1]$, the map
		$i_t:\mathbb{R}\to \mathbb{R}\times\{t\}$, $x\mapsto(x,t)$,
		is a homeomorphism with inverse $(x,t)\mapsto x$.
		\par\noindent\textbullet\quad $X=S^1$, $Y=\mathbb{R}$. Each slice $S^1\times\{y\}$ is homeomorphic to $S^1$.
		\par\noindent\textbullet\quad $X=\{1,2,3\}$ (discrete), arbitrary $Y$. Each $\{1,2,3\}\times\{y\}$ is a 3--point discrete space $\cong X$.
		\par\noindent\textbullet\quad $X$ arbitrary, $Y$ non-Hausdorff (e.g.\ indiscrete). Still $X\times\{y\}\cong X$; the slice homeomorphism does not use separation axioms.

	Let $(x,y)\sim(x',y')$ iff $x=x'$ and assume $Y\neq\varnothing$.

		\par\noindent\textbullet\quad $X=\mathbb{R}$, $Y=[0,1]$. Each vertical segment $\{x\}\times[0,1]$ collapses to one point; the quotient is $\mathbb{R}$.
		\par\noindent\textbullet\quad $X=S^1$, $Y=\{0,1\}$. The two parallel circles collapse columnwise; the quotient is $S^1$.
		\par\noindent\textbullet\quad $X=\{1,2,3\}$ (discrete), $Y=\{a,b,c\}$. The $3\times3$ grid collapses each column to one point; the quotient is a 3--point discrete space $\cong X$.
		\par\noindent\textbullet\quad $X$ arbitrary, $Y$ indiscrete nonempty. Despite $X\times Y$ not being Hausdorff, the quotient by vertical fibers is homeomorphic to $X$ via the factorization of $\pi_X$.

	If $Y=\varnothing$ then $X\times Y=\varnothing$ and $(X\times Y)/\!\sim=\varnothing\not\cong X$ unless $X=\varnothing$.

	\section*{Problem 12: $\mathbb{R}^2/\mathbb{Z}^2$ is a torus}

	Let $\sim$ on $\mathbb{R}^2$ be given by
	\[
	(x,y)\sim(z,w)\quad\Longleftrightarrow\quad x-z\in\mathbb{Z}\ \text{ and }\ y-w\in\mathbb{Z}.
	\]
	Show that $\mathbb{R}^2/\!\sim$ is homeomorphic to the embedded torus
	\[
	T=\Bigl\{\bigl((2+\cos\theta)\cos\phi,\ (2+\cos\theta)\sin\phi,\ \sin\theta\bigr)\ :\ \theta,\phi\in[0,2\pi]\Bigr\}\subset\mathbb{R}^3.
	\]

	Define
	\[
	F:\mathbb{R}^2\longrightarrow S^1\times S^1,\qquad
	F(x,y)=\bigl(e^{2\pi i x},\,e^{2\pi i y}\bigr).
	\]
	Then:

		\par\noindent\textbullet\quad $F$ is continuous.
		\par\noindent\textbullet\quad $F$ is constant on $\sim$-classes (adding integers to $x$ or $y$ does not change the exponentials).

	Hence $F$ descends to a unique continuous
	\[
	\tilde F:\ \mathbb{R}^2/\!\sim\ \longrightarrow\ S^1\times S^1
	\quad\text{with}\quad
	\tilde F\circ q=F \ \ (q \text{ the quotient map}).
	\]

	Given $(u,v)\in S^1\times S^1$, choose arguments $u=e^{2\pi i x}$, $v=e^{2\pi i y}$.
	Different choices differ by integers, hence determine the same class. Therefore $\tilde F$ is bijective.

	$\mathbb{R}^2/\!\sim$ is compact (homeomorphic to $[0,1]^2$ with opposite edges identified), and $S^1\times S^1$ is Hausdorff.
	A continuous bijection from a compact space onto a Hausdorff space is a homeomorphism; thus $\tilde F$ is a homeomorphism.

	\par\medskip\noindent\textbf{Step 4 (embed into $\mathbb{R}^3$).}\quad
	Define
	\[
	\Phi: S^1\times S^1\to T,\qquad
	\Phi\bigl(e^{i\theta},e^{i\phi}\bigr)
	=\bigl((2+\cos\theta)\cos\phi,\ (2+\cos\theta)\sin\phi,\ \sin\theta\bigr).
	\]
	$\Phi$ is a homeomorphism onto $T$. Therefore
	\[
	\mathbb{R}^2/\!\sim\ \cong\ S^1\times S^1\ \cong\ T.
	\]

	\bigskip

	\par\medskip\noindent\textbf{Step 1 (define a $\mathbb{Z}^2$-periodic map).}\quad
	Set
	\[
	G:\mathbb{R}^2\to T,\qquad
	G(x,y)=\Bigl((2+\cos(2\pi x))\cos(2\pi y),\ (2+\cos(2\pi x))\sin(2\pi y),\ \sin(2\pi x)\Bigr).
	\]
	Then $G$ is continuous and satisfies $G(x+m,y+n)=G(x,y)$ for all $m,n\in\mathbb{Z}$, so $G$ is constant on $\sim$-classes and factors through a continuous
	\[
	\tilde G:\ \mathbb{R}^2/\!\sim\ \longrightarrow\ T.
	\]

	For any $(\theta,\phi)\in[0,2\pi]^2$, the point of $T$ with those angles equals
	\[
	G\!\left(\frac{\theta}{2\pi},\,\frac{\phi}{2\pi}\right).
	\]
	Changing $(\theta,\phi)$ by integer multiples of $2\pi$ changes $(x,y)$ by integers, i.e.\ stays in the same class.
	Thus $\tilde G$ is bijective.

	As above, $\mathbb{R}^2/\!\sim$ is compact and $T$ is Hausdorff (subspace of $\mathbb{R}^3$), hence the continuous bijection $\tilde G$ is a homeomorphism.

	\bigskip

		\par\noindent\textbullet\quad $\mathbb{R}/\mathbb{Z}\cong S^1$ (the 1-torus).
		\par\noindent\textbullet\quad $\mathbb{R}^n/\mathbb{Z}^n\cong (S^1)^n$ (the $n$-torus).
		\par\noindent\textbullet\quad Identifying only the $y$-coordinate modulo $\mathbb{Z}$ gives the cylinder $\mathbb{R}\times S^1$.

	\par\medskip\noindent\textbf{Description of the map $G:\mathbb{R}^2\to T$.}\quad
	Define
	\[
	G(x,y)=\Big((2+\cos(2\pi x))\cos(2\pi y),\ (2+\cos(2\pi x))\sin(2\pi y),\ \sin(2\pi x)\Big).
	\]

	Set
	\[
	\theta=2\pi x,\qquad \phi=2\pi y.
	\]
	Then
	\[
	G(x,y)=\bigl((2+\cos\theta)\cos\phi,\ (2+\cos\theta)\sin\phi,\ \sin\theta\bigr),
	\]
	which is the standard parametrization of the embedded torus $T\subset\mathbb{R}^3$
	with major radius $2$ and minor radius $1$.
	Here $\theta$ moves around the small circular cross--section (the ``tube''),
	producing the vertical coordinate $z=\sin\theta$ and the tube radius $1$,
	while $\phi$ rotates the cross--section around the $z$--axis; the distance from the
	$z$--axis is $2+\cos\theta$ and multiplying by $(\cos\phi,\sin\phi)$ sweeps the big circle.

	For every $(m,n)\in\mathbb{Z}^2$,
	\[
	G(x+m,y+n)=G(x,y),
	\]
	since only $2\pi x$ and $2\pi y$ appear in trigonometric functions.
	Thus $G$ is constant on cosets of $\mathbb{Z}^2$ in $\mathbb{R}^2$, i.e.\ on the equivalence
	classes for the relation $(x,y)\sim(x',y')\iff (x-x',y-y')\in\mathbb{Z}^2$.
	Let $q:\mathbb{R}^2\to\mathbb{R}^2/\mathbb{Z}^2$ be the quotient map.
	By the universal property of the quotient, there exists a unique continuous
	\[
	\tilde G:\ \mathbb{R}^2/\mathbb{Z}^2 \longrightarrow T \quad\text{such that}\quad \tilde G\circ q = G.
	\]

	Given any point of $T$ written as
	\[
	\bigl((2+\cos\theta)\cos\phi,\ (2+\cos\theta)\sin\phi,\ \sin\theta\bigr)
	\quad (\theta,\phi\in[0,2\pi]),
	\]
	choose $(x,y)=(\theta/2\pi,\ \phi/2\pi)\in\mathbb{R}^2$; then $G(x,y)$ equals that point.
	Different choices of $(\theta,\phi)$ differ by integer multiples of $2\pi$ and hence change
	$(x,y)$ by integers only; therefore they lie in the same class in $\mathbb{R}^2/\mathbb{Z}^2$.
	Consequently $\tilde G$ is bijective.

	The space $\mathbb{R}^2/\mathbb{Z}^2$ is compact (homeomorphic to the unit square $[0,1]^2$
	with opposite edges identified), and $T\subset\mathbb{R}^3$ is Hausdorff.
	Hence the continuous bijection $\tilde G:\mathbb{R}^2/\mathbb{Z}^2\to T$ is a homeomorphism.

	The relation $(x,y)\sim(x+m,y+n)$, $m,n\in\mathbb{Z}$, identifies opposite edges of the unit square
	$[0,1]^2$, producing the compact surface $[0,1]^2/\!\sim$ which is homeomorphic to $S^1\times S^1$,
	i.e.\ a (topological) torus. The set
	\[
	T=\{((2+\cos\theta)\cos\phi,(2+\cos\theta)\sin\phi,\sin\theta):\theta,\phi\in[0,2\pi]\}\subset\mathbb{R}^3
	\]
	is a standard embedded model of this torus. The map
	\[
	G(x,y)=\big((2+\cos 2\pi x)\cos 2\pi y,\ (2+\cos 2\pi x)\sin 2\pi y,\ \sin 2\pi x\big)
	\]
	is $\,\mathbb{Z}^2$–periodic and hence factors through the quotient, yielding a homeomorphism
	$\tilde G:\mathbb{R}^2/\mathbb{Z}^2\to T$.
```

## CP-II-0321

- chapter line: 5618

```tex
\label{prob:cp-ii-0321}
(Local submersion theorem and consequences)

The \emph{canonical submersion} is the standard projection $\mathbb{R}^k\to\mathbb{R}^\ell$ for $k\ge \ell$,
\[
(x_1,\dots,x_k)\longmapsto (x_1,\dots,x_\ell).
\]
Let $f$ be a submersion and $y=f(x)$. Show:

	\par\noindent\textbullet\quad there exist local coordinates around $x$ and $y$ such that $f$ becomes the canonical submersion;
	\par\noindent\textbullet\quad submersions are open maps;
	\par\noindent\textbullet\quad if $X$ is compact and $Y$ connected, then every submersion $f:X\to Y$ is surjective;
	\par\noindent\textbullet\quad decide whether there exist submersions from compact manifolds into Euclidean spaces.

A smooth map $f:X^k\to Y^\ell$ is a \emph{submersion at $x$} if $df_x:T_xX\to T_{f(x)}Y$ is surjective.
Equivalently, $\operatorname{rank}(df_x)=\ell$ (so $\ell\le k$). The constant rank theorem gives a local normal form.

Since $f$ is a submersion at $x$, we have $\operatorname{rank}(df_x)=\ell$.
By the constant rank theorem, there exist coordinate charts $(U,\varphi)$ about $x$ and $(V,\psi)$ about $y=f(x)$
such that in these coordinates
\[
(\psi\circ f\circ \varphi^{-1})(u_1,\dots,u_k)=(u_1,\dots,u_\ell),
\]
i.e.\ $f$ becomes the canonical projection $\mathbb{R}^k\to\mathbb{R}^\ell$.


Let $U\subset X$ be open. Fix $x\in U$ and choose local coordinates as in (i), so that locally $f$ is the projection
$\pi(u_1,\dots,u_k)=(u_1,\dots,u_\ell)$. The projection $\pi:\mathbb{R}^k\to\mathbb{R}^\ell$ is an open map.
Since coordinate changes are diffeomorphisms (hence homeomorphisms), they preserve openness. Therefore $f(U)$ is open in $Y$.
Thus every submersion is an open map.


Let $f:X\to Y$ be a submersion. Since $X$ is compact and $f$ is continuous, $f(X)$ is compact.
Because manifolds are Hausdorff, compact sets are closed, hence $f(X)$ is closed in $Y$.
On the other hand, by (ii), $f(X)=f(\,X\,)$ is open in $Y$ (since $X$ is open in itself).
Assuming $X\neq\emptyset$, the set $f(X)$ is nonempty. Hence $f(X)$ is a nonempty subset of $Y$ that is both open and closed.
If $Y$ is connected, this forces $f(X)=Y$. Thus $f$ is surjective.


Let $X$ be compact and suppose $f:X\to\mathbb{R}^\ell$ is a submersion with $\ell\ge 1$.
Then $\mathbb{R}^\ell$ is connected, so by (iii) the map must be surjective: $f(X)=\mathbb{R}^\ell$.
But $f(X)$ is compact, hence cannot equal the non-compact space $\mathbb{R}^\ell$.
This contradiction shows that no such submersion exists for $\ell\ge 1$.
(For $\ell=0$, the target is a point and any smooth map is trivially a submersion.)


A \emph{normal form} is the expression of a smooth map after choosing suitable local coordinates
in the domain and codomain.

	\par\noindent\textbullet\quad \textbf{Immersion normal form.}
	If $f:M^k\to N^n$ is an immersion at $x$ (so $df_x$ is injective, rank $k$), then there exist
	local coordinates $u$ near $x$ and $v$ near $y=f(x)$ such that
	\[
	(v\circ f\circ u^{-1})(u_1,\dots,u_k)=(u_1,\dots,u_k,0,\dots,0).
	\]
	Geometrically, $f(M)$ looks locally like a coordinate $k$-plane in $N$.

	\par\noindent\textbullet\quad \textbf{Submersion normal form.}
	If $f:X^k\to Y^\ell$ is a submersion at $x$ (so $df_x$ is surjective, rank $\ell$), then there exist
	local coordinates $u$ near $x$ and $v$ near $y=f(x)$ such that
	\[
	(v\circ f\circ u^{-1})(u_1,\dots,u_k)=(u_1,\dots,u_\ell).
	\]
	Geometrically, the fibers $f^{-1}(c)$ are locally the coordinate slices
	$\{u_1=c_1,\dots,u_\ell=c_\ell\}$, hence smooth manifolds of dimension $k-\ell$.
```

## CP-II-0323

- chapter line: 5810

```tex
\label{prob:cp-ii-0323}
\par\noindent\textbullet\quad \emph{Sequential compactness route.}
	From boundedness, every sequence in $E$ lies in a bounded subset of $\mathbb R^n$,
	hence has a convergent subsequence $(x_{n_k})\to q\in\mathbb R^n$.
	If $q\notin E$, the function $x\mapsto 1/\|x-q\|$ would be an unbounded continuous map on $E$,
	contradiction. Thus every sequence in $E$ has a convergent subsequence whose limit lies in $E$,
	so $E$ is sequentially compact, hence compact.
```

## CP-II-0326

- chapter line: 5820

```tex
\label{prob:cp-ii-0326}
Let $E\subset\mathbb{R}^n$ be compact and $f:E\to\mathbb{R}^m$ continuous.

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad $f(E)$ is bounded. \textit{Proof.} Each component $f^j$ attains its max/min on $E$.
\par\noindent\textbullet\quad $f(E)$ is closed, hence compact. \textit{Proof.} Use sequential closedness via compactness of $E$.
\par\noindent\textbullet\quad If $E$ is merely closed, $f(E)$ need not be closed; e.g.\ $f(x)=\arctan x$ on $E=\mathbb{R}$.
```

## CP-II-0330

- chapter line: 5830

```tex
\label{prob:cp-ii-0330}
\par\noindent\textbullet\quad The sequence $(f_n)$ is bounded but \emph{translates to infinity}.
		This shows that the $L^1$ unit ball is not weakly compact.
```

## CP-II-0332

- chapter line: 5836

```tex
\label{prob:cp-ii-0332}
Closure vs.\ Sequential Closure

For $A\subseteq X$, the \emph{sequential closure} $\operatorname{scl}(A)$ is the set of all limits of sequences $(x_n)$ with $x_n\in A$.
	We say $A$ is \emph{sequentially closed} if $\operatorname{scl}(A)\subseteq A$, i.e.\ whenever $x_n\in A$ and $x_n\to x$ in $X$, then $x\in A$.

	Assume $X$ is uncountable and $\tau=\{\varnothing\}\cup\{\,U\subseteq X:\ X\setminus U\ \text{is countable}\,\}$ (the co-countable topology).

	\begin{lemma}
		In $(X,\tau)$, a sequence $(x_n)$ converges to $x$ if and only if it is eventually constant equal to $x$.
	\end{lemma}
	\begin{proof}
		($\Rightarrow$) Let $(x_n)\to x$. Any neighborhood of $x$ is of the form $X\setminus C$ with $C$ countable and $x\notin C$; thus for each such $C$, $\{n:\ x_n\in C\}$ is finite.
		Let $S$ be the set of values taken by the tail of $(x_n)$; $S$ is countable. If $x\notin S$, take $C=S$ and get a contradiction. Hence $x\in S$. Taking $C=S\setminus\{x\}$ forces $x_n\in\{x\}$ eventually.
		($\Leftarrow$) If $x_n=x$ eventually, then every neighborhood of $x$ contains all sufficiently large $n$, so $x_n\to x$.
	\end{proof}

	\begin{proposition}
		Every subset $A\subseteq X$ is sequentially closed, but an uncountable proper subset $A$ is not closed.
	\end{proposition}
	\begin{proof}
		If $x_n\in A$ and $x_n\to x$, the lemma shows $x_n=x$ eventually, hence $x\in A$; thus $A$ is sequentially closed.
		Closed sets in the co-countable topology are precisely the countable sets together with $X$; therefore any uncountable proper $A$ is not closed.
	\end{proof}

	On $X=\mathbb{R}$ with the co-countable topology, $A=\mathbb{R}\setminus\mathbb{Q}$ is sequentially closed but not closed.

	\begin{proposition}
		If $(X,\tau)$ is second countable, then for every $A\subseteq X$ we have $\operatorname{scl}(A)=\overline{A}$. In particular, $A$ is sequentially closed iff $A$ is closed.
	\end{proposition}
	\begin{proof}
		Let $\mathcal{B}=\{B_1,B_2,\dots\}$ be a countable base for $X$. Fix $x\in X$ and enumerate $\mathcal{B}_x=\{B\in\mathcal{B}: x\in B\}$ as $(C_n)_{n\ge1}$.
		Define $U_n=\bigcap_{k=1}^n C_k$. Then $(U_n)$ is a decreasing countable neighborhood base at $x$.
		If $x\in\overline{A}$, then $A\cap U_n\neq\varnothing$ for all $n$; choose $x_n\in A\cap U_n$.
		By construction $x_n\to x$. Hence every point of $\overline{A}$ is a sequential limit of points of $A$, so $\operatorname{scl}(A)\supseteq\overline{A}$.
		The reverse inclusion is always true. Therefore $\operatorname{scl}(A)=\overline{A}$, and the equivalence follows.
	\end{proof}

	In $(\mathbb{R},\text{usual})$ the set $A=(0,1)$ is not sequentially closed since $x_n=1/n\to 0\notin A$.
	In contrast, in the co-countable $\mathbb{R}$ every subset is sequentially closed, while uncountable proper subsets are not closed.
```

## CP-II-0333

- chapter line: 5879

```tex
\label{prob:cp-ii-0333}
Small Metric Spaces and Isometric Embeddings

Let $(X,d)$ be a metric space.

		\par\noindent\textbullet\quad If $X=\{p_1,p_2,p_3\}$ has only three points, show that $X$ admits an
		isometric embedding into the Euclidean plane $(\mathbb{R}^2,d_{\mathrm{eucl}})$.

		\par\noindent\textbullet\quad Show that the four-point space
		\[
		X=\{p_1,p_2,p_3,q\}
		\]
		with distances
		\[
		d(p_i,p_j)=2L \quad(1\le i<j\le 3),\qquad
		d(p_1,q)=2L,\qquad d(p_2,q)=d(p_3,q)=L
		\]
		is a metric space which admits no isometric embedding into any Euclidean
		space $\mathbb{R}^n$.

		\par\noindent\textbullet\quad Let $L=\pi/4$ in \textnormal{(b)}.  Show that $X$ isometrically embeds
		in the unit sphere $(S^2,d_{S^2})\subset\mathbb{R}^3$, where $d_{S^2}$ is
		great-circle distance, and deduce that no subset of $S^2$ containing an open
		hemisphere admits an isometric embedding into the plane
		$(\mathbb{R}^2,d_{\mathrm{eucl}})$.

	A map $F:(X,d_X)\to(Y,d_Y)$ is an \emph{isometric embedding} if it is
	injective and
	\[
	d_Y(F(x),F(x'))=d_X(x,x')\quad\forall\,x,x'\in X.
	\]
	Any three-point metric space satisfying the triangle inequalities can be
	realised as a Euclidean triangle.  In Euclidean space, distance constraints
	give quadratic equations; for small configurations one can solve them
	explicitly and detect contradictions (e.g.\ a negative ``squared length'').

	On the unit sphere $S^2\subset\mathbb{R}^3$ with the intrinsic metric,
	the distance between unit vectors $u,v$ is
	\[
	d_{S^2}(u,v)=\arccos(u\cdot v),
	\]
	where $\cdot$ denotes the Euclidean dot product.  Rotations of $\mathbb{R}^3$
	preserve both $S^2$ and $d_{S^2}$, so any finite configuration can be rotated
	into a given open hemisphere.

	Let
	\[
	a=d(p_1,p_2),\quad b=d(p_1,p_3),\quad c=d(p_2,p_3).
	\]
	By the triangle inequality the three numbers $a,b,c$ satisfy
	\[
	a\le b+c,\quad b\le a+c,\quad c\le a+b.
	\]

	Place
	\[
	F(p_1)=(0,0),\qquad F(p_2)=(a,0)\in\mathbb{R}^2
	\]
	and seek $F(p_3)=(x,y)$ with
	\[
	\|F(p_3)-F(p_1)\|=b,\qquad \|F(p_3)-F(p_2)\|=c.
	\]
	Equivalently,
	\[
	x^2+y^2=b^2,\qquad (x-a)^2+y^2=c^2.
	\]
	Subtracting gives
	\[
	a^2-2ax=c^2-b^2,\qquad
	x=\frac{a^2+b^2-c^2}{2a}.
	\]
	Then
	\[
	y^2=b^2-x^2
	=\frac{(a+b+c)(a+b-c)(a-b+c)(-a+b+c)}{16a^2}\ge 0,
	\]
	by the triangle inequalities.  Hence there exists $y\in\mathbb{R}$ and an
	isometric embedding $F:X\to\mathbb{R}^2$.

	Suppose, for a contradiction, that there exists an isometric embedding
	$F:X\to\mathbb{R}^n$.  Let
	\[
	P_i=F(p_i),\qquad Q=F(q).
	\]
	The points $P_1,P_2,P_3$ form an equilateral triangle of side $2L$.  After a
	rigid motion we may assume
	\[
	P_1=(0,0,0,\dots),\quad
	P_2=(2L,0,0,\dots),\quad
	P_3=(L,\sqrt{3}\,L,0,\dots).
	\]
	Write $Q=(x,y,u)$ with $(x,y)\in\mathbb{R}^2$ and $u\in\mathbb{R}^{n-2}$; set
	$\|u\|^2=U\ge0$.

	The distance conditions become
	\begin{align*}
		(x-2L)^2+y^2+U &= L^2, \tag{1}\\
		(x-L)^2+(y-\sqrt{3}L)^2+U &= L^2, \tag{2}\\
		x^2+y^2+U &= 4L^2. \tag{3}
	\end{align*}
	Subtracting \textnormal{(2)} from \textnormal{(1)} yields
	\[
	-2Lx+2\sqrt{3}Ly=0,\qquad x=\sqrt{3}\,y.
	\]
	Subtracting \textnormal{(1)} from \textnormal{(3)} gives
	\[
	x^2-(x-2L)^2=3L^2,\qquad 4Lx-4L^2=3L^2,
	\]
	so $x=7L/4$ and hence $y=7L/(4\sqrt{3})$.

	From \textnormal{(1)},
	\[
	(x-2L)^2+y^2+U=L^2
	\]
	implies
	\[
	U = L^2 - \frac{L^2}{16}-\frac{49L^2}{48}
	= -\frac{L^2}{12}<0,
	\]
	contradicting $U=\|u\|^2\ge0$.  Thus no isometric embedding of $X$ into any
	$\mathbb{R}^n$ exists.

	Set $L=\pi/4$ and consider the unit sphere $S^2\subset\mathbb{R}^3$ with
	intrinsic distance
	\[
	d_{S^2}(u,v)=\arccos(u\cdot v).
	\]

	Choose
	\[
	P_1=(1,0,0),\quad P_2=(0,1,0),\quad P_3=(0,0,1)\in S^2.
	\]
	These are pairwise orthogonal, so
	\[
	d_{S^2}(P_i,P_j)=\arccos(0)=\frac{\pi}{2}=2L
	\quad (1\le i<j\le 3).
	\]
	Let
	\[
	Q=\left(0,\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right)\in S^2.
	\]
	Then
	\[
	P_1\cdot Q=0,\qquad
	P_2\cdot Q=P_3\cdot Q=\frac{1}{\sqrt{2}},
	\]
	so
	\[
	d_{S^2}(P_1,Q)=\frac{\pi}{2}=2L,\qquad
	d_{S^2}(P_2,Q)=d_{S^2}(P_3,Q)=\frac{\pi}{4}=L.
	\]
	Therefore the map $F$ defined by $F(p_i)=P_i$, $F(q)=Q$ is an isometric
	embedding of $X$ into $(S^2,d_{S^2})$.

	Now let $Y\subset S^2$ contain an open hemisphere $H$.  Since rotations of
	$S^2$ are isometries and $H$ is open, we can rotate the above four-point
	configuration so that all four points lie in $H\subset Y$.  Thus $Y$
	contains a subset isometric to $X$.

	If there were an isometric embedding $\Phi:Y\to\mathbb{R}^2$, its restriction
	to this four-point subset would be an isometric embedding of $X$ into
	$\mathbb{R}^2$, contradicting part \textnormal{(b)}.  Hence no subset of $S^2$
	containing an open hemisphere admits an isometric embedding into the plane.


	Let $X=\{a,b\}$ with $d(a,b)=\ell>0$.  An isometric embedding into
	$\mathbb{R}$ is given by
	\[
	F(a)=0,\qquad F(b)=\ell,
	\]
	since $|F(a)-F(b)|=\ell=d(a,b)$.  Likewise, into $\mathbb{R}^2$ we may choose
	$G(a)=(0,0)$ and $G(b)=(\ell,0)$.  Any map which sends $a,b$ to points at a
	different distance, or fails to be injective (for instance $K(a)=K(b)=0$), is
	\emph{not} an isometric embedding.

	Let $X=\{p_1,p_2,p_3\}$ and set
	\[
	a=d(p_1,p_2),\quad b=d(p_1,p_3),\quad c=d(p_2,p_3).
	\]
	Because $d$ is a metric, the triangle inequalities hold:
	\[
	a\le b+c,\quad b\le a+c,\quad c\le a+b.
	\]
	We now construct an isometric embedding $F:X\to\mathbb{R}^2$.

	Place
	\[
	F(p_1)=(0,0),\qquad F(p_2)=(a,0),
	\]
	and write $F(p_3)=(x,y)$.  The distance constraints become
	\[
	x^2+y^2=b^2,\qquad (x-a)^2+y^2=c^2.
	\]
	Subtracting the equations gives
	\[
	a^2-2ax=c^2-b^2,\qquad
	x=\frac{a^2+b^2-c^2}{2a}.
	\]
	Then
	\[
	y^2=b^2-x^2
	=b^2-\left(\frac{a^2+b^2-c^2}{2a}\right)^2
	=\frac{(a+b+c)(a+b-c)(a-b+c)(-a+b+c)}{16a^2}\ge 0.
	\]
	Thus $y\in\mathbb{R}$ exists and the three points
	\[
	F(p_1)=(0,0),\quad F(p_2)=(a,0),\quad F(p_3)=(x,y)
	\]
	form a Euclidean triangle whose side lengths are exactly
	$a,b,c$.  Hence every three-point metric space satisfying the triangle
	inequalities can be realised as a Euclidean triangle via an isometric
	embedding into $\mathbb{R}^2$.

	Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces.

	A \emph{topological embedding} is a continuous map $f:X\to Y$ which is
	injective and a homeomorphism from $X$ onto its image $f(X)$, equipped with
	the subspace topology.  Such a map may distort distances; it preserves only
	the topology.

	An \emph{isometric embedding} is a map $f:X\to Y$ satisfying
	\[
	d_Y(f(x),f(y)) = d_X(x,y)\qquad\text{for all }x,y\in X.
	\]
	This condition preserves the metric exactly.  In particular, if $f$ is
	distance-preserving then it is automatically injective: if $f(x)=f(y)$ then
	\[
	0 = d_Y(f(x),f(y)) = d_X(x,y),
	\]
	and since $d_X$ is a metric we must have $x=y$.  Thus an isometric embedding
	is a special kind of topological embedding which preserves all distances and
	hence all geometric information encoded by the metric.

	When we speak of an ``embedding'' we want to regard $X$ as a copy of a
	subspace of $Y$.  This requires a one-to-one correspondence between points of
	$X$ and points of the image $f(X)\subset Y$; otherwise different points of $X$
	would be identified in $Y$ and the structure of $X$ would be lost.  For
	general topological embeddings injectivity is imposed by definition; for
	isometric embeddings it follows automatically from the metric property.
```

## CP-II-0334

- chapter line: 6121

```tex
\label{prob:cp-ii-0334}
Topological vs.\ metric properties

Each item makes sense for a metric space $(X,d)$. Decide which are \emph{topological}
(depend only on the open sets) and justify.

	\par\noindent\textbullet\quad \textbf{Boundedness of a subset of $X$} — \emph{Not topological.}
On $\mathbb R$, the metrics $d(x,y)=|x-y|$ and $d'(x,y)=\min\{1,|x-y|\}$ generate the same
	topology. Then $(\mathbb R,d')$ is bounded (diameter $\le 1$) while $(\mathbb R,d)$ is unbounded.

	\par\noindent\textbullet\quad \textbf{Closedness of a subset of $X$} — \emph{Topological.}

	Closed sets are complements of open sets; hence determined by the topology alone.

	\par\noindent\textbullet\quad \textbf{“Closed and bounded” for a subset of $X$} — \emph{Not topological.}

	Closed is topological, bounded is not. With $d,d'$ as in (i), $\mathbb R$ is closed in itself and
	bounded in $(\mathbb R,d')$ but not in $(\mathbb R,d)$.

	\par\noindent\textbullet\quad \textbf{Total boundedness of $X$} — \emph{Not topological.}

	Let $h:\mathbb R\to(0,1)$ be a homeomorphism, and define $d_h(x,y)=|h(x)-h(y)|$. Then $d_h$
	induces the usual topology on $\mathbb R$, but $(\mathbb R,d_h)$ is isometric to $(0,1)$ and thus
	totally bounded, while $(\mathbb R,|\cdot|)$ is not.

	\par\noindent\textbullet\quad \textbf{Completeness of $X$} — \emph{Not topological.}

	Let $h:(0,1)\to\mathbb R$ be a homeomorphism and $\rho(x,y)=|h(x)-h(y)|$. Then $\rho$ induces the
	usual topology on $(0,1)$, but $(0,1,\rho)$ is complete (isometric to $\mathbb R$), whereas
	$(0,1,|\cdot|)$ is not complete.

	\par\noindent\textbullet\quad \textbf{“$X$ is complete and totally bounded$\,\,$”} — \emph{Topological (for metric spaces).}

	In metric spaces,
	\[
	\text{complete and totally bounded}\quad\Longleftrightarrow\quad\text{compact}.
	\]
	Compactness is a topological property; hence the conjunction is topological.
	(Neither completeness nor total boundedness alone is topological; see (iv)–(v).)
```

## CP-II-0357

- chapter line: 6189

```tex
\label{prob:cp-ii-0357}
/ Non-Example

$(\mathbb{R},\text{usual})$ is Hausdorff and second countable, while $(\mathbb{R},\text{cofinite})$ is $T_1$ but neither Hausdorff nor second countable. Therefore they are not homeomorphic, illustrating invariance.

\bigskip

\subsection*{Problem 4: Equality of the Euclidean Metric Topology and the Product Topology on $\mathbb{R}^n$}

Show that the topology on $\mathbb{R}^n$ induced by the Euclidean metric equals the product topology inherited from $\mathbb{R}$ with its usual metric.

Let $\|\cdot\|_2$ be the Euclidean norm and $\|\cdot\|_\infty$ the sup-norm on $\mathbb{R}^n$. For all $v\in\mathbb{R}^n$,
\[
\|v\|_\infty \le \|v\|_2 \le \sqrt{n}\,\|v\|_\infty.
\]
Hence for balls centered at $x\in\mathbb{R}^n$ and $r>0$,
\[
B_2(x,r)\subseteq B_\infty(x,r)\subseteq B_2\!\bigl(x,\sqrt{n}\,r\bigr).
\]
Basic product-open sets are the open boxes $\prod_{i=1}^n (a_i,b_i)=B_\infty(x,r)$.
```

## CP-II-0365

- chapter line: 6212

```tex
\label{prob:cp-ii-0365}
\par\noindent\textbullet\quad The set \((0.2,0.7)\) \emph{is} open in \(X\).

\smallskip

In Problem~4 we defined a new metric on \(X\) by
\[
d(x,y)=\left|\frac{1}{x}-\frac{1}{y}\right|.
\]

The key property required was:
\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
\text{a subset of } X \text{ is open with respect to } d
\quad\text{iff}\quad
\text{it is open in the usual Euclidean subspace topology.}
$}
\end{center}

\smallskip

That means:
\[
\text{$d$-open sets on $X$} \;=\; \text{open sets of the subspace topology from $\mathbb{R}$.}
\]

So the metric \(d\) does not change which sets are open;
it only changes the distances so that completeness is recovered.

\medskip
```

## CP-II-0367

- chapter line: 6245

```tex
\label{prob:cp-ii-0367}
\par\noindent\textbullet\quad Hence $f,g \in C_0^0(\mathbb{R})$ (continuous with compact support, $k=0$).

Their convolution is
\[
(f*g)(x) = \int_{\mathbb{R}} f(x-y)\,g(y)\,dy,
\]
which is a continuous Ă˘â‚¬Ĺ›rounded tentĂ˘â‚¬â„˘Ă˘â‚¬â„˘ supported in the interval $[-2,2]$.
```
