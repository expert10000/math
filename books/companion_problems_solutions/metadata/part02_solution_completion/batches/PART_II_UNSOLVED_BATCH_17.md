# Part II missing-solution batch 17

- problems: **20**
- IDs: CP-II-0444, CP-II-0447, CP-II-0448, CP-II-0450, CP-II-0451, CP-II-0452, CP-II-0455, CP-II-0456, CP-II-0463, CP-II-0465, CP-II-0470, CP-II-0472, CP-II-0474, CP-II-0478, CP-II-0482, CP-II-0484, CP-II-0486, CP-II-0487, CP-II-0488, CP-II-0489

## CP-II-0444

- chapter line: 19250

```tex
\label{prob:cp-ii-0444}
Let $L=\sum_{n=1}^\infty 10^{-n!}$ and $r_N=\sum_{n=1}^{N}10^{-n!}=p_N/10^{N!}$.
	Then
	\[
	|L-r_N|=\sum_{n\ge N+1}10^{-n!}
	=10^{-(N+1)!}\Bigl(1+\sum_{n\ge N+2}10^{-(n!-(N+1)!)}\Bigr).
	\]
	For $n\ge N+2$ we have $n!-(N+1)!\ge (N+2)!-(N+1)!=(N+1)N!\ge N!$, hence
	\[
	\sum_{n\ge N+2}10^{-(n!-(N+1)!)}\le \sum_{k=1}^\infty (10^{-N!})^{k}
	=\frac{10^{-N!}}{1-10^{-N!}}\le \frac{1}{9}.
	\]
	Therefore
	\[
	\boxed{\ |L-r_N|< \frac{10}{9}\,10^{-(N+1)!}\ }.
	\]
	Fix $m\in\mathbb N$ and choose $N\ge m$. Since $((N+1)-m)N!\ge N!\ge1$,
	\[
	\frac{10}{9}\,10^{-(N+1)!}
	=\frac{10}{9}\,10^{-((N+1)-m)N!}\cdot 10^{-mN!}\le 10^{-mN!}
	=\frac{1}{(10^{N!})^{\,m}}.
	\]
	Thus for $q_N=10^{N!}$ we obtain
	\[
	\Bigl|L-\frac{p_N}{q_N}\Bigr|<\frac{1}{q_N^{\,m}}
	\quad\text{for all }N\ge m.
	\]
	Since this holds for every $m$ and infinitely many $N$, $L$ is a Liouville number and hence transcendental.
```

## CP-II-0447

- chapter line: 19478

```tex
\label{prob:cp-ii-0447}
One may build $p_n$ via Faber polynomials of the arc or via discrete least–squares fits on $K$;
both converge uniformly by Mergelyan.

\noindent\rule{\textwidth}{0.4pt}

\bigskip
```

## CP-II-0448

- chapter line: 19488

```tex
\label{prob:cp-ii-0448}
\par\noindent\textbullet\quad More conceptually: the functions $x \mapsto x^p/p$ and
	$y \mapsto y^q/q$ are Legendre transforms of each other.
	Young's inequality expresses this duality.
```

## CP-II-0450

- chapter line: 19520

```tex
\label{prob:cp-ii-0450}
\par\noindent\textbullet\quad \textbf{Shrinking supports.}
		In $\mathbb R^{n}$, set $f_j := |B_{1/j}|^{-1/p}\,\mathbf 1_{B_{1/j}}$. Then $\|f_j\|_p=1$ and
		$f_j\rightharpoonup 0$ in $L^{p}$; indeed $\int f_j h \to 0$ for $h\in C_c^\infty$, then extend to $L^{p'}$.
```

## CP-II-0451

- chapter line: 19527

