# Part II missing-solution batch 05

- problems: **20**
- IDs: CP-II-0471, CP-II-0475, CP-II-0494, CP-II-0495, CP-II-0498, CP-II-0500, CP-II-0506, CP-II-0514, CP-II-0523, CP-II-0530, CP-II-0532, CP-II-0533, CP-II-0539, CP-II-0540, CP-II-0544, CP-II-0545, CP-II-0547, CP-II-0548, CP-II-0549, CP-II-0551

## CP-II-0471

- chapter line: 7744

```tex
\label{prob:cp-ii-0471}
Norms on $C^1([0,1])$ and $C^1_0([0,1])$

	\par\noindent\textbullet\quad Let $C^{1}([0,1])$ be the vector space of real continuous functions on $[0,1]$ with
	continuous first derivatives. Define functions $\alpha,\beta,\gamma,\delta:C^{1}([0,1])\to\mathbb{R}$ by
	\[
	\alpha(f)=\sup_{x\in[0,1]}|f(x)|+\sup_{x\in[0,1]}|f'(x)|,\qquad
	\beta(f)=\sup_{x\in[0,1]} \big(|f(x)|+|f'(x)|\big),
	\]
	\[
	\gamma(f)=\sup_{x\in[0,1]}|f(x)|,\qquad
	\delta(f)=\sup_{x\in[0,1]}|f'(x)|.
	\]
	Which of these define norms on $C^{1}([0,1])$?
	Out of those that define norms, which pairs are Lipschitz equivalent?

	\par\noindent\textbullet\quad Let $C^{1}_{0}([0,1])$ be the set of functions $f\in C^{1}([0,1])$ such that
	$f(x)=0$ for $x$ in some neighborhood of the end points $0$ and $1$. Verify that
	$C^{1}_{0}([0,1])$ is a vector space. How would your answers in (a) change if we replace
	$C^{1}([0,1])$ by $C^{1}_{0}([0,1])$ (equivalently $C^{1}_{c}((0,1))$)?

\noindent\rule{\linewidth}{0.6pt}

	\par\noindent\textbullet\quad A norm requires positivity, absolute homogeneity, triangle inequality, and
	\emph{definiteness} ($\|f\|=0\Rightarrow f=0$ in the underlying space).
	\par\noindent\textbullet\quad For any functions $A(x),B(x)$:
	$\sup(A+B)\le \sup A+\sup B$ and $\sup A\le \sup(A+B)$, $\sup B\le \sup(A+B)$.
	\par\noindent\textbullet\quad Mean–Value Theorem: $|f(x)-f(t)|\le |x-t|\;\sup|f'|$.
	\par\noindent\textbullet\quad Lipschitz equivalence of norms $\|\cdot\|_a,\|\cdot\|_b$:
	$\exists\,c,C>0$ with $c\|f\|_a\le \|f\|_b\le C\|f\|_a$ for all $f$.

Define
\[
\alpha(f)=\|f\|_\infty+\|f'\|_\infty,\qquad
\beta(f)=\big\|\,|f|+|f'|\,\big\|_\infty,\qquad
\gamma(f)=\|f\|_\infty,\qquad
\delta(f)=\|f'\|_\infty.
\]
Then $\alpha,\beta,\gamma$ are norms on $C^1([0,1])$, while $\delta$ is not (constants have
$\delta=0$ but are nonzero). Moreover,
\[
\beta(f)\le \alpha(f)\le 2\beta(f),
\]
so $\alpha\sim\beta$. The uniform norm $\gamma$ is not equivalent to $\alpha$ or $\beta$:
take smooth spikes $f_n$ with $\|f_n\|_\infty=1$ and $\|f'_n\|_\infty\to\infty$, giving
$\gamma(f_n)=1$ yet $\alpha(f_n)\to\infty$.

The set $C^1_0([0,1])=\{f\in C^1([0,1]): f=0\ \text{on neighborhoods of }0,1\}$ is a vector space.
Now $\delta$ is a norm: if $\|f'\|_\infty=0$, then $f$ is constant; since $f=0$ near an endpoint,
$f\equiv0$. For $f\in C^1_0$ we have $\|f\|_\infty\le \|f'\|_\infty$ (choose $t$ with $f(t)=0$ and apply MVT),
hence
\[
\delta(f)\le \beta(f)\le \alpha(f)\le 2\,\delta(f).
\]
Therefore $\alpha,\beta,\delta$ are pairwise equivalent on $C^1_0([0,1])$, while $\gamma$
is dominated by $\delta$ but not equivalent to it (spike example).
Replacing $C^1_0([0,1])$ by $C^1_c((0,1))$ yields the same conclusions.

\section*{Problem 6: Open and Closed Subsets of $\mathbb{R}^2$}

Which of the following subsets of $\mathbb{R}^2$ with the Euclidean norm are open? Which are closed? (And why?)

	\par\noindent\textbullet\quad $\{(x,0): 0\le x\le 1\}$;
	\par\noindent\textbullet\quad $\{(x,0): 0< x< 1\}$;
	\par\noindent\textbullet\quad $\{(x,y): y\ne 0\}$;
	\par\noindent\textbullet\quad $\{(x,y): x\in\mathbb{Q}\ \text{or}\ y\in\mathbb{Q}\}$;
	\par\noindent\textbullet\quad $\{(x,y): y=nx \text{ for some } n\in\mathbb{N}\}\ \cup\ \{(x,y): x=0\}$;
	\par\noindent\textbullet\quad $\{(x,f(x)) : x\in\mathbb{R}\}$, where $f:\mathbb{R}\to\mathbb{R}$ is a continuous function.

A set $U\subset\mathbb{R}^2$ is open iff every $p\in U$ admits $\varepsilon>0$ with $B_\varepsilon(p)\subset U$.
A set $F\subset\mathbb{R}^2$ is closed iff it contains all its limit points (equivalently, $\mathbb{R}^2\setminus F$ is open).
If $g$ is continuous, then $g^{-1}(C)$ is closed whenever $C$ is closed, and $g^{-1}(O)$ is open whenever $O$ is open.
Graphs of continuous functions are closed: $\{(x,y): y=f(x)\}=\{(x,y): y-f(x)=0\}$ is the zero set of a continuous map.

	\par\noindent\textbullet\quad Not open (a ball around any point leaves the segment). Closed: image of compact $[0,1]$ under $x\mapsto(x,0)$, hence compact in $\mathbb{R}^2$, thus closed. \emph{Answer:} closed, not open.

	\par\noindent\textbullet\quad Not open (no interior). Not closed: the limit points $(0,0)$ and $(1,0)$ are missing. \emph{Answer:} neither.

	\par\noindent\textbullet\quad Complement is $\{(x,0)\}$, which is closed as $\{(x,y):y=0\}=(\pi_2)^{-1}(\{0\})$ where $\pi_2(x,y)=y$ is continuous. Hence the set is open. It is not closed since points with $y\to 0$ converge to the $x$-axis. \emph{Answer:} open, not closed.

	\par\noindent\textbullet\quad Not open: every open ball contains a point with both coordinates irrational. The complement
	$(\mathbb{R}\setminus\mathbb{Q})\times(\mathbb{R}\setminus\mathbb{Q})$ is not open for the same reason, so the set is not closed. \emph{Answer:} neither.

	\par\noindent\textbullet\quad Each line $\{(x,y):y=nx\}$ and $\{x=0\}$ is closed. Let $(x_k,n_k x_k)\to(x_0,y_0)$ with $n_k\in\mathbb{N}$ or $x_k=0$.
	If $x_0=0$, the limit lies on $\{x=0\}$. If $x_0\neq 0$, then $n_k=\frac{n_k x_k}{x_k}\to \frac{y_0}{x_0}$, forcing $\frac{y_0}{x_0}\in\mathbb{N}$; hence $(x_0,y_0)$ lies on one of the listed lines. Thus the union is closed. It is not open (lines have empty interior). \emph{Answer:} closed, not open.

	\par\noindent\textbullet\quad The graph $\{(x,f(x))\}$ equals $\{(x,y): y-f(x)=0\}$, the zero set of the continuous map $(x,y)\mapsto y-f(x)$. Hence it is closed. It has empty interior in $\mathbb{R}^2$, so it is not open. \emph{Answer:} closed, not open.

Line segments and lines have empty interior; removing a closed line (the $x$-axis) leaves an open set;
in (iv) both the set and its complement are dense with empty interior; graphs of continuous functions are closed.
```

