# Part II missing-solution batch 04

- problems: **20**
- IDs: CP-II-0372, CP-II-0375, CP-II-0393, CP-II-0395, CP-II-0396, CP-II-0406, CP-II-0411, CP-II-0413, CP-II-0415, CP-II-0424, CP-II-0426, CP-II-0434, CP-II-0441, CP-II-0443, CP-II-0445, CP-II-0453, CP-II-0458, CP-II-0460, CP-II-0467, CP-II-0468

## CP-II-0372

- chapter line: 6256

```tex
\label{prob:cp-ii-0372}
— Polynomial (vs.\ rational) approximation on a punctured disc

paragraph{Problem (exact).}
Let $B_r(z)$ denote the open disc of radius $r$ about $z\in\mathbb C$ and set
\[
U \;=\; B_2(1)\setminus B_1(0).
\]
Suppose $f$ is holomorphic on $U$.

	\par\noindent\textbullet\quad Prove that there exists a sequence of \emph{rational functions} which converges to $f$
	uniformly on compact subsets of $U$.
	\par\noindent\textbullet\quad Must there be a sequence of \emph{polynomials} which converges to $f$ uniformly on $U$?
	\par\noindent\textbullet\quad If, in addition, $f$ is holomorphic on some open set containing $\overline U$,
	must there be a sequence of \emph{polynomials} which converges to $f$ uniformly on $U$?

We will use the following results.

	\par\noindent\textbullet\quad \textbf{RungeĂ˘â‚¬â„˘s theorem (rational form).}
	Let $K\subset\mathbb C$ be compact and let $E=\widehat{\mathbb C}\setminus K$.
	If $E$ has finitely many components, then every function holomorphic on a neighborhood
	of $K$ can be uniformly approximated on $K$ by rational functions whose poles lie in a
	prescribed finite set containing at least one point from each bounded component of $E$.
	If $E$ is connected and contains $\infty$, the approximants can be chosen to be polynomials.
	\par\noindent\textbullet\quad \textbf{MergelyanĂ˘â‚¬â„˘s theorem (polynomial form).}
	If $K\subset\mathbb C$ is compact with connected complement and $f$ is continuous on $K$
	and holomorphic in $\operatorname{int}K$, then there exists a sequence of polynomials
	converging uniformly to $f$ on $K$.
	\par\noindent\textbullet\quad \textbf{Cauchy integral test for non-approximability.}
	If $p_n\to g$ uniformly on a simple closed curve $\Gamma$, then
	$\int_\Gamma p_n(z)\,dz\to\int_\Gamma g(z)\,dz$.
	For every polynomial $p$, $\int_\Gamma p(z)\,dz=0$.
	\par\noindent\textbullet\quad \textbf{Geometry of $U$.}
	The complement of $U$ in the Riemann sphere has two components:
	the unbounded $\mathbb C\setminus B_2(1)$ (containing $\infty$) and the bounded
	$\overline{B_1(0)}$ (containing $0$). Thus RungeĂ˘â‚¬â„˘s theorem yields rational
	approximation on compacts of $U$ with all poles placed in the bounded component
	(e.g.\ at $0$), but not, in general, polynomial approximation on all of $U$ unless
	$f$ extends holomorphically across the hole so that the relevant compact has
	connected complement.

Let $B_r(z)$ be the open disc of radius $r$ about $z\in\mathbb C$ and
$U=B_2(1)\setminus B_1(0)$. Assume $f$ is holomorphic on $U$.

The complement $\widehat{\mathbb C}\setminus U$ has two components:
the unbounded $\mathbb C\setminus B_2(1)$ and the bounded $\overline{B_1(0)}$.
By RungeĂ˘â‚¬â„˘s theorem, for every compact $K\Subset U$ there exist rational functions $r_n$
with all poles in $\overline{B_1(0)}$ (indeed at $0$) such that $r_n\to f$
uniformly on $K$. Thus $f$ is locally uniformly approximable by rational functions with poles at $0$.
\emph{(If the statement asks for polynomials, this is false in general; see (ii).)}

\emph{No.} Consider $f(z)=1/z\in O(U)$. Suppose polynomials $p_n$ satisfy $p_n\to f$
uniformly on $U$. Let $\Gamma=\{\,|z|=r\,\}$ with $1<r<2$ and $\Gamma\subset U$.
Then
\[
\int_\Gamma p_n(z)\,dz \longrightarrow \int_\Gamma \frac{1}{z}\,dz = 2\pi i,
\]
whereas for all polynomials $p_n$ we have $\int_\Gamma p_n(z)\,dz=0$ by CauchyĂ˘â‚¬â„˘s theorem,
a contradiction. Hence, in general, no such polynomial sequence exists.

Assume $f$ is holomorphic on some open set $W\supset \overline U$.
Then $f$ is holomorphic on a neighborhood of the compact set $K=\overline{B_2(1)}$,
whose complement is connected and contains $\infty$.
By RungeĂ˘â‚¬â„˘s theorem (or MergelyanĂ˘â‚¬â„˘s theorem),
there are polynomials $p_n$ with $p_n\to f$ uniformly on $K$; in particular,
$p_n\to f$ uniformly on $U$.
Therefore under this additional assumption the answer is \emph{yes}.
```

## CP-II-0375

- chapter line: 6326

```tex
\label{prob:cp-ii-0375}
\par\noindent\textbullet\quad \emph{Compact}: every open cover has a finite subcover (equivalently in metric spaces: sequentially compact).

\bigskip

Fix the scale sequence $\varepsilon_m := 2^{-m}$ for $m\in\mathbb{N}$.

\medskip

\emph{Step 1 (first thinning).} By total boundedness, $X$ can be covered by finitely many balls of radius $\varepsilon_1$.
One of these balls contains infinitely many terms of $(x_k)$. Pass to that infinite subsequence and relabel it $(x^{(1)}_k)$.

\medskip

\emph{Step 2 (iterated thinning).} Again by total boundedness, cover $X$ by finitely many balls of radius $\varepsilon_2$.
One such ball contains infinitely many terms of $(x^{(1)}_k)$. Pass to that infinite subsequence and relabel it $(x^{(2)}_k)$.

\medskip

\emph{Step 3 (continue).} Proceed inductively: after step $m$ we have an infinite subsequence
$(x^{(m)}_k)$ contained in a single ball of radius $\varepsilon_m$.

\medskip

\emph{Step 4 (diagonal choice).} Define the diagonal subsequence $y_m := x^{(m)}_m$.
Then $y_m$ lies inside a ball of radius $\varepsilon_m$ that contains all but finitely many terms of the previous stage.
In particular,
\[
d(y_{m+1},y_m) \;<\; \varepsilon_m \qquad \text{for all } m\in\mathbb{N}.
\]

\medskip

\emph{Step 5 (Cauchy property).} Let $\varepsilon>0$ and choose $M$ with $\varepsilon_M<\varepsilon/2$.
For $n>m\ge M$, the points $y_m,y_n$ both lie in a ball of radius $\varepsilon_m\le \varepsilon_M<\varepsilon/2$,
so $d(y_m,y_n)\le 2\varepsilon_M<\varepsilon$. Hence $(y_m)$ is Cauchy.

\medskip

Thus every sequence in a totally bounded metric space admits a Cauchy subsequence.

\bigskip

\emph{($\Rightarrow$) Compact $\Rightarrow$ complete and totally bounded.}
Compact metric spaces are sequentially compact. A Cauchy sequence has a convergent subsequence;
Cauchy $+$ convergent subsequence forces the whole sequence to converge, hence completeness.
Total boundedness follows since otherwise some $\varepsilon$-net would require infinitely many balls,
contradicting compactness (use a standard Lebesgue number/covering argument).

\medskip

\emph{($\Leftarrow$) Complete and totally bounded $\Rightarrow$ compact.}
Let $(x_k)$ be any sequence in $X$. By (a), it has a Cauchy subsequence; by completeness this subsequence converges in $X$.
Hence $X$ is sequentially compact. In metric spaces, sequential compactness is equivalent to compactness.
Therefore $X$ is compact.

\hfill$\Box$
```

## CP-II-0393

- chapter line: 6543

```tex
\label{prob:cp-ii-0393}
\par\noindent\textbullet\quad Haar measure on a locally compact topological group $G$ is a Radon Borel measure on $\mathcal{B}(G)$.

	\bigskip\bigskip

	\[
	\text{Topology on } X
	\ \Longrightarrow\
	\mathcal{B}(X)
	\ \xrightarrow{\ \text{measure}\ }\
	\text{Borel measure}
	\ \xRightarrow[\text{locally finite}]{\text{inner/outer regular}}
	\ \text{Radon measure}.
	\]

	On a locally compact group $G$, a Radon Borel measure that is left-invariant
	is Haar measure (unique up to scale). Given a reference Radon measure $\mu$
	(e.g.\ Lebesgue or Haar), any finite measure $\nu$ admits the \emph{Lebesgue decomposition}
	$\nu=\nu_a+\nu_s$ with $\nu_a\ll\mu$ and $\nu_s\perp\mu$.
```

## CP-II-0395

- chapter line: 6565

