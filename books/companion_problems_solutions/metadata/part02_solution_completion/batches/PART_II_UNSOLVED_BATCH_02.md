# Part II missing-solution batch 02

- problems: **20**
- IDs: CP-II-0136, CP-II-0137, CP-II-0138, CP-II-0145, CP-II-0146, CP-II-0153, CP-II-0166, CP-II-0168, CP-II-0180, CP-II-0185, CP-II-0191, CP-II-0203, CP-II-0218, CP-II-0223, CP-II-0229, CP-II-0257, CP-II-0265, CP-II-0268, CP-II-0269, CP-II-0271

## CP-II-0136

- chapter line: 2654

```tex
\label{prob:cp-ii-0136}
Compactness of Cocountable vs.\ Cofinite Topologies

On a set $X$, let
	\[
	\tau=\{\varnothing\}\cup\{\,U\subseteq X:\ X\setminus U\ \text{is countable}\,\}
	\quad\text{and}\quad
	\rho=\{\varnothing\}\cup\{\,U\subseteq X:\ X\setminus U\ \text{is finite}\,\}.
	\]

		\par\noindent\textbullet\quad If $X$ is finite, then every subset is open (discrete topology), hence $(X,\tau)$ is compact.
		\par\noindent\textbullet\quad If $X$ is infinite, then $(X,\tau)$ is \emph{not} compact.
		Choose a countably infinite subset $A=\{a_1,a_2,\dots\}\subseteq X$.
		For $n\ge1$ set $C_n=\{a_n,a_{n+1},\dots\}$ (countable) and $U_n=X\setminus C_n\in\tau$.
		Then $\bigcup_{n\ge1}U_n=X$ since $\bigcap_{n\ge1} C_n=\varnothing$, but for each $k$,
		\[
		\bigcup_{n=1}^k U_n=X\setminus\Big(\bigcap_{n=1}^k C_n\Big)=X\setminus\{a_k,a_{k+1},\dots\}\neq X,
		\]
		so no finite subcover exists. Hence $(X,\tau)$ is compact iff $X$ is finite (the empty space is compact as usual).

	$(X,\rho)$ is compact for \emph{every} $X$.
	Indeed, given an open cover $\{U_\alpha\}_{\alpha\in A}$ of $X$, pick a nonempty $U_{\alpha_0}$.
	Then $F=X\setminus U_{\alpha_0}$ is finite. For each $x\in F$ choose $U_{\alpha(x)}$ with $x\in U_{\alpha(x)}$.
	Thus
	\[
	X=U_{\alpha_0}\ \cup\ \bigcup_{x\in F} U_{\alpha(x)}
	\]
	is a finite subcover.

	On $X=\mathbb{R}$ the cocountable topology is not compact (use the $U_n=\mathbb{R}\setminus\{a_n,a_{n+1},\dots\}$ cover for a countably infinite subset $\{a_n\}$), while the cofinite topology is compact. If $X$ is finite, both topologies coincide with the discrete topology and are compact.
```

## CP-II-0137

- chapter line: 2687

```tex
\label{prob:cp-ii-0137}
— Positive distributions have order $0$

Suppose $u\in\mathcal D'(\mathbb R^n)$ is positive, i.e.\ $u[\phi]\ge 0$ for all $\phi\in\mathcal D(\mathbb R^n)$ with $\phi\ge 0$.
Show that $u$ has order $0$: for each compact $K\subset\mathbb R^n$ there exists $C_K>0$ such that
\[
|u[\phi]|\le C_K\,\sup_{x\in K}|\phi(x)|,\qquad \forall\,\phi\in C_c^\infty(K).
\]

Fix compact $K$. Define
\[
C_K:=\sup\{\,u[\psi]:\ \psi\in C_c^\infty(K),\ 0\le \psi\le 1\,\}.
\]
Approximating the indicator $\mathbf 1_K$ from below by smooth cutoffs shows $C_K<\infty$ by monotone convergence and positivity.
For any $\phi\in C_c^\infty(K)$ write $\phi=\phi^+-\phi^-$ with $\phi^\pm\ge 0$ and
$\|\phi^\pm\|_{L^\infty(K)}\le \|\phi\|_{L^\infty(K)}$. Then
\[
|u[\phi]|\le u[\phi^+]+u[\phi^-]
\le \|\phi\|_{L^\infty(K)}\,
\sup\{u[\psi]:\ 0\le\psi\le 1,\ \operatorname{supp}\psi\subset K\}
= C_K\,\|\phi\|_{L^\infty(K)}.
\]
Thus $u$ is of order $0$ on $K$. Equivalently, by the Riesz--Markov representation, $u$ is integration against a finite Radon measure on $K$.

\bigskip
\bigskip
```

## CP-II-0138

- chapter line: 2716

