# Part II missing-solution batch 10

- problems: **20**
- IDs: CP-II-0149, CP-II-0150, CP-II-0151, CP-II-0152, CP-II-0154, CP-II-0155, CP-II-0157, CP-II-0158, CP-II-0161, CP-II-0164, CP-II-0165, CP-II-0167, CP-II-0170, CP-II-0173, CP-II-0175, CP-II-0176, CP-II-0178, CP-II-0179, CP-II-0186, CP-II-0188

## CP-II-0149

- chapter line: 13857

```tex
\label{prob:cp-ii-0149}
Let $X=\mathbb{R}$ with the co-countable topology and let $Y=\{0,1\}$ with the discrete topology. Define
		\[
		f(x)=\begin{cases}
			0,& x\in \mathbb{Q},\\
			1,& x\in \mathbb{R}\setminus \mathbb{Q}.
		\end{cases}
		\]
		In $X$, a sequence converges to $x$ iff it is eventually constant equal to $x$. Hence for any $x_n\to x$,
		the sequence $f(x_n)$ is eventually constant equal to $f(x)$, so $f$ is sequentially continuous.
		However, $\{0\}\subset Y$ is open while $f^{-1}(\{0\})=\mathbb{Q}$ is not open in the co-countable topology.
		Thus $f$ is not continuous.
```

## CP-II-0150

- chapter line: 13872

```tex
\label{prob:cp-ii-0150}
\par\noindent\textbullet\quad Suppose $u(x,t) = \frac{1}{r}v(r,t)$ for some function $v$.
	Show that $u$ solves the wave equation on $\mathbb{R}^3_*\times(-T,T)$
	if and only if $v$ satisfies the one-dimensional wave equation
	\[
	-\,\frac{\partial^2 v}{\partial t^2}(r,t)
	+ \frac{\partial^2 v}{\partial r^2}(r,t)
	= 0
	\quad\text{on } (0,\infty)\times(-T,T).
	\]
```

## CP-II-0151

- chapter line: 13885

```tex
\label{prob:cp-ii-0151}
\par\noindent\textbullet\quad \textbf{Norming functional.} For each $x\in X$, $x\neq0$, there is $\Lambda\in X'$ with
		$\|\Lambda\|=1$ and $\Lambda(x)=\|x\|$.
```

## CP-II-0152

- chapter line: 13891

```tex
\label{prob:cp-ii-0152}
— Moving points vs.\ uniform convergence on $[a,b]$

Let $(f_n)$ be a sequence of real-valued continuous functions on the compact interval $[a,b]$,
and suppose $f_n \to f$ pointwise with $f$ continuous on $[a,b]$.

	\par\noindent (i)\quad If $f_n \to f$ uniformly and $x_n \to x$ in $[a,b]$, prove that $f_n(x_n)\to f(x)$.
	\par\noindent (ii)\quad Conversely, if $f_n \not\to f$ uniformly on $[a,b]$, prove that there exist $x_n\to x$ in $[a,b]$
	such that $f_n(x_n)\not\to f(x)$.

We collect the tools used in the proofs.

\begin{definition}[Uniform convergence]
	A sequence $(f_n)$ of functions on $E$ converges uniformly to $f$ if
	\[
	\sup_{y\in E} |f_n(y)-f(y)| \xrightarrow[n\to\infty]{} 0.
	\]
\end{definition}

\begin{lemma}[Uniform convergence controls moving points]
	Let $E$ be a metric space. If $f_n\to f$ uniformly on $E$ and $x_n\to x$ in $E$ with $f$ continuous at $x$, then
	\[
	|f_n(x_n)-f(x)| \le \underbrace{|f_n(x_n)-f(x_n)|}_{\le \sup_E |f_n-f|} + \underbrace{|f(x_n)-f(x)|}_{\to 0}
	\longrightarrow 0.
	\]
\end{lemma}

\begin{lemma}[Compactness selection]
	If $(x_n)$ is a sequence in a compact set $K$, then there exists a convergent subsequence $x_{n_k}\to x\in K$.
\end{lemma}

\begin{lemma}[Witness for failure of uniform convergence]
	Let $K$ be compact. If $f_n \not\to f$ uniformly on $K$, then there exists $\varepsilon>0$, a strictly increasing $n_k$,
	and points $x_k\in K$ such that $|f_{n_k}(x_k)-f(x_k)|\ge \varepsilon$ for all $k$.
\end{lemma}

\begin{remark}[Equivalence on compact sets]
	Assume each $f_n$ is continuous on $[a,b]$ and $f$ is continuous. Then the following are equivalent:

		\par\noindent\textbullet\quad $f_n \to f$ uniformly on $[a,b]$.
		\par\noindent\textbullet\quad For every sequence $x_n\to x$ in $[a,b]$, we have $f_n(x_n)\to f(x)$.

	The direction (1)$\Rightarrow$(2) follows from uniform convergence together with continuity of $f$. The converse follows from (ii) below.
\end{remark}

Let $x_n\to x$ in $[a,b]$. By uniform convergence and continuity of $f$,
\[
|f_n(x_n)-f(x)| \le \sup_{y\in[a,b]}|f_n(y)-f(y)| + |f(x_n)-f(x)| \xrightarrow[n\to\infty]{} 0,
\]
because the first term $\to 0$ by uniform convergence and the second by continuity of $f$ at $x$.

Assume $f_n \not\to f$ uniformly on $[a,b]$. By the negation of uniform convergence there exist $\varepsilon>0$, indices $n_k\uparrow\infty$,
and points $x_k\in[a,b]$ such that
\[
|f_{n_k}(x_k)-f(x_k)| \ge \varepsilon \qquad \text{for all } k.
\]
By compactness of $[a,b]$, pass to a subsequence (not relabeled) with $x_k\to x\in[a,b]$.
Since $f$ is continuous, $f(x_k)\to f(x)$. Then
\[
\liminf_{k\to\infty} |f_{n_k}(x_k)-f(x)|
\;\ge\; \liminf_{k\to\infty}\Big(|f_{n_k}(x_k)-f(x_k)| - |f(x_k)-f(x)|\Big)
\;\ge\; \varepsilon - 0 \;=\; \varepsilon.
\]
Hence $f_{n_k}(x_k)\not\to f(x)$. Defining a sequence $(x_n)$ by $x_{n_k}=x_k$ and setting $x_n=x$ for other $n$
gives $x_n\to x$ with $f_n(x_n)\not\to f(x)$.

Let
\[
\phi(t) = \max\{1-|t|,\,0\}, \qquad t\in\mathbb{R}.
\]
Define $f_n:[0,1]\to\mathbb{R}$ by
\[
f_n(x) = \phi(nx-1).
\]
Then each $f_n$ is continuous, $f_n(x)\to 0$ for every $x\in[0,1]$ (so $f\equiv 0$), but
\[
\sup_{x\in[0,1]}|f_n(x)-f(x)|=\sup_{x\in[0,1]} f_n(x)=1 \quad \text{for all } n,
\]
so the convergence is \emph{not} uniform. Taking $x_n=1/n\to 0$ yields $f_n(x_n)=1\nrightarrow 0=f(0)$,
which witnesses the conclusion of (ii).

On $[0,1]$, let $f_n(x)=x^n$ and $f\equiv 0$. Then for any $\delta\in(0,1)$, $f_n\to f$ uniformly on $[0,1-\delta]$ with
\[
\sup_{x\in[0,1-\delta]}|f_n(x)-f(x)| \le (1-\delta)^n \to 0.
\]
Thus for any $x_n\to x\in[0,1-\delta]$, the moving-point estimate above gives $f_n(x_n)\to f(x)=0$.
(Contrast with the boundary case $x_n\to 1$, where uniformity fails on $[0,1]$ and moving-point convergence can fail.)

Let $f_n(x)=x e^{-n x}$ on $[0,\infty)$. Then
\[
\sup_{x\ge 0} |f_n(x)| = \frac{1}{n e}\to 0,
\]
so $f_n\to 0$ uniformly. Hence for any $x_n\to x\ge 0$ we have $f_n(x_n)\to 0$.

	\par\noindent\textbullet\quad The compactness of $[a,b]$ is crucial in (ii) to extract a convergent subsequence $(x_{n_k})$.
	\par\noindent\textbullet\quad The continuity of $f$ at the limit point is used twice: in the moving-point estimate and to conclude $f(x_k)\to f(x)$ in (ii).
	\par\noindent\textbullet\quad On compact domains, the equivalence above provides a practical test for uniform convergence: \emph{check moving points}.
```