```tex
\label{prob:cp-ii-0395}
Let $X$ be a reflexive Banach space, and let $Y\subset X$ be a closed subspace. Show that $Y$ is reflexive.

	In a reflexive Banach space, the closed unit ball is weakly compact.
	Since $B_Y=B_X\cap Y$ is closed, bounded and convex, it is weakly compact in the relative weak topology of $Y$.
	By KakutaniĂ˘â‚¬â„˘s theorem (or JamesĂ˘â‚¬â„˘ criterion), $Y$ is reflexive.
	Equivalently, the canonical map $J_Y:Y\to Y''$ is surjective because every bounded sequence in $Y$ admits a weakly convergent subsequence; its limit represents the image under $J_Y$.

	Any closed subspace of $L^p(\Omega)$ ($1<p<\infty$), e.g.\ $W^{1,p}_0(\Omega)$, is reflexive;
	any closed subspace of $\ell^2$ is reflexive.

	Let $X$ be a Banach space, $X'$ its dual, and $X''=(X')'$ its bidual.
	The canonical map $J_X:X\to X''$ is given by
	\[
	J_X(x)(\varphi)=\varphi(x)\qquad(\varphi\in X').
	\]
	It is linear and isometric. We say that $X$ is \emph{reflexive} if $J_X$ is surjective
	(equivalently $X\cong X''$ isometrically).

		\par\noindent\textbullet\quad \textbf{Kakutani.} $X$ is reflexive $\iff$ the closed unit ball $B_X$ is weakly compact.
		\par\noindent\textbullet\quad \textbf{Eberlein--\v{S}mulian.} In Banach spaces, weak compactness $\iff$ weak sequential compactness.
		Hence $X$ is reflexive $\iff$ every bounded sequence in $X$ has a weakly convergent subsequence.
		\par\noindent\textbullet\quad \textbf{James.} $X$ is reflexive $\iff$ every $\varphi\in X'$ attains its norm on $B_X$.
		\par\noindent\textbullet\quad \textbf{Dual stability.} $X$ is reflexive $\iff$ $X'$ is reflexive.
		\par\noindent\textbullet\quad \textbf{Uniform convexity (Milman--Pettis).} If $X$ is uniformly convex, then $X$ is reflexive.

	If $X$ is reflexive and $Y\subset X$ is a closed subspace, then $Y$ is reflexive.
	Moreover, the quotient $X/Y$ is also reflexive.

		\par\noindent\textbullet\quad \textbf{Reflexive.} Every finite dimensional normed space; every Hilbert space;
		$L^{p}(\Omega)$ for $1<p<\infty$; $\ell^{p}$ for $1<p<\infty$; Sobolev spaces
		$W^{k,p}(\Omega)$ for $1<p<\infty$, and closed subspaces like $W^{1,p}_0(\Omega)$.
		\par\noindent\textbullet\quad \textbf{Non-reflexive.} $L^{1}(\Omega)$ and $L^{\infty}(\Omega)$;
		$\ell^{1}$, $\ell^{\infty}$, and $c_{0}$; $C(K)$ with $\|\cdot\|_\infty$ for infinite compact $K$.

		\par\noindent\textbullet\quad If $H$ is a Hilbert space, any closed subspace $M\subset H$ is reflexive
		(it is itself a Hilbert space with the induced inner product).
		\par\noindent\textbullet\quad In $L^{p}(\Omega)$, $1<p<\infty$, examples include:

			\par\noindent\textbullet\quad $W^{1,p}_0(\Omega)$ (closure of $C_c^\infty$ in $W^{1,p}$),
			\par\noindent\textbullet\quad kernels of bounded operators (e.g.\ $\{f:\int_\Omega f=0\}$),
			\par\noindent\textbullet\quad ranges/orthogonal complements when $p=2$.

		All are reflexive since they are closed subspaces of a reflexive space.
		\par\noindent\textbullet\quad In a non-reflexive space (e.g.\ $L^{1}$), closed subspaces can be
		\emph{either} reflexive (finite-dimensional) \emph{or} non-reflexive
		(e.g.\ a closed subspace isomorphic to $\ell^{1}$).

	If $X$ is reflexive, every bounded sequence admits a weakly convergent subsequence.
	Minimization of weakly lower semicontinuous convex functionals on closed, convex, bounded sets
	is therefore well-posed (direct method of the calculus of variations).

		\par\noindent\textbullet\quad Finite-dimensional $\Rightarrow$ reflexive.
		\par\noindent\textbullet\quad Uniformly convex (e.g.\ Hilbert, $L^p$ with $1<p<\infty$) $\Rightarrow$ reflexive.
		\par\noindent\textbullet\quad Unit ball weakly compact / every bounded sequence has a weakly convergent subsequence $\Rightarrow$ reflexive.
		\par\noindent\textbullet\quad Presence of subspaces isomorphic to $\ell^1$ or $c_0$ often signals non-reflexivity.

	Let $X$ be a Banach space, $X'$ its dual and $X''=(X')'$ its bidual.
	The canonical map $J_X:X\to X''$ is
	\[
	J_X(x)(\varphi)=\varphi(x)\qquad(\varphi\in X').
	\]
	Then $J_X$ is linear and isometric. We call $X$ \emph{reflexive} if $J_X$ is surjective
	(equivalently $X\cong X''$ isometrically).

	The following are equivalent:

		\par\noindent\textbullet\quad (Kakutani) The closed unit ball $B_X$ is weakly compact.
		\par\noindent\textbullet\quad (Eberlein--\v{S}mulian) Every bounded sequence in $X$ admits a weakly convergent subsequence.
		\par\noindent\textbullet\quad (James) Every $\varphi\in X'$ attains its norm on $B_X$.

	Moreover, if $X$ is uniformly convex (e.g.\ $L^p$, $1<p<\infty$), then $X$ is reflexive (Milman--Pettis).

	\par\noindent\textbullet\quad \textbf{Dual.} $(L^p)'\cong L^{p'}$ via $g\mapsto\big[f\mapsto\!\int f g\,d\mu\big]$, with $1/p+1/p'=1$.
	\par\noindent\textbullet\quad \textbf{Bidual.} $(L^p)''\cong (L^{p'})'\cong L^p$.
	\par\noindent\textbullet\quad \textbf{Why onto?} The canonical $J_{L^p}$ is an isometric isomorphism because $L^p$ is uniformly convex (Milman--Pettis) and the duality pairing is full. \textbf{Hence reflexive.}

	\par\noindent\textbullet\quad \textbf{Dual.} $(L^1)'\cong L^\infty$ (pointwise multiplier functionals).
	\par\noindent\textbullet\quad \textbf{Bidual.} $(L^1)''\cong (L^\infty)'$, but $(L^\infty)'=\mathrm{ba}(\mu)$ (bounded finitely additive signed measures, Yosida--Hewitt), which strictly contains $L^1$. The canonical embedding $L^1\hookrightarrow (L^\infty)'$ hits only the countably additive part.
	\par\noindent\textbullet\quad \textbf{Conclusion.} $J_{L^1}$ is not onto (except in essentially finite cases), so \textbf{$L^1$ is non-reflexive}.

	\par\noindent\textbullet\quad \textbf{Dual.} $(L^\infty)'=\mathrm{ba}(\mu)$ (strictly larger than $L^1$).
	\par\noindent\textbullet\quad \textbf{Bidual.} $(L^\infty)''$ is huge; the canonical map is not surjective. \textbf{Thus non-reflexive.}

	\par\noindent\textbullet\quad \textbf{Dual.} $(\ell^p)'\cong \ell^{p'}$ via $\phi_y(x)=\sum_{k=1}^\infty x_k\overline{y_k}$.
	\par\noindent\textbullet\quad \textbf{Bidual.} $(\ell^p)''\cong \ell^p$.
	\par\noindent\textbullet\quad \textbf{Conclusion.} Uniformly convex $\Rightarrow J_{\ell^p}$ onto $\Rightarrow$ \textbf{reflexive}.

	\par\noindent\textbullet\quad \textbf{Dual.} $(\ell^1)'\cong \ell^\infty$.
	\par\noindent\textbullet\quad \textbf{Bidual.} $(\ell^1)''\cong (\ell^\infty)'$ (far larger than $\ell^1$).
	\par\noindent\textbullet\quad \textbf{Conclusion.} $J_{\ell^1}$ not onto $\Rightarrow$ \textbf{non-reflexive}.

	\par\noindent\textbullet\quad \textbf{Dual.} $c_0'=\ell^1$.
	\par\noindent\textbullet\quad \textbf{Bidual.} $c_0''=(\ell^1)'=\ell^\infty$. The canonical embedding $c_0\hookrightarrow\ell^\infty$ is the inclusion, which is not onto.
	\par\noindent\textbullet\quad \textbf{Conclusion.} $c_0$ is \textbf{non-reflexive}.

	\par\noindent\textbullet\quad \textbf{Dual.} $C(K)'\cong M(K)$ (finite regular Borel measures, Riesz--Markov).
	\par\noindent\textbullet\quad \textbf{Bidual.} $C(K)''\cong M(K)'$; the canonical map is onto iff $C(K)$ is finite-dimensional.
	\par\noindent\textbullet\quad \textbf{Conclusion.} $C(K)$ is \textbf{reflexive iff $K$ is finite} (then $C(K)\cong \mathbb{K}^n$).

If $X$ is reflexive and $Y\subset X$ is closed, then $Y$ and $X/Y$ are reflexive. Hence closed subspaces of $L^p$, $1<p<\infty$ (e.g.\ $W^{1,p}_0(\Omega)$, mean-zero subspaces, kernels of bounded maps) are reflexive.

	\textbf{Theorem.} Let $(x_n)$ be a sequence in a Banach space $X$ with $x_n \rightharpoonup x$.
	Then there exist finite convex combinations of the tails
	\[
	y_k=\sum_{n\ge k}\alpha^{(k)}_n\,x_n,\qquad \alpha^{(k)}_n\ge 0,\ \sum_{n\ge k}\alpha^{(k)}_n=1,
	\]
	such that $y_k \to x$ in norm.

	\textbf{Equivalent form.} For any convex $C\subset X$,
	\[
	\overline{C}^{\,\mathrm{weak}}=\overline{C}^{\,\|\cdot\|}.
	\]

	\textbf{Sketch of proof.} If no convex averages converge strongly, the sets
	$A_k=\overline{\mathrm{co}}\{x_n:n\ge k\}$ stay a positive distance from $x$.
	By Hahn–Banach, separate $x$ from $A_k$ with $\varphi_k\in X'$, contradicting
	$\varphi_k(x_n)\to\varphi_k(x)$ (weak convergence). Hence some convex averages converge in norm.

	\textbf{Examples.}

		\par\noindent\textbullet\quad $X=L^p(\Omega)$, $1\le p<\infty$: if $f_n\rightharpoonup f$, then $\exists$ convex averages $g_k$ with $\|g_k-f\|_p\to 0$.
		\par\noindent\textbullet\quad $X=H$ Hilbert: if $x_n\rightharpoonup x$, then Ces\`aro means of a subsequence converge to $x$ in norm.

	\bigskip

	\textbf{Theorem.} Let $X$ be a Banach space, $K\subset X$ open and convex, $C\subset X$ closed and convex,
	and $K\cap C=\varnothing$. Then there exist $\Lambda\in X'\setminus\{0\}$ and $\alpha\in\mathbb R$ such that
	\[
	\Re\Lambda(c)\le \alpha \quad\text{for all } c\in C, \qquad
	\inf_{k\in K}\Re\Lambda(k)>\alpha.
	\]
	In particular, if $C=M$ is a closed subspace disjoint from $K$, then $N:=\ker\Lambda$ is a closed
	hyperplane (codimension one) containing $M$ and disjoint from $K$.

	\textbf{Examples.}

		\par\noindent\textbullet\quad $X=\mathbb R^2$, $K=B((0,1),1)$, $M=\{(t,0):t\in\mathbb R\}$.
		With $\Lambda(x,y)=y$ we have $\Lambda(M)=\{0\}$ and $\Lambda(K)=(0,2)$.
		\par\noindent\textbullet\quad $X=\ell^2$, $M=\mathrm{span}\{e_1\}$, $K=B(e_2,\tfrac12)$.
		The functional $\Lambda(x)=\langle x,e_1\rangle$ and a suitable translation yield a separating hyperplane $N=\ker\Lambda$.

	\bigskip

		\par\noindent\textbullet\quad \emph{Closure of convex sets:} MazurĂ˘â‚¬â„˘s lemma $\Rightarrow$ weak and strong closures of convex sets coincide.
		\par\noindent\textbullet\quad \emph{Optimization:} Direct method—weak limits of minimizing sequences can be averaged to obtain strong convergence.
		\par\noindent\textbullet\quad \emph{Spaces:} All Banach spaces (e.g.\ Hilbert, $L^p$ with $1\le p\le\infty$, Sobolev spaces) admit both results.

	For $1\le p<\infty$,
	\[
	\ell^p := \Bigl\{ x=(x_k)_{k\ge1} : \sum_{k=1}^{\infty} |x_k|^p < \infty \Bigr\},
	\qquad
	\|x\|_{\ell^p} := \Bigl( \sum_{k=1}^{\infty} |x_k|^p \Bigr)^{1/p}.
	\]
	For $p=\infty$,
	\[
	\ell^\infty := \Bigl\{ x=(x_k): \sup_{k} |x_k| < \infty \Bigr\},
	\qquad
	\|x\|_{\ell^\infty} := \sup_{k} |x_k|.
	\]
	Then $(\ell^p,\|\cdot\|_{\ell^p})$ is a Banach space for all $1\le p\le\infty$.
	In particular,
	\[
	\ell^2 \text{ is a Hilbert space with }
	\langle x,y\rangle := \sum_{k=1}^\infty x_k \overline{y_k}.
	\]
	For $1<p<\infty$, the dual space $(\ell^p)'$ is isometrically isomorphic to $\ell^{p'}$,
	where $1/p+1/p'=1$, via $y\mapsto[x\mapsto \sum_k x_k \overline{y_k}]$.

	Let $(\Omega,\mathcal F,\mu)$ be a measure space. For $1\le p<\infty$,
	\[
	L^p(\mu) := \Bigl\{ [f] : f \text{ measurable},\ \int_\Omega |f|^p\,d\mu < \infty \Bigr\},
	\qquad
	\|f\|_{L^p} := \Bigl( \int_\Omega |f|^p\, d\mu \Bigr)^{1/p}.
	\]
	Elements are equivalence classes modulo equality $\mu$-a.e.
	For $p=\infty$,
	\[
	L^\infty(\mu) := \Bigl\{ [f] : \operatorname*{ess\,sup}_{\Omega} |f| < \infty \Bigr\},
	\qquad
	\|f\|_{L^\infty} := \operatorname*{ess\,sup}_{\Omega} |f|.
	\]
	Then $L^p(\mu)$ is a Banach space for $1\le p\le\infty$. For $1<p<\infty$:
	\begin{align*}
		\text{(H\"older)}\quad & \int_\Omega |fg|\,d\mu \le \|f\|_{L^p}\,\|g\|_{L^{p'}},\\
		\text{(Minkowski)}\quad & \|f+g\|_{L^p} \le \|f\|_{L^p}+\|g\|_{L^p},\\
		\text{(Duality)}\quad & (L^p(\mu))' \cong L^{p'}(\mu),\quad \tfrac1p+\tfrac1{p'}=1,
	\end{align*}
	via $g\mapsto \bigl[f\mapsto \int_\Omega f\,g\,d\mu\bigr]$.
```