```tex
\label{prob:cp-ii-0138}
Let $A+B:=\{a+b:a\in A,\ b\in B\}$ and
	$B_r(x)=\{y\in\mathbb{R}^n:\|y-x\|<r\}$,
	$\overline{B_r(x)}=\{y:\|y-x\|\le r\}$.

		\par\noindent\textbullet\quad Prove the following identities for $r,s>0$ and $x\in\mathbb{R}^n$:

			\par\noindent\textbullet\quad $B_r(x)+B_s(0)=B_{r+s}(x)$;
			\par\noindent\textbullet\quad $\overline{B_r(x)}+B_s(0)=B_{r+s}(x)$;
			\par\noindent\textbullet\quad $\overline{B_r(x)}+\overline{B_s(0)}=\overline{B_{r+s}(x)}$.

		\par\noindent\textbullet\quad Suppose that $A,B\subset\mathbb{R}^n$.
		Show that:

			\par\noindent\textbullet\quad If one of $A$ or $B$ is open, then so is $A+B$.
			\par\noindent\textbullet\quad If $A$ and $B$ are both bounded, then so is $A+B$.
			\par\noindent\textbullet\quad If $A$ is closed and $B$ is compact, then $A+B$ is closed.
			\par\noindent\textbullet\quad If $A$ and $B$ are both compact, then so is $A+B$.

\begin{proof}
	(a)\,(i)\;
	Let $z\in B_r(x)+B_s(0)$, so $z=y+u$ with $\|y-x\|<r$ and $\|u\|<s$.
	Then
	\[
	\|z-x\|\le \|y-x\|+\|u\|<r+s,
	\]
	hence $z\in B_{r+s}(x)$.

	Conversely, let $z\in B_{r+s}(x)$, so $\|z-x\|<r+s$.
	Set
	\[
	y:=x+\frac{r}{r+s}(z-x), \qquad
	u:=z-y=\frac{s}{r+s}(z-x).
	\]
	Then
	\[
	\|y-x\|=\frac{r}{r+s}\|z-x\|<r,\qquad
	\|u\|=\frac{s}{r+s}\|z-x\|<s,
	\]
	so $y\in B_r(x)$, $u\in B_s(0)$ and $z=y+u\in B_r(x)+B_s(0)$.
	Thus $B_r(x)+B_s(0)=B_{r+s}(x)$.

	\smallskip
	(ii)\;
	If $z=y+u$ with $\|y-x\|\le r$ and $\|u\|<s$, then
	\[
	\|z-x\|\le \|y-x\|+\|u\|\le r+\|u\|<r+s,
	\]
	so $z\in B_{r+s}(x)$ and
	$\overline{B_r(x)}+B_s(0)\subset B_{r+s}(x)$.

	Conversely, if $z\in B_{r+s}(x)$, part (i) gives $z=y+u$ with
	$y\in B_r(x)\subset\overline{B_r(x)}$ and $u\in B_s(0)$, hence
	$z\in\overline{B_r(x)}+B_s(0)$. Therefore
	$\overline{B_r(x)}+B_s(0)=B_{r+s}(x)$.

	\smallskip
	(iii)\;
	If $z=y+u$ with $\|y-x\|\le r$, $\|u\|\le s$, then
	$\|z-x\|\le r+s$, so
	$\overline{B_r(x)}+\overline{B_s(0)}\subset\overline{B_{r+s}(x)}$.

	For the reverse inclusion, let $\|z-x\|<r+s$. Then
	$z\in B_{r+s}(x)$ and by (i) we have $z=y+u$ with
	$y\in B_r(x)\subset\overline{B_r(x)}$ and
	$u\in B_s(0)\subset\overline{B_s(0)}$, so
	$z\in\overline{B_r(x)}+\overline{B_s(0)}$.

	If $\|z-x\|=r+s$, set $z_t=x+t(z-x)$, $0<t<1$.
	Then $\|z_t-x\|=t(r+s)<r+s$, hence $z_t\in B_{r+s}(x)$ and thus
	$z_t\in\overline{B_r(x)}+\overline{B_s(0)}$.
	The set $\overline{B_r(x)}+\overline{B_s(0)}$ is compact (sum of two
	compact sets), hence closed, so $z=\lim_{t\to1}z_t$ also belongs to it.
	Therefore $\overline{B_{r+s}(x)}\subset
	\overline{B_r(x)}+\overline{B_s(0)}$ and
	\[
	\overline{B_r(x)}+\overline{B_s(0)}=\overline{B_{r+s}(x)}.
	\]

	\medskip
	(b)\;
	Assume $A$ is open (the case where $B$ is open is analogous).
	Let $z\in A+B$, so $z=a+b$ with $a\in A$, $b\in B$.
	Since $A$ is open, there exists $r>0$ with $B_r(a)\subset A$.
	If $\|y-z\|<r$ and we set $a':=a+(y-z)$, then
	$\|a'-a\|=\|y-z\|<r$, so $a'\in B_r(a)\subset A$, and
	$y=a'+b\in A+B$. Thus $B_r(z)\subset A+B$ and $A+B$ is open.

	\medskip
	(c)\;
	Suppose $A\subset B_M(0)$ and $B\subset B_N(0)$ for some $M,N>0$.
	If $z=a+b\in A+B$, then
	\[
	\|z\|\le\|a\|+\|b\|\le M+N,
	\]
	so $A+B\subset B_{M+N}(0)$ and $A+B$ is bounded.

	\medskip
	(d)\;
	Assume $A$ is closed and $B$ is compact. Let $(z_k)$ be a sequence in
	$A+B$ with $z_k\to z$. Write $z_k=a_k+b_k$ with
	$a_k\in A$ and $b_k\in B$.

	By compactness of $B$, there is a subsequence $(b_{k_j})$ such that
	$b_{k_j}\to b\in B$. Then
	\[
	a_{k_j}=z_{k_j}-b_{k_j}\longrightarrow z-b.
	\]
	Since $A$ is closed and $a_{k_j}\in A$, we have $z-b\in A$, hence
	$z=(z-b)+b\in A+B$. Therefore $A+B$ is closed.

	\medskip
	(e)\;
	If $A$ and $B$ are compact, then $A\times B$ is compact and the map
	\[
	f:A\times B\to\mathbb{R}^n,\qquad f(a,b)=a+b
	\]
	is continuous. Hence $A+B=f(A\times B)$ is compact as the continuous
	image of a compact set.
\end{proof}

Figure~\ref{fig:triangle-plus-ball} gives a concrete picture: if $A$ is a closed triangle and $B$ a small closed ball, then $A+B$ is a uniformly thickened version of $A$.

\begin{figure}[ht]
	\centering
	\begin{tikzpicture}[scale=1.7]

		% axes (optional)
		\draw[->,gray!60] (-0.6,0) -- (2.6,0) node[below] {$x_1$};
		\draw[->,gray!60] (0,-0.6) -- (0,2.0) node[left] {$x_2$};

		% --- compact set A: a triangle ---
		\coordinate (A1) at (0.2,0.0);
		\coordinate (A2) at (2.0,0.0);
		\coordinate (A3) at (1.1,1.6);

		\fill[blue!10] (A1)--(A2)--(A3)--cycle;
		\draw[blue!70!black,thick] (A1)--(A2)--(A3)--cycle;
		\node[blue!70!black] at (1.1,0.2) {$A$};

		% --- small ball B centred at the origin ---
		\def\r{0.35}
		\fill[red!10] (0,0) circle (\r);
		\draw[red!70!black,thick] (0,0) circle (\r);
		\node[red!70!black] at (-0.15,-0.45) {$B$};

		% --- Minkowski sum A+B (schematic outline) ---
		% (offset triangle by radius r; this is only illustrative)
		\draw[green!50!black,thick,dashed]
		($(A1)+(-\r,0)$) arc (180:360:\r) -- ($(A2)+(0,\r)$)
		arc (-90:30:\r) -- ($(A3)+(\r*0.5,\r*0.866)$)
		arc (30:150:\r) -- ($(A1)+(-\r*0.5,\r*0.866)$)
		arc (150:210:\r) -- cycle;

		\node[green!50!black] at (1.3,1.3) {$A+B$};

	\end{tikzpicture}
	\caption{Minkowski sum of a compact set $A$ (triangle) with a small ball $B$.
		Geometrically, $A+B$ is obtained by ``thickening'' $A$ by the radius of $B$.
		Since both $A$ and $B$ are compact, their sum $A+B$ is compact as well.}
	\label{fig:triangle-plus-ball}
\end{figure}

Let $A = B_1(0) = \{x\in\mathbb{R}^2 : \|x\|<1\}$ and let $b\in\mathbb{R}^2$.
Define
\[
B = \{0,b\}.
\]
Then
\[
A+B = \{a+p : a\in A,\ p\in B\}
= A + \{0,b\}
= A \cup (A+b).
\]
In particular, for the two specific choices
\[
b_1=(2,0), \qquad b_2=(0,2),
\]
we obtain
\[
A+\{0,b_1\} = B_1(0)\cup B_1\bigl((2,0)\bigr), \qquad
A+\{0,b_2\} = B_1(0)\cup B_1\bigl((0,2)\bigr).
\]
In each case $A$ is open, $B$ is finite, and $A+B$ is the union of two
open discs, hence open but not connected.

Let
\[
A = B_1(0) = \{x\in\mathbb{R}^2 : \|x\|<1\}
\]
and choose two vectors
\[
b_1 = (2,0), \qquad b_2 = (0,2).
\]
Define
\[
B = \{b_1, b_2\}.
\]
Then the Minkowski sum is
\[
\begin{aligned}
	A+B
	&= \{a+p : a\in A,\ p\in B\}
	= A + \{b_1,b_2\} \\
	&= (A+b_1)\ \cup\ (A+b_2) \\
	&= B_1\bigl((2,0)\bigr)\ \cup\ B_1\bigl((0,2)\bigr).
\end{aligned}
\]
Thus $A+B$ is the union of two open discs, hence open but not connected.
Note that, in contrast with the case $B=\{0,b_1,b_2\}$, there is now no
disc centred at the origin, because $0\notin B$.
```