## CP-II-0475

- chapter line: 7837

```tex
\label{prob:cp-ii-0475}
\par\noindent\textbullet\quad The hypothesis Ă˘â‚¬Ĺ›every continuous $f:E\to\mathbb R$ is boundedĂ˘â‚¬â„˘Ă˘â‚¬â„˘ is called
	\emph{pseudocompactness}. In metric spaces (in particular in $\mathbb R^n$),
	pseudocompact $\Longleftrightarrow$ compact; our proof used Heine--Borel.
```

## CP-II-0494

- chapter line: 7879

```tex
\label{prob:cp-ii-0494}
Continuity of Linear Operators between Normed Spaces

Let $X,Y$ be normed spaces and $T:X\to Y$ a linear map. Prove that the following are equivalent:

	\par\noindent\textbullet\quad $T$ is continuous;
	\par\noindent\textbullet\quad $T$ is continuous at $0$;
	\par\noindent\textbullet\quad $T$ is bounded: $\exists M>0$ such that $\|Tx\|_Y\le M\|x\|_X$ for all $x\in X$;
	\par\noindent\textbullet\quad $T$ is uniformly continuous on $X$.

For a linear map $T$, continuity at a single point implies continuity everywhere, since
$T(x+h)-T(x)=T(h)$. A linear operator is called \emph{bounded} if
$\|Tx\|\le M\|x\|$ for some $M$. The smallest such $M$ is
\[
\|T\|=\sup_{\|x\|\le 1}\|Tx\|.
\]
Boundedness is equivalent to continuity, and implies uniform continuity:
\(\|Tx-Ty\|=\|T(x-y)\|\le\|T\|\|x-y\|\).

	\par\noindent (1)$\Rightarrow$(2)\quad Immediate.

	\par\noindent (2)$\Rightarrow$(3)\quad Assume $T$ is continuous at $0$.
	Then $\exists\delta>0$ such that $\|x\|<\delta\Rightarrow\|Tx\|<1$.
	For arbitrary $x\ne0$ let $y=\frac{\delta}{2\|x\|}x$.
	Then $\|y\|<\delta$ and $\|Ty\|<1$, so
	\[
	\|Tx\|=\frac{2\|x\|}{\delta}\|Ty\|<\frac{2}{\delta}\|x\|.
	\]
	Hence $T$ is bounded with $M=2/\delta$.

	\par\noindent (3)$\Rightarrow$(1)\quad If $T$ is bounded, for all $x,h$ we have
	$\|T(x+h)-T(x)\|=\|Th\|\le M\|h\|$, so $T$ is continuous everywhere.

	\par\noindent (3)$\Leftrightarrow$(4)\quad From boundedness, $\|Tx-Ty\|\le M\|x-y\|$, so $T$ is uniformly continuous.
	Uniform continuity implies continuity at $0$, hence boundedness as before.

	\par\noindent\textbullet\quad $T:\mathbb{R}^2\to\mathbb{R}$, $T(x,y)=x+y$ is bounded with $\|T\|\le\sqrt2$, so continuous.
	\par\noindent\textbullet\quad $T:\ell^1\to\ell^\infty$, $T((x_n))=(n x_n)$ is linear but unbounded, hence not continuous.
```

## CP-II-0495

- chapter line: 7920

```tex
\label{prob:cp-ii-0495}
(with integrand chart)

The integrand is $f(u)=e^{-u^2}$.
It is symmetric, maximised at $u=0$ with $f(0)=1$, and decays rapidly to $0$ as $|u|\to\infty$.
This rapid decay ensures convergence of the Gaussian integral.

\begin{center}

\end{center}

This graph shows the bell-shaped curve of $e^{-u^2}$.
It is clear that the function is bounded and rapidly decays to zero outside a neighbourhood of $0$, so the area under the curve converges.
Indeed,
\[
I=\int_{-\infty}^{\infty} e^{-u^2}\,du = \sqrt{\pi}.
\]

To evaluate
\[
I=\int_{-\infty}^{\infty} e^{-u^2}\,du,
\]
we square it:
\[
I^2=\left(\int_{-\infty}^{\infty} e^{-u^2}\,du\right)
\left(\int_{-\infty}^{\infty} e^{-v^2}\,dv\right)
=\iint_{\mathbb{R}^2} e^{-(u^2+v^2)}\,du\,dv.
\]

Since the integrand depends only on $u^2+v^2=r^2$, we switch to polar coordinates:
\[
u=r\cos\theta,\quad v=r\sin\theta, \qquad du\,dv = r\,dr\,d\theta.
\]

Thus
\[
I^2=\int_0^{2\pi}\int_0^\infty e^{-r^2}\,r\,dr\,d\theta
= \left(\int_0^{2\pi} d\theta\right)\left(\int_0^\infty r e^{-r^2}\,dr\right).
\]

Let $t=r^2$, $dt=2r\,dr$:
\[
\int_0^\infty r e^{-r^2}\,dr=\tfrac{1}{2}\int_0^\infty e^{-t}\,dt=\tfrac{1}{2}.
\]

So
\[
I^2=2\pi\cdot \tfrac{1}{2}=\pi,\qquad I=\sqrt{\pi}.
\]

	\begin{theorem}[Heine--Cantor]
		Suppose that $E \subset \mathbb{R}^n$ is compact and $f:E \to \mathbb{R}^m$ is continuous on $E$.
		Then $f$ is uniformly continuous on $E$.
	\end{theorem}

	---
```

## CP-II-0498

- chapter line: 7979

```tex
\label{prob:cp-ii-0498}
\par\noindent\textbullet\quad Smooth $f\in C_c^\infty$ have rapidly decaying Haar coefficients, illustrating completeness.

	\section*{Problem 12$^{\ast}$ — Lebesgue decomposition}

	\textbf{Statement.}
	Let $(E,\mathcal{E})$ be a measurable space and let $\mu,\nu$ be finite measures on $(E,\mathcal{E})$.
	Show that there exist \emph{unique} finite measures $\nu_a,\nu_s$ such that
	\[
	\nu=\nu_a+\nu_s,\qquad \nu_a\ll \mu,\qquad \nu_s\perp \mu.
	\]

	\bigskip

	\textbf{Theory.}
```

## CP-II-0500

- chapter line: 7997

```tex
\label{prob:cp-ii-0500}
$^*$: Absolute convergence characterizes completeness

Let $(V,\|\cdot\|)$ be a normed space. Show that $V$ is complete if and only if
for every sequence $(x_n)$ in $V$ with $\sum_{j=1}^\infty \|x_j\|$ convergent,
the series $\sum_{n=1}^\infty x_n$ is convergent.
\emph{Hint.} If $(x_n)$ is Cauchy, then there is a subsequence $(x_{n_j})$
such that $\sum_j \|x_{n_{j+1}}-x_{n_j}\|<\infty$.

A series $\sum x_n$ converges iff its partial sums $s_N=\sum_{n=1}^N x_n$ converge.
If $\sum \|x_n\|<\infty$, then $(s_N)$ is Cauchy since
$\|s_m-s_n\|\le\sum_{k=n+1}^m \|x_k\|$.
In a complete space, every Cauchy sequence converges.
From a Cauchy sequence one can extract a subsequence with summable differences.

\textbf{($\Rightarrow$)} Suppose $V$ is complete and $\sum_{n=1}^\infty \|x_n\|<\infty$.
Then for $m>n$,
\[
\|s_m-s_n\|=\Big\|\sum_{k=n+1}^m x_k\Big\|
\le \sum_{k=n+1}^m \|x_k\|\xrightarrow[n,m\to\infty]{}0,
\]
so $(s_N)$ is Cauchy and converges in $V$. Hence $\sum x_n$ converges.

\textbf{($\Leftarrow$)} Assume every absolutely convergent series converges in $V$.
Let $(y_n)$ be Cauchy. Choose a subsequence $(y_{n_j})$ with
$\|y_{n_{j+1}}-y_{n_j}\|\le 2^{-j}$.
Then $\sum_{j=1}^\infty \|y_{n_{j+1}}-y_{n_j}\|\le 1$, so by the assumption the series
$\sum_{j=1}^\infty (y_{n_{j+1}}-y_{n_j})$ converges.
Its $m$-th partial sum equals $y_{n_m}-y_{n_1}$; hence $y_{n_j}\to y$ for some $y\in V$.

To prove $y_n\to y$, fix $\varepsilon>0$. Since $(y_n)$ is Cauchy, there exists $N$ such that
$\|y_n-y_m\|<\varepsilon/2$ for all $n,m\ge N$.
Choose $j$ with $n_j\ge N$ and $\|y_{n_j}-y\|<\varepsilon/2$.
Then for all $n\ge N$,
\[
\|y_n-y\|\le \|y_n-y_{n_j}\|+\|y_{n_j}-y\|<\varepsilon/2+\varepsilon/2=\varepsilon.
\]
Hence $y_n\to y$ and $V$ is complete.


Let $c_{00}$ be the space of finitely supported sequences with the $\ell^1$-norm.
Take $x_n=\frac{1}{2^n}e_n$. Then $\sum\|x_n\|_1=1$ but
$\sum x_n=(\frac{1}{2^n})_{n\ge1}\notin c_{00}$.
So absolute convergence does not imply convergence in $c_{00}$, and $c_{00}$ is not complete.

In a normed space, an absolutely convergent series always has Cauchy partial sums, but it
\emph{converges in the space} if and only if the space is complete.

\textbf{Counterexample.}
Let $c_{00}$ be the space of finitely supported sequences with the $\ell^{1}$-norm.
Define
\[
x_n = \frac{1}{2^{n}} e_n, \qquad (n\ge1),
\]
where $e_n$ is the sequence with $1$ in position $n$ and zeros elsewhere.
Then
\[
\sum_{n=1}^\infty \|x_n\|_1 = \sum_{n=1}^\infty \frac{1}{2^n} = 1 < \infty,
\]
so the series $\sum x_n$ is \emph{absolutely convergent}.
Its partial sums are
\[
s_N = \sum_{n=1}^N x_n = \bigg(\frac12, \frac14, \dots, \frac{1}{2^N}, 0, 0, \dots\bigg),
\]
which converge (in $\ell^1$) to
\[
s = \bigg(\frac12, \frac14, \frac18, \dots\bigg).
\]
However, $s\notin c_{00}$ (it is not finitely supported), so $\sum x_n$
does \emph{not} converge in $c_{00}$.

\textbf{Conclusion.}
Absolute convergence does not guarantee convergence in an incomplete space.
In contrast, in any Banach space (complete normed space), every absolutely
convergent series converges in the space.
```