## CP-II-0396

- chapter line: 6757

```tex
\label{prob:cp-ii-0396}
Gluing (Pasting) Continuous Maps

Let $(X,\tau)$ be a topological space with $X=A\cup B$ and $(Y,\rho)$ another space.
	Let $g:A\to Y$ and $h:B\to Y$ be continuous (with subspace topologies) and suppose $g=h$ on $A\cap B$.
	Define
	\[
	f(x)=
	\begin{cases}
		g(x),& x\in A,\\
		h(x),& x\in B.
	\end{cases}
	\]

	\begin{proof}
		Let $C\subseteq Y$ be closed. Since $g$ is continuous, $g^{-1}(C)$ is closed in $A$, so $g^{-1}(C)=A\cap F$ for some closed $F\subseteq X$.
		Similarly $h^{-1}(C)=B\cap G$ for some closed $G\subseteq X$.
		Then
		\[
		f^{-1}(C)=\big(A\cap g^{-1}(C)\big)\cup\big(B\cap h^{-1}(C)\big)=(A\cap F)\cup(B\cap G),
		\]
		a union of closed subsets of $X$. Hence $f^{-1}(C)$ is closed for every closed $C$, so $f$ is continuous.
	\end{proof}

\textit{Counterexample.}
Let \(X=(0,2]\) with the subspace topology from \(\mathbb{R}\).
Take \(A=(0,1)\) (not closed in \(X\)) and \(B=[1,2]\) (closed).

Define \(g\equiv 0\) on \(A\) and \(h\equiv 1\) on \(B\).
They agree on \(A\cap B=\varnothing\), so the glued map
\[
f(x)=
\begin{cases}
	0, & x\in A,\\[4pt]
	1, & x\in B
\end{cases}
\]
is well-defined.

For the open set \(U=\bigl(\tfrac12,\tfrac32\bigr)\subset\mathbb{R}\) we have
\[
f^{-1}(U)=B=[1,2],
\]
which is not open in \(X\) (every neighborhood of \(1\) in \(X\) meets \(A\)).

Thus \(f\) is not continuous.

	If $A$ and $B$ are both \emph{open} in $X$, then for any open $U\subseteq Y$,
	\[
	f^{-1}(U)=(A\cap g^{-1}(U))\cup(B\cap h^{-1}(U)),
	\]
	and each term is open in $X$ (since $g^{-1}(U)$ is open in $A$, it equals $A\cap G$ for some open $G\subseteq X$).
	Hence $f$ is continuous when $A,B$ form an open cover as well.
```

## CP-II-0406

- chapter line: 6813