## CP-II-0145

- chapter line: 2930

```tex
\label{prob:cp-ii-0145}
\par\noindent\textbullet\quad Lebesgue measure $m$ on $\mathbb{R}^n$ is a complete Radon Borel measure.
```

## CP-II-0146

- chapter line: 2935

```tex
\label{prob:cp-ii-0146}
s.

\par\noindent\textbullet\quad Conversely, from $a\|x\|_1\le\|x\|_2$, we get
	$B_2(x_0,r)\subseteq B_1(x_0,r/a)$.

So open balls in one norm contain open balls of the other.
Hence both topologies have the same open sets.

\par\medskip\noindent\textbf{(2)$\Rightarrow$(3).}\quad
If the two topologies coincide, then convergence (defined by open neighborhoods)
is identical. Thus a sequence converges in one norm if and only if it converges in the other.

\par\medskip\noindent\textbf{(3)$\Rightarrow$(1).}\quad
Assume the same convergent sequences.
We show existence of $a,b>0$.

Define $f(x)=\|x\|_2$.
If no $b$ exists with $\|x\|_2\le b\|x\|_1$,
we could find a sequence $x_n$ with $\|x_n\|_1=1$ and $\|x_n\|_2>n$.
Then $x_n/n\to 0$ in $\|\cdot\|_1$ but not in $\|\cdot\|_2$, contradicting (3).
Thus $\exists b>0$ s.t.\ $\|x\|_2\le b\|x\|_1$.

Similarly, interchanging norms gives $a>0$ s.t.\ $a\|x\|_1\le\|x\|_2$.
Hence the norms are equivalent.
```

## CP-II-0153

- chapter line: 2963