```tex
\label{prob:cp-ii-0451}
\par\noindent\textbullet\quad \textbf{Total variation.} If $u_n\to u$ in $L^1(\Omega)$, then
		$\mathrm{TV}(u)\le \liminf_n \mathrm{TV}(u_n)$.

	If $x_n\rightharpoonup x$ in a Hilbert space, then
	$\|x\|\le \liminf_n \|x_n\|$ (weak l.s.c.\ of the norm). Moreover,
	if also $\|x_n\|\to\|x\|$, then
	\[
	\|x_n-x\|^2=\|x_n\|^2+\|x\|^2-2\,\Re\langle x_n,x\rangle \longrightarrow 0,
	\]
	hence $x_n\to x$ in norm.

	\clearpage

\subsection*{A. $L^p$ norms: weak l.s.c.\ $\;\|f\|_{p}\le \liminf_{n}\|f_n\|_{p}$}

\noindent\textbf{1.\ Strict inequality (moving bump).}\par
\noindent
On $\mathbb{R}$ set $f_n=\mathbf 1_{(n,n+1)}$. Then $f_n\rightharpoonup 0$ in $L^p$ for any $1\le p<\infty$
(vanishes on every bounded set), but
\[
\|f_n\|_{p}=1.
\]
Hence
\[
\|0\|_{p}=0 \;<\; \liminf_{n\to\infty}\|f_n\|_{p}=1.
\]

\medskip
\noindent\textbf{2.\ Strict inequality (oscillations).}\par
\noindent
On $[0,1]$, $f_n(x)=\sin(2\pi n x)$ is bounded in $L^2$ and $f_n\rightharpoonup 0$ (Riemann–Lebesgue).
But
\[
\|f_n\|_{2}=\Big(\int_0^1 \sin^2(2\pi n x)\,dx\Big)^{1/2}=\frac{1}{\sqrt{2}},
\]
so
\[
0 \;<\; \liminf_{n\to\infty}\|f_n\|_{2}=\frac{1}{\sqrt{2}}.
\]

\medskip
\noindent\textbf{3.\ Equality case (then strong convergence).}\par
\noindent
Let $f,g\in L^2[0,1]$ with $\langle f,g\rangle=0$ and set $f_n=f+\tfrac{1}{n}g$.
Then $f_n\rightharpoonup f$ and
\[
\|f_n\|_{2}^{2}=\|f\|_{2}^{2}+\frac{1}{n^{2}}\|g\|_{2}^{2}\ \longrightarrow\ \|f\|_{2}^{2}.
\]
Hence $\|f_n\|_{2}\to\|f\|_{2}$, and by the criterion ``weak $+$ norms $\Rightarrow$ strong'' we get
\[
f_n\ \to\ f \quad\text{in }L^2.
\]

\vspace{1em}

\subsection*{B. Dirichlet energy $E(u)=\displaystyle\int_{\Omega} |\nabla u|^{2}$: weak l.s.c.\ and minimizers}

\noindent\textbf{1.\ Weak l.s.c.\ in action (strict inequality possible).}\par
\noindent
Take $\Omega=(0,1)$ and $u_n(x)=\sin(2\pi n x)$. Then $u_n\rightharpoonup 0$ in $H^1_0(0,1)$, but
\[
E(u_n)=\int_0^1 |u_n'(x)|^2\,dx=\int_0^1 (2\pi n)^2\cos^2(2\pi n x)\,dx
=2\pi^{2}n^{2}\ \longrightarrow\ \infty,
\]
so trivially
\[
E(0)=0\ \le\ \liminf_{n\to\infty} E(u_n).
\]

\medskip
\noindent\textbf{2.\ Existence of a minimizer (direct method).}\par
\noindent
Let $\Omega\subset\mathbb{R}^{n}$ be bounded Lipschitz and fix boundary data $g\in H^{1/2}(\partial\Omega)$.
Minimize
\[
\mathcal{A}=\{\,u\in H^{1}(\Omega): u=g \text{ on }\partial\Omega\,\},\qquad
E(u)=\int_{\Omega}|\nabla u|^{2}\,dx.
\]
Let $(u_k)\subset\mathcal{A}$ be such that $E(u_k)\downarrow\inf_{\mathcal{A}}E$. Then $(u_k)$ is bounded in $H^{1}(\Omega)$,
hence (by reflexivity and Rellich–Kondrachov) there is a subsequence $u_{k_j}$ with
\[
u_{k_j}\rightharpoonup u \ \text{ in } H^{1}(\Omega),\qquad u_{k_j}\to u \ \text{ in } L^{2}(\Omega).
\]
The trace is stable under weak $H^1$ convergence, so $u\in\mathcal{A}$. Weak lower semicontinuity yields
\[
E(u)\ \le\ \liminf_{j\to\infty} E(u_{k_j}) \;=\; \inf_{\mathcal{A}}E,
\]
hence $u$ is a minimizer (the weakly harmonic extension of $g$).

\medskip
\noindent\textbf{3.\ Concrete 1D minimizer.}\par
\noindent
On $\Omega=(0,1)$ with boundary data $u(0)=0$, $u(1)=1$, the minimizer is $u(x)=x$, and
\[
E(u)=\int_0^1 |u'(x)|^{2}\,dx=\int_0^1 1\,dx=1.
\]
Any minimizing sequence $(u_k)$ has (up to subsequence) $u_k\rightharpoonup x$ in $H^{1}(0,1)$ and
$E(x)\le\liminf E(u_k)$.

	\subsection*{Why $f_n=\mathbf 1_{(n,n+1)} \rightharpoonup 0$ in $L^p(\mathbb R)$ for $1<p<\infty$}

	Let $p\in(1,\infty)$ and $p'$ be its H\"older conjugate. For any $h\in L^{p'}(\mathbb R)$,
	\[
	\int_{\mathbb R} f_n(x)\,h(x)\,dx=\int_{n}^{n+1} h(x)\,dx.
	\]
	Given $\varepsilon>0$, choose $R>0$ so large that
	\[
	\|h\|_{L^{p'}(\{|x|>R\})}<\varepsilon
	\qquad\text{(possible since $h\in L^{p'}$).}
	\]
	If $n>R$, then $(n,n+1)\subset\{|x|>R\}$ and, by H\"older,
	\[
	\Big|\int_{n}^{n+1} h(x)\,dx\Big|
	\le \|\mathbf 1_{(n,n+1)}\|_{L^p}\,\|h\|_{L^{p'}((n,n+1))}
	\le 1\cdot \|h\|_{L^{p'}(\{|x|>R\})}
	<\varepsilon.
	\]
	Hence $\int f_n h\to 0$ for every $h\in L^{p'}$, i.e.\ $f_n\rightharpoonup 0$ in $L^p$.

	\bigskip
	\noindent\textbf{Important caveat for $p=1$.}
	For $p=1$ the dual is $L^\infty$. The same argument does \emph{not} force
	$\int_{n}^{n+1} h \to 0$ for all $h\in L^\infty$ (one only gets $|\int_{n}^{n+1} h|\le \|h\|_\infty$).
	In fact, taking
	\[
	h(x)=\sum_{k\in\mathbb Z}(-1)^k\,\mathbf 1_{[k,k+1]}(x)\in L^\infty
	\]
	gives
	\[
	\int f_n h = (-1)^n,
	\]
	which does not converge. Therefore $f_n$ does \emph{not} converge weakly to $0$ in $L^1$.

	\bigskip
	\noindent\textbf{Summary.}
	\[
	\begin{aligned}
		&f_n \rightharpoonup 0 \quad \text{in } L^p(\mathbb R)\ \text{for } 1<p<\infty,\\[0.3em]
		&\text{not true in } L^1;\ \text{indeed, } (f_n)\ \text{has no weakly convergent subsequence in } L^1.
	\end{aligned}
	\]
```