```tex
\label{prob:cp-ii-0406}
Connected sums \(\#^k(S^3\times S^3)\) (dimension \(6\))

Let
\[
M=\#^k(S^3\times S^3).
\]
Then \(M\) is closed oriented of dimension \(6\), and the middle degree is \(3\).
For connected sums in dimension \(\ge 3\),
\[
H_3\!\left(\#^k(S^3\times S^3);\mathbb Q\right)
\cong
\bigoplus_{j=1}^k H_3(S^3\times S^3;\mathbb Q)
\cong
(\mathbb Q^2)^{\oplus k}\cong \mathbb Q^{2k}.
\]
Thus
\[
\dim_{\mathbb Q} H_3(M;\mathbb Q)=2k,
\]
again even. This gives a large family where the middle Betti number can be any even integer.

\subsubsection{Example 5: Products \(\Sigma_g\times S^{4n}\) (general \(n\ge 1\))}

Let \(n\ge 1\) and set
\[
M=\Sigma_g\times S^{4n}.
\]
Then \(\dim M=2+4n=4n+2\), and the middle degree is \(2n+1\).
By K\"unneth over \(\mathbb Q\),
\[
H_{2n+1}(M;\mathbb Q)
\cong
\bigoplus_{i+j=2n+1} H_i(\Sigma_g;\mathbb Q)\otimes H_j(S^{4n};\mathbb Q).
\]
But the only nonzero rational homology of \(S^{4n}\) is in degrees \(0\) and \(4n\), so the only possible
summands would require \(j=0\) or \(j=4n\), i.e.
\[
i=2n+1 \quad \text{or}\quad i=2n+1-4n=1-2n.
\]
For \(n\ge 1\), both indices are impossible for \(\Sigma_g\) (the first is \(>2\), the second is negative), so
\[
H_{2n+1}(\Sigma_g\times S^{4n};\mathbb Q)=0.
\]
Hence the middle Betti number is \(0\), which is even.

The evenness argument uses a nondegenerate \emph{alternating} pairing on \(H^{2n+1}(M;\mathbb Q)\).
Over a field of characteristic \(2\), Ă˘â‚¬Ĺ›skew-symmetricĂ˘â‚¬ĹĄ and Ă˘â‚¬Ĺ›symmetricĂ˘â‚¬ĹĄ coincide, and one can no longer
conclude that the dimension must be even. This is why the clean parity statement is formulated over
\(\mathbb Q\) (or any field of characteristic \(\neq 2\)).

An \(n\)-manifold \(M\) is \textbf{closed} if it is \emph{compact} and has \emph{empty boundary}:
\[
M \text{ closed}\quad \Longleftrightarrow\quad M \text{ compact and }\partial M=\varnothing.
\]
Examples: \(S^n\), \(T^n\), \(\mathbb{CP}^m\).
Non-examples: \(D^n\) (has boundary), \(\mathbb R^n\) (not compact).

A manifold \(M\) is \textbf{orientable} if one can choose a consistent orientation on all coordinate
charts (equivalently, all transition maps between oriented charts have positive Jacobian determinant in the smooth case).
There are several equivalent algebraic-topological characterizations.

\begin{remark}[Homology characterization for closed connected manifolds]
	If \(M\) is a connected closed \(n\)-manifold, then
	\[
	M \text{ orientable}\quad \Longleftrightarrow\quad H_n(M;\mathbb Z)\cong \mathbb Z,
	\]
	and
	\[
	M \text{ nonorientable}\quad \Longleftrightarrow\quad H_n(M;\mathbb Z)=0.
	\]
\end{remark}

Saying that \(M\) is \textbf{\(\mathbb Z\)-orientable} means that \(M\) admits a fundamental class with integer coefficients.
For a connected closed \(n\)-manifold this is exactly the usual notion of orientability:
\[
\mathbb Z\text{-orientable}\quad \Longleftrightarrow\quad \text{orientable}.
\]

Let \(F\) be a field. A connected closed \(n\)-manifold \(M\) is called \textbf{\(F\)-orientable} if it admits a fundamental class
\([M]_F\in H_n(M;F)\), equivalently
\[
H_n(M;F)\cong F.
\]
In particular, \(M\) is \textbf{\(\mathbb Q\)-orientable} if
\[
H_n(M;\mathbb Q)\cong \mathbb Q.
\]

\begin{remark}[Relations between \(\mathbb Z\)- and \(\mathbb Q\)-orientability]
	For closed connected manifolds one has
	\[
	\mathbb Z\text{-orientable}\ \Longrightarrow\ \mathbb Q\text{-orientable}.
	\]
	Moreover, since \(\mathbb Q\) has characteristic \(\neq 2\), for manifolds one actually has the equivalence
	\[
	\mathbb Q\text{-orientable}\ \Longleftrightarrow\ \mathbb Z\text{-orientable}\ \Longleftrightarrow\ \text{orientable}.
	\]
\end{remark}

Over the field \(\mathbb F_2\), signs disappear (\(-1=+1\)), and every manifold becomes orientable.

\begin{remark}[\(\mathbb F_2\)-orientability]
	Every connected closed manifold \(M\) is \(\mathbb F_2\)-orientable:
	\[
	H_n(M;\mathbb F_2)\cong \mathbb F_2.
	\]
	For example, \(\mathbb{RP}^2\) is not \(\mathbb Z\)-orientable (so \(H_2(\mathbb{RP}^2;\mathbb Z)=0\)),
	but it is \(\mathbb F_2\)-orientable (so \(H_2(\mathbb{RP}^2;\mathbb F_2)\cong \mathbb F_2\)).
\end{remark}

Let \(M\) be a connected closed \(n\)-manifold and let \(F\) be a field.
If \(M\) is \(F\)-orientable, then Poincar\'e duality holds with coefficients in \(F\):
\[
H^i(M;F)\cong H_{n-i}(M;F),
\]
via cap product with the fundamental class \([M]_F\).
In particular:

	\par\noindent\textbullet\quad If \(M\) is orientable, then duality holds over \emph{any} field \(F\) (including \(\mathbb Q\)).
	\par\noindent\textbullet\quad For an arbitrary (possibly nonorientable) manifold, duality always holds over \(\mathbb F_2\).

For connected closed manifolds:
\[
\text{orientable}\ \Longleftrightarrow\ \mathbb Z\text{-orientable}\ \Longleftrightarrow\ \mathbb Q\text{-orientable},
\]
while
\[
\text{every manifold is } \mathbb F_2\text{-orientable}.
\]
```

## CP-II-0411

- chapter line: 6966

```tex
\label{prob:cp-ii-0411}
Finite Products of Metrizable Spaces

Show that a finite product of metrizable topological spaces is metrizable. (Hint: start with two metric spaces and define a metric on the product.)

Let $(X,d)$ and $(Y,e)$ be metric spaces. Set $\displaystyle d_1(x,x')=\min\{1,d(x,x')\}$ and $\displaystyle e_1(y,y')=\min\{1,e(y,y')\}$, which induce the same topologies as $d$ and $e$ but are bounded by $1$.
Define
\[
D\big((x,y),(x',y')\big)=d_1(x,x')+e_1(y,y').
\]
Then $D$ is a metric on $X\times Y$.

We claim that the topology induced by $D$ equals the product topology.

(i) If $D((x,y),(x',y'))<r$, then $d_1(x,x')<r$ and $e_1(y,y')<r$, hence
\[
B_D((x,y),r)\subseteq B_{d_1}(x,r)\times B_{e_1}(y,r),
\]
so every $D$-open set is product-open.

(ii) Conversely, let $U=B_{d_1}(x,\alpha)$ and $V=B_{e_1}(y,\beta)$. For $r=\min\{\alpha,\beta\}/2$ we have
\[
B_D((x,y),r)\subseteq U\times V,
\]
so every basic product-open set is $D$-open.

Thus the two topologies coincide, and $X\times Y$ is metrizable.

If $(X_i,d_i)$ for $i=1,\dots,n$ are metric,

 define on $X=\prod_{i=1}^n X_i$ the metric
\[
D\big((x_i),(x_i')\big)=\sum_{i=1}^n \min\{1,d_i(x_i,x_i')\}.
\]
Exactly the same containment argument shows that $D$ induces the product topology on $X$. Hence any finite product of metrizable spaces is metrizable.

	\par\noindent\textbullet\quad $\mathbb{R}^n$ is metrizable (finite product of $(\mathbb{R},|\cdot|)$).
	\par\noindent\textbullet\quad A finite product of discrete spaces is again discrete (hence metrizable).
	\par\noindent\textbullet\quad $S^1\times[0,1]$ is metrizable; for instance, with
	\[
	d\big((\theta,t),(\phi,s)\big)
	=\sqrt{\,d_{S^1}(\theta,\phi)^2 + |t-s|^2\,},
	\]
	where $d_{S^1}$ is the arc-length distance on the circle.
```

## CP-II-0413

- chapter line: 7013