## CP-II-0154

- chapter line: 13991

```tex
\label{prob:cp-ii-0154}
\par\noindent\textbullet\quad By contrast, for $1<p<\infty$, $L^p$ is reflexive and every bounded sequence
		admits a weakly convergent subsequence (Banach–Alaoglu + reflexivity).
```

## CP-II-0155

- chapter line: 13997

```tex
\label{prob:cp-ii-0155}
Consider the series $\sum_{n=1}^\infty (x-n)^{-2}$ for $x\in X:=\mathbb{R}\setminus\mathbb{N}$.

		\par\noindent\textbullet\quad Show that the series converges pointwise on $X$.
		\par\noindent\textbullet\quad Does the series converge uniformly on $X$?
		\par\noindent\textbullet\quad Show that the sum $f(x)=\sum_{n=1}^\infty (x-n)^{-2}$ is continuous on $X$.


	\textbf{(a) Pointwise convergence.}
	Fix $x\in X$.
	For $n>\lvert x\rvert+1$,
	$|x-n|\ge n-\lvert x\rvert\ge \tfrac{n}{2}$, hence
	\[
	0\le \frac{1}{(x-n)^2}\le \frac{4}{n^2}.
	\]
	Since $\sum 4/n^2$ converges, by comparison $\sum (x-n)^{-2}$ converges (absolutely) for the fixed $x$.
	Thus the series converges pointwise on $X$.

	\medskip

	\textbf{(b) Not uniformly convergent on $X$.}
	Uniform convergence would imply
	\[
	\sup_{x\in X}\sum_{n=N}^{M}\frac{1}{(x-n)^2}\xrightarrow[N,M\to\infty]{}0.
	\]
	But for any $N$ choose an integer $k\ge N$ and take $x=k+\delta$ with $0<\delta<1$.
	Then the tail contains the term $1/(x-k)^2=1/\delta^2$, which can be made arbitrarily large as $\delta\downarrow0$.
	Hence the supremum of the tail is infinite for every $N$, so the Cauchy criterion fails.
	Therefore the series is \emph{not} uniformly convergent on $X$.

	\medskip

	\textbf{(c) Continuity of the sum.}
	Fix $x_0\in X$ and set $\delta=\tfrac12\,\mathrm{dist}(x_0,\mathbb{N})>0$.
	On the interval $I=(x_0-\delta,x_0+\delta)\subset X$, the finitely many functions
	$(x-n)^{-2}$ with $n$ near $I$ are continuous, and for all sufficiently large $n$ and all $x\in I$,
	\[
	\frac{1}{(x-n)^2}\le \frac{4}{n^2}.
	\]
	By the Weierstrass M-test, the tail $\sum_{n>N}(x-n)^{-2}$ converges uniformly on $I$.
	Hence the whole series converges uniformly on $I$ to a continuous function.
	Since $x_0$ was arbitrary, the sum $f$ is continuous on $X$.


	\textbf{Conclusion.}
	The series converges pointwise and absolutely on $X$, is not uniformly convergent on $X$, and its sum belongs to $C(X)$ (local uniform convergence).

	\par\medskip\noindent\textbf{Convergence Criteria for Sequences and Series of Functions}\par

	\textbf{A) Sequences of functions $(f_n:X\to\mathbb R)$.}

		\par\noindent\textbullet\quad \emph{Pointwise convergence:} $f_n\to f$ if $\forall x\in X$, $f_n(x)\to f(x)$.
		\par\noindent\textbullet\quad \emph{Uniform convergence:} $f_n\to f$ uniformly if
		\[
		\sup_{x\in X}|f_n(x)-f(x)|\xrightarrow[n\to\infty]{}0.
		\]
		\par\noindent\textbullet\quad \emph{Uniform Cauchy criterion:} $f_n$ converges uniformly $\iff$
		$\sup_{x\in X}|f_m(x)-f_n(x)|\xrightarrow[m,n\to\infty]{}0$.
		\par\noindent\textbullet\quad \emph{Dini (compact $X$):} If $X$ compact, $f_n\in C(X)$, $f_n\downarrow f$ or $f_n\uparrow f$
		pointwise and $f\in C(X)$, then $f_n\to f$ uniformly.
		\par\noindent\textbullet\quad \emph{Uniform limit theorem:} If $f_n\in C(X)$ and $f_n\to f$ uniformly, then $f\in C(X)$.

	\textbf{Examples.}

		\par\noindent\textbullet\quad $f_n(x)=x^n$ on $[0,1]$: pointwise $\to \mathbf 1_{\{1\}}$, not uniform.
		\par\noindent\textbullet\quad Geometric partial sums $S_n(x)=\sum_{k=0}^n x^k$ on $[0,a]$ with $0<a<1$:
		$(S_n)$ is uniformly Cauchy $\Rightarrow$ uniform convergence.
		\par\noindent\textbullet\quad $f_n(x)=x^n$ on $[0,a]$ with $0<a<1$:
		monotone $\downarrow$ to $0\in C([0,a])$ $\Rightarrow$ uniform by Dini.


	\textbf{B) Series of functions $\sum_{n=1}^\infty f_n$.}

	Let $S_N=\sum_{n=1}^N f_n$.

		\par\noindent\textbullet\quad \emph{Pointwise convergence:} $S_N(x)\to S(x)$ for each $x\in X$.
		\par\noindent\textbullet\quad \emph{Uniform convergence (Cauchy form):} $\sum f_n$ converges uniformly $\iff$
		$\sup_{x\in X}\big|\sum_{k=m}^{n} f_k(x)\big|\xrightarrow[m,n\to\infty]{}0$.
		\par\noindent\textbullet\quad \emph{Weierstrass M-test (uniform absolute):} If $|f_n(x)|\le M_n$ on $X$ and
		$\sum M_n<\infty$, then $\sum f_n$ converges uniformly (hence absolutely).
		\par\noindent\textbullet\quad \emph{Leibniz alternating test (uniform):} If $f_n=(-1)^n a_n$ with $a_n\ge0$,
		$a_{n+1}(x)\le a_n(x)$ for all $x$ and $a_n\to0$ uniformly on $X$,
		then $\sum f_n$ converges uniformly on $X$.
		\par\noindent\textbullet\quad \emph{Dirichlet test (uniform):} If partial sums $A_N(x)=\sum_{n=1}^N a_n(x)$ are
		uniformly bounded on $X$, and $b_n(x)$ is monotone in $n$ for each $x$ with
		$b_n\to0$ uniformly, then $\sum a_n(x)b_n(x)$ converges uniformly.
		\par\noindent\textbullet\quad \emph{Abel test (uniform):} If $\sum a_n(x)$ converges uniformly on $X$ and
		$b_n(x)$ is uniformly bounded and monotone in $n$ for each $x$, then
		$\sum a_n(x)b_n(x)$ converges uniformly.
		\par\noindent\textbullet\quad \emph{Preservation:} If $f_n\in C(X)$ and $\sum f_n$ converges uniformly, then
		the sum $S\in C(X)$ (and $\int \sum f_n=\sum \int f_n$).

	\textbf{Examples.}

		\par\noindent\textbullet\quad (\emph{M-test}) $f_n(x)=\dfrac{x^n}{n^2}$ on $[0,1]$:
		$|f_n|\le 1/n^2$, $\sum 1/n^2<\infty$ $\Rightarrow$ uniform absolute convergence.
		\par\noindent\textbullet\quad (\emph{Leibniz}) $f_n(x)=(-1)^n\dfrac{x^n}{n}$ on $[0,1]$:
		$a_n=x^n/n\downarrow$ and $a_n\to0$ uniformly $\Rightarrow$ uniform convergence (not uniformly absolute).
		\par\noindent\textbullet\quad (\emph{Dirichlet}) $\sum_{n=1}^\infty \dfrac{\sin(nx)}{n}$ on $[\delta,2\pi-\delta]$:
		partial sums of $\sin(nx)$ uniformly bounded; $1/n\downarrow 0$ uniformly
		$\Rightarrow$ uniform convergence on those compact subintervals.
		\par\noindent\textbullet\quad (\emph{Pointwise but not uniform}) $\sum_{n=1}^\infty \dfrac{n^2x}{1+n^4x^2}$ on $[0,1]$:
		pointwise (absolute) convergence, not uniform on the whole interval.
		\par\noindent\textbullet\quad (\emph{Locally uniform}) $\sum_{n=1}^\infty (x-n)^{-2}$ on $X=\mathbb{R}\setminus\mathbb{N}$:
		not uniform on $X$, but uniform on neighborhoods avoiding integers $\Rightarrow$ sum is continuous.

	\par\medskip\noindent\textbf{What Uniform Convergence Buys You (and Key Tools)}\par

	\textbf{Uniform Limit Theorem.}
	If $X$ is a metric space, $f_n\in C(X)$, and $f_n\to f$ uniformly on $X$, then $f\in C(X)$.

	\textbf{Integration commutes with uniform limit (Riemann).}
	If $f_n:[a,b]\to\mathbb{R}$ are Riemann integrable and $f_n\to f$ uniformly on $[a,b]$, then
	\[
	\int_a^b f_n \,dx \to \int_a^b f \,dx .
	\]

	\textbf{Termwise integration of series.}
	If $\sum f_n$ converges uniformly on $[a,b]$ and each $f_n$ is Riemann integrable, then
	\[
	\int_a^b \Big(\sum_{n=1}^\infty f_n\Big)=\sum_{n=1}^\infty \int_a^b f_n.
	\]

	\textbf{Termwise differentiation (sufficient condition).}
	Let $I=[a,b]$. If $f_n\in C^1(I)$, $f_n'\to g$ uniformly on $I$, and $(f_n(x_0))_n$ converges for some $x_0\in I$, then
	$f_n\to f$ uniformly on $I$, $f\in C^1(I)$, and $f'=g$.

	\textbf{Power series.}
	For $\sum_{n=0}^\infty a_n (x-x_0)^n$ with radius $R>0$:
	uniform convergence on each closed $[x_0-r,x_0+r]\subset (x_0-R,x_0+R)$;
	termwise integration/differentiation valid on $(x_0-R,x_0+R)$; the derivative series has radius $R$.

	\textbf{DiniĂ˘â‚¬â„˘s theorem (compact $X$).}
	If $X$ is compact, $f_n\in C(X)$, and $f_n\downarrow f\in C(X)$ (or $f_n\uparrow f$), then $f_n\to f$ uniformly.

	\textbf{Arzel\`a--Ascoli.}
	If $X$ is compact and $\mathcal F\subset C(X)$ is equicontinuous and pointwise bounded, then every sequence in $\mathcal F$ has a uniformly convergent subsequence with continuous limit.

	\textbf{Uniform Dirichlet test.}
	If $A_N(x)=\sum_{n=1}^N a_n(x)$ are uniformly bounded on $X$, and $b_n(x)$ is monotone in $n$ for each $x$ with $b_n\to0$ uniformly, then $\sum a_n(x)b_n(x)$ converges uniformly.

	\textbf{Uniform Abel test.}
	If $\sum a_n(x)$ converges uniformly on $X$ and $b_n(x)$ is uniformly bounded and monotone in $n$ for each $x$, then $\sum a_n(x)b_n(x)$ converges uniformly.


	\textbf{Mini-examples.}

		\par\noindent\textbullet\quad (Uniform limit) $f_n(x)=x^n$ on $[0,a]$, $0<a<1$: $f_n\downarrow 0$ and $f_n\to 0$ uniformly (Dini).
		\par\noindent\textbullet\quad (M-test) $\sum \frac{x^n}{n^2}$ on $[0,1]$: $|f_n|\le 1/n^2$, so uniform absolute convergence; integrals may be swapped with sum.
		\par\noindent\textbullet\quad (Alternating uniform) $\sum (-1)^n \frac{x^n}{n}$ on $[0,1]$: uniform (Leibniz), but not uniformly absolute.
		\par\noindent\textbullet\quad (Dirichlet) $\sum \frac{\sin(nx)}{n}$: uniform on $[\delta,2\pi-\delta]$ for any $\delta>0$.
		\par\noindent\textbullet\quad (Arzel\`a--Ascoli) $f_n(x)=\sin(nx)/n$ on $[0,2\pi]$: equicontinuous and bounded $\Rightarrow$ a uniformly convergent subsequence.

	\textbf{Gotchas.}
	Pointwise convergence does not preserve continuity or integrals;
	 uniform convergence does.

	Uniform absolute $\Rightarrow$ uniform, but not conversely.

	Local uniform convergence suffices for continuity on open domains.

	\par\medskip\noindent\textbf{Decision Tree for Convergence of Sequences and Series of Functions}\par

	\textbf{Series of functions $\sum f_n$ on $X$.}

		\par\noindent\textbullet\quad \textit{Uniform bound by a summable scalar?} \\
		If $|f_n(x)|\le M_n$ on $X$ and $\sum M_n<\infty$ $\Rightarrow$ \textbf{Weierstrass M-test}:
		uniform absolute convergence.

		\par\noindent\textbullet\quad \textit{Alternating in $n$?} $f_n=(-1)^n a_n$. \\
		If $a_n(x)\ge0$, nonincreasing in $n$ for each $x$, and $a_n\to0$ uniformly on $X$ $\Rightarrow$
		\textbf{Leibniz (uniform)}: uniform convergence (typically not uniformly absolute).

		\par\noindent\textbullet\quad \textit{Product form $a_n(x)b_n(x)$?} \\
		\textbf{Dirichlet (uniform):} if $A_N(x)=\sum_{n=1}^N a_n(x)$ are uniformly bounded on $X$ and
		$b_n(x)$ is monotone in $n$ with $b_n\to0$ uniformly, then $\sum a_n b_n$ converges uniformly. \\
		\textbf{Abel (uniform):} if $\sum a_n(x)$ converges uniformly on $X$ and $b_n(x)$ is uniformly bounded
		and monotone in $n$, then $\sum a_n b_n$ converges uniformly.

		\par\noindent\textbullet\quad \textit{Power series / radius present?} \\
		Determine radius $R$ via root/ratio pointwise. Convergence is uniform on every closed subinterval
		strictly inside the radius; termwise differentiation/integration valid in $(x_0-R,x_0+R)$.

		\par\noindent\textbullet\quad \textit{Spikes or singularities at isolated points?} \\
		Expect global uniform \emph{fails}. Prove \textbf{local uniform} convergence on neighborhoods avoiding singularities
		to deduce continuity on the punctured domain.

		\par\noindent\textbullet\quad \textit{No pattern? Use uniform Cauchy on compacta.} \\
		Show tail $\sup_{x\in K}|\sum_{n>N} f_n(x)|\to0$ for each compact $K\subset X$.

		\par\noindent\textbullet\quad \textit{Absolute vs conditional.} \\
		If $\sum \|f_n\|_\infty<\infty$ $\Rightarrow$ uniform absolute. Alternating/Dirichlet/Abel often give uniform but not absolute.

	\textbf{Sequences of functions $(f_n)$.}

		\par\noindent\textbullet\quad \textbf{Dini (compact $X$):} If $f_n\in C(X)$ and $f_n\downarrow f\in C(X)$ (or $\uparrow$), then $f_n\to f$ uniformly.
		\par\noindent\textbullet\quad \textbf{Arzel\`a--Ascoli:} On compact $X$, equicontinuous and pointwise bounded families have uniformly convergent subsequences.
		\par\noindent\textbullet\quad \textbf{Uniform Cauchy:} $\sup_{x\in X}|f_m(x)-f_n(x)|\to0$ $\Rightarrow$ uniform convergence.
		\par\noindent\textbullet\quad \textbf{Power-series tails:} Use M-test on tails to get uniform convergence on compacta.


	\textbf{Micro-examples.}

		\par\noindent\textbullet\quad (M-test) $\displaystyle f_n(x)=\frac{x^n}{n^2}$ on $[0,1]$:
		$|f_n|\le 1/n^2$, so uniform absolute convergence.
		\par\noindent\textbullet\quad (Leibniz) $\displaystyle f_n(x)=(-1)^n\frac{x^n}{n}$ on $[0,1]$:
		$a_n=x^n/n$ decreases in $n$, $a_n\to0$ uniformly $\Rightarrow$ uniform, not uniformly absolute.
		\par\noindent\textbullet\quad (Dirichlet) $\displaystyle \sum_{n=1}^\infty \frac{\sin(nx)}{n}$:
		uniform on $[\delta,2\pi-\delta]$ for any $\delta>0$; not uniform on all of $[0,2\pi]$.
		\par\noindent\textbullet\quad (Local uniform) $\displaystyle \sum_{n=1}^\infty (x-n)^{-2}$ on $\mathbb R\setminus\mathbb N$:
		not uniform globally; locally uniform $\Rightarrow$ continuous sum on the punctured domain.
		\par\noindent\textbullet\quad (Dini) $f_n(x)=x^n$ on $[0,a]$, $0<a<1$: $f_n\downarrow 0\in C$ $\Rightarrow$ uniform.


	\textbf{What uniform convergence buys you.}
	Uniform limit of continuous functions is continuous; integrals pass to the limit.
	For series: uniform convergence $\Rightarrow$ termwise integration; with extra hypotheses on derivatives,
	termwise differentiation on compact intervals.

	\par\medskip\noindent\textbf{Problem 16 — Implicit Function Theorem via a block map}\par

	\textbf{Setup.}
	Let $U\subset\mathbb{R}^{n+m}$ be open and $f:U\to\mathbb{R}^m$ be $C^1$.
	Write $(x,y)\in\mathbb{R}^n\times\mathbb{R}^m$ and assume $(x_0,y_0)\in U$ with
	\[
	f(x_0,y_0)=0
	\qquad\text{and}\qquad
	J_y f\big|_{(x_0,y_0)}:=\det\!\Big[\tfrac{\partial f^i}{\partial y^j}\Big]_{i,j=1}^m\neq 0.
	\]

		\par\noindent \textbf{(a)}\quad \textbf{Local invertibility of $F$.}
		Define $F(x,y)=(x,f(x,y))$. Its Jacobian at $(x_0,y_0)$ is
		\[
		DF\big|_{(x_0,y_0)}=
		\begin{pmatrix}
			I_n & 0\\
			D_x f\big|_{(x_0,y_0)} & D_y f\big|_{(x_0,y_0)}
		\end{pmatrix}.
		\]
		This block–triangular matrix has
		$\det DF=\det(I_n)\,\det(D_y f)\neq0$,
		so by the inverse function theorem $F$ is a local $C^1$ diffeomorphism
		near $(x_0,y_0)$.

		\medskip

		\par\noindent \textbf{(b)}\quad \textbf{A property of the inverse $G$.}
		Let $G=(G^1,\dots,G^{n+m})$ be the local inverse of $F$ on a neighborhood
		$V\ni (x_0,0)$. For any $(X,0)\in V$,
		\[
		F\big(G(X,0)\big)=(X,0)
		\quad\Longrightarrow\quad
		\begin{cases}
			(G^1,\dots,G^n)(X,0)=X,\\[2pt]
			\displaystyle f\!\big(X,\;G^{n+1}(X,0),\dots,G^{n+m}(X,0)\big)=0.
		\end{cases}
		\]

		\medskip

		\par\noindent \textbf{(c)}\quad \textbf{Existence and uniqueness of the implicit function.}
		Define, for $X$ near $x_0$,
		\[
		g(X):=\big(G^{n+1}(X,0),\dots,G^{n+m}(X,0)\big).
		\]
		Then $f(X,g(X))=0$ and $g(x_0)=y_0$.
		If $f(X,y)=0$ with $X$ near $x_0$, $y$ near $y_0$, then
		$F(X,y)=(X,0)$, so $(X,y)=G(X,0)$ and hence $y=g(X)$ (uniqueness).

		\medskip

		\par\noindent \textbf{(d)}\quad \textbf{Differentiability and the formula for $Dg$.}
		Since $G$ is $C^1$, so is $g$. Differentiating $f(x,g(x))\equiv0$ gives
		\[
		D_x f(x,g(x)) \;+\; D_y f(x,g(x))\,Dg(x) \;=\; 0,
		\]
		and because $D_y f$ stays invertible nearby,
		\[
		\boxed{\; Dg(x) \;=\; -\big[D_y f(x,g(x))\big]^{-1} \, D_x f(x,g(x)) \; }.
		\]

		\medskip

		\par\noindent \textbf{(e)}\quad \textbf{Application: the folium $x^3+y^3-3xy=0$.}
		Let $f(x,y)=x^3+y^3-3xy$. Then
		\[
		\frac{\partial f}{\partial y}=3y^2-3x, \qquad
		\frac{\partial f}{\partial x}=3x^2-3y.
		\]
		On the level set $C=\{f=0\}$ the IFT yields a local graph $y=g(x)$ at points
		with $\frac{\partial f}{\partial y}\neq0$.
		Solving on $C$ the system $\{f=0,\ \partial f/\partial y=0\}$ gives
		$x=y^2$ and $y^6-2y^3=0$, so $(x,y)=(0,0)$ or $(2^{2/3},2^{1/3})$.
		Hence $C$ is locally a graph $y=g(x)$ away from small neighborhoods
		of these two exceptional points.

	\noindent
	Here is a visualization of the \emph{folium curve}
	\[
	x^{3}+y^{3}-3xy=0,
	\]
	showing the \textbf{exceptional points} $(0,0)$ and $(2^{2/3},\,2^{1/3})$ where IFT fails for
	$y=g(x)$. Indeed,
	\[
	\frac{\partial f}{\partial y}=3y^{2}-3x=0 \iff x=y^{2},
	\qquad
	f(x,y)=0 \iff y^{6}-2y^{3}=0 \iff y=0 \ \text{or}\ y^{3}=2.
	\]
	Everywhere else on the curve, $\partial f/\partial y\neq0$ and the set is locally a graph $y=g(x)$.

	\textbf{IFT (finite-dimensional $C^1$).}
	Let $U\subset\mathbb{R}^{n+m}$ be open and $f:U\to\mathbb{R}^m$ be $C^1$.
	Write $(x,y)\in\mathbb{R}^n\times\mathbb{R}^m$. Suppose $(x_0,y_0)\in U$ with
	\[
	f(x_0,y_0)=0,\qquad \det D_y f(x_0,y_0)\neq 0.
	\]
	Then there exist neighborhoods $W'\ni x_0$, $W''\ni y_0$ and a unique map $g:W'\to W''$,
	of class $C^1$, such that $g(x_0)=y_0$ and $f(x,g(x))=0$ on $W'$. Moreover
	\[
	Dg(x)= -\big[D_y f(x,g(x))\big]^{-1} D_x f(x,g(x)).
	\]
	If $f\in C^k$ (resp.\ real-analytic) then $g\in C^k$ (resp.\ analytic).

	\medskip
	\textbf{Geometric picture.}
	Near $(x_0,y_0)$, the zero set $f^{-1}(0)$ is a smooth $n$-dimensional surface; in suitable
	coordinates it is the graph $y=g(x)$.

	\medskip
	\textbf{Proof sketch.}
	Apply the inverse function theorem to $F(x,y)=(x,f(x,y))$:
	\[
	DF\big|_{(x_0,y_0)}=
	\begin{pmatrix}
		I_n & 0\\
		D_x f & D_y f
	\end{pmatrix}_{(x_0,y_0)}
	\]
	is invertible by hypothesis (block-triangular). Then $F$ has a local inverse $G$ and
	$g(x):=(G^{n+1},\dots,G^{n+m})(x,0)$.


	\textbf{Examples.}

	\emph{1) Circle.} $f(x,y)=x^2+y^2-1$. At $(0,1)$, $\partial f/\partial y=2\ne0$,
	so $y=g(x)$ exists locally (upper semicircle). At $(1,0)$ we cannot solve for $y$,
	but can solve for $x=h(y)$ since $\partial f/\partial x=2\ne0$.

	\emph{2) Parabola: solve for the right variable.}
	$f(x,y)=y^2-x$ at $(0,0)$ has $\partial f/\partial y=0$ (no $y=g(x)$),
	but $\partial f/\partial x=-1\ne0$; hence $x=h(y)=y^2$.

	\emph{3) Transcendental (Lambert $W$).}
	$f(x,y)=y e^y - x$. At $(0,0)$, $\partial f/\partial y=1$, so $y=g(x)=W(x)$ exists,
	analytic near $0$, with $g'(x)=\big(e^{g(x)}(1+g(x))\big)^{-1}$.

	\emph{4) Constraint manifolds.}
	If $\operatorname{rank} Df = m$ on $f^{-1}(0)$, the level set is an $n$-dimensional submanifold,
	locally a graph by IFT.


	\textbf{Failures / counterexamples.}

	\emph{(i) Cusp:} $f(x,y)=y^3-x^2$ at $(0,0)$ has $\partial f/\partial y=0$.
	The zero set has a cusp; it is not a graph $y=g(x)$ nor $x=h(y)$ there.

	\emph{(ii) Two branches:} $f(x,y)=y^2-x$ at $(0,0)$: cannot solve for $y$ (two values
	$\pm\sqrt{x}$), but can solve for $x$ as above. The condition must be on the variable you
	solve for.

	\emph{(iii) Lack of smoothness:} $f(x,y)=|y|-x$ at $(0,0)$ is not $C^1$ in $y$.
	The zero set is $y=\pm x$, not a single branch; IFT does not apply.

	\medskip
	\textbf{Banach-space version.}
	If $E,F$ are Banach spaces, $f:E\times F\to F$ is $C^1$ near $(x_0,y_0)$,
	$f(x_0,y_0)=0$, and $D_y f(x_0,y_0):F\to F$ is an isomorphism, then there exists a unique
	$C^1$ map $g$ near $x_0$ with $f(x,g(x))=0$ and
	$Dg(x)= -\big[D_y f(x,g(x))\big]^{-1} D_x f(x,g(x))$.

	Let $f(x,y)=x^2+y^2-1$. Then $\partial f/\partial x=2x$, $\partial f/\partial y=2y$.

	Since $\partial f/\partial y(0,1)=2\neq 0$, the IFT gives a unique $C^\infty$ function
	$g$ with $g(0)=1$ and $f(x,g(x))\equiv 0$ for $|x|$ small (upper semicircle).
	The IFT derivative formula (with $n=m=1$) yields
	\[
	g'(x)= -\frac{\partial f/\partial x}{\partial f/\partial y}\Big|_{(x,g(x))}
	= -\frac{2x}{2\,g(x)} = -\frac{x}{g(x)}.
	\]
	Hence $g'(0)=0$. Using the exact branch $g(x)=\sqrt{1-x^2}$ gives
	$g''(0)=-1$.

	Here $\partial f/\partial y(1,0)=0$ so we cannot solve $y=g(x)$,
	but $\partial f/\partial x(1,0)=2\neq0$ gives a unique $C^\infty$ function $x=h(y)$ with
	$h(0)=1$ and $f(h(y),y)\equiv 0$ (right semicircle).
	The derivative formula (solving for $x$) gives
	\[
	h'(y) = -\,\frac{\partial f/\partial y}{\partial f/\partial x}\Big|_{(h(y),y)}
	= -\,\frac{2y}{2\,h(y)} = -\frac{y}{h(y)},
	\]
	so $h'(0)=0$. With the exact branch $h(y)=\sqrt{1-y^2}$, one gets $h''(0)=-1$.

	Let $f(x,y)=y^2-x$. Then $\partial f/\partial x=-1$, $\partial f/\partial y=2y$.

	Since $\partial f/\partial y(0,0)=0$, we cannot solve $y=g(x)$ there (two values $\pm\sqrt{x}$ for $x>0$),
	but $\partial f/\partial x(0,0)=-1\neq0$ gives a unique $C^\infty$ function $x=h(y)$ with $h(0)=0$.
	The IFT formula (solving for $x$) yields
	\[
	h'(y) = -\,\frac{\partial f/\partial y}{\partial f/\partial x}\Big|_{(h(y),y)}
	= -\,\frac{2y}{-1} = 2y,
	\]
	so $h'(0)=0$ and $h''(y)=2$. In fact $h(y)=y^2$ exactly.

	If $y_0\neq 0$, then $\partial f/\partial y(x_0,y_0)=2y_0\neq 0$, so there is a unique branch
	$y=g(x)$ through $(x_0,y_0)$ with
	\[
	g'(x)= -\frac{\partial f/\partial x}{\partial f/\partial y}\Big|_{(x,g(x))}
	= \frac{1}{2g(x)}.
	\]
	These are the two smooth branches $y=\pm\sqrt{x}$ away from the vertex.

	We have $f_x=-2x$, $f_y=3y^2$, so $f_x(0,0)=f_y(0,0)=0$. The IFT hypothesis fails for both
	solving $y=g(x)$ and $x=h(y)$ at $(0,0)$.

	The zero set is $y^3=x^2$, i.e.\ $y=|x|^{2/3}\ (\ge0)$, a continuous but \emph{non-differentiable}
	graph over $x$ at $0$.
	Implicit differentiation gives $3y^2\,y'-2x=0$, so along the curve
	\[
	y'=\frac{2x}{3y^2}=\frac{2x}{3|x|^{4/3}}=\frac{2}{3}\,\mathrm{sgn}(x)\,|x|^{-1/3}\xrightarrow[x\to 0]{}\pm\infty,
	\]
	i.e.\ a vertical tangent and no $C^1$ graph $y=g(x)$ through $(0,0)$.
	Solving for $x$ yields two branches $x=\pm y^{3/2}$ for $y\ge0$; thus there is no single-valued
	implicit function $x=h(y)$ on a neighborhood of $(0,0)$. The zero set has a \emph{cusp}.

	Here $f_x=-1$, $f_y=2y$, so $f_y(0,0)=0$ (cannot solve $y=g(x)$: two values $y=\pm\sqrt{x}$ for $x>0$),
	but $f_x(0,0)=-1\neq0$ so the IFT applies to solve $x=h(y)$.
	Indeed $x=h(y)=y^2$ with
	\[
	h'(y)=-\frac{f_y}{f_x}\Big|_{(h(y),y)}=-\frac{2y}{-1}=2y,\qquad h''(y)=2.
	\]
	Thus the correct variable to solve for is dictated by which partial derivative is nonzero.
```