## CP-II-0452

- chapter line: 19672

```tex
\label{prob:cp-ii-0452}
— Uniform limits: sums vs products

Let $(f_n)$ and $(g_n)$ be sequences of real-valued functions on a set $E$ converging uniformly to $f$ and $g$, respectively.

By the triangle inequality,
\[
\sup_{x\in E}\big|(f_n+g_n)-(f+g)\big|
\le \sup_{x\in E}|f_n-f|+\sup_{x\in E}|g_n-g|\xrightarrow[n\to\infty]{}0.
\]
Thus $f_n+g_n\to f+g$ uniformly on $E$.

Consider $E=\mathbb{R}$ and define $f_n(x)\equiv \frac1n$, $f(x)\equiv 0$, and $g_n(x)\equiv g(x)=x$. Then
\[
\sup_{x\in\mathbb{R}}|f_n(x)-f(x)|=\frac1n\to0,\qquad
\sup_{x\in\mathbb{R}}|g_n(x)-g(x)|=0,
\]
so $f_n\to f$ and $g_n\to g$ uniformly. However
\[
f_n(x)g_n(x)=\frac{x}{n},\qquad
\sup_{x\in\mathbb{R}}\Big|\frac{x}{n}-0\Big|=\infty,
\]
so $(f_ng_n)$ does not converge uniformly to $fg$ on $\mathbb{R}$ (even though it converges pointwise to $0$).

Suppose $|f|\le M$ and $|g|\le L$ on $E$. Since $g_n\to g$ uniformly, there exists $N_0$ such that for all $n\ge N_0$,
\[
\sup_{x\in E}|g_n(x)-g(x)|<1\quad\Rightarrow\quad
\sup_{x\in E}|g_n(x)|\le L+1.
\]
Then for $n\ge N_0$,
\[
\begin{aligned}
	\sup_{x\in E}|f_n(x)g_n(x)-f(x)g(x)|
	&\le \sup_{x\in E}|f_n(x)-f(x)|\,\sup_{x\in E}|g_n(x)|
	+ \sup_{x\in E}|f(x)|\,\sup_{x\in E}|g_n(x)-g(x)| \\
	&\le (L+1)\sup_{x\in E}|f_n-f| + M\sup_{x\in E}|g_n-g|\xrightarrow[n\to\infty]{}0.
\end{aligned}
\]
Hence $f_ng_n\to fg$ uniformly on $E$.

Uniform convergence of $(f_ng_n)$ to $fg$ need not hold. The example in (2) has bounded $f\equiv 0$, unbounded $g(x)=x$, uniform convergence $f_n\to f$ and $g_n\to g$, yet $(f_ng_n)$ fails to converge uniformly to $fg$.
```