```tex
\label{prob:cp-ii-0413}
— Stability of translations and difference quotients

Let
\[
X\in\bigl\{\mathcal D(\mathbb R^n),\ \mathcal S(\mathbb R^n),\ \mathcal E(\mathbb R^n)\bigr\},
\qquad \phi\in X.
\]
Establish the following properties.

\bigskip

\textbf{(a)} If $x_\ell\in\mathbb R^n$ with $x_\ell\to0$, then
\[
\tau_{x_\ell}\phi\longrightarrow\phi
\qquad\text{in }X\text{ as }\ell\to\infty,
\]
where the translation operator $\tau_x$ is defined by
\[
(\tau_x\phi)(y):=\phi(y-x).
\]

\bigskip

\textbf{(b)} If $h_\ell\in\mathbb R$ with $h_\ell\to0$, then
\[
\Delta_i^{h_\ell}\phi\longrightarrow D_i\phi
\qquad\text{in }X\text{ as }\ell\to\infty,
\]
where
\[
\Delta_i^{h}\phi
:=h^{-1}\bigl(\tau_{h e_i}\phi-\phi\bigr)
=\frac{\phi(\cdot-h e_i)-\phi}{h}
\]
is the \emph{difference quotient} in the $i$-th coordinate direction.

\bigskip

In words: small translations of a smooth function tend to zero in the topology of $X$, and the difference quotients converge to the partial derivative $D_i\phi$ in the same sense.

\bigskip

\textit{Case $X=\mathcal E(\mathbb R^n)$.}
Fix a compact $K\Subset\mathbb R^n$ and $m\in\mathbb N$. For any multi-index $\alpha$ with $|\alpha|\le m$,
\[
\sup_{y\in K}\big|D^\alpha(\tau_{x_\ell}\phi-\phi)(y)\big|
=\sup_{y\in K}\big|D^\alpha\phi(y-x_\ell)-D^\alpha\phi(y)\big|.
\]
Choose a compact $K'$ containing $K\cup(K-x_\ell)$ for all large $\ell$. Since $D^\alpha\phi$ is uniformly continuous on $K'$, the right-hand side tends to $0$ as $\ell\to\infty$. Hence $\tau_{x_\ell}\phi\to\phi$ in $\mathcal E$.

\bigskip

\textit{Case $X=\mathcal D(\mathbb R^n)$.}
Choose a compact $K$ with $\operatorname{supp}\phi\subset K^\circ$. For $\ell$ large,
\[
\operatorname{supp}(\tau_{x_\ell}\phi)\subset K+x_\ell\subset K'',
\]
for some fixed compact $K''$. Applying the estimate from the $\mathcal E$ case on $K''$ yields, for every $m$,
\[
\sup_{y\in K''}\big|D^\alpha(\tau_{x_\ell}\phi-\phi)(y)\big|\xrightarrow[\ell\to\infty]{}0
\quad\text{for all }|\alpha|\le m,
\]
and the supports remain in the common compact $K''$. Therefore $\tau_{x_\ell}\phi\to\phi$ in $\mathcal D$.

\bigskip

\textit{Case $X=\mathcal S(\mathbb R^n)$.}
For any $\alpha,\beta$,
\[
x^\alpha D^\beta\big(\tau_{x_\ell}\phi-\phi\big)(x)
=(x^\alpha-(x-x_\ell)^\alpha)D^\beta\phi(x-x_\ell)
+(x-x_\ell)^\alpha\big(D^\beta\phi(x-x_\ell)-D^\beta\phi(x)\big).
\]
The polynomial difference satisfies
\[
|x^\alpha-(x-x_\ell)^\alpha|\le C_\alpha |x_\ell|\,(1+|x|)^{|\alpha|-1},
\]
and all derivatives of $\phi$ are rapidly decreasing; hence the first term tends to $0$ uniformly in $x$.
For the second term, the uniform continuity of $D^\beta\phi$ together with rapid decrease implies that, for every $N$,
\[
\sup_{x\in\mathbb R^n}(1+|x|)^{-N}\,
\big|x^\alpha D^\beta\big(\tau_{x_\ell}\phi-\phi\big)(x)\big|\longrightarrow 0
\qquad (\ell\to\infty).
\]
Thus every Schwartz seminorm goes to $0$, and $\tau_{x_\ell}\phi\to\phi$ in $\mathcal S(\mathbb R^n)$.

\bigskip

Fix $i$ and a multi-index $\alpha$. For any $h\neq 0$,
\[
D^\alpha\Delta_i^{h}\phi
=\frac{D^\alpha\phi(\,\cdot-h e_i)-D^\alpha\phi}{h}.
\]

\medskip

\textit{Case $X=\mathcal E$ (and inside a fixed $\mathcal D_K\subset\mathcal D$).}
Let $K\Subset\mathbb R^n$. By the mean value theorem along $e_i$,
\[
\frac{D^\alpha\phi(x-he_i)-D^\alpha\phi(x)}{h}-D^{\alpha+e_i}\phi(x)
=\int_0^1\big(D^{\alpha+e_i}\phi(x-th e_i)-D^{\alpha+e_i}\phi(x)\big)\,dt.
\]
Hence
\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
\sup_{x\in K}\left|D^\alpha\Delta_i^h\phi(x)-D^{\alpha+e_i}\phi(x)\right|
\le \sup_{0\le t\le 1}\ \sup_{x\in K}
\left|D^{\alpha+e_i}\phi(x-th e_i)-D^{\alpha+e_i}\phi(x)\right|
\longrightarrow 0 \quad \text{as } h\to 0.
$}
\end{center}
For $\mathcal D$, the supports remain in a common compact set for $|h|$ small, so the same uniform estimate yields convergence in $\mathcal D$.

\bigskip

\textit{Case $X=\mathcal S$.}
For any $\alpha,\beta$,
\[
x^\beta\big(D^\alpha\Delta_i^{h}\phi-D^{\alpha+e_i}\phi\big)(x)
= A_{\alpha,\beta,h}(x)+B_{\alpha,\beta,h}(x),
\]
where
\[
A_{\alpha,\beta,h}(x)
=\frac{x^\beta-(x-he_i)^\beta}{h}\,
\]
\[
B_{\alpha,\beta,h}(x)
=(x-he_i)^\beta\!\left(\frac{D^\alpha\phi(x-he_i)-D^\alpha\phi(x)}{h}-D^{\alpha+e_i}\phi(x)\right).
\]
\medskip

For $A_{\alpha,\beta,h}$, expand the polynomial difference:
\[
\frac{x^\beta-(x-he_i)^\beta}{h}
=\sum_{|\gamma|\le |\beta|-1} c_{\beta,\gamma}(h)\,x^\gamma, \qquad |c_{\beta,\gamma}(h)|\le C_\beta,
\]
so that
\[
|A_{\alpha,\beta,h}(x)|
\le C_\beta (1+|x|)^{|\beta|-1}\,|D^\alpha\phi(x-he_i)|.
\]
Since $D^\alpha\phi$ is rapidly decreasing, the right-hand side defines a family bounded in every Schwartz seminorm and tends to $0$ as $h\to0$.

\medskip

For $B_{\alpha,\beta,h}$, the integral remainder form of the mean value theorem gives
\[
\frac{D^\alpha\phi(x-he_i)-D^\alpha\phi(x)}{h}-D^{\alpha+e_i}\phi(x)
=\int_0^1\!\big(D^{\alpha+e_i}\phi(x-th e_i)-D^{\alpha+e_i}\phi(x)\big)\,dt,
\]
whence
\[
|B_{\alpha,\beta,h}(x)|
\le (1+|x|)^{|\beta|}\int_0^1
\big|D^{\alpha+e_i}\phi(x-th e_i)-D^{\alpha+e_i}\phi(x)\big|\,dt.
\]
The integrand tends to $0$ uniformly in $x$ by the uniform continuity of $D^{\alpha+e_i}\phi$, and the polynomial factor is absorbed by the rapid decay of the derivatives of $\phi$. Consequently, for every pair $(\alpha,\beta)$,
\[
q_{\alpha,\beta}(\Delta_i^{h}\phi-D_i\phi)\longrightarrow 0 \qquad (h\to0).
\]

\bigskip

This proves $\Delta_i^{h}\phi\to D_i\phi$ in $\mathcal E$, $\mathcal D$, and $\mathcal S$.

\bigskip
Let $\phi(x)=e^{-|x|^2}\in\mathcal S(\mathbb R^n)$. Then, for any translation vector $x_\ell\to0$,
\[
(\tau_{x_\ell}\phi)(y)=e^{-|y-x_\ell|^2}
\longrightarrow e^{-|y|^2}=\phi(y)
\]
together with all derivatives, because every derivative of $\phi$ is a polynomial times $e^{-|y|^2}$,
which is uniformly continuous and rapidly decreasing. Hence each Schwartz seminorm
\[
q_{\alpha,\beta}(\tau_{x_\ell}\phi-\phi)
=\sup_{y\in\mathbb R^n}|\,y^\alpha D^\beta(\tau_{x_\ell}\phi-\phi)(y)\,|
\]
tends to $0$ as $\ell\to\infty$.

\medskip

For the difference quotient,
\[
\Delta_i^{h}\phi(x)=\frac{\phi(x-h e_i)-\phi(x)}{h},
\]
Taylor's theorem gives
\[
\phi(x-h e_i)=\phi(x)-h\,D_i\phi(x)+\tfrac{h^2}{2}D_i^2\phi(x-\theta h e_i),
\qquad 0<\theta<1,
\]
so that
\[
\Delta_i^{h}\phi(x)-D_i\phi(x)
=\tfrac{h}{2}\,D_i^2\phi(x-\theta h e_i)\to0
\]
uniformly with all derivatives. Therefore $\Delta_i^{h}\phi\to D_i\phi$ in $\mathcal S(\mathbb R^n)$.

\bigskip
\bigskip
Let $\phi\in\mathcal D(\mathbb R)$ be compactly supported in $[-1,1]$. For small $|h|$,
\[
\operatorname{supp}(\phi(\cdot-h))\subset[-1+h,1+h]\subset[-2,2].
\]
Hence every difference quotient
\[
\Delta^{h}\phi(x)=\frac{\phi(x-h)-\phi(x)}{h}
\]
has support contained in a fixed compact interval, and all derivatives converge uniformly:
\[
\sup_{x\in[-2,2]}|D^m(\Delta^{h}\phi-\phi')(x)|\longrightarrow0
\quad\text{as }h\to0.
\]
Thus $\Delta^{h}\phi\to\phi'$ in the $\mathcal D$-topology.

\bigskip
```