## CP-II-0157

- chapter line: 14473

```tex
\label{prob:cp-ii-0157}
\par\noindent\textbullet\quad \textbf{$L^p$ norms.} For $1\le p<\infty$, the map $f\mapsto\|f\|_{L^p}$ is weakly l.s.c.:
		if $f_n\rightharpoonup f$ in $L^p$, then $\|f\|_{p}\le \liminf_n \|f_n\|_{p}$.
```

## CP-II-0158

- chapter line: 14479

```tex
\label{prob:cp-ii-0158}
(Indicator; threshold $s<\tfrac12$ in 1D).

For $f=\mathbf 1_{(0,1)}$ one has
\(
\widehat f(\xi)=e^{-i\xi/2}\,\frac{2\sin(\xi/2)}{\xi}
\),
so $|\widehat f(\xi)|^2\sim 2/\xi^2$ as $|\xi|\to\infty$. Therefore
\[
\|f\|_{H^s(\mathbb R)}^2 \sim \int_{\mathbb R} (1+\xi^2)^s \frac{1}{\xi^2}\,d\xi<\infty
\iff s<\tfrac12.
\]
Equivalently, for $0<s<1$, the Gagliardo seminorm
$\iint \frac{|f(x)-f(y)|^2}{|x-y|^{1+2s}}dx\,dy$
converges iff $s<\tfrac12$.
```