## CP-II-0506

- chapter line: 8075

```tex
\label{prob:cp-ii-0506}
\par\noindent\textbullet\quad \textbf{With the sup norm $\|\cdot\|_{\infty}$.}
	$\|\cdot\|_{\infty}$ is a norm on $R([0,1])$. If $(f_n)$ is $\|\cdot\|_{\infty}$–Cauchy, then
	$f_n\to f$ uniformly for some bounded $f$, and uniform limits of Riemann–integrable functions are
	Riemann–integrable; thus $f\in R([0,1])$. Therefore $R([0,1])$ is closed in the complete space of bounded
	functions and is itself complete in $\|\cdot\|_{\infty}$.
```

## CP-II-0514

- chapter line: 8194

```tex
\label{prob:cp-ii-0514}
Which of the following subsets of $\mathbb{R}^2$ with the Euclidean topology are connected?
	Which are path-connected? (And why?)

		\par\noindent\textbullet\quad $\{(x,y)\in\mathbb{R}^2:\|(x,y)-(-1,0)\|\le1
		\text{ or }\|(x,y)-(1,0)\|<1\}$

		\par\noindent\textbullet\quad $\{(x,y)\in\mathbb{R}^2:\ x=0
		\text{ or }y=qx\text{ for }q\in\mathbb{Q}\}$

		\par\noindent\textbullet\quad $\{(x,y)\in\mathbb{R}^2:\ x=0
		\text{ or }y=qx\text{ for }q\in\mathbb{Q}\}\setminus\{(0,0)\}$

		\par\noindent\textbullet\quad $S\subset\mathbb{R}^2$ any star-shaped domain,
		i.e.\ there exists $x_0\in S$ such that for all $x\in S$
		the line segment $[x_0,x]\subset S$.


	\textbf{Theory.}
	A subset $A\subset\mathbb{R}^2$ is \emph{connected} if it cannot be written
	as the disjoint union of two non-empty open subsets in the subspace topology.
	It is \emph{path-connected} if for every $x,y\in A$ there exists a continuous
	$\gamma:[0,1]\to A$ with $\gamma(0)=x$, $\gamma(1)=y$.
	In $\mathbb{R}^n$, path-connected $\Rightarrow$ connected, but not conversely.


	\textbf{Solutions.}

	\textit{(a) Two tangent disks.}
	Let $D_1=\{(x,y):\|(x,y)-(-1,0)\|\le1\}$,
	$D_2=\{(x,y):\|(x,y)-(1,0)\|<1\}$.
	They intersect at $(0,0)$.
	Each disk is convex and hence path-connected;
	their intersection is non-empty,
	so $D_1\cup D_2$ is both connected and path-connected.

	\medskip

	\textit{(b) Rational-slope lines.}
	$A=\{(x,y):x=0\text{ or }y=qx,\ q\in\mathbb{Q}\}$.
	Each line $y=qx$ and the $y$-axis are path-connected and meet at $(0,0)$.
	Thus their union is path-connected (hence connected).

	\medskip

	\textit{(c) Same family minus the origin.}
	$B=A\setminus\{(0,0)\}$.
	Removing $(0,0)$ disconnects the family:
	each branch $L_q=\{(x,y):y=qx,\ x\neq0\}$ and $L_0=\{(0,y):y\neq0\}$
	is still path-connected, but the branches are disjoint.
	No path can move from one branch to another without passing through $(0,0)$.
	Hence $B$ is disconnected.
	Each component (each branch) remains path-connected.

	\medskip

	\textit{(d) Star-shaped domain.}
	If $S$ is star-shaped with center $x_0$,
	then for each $x\in S$ the path
	$\gamma_x(t)=(1-t)x_0+t\,x$ ($t\in[0,1]$)
	lies in $S$, joining $x_0$ and $x$.
	Thus $S$ is path-connected, hence connected.


	\textbf{Summary table.}

	\begin{center}
		\begin{tabular}{c|l|c|c}
			Case & Description & Connected & Path-connected\\\hline
			(a) & Two tangent disks & Yes & Yes\\
			(b) & Rational-slope lines (fan) & Yes & Yes\\
			(c) & Fan without the origin & No & No (each branch yes)\\
			(d) & Star-shaped domain & Yes & Yes
		\end{tabular}
	\end{center}

	\par\medskip\noindent\textbf{Problem 7 — Intersection of Nested Compact Connected Sets}\par
```

## CP-II-0523

- chapter line: 8320

```tex
\label{prob:cp-ii-0523}
\par\noindent\textbullet\quad if $x,y\le R+1$: done by compact uniform continuity on $[0,R+1]$;
```

## CP-II-0530

- chapter line: 8325