```tex
\label{prob:cp-ii-0153}
— Positive separation

Let \(K\subset \mathbb{R}^2\) be compact and let \(F\subset \mathbb{R}^2\) be closed with \(K\cap F=\varnothing\).

Show that there exists \(\delta>0\) such that \(d(x,y)\ge \delta\) for every \(x\in K\) and every \(y\in F\).

Give two proofs: one from compactness of \(K\), and one using sequential compactness.

\bigskip

For \(A\subset\mathbb{R}^2\) and \(x\in\mathbb{R}^2\),
\[
\operatorname{dist}(x,A)=\inf\{\|x-a\|:a\in A\}.
\]
If \(A\) is closed and \(x\notin A\), then \(\operatorname{dist}(x,A)>0\).

Compactness: every open cover has a finite subcover.

Sequential compactness: every sequence in \(K\) has a convergent subsequence with limit in \(K\).

Closed sets are sequentially closed.

\bigskip

For each \(x\in K\), since \(x\notin F\) and \(F\) is closed, we have \(\operatorname{dist}(x,F)>0\).
Let
\[
r_x=\tfrac12\,\operatorname{dist}(x,F).
\]
Then \(B(x,r_x)\cap F=\varnothing\).
The family \(\{B(x,r_x):x\in K\}\) covers \(K\).

By compactness of \(K\), choose \(x_1,\dots,x_m\in K\) with
\[
K\subset \bigcup_{i=1}^{m} B(x_i,r_{x_i}).
\]
Set
\[
\delta=\min_{1\le i\le m} r_{x_i}>0.
\]
If \(x\in K\) and \(y\in F\), choose \(i\) so that \(x\in B(x_i,r_{x_i})\).
Because \(B(x_i,r_{x_i})\cap F=\varnothing\), we have \(d(x,y)\ge r_{x_i}\ge\delta\).
Thus \(d(x,y)\ge\delta\) for all \(x\in K,\; y\in F\).

\bigskip

Assume no such \(\delta>0\) exists.
Then for each \(n\in\mathbb{N}\) there exist \(x_n\in K\) and \(y_n\in F\) with
\[
d(x_n,y_n)<\tfrac{1}{n}.
\]
By sequential compactness, there is a subsequence \(x_{n_k}\to x\in K\).
Since \(d(x_{n_k},y_{n_k})\to 0\), it follows that \(y_{n_k}\to x\).
Because \(F\) is closed and all \(y_{n_k}\in F\), we have \(x\in F\).
Hence \(x\in K\cap F\), a contradiction.

Therefore some \(\delta>0\) exists.

\bigskip

If \(K=\{(x,y):x^2+y^2=1\}\) and \(F=\{(3,t):t\in\mathbb{R}\}\), then the minimal distance is \(2\).

If compactness of \(K\) is dropped, the claim may fail; there are disjoint closed sets with zero infimum distance.

A topological space \(X\) is sequentially compact if every sequence in \(X\) has a convergent subsequence with limit in \(X\).

\bigskip

\par\noindent\textbullet\quad Closed and bounded subsets of \(\mathbb{R}^n\) (e.g.\ \([0,1]^n\), spheres, closed balls). By Bolzano--Weierstrass.
\par\noindent\textbullet\quad Any compact metric space (in metric spaces, compact \(\Leftrightarrow\) sequentially compact).
\par\noindent\textbullet\quad Finite spaces (every sequence is eventually constant).

\medskip

\par\noindent\textbullet\quad \((0,1)\subset\mathbb{R}\): the sequence \(x_n=1/n\) has no convergent subsequence in \((0,1)\).
\par\noindent\textbullet\quad \([0,\infty)\): the sequence \(x_n=n\) has no convergent subsequence.
\par\noindent\textbullet\quad \([0,1]\cap\mathbb{Q}\): rationals \(q_n\to\sqrt{2}\) (in \(\mathbb{R}\)) yield no convergent subsequence in the space.

\medskip

\par\noindent\textbullet\quad An uncountable set with the co-countable topology.

Any sequence has a convergent subsequence (indeed, often converges to every point), so the space is sequentially compact.
The open cover \(\{\,X\setminus\{x\}\,:\,x\in X\,\}\) has no finite subcover, so the space is not compact.

\smallskip

\par\noindent\textbullet\quad The Cantor cube \(2^{\mathbb{R}}\) (product of \(\{0,1\}\) over an uncountable index set).

Compact by Tychonoff, but not sequentially compact; there exist sequences with no convergent subsequence (product convergence is coordinatewise and can be made to oscillate on infinitely many coordinates).

\par\noindent\textbullet\quad The Stone--Ă„Ĺšech compactification \(\beta\mathbb{N}\).

Compact Hausdorff, yet not sequentially compact.

\medskip

\noindent\textbf{Summary.}
In metric spaces, compactness and sequential compactness coincide. In general topological spaces, neither implies the other.

\noindent\textbf{Compact.}
Every open cover has a finite subcover.

\smallskip

\noindent\textbf{Paracompact.}
Every open cover has a locally finite open refinement
(i.e., each point meets only finitely many sets of the refinement).

\smallskip

\noindent\textbf{Precompact (totally bounded / relatively compact).}
In a metric (or uniform) space: for every \(\varepsilon>0\) there exist finitely many
\(\varepsilon\)-balls covering the space.
Equivalently, the closure in the completion is compact.

\smallskip

\noindent\textbf{Sequentially compact.}
Every sequence has a convergent subsequence with limit in the space.

\smallskip

\noindent\textbf{Lindel\"of.}
Every open cover admits a countable subcover.

\smallskip

\noindent\textbf{General spaces.}
\[
\text{Compact} \;\Rightarrow\; \text{Lindel\"of} \quad\text{and}\quad
\text{Compact} \;\Rightarrow\; \text{Paracompact}.
\]
The converses need not hold.

\smallskip

\noindent\textbf{Metric spaces.}
\[
\text{Compact} \;\Longleftrightarrow\; \text{Sequentially compact}
\;\Longleftrightarrow\; \text{Complete}+\text{Totally bounded (Precompact)}.
\]
Also, every metric space is paracompact, and
\[
\text{Separable} \;\Longleftrightarrow\; \text{Second countable}
\;\Longleftrightarrow\; \text{Lindel\"of}.
\]

\smallskip

\noindent\emph{Precompact but not compact:} \((0,1)\subset\mathbb{R}\).

\smallskip

\noindent\emph{Lindel\"of but not compact:} \(\mathbb{R}\) with the usual topology.

\smallskip

\noindent\emph{Compact hence paracompact:} any compact Hausdorff space.

\smallskip

\noindent\emph{Sequentially compact} \(=\) \emph{compact (metric):} closed intervals \([a,b]\subset\mathbb{R}\).
```

## CP-II-0166

- chapter line: 3160

```tex
\label{prob:cp-ii-0166}
Identity property of the Dirac distribution

\noindent
(a)\; Show that if $\phi \in \mathcal{D}(\mathbb{R}^n)$ then
\[
\delta_0 * \phi = \phi .
\]

\medskip
\noindent
(b)\; Show that if $u \in \mathcal{D}'(\mathbb{R}^n)$ has compact support, then
\[
\delta_0 * u = u .
\]
```

## CP-II-0168

- chapter line: 3178

```tex
\label{prob:cp-ii-0168}
\textbf{Approximating $1/z$ on $U=B_2(1)\setminus B_1(0)$.}

		\par\noindent (i)\quad (Compacts in $U$.) Runge with poles at $\{0,\infty\}$ allows Laurent polynomials.
		For $f(z)=1/z$ the constant sequence
		\[
		r_n(z)\equiv \frac{1}{z}
		\]
		already works and converges uniformly to $1/z$ on every compact $K\subset U$.

		If $K\subset B_1(1)$ (so $|z-1|<1$ on $K$), the \emph{polynomials}
		\[
		p_N(z)=\sum_{k=0}^N (-1)^k(z-1)^k
		\]
		satisfy $p_N\to 1/z$ uniformly on $K$ by the geometric series
		$\frac{1}{1+w}=\sum_{k\ge0}(-w)^k$ with $w=z-1$.

		\par\noindent (ii)\quad (No polynomials on all of $U$.) Suppose $p_n$ were polynomials with
		$p_n\to 1/z$ uniformly on $U$. For the loop $\gamma(t)=e^{it}$,
		\[
		\int_\gamma p_n(z)\,dz \longrightarrow \int_\gamma \frac{1}{z}\,dz=2\pi i,
		\]
		but each $\int_\gamma p_n(z)\,dz=0$, contradiction. Hence no polynomial sequence
		converges to $1/z$ uniformly on $U$ (and the same holds even if $1/z$ extends past $\overline U$).
```

## CP-II-0180

- chapter line: 3205