## CP-II-0161

- chapter line: 14522

```tex
\label{prob:cp-ii-0161}
Gaussian smoothing.

Let
\[
g_\varepsilon(y)
= \frac{1}{\sqrt{\pi}\,\varepsilon}\,e^{-y^2/\varepsilon^2}.
\]
Then $f*g_\varepsilon$ is the \emph{Gaussian--blurred} version of $f$.

\medskip
\noindent$\Rightarrow$ \emph{Effect:} removes noise, increases
differentiability.

\bigskip\hrule\bigskip
```

## CP-II-0164

- chapter line: 14540

```tex
\label{prob:cp-ii-0164}
\par\noindent\textbullet\quad Tonelli--Fubini can be verified directly;
```

## CP-II-0165

- chapter line: 14545

```tex
\label{prob:cp-ii-0165}
\par\noindent\textbullet\quad \textbf{Singular (continuous):}
		The Cantor probability measure $\gamma$ is supported on the middle--third Cantor set $C$ with $m(C)=0$,
		hence $\gamma\perp m$ and has no atoms.
```

## CP-II-0167

- chapter line: 14552

```tex
\label{prob:cp-ii-0167}
— A Schauder basis for $C([-1,1])$ from hat functions

Using the result of Question~5, prove that there exists a sequence
$\{\phi_n\}_{n\ge0}\subset C([-1,1])$ such that for every $f\in C([-1,1])$ there exists a
\emph{unique} series $\sum_{n=0}^{\infty} a_n \phi_n$ which converges uniformly to $f$.

We recall the hat (tent) framework from Question~5 and collect the identities used in the proof.

	\par\noindent\textbullet\quad \textbf{Hat functions on a uniform grid.}
	For $n\in\mathbb{N}$ and $r\in\mathbb{Z}$ define
	\[
	\Delta_{n,r}(x)=\max\!\{0,\;1-n\lvert x-r/n\rvert\},\qquad x\in[-1,1].
	\]
	Then $\Delta_{n,r}$ is supported on $[(r-1)/n,(r+1)/n]$, satisfies
	$\Delta_{n,r}(r/n)=1$, is linear with slopes $\pm n$ on its support, and for each
	$x\in[k/n,(k+1)/n]$ one has
	\[
	\Delta_{n,k}(x)+\Delta_{n,k+1}(x)=1,\qquad
	\Delta_{n,m}(x)=0\ \text{for } m\notin\{k,k+1\}.
	\]
	Consequently, for any $f\in C([-1,1])$ the piecewise–linear interpolant
	\[
	f_n(x)=\sum_{m=-n}^{n} f\!\left(\frac{m}{n}\right)\Delta_{n,m}(x)
	\]
	is linear on each $[k/n,(k+1)/n]$, interpolates the data $f_n(m/n)=f(m/n)$, and
	satisfies the uniform error bound
	\[
	\|f-f_n\|_\infty\le \omega_f\!\left(\frac{1}{n}\right),
	\]
	where $\omega_f(\delta)=\sup_{|x-y|\le \delta}|f(x)-f(y)|$ is the modulus of continuity.

	\par\noindent\textbullet\quad \textbf{Dyadic refinement and midpoint hats (Faber–Schauder atoms).}
	On $[0,1]$ (with $u=\frac{x+1}{2}$) define the dyadic midpoint hats
	\[
	h_{k,m}(u)=\max\!\Big\{0,\;1-2^{k+1}\Big|u-\frac{2m-1}{2^{k+1}}\Big|\Big\},
	\qquad k\ge 0,\ m=1,\dots,2^{k}.
	\]
	Each $h_{k,m}$ is the tent of height $1$ with support
	$\big[(m-1)/2^{k},(m+1)/2^{k}\big]$ and peak at $(2m-1)/2^{k+1}$.
	Transport to $[-1,1]$ via $\phi_{k,m}(x)=h_{k,m}\big(\frac{x+1}{2}\big)$ and add two
	low-order functions $\phi_0(x)=1$, $\phi_1(x)=\frac{x+1}{2}$.

	\par\noindent\textbullet\quad \textbf{Telescoping of piecewise–linear interpolants.}
	Let $g(u)=f(2u-1)$ and let $g_{2^K}$ be the piecewise–linear interpolant on the dyadic
	grid $\{j/2^K\}_{j=0}^{2^K}$. Then
	\[
	g_{2^{K}}(u)
	= g_{2^{0}}(u)
	+ \sum_{k=0}^{K-1}\big(g_{2^{k+1}}(u)-g_{2^{k}}(u)\big),
	\]
	and each difference admits the representation
	\[
	g_{2^{k+1}}(u)-g_{2^{k}}(u)
	= \sum_{m=1}^{2^{k}} d_{k,m}\,h_{k,m}(u),
	\]
	with \emph{detail coefficients} (midpoint second differences)
	\[
	d_{k,m}
	= g\!\Big(\frac{2m-1}{2^{k+1}}\Big)
	-\frac{1}{2}\Bigg[
	g\!\Big(\frac{m-1}{2^{k}}\Big)
	+ g\!\Big(\frac{m}{2^{k}}\Big)\Bigg].
	\]
	Hence, for $K\ge1$,
	\[
	g_{2^{K}}(u) = a_0 + a_1 u + \sum_{k=0}^{K-1}\sum_{m=1}^{2^{k}} d_{k,m}\,h_{k,m}(u),
	\qquad a_0=g(0),\ \ a_1=g(1)-g(0).
	\]
	Pulling back to $[-1,1]$ yields
	\[
	f_{2^{K}}(x)= a_0\,\phi_0(x)+a_1\,\phi_1(x)
	+ \sum_{k=0}^{K-1}\sum_{m=1}^{2^{k}} d_{k,m}\,\phi_{k,m}(x).
	\]

	\par\noindent\textbullet\quad \textbf{Uniform convergence and uniqueness.}
	By the bound in (a), $f_{2^{K}}\to f$ uniformly as $K\to\infty$, hence
	\[
	f(x)= a_0\,\phi_0(x)+a_1\,\phi_1(x)
	+ \sum_{k=0}^{\infty}\sum_{m=1}^{2^{k}} d_{k,m}\,\phi_{k,m}(x)
	\]
	is a uniformly convergent series in $\{\phi_n\}\subset C([-1,1])$.
	Uniqueness of the coefficients follows from the triangular structure with respect to
	levels: if $\sum a_n\phi_n\equiv 0$, then $a_0=a_1=0$ (evaluation at the endpoints),
	and at each level $k$ the functions $\{\phi_{k,m}\}_m$ have disjoint supports and are
	the only basis elements nonzero at their midpoints; thus all detail coefficients vanish
	by induction.

\noindent\rule{\textwidth}{0.4pt}

Work on $[0,1]$ with $u\in[0,1]$ and define
\[
\psi_0(u)=1,\quad \psi_1(u)=u,\qquad
h_{k,m}(u)=\max\!\Big\{0,\;1-2^{k+1}\Big|u-\frac{2m-1}{2^{k+1}}\Big|\Big\}
\]
for $k\ge0$ and $m=1,\dots,2^k$.
Transport to $[-1,1]$ by $u=(x+1)/2$:
\[
\phi_0(x)=1,\qquad \phi_1(x)=\tfrac{x+1}{2},\qquad
\phi_{k,m}(x)=h_{k,m}\!\Big(\tfrac{x+1}{2}\Big).
\]
Enumerate $\{\phi_n\}$ as $(\phi_0,\phi_1,\phi_{0,1},\phi_{1,1},\phi_{1,2},\ldots)$.

Given $f\in C([-1,1])$, set $g(u)=f(2u-1)$. Define
\[
a_0=g(0),\qquad a_1=g(1)-g(0),
\]
and for $k\ge0$, $m=1,\dots,2^k$,
\[
d_{k,m}=g\!\Big(\frac{2m-1}{2^{k+1}}\Big)
-\frac12\Bigg[g\!\Big(\frac{m-1}{2^k}\Big)+g\!\Big(\frac{m}{2^k}\Big)\Bigg].
\]
Let $g_{2^K}$ be the piecewise–linear interpolant on the dyadic grid $\{j/2^K\}$.
Then the standard decomposition (telescoping across levels) gives
\[
g_{2^K}(u)=a_0+a_1 u+\sum_{k=0}^{K-1}\sum_{m=1}^{2^k} d_{k,m}\,h_{k,m}(u).
\]
Hence, on $[-1,1]$,
\[
f_{2^K}(x)=a_0\,\phi_0(x)+a_1\,\phi_1(x)
+\sum_{k=0}^{K-1}\sum_{m=1}^{2^k} d_{k,m}\,\phi_{k,m}(x).
\]

By Question~5, $f_{2^K}\to f$ uniformly on $[-1,1]$. Letting $K\to\infty$ yields the uniformly
convergent expansion
\[
f(x)=a_0\,\phi_0(x)+a_1\,\phi_1(x)
+\sum_{k=0}^{\infty}\sum_{m=1}^{2^k} d_{k,m}\,\phi_{k,m}(x),
\]
i.e. a series $\sum_{n\ge0} a_n\phi_n$ converging uniformly to $f$.

Suppose $\sum_{n\ge0} a_n\phi_n\equiv 0$. Evaluating at $x=-1$ and $x=1$ gives
$a_0=0$ and $a_1=0$. Proceeding by levels, at level $k$ the functions
$\{\phi_{k,m}\}_m$ have disjoint supports and each is the only basis function nonzero at
its own midpoint; hence each coefficient must be zero. By induction, all coefficients vanish,
so the representation is unique.

	\par\noindent\textbullet\quad $f(x)=ax+b$: all detail coefficients $d_{k,m}$ vanish; only the low–order terms
	$\phi_0,\phi_1$ remain.
	\par\noindent\textbullet\quad $f(x)=x^2$: $d_{k,m}=\frac14\,2^{-2k}$ for all $m$, giving a rapidly convergent sum of
	midpoint hats across levels.

The system $\{\phi_n\}$ is a Schauder basis for $C([-1,1])$ (the Faber–Schauder basis):
every continuous function admits a unique uniformly convergent series in these functions.
```