## CP-II-0415

- chapter line: 7233

```tex
\label{prob:cp-ii-0415}
On $C^\infty(\mathbb R^n)$, the seminorms
	$p_{K,m}(f)=\sup_{x\in K,\,|\alpha|\le m}|D^\alpha f(x)|$ (compact $K$, $m\in\mathbb N$)
	generate the usual Fréchet topology. Convergence $f_k\to f$ means
	$p_{K,m}(f_k-f)\to0$ for all $K,m$ (uniform convergence of all derivatives on compacts).

	\bigskip
```

## CP-II-0424

- chapter line: 7243

```tex
\label{prob:cp-ii-0424}
s.

\par\noindent\textbullet\quad For $1\le p\le\infty$, the \textbf{weak topology} on $L^{p}(\Omega)$ is
		$\sigma(L^{p},L^{p'})$: the coarsest topology making all linear functionals
		\[
		T_h(f)\;:=\;\int_{\Omega} f\,h\,d\mu
		\qquad (\,h\in L^{p'}(\Omega)\,)
		\]
		continuous.

		\vspace{0.25em}
		A sequence $f_j$ converges weakly to $f$ iff
		\[
		\int_{\Omega} f_j\,h\,d\mu \;\longrightarrow\; \int_{\Omega} f\,h\,d\mu
		\qquad \text{for every } h\in L^{p'}.
		\]

	\medskip
	\noindent\emph{Reflexivity.}
	If $1<p<\infty$, $L^{p}$ is reflexive; hence bounded sets are relatively weakly compact
	(Banach--Alaoglu + Eberlein--\v{S}mulian). For $p=1$ or $p=\infty$ this fails in general.

	\medskip
	\noindent\emph{Indicators and density.}
	Let $\mathcal S$ denote the linear span of indicators of bounded measurable sets:
	\[
	\mathcal S := \left\{\, g=\sum_{k=1}^{m} a_k\,\mathbf 1_{E_k}\ :\ m<\infty,\ a_k\in\mathbb R,\ \mu(E_k)<\infty \,\right\}.
	\]
	Then $\mathcal S$ is exactly the class of bounded simple functions with bounded support,
	and for $1<p<\infty$ one has the density
	\[
	\overline{\mathcal S}^{\,L^{p'}} = L^{p'}(\Omega).
	\]

	\noindent\emph{Proof sketch of density.}
	Given $h\in L^{p'}$, define the truncations $h^N := h\,\mathbf 1_{\{|h|\le N\}\cap B_N}$,
	where $B_N$ is a set of finite measure increasing to $\Omega$ (e.g.\ balls of radius $N$ if $\Omega=\mathbb R^n$).
	Then $\|h-h^N\|_{p'}\to0$ by dominated convergence and monotone convergence.
	Each bounded, finitely supported $h^N$ is approximated in $L^{p'}$ by simple functions via range partitioning:
	$h^N=\lim_{m\to\infty}\sum_\ell c_{\ell,m}\,\mathbf 1_{E_{\ell,m}}$.
	Hence $\mathcal S$ is dense.

	\medskip
	\noindent\emph{Consequences.}
	If $(f_j)$ is bounded in $L^{p}$ and $\int (f_j-f)\,\mathbf 1_E\to0$ for every bounded $E$,
	then by linearity the convergence holds for all $g\in\mathcal S$; by density and H\"older,
	\[
	\Big|\!\int (f_j-f)h\Big|
	\le \Big|\!\int (f_j-f)g\Big| + \|f_j-f\|_{p}\,\|h-g\|_{p'} \;\xrightarrow[j\to\infty]{}\; \|f_j-f\|_{p}\,\|h-g\|_{p'}.
	\]
	Let $g\to h$ in $L^{p'}$ to conclude $\int (f_j-f)h\to0$ for all $h\in L^{p'}$, i.e.\ $f_j\rightharpoonup f$.

	\bigskip
```

## CP-II-0426

- chapter line: 7300

```tex
\label{prob:cp-ii-0426}
\par\noindent\textbullet\quad Every compactly supported smooth function is Schwartz, so
	$\mathcal{D}(\mathbb{R}^n)\subset\mathcal{S}(\mathbb{R}^n)$.
```

## CP-II-0434

- chapter line: 7306

```tex
\label{prob:cp-ii-0434}
\par\noindent (ii)\quad Using the definition of compactness, show that $X$ is not compact.
```

## CP-II-0441

- chapter line: 7311

```tex
\label{prob:cp-ii-0441}
\par\noindent\textbullet\quad \textbf{Completeness with $\|\cdot\|_{1}$.}
	Since $\|\cdot\|_{1}$ is not a norm on the pointwise space $R([0,1])$, completeness as a normed space
	is not applicable. Passing to equivalence classes a.e.\ gives $L^{1}$, which is complete.
```

## CP-II-0443

- chapter line: 7318

```tex
\label{prob:cp-ii-0443}
Let $f(x) = \sin(x)$ on $E=[0,100]$.
		$E$ is compact, $f$ is continuous, hence uniformly continuous.
```

## CP-II-0445

- chapter line: 7324