```tex
\label{prob:cp-ii-0180}
— Which duals contain $u_f$ for $f(x)=e^x\cos(e^x)$?

Let $f:\mathbb R\to\mathbb R$, $f(x)=e^x\cos(e^x)$, and let $u_f[\phi]=\int_{\mathbb R} f(x)\phi(x)\,dx$.
Decide whether $u_f$ belongs to $\mathcal D'(\mathbb R)$, $\mathcal S'(\mathbb R)$, and $\mathcal E'(\mathbb R)$.

\smallskip

$\mathcal D'(\mathbb R)$: For $\phi\in\mathcal D(\mathbb R)$ the support is compact, hence $\int f\phi$ is finite and depends continuously on $\phi$.
Thus $u_f\in\mathcal D'(\mathbb R)$.

\smallskip

$\mathcal E'(\mathbb R)$: Elements of $\mathcal E'$ are compactly supported distributions. Since $f$ is not compactly supported,
the regular distribution $u_f$ is not in $\mathcal E'(\mathbb R)$.

\smallskip

$\mathcal S'(\mathbb R)$: A regular distribution is tempered iff its defining function has at most polynomial growth.
Here $|f(x)|\le e^x$, so the growth is exponential. To see non–temperateness directly, set
\[
\phi_k(x)=\frac{e^{-(x-k)^2}}{(1+k)^M},\qquad k\in\mathbb N,
\]
with $M$ chosen large enough that all Schwartz seminorms of $\phi_k$ remain bounded in $k$.
Then
\[
\int_{\mathbb R} e^x\cos(e^x)\,\phi_k(x)\,dx
= \frac{e^{k}}{(1+k)^M}\int_{\mathbb R} e^{-(y^2-y)}\cos(e^{k+y})\,dy,
\]
whose absolute value is $\gtrsim e^{k}/(1+k)^M\to\infty$.
Hence the functional is not continuous on $\mathcal S$, so $u_f\notin\mathcal S'(\mathbb R)$.

$u_f\in\mathcal D'(\mathbb R)$, but $u_f\notin\mathcal S'(\mathbb R)$ and $u_f\notin\mathcal E'(\mathbb R)$.

\bigskip
\bigskip
```

## CP-II-0185

- chapter line: 3244

```tex
\label{prob:cp-ii-0185}
Every bounded sequence has a convergent subsequence

Let $V$ be a normed space in which every bounded sequence has a convergent subsequence.

	\par\noindent\textbullet\quad Show that this property is equivalent to the sequential compactness of the unit sphere
	$S=\{x\in V:\|x\|=1\}$.
	\par\noindent\textbullet\quad Show that $V$ must be complete.
	\par\noindent \textnormal{(c)$^*$}\quad Show further that $V$ must be finite--dimensional.

\emph{Hint for (c).} For every finite--dimensional subspace $V_0$ of $V$, there exists $x\in V$
with $\|x+y\|>\|x\|/2$ for each $y\in V_0$.

Sequential compactness means every sequence has a convergent subsequence.
Cauchy sequences are bounded; if a Cauchy sequence has one convergent subsequence, then the whole sequence converges.
A Riesz--lemma variant: if $V_0$ is finite--dimensional (hence closed) and $0<\alpha<1$, there exists $x$ with $\|x\|=1$ and
$\operatorname{dist}(x,V_0)>\alpha$; equivalently, $\|x+y\|>\alpha$ for all $y\in V_0$.

	\par\noindent\textbullet\quad
	Assume every bounded sequence in $V$ has a convergent subsequence. Then the unit sphere $S$ is bounded,
	so any sequence in $S$ has a convergent subsequence in $V$. If $x_{n_k}\to x$, then
	$\|x\|=\lim_k\|x_{n_k}\|=1$, hence $x\in S$. Thus $S$ is sequentially compact.

	Conversely, suppose $S$ is sequentially compact. Let $(x_n)$ be bounded in $V$ and set $r_n=\|x_n\|$.
	Passing to a subsequence we may assume $(r_n)$ converges to $r\ge 0$.
	For each $n$ with $x_n\neq 0$ define $u_n=x_n/\|x_n\|\in S$; for $x_n=0$ define $u_n$ arbitrarily in $S$.
	By sequential compactness of $S$, $(u_n)$ admits a convergent subsequence $u_{n_k}\to u\in S$.
	Then $x_{n_k}=r_{n_k}u_{n_k}\to r u$ in $V$. Hence every bounded sequence has a convergent subsequence.

	\par\noindent\textbullet\quad
	Let $(y_n)$ be Cauchy in $V$. Then $(y_n)$ is bounded, so it has a convergent subsequence $y_{n_k}\to y$.
	Fix $\varepsilon>0$. Choose $N$ such that $\|y_n-y_m\|<\varepsilon/2$ for all $m,n\ge N$,
	and choose $k$ with $n_k\ge N$ and $\|y_{n_k}-y\|<\varepsilon/2$.
	For $n\ge N$ we have
	\[
	\|y_n-y\|\le \|y_n-y_{n_k}\|+\|y_{n_k}-y\|<\varepsilon.
	\]
	Thus $y_n\to y$, so $V$ is complete.

	\par\noindent \textnormal{(c)$^*$}\quad
	Suppose $V$ were infinite--dimensional. Construct inductively a sequence $(x_n)\subset V$ with
	$\|x_n\|=1$ and
	\[
	\operatorname{dist}(x_{n+1},V_n)>\tfrac12,
	\qquad
	V_n=\operatorname{span}\{x_1,\dots,x_n\}.
	\]
	This is possible by the Riesz--lemma variant (applied to the finite--dimensional subspace $V_n$ with $\alpha=\tfrac12$).
	Then for $j>i$ we have $x_i\in V_{j-1}$, hence
	\[
	\|x_j-x_i\|\ge \operatorname{dist}(x_j,V_{j-1})>\tfrac12 .
	\]
	Therefore $(x_n)$ is bounded (all have norm $1$) but has no Cauchy subsequence, because any two distinct
	terms of any tail are at distance $>1/2$.
	This contradicts the hypothesis that every bounded sequence has a convergent subsequence.
	Hence $V$ must be finite--dimensional.
```

## CP-II-0191

- chapter line: 3303

```tex
\label{prob:cp-ii-0191}
Let $f:\mathbb{R}^m\to\mathbb{R}^n$ be a function such that:

		\par\noindent\textbullet\quad the image of every path-connected subset of $\mathbb{R}^m$ is path-connected;
		\par\noindent\textbullet\quad the image of every compact subset of $\mathbb{R}^m$ is compact.

	Show that $f$ is continuous.


	\textbf{Theory.}
	A continuous map between Hausdorff spaces preserves compactness and connectedness.
	Conversely, if a map preserves both compactness and (path-)connectedness in $\mathbb{R}^m$,
	then discontinuities would produce separated image pieces—contradicting path-connectedness.
	Hence these two preservation properties together imply continuity.
```