## CP-II-0170

- chapter line: 14713

```tex
\label{prob:cp-ii-0170}
{Polynomials $p_n$ with $p_n(0)=1$ and $p_n(z)\to0$ for $z\neq0$}{poly-vanish-off-zero}
	Does there exist a sequence of complex polynomials $(p_n)$ such that
	$p_n(0)=1$ for all $n$ and $p_n(z)\to 0$ for each $z\in\mathbb C\setminus\{0\}$?
```

## CP-II-0173

- chapter line: 14720

```tex
\label{prob:cp-ii-0173}
\par\noindent\textbullet\quad \textbf{Bounded:} yes, $|\sin|\le1$. \textbf{Not uniformly continuous.}
	Let $a_k=\sqrt{k\pi}$, $b_k=\sqrt{k\pi+\pi/2}$. Then $|a_k-b_k|\to0$ but
	$|f(a_k)-f(b_k)|=1$.
```

## CP-II-0175

- chapter line: 14727

```tex
\label{prob:cp-ii-0175}
\par\noindent\textbullet\quad \textbf{Not Lipschitz equivalent to $\|\cdot\|_{\infty}$.}
	Always $\|f\|_{1}\le \|f\|_{\infty}$. A reverse uniform bound
	$c\|f\|_{\infty}\le \|f\|_{1}$ fails: take continuous Ă˘â‚¬Ĺ›spikesĂ˘â‚¬ĹĄ
	\[
	f_n(x)=\begin{cases}
		1-\dfrac{|x-a_n|}{\ell_n}, & |x-a_n|\le \ell_n,\\[4pt]
		0, & \text{otherwise},
	\end{cases}
	\quad a_n\to 0,\ \ell_n\downarrow 0.
	\]
	Then $\|f_n\|_{\infty}=1$ but $\|f_n\|_{1}=\int_{a_n-\ell_n}^{a_n+\ell_n}\!\!\big(1-\frac{|x-a_n|}{\ell_n}\big)\,dx
	=\ell_n\to 0$. No $c>0$ works, so the norms are not Lipschitz equivalent.
```