## CP-II-0455

- chapter line: 19716

```tex
\label{prob:cp-ii-0455}
(Trace theorem on a hyperplane)

Assume $s>\tfrac12$ and suppose $u\in\mathcal S(\mathbb R^n)$.
Write $x=(x',x_n)\in\mathbb R^{n-1}\times\mathbb R$ and define the trace
\[
Tu(x') := u(x',0),\qquad x'\in\mathbb R^{n-1}.
\]

Show that for each $\xi'\in\mathbb R^{n-1}$ one has
\[
\widehat{Tu}(\xi') = \frac{1}{2\pi}\int_{\mathbb R}\widehat u(\xi',\xi_n)\,d\xi_n.
\]

Deduce that
\[
\bigl|\widehat{Tu}(\xi')\bigr|^2
\;\le\;
\frac{1}{(2\pi)^2}
\left(\int_{\mathbb R} (1+|\xi|^2)^s\,|\widehat u(\xi',\xi_n)|^2\,d\xi_n\right)
\left(\int_{\mathbb R}\frac{d\xi_n}{(1+|\xi|^2)^s}\right),
\]
where $\xi=(\xi',\xi_n)$.

By changing variables in the second integral above to
$\xi_n = t\sqrt{1+|\xi'|^2}$, show that there exists a constant $C(s)>0$
such that
\[
\|Tu\|_{H^{s-\frac12}(\mathbb R^{n-1})}
\;\le\; C(s)\,\|u\|_{H^s(\mathbb R^n)}.
\]

Conclude that $T$ extends uniquely by density to a bounded linear operator
\[
T:H^s(\mathbb R^n)\longrightarrow H^{s-\frac12}(\mathbb R^{n-1}),
\qquad s>\tfrac12.
\]

Suppose $\nu\in\mathcal S(\mathbb R^{n-1})$ and let $\phi\in C_c^\infty(\mathbb R)$ satisfy
\[
\int_{\mathbb R}\phi(t)\,dt = \sqrt{2\pi}.
\]
Define $u$ through its Fourier transform by
\[
\widehat u(\xi',\xi_n)
:= \frac{\widehat\nu(\xi')}{\sqrt{1+|\xi'|^2}}\,
\phi\!\left(\frac{\xi_n}{\sqrt{1+|\xi'|^2}}\right).
\]
Show that there exists a constant $C>0$ such that
\[
\|u\|_{H^s(\mathbb R^n)} \le C\,\|\nu\|_{H^{s-\frac12}(\mathbb R^{n-1})}.
\]
Compute $Tu$ and verify that $Tu=\nu$. Conclude that
\[
T:H^s(\mathbb R^n)\longrightarrow H^{s-\frac12}(\mathbb R^{n-1})
\]
is surjective and hence an isomorphism onto $H^{s-\frac12}(\mathbb R^{n-1})$.

\bigskip

For $s>\tfrac12$ the trace operator
\[
T:H^s(\mathbb R^n)\to H^{s-\frac12}(\mathbb R^{n-1}),
\qquad Tu(x')=u(x',0),
\]
is well defined, bounded and surjective. The proof above is based on the
Fourier identity in (a), the Cauchy--Schwarz estimate in (b),
and the estimate
\[
\int_{\mathbb R}\frac{d\xi_n}{(1+|\xi'|^2+\xi_n^2)^s}
= c_s\,(1+|\xi'|^2)^{\frac12-s},\qquad s>\tfrac12,
\]
which exactly produces the $H^{s-\frac12}$-weight in $\xi'$.
Part (e) constructs a bounded extension operator
$E:H^{s-\frac12}(\mathbb R^{n-1})\to H^s(\mathbb R^n)$ with $T\circ E=\mathrm{Id}$,
showing that every element of $H^{s-\frac12}(\mathbb R^{n-1})$ arises as a trace.
```