```tex
\label{prob:cp-ii-0445}
\par\noindent *d)\quad By considering a suitable sequence of functions $f$, or otherwise,
	deduce that there exists no constant $C$, independent of $u$, such that
	the estimate
	\[
	\sup_{S_T} (|u|+|u_t|)
	\le C \sup_{\Sigma_0} (|u|+|u_t|)
	\]
	holds for all solutions $u\in C^2(S_T)$ of the wave equation which vanish
	for large $|x|$.

\par\medskip\noindent\textbf{\textbf{Goal.}}\quad
Show that if $u(r,t) = v(r,t)/r$ is radial, then $u$ solves
$-u_{tt} + \Delta u = 0$ on $\mathbb{R}^3_*\times(-T,T)$ if and only if
$v$ solves the one-dimensional wave equation
$-v_{tt}+v_{rr}=0$ on $(0,\infty)\times(-T,T)$.

\par\medskip\noindent\textbf{\textbf{Computation.}}\quad
Let $u(r,t) = v(r,t)/r$. Then
\[
u_r = \frac{v_r}{r} - \frac{v}{r^2},
\qquad
u_{rr}
= \frac{v_{rr}}{r} - \frac{2v_r}{r^2} + \frac{2v}{r^3},
\qquad
u_{tt} = \frac{v_{tt}}{r}.
\]
Using the radial Laplacian,
\[
\Delta u
= u_{rr} + \frac{2}{r}u_r
= \left(\frac{v_{rr}}{r} - \frac{2v_r}{r^2} + \frac{2v}{r^3}\right)
+ \frac{2}{r}\left(\frac{v_r}{r} - \frac{v}{r^2}\right)
= \frac{v_{rr}}{r}.
\]
Thus the wave equation
\[
-u_{tt} + \Delta u = 0
\]
becomes
\[
-\frac{v_{tt}}{r} + \frac{v_{rr}}{r} = 0
\quad\Longleftrightarrow\quad
-v_{tt} + v_{rr} = 0,
\]
for $r>0$. This proves the equivalence.

\par\medskip\noindent\textbf{\textbf{Goal.}}\quad
Use d'Alembert's formula for the one-dimensional wave equation to
construct radial solutions in $\mathbb{R}^3$.

\par\medskip\noindent\textbf{\textbf{D'Alembert solution.}}\quad
For the one-dimensional wave equation $-v_{tt}+v_{rr}=0$ on $\mathbb{R}$,
the general solution is
\[
v(r,t) = f(r+t) + g(r-t),
\]
for some functions $f,g$.

\par\medskip\noindent\textbf{\textbf{Conclusion.}}\quad
If $f,g\in C_c^2(\mathbb{R})$, set
\[
v(r,t) = f(r+t) + g(r-t),
\qquad
u(r,t) = \frac{v(r,t)}{r}
= \frac{f(r+t)}{r} + \frac{g(r-t)}{r}.
\]
Then $v$ solves the one-dimensional wave equation, and by part~(a),
$u$ solves the three-dimensional wave equation on $S_{*,T}$.

Since $f,g$ are compactly supported, there exists $R>0$ such that
$f(s)=g(s)=0$ whenever $|s|\ge R$. For fixed $t\in(-T,T)$ and for $r$
sufficiently large, both $r+t$ and $r-t$ lie outside the supports of
$f$ and $g$, so $u(r,t)=0$. Hence $u$ vanishes for large $|x|$.

\par\medskip\noindent\textbf{\textbf{Goal.}}\quad
Assume $f\in C_c^3(\mathbb{R})$ is odd ($f(-s)=-f(s)$). Show that
\[
u(r,t) := \frac{f(r+t)+f(r-t)}{2r}
\]
extends to a $C^2$ solution on $S_T$ and satisfies $u(0,t)=f'(t)$.

\par\medskip\noindent\textbf{\textbf{Construction.}}\quad
Define
\[
v(r,t) := \frac12\bigl(f(r+t)+f(r-t)\bigr).
\]
Then $v\in C^3$ and solves $-v_{tt}+v_{rr}=0$ on $(0,\infty)\times(-T,T)$.
By part~(a), $u(r,t)=v(r,t)/r$ solves the wave equation on
$\mathbb{R}^3_*\times(-T,T)$.

Because $f$ is odd,
\[
v(0,t)
= \frac12\bigl(f(t)+f(-t)\bigr)
= \frac12\bigl(f(t)-f(t)\bigr)
= 0.
\]
Thus $v(r,t)$ vanishes at $r=0$ for each $t$.

Differentiating,
\[
v_r(r,t) = \frac12\bigl(f'(r+t)+f'(r-t)\bigr),
\]
so
\[
v_r(0,t)
= \frac12\bigl(f'(t)+f'(-t)\bigr).
\]
Since $f$ is odd, $f'$ is even, hence $f'(-t)=f'(t)$ and
\[
v_r(0,t) = f'(t).
\]

\par\medskip\noindent\textbf{\textbf{Extension and regularity.}}\quad
Near $r=0$ we have the Taylor expansion
\[
v(r,t) = v_r(0,t)\,r + O(r^3) = f'(t)\,r + O(r^3),
\]
so
\[
u(r,t) = \frac{v(r,t)}{r} = f'(t) + O(r^2),
\]
which has a finite limit as $r\to0$. Define
\[
u(0,t) := f'(t).
\]
This defines a $C^2$ function $u$ on $S_T$ which coincides with the
radial solution for $r>0$ and therefore solves the wave equation on all
of $S_T$.

\par\medskip\noindent\textbf{\textbf{Claim.}}\quad
There is no constant $C>0$ such that
\[
\sup_{S_T} (|u|+|u_t|)
\le C \sup_{\Sigma_0} (|u|+|u_t|),
\]
for all solutions $u\in C^2(S_T)$ of the wave equation that vanish for
large $|x|$.

\par\medskip\noindent\textbf{\textbf{Reduction to a one-dimensional inequality.}}\quad
For solutions of the form in part~(c),
\[
u(r,t) = \frac{f(r+t)+f(r-t)}{2r}
\]
with $f\in C_c^3(\mathbb{R})$ odd, we have
\[
u(0,t) = f'(t).
\]
At $t=0$,
\[
u(r,0) = \frac{f(r)+f(r)}{2r} = \frac{f(r)}{r},
\qquad
u_t(r,0) = 0,
\]
since $f'$ is even. Therefore,
\[
\sup_{\Sigma_0} (|u|+|u_t|)
= \sup_{r>0}\left|\frac{f(r)}{r}\right|.
\]
On the other hand,
\[
\sup_{S_T} (|u|+|u_t|)
\ge \sup_{t\in(-T,T)} |u(0,t)|
= \sup_{t\in(-T,T)} |f'(t)|.
\]

If the estimate above held for all such $u$, then for all odd
$f\in C_c^3(\mathbb{R})$ we would have
\[
\sup_{t\in(-T,T)} |f'(t)|
\le C \sup_{r>0}\left|\frac{f(r)}{r}\right|.
\tag{$\dagger$}
\]

\par\medskip\noindent\textbf{\textbf{Construction of a contradicting sequence.}}\quad
Fix a nonzero $\psi\in C_c^3(\mathbb{R})$ supported in $(-1,1)$, and
define for $R>1$:
\[
f_R(s) := \psi(s-R) - \psi(-s-R).
\]
Then $f_R\in C_c^3(\mathbb{R})$ is odd (one checks $f_R(-s)=-f_R(s)$),
and its support is contained in two disjoint intervals located near
$s\approx \pm R$.

Since $f_R'$ is just a translate of $\psi'$, we have
\[
\sup_{s\in\mathbb{R}} |f_R'(s)|
= \sup_{s\in\mathbb{R}} |\psi'(s)| =: M > 0,
\]
independent of $R$.

However, for $s$ in the support of $f_R$ we have $|s|\ge R-1$, so
\[
\left|\frac{f_R(s)}{s}\right|
\le \frac{\sup_{|y|\le 1}|\psi(y)|}{R-1},
\]
and hence
\[
\sup_{r>0}\left|\frac{f_R(r)}{r}\right|
\le \frac{C_0}{R-1},
\]
for some constant $C_0$ independent of $R$.

\par\medskip\noindent\textbf{\textbf{Contradiction.}}\quad
If $(\dagger)$ held for all odd $f$, it would hold for $f_R$:
\[
M \le C \sup_{r>0}\left|\frac{f_R(r)}{r}\right|
\le C\,\frac{C_0}{R-1}.
\]
Letting $R\to\infty$ forces the right-hand side to $0$, while $M>0$ is
fixed. This is impossible, and therefore no such constant $C$ can exist.

\par\medskip\noindent\textbf{\textbf{Conclusion.}}\quad
The wave equation in three dimensions does not satisfy a global
maximum-principle-type estimate of the form above; the size of the
solution at later times cannot be controlled solely by the supremum of
its initial data.
```

## CP-II-0453

- chapter line: 7545

```tex
\label{prob:cp-ii-0453}
Extra Examples and Sequential Spaces

In the co-countable topology on an uncountable set $X$, a sequence converges iff it is eventually constant.
	Hence every subset $A\subseteq X$ is sequentially closed, while the closed sets are exactly the countable subsets and $X$ itself.

		\par\noindent\textbullet\quad $X=\mathbb{R}$, $A=\mathbb{R}\setminus\mathbb{Q}$: sequentially closed, not closed.
		\par\noindent\textbullet\quad $X=\mathbb{R}$, $A=(0,1)\cup\{\pi\}$: sequentially closed, not closed.
		\par\noindent\textbullet\quad $X$ uncountable, $A=X\setminus C$ with nonempty countable $C$: sequentially closed, not closed.
		\par\noindent\textbullet\quad Any countably infinite $C\subset X$ is closed; its sequential closure equals $C$.

	\emph{Non-example.} If $X$ is finite with the co-countable topology, then $X$ is discrete; sequentially closed sets are exactly the closed sets.

	In every second countable space (hence first countable), $A$ is sequentially closed iff $A$ is closed.

		\par\noindent\textbullet\quad $\mathbb{R}^n$: $(0,1)$ is not sequentially closed (since $1/n\to0\notin(0,1)$); $[0,1]$ is sequentially closed (closed).
		\par\noindent\textbullet\quad Any metric space (Polish spaces, manifolds, graphs with path metric, metric CW-complexes): same equivalence.
		\par\noindent\textbullet\quad Subspaces of second countable spaces: e.g.\ $S^1\subset\mathbb{R}^2$. The set $S^1\setminus\{1\}$ is not sequentially closed (points approach $1$).
		\par\noindent\textbullet\quad Countable products of second countable spaces (e.g.\ $\mathbb{R}^{\mathbb N}$ with product topology): still second countable; sequentially closed $\Leftrightarrow$ closed.

	\emph{Non-examples.} For uncountable $I$, $\mathbb{R}^I$ (product topology) is not second countable; there are subsets whose topological closure strictly contains their sequential closure. Likewise, $\mathbb{R}$ with the co-countable topology is not first/second countable; every set is sequentially closed but many are not closed.

	\begin{definition}
		A topological space $X$ is \emph{sequential} if for all $A\subseteq X$,
		\[
		\overline{A}=\operatorname{scl}(A),
		\]
		i.e.\ $A$ is closed iff $A$ is sequentially closed.
	\end{definition}

		\par\noindent\textbullet\quad Every first countable space (in particular, every metric or second countable space) is sequential.
		\par\noindent\textbullet\quad The Arens--Fort space is sequential but not first countable.
		\par\noindent\textbullet\quad Quotients of metric spaces are sequential.
		\par\noindent\textbullet\quad Products of sequential spaces need not be sequential.

		\par\noindent\textbullet\quad The Tikhonoff cube $[0,1]^I$ with $I$ uncountable is not sequential.
		\par\noindent\textbullet\quad The Stone--\v{C}ech compactification $\beta\mathbb{N}$ is not sequential.
		\par\noindent\textbullet\quad The Fortissimo space is not sequential (fails countable tightness).
		\par\noindent\textbullet\quad $\mathbb{R}$ with the co-countable topology is not sequential (every set is sequentially closed, many are not closed).

	\begin{definition}
		Let $f:X\to Y$ be a map between topological spaces.

			\par\noindent\textbullet\quad $f$ is \emph{sequentially continuous at $x\in X$} if for every sequence $(x_n)$ with $x_n\to x$ in $X$ we have $f(x_n)\to f(x)$ in $Y$.
			\par\noindent\textbullet\quad $f$ is \emph{continuous} if $f^{-1}(U)$ is open in $X$ for every open $U\subseteq Y$.

	\end{definition}

	\begin{proposition}
		If $X$ is a sequential space (e.g.\ first countable, metric, or second countable), then $f:X\to Y$ is continuous iff it is sequentially continuous.
	\end{proposition}
```