## CP-II-0203

- chapter line: 3321

```tex
\label{prob:cp-ii-0203}
\par\noindent\textbullet\quad For $\mu=m$ and $\nu=f\,m+\sum_{k\ge1} a_k\delta_{x_k}$ with $f\in L^1(m)$, $a_k\ge0$,
		the decomposition is $\nu_a=f\,m$ and $\nu_s=\sum_{k\ge1} a_k\delta_{x_k}$.

	A measure $\mu$ on $(E,\mathcal E)$ is \emph{finite} if $\mu(E)<\infty$.
	Finite measures are automatically $\sigma$-finite, and the Radon--Nikodym and
	Lebesgue decomposition theorems hold in this setting.

	\bigskip

	Let $X$ be a locally compact Hausdorff space (often second countable).
	A (positive) Borel measure $\mu$ on $X$ is a \emph{Radon measure} if it is
	\emph{inner regular} ($\mu(A)=\sup\{\mu(K):K\subset A,~K\text{ compact}\}$),
	\emph{outer regular} ($\mu(A)=\inf\{\mu(U):A\subset U,~U\text{ open}\}$),
	and \emph{locally finite}. Typical examples include Lebesgue measure on
	$\mathbb R^n$, counting measure on a discrete LCH space, and surface measure on smooth manifolds.

	\bigskip

	If $G$ is a locally compact topological group, a \emph{Haar measure} is a nonzero
	Radon measure $\eta$ that is left invariant: $\eta(gA)=\eta(A)$ for all Borel $A$ and $g\in G$.
	Haar measure is unique up to a positive scalar multiple.
	Examples: on $\mathbb R^n$, Haar measure equals Lebesgue measure; on a compact group
	(e.g.\ $\mathbb T^n$), Haar measure can be normalized to total mass $1$; on discrete groups, Haar is counting measure.

	\bigskip

	For measures $\nu,\mu$ on $(E,\mathcal E)$:
```

## CP-II-0218

- chapter line: 3400

```tex
\label{prob:cp-ii-0218}
Hausdorffness and Second Countability are Topological Invariants

Show that the Hausdorff property and second countability are preserved under homeomorphisms.

A homeomorphism $f:X\to Y$ is a bijection such that both $f$ and $f^{-1}$ are continuous. Such a map carries open sets to open sets and bases to bases via images.

Assume $f:X\to Y$ is a homeomorphism and $X$ is Hausdorff. For $y_1\neq y_2$ in $Y$, set $x_i=f^{-1}(y_i)$. Since $X$ is Hausdorff there exist disjoint open sets $U_i\ni x_i$. Then $f(U_i)$ are disjoint open neighbourhoods of $y_i$, so $Y$ is Hausdorff. The converse follows by applying the same argument to $f^{-1}$.

Let $\mathcal{B}=\{B_n:n\in\mathbb{N}\}$ be a countable base for $X$. Because $f$ is open and bijective, $\{f(B_n):n\in\mathbb{N}\}$ is a countable base for $Y$. Conversely, apply the same reasoning to $f^{-1}$.
```

## CP-II-0223

- chapter line: 3413

```tex
\label{prob:cp-ii-0223}
\par\noindent\textbullet\quad If $U_1,U_2$ are open, then $U_1\cup U_2$ and $U_1\cap U_2$ are open.
\par\noindent\textbullet\quad If $E_1,E_2$ are closed, then $E_1\cup E_2$ and $E_1\cap E_2$ are closed.
\par\noindent\textbullet\quad For any collection $\mathcal U$ of open sets: $\bigcup\mathcal U$ is open; $\bigcap\mathcal U$ need not be open (e.g.\ $\cap_{n\ge1}(-1/n,1/n)=\{0\}$);
for closed sets: arbitrary intersections are closed, finite unions are closed, infinite unions need not be closed.
```

## CP-II-0229

- chapter line: 3421

```tex
\label{prob:cp-ii-0229}
\par\noindent\textbullet\quad Suppose that $(u_i)_{i=1}^\infty$ is a sequence with
	$u_i\in H_0^1(\Omega)$ and $u_i\rightharpoonup u$ weakly in $H_0^1(\Omega)$.
	Show that
	\[
	E[u]\le \liminf_{i\to\infty}E[u_i].
	\]

	\par\noindent\textbullet\quad Consider the set
	\[
	\mathcal{E}_1=\{E[u]:u\in H_0^1(\Omega),\ \|u\|_{L^2}=1\}.
	\]
	Let $\lambda_1:=\inf\mathcal{E}_1$. Show that there exists
	$w_1\in H_0^1(\Omega)$ with $\|w_1\|_{L^2}=1$ and $E[w_1]=\lambda_1$, and
	deduce that $\lambda_1>0$.

	\par\noindent\textbullet\quad Deduce that
	\[
	\lambda_1\|u\|_{L^2}^2\le \int_\Omega |Du|^2\,dx
	\]
	holds for all $u\in H_0^1(\Omega)$, with equality for $u=w_1$.
	This is Poincar\'e's inequality.

	\par\noindent\textbullet\quad By considering $u=w_1+t\varphi$ for $t\in\mathbb{R}$ and
	$\varphi\in\mathcal{D}(\Omega)=C_c^\infty(\Omega)$, or otherwise,
	show that $w_1$ satisfies
	\[
	-\Delta w_1=\lambda_1 w_1
	\]
	in the sense of distributions, i.e.\ in $\mathcal{D}'(\Omega)$.

	\par\noindent \textnormal{(e)}\quad Suppose $\chi\in C_c^\infty(\Omega)$ and put $v=\chi w_1$.
	Show that $v$ satisfies
	\[
	-\Delta v + v = f
	\]
	in $\mathcal{S}'(\mathbb{R}^n)$, where $f\in L^2(\mathbb{R}^n)$.
	Deduce that $v\in H^2(\mathbb{R}^n)$. By iterating this argument, deduce that
	\[
	w_1\in H_0^1(\Omega)\cap C^\infty(\Omega).
	\]

	\par\noindent \textnormal{(f)}\quad Consider
	\[
	\mathcal{E}_2=\{E[u]:u\in H_0^1(\Omega),\ \|u\|_{L^2}=1,\ (u,w_1)_{L^2}=0\}.
	\]
	Show that there exist $\lambda_2\ge\lambda_1$ and
	$w_2\in H_0^1(\Omega)\cap C^\infty(\Omega)$ with
	$w_2\neq w_1$, $\|w_2\|_{L^2}=1$ and
	\[
	-\Delta w_2=\lambda_2 w_2.
	\]

The space $H_0^1(\Omega)$ is the closure of $C_c^\infty(\Omega)$ in the
Sobolev norm
\[
\|u\|_{H^1}^2=\|u\|_{L^2}^2+\|Du\|_{L^2}^2.
\]
The functional $E[u]=\|Du\|_{L^2}^2$ is convex and weakly lower semicontinuous
on $H_0^1(\Omega)$. Since $\Omega$ is bounded, the embedding
$H_0^1(\Omega)\hookrightarrow L^2(\Omega)$ is compact (Rellich--Kondrachov).

The Dirichlet Laplacian $-\Delta$ with domain $H_0^1(\Omega)$ has discrete
spectrum
\[
0<\lambda_1\le\lambda_2\le\cdots\to\infty,
\]
and the first eigenvalue admits the variational characterisation
\[
\lambda_1 = \inf\left\{
\frac{\int_\Omega |Du|^2}{\int_\Omega |u|^2}
: u\in H_0^1(\Omega),\,u\neq 0\right\}.
\]
Minimisers are eigenfunctions solving $-\Delta u=\lambda_1 u$.

For the constant–coefficient elliptic operator $-\Delta+I$ on $\mathbb{R}^n$
the equation $(-\Delta+I)v=f$ with $f\in L^2(\mathbb{R}^n)$ implies
$v\in H^2(\mathbb{R}^n)$. By iterating and using Sobolev embedding, one
derives interior smoothness for solutions of $-\Delta u = \lambda u$.
```