## CP-II-0456

- chapter line: 19795

```tex
\label{prob:cp-ii-0456}
\par\noindent\textbullet\quad \textbf{Tolerance–driven truncation.}
	Given $\varepsilon>0$, choose $n$ so that $S_n\le \varepsilon$. If $\gamma_j$ are unknown,
	estimate $S_n$ via
	\[
	S_n = \max_{0\le k\le 3^{n+1}} |f(x_k)-P_n(x_k)|.
	\]
```

## CP-II-0463

- chapter line: 19866

```tex
\label{prob:cp-ii-0463}
\par\noindent\textbullet\quad \emph{Absolute continuity:} $\nu\ll\mu$ means $\mu(A)=0 \Rightarrow \nu(A)=0$ for all $A\in\mathcal E$.
```

## CP-II-0465

- chapter line: 19871

```tex
\label{prob:cp-ii-0465}
Uniform convergence (Cauchy)

$f_n(x)=x/n$ on $[0,1]$. Limit $f(x)=0$.
Uniform convergence since $\|f_n-0\|_\infty=1/n \to 0$.

---
```

## CP-II-0470

- chapter line: 19881

```tex
\label{prob:cp-ii-0470}
— Separate continuity vs.\ joint continuity; Lipschitz criterion

\textbf{Statement.}\quad

Let $f:U\subset\mathbb{R}^2\to\mathbb{R}$ satisfy:
for each fixed $y$, $f(\cdot,y)$ is continuous; for each fixed $x$, $f(x,\cdot)$ is continuous.
 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad Give an example where $f$ is \emph{not} jointly continuous on $U$.
	\par\noindent\textbullet\quad Suppose there exist $L,M\ge0$ such that
	\[
	|f(x_1,y)-f(x_2,y)|\le L|x_1-x_2|, \qquad
	|f(x,y_1)-f(x,y_2)|\le M|y_1-y_2|
	\]
	for all relevant points in $U$ (constants independent of the other variable).
	Show that $f$ is jointly continuous on $U$.
	\par\noindent\textbullet\quad Deduce: if $D_1 f$ exists and is bounded on $U$, and $f(x,\cdot)$ is continuous for each fixed $x$,
	then $f$ is continuous on $U$.

\bigskip\hrule\bigskip

\textbf{Theory \& Solution.}\quad

\textbf{(1) Counterexample: separate $\not\Rightarrow$ joint).}\;
\[
f(x,y)=
\begin{cases}
	\dfrac{xy}{x^2+y^2}, & (x,y)\neq(0,0),\\[4pt]
	0,&(x,y)=(0,0).
\end{cases}
\]
For fixed $x$ or fixed $y$, $f\to 0$ at the origin; along $y=x$ we have $f(x,x)=\tfrac12$, so $f$ is not continuous at $(0,0)$.

\medskip

\textbf{(2) Uniform one–variable Lipschitz $\Rightarrow$ joint continuity).}\;
For $(x_1,y_1),(x_2,y_2)$,
\[
\begin{aligned}
	|f(x_1,y_1)-f(x_2,y_2)|
	&\le |f(x_1,y_1)-f(x_2,y_1)| + |f(x_2,y_1)-f(x_2,y_2)|\\
	&\le L|x_1-x_2| + M|y_1-y_2|,
\end{aligned}
\]
hence $f$ is globally Lipschitz on $U$ and therefore continuous.

\medskip

\textbf{(3) Bounded $D_1 f$ gives the needed uniform Lipschitz in $x$).}\;
If $|D_1 f|\le L$ on $U$ and $y$ is fixed, the 1D mean value theorem in $x$ yields
$|f(x_1,y)-f(x_2,y)|\le L|x_1-x_2|$ (constant independent of $y$).
Combine with continuity in $y$ and apply (2). \hfill$\square$

\bigskip\hrule\bigskip

\textbf{Examples.}\quad

 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad $f(x,y)=|x|\,\sin y$: here $D_1 f=\operatorname{sgn}(x)\sin y$ is bounded; $f(x,\cdot)$ is continuous. Conclusion: $f$ is continuous on $U$.
	\par\noindent\textbullet\quad The counterexample above shows separate continuity alone is insufficient.
```