```tex
\label{prob:cp-ii-0530}
— Wiener and Vitali covering lemmas

\textbf{(a) Finite family, factor $3$.}
Given open balls $B_1,\dots,B_N\subset\mathbb{R}^n$, there exist indices $i_1,\dots,i_k$ with
$B_{i_1},\dots,B_{i_k}$ pairwise disjoint such that
\[
\bigcup_{i=1}^{N} B_i \subset \bigcup_{j=1}^{k} 3B_{i_j},
\qquad\text{hence}\qquad
\Bigl|\bigcup_{i=1}^{N} B_i\Bigr| \le 3^n\sum_{j=1}^{k}|B_{i_j}|.
\]

\textit{Proof.}
Select greedily a ball of maximal radius, delete all balls it meets, and iterate.
The selected family is disjoint.
If $B$ was deleted because it meets a selected ball $B^\ast$ with radius $\ge$ radius$(B)$,
then $B\subset 3B^\ast$.
Therefore $\bigcup_i B_i \subset \bigcup_j 3B_{i_j}$ and $|3B|=3^n|B|$ yields the measure bound.

\medskip
\textbf{(b) Vitali, factor $5$.}
Let $\{B_j:j\in J\}$ be any family of balls with $\operatorname{rad}(B_j)\le R$.
There exists a countable disjoint subfamily $\{B_j:j\in J'\}$ with
\[
\bigcup_{i\in J} B_i \subset \bigcup_{j\in J'} 5B_j .
\]

\textit{Proof.}
Order by decreasing radius and run the same greedy algorithm; radii $\le R$ imply
a maximal disjoint subfamily is countable (each contains a distinct rational point).
If $x\in B$ for some original $B$ that is not chosen, then when $B$ was removed it met
a chosen ball $B^\ast$ with radius $\ge$ radius$(B)$, whence $B\subset 5B^\ast$ by a geometric estimate.
Thus the stated inclusion holds.

\clearpage
\subsection*{Examples of functions in $L^r(\mathbb{R}^n)\cap L^\infty(\mathbb{R}^n)$}

Here are several illustrative examples of measurable functions on $\mathbb{R}^n$
that belong to both $L^r$ and $L^\infty$ for some fixed $1\le r<\infty$.
Each example includes a short justification and (where possible) explicit norms.

\bigskip

If $\mathrm{supp}\,f\subset E$ with $|E|<\infty$ and $\|f\|_\infty=M<\infty$, then
\[
\|f\|_{L^r} \le M\,|E|^{1/r}
\qquad\Longrightarrow\qquad
f\in L^r\cap L^\infty.
\]
\textbf{Concrete example.} The indicator of a unit ball:
\[
f(x)=\mathbf{1}_{B(0,1)}(x)
\quad\Rightarrow\quad
\|f\|_\infty=1,\quad
\|f\|_{L^r}=|B(0,1)|^{1/r}=(\omega_n)^{1/r}.
\]
\textbf{Another example.} A ``hat'' (Lipschitz) bump:
\[
f(x)=\max\{0,1-|x|\},
\qquad
\mathrm{supp}\,f\subset B(0,1),\quad
\|f\|_\infty=1,\ f\in L^r.
\]

\bigskip

\[
f(x)=(1+|x|)^{-\alpha},\qquad \alpha>\frac{n}{r}.
\]
Then $0<f\le1\Rightarrow f\in L^\infty$, and
in spherical coordinates
\[
\int_{\mathbb{R}^n}(1+|x|)^{-\alpha r}dx
<\infty \quad\Longleftrightarrow\quad
\alpha r>n.
\]
Hence $f\in L^r$ whenever $\alpha>n/r$.
\textbf{Easy pick:} $\alpha=\tfrac{n}{r}+1$ works for any $r,n$.

\bigskip

\[
f(x)=\frac{\sin|x|}{(1+|x|)^{\alpha}},\qquad \alpha>\frac{n}{r}.
\]
Then $|f(x)|\le (1+|x|)^{-\alpha}$, so the same integrability condition applies.
Boundedness is clear from $|\sin|x||\le1$.

\bigskip

\[
f(x)=\min(1,|x|^{-\beta}),\qquad \beta>\frac{n}{r}.
\]
Then $f\le1\Rightarrow f\in L^\infty$.
Away from the origin, $\int_{|x|\ge1}|x|^{-\beta r}dx<\infty$ when $\beta r>n$, so $f\in L^r$.
Near $0$, $f=1$ is bounded, hence no singularity occurs.

\bigskip

Let $(Q_k)_{k\ge1}$ be disjoint cubes with finite measure, and define
\[
f(x)=\sum_{k=1}^\infty a_k\,\mathbf{1}_{Q_k}(x),
\qquad |a_k|\le1,\quad
\sum_{k=1}^\infty |a_k|^r|Q_k|<\infty.
\]
Then $\|f\|_\infty\le1$ and $\|f\|_{L^r}^r=\sum_k |a_k|^r|Q_k|<\infty$,
so $f\in L^r\cap L^\infty$.

\bigskip

 \par\noindent\textbullet\quad sep4pt
	\par\noindent\textbullet\quad $f\equiv1$: in $L^\infty$ but not in $L^r$ on $\mathbb{R}^n$ (non-integrable tail).
	\par\noindent\textbullet\quad $f(x)=|x|^{-\beta}\mathbf{1}_{\{|x|\le1\}}$, $0<\beta<\tfrac{n}{r}$:
	in $L^r$ but not in $L^\infty$ (unbounded at $0$).

\par\medskip\noindent\textbf{Examples in $L^r(\mathbb{R}^n)\cap L^\infty(\mathbb{R}^n)$.}\quad

	\par\noindent\textbullet\quad $\mathbf 1_{B(0,1)}$: $\|\,\cdot\,\|_\infty=1$, $\|\,\cdot\,\|_{L^r}=\omega_n^{1/r}$.
	\par\noindent\textbullet\quad $(1+|x|)^{-\alpha}$ with $\alpha>n/r$ (bounded and $\alpha r>n$ ensures $L^r$).
	\par\noindent\textbullet\quad $\dfrac{\sin|x|}{(1+|x|)^\alpha}$ with $\alpha>n/r$.
	\par\noindent\textbullet\quad $\min\!\bigl(1,\,|x|^{-\beta}\bigr)$ with $\beta>n/r$.
	\par\noindent\textbullet\quad $\displaystyle f=\sum_{k\ge1} a_k\,\mathbf 1_{Q_k}$, $|a_k|\le1$, disjoint $Q_k$, and
	$\sum |a_k|^r|Q_k|<\infty$.
```

## CP-II-0532

- chapter line: 8450

```tex
\label{prob:cp-ii-0532}
{Polynomial characterization of holomorphicity on Runge domains}{poly-char}
	Let $U\subset\mathbb C$ be bounded, open, and suppose $\mathbb C\setminus U$ is connected.
	Show that $f:U\to\mathbb C$ is holomorphic iff for every compact $K\Subset U$ and every
	$\varepsilon>0$ there exists a polynomial $P$ with
	\[
	\sup_{z\in K}|f(z)-P(z)|<\varepsilon.
	\]
```

## CP-II-0533

- chapter line: 8461

```tex
\label{prob:cp-ii-0533}
Let $(X,d)$ be a metric space. In the definition of the topology of $(X,d)$, why donĂ˘â‚¬â„˘t we require arbitrary (possibly infinite) intersections of open sets to be open? Give a counterexample with $X=\mathbb{R}$.

In a metric space $(X,d)$, a set $U\subset X$ is open if for every $x\in U$ there exists $r>0$ such that the open ball $B(x,r)=\{y\in X:\ d(x,y)<r\}\subset U$. It follows immediately that:

\par\noindent\textbullet\quad arbitrary unions of open sets are open;
\par\noindent\textbullet\quad finite intersections of open sets are open (take the minimum of finitely many witness radii).

However, these arguments do not extend to infinite families of open sets.
```

## CP-II-0539

- chapter line: 8473

```tex
\label{prob:cp-ii-0539}
\par\noindent\textbullet\quad \textbf{Mixed measure:}
		Let $\mu=m$ (Lebesgue) on $\mathbb R$, and set
		$\displaystyle \nu = f\,m \;+\; \sum_{k=1}^\infty a_k\,\delta_{x_k}$
		with $f\in L^1(m)$ and $a_k\ge0$.
		Then the Lebesgue decomposition of $\nu$ w.r.t.\ $\mu$ is
		$\nu_a=f\,m$ and $\nu_s=\sum_{k\ge1} a_k\,\delta_{x_k}$.

	\bigskip

	The Lebesgue decomposition and Radon--Nikodym theorems both extend to $\sigma$-finite measures.
	For signed or complex measures, combine the Jordan (Hahn) decomposition with the Lebesgue decomposition.
	In harmonic analysis, decomposing a Borel measure on a locally compact group into its absolutely continuous
	part w.r.t.\ Haar measure and its singular part is fundamental (e.g.\ spectral decompositions).

	We write \(m\) for Lebesgue measure on \(\mathbb{R}^n\).
	The notation \(\int_A f\,dm\) means integration with respect to \(m\)
	(i.e.\ \(\int_A f(x)\,dx\) in classical notation), explicitly indicating the underlying measure.

	\bigskip

	Let \(f\in L^1(m)\) and define \(\nu(A):=\int_A f\,dm\) for Borel \(A\).
	If \(m(A)=0\), then \(\int_A |f|\,dm=0\), hence
	\[
	|\nu(A)|=\left|\int_A f\,dm\right|\le \int_A |f|\,dm=0,
	\]
	so \(\nu(A)=0\). Therefore \(\nu\ll m\).
	This remains true for signed or complex \(f\in L^1(m)\) by using \(\int_A |f|\,dm\).

	\bigskip

	A measure \(\mu\) on \((E,\mathcal E)\) is \(\sigma\)-finite if
	\(E=\bigcup_{k=1}^\infty E_k\) with \(\mu(E_k)<\infty\) for all \(k\).
	Lebesgue measure \(m\) on \(\mathbb{R}^n\) is \(\sigma\)-finite since
	\(\mathbb{R}^n=\bigcup_{k=1}^\infty [-k,k]^n\) and each cube has finite measure.
	The Radon--Nikodym and Lebesgue decomposition theorems hold under \(\sigma\)-finiteness.

	\bigskip

	For \(x\in E\), the Dirac measure \(\delta_x\) is defined by \(\delta_x(A)=\mathbf{1}_A(x)\).
	On \(\mathbb{R}^n\) with Lebesgue measure \(m\), we have \(\delta_x\perp m\),
	since \(\delta_x\) is supported on the \(m\)-null set \(\{x\}\).
	In general, any atomic part \(\sum_k a_k \delta_{x_k}\) of a measure is singular w.r.t.\ \(m\).

	\bigskip

	Let \(C\subset[0,1]\) be the middle-third Cantor set.
	The Cantor measure \(\gamma\) is the unique Borel probability measure satisfying
	\[
	\gamma(A)=\tfrac12\,\gamma(3A)+\tfrac12\,\gamma(3A-2),
	\]
	equivalently, the measure whose distribution function is the Devil's staircase.
	It is \emph{singular continuous}: it has no atoms (\(\gamma(\{x\})=0\) for all \(x\))
	and is supported on \(C\) with \(m(C)=0\). Hence \(\gamma\perp m\).

	\bigskip

	On \(\mathbb{R}^n\) with background measure \(m\), any finite measure \(\nu\) decomposes uniquely as
	\[
	\nu=\nu_a+\nu_s,\qquad \nu_a\ll m,\quad \nu_s\perp m.
	\]
	Typical instances:
```