## CP-II-0257

- chapter line: 4148

```tex
\label{prob:cp-ii-0257}
Convolution of regular and general distributions

\noindent
(a)\; Show that for $f,g\in C_0^\infty(\mathbb{R}^n)$,
\[
T_{f*g} = T_f * T_g .
\]

\medskip
\noindent
(b)\; Show that convolution is linear in both of its arguments, i.e.\ if
$u_i\in\mathcal{D}'(\mathbb{R}^n)$ and $u_3,u_4$ have compact support, then
for any $a\in\mathbb{C}$,
\[
(u_1 + a u_2)\,*\,u_3 = u_1*u_3 + a\,u_2*u_3,
\]
and
\[
u_1 * (u_3 + a u_4) = u_1*u_3 + a\,u_1*u_4.
\]
```

## CP-II-0265

- chapter line: 4205

```tex
\label{prob:cp-ii-0265}
— Strict contractions on complete vs compact spaces; non-expansive maps

\noindent\textbf{Task.}
 \setlength{\itemsep}{4pt}
	\par\noindent\textbullet\quad Give a non-empty complete metric space $(X,d)$ and a map $f:X\to X$ with
	$d(f(x),f(y))<d(x,y)$ for all $x\neq y$, but \emph{no fixed point}.
	\par\noindent\textbullet\quad Now assume $X\subset\mathbb{R}^n$ is non-empty and \emph{compact} (Euclidean metric).
	Show that such an $f$ \emph{must} have a fixed point (and decide uniqueness).
	\par\noindent\textbullet\quad If $g:X\to X$ only satisfies $d(g(x),g(y))\le d(x,y)$ for all $x,y$, must $g$ have a fixed point?

\bigskip
\hrule
\bigskip

\noindent\textbf{Theory youĂ˘â‚¬â„˘ll use.}
 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad A metric space is \emph{complete} if every Cauchy sequence converges.
	\par\noindent\textbullet\quad On a compact metric space, any continuous map $h:X\to\mathbb{R}$ attains its minimum
	(apply this to $h(x)=d(f(x),x)$).
	\par\noindent\textbullet\quad \emph{EdelsteinĂ˘â‚¬â„˘s fixed point theorem.} On a compact metric space, a map
	$f$ with $d(f(x),f(y))<d(x,y)$ for all $x\neq y$ has a \emph{unique} fixed point.
	\par\noindent\textbullet\quad If $a_n=d(x_{n+1},x_n)$ and $a_{n+1}<a_n$, then $(a_n)$ is strictly decreasing
	and converges to some $L\ge0$.

\bigskip
\hrule
\bigskip

\noindent\textbf{Part 1 — Strictly contractive, complete, no fixed point (example).}

\medskip
\noindent Let $X=(0,\infty)$ and define
\[
d(x,y):=\big|\ln x-\ln y\big|\qquad (x,y>0).
\]
Then $(X,d)$ is complete because $(0,\infty)$ with this metric is isometric to
$(\mathbb{R},|\cdot|)$ via $x\mapsto \ln x$.

\medskip
\noindent Define $f(x)=x+1$. For $x\neq y$, by the mean value theorem there exist
$\xi$ between $x+1$ and $y+1$ and $\eta$ between $x$ and $y$ with
\[
\big|\ln(x+1)-\ln(y+1)\big|=\frac{|x-y|}{\xi},
\qquad
\big|\ln x-\ln y\big|=\frac{|x-y|}{\eta}.
\]
Since $\xi>\eta>0$, we have
\[
d\big(f(x),f(y)\big)=\frac{|x-y|}{\xi}\;<\;\frac{|x-y|}{\eta}=d(x,y)
\quad\text{for all }x\ne y.
\]
But $f(x)=x+1$ has no fixed point. Hence we have a complete space with a strict
contraction (in the pointwise sense) without a fixed point.

\bigskip
\hrule
\bigskip

\noindent\textbf{Part 2 — Compact $X\subset\mathbb{R}^n$: existence and uniqueness.}

\medskip
\noindent Let $X\subset\mathbb{R}^n$ be non-empty and compact (Euclidean metric).
Suppose $f:X\to X$ satisfies $d(f(x),f(y))<d(x,y)$ for all $x\ne y$.

\medskip
\noindent\emph{Existence.}
Pick any $x_0\in X$ and iterate $x_{k+1}=f(x_k)$. Set $a_k=d(x_{k+1},x_k)$.
Then
\[
a_{k+1}=d\big(f(x_{k+1}),f(x_k)\big)\;<\;d(x_{k+1},x_k)=a_k,
\]
so $(a_k)$ decreases to some $L\ge0$. By compactness, there is a subsequence
$x_{n_j}\to p\in X$. Then $x_{n_j+1}=f(x_{n_j})\to f(p)$, and by continuity of $d$,
\[
L=\lim_{j\to\infty} d\big(x_{n_j+1},x_{n_j}\big)
= d\big(f(p),p\big).
\]
If $L>0$, applying the strict inequality to $(p,f(p))$ gives
\[
d\big(f(f(p)),f(p)\big)\;<\;d\big(p,f(p)\big)=L,
\]
but the left-hand side equals $\lim_j d(x_{n_j+2},x_{n_j+1})=L$, a contradiction.
Hence $L=0$ and $f(p)=p$.

\medskip
\noindent\emph{Uniqueness.}
If $p\ne q$ are fixed points, then
\[
d\big(f(p),f(q)\big)=d(p,q)\;<\;d(p,q),
\]
impossible. Therefore the fixed point is \emph{unique}.

\bigskip
\hrule
\bigskip

\noindent\textbf{Part 3 — Non-expansive maps ($\le$) need not have fixed points.}

\medskip
\noindent Let $X=S^1\subset\mathbb{R}^2$ be the unit circle with the Euclidean metric,
and let $g$ be rotation by a nonzero angle. Then
\[
d\big(g(x),g(y)\big)=d(x,y)\le d(x,y)\quad\text{for all }x,y\in S^1,
\]
but $g$ has no fixed point. Thus the condition $d(g(x),g(y))\le d(x,y)$
does \emph{not} ensure a fixed point, even on compact sets.

\bigskip
\hrule
\bigskip
```