## CP-II-0176

- chapter line: 14743

```tex
\label{prob:cp-ii-0176}
\par\noindent\textbullet\quad The subspace topology on \(X\) consists of all sets of the form \((a,b)\cap(0,1]\).

	For example:
```

## CP-II-0178

- chapter line: 14770

```tex
\label{prob:cp-ii-0178}
\par\noindent\textbullet\quad If $T=\delta_0$, then
	\[
	(\delta_0*\phi)(x)
	= \langle\delta_0,\phi(x-\cdot)\rangle
	= \phi(x-0) = \phi(x).
	\]
```

## CP-II-0179

- chapter line: 14780

```tex
\label{prob:cp-ii-0179}
\par\noindent\textbullet\quad Dyadic intervals: $I_{n,k}=[k2^{-n},(k+1)2^{-n})$.
```

## CP-II-0186

- chapter line: 14922

```tex
\label{prob:cp-ii-0186}
\par\noindent\textbullet\quad Integrating over $\mathbb{R}^n$ gives
	\[
	\int_{\mathbb{R}^n} |f(x)g(x)|\,dx
	\;\le\;
	\frac{1}{p}\int |f|^p + \frac{1}{q}\int |g|^q.
	\]
```

## CP-II-0188

- chapter line: 14989

```tex
\label{prob:cp-ii-0188}
Dirac mass $\delta_0$.

The Dirac distribution acts by evaluation:
\[
\langle\delta_0,\varphi\rangle = \varphi(0).
\]
The following figure shows a test function $\varphi$ together with the
highlighted value $\varphi(0)$.
```