## CP-II-0540

- chapter line: 8538

```tex
\label{prob:cp-ii-0540}
\par\noindent (b)\quad For each $i\in\{1,\dots,n\}$ and $h\neq 0$ the difference
		quotient operator
		\[
		(\Delta_i^h\phi)(x)
		:= \frac{\phi(x+he_i)-\phi(x)}{h}
		\]
		is a continuous linear map on $\mathcal{E}(\mathbb{R}^n)$, and
		for every $\phi\in\mathcal{E}(\mathbb{R}^n)$ one has
		\[
		\Delta_i^h\phi \longrightarrow D_i\phi
		\quad\text{in }\mathcal{E}(\mathbb{R}^n)
		\quad\text{as } h\to 0.
		\]



\begin{proof}
	Fix a compact $K\subset\mathbb{R}^n$ and $m\in\mathbb{N}$.

	\emph{(a) Translations.}
	For $|\alpha|\le m$ we have
	\[
	D^\alpha(\tau_x\phi)(y)=D^\alpha\phi(y-x).
	\]
	If $x_l\to 0$, choose a compact set $K'$ containing $K$ and $K-x_l$ for
	all $l$ large.  Then $D^\alpha\phi$ is uniformly continuous on $K'$, so
	given $\varepsilon>0$ there exists $\delta>0$ such that
	$|z-z'|<\delta\Rightarrow |D^\alpha\phi(z)-D^\alpha\phi(z')|<\varepsilon$
	for all $z,z'\in K'$.  For $l$ large enough we have $|x_l|<\delta$ and
	therefore
	\[
	\sup_{y\in K} |D^\alpha\phi(y-x_l)-D^\alpha\phi(y)|
	\le \varepsilon.
	\]
	Taking the supremum over $|\alpha|\le m$ yields
	$p_{K,m}(\tau_{x_l}\phi-\phi)\to 0$, i.e.\ $\tau_{x_l}\phi\to\phi$ in
	$\mathcal{E}(\mathbb{R}^n)$.

	\medskip\noindent
	\emph{(b) Difference quotients.}
	Let $g(x) := D^\alpha\phi(x)$ for some $|\alpha|\le m$.  Then
	\[
	D^\alpha(\Delta_i^h\phi)(x)
	= \frac{g(x+he_i)-g(x)}{h}.
	\]
	By the mean value theorem,
	\[
	\frac{g(x+he_i)-g(x)}{h} = D_i g(x+\theta h e_i)
	\]
	for some $\theta=\theta(x,h)\in(0,1)$.  Choosing a compact $K'$ containing
	$K$ and $K+he_i$ for all $|h|$ small, we see that $D_i g$ is uniformly
	continuous on $K'$.  Hence for every $\varepsilon>0$ there exists
	$\delta>0$ such that for $|h|<\delta$,
	\[
	\sup_{x\in K}
	\bigl|D^\alpha(\Delta_i^h\phi)(x)-D_iD^\alpha\phi(x)\bigr|
	= \sup_{x\in K}
	|D_i g(x+\theta h e_i)-D_i g(x)|
	< \varepsilon.
	\]
	Taking the supremum over $|\alpha|\le m$ shows that
	$p_{K,m}(\Delta_i^h\phi - D_i\phi)\to 0$ as $h\to 0$, which is precisely
	$\Delta_i^h\phi\to D_i\phi$ in $\mathcal{E}(\mathbb{R}^n)$.
\end{proof}
```

## CP-II-0544

- chapter line: 8606

```tex
\label{prob:cp-ii-0544}
\par\noindent\textbullet\quad \textbf{Bounded:} $|f(x)|\le 1/(x+1)\le1$.
	\textbf{Uniformly continuous:} yes. Given $\varepsilon>0$, choose $R$ with $2/(R+1)<\varepsilon/2$.
	If $x,y\ge R$ then $|f(x)-f(y)|\le 2/(R+1)<\varepsilon/2$.
	On $[0,R+1]$, $f$ is continuous on a compact set, hence uniformly continuous;
	choose $\delta\le1$ to combine the cases.

\bigskip
```

## CP-II-0545

- chapter line: 8617

```tex
\label{prob:cp-ii-0545}
\par\noindent\textbullet\quad \emph{Cauchy sequence}: $(y_n)$ is Cauchy if for every $\varepsilon>0$ there exists $N$ such that
	$d(y_m,y_n)<\varepsilon$ for all $m,n\ge N$.
```

## CP-II-0547

- chapter line: 8623

```tex
\label{prob:cp-ii-0547}
\par\noindent\textbullet\quad \emph{Complete}: every Cauchy sequence converges in $X$.
```

## CP-II-0548

- chapter line: 8628