## CP-II-0472

- chapter line: 19944

```tex
\label{prob:cp-ii-0472}
\par\noindent\textbullet\quad simple functions are finite linear combinations of indicator sets;
```

## CP-II-0474

- chapter line: 19949

```tex
\label{prob:cp-ii-0474}
\par\noindent\textbullet\quad Show that if $f\in C_c^3(\mathbb{R})$ is an odd function
	(i.e.\ $f(s)=-f(-s)$ for all $s$), then
	\[
	u(x,t) \equiv \frac{f(r+t)+f(r-t)}{2r}
	\]
	extends as a $C^2$ function which solves the wave equation on
	$S_T=(-T,T)\times\mathbb{R}^3$, with
	\[
	u(0,t) = f'(t).
	\]
```

## CP-II-0478

- chapter line: 19963

```tex
\label{prob:cp-ii-0478}
Integrals of vector-valued maps

Let $f:[0,1]\to\mathbb R^n$ be continuous and $\displaystyle \int_0^1 f:=\big(\int_0^1 f_1,\dots,\int_0^1 f_n\big)$.

	With $v=\int_0^1 f$ and the Euclidean dot product,
	\[
	\|v\|_2^2=v\cdot v=v\cdot \int_0^1 f=\int_0^1 v\cdot f(x)\,dx
	\le \int_0^1 \|v\|_2\,\|f(x)\|_2\,dx
	=\|v\|_2\int_0^1 \|f(x)\|_2\,dx,
	\]
	hence $\Big\|\int_0^1 f\Big\|_2 \le \int_0^1 \|f(x)\|_2\,dx$.

Equality
\[
\Bigl\|\!\int_{0}^{1} f \Bigr\| \;=\; \int_{0}^{1} \|f\|
\]
holding for \emph{every} norm on $\mathbb{R}^n$ occurs precisely when there exist
\[
u\in\mathbb{R}^n\setminus\{0\}
\quad\text{and}\quad
\alpha:[0,1]\to\mathbb{R}\ \text{of constant sign}
\]
such that
\[
f(x)=\alpha(x)\,u \qquad (x\in[0,1]).
\]

\noindent\textit{Sufficiency.}
If $f(x)=\alpha(x)u$ and $\alpha$ has constant sign, then for any norm $\|\cdot\|$,
\[
\Bigl\|\!\int_{0}^{1} f \Bigr\|
=\bigl\| (\int_{0}^{1}\alpha)\,u \bigr\|
= \bigl|\!\int_{0}^{1}\alpha \bigr|\,\|u\|
= \int_{0}^{1} |\alpha|\,\|u\|
= \int_{0}^{1} \|f\|.
\]

\noindent\textit{Necessity.}
Fix a strictly convex norm (e.g.\ Euclidean). Equality in the triangle inequality forces
$f(x)$ to be positively colinear a.e.; hence $f(x)=\alpha(x)u$ for some $u$ and scalar $\alpha$.
Requiring equality for \emph{every} norm rules out sign changes of $\alpha$, so $\alpha$ has
constant sign on $[0,1]$.
\medskip
```

## CP-II-0482

- chapter line: 20032