## CP-II-0458

- chapter line: 7599

```tex
\label{prob:cp-ii-0458}
(Degree mod $2$ and surjectivity)

Let $X$ be a compact manifold without boundary and $Y$ a connected manifold with the same dimension as $X$.

	\par\noindent \textbf{(i)}\quad Suppose that $f : X \to Y$ has $\deg_2(f) \neq 0$. Prove that $f$ is onto.
	\par\noindent \textbf{(ii)}\quad If $Y$ is not compact, prove that $\deg_2(f) = 0$ for all smooth maps $f : X \to Y$.

Let $X$ be a compact smooth $n$-manifold without boundary and let $Y$ be a connected smooth $n$-manifold with $\dim X=\dim Y=n$.
Let $f:X\to Y$ be smooth.

\medskip
\noindent\textbf{Regular values and finite fibres.}
A point $y\in Y$ is a \emph{regular value} of $f$ if for every $x\in f^{-1}(y)$ the differential
\[
df_x:T_xX\longrightarrow T_yY
\]
is surjective. Since $\dim X=\dim Y=n$, surjectivity is equivalent to $df_x$ being an isomorphism; equivalently $\det(df_x)\neq 0$ in local coordinates.
By Sard's theorem, regular values exist and form a dense subset of $Y$.
If $y$ is a regular value, then $f^{-1}(y)$ is a $0$-dimensional submanifold of $X$, hence a discrete subset of $X$.
Because $X$ is compact, every discrete subset is finite, so
\[
f^{-1}(y)=\{x_1,\dots,x_k\}\quad\text{for some }k<\infty.
\]

\medskip
\noindent\textbf{Definition of $\deg_2(f)$.}
For any regular value $y\in Y$, define the \emph{degree mod $2$} of $f$ by
\[
\deg_2(f)\;:=\;|f^{-1}(y)|\pmod 2\ \in\ \mathbb Z/2.
\]
Thus $\deg_2(f)=0$ means that $|f^{-1}(y)|$ is even, and $\deg_2(f)=1$ means that $|f^{-1}(y)|$ is odd.
(If $f^{-1}(y)=\varnothing$, then $y$ is automatically a regular value and the above gives $\deg_2(f)=0$.)

\medskip
\noindent\textbf{Why this is well-defined (independence of $y$).}
We show that $|f^{-1}(y)|\pmod 2$ does not depend on the chosen regular value $y$.
Let $y_0,y_1\in Y$ be regular values. Since $Y$ is connected, choose a smooth path $\gamma:[0,1]\to Y$ with $\gamma(0)=y_0$ and $\gamma(1)=y_1$.
By a small perturbation (generic choice), we may assume $\gamma$ is transverse to $f$.
Consider the subset
\[
\widetilde M \;:=\;\{(x,t)\in X\times[0,1]\;:\; f(x)=\gamma(t)\}.
\]
Define $H:X\times[0,1]\to Y\times Y$ by $H(x,t)=(f(x),\gamma(t))$ and let $\Delta\subset Y\times Y$ be the diagonal.
Then $\widetilde M=H^{-1}(\Delta)$, and transversality of $\gamma$ to $f$ implies $H$ is transverse to $\Delta$.
Hence $\widetilde M$ is a smooth submanifold of $X\times[0,1]$ of dimension
\[
\dim(X\times[0,1])-\codim(\Delta)=(n+1)-n=1,
\]
so $\widetilde M$ is a compact smooth $1$-manifold (compactness because $X\times[0,1]$ is compact).

\medskip
\noindent\textbf{Boundary computation.}
A point $(x,t)\in \widetilde M$ lies in the boundary of $X\times[0,1]$ iff $t\in\{0,1\}$, so
\[
\partial \widetilde M \;=\;\widetilde M\cap \bigl(X\times\{0,1\}\bigr)
\;\cong\; f^{-1}(y_0)\;\sqcup\; f^{-1}(y_1).
\]
Therefore
\[
|\partial \widetilde M|=|f^{-1}(y_0)|+|f^{-1}(y_1)|.
\]

\medskip
\noindent\textbf{Lemma (boundary points of a compact $1$-manifold come in pairs).}
Every compact smooth $1$-manifold is a finite disjoint union of circles $S^1$ and closed intervals $[0,1]$.
Each circle has empty boundary, and each interval has exactly two boundary points. Hence every compact $1$-manifold has an even number of boundary points:
\[
|\partial \widetilde M|\equiv 0 \pmod 2.
\]

\medskip
\noindent\textbf{Conclusion (well-definedness).}
Combining the two displays above gives
\[
|f^{-1}(y_0)|+|f^{-1}(y_1)|\equiv 0 \pmod 2,
\]
hence
\[
|f^{-1}(y_0)|\equiv |f^{-1}(y_1)|\pmod 2.
\]
Thus $\deg_2(f)$ is independent of the choice of regular value $y$ and is therefore well-defined.

\medskip
\noindent\textbf{Relation to the usual integer degree (oriented case).}
If $X$ and $Y$ are oriented, one can define the usual degree $\deg(f)\in\mathbb Z$ by
\[
\deg(f)=\sum_{x\in f^{-1}(y)} \operatorname{sign}\bigl(\det(df_x)\bigr),
\]
for any regular value $y$. Reducing this identity modulo $2$ gives
\[
\deg_2(f)\equiv \deg(f)\pmod 2,
\]
since $\operatorname{sign}(\det(df_x))\in\{\pm 1\}\equiv 1 \pmod 2$.
In particular, $\deg_2$ is the ``orientation-free'' version of degree: it is defined without choosing orientations.

	\par\noindent \textbf{(i)}\quad
	Assume for contradiction that $f$ is not onto. Then there exists $y\in Y\setminus f(X)$. For this $y$ we have
	$f^{-1}(y)=\varnothing$. In particular $y$ is a regular value (vacuously), and therefore
	\[
	\deg_2(f)\equiv |f^{-1}(y)|\equiv 0 \pmod 2,
	\]
	contradicting the assumption $\deg_2(f)\neq 0$. Hence $f$ must be onto.

	\par\noindent \textbf{(ii)}\quad
	Since $X$ is compact and $f$ is continuous, the image $f(X)\subset Y$ is compact. If $Y$ is not compact then
	$f(X)\neq Y$, so choose $y\in Y\setminus f(X)$. Then $f^{-1}(y)=\varnothing$, hence (as above) $y$ is a regular value and
	\[
	\deg_2(f)\equiv |f^{-1}(y)|\equiv 0 \pmod 2.
	\]
	Thus $\deg_2(f)=0$ for every smooth map $f:X\to Y$ whenever $Y$ is non-compact.

	\par\noindent\textbullet\quad The antipodal map $A:S^n\to S^n$, $A(x)=-x$, satisfies $|A^{-1}(y)|=1$ for every $y$, hence $\deg_2(A)=1$, so $A$ is onto.
	\par\noindent\textbullet\quad If $Y$ is non-compact and $X$ is compact, then every smooth $f:X\to Y$ has $\deg_2(f)=0$ by part \textbf{(ii)}.
```

## CP-II-0460

- chapter line: 7716

```tex
\label{prob:cp-ii-0460}
{Runge approximation on a punctured domain}{runge-annulus}
	Let $B_r(z)$ be the open disc of radius $r$ about $z\in\mathbb C$, and set
	$U:=B_2(1)\setminus B_1(0)$. Suppose $f$ is holomorphic on $U$.

		\par\noindent (i)\quad Show there exists a sequence converging to $f$ uniformly on compact subsets of $U$.
		\par\noindent (ii)\quad Must there be a sequence of polynomials converging to $f$ uniformly on $U$?
		\par\noindent (iii)\quad If, moreover, $f$ is holomorphic on an open set containing $\overline U$, must there be a sequence
		of polynomials converging to $f$ uniformly on $U$?
```

## CP-II-0467

- chapter line: 7728

```tex
\label{prob:cp-ii-0467}
Let $E\subset\mathbb{R}^n$ be compact and $f:E\to\mathbb{R}^m$ continuous.

\par\noindent\textbullet\quad $f(E)$ is bounded. \textit{Proof.} Each component $f^j$ attains its max/min on $E$.
\par\noindent\textbullet\quad $f(E)$ is closed, hence compact. \textit{Proof.} Use sequential closedness via compactness of $E$.
\par\noindent\textbullet\quad If $E$ is merely closed, $f(E)$ need not be closed; e.g.\ $f(x)=\arctan x$ on $E=\mathbb{R}$.
```

## CP-II-0468

- chapter line: 7737

```tex
\label{prob:cp-ii-0468}
\par\noindent\textbullet\quad On disjoint compact sets $K_1,K_2\subset[0,1]$ there exists $f\in C([0,1])$ with
	$f|_{K_1}\equiv0$ and $f|_{K_2}\equiv1$ (Urysohn on $[0,1]$).
	By Weierstrass, there are polynomials $p_n\to f$ uniformly on $[0,1]$.
```