```tex
\label{prob:cp-ii-0548}
Let $(X,d)$ be a metric space.

Show that the union of any collection of open subsets of $X$ must be open (regardless of whether
the collection is finite, countable or uncountable), and that the intersection of any finite
collection of open subsets is again open. Formulate and prove similar properties about the
closed subsets of $X$.

Let $E$ be a subset of $X$. Show that there is a unique largest open subset $E^\circ$ of $X$
contained in $E$, i.e.\ a unique open subset $E^\circ$ of $X$ such that $E^\circ\subset E$ and if
$G$ is any open subset of $X$ with $G\subset E$ then $G\subset E^\circ$. The set $E^\circ$ is
called the \emph{interior} of $E$ in $X$. Show also that there is a unique smallest closed subset
$\overline{E}$ of $X$ containing $E$, i.e.\ a unique closed subset $\overline{E}$ of $X$ with
$E\subset \overline{E}$ and if $F$ is any closed subset of $X$ with $E\subset F$ then
$\overline{E}\subset F$. The set $\overline{E}$ is called the \emph{closure} of $E$ in $X$.

Show that
\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
E^\circ=\{\,x\in X:\ B_\varepsilon(x)\subset E\ \text{for some }\varepsilon>0\,\}
\qquad\text{and}\qquad
\overline{E}=\{\,x\in X:\ x_n\to x\ \text{for some sequence }(x_n)\subset E\,\}.
$}
\end{center}

\bigskip
\noindent\textbf{Theory (tools and facts).}

	\par\noindent\textbullet\quad \textbf{Open/closed set algebra.}

		\par\noindent\textbullet\quad Arbitrary unions of open sets are open; finite intersections of open sets are open.
		\par\noindent\textbullet\quad Arbitrary intersections of closed sets are closed; finite unions of closed sets are closed.
		\par\noindent\textbullet\quad Complement duality: $U$ open $\Leftrightarrow$ $X\setminus U$ closed.

	\par\noindent\textbullet\quad \textbf{Open balls.} For $x\in X$ and $\varepsilon>0$,
	\[
	B_\varepsilon(x)=\{y\in X:\ d(x,y)<\varepsilon\}
	\]
	is open; every open set is a union of open balls.

	\par\noindent\textbullet\quad \textbf{Interior.}
	\[
	E^\circ=\bigcup\{\,G\subset X:\ G\ \text{open and } G\subset E\,\}
	\]
	is open, satisfies $E^\circ\subset E$, and is the largest open subset of $E$.
	Metric characterisation:
	\[
	x\in E^\circ\ \Longleftrightarrow\ \exists\,\varepsilon>0:\ B_\varepsilon(x)\subset E.
	\]

	\par\noindent\textbullet\quad \textbf{Closure.}
	\[
	\overline{E}=\bigcap\{\,F\subset X:\ F\ \text{closed and } E\subset F\,\}
	\]
	is closed, contains $E$, and is the smallest closed set containing $E$.
	Equivalent characterisations:
	\[
	x\in\overline{E}\ \Longleftrightarrow\ \forall\,\varepsilon>0,\ B_\varepsilon(x)\cap E\neq\varnothing
	\ \Longleftrightarrow\ \exists\ (x_n)\subset E\ \text{with } x_n\to x.
	\]

	\par\noindent\textbullet\quad \textbf{Limit points.} $x$ is a limit (accumulation) point of $E$ iff every ball
	$B_\varepsilon(x)$ intersects $E\setminus\{x\}$; then $x\in\overline{E}$.

	\par\noindent\textbullet\quad \emph{Arbitrary union of open sets is open.}
	If $x\in\bigcup_{i\in I}U_i$ with each $U_i$ open, then $x\in U_j$ for some $j$,
	so $\exists\,\varepsilon>0$ with $B_\varepsilon(x)\subset U_j\subset\bigcup_{i\in I}U_i$.
	\par\noindent\textbullet\quad \emph{Finite intersection of open sets is open.}
	If $x\in\bigcap_{k=1}^m U_k$, pick $\varepsilon_k>0$ with $B_{\varepsilon_k}(x)\subset U_k$.
	Then $B_{\min_k \varepsilon_k}(x)\subset\bigcap_{k=1}^m U_k$.
	\par\noindent\textbullet\quad \emph{Closed sets (duals).}
	Arbitrary intersections of closed sets are closed, and finite unions of closed sets are closed
	(by complements of the two statements above).

\noindent\hrulefill

Define
\[
E^\circ=\bigcup\{G\subset X:\ G\ \text{open and}\ G\subset E\},\qquad
\overline E=\bigcap\{F\subset X:\ F\ \text{closed and}\ E\subset F\}.
\]
Then $E^\circ$ is open, $E^\circ\subset E$, and if $G$ is open with $G\subset E$ then $G\subset E^\circ$;
hence $E^\circ$ is the unique largest open subset of $X$ contained in $E$.
Also $\overline E$ is closed, $E\subset\overline E$, and if $F$ is closed with $E\subset F$,
then $\overline E\subset F$; hence $\overline E$ is the unique smallest closed subset of $X$
containing $E$.

\noindent\hrulefill

\begin{align*}
	E^\circ&=\{x\in X:\ \exists\,\varepsilon>0\ \text{with}\ B_\varepsilon(x)\subset E\},\\
	\overline E&=\{x\in X:\ \exists\ (x_n)\subset E\ \text{with}\ x_n\to x\}.
\end{align*}
\emph{Proof of the first:} If $x\in E^\circ$, then $x$ lies in some open $G\subset E$, so
$B_\varepsilon(x)\subset G\subset E$ for some $\varepsilon>0$.
Conversely, if $B_\varepsilon(x)\subset E$, then $x$ lies in the open set $B_\varepsilon(x)\subset E$,
hence $x\in E^\circ$.

\emph{Proof of the second:} If $x\in\overline E$, then every ball $B_{1/n}(x)$ meets $E$; pick
$x_n\in E\cap B_{1/n}(x)$ to get $x_n\to x$. Conversely, if $x_n\in E$ and $x_n\to x$, then every
neighbourhood of $x$ contains some $x_n\in E$, so every ball around $x$ meets $E$, hence
$x\in\overline E$.
```

## CP-II-0549

- chapter line: 8733

```tex
\label{prob:cp-ii-0549}
— Characterization on a Runge domain

Let $U\subset\mathbb C$ be bounded and assume $\mathbb C\setminus U$ is connected.
Show that $f:U\to\mathbb C$ is holomorphic iff for every compact $K\subset U$ and $\varepsilon>0$
there exists a polynomial $P$ with $\sup_{K}|f-P|<\varepsilon$.

If $\mathbb C\setminus U$ is connected, $U$ is a Runge domain; by the
Runge–Oka–Weil theorem, holomorphic functions on $U$ can be uniformly approximated on compacts
by polynomials. Uniform limits of holomorphic functions on open sets are holomorphic.

($\Rightarrow$) For $f\in\mathcal O(U)$ and $K\Subset U$, Runge–Oka–Weil yields a polynomial $P$
with $\sup_{K}|f-P|<\varepsilon$.
($\Leftarrow$) If for each $K\Subset U$ there are polynomials $P_n$ with $P_n\to f$ uniformly on $K$,
then by Weierstrass $f$ is holomorphic on $K^\circ$, hence on $U$.

\noindent\rule{\textwidth}{0.4pt}

\bigskip
```

## CP-II-0551

- chapter line: 8755