```tex
\label{prob:cp-ii-0482}
\par\noindent\textbullet\quad \textbf{Logarithmic rate.}
	For $\delta_n=\frac{1}{\log(n+2)}$,
	$\gamma_j=\frac{1}{\log(j+1)}-\frac{1}{\log(j+2)}$ and
	$E_n(f)\ge 1/\log(n+2)$.
```

## CP-II-0484

- chapter line: 20077

```tex
\label{prob:cp-ii-0484}
\par\noindent\textbullet\quad \textbf{Triangle inequality:}
	$\|p+q\|_{I}=\sup_{t\in I}|p(t)+q(t)|\le \sup_{t\in I}|p(t)|+\sup_{t\in I}|q(t)|=\|p\|_{I}+\|q\|_{I}$.

Hence $\|\cdot\|_{I}$ is a norm on $\mathcal{P}$.

\bigskip
\par\medskip\noindent\textbf{(b) Same sequence, two norms, two different limits.}\quad
Let
\[
K_1=[0,\tfrac12],\qquad K_2=[\tfrac12,1],
\]
and pick infinite sets $I\subset K_1$, $J\subset K_2$.

By Urysohn on $[0,1]$ choose $f\in C([0,1])$ with $f|_{K_1}\equiv0$ and $f|_{K_2}\equiv1$.
By Weierstrass there exist polynomials $p_n\in\mathcal{P}$ such that
\[
\|p_n-f\|_{[0,1]}:=\sup_{t\in[0,1]}|p_n(t)-f(t)| \xrightarrow[n\to\infty]{} 0.
\]

Then
\[
\|p_n-0\|_{I}=\sup_{t\in I}|p_n(t)|
\ \le\ \sup_{t\in K_1}|p_n(t)-f(t)|
\ \xrightarrow[n\to\infty]{}\ 0,
\]
so $p_n\to 0$ in $(\mathcal{P},\|\cdot\|_{I})$.

Similarly,
\[
\|p_n-1\|_{J}=\sup_{t\in J}|p_n(t)-1|
\ \le\ \sup_{t\in K_2}|p_n(t)-f(t)|
\ \xrightarrow[n\to\infty]{}\ 0,
\]
so $p_n\to 1$ in $(\mathcal{P},\|\cdot\|_{J})$.

\medskip
\noindent
Thus the \emph{same} sequence $(p_n)$ converges to \emph{different} elements (0 and 1) under two different norms on the same vector space $\mathcal{P}$.

\bigskip
\par\medskip\noindent\textbf{(c) Impossibility in $\ell^1,\ell^2$ and in $C([0,1])$ with standard norms.}\quad
No such example exists.
```

## CP-II-0486

- chapter line: 20123

```tex
\label{prob:cp-ii-0486}
\par\noindent\textbullet\quad The pair $(p,q)$ is fundamental: these are exactly the exponents
	for which Young's and Hölder's inequalities hold and for which the
	duality $(L^p)^* \cong L^q$ is valid.

\bigskip
```

## CP-II-0487

- chapter line: 20132

```tex
\label{prob:cp-ii-0487}
\par\noindent (b)\quad Use this to produce a vector space, a single sequence in it, and two different norms on it
	such that the sequence converges to \emph{different} elements of the space with respect to the two norms.
	(Hint: Weierstrass approximation.)
```

## CP-II-0488

- chapter line: 20139

```tex
\label{prob:cp-ii-0488}
{Polynomial step approximations on a half-disk and half-plane}{poly-step}
	(i) Show there exists a sequence of polynomials $(P_n)$ such that
	\[
	P_n(z)\longrightarrow
	\begin{cases}
		1,& |z|\le1,\ \Re z\ge0,\\
		0,& |z|\le1,\ \Re z<0,
	\end{cases}
	\quad\text{as }n\to\infty.
	\]
	(ii) Show there exists a sequence of polynomials $(Q_n)$ such that
	\[
	Q_n(z)\longrightarrow
	\begin{cases}
		1,& \Re z\ge0,\\
		0,& \Re z<0,
	\end{cases}
	\quad\text{as }n\to\infty.
	\]
```

## CP-II-0489

- chapter line: 20162

```tex
\label{prob:cp-ii-0489}
\par\noindent\textbullet\quad For complex-valued $F$, apply the inequality to $|F|$.
```