## CP-II-0268

- chapter line: 4319

```tex
\label{prob:cp-ii-0268}
— Statements and Theory

	\par\noindent\textbullet\quad Is the set $(1,2]$ an open subset of the metric space $\mathbb{R}$ with the metric $d(x,y)=|x-y|$? Is it closed?
	What if we replace the metric space $\mathbb{R}$ with the space $[0,2]$, the space $(1,3)$ or the space $(1,2]$, in each case with the metric $d$?
	\par\noindent\textbullet\quad Let $X$ be a set equipped with the discrete metric, and $Y$ any metric space. Describe all open subsets of $X$, closed subsets of $X$, compact subsets of $X$, Cauchy sequences in $X$, continuous functions $f:X\to Y$ and continuous functions $f:Y\to X$.

	\par\noindent\textbullet\quad \textbf{Subspace topology / metric.}
	If $M\subset Z$ and $Z$ is metric with $d_Z$, the subspace metric on $M$ is
	$d_M(x,y)=d_Z(x,y)$. A set $U\subset M$ is open in $M$ iff $U=M\cap O$ for some open $O\subset Z$.
	Closedness is analogous.

	\par\noindent\textbullet\quad \textbf{Open/closed in the line.}
	With $d(x,y)=|x-y|$ on $\mathbb R$, an interval of the form $(\alpha,\beta)$ is open, $[\alpha,\beta]$ is closed; a half-open interval like $(1,2]$ is neither open (no ball around $1$ stays inside) nor closed (its complement is not open).

	\par\noindent\textbullet\quad \textbf{Discrete metric.}
	The discrete metric is $d(x,y)=\mathbf 1_{x\ne y}$. Then every singleton $\{x\}$ is open; hence \emph{every subset of $X$ is open and also closed}. Compact subsets are exactly the finite subsets (an infinite discrete space is not compact). A sequence in $X$ is Cauchy iff it is eventually constant (for $\varepsilon=\tfrac12$). Every function $f:X\to Y$ is continuous (domain is discrete). For maps into a discrete space, $f:Y\to X$ is continuous iff for each $x\in X$, the fibre $f^{-1}(\{x\})$ is open in $Y$ (equivalently, $f$ is \emph{locally constant}; in particular, if $Y$ is connected then $f$ is constant).

With the usual metric $d(x,y)=|x-y|$:

\par\noindent\textbullet\quad In $\mathbb R$, $(1,2]$ is neither open nor closed:
it is not open because the point $2\in(1,2]$ has no $\varepsilon$-ball contained in $(1,2]$;
it is not closed because $1$ is a limit point (e.g. $1+1/n\to1$) not belonging to the set.

	\par\noindent\textbullet\quad As a subspace of $[0,2]$, $(1,2]$ is both open ($[0,2]\cap (1,\infty)$) and closed (complement $[0,1]$ is open in $[0,2]$).
\par\noindent\textbullet\quad As a subspace of $(1,3)$, the set $(1,2]$ is \emph{closed} because it can be written as the
intersection of the subspace with a closed subset of $\mathbb{R}$:
\[
(1,2]=(1,3)\cap(-\infty,2].
\]
Since $(-\infty,2]$ is closed in $\mathbb{R}$, the intersection is closed in the subspace $(1,3)$.
Equivalently, the complement $(1,3)\setminus(1,2]=(2,3)$ is open in $(1,3)$ (it is $(1,3)\cap(2,\infty)$),
so $(1,2]$ is closed but not open in the subspace.

	\par\noindent\textbullet\quad In the space $(1,2]$ itself, it is clopen (the whole space).

If $X$ has the discrete metric $d(x,y)=\mathbf 1_{x\ne y}$ and $Y$ is any metric space, then:

	\par\noindent\textbullet\quad Every subset of $X$ is open (hence also closed).
	\par\noindent\textbullet\quad The compact subsets of $X$ are exactly the finite subsets.
	\par\noindent\textbullet\quad A sequence in $X$ is Cauchy iff it is eventually constant.
	\par\noindent\textbullet\quad Every function $f:X\to Y$ is continuous.
```

## CP-II-0269

- chapter line: 4364

```tex
\label{prob:cp-ii-0269}
Let $f(x) = \sqrt{x}$ on $E=[0,1]$.
		Here $E$ is compact and $f$ is continuous.
		By Heine--Cantor, $f$ is uniformly continuous, even though $f'(x)=\tfrac{1}{2\sqrt{x}}$ is unbounded near $0$.
```

## CP-II-0271

- chapter line: 4371

```tex
\label{prob:cp-ii-0271}
\par\noindent\textbullet\quad In metric spaces, $F$ is l.s.c.\ (resp.\ u.s.c.) iff for all $x_n\to x$,
		$\displaystyle F(x)\le\liminf_n F(x_n)$ (resp.\ $\displaystyle F(x)\ge\limsup_n F(x_n)$).

	Let $X$ be a Banach space.
```