```tex
\label{prob:cp-ii-0551}
— Riesz' Lemma and non-compactness of the unit ball

Let $X$ be a normed space, $V\subset X$ a proper closed subspace, and $0<\alpha<1$.
	There exists $x\in X$ with $\|x\|=1$ such that $\|x-y\|\ge \alpha$ for all $y\in V$.

	\emph{Proof.}
	Pick $x_{0}\notin V$ and set $d:=\operatorname{dist}(x_{0},V)>0$.
	Choose $v\in V$ with $\|x_{0}-v\|<d/\alpha$, and define $x:=(x_{0}-v)/\|x_{0}-v\|$.
	For any $y\in V$,
	\[
	\|x-y\|
	=\frac{\|x_{0}-(v+\|x_{0}-v\|\,y)\|}{\|x_{0}-v\|}
	\ge \frac{d}{\|x_{0}-v\|}>\alpha,
	\]
	since $v+\|x_{0}-v\|\,y\in V$. Hence $\|x-y\|\ge\alpha$ for all $y\in V$.


	Let $X$ be an infinite-dimensional Banach space.

	Inductively construct $(x_{k})$ in the unit sphere by applying Riesz' lemma with $\alpha=\tfrac12$
	to the nested closed subspaces $V_{k}=\overline{\operatorname{span}}\{x_{1},\dots,x_{k}\}$.

	Then $\|x_{i}-x_{j}\|\ge\tfrac12$ for $i\ne j$, so the unit ball contains a sequence with no
	Cauchy (hence no convergent) subsequence. Therefore the unit ball of $X$ is not compact.

	Every bounded sequence in a finite dimensional normed space has a convergent subsequence.
	Equivalently, the closed unit ball is compact.

	If $X$ is infinite dimensional, the closed unit ball of $X$ is not compact (indeed, not sequentially compact).
	There exists a bounded sequence with no Cauchy subsequence.

		\par\noindent\textbullet\quad In $\ell^2$, let $e_n$ be the standard basis. Then $\|e_n\|=1$ and
		$\|e_n-e_m\|=\sqrt{2}$ for $n\neq m$; hence no Cauchy subsequence exists.
		\par\noindent\textbullet\quad In $L^p$ $(1\le p<\infty)$, choose pairwise disjoint measurable sets $E_n$ with $0<m(E_n)<\infty$, and set
		$x_n:=\mathbf 1_{E_n}/\|\mathbf 1_{E_n}\|_p$. Then $\|x_n\|_p=1$ and
		$\|x_n-x_m\|_p=(\|x_n\|_p^p+\|x_m\|_p^p)^{1/p}=2^{1/p}$ for $n\ne m$.

	\bigskip

	Let $X$ be a normed space, $V\subset X$ a proper closed subspace, and $0<\alpha<1$.
	There exists $x\in X$ with $\|x\|=1$ and $\operatorname{dist}(x,V)\ge \alpha$.

	With $V_k=\overline{\operatorname{span}}\{x_1,\dots,x_k\}$ and $\alpha=\tfrac12$,
	one can construct a sequence $(x_k)$ in the unit sphere such that
	$\|x_i-x_j\|\ge \tfrac12$ for $i\ne j$, proving the unit ball of an infinite dimensional Banach space is not compact.

		\par\noindent\textbullet\quad \textbf{In $\ell^2$:} take $V_k=\operatorname{span}\{e_1,\dots,e_k\}$ and $x_{k+1}=e_{k+1}$;
		then $\operatorname{dist}(x_{k+1},V_k)=1$.
		\par\noindent\textbullet\quad \textbf{In $L^p$:} pick disjoint sets $(E_k)$ with $0<m(E_k)<\infty$, set
		\[
		x_k=\frac{\mathbf 1_{E_k}}{\|\mathbf 1_{E_k}\|_p},\qquad V_k=\operatorname{span}\{x_1,\dots,x_k\}.
		\]
		For any $y\in V_k$, $y=0$ a.e.\ on $E_{k+1}$, so
		\[
		\|x_{k+1}-y\|_p^p \ge \int_{E_{k+1}} |x_{k+1}|^p = 1,
		\]
		hence $\operatorname{dist}(x_{k+1},V_k)=1$ and $\|x_i-x_j\|_p=2^{1/p}$ for $i\ne j$.

	\bigskip

	To produce the nested closed subspaces used with Riesz' lemma in the $L^p$ setting, fix disjoint measurable sets
	$E_k$ with $0<m(E_k)<\infty$ and define
	\[
	x_k:=\frac{\mathbf 1_{E_k}}{\|\mathbf 1_{E_k}\|_p},\qquad
	V_k:=\overline{\operatorname{span}}\{x_1,\dots,x_k\}.
	\]
	Then $x_{k+1}$ has distance $1$ from $V_k$, giving a concrete Riesz sequence and proving the unit ball is not compact.

	Let $(\Omega,\mathcal{F},\mu)$ be a $\sigma$-finite measure space and $1\le p\le\infty$.
	We construct nested finite-dimensional subspaces $V_k$ and a sequence $(x_k)$ in the unit sphere
	with $\operatorname{dist}(x_{k+1},V_k)=1$ for all $k$, yielding a concrete ``Riesz sequence''
	and the non-compactness of the unit ball.

	\bigskip

	Because $\mu$ is $\sigma$-finite, we can choose pairwise disjoint measurable sets
	$(E_k)_{k\ge1}$ with $0<\mu(E_k)<\infty$.

		\par\noindent\textbullet\quad On $(\mathbb{R}^n,\mathcal{B},m)$, one convenient choice is the dyadic cubes
		\[
		E_k = \bigl((k-1,k]\times(0,1]^{n-1}\bigr) \quad (k\ge1),
		\]
		or on $[0,1]$ the dyadic subintervals
		$E_k = \bigl((2^{-k},2^{-(k-1)}]\bigr)$.
		\par\noindent\textbullet\quad On a non-atomic probability space, recursively bisect any set of positive measure to obtain
		an infinite disjoint family of positive-measure sets.

	\bigskip

	For $1\le p<\infty$ define
	\[
	x_k := \frac{\mathbf{1}_{E_k}}{\|\mathbf{1}_{E_k}\|_{L^p}}
	= \frac{\mathbf{1}_{E_k}}{\mu(E_k)^{1/p}},
	\qquad \|x_k\|_{L^p}=1.
	\]
	For $p=\infty$, simply set $x_k:=\mathbf{1}_{E_k}$ so that $\|x_k\|_\infty=1$.

	\bigskip

	Let
	\[
	V_k := \operatorname{span}\{x_1,\dots,x_k\}.
	\]
	(Each $V_k$ is finite dimensional, hence closed, so the closure bar is superfluous:
	$\overline{\operatorname{span}}\{x_1,\dots,x_k\}=V_k$.)

	\bigskip

	Fix $k\ge1$ and $y\in V_k$, say $y=\sum_{j=1}^k a_j x_j$.
	Because the supports are disjoint, $y=0$ a.e.\ on $E_{k+1}$.
	Therefore
	\[
	\|x_{k+1}-y\|_{L^p}^p
	= \int_{E_{k+1}} |x_{k+1}|^p\,d\mu \;+\; \int_{\Omega\setminus E_{k+1}} |y|^p\,d\mu
	\ge \int_{E_{k+1}} |x_{k+1}|^p\,d\mu
	= 1.
	\]
	Taking $y=0$ shows the infimum is attained, hence
	\[
	\operatorname{dist}(x_{k+1},V_k)=\inf_{y\in V_k}\|x_{k+1}-y\|_{L^p}=1.
	\]
	Consequently, for $i\neq j$,
	\[
	\|x_i-x_j\|_{L^p}^p
	= \|x_i\|_{L^p}^p + \|x_j\|_{L^p}^p
	= 2 \quad\Longrightarrow\quad \|x_i-x_j\|_{L^p}=2^{1/p}.
	\]

	\bigskip

	For $y\in V_k$, again $y=0$ on $E_{k+1}$, so
	\[
	\|x_{k+1}-y\|_\infty
	= \operatorname*{ess\,sup}_{\omega\in\Omega} |x_{k+1}(\omega)-y(\omega)|
	\ge \operatorname*{ess\,sup}_{\omega\in E_{k+1}} |x_{k+1}(\omega)|
	= 1.
	\]
	With $y=0$ we get $\operatorname{dist}(x_{k+1},V_k)=1$, and for $i\neq j$,
	$\|x_i-x_j\|_\infty=1$ (since the values are $1$ on $E_i$, $0$ there for $x_j$, and vice versa).

	\bigskip

		\par\noindent\textbullet\quad \textbf{Riesz sequence.} The unit sphere of $L^p$ contains a sequence $(x_k)$ with
		$\|x_i-x_j\|\ge c_p$ for $i\ne j$, where $c_p=2^{1/p}$ for $1\le p<\infty$ and $c_\infty=1$.
		Thus the closed unit ball is not (sequentially) compact.
		\par\noindent\textbullet\quad \textbf{Explicit Riesz lemma step.} With $V_k$ as above and any $0<\alpha<1$,
		the vector $x_{k+1}$ satisfies $\|x_{k+1}\|=1$ and $\operatorname{dist}(x_{k+1},V_k)=1\ge\alpha$,
		giving the Riesz–lemma vector at step $k$ without any abstract selection.

	\bigskip

	Let $F_k$ be sets with $\mu(F_k)>0$ and $\mu(F_i\cap F_j)=0$ for $i\neq j$ \emph{except} possibly on
	small overlaps of measure at most $\varepsilon_k>0$. Define
	$x_k=\mathbf{1}_{F_k}/\mu(F_k)^{1/p}$ ($1\le p<\infty$).
	Then for $y\in V_k$,
	\[
	\|x_{k+1}-y\|_{L^p}^p
	\ge 1 - C_p\,\varepsilon_{k+1}
	\quad\text{with a constant }C_p \text{ depending only on }p.
	\]
	Choosing $\varepsilon_{k}\downarrow0$ fast, one still gets a sequence bounded away from $V_k$,
	showing non-compactness. This is sometimes convenient when one constructs localized bumps $\varphi_k$
	with small overlaps instead of strict indicators.

	\bigskip

	\noindent
	In Exercise~3 we considered a bounded linear functional
	$u:L^{p}(\Omega)\to\mathbb{R}$ and constructed from it the auxiliary map
	$\tilde u$ on nonnegative functions together with the linear functional
	\[
	w(f)=\tilde u(f^{+})-\tilde u(f^{-})
	\qquad (f\in L^{p}).
	\]
	The sequence $(x_k)$ and subspaces $(V_k)$ above give a concrete geometric
	framework in which one can \emph{visualize} the decomposition $u=w-(w-u)$
	into its positive and negative parts.

	\medskip

	\noindent
	Because the functions $x_k$ have pairwise disjoint supports, any
	$f\in V_k$ can be written uniquely as a finite linear combination
	\[
	f = a_1 x_1 + a_2 x_2 + \dots + a_k x_k,
	\qquad  a_j\in\mathbb{R}.
	\]
	On such simple functions, a bounded linear functional $u$
	is completely determined by its values on the basis $\{x_1,\dots,x_k\}$:
	\[
	u(f) = \sum_{j=1}^{k} a_j\,u(x_j).
	\]
	If we denote $c_j:=u(x_j)$, then the action of $u$ on $V_k$
	is given by the coordinate functional
	$f\mapsto\sum_{j=1}^{k} c_j a_j$.
	In this coordinate form, the \emph{positive} and \emph{negative} parts
	of $u$ simply correspond to the positive and negative coefficients $c_j$.

	\medskip

	\noindent
	Indeed, on $V_k$ we may define
	\[
	u_{+}(f)
	= \sum_{j=1}^{k} a_j\,c_j^{+},
	\qquad
	u_{-}(f)
	= \sum_{j=1}^{k} a_j\,c_j^{-},
	\qquad
	c_j^{\pm} := \max\{\pm c_j,0\}.
	\]
	Then $u(f)=u_{+}(f)-u_{-}(f)$, and both $u_{+}$ and $u_{-}$ are
	positive linear functionals on $V_k$.
	By density of $\operatorname{span}\{x_j\}$ in the $L^{p}$ space,
	this algebraic decomposition extends uniquely (by continuity) to
	all of $L^{p}(\Omega)$, yielding the decomposition $u=w-(w-u)$
	described abstractly in Exercise~3.

	\bigskip

	\noindent
	\textbf{Interpretation.}\;
	The sequence $(x_k)$ serves as a concrete ``basis'' of nonnegative,
	almost orthogonal directions that separates the positive and negative
	components of $u$:

		\par\noindent\textbullet\quad if $u(x_k)\ge 0$, the contribution of $x_k$ lies in $u_{+}$,
		\par\noindent\textbullet\quad if $u(x_k)<0$, the contribution lies in $u_{-}$.

	The functional $w$ constructed from $\tilde u$ captures precisely
	the accumulation of the positive coefficients $u(x_k)$, while $w-u$
	captures the negative ones.
	This explicit coordinate model clarifies the abstract Jordan decomposition
	of a functional on $L^{p}$ and shows that it mirrors the decomposition
	of a signed measure into its positive and negative parts.

	\bigskip

	\noindent
	\textbf{Summary.}\;
	The disjoint-support family $(x_k)$ realizes geometrically what the
	functional decomposition $u=u_{+}-u_{-}$ expresses analytically:
	each component acts as a ``measure'' supported on a disjoint sector
	of the space, so that the positivity or negativity of $u$
	can be analyzed one region at a time.
	This viewpoint unites the measure-theoretic intuition
	with the functional-analytic structure built in Exercise~3.

	We work on the measure space $([0,1],\mathcal B,m)$ with Lebesgue measure $m$.
	For $k\ge 1$ set
	\[
	E_k := (2^{-k},2^{-(k-1)}].
	\]
	Then the $E_k$ are pairwise disjoint and $m(E_k)=2^{-k}$.

	\bigskip

	Define
	\[
	x_k := \frac{\mathbf 1_{E_k}}{\sqrt{m(E_k)}}
	= 2^{k/2}\,\mathbf 1_{E_k} \in L^2[0,1].
	\]
	\textbf{Norm.}\quad
	\[
	\|x_k\|_2^2 = \int 4^{k/2}\,\mathbf 1_{E_k}
	= 2^{k} m(E_k) = 1
	\quad \Rightarrow \quad \|x_k\|_2 = 1.
	\]

	\textbf{Orthogonality.}\quad
	Since $x_i x_j=0$ a.e.\ for $i\ne j$ (disjoint supports),
	\[
	\langle x_i,x_j\rangle=\int x_i x_j = 0.
	\]
	Thus $\{x_k\}$ is an orthonormal set.

	\bigskip

	For $i\ne j$,
	\[
	\|x_i-x_j\|_2^2
	= \|x_i\|_2^2+\|x_j\|_2^2 - 2\langle x_i,x_j\rangle
	= 1+1-0=2,
	\]
	so
	\[
	\|x_i-x_j\|_2=\sqrt{2}.
	\]

	\bigskip

	Define
	\[
	u(f):=\int_0^1 f(t)\,dt.
	\]
	\textbf{Boundedness and norm.}\quad
	By Cauchy--Schwarz,
	\[
	|u(f)| = \Bigl|\int f\Bigr|
	\le \|f\|_2\,\|1\|_2
	= \|f\|_2,
	\]
	so $\|u\|=1$.

	\textbf{Values on the blocks.}\quad
	\[
	u(x_k)
	= \int x_k
	= \int 2^{k/2}\,\mathbf 1_{E_k}
	= 2^{k/2}\,m(E_k)
	= 2^{k/2}\cdot 2^{-k}
	= 2^{-k/2} > 0.
	\]
	Hence all coefficients $c_k:=u(x_k)$ are positive.

	\bigskip

	Let
	\[
	V_k := \operatorname{span}\{x_1,\dots,x_k\}.
	\]
	Any $y\in V_k$ vanishes a.e.\ on $E_{k+1}$, hence
	\[
	\|x_{k+1}-y\|_2^2
	\ge \int_{E_{k+1}}|x_{k+1}|^2
	= \int_{E_{k+1}}2^{k+1}\mathbf 1_{E_{k+1}}
	= 2^{k+1}m(E_{k+1}) = 1.
	\]
	Taking $y=0$ shows
	\[
	\operatorname{dist}(x_{k+1},V_k)=1.
	\]

	\bigskip

	For $f\ge0$, the functional $u(g)=\int g$ is monotone increasing in $g$.
	If $0\le g\le f$, the supremum of $\int g$ occurs for $g=f$, so
	\[
	\tilde u(f)
	= \sup_{0\le g\le f} \int g
	= \int f = u(f).
	\]
	Therefore
	\[
	w(f) = \tilde u(f^+) - \tilde u(f^-)
	= \int f^+ - \int f^- = \int f = u(f),
	\]
	and $w=u$, $w-u\equiv0$ (both positive).

	\bigskip

	Let $\phi=\sum_{k=1}^\infty s_k\,\mathbf 1_{E_k}$ with $s_k\in\{-1,+1\}$.
	Then $\|\phi\|_2^2=\sum_k m(E_k)=1$ and define
	\[
	u_\phi(f):=\int_0^1 f(t)\,\phi(t)\,dt.
	\]
	By Cauchy--Schwarz, $\|u_\phi\|=\|\phi\|_2=1$.
	For each block,
	\[
	u_\phi(x_k)
	= \int x_k\phi
	= \int 2^{k/2}\,\mathbf 1_{E_k}\,s_k
	= s_k\,2^{k/2}m(E_k)
	= s_k\,2^{-k/2}.
	\]
	Now some $u_\phi(x_k)$ are positive and some negative.

	For $f\ge0$,
	\[
	\tilde u_\phi(f)
	= \sup_{0\le g\le f}\int g\,\phi
	= \int f\,\phi_{+},
	\qquad \phi_{+}=\max(\phi,0).
	\]
	Hence
	\[
	w_\phi(f)
	= \tilde u_\phi(f^+) - \tilde u_\phi(f^-)
	= \int f\,\phi_{+},
	\qquad
	(w_\phi - u_\phi)(f)
	= \int f\,\phi_{-} \ge 0,
	\]
	where $\phi_-=\max(-\phi,0)$.
	Therefore $w_\phi$ and $w_\phi-u_\phi$ are positive and
	\[
	u_\phi = w_\phi - (w_\phi - u_\phi)
	\]
	is exactly the positive-minus-negative decomposition of $u_\phi$.

	\bigskip

	On the finite-dimensional space $V_k$ we can write
	\[
	u_\phi\!\left(\sum_{j=1}^{k} a_j x_j\right)
	= \sum_{j=1}^{k} a_j\,s_j\,2^{-j/2},
	\]
	so that
	\[
	(u_\phi)_+\!\left(\sum a_j x_j\right)
	= \sum a_j\,(s_j 2^{-j/2})^{+},
	\qquad
	(u_\phi)_-\!\left(\sum a_j x_j\right)
	= \sum a_j\,(s_j 2^{-j/2})^{-}.
	\]
	This makes the abstract decomposition $u=u_+-u_-$ completely explicit
	on the orthonormal basis $\{x_k\}$.

	\bigskip

		\par\noindent\textbullet\quad $\{x_k\}$ is an orthonormal family in $L^2[0,1]$,
		with $\|x_i-x_j\|_2=\sqrt{2}$ and
		$\operatorname{dist}(x_{k+1},V_k)=1$.
		\par\noindent\textbullet\quad For the positive functional $u(f)=\int f$, we have $w=u$ and $w-u=0$.
		\par\noindent\textbullet\quad For sign-changing densities $\phi$, we get
		$u_\phi=w_\phi-(w_\phi-u_\phi)$ with both parts positive.
		\par\noindent\textbullet\quad On $V_k$, $u_\phi$ acts as a coordinate functional with
		coefficients $s_k 2^{-k/2}$ separating positive and negative parts.

	\clearpage
```
