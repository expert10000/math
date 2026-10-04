# Part II missing-solution batch 12

- problems: **20**
- IDs: CP-II-0228, CP-II-0231, CP-II-0232, CP-II-0233, CP-II-0234, CP-II-0235, CP-II-0236, CP-II-0239, CP-II-0240, CP-II-0241, CP-II-0243, CP-II-0244, CP-II-0245, CP-II-0246, CP-II-0247, CP-II-0248, CP-II-0255, CP-II-0258, CP-II-0259, CP-II-0261

## CP-II-0228

- chapter line: 15394

```tex
\label{prob:cp-ii-0228}
\par\noindent\textbullet\quad For general nonnegative measurable $F$, approximate $F$ from below
	by simple functions and use the Monotone Convergence Theorem.
```

## CP-II-0231

- chapter line: 15400

```tex
\label{prob:cp-ii-0231}
\par\noindent\textbullet\quad More generally, for any polynomial $P$ we have
	$P(x)e^{-|x|^2}\in\mathcal{S}(\mathbb{R}^n)$.
```

## CP-II-0232

- chapter line: 15406

```tex
\label{prob:cp-ii-0232}
Let $A\subset \mathbb{R}^n$ and $f,g:A\to\mathbb{R}$.

\par\noindent\textbullet\quad Suppose $f$ and $g$ are uniformly continuous and bounded on $A$. Then $fg$ is uniformly continuous and bounded on $A$.

\textit{Solution (boundedness).} If $|f|\le M_f$ and $|g|\le M_g$ on $A$, then $|fg|\le M_fM_g$.

\textit{Solution (uniform continuity).} Fix $\varepsilon>0$ and set
$\eta=\min\!\left(1,\frac{\varepsilon}{2(M_f+M_g+1)}\right)$.
By uniform continuity of $f$ and $g$, there exists $\delta>0$ such that
$\|x-y\|<\delta$ implies $|f(x)-f(y)|<\eta$ and $|g(x)-g(y)|<\eta$.
Then for such $x,y$,
\begin{align*}
|f(x)g(x)-f(y)g(y)|
&= |[f(x)-f(y)][g(x)-g(y)] + g(y)[f(x)-f(y)] + f(y)[g(x)-g(y)]|\\
&\le \eta^2 + M_g\,\eta + M_f\,\eta
\;\le\; (M_f+M_g+1)\eta \;\le\; \varepsilon.
\end{align*}
Hence $fg$ is uniformly continuous.

\par\noindent\textbullet\quad If $f$ and $g$ are uniformly continuous but not necessarily bounded, $fg$ need not be uniformly continuous.

\textit{Counterexample.} On $\mathbb{R}$, take $f(x)=x$ and $g(x)=\sin x$. Both are uniformly continuous (Lipschitz).
Assume $x\sin x$ were uniformly continuous. For $\varepsilon=1$, let $\delta>0$ be its modulus.
Set $t=\min(\delta/2,1)$ and take $y_k=k\pi$, $x_k=k\pi+t$.
Then $|x_k-y_k|=t<\delta$ but
\[
|x_k\sin x_k - y_k\sin y_k| = |(k\pi+t)\sin t| \ge k\pi \sin t \xrightarrow{k\to\infty} \infty,
\]
contradicting uniform continuity. Thus $x\sin x$ is not uniformly continuous.
```

## CP-II-0233

- chapter line: 15439

```tex
\label{prob:cp-ii-0233}
(Diagonal).

$A=\begin{pmatrix}3&0\\0&1\end{pmatrix}$ has $p_A(\lambda)=(\lambda-3)(\lambda-1)$, eigenvectors $e_1$ for $\lambda=3$ and $e_2$ for $\lambda=1$. Here $m_a=m_g=1$ for each eigenvalue, so $A$ is diagonalizable.
```

## CP-II-0234

- chapter line: 15446

```tex
\label{prob:cp-ii-0234}
\par\noindent\textbullet\quad \emph{Mutual singularity:} $\nu\perp\mu$ means there is $S\in\mathcal E$ with $\mu(S)=0$ and $\nu(E\setminus S)=0$.
```

## CP-II-0235

- chapter line: 15451

```tex
\label{prob:cp-ii-0235}
\par\noindent\textbullet\quad Let $\eta \in \mathscr{S}(\mathbb{R}^n)$ satisfy
	\[
	\int_{\mathbb{R}^n} \eta(x)\,dx = 1,
	\]
	and define the mollifiers
	\[
	\eta_\varepsilon(x) := \varepsilon^{-n}\eta\!\left(\frac{x}{\varepsilon}\right),
	\qquad \varepsilon>0.
	\]
	Show that for every $f \in H^{s}(\mathbb{R}^n)$ one has
	\[
	\eta_\varepsilon * f \longrightarrow f
	\quad\text{in } H^{s}(\mathbb{R}^n)
	\quad\text{as } \varepsilon\to 0.
	\]
```

## CP-II-0236

- chapter line: 15470

```tex
\label{prob:cp-ii-0236}
\par\noindent\textbullet\quad The key idea is to define
	\[
	u(x) := \int_{\mathbb{R}^n} F(x,y)\,dy,
	\qquad
	G(y) := |u(y)|^{p-1}\operatorname{sgn}(u(y)),
	\]
	so that
	\[
	\|u\|_{L^p}^p = \int_{\mathbb{R}^n} u(x) G(x)\,dx.
	\]
```

## CP-II-0239

- chapter line: 15548

```tex
\label{prob:cp-ii-0239}
Suppose $A\subset\mathbb{R}^n$ and let $(f_i)_{i=0}^\infty$ with $f_i:A\to\mathbb{R}^m$ be a sequence of functions.
Assume $f_i\to f$ \emph{uniformly} on $A$. Show that if $B\subset A$, then $f_i\to f$ uniformly on $B$.

\textit{Solution.} By uniform convergence on $A$, for every $\varepsilon>0$ there exists $N\in\mathbb{N}$ such that
for all $i\ge N$ and all $x\in A$ we have $\|f_i(x)-f(x)\|<\varepsilon$. Since $B\subset A$, this inequality holds
for all $x\in B$ as well, with the \emph{same} $N$. Hence $f_i\to f$ uniformly on $B$. Equivalently,
\[
\sup_{x\in B}\|f_i(x)-f(x)\|\le \sup_{x\in A}\|f_i(x)-f(x)\|\xrightarrow{i\to\infty} 0.
\]
```

## CP-II-0240

- chapter line: 15561

```tex
\label{prob:cp-ii-0240}
\par\noindent\textbullet\quad Conclude that
		\[
		\widehat{K_t}(\xi) = e^{-it|\xi|^2}.
		\]
```

## CP-II-0241

- chapter line: 15569

```tex
\label{prob:cp-ii-0241}
Suppose $A\subset\mathbb{R}^n$ and let $(f_i)_{i=0}^\infty$ with $f_i:A\to\mathbb{R}^m$.
Classify whether each statement is equivalent to (i) pointwise convergence $f_i\to f$,
(ii) uniform convergence $f_i\to f$ uniformly, or (iii) neither.

\renewcommand\labelenumi{(\alph{enumi})}

\par\noindent\textbullet\quad Given $\varepsilon>0$, there exists $N\in\mathbb{N}$ such that for all $i\ge N$:
\[
\sup_{x\in A}\|f_i(x)-f(x)\|<\varepsilon.
\]
\textit{Classification: (ii) uniform convergence.} This is exactly the definition via the sup norm.

\par\noindent\textbullet\quad For all $x\in A$, for all $i\in\mathbb{N}$ there exists $\varepsilon>0$ such that
\[
\|f_i(x)-f(x)\|<\varepsilon.
\]
\textit{Classification: (iii) neither.} The statement is always true (take, e.g., $\varepsilon=\|f_i(x)-f(x)\|+1$), so it does not characterize convergence.

\par\noindent\textbullet\quad There exists $N\in\mathbb{N}$ such that for all $x\in A$, $i\ge N$, $\varepsilon>0$:
\[
\|f_i(x)-f(x)\|<\varepsilon.
\]
\textit{Classification: (iii) neither.} Since the left-hand side is nonnegative, the inequality for \emph{all} $\varepsilon>0$ forces $\|f_i(x)-f(x)\|=0$; i.e.\ there is $N$ with $f_i\equiv f$ on $A$ for all $i\ge N$. This condition is much stronger than uniform convergence and is not equivalent to it in general.

\par\noindent \textit{*}d)\quad $\forall\varepsilon>0\ \forall x\in A\ \exists N\in\mathbb{N}\ \forall i\ge N:\ \|f_i(x)-f(x)\|<\varepsilon$.\\
\textit{Classification: (i) pointwise convergence.} The quantifier order matches the definition; $N$ may depend on $x$ and $\varepsilon$.

\par\noindent \textit{*}e)\quad $\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall x\in A\ \forall i\ge N:\ \|f_i(x)-f(x)\|<\varepsilon$.\\
\textit{Classification: (ii) uniform convergence.} Here $N$ works simultaneously for all $x\in A$.

\par\noindent \textit{*}f)\quad $\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall x\in A:\ (\,i\ge N\ \Leftrightarrow\ \|f_i(x)-f(x)\|<\varepsilon\,)$.\\
\textit{Classification: (iii) neither.} This is far stronger than uniform convergence (it also demands that for $i<N$ the error is $\ge\varepsilon$ for every $x$), and it need not hold even when $f_i\to f$ uniformly.
```

## CP-II-0243

- chapter line: 15605

```tex
\label{prob:cp-ii-0243}
\par\noindent\textbullet\quad \textbf{Indicators.} For a set $C\subset X$, the indicator
		$I_C(x)=0$ if $x\in C$ and $+\infty$ otherwise is l.s.c.\ iff $C$ is closed;
		u.s.c.\ iff $C$ is open.
```

## CP-II-0244

- chapter line: 15612

```tex
\label{prob:cp-ii-0244}
\par\noindent\textbullet\quad Set $t = p^{-1}$ and consider the function
	\[
	\varphi(t) = \log\bigl[t a^p + (1-t)b^q\bigr].
	\]
	Because $\log$ is concave, Jensen's inequality yields
	\[
	\log\bigl[t a^p + (1-t)b^q\bigr]
	\;\ge\; t\log(a^p) + (1-t)\log(b^q)
	= p\,t\log a + q(1-t)\log b.
	\]
	Choosing $t=1/p$ (so $1-t=1/q$) gives
	\[
	\log\!\left(\frac{a^p}{p} + \frac{b^q}{q}\right)
	\;\ge\; \log a + \log b = \log(ab),
	\]
	which is precisely Young's inequality.

Let
\[
\Phi(x) = \frac{x^p}{p}, \qquad x\ge 0.
\]
Then $\Phi$ is convex and its Legendre transform (convex conjugate) is
\[
\Phi^*(y)
= \sup_{x\ge0}\bigl(xy - \Phi(x)\bigr)
= \frac{y^q}{q}, \qquad y\ge0,
\]
where $q$ is the Hölder conjugate of $p$, i.e.\ $\frac1p+\frac1q=1$.
The Fenchel--Young inequality asserts that
\[
xy \le \Phi(x) + \Phi^*(y), \qquad x,y\ge0.
\]
Substituting $\Phi(x)=x^p/p$ and $\Phi^*(y)=y^q/q$ yields
\[
xy \le \frac{x^p}{p} + \frac{y^q}{q},
\]
which is Young's inequality (with $x=a$, $y=b$).  Thus Young's
inequality expresses the Legendre duality between the functions
$x\mapsto x^p/p$ and $y\mapsto y^q/q$.

\bigskip
```

## CP-II-0245

- chapter line: 15657

```tex
\label{prob:cp-ii-0245}
\par\noindent\textbullet\quad For $t>0$, define $K_\varepsilon \in L^1_{\mathrm{loc}}(\mathbb{R}^n)$ by
	\[
	K_\varepsilon(x)
	= \frac{1}{(4\pi i t)^{n/2}} \, e^{\, i|x|^2 / 4t },
	\]
	where for $n$ odd we take the usual branch cut so that $i^{1/2}=e^{i\pi/4}$.
	For $\varepsilon>0$ set
	\[
	K_\varepsilon^t(x) = e^{-\varepsilon|x|^2}\, K_t(x).
	\]
```

## CP-II-0246

- chapter line: 15671

```tex
\label{prob:cp-ii-0246}
$f_n(x)=\sin(nx)/n$ on $[0,2\pi]$ (Equicontinuous, converges uniformly to 0)

---
```

## CP-II-0247

- chapter line: 15678

```tex
\label{prob:cp-ii-0247}
\par\noindent\textbullet\quad $f=\mathbf 1_{[0,1]}$. Then $F(x)=0$ for $x<0$, $F(x)=x$ on $[0,1]$, $F(x)=1$ for $x>1$.
	$F'(x)=1$ on $(0,1)$ and $0$ elsewhere; $x=0,1$ are the only non-Lebesgue points for $f$.
```

## CP-II-0248

- chapter line: 15684

```tex
\label{prob:cp-ii-0248}
\par\noindent\textbullet\quad Applying Hölder's inequality to the right-hand side gives
	\[
	\|u\|_{L^p}^p
	\le
	\|G\|_{L^q}
	\int_{\mathbb{R}^n}
	\left(
	\int_{\mathbb{R}^n} |F(x,y)|^p \, dx
	\right)^{1/p} dy,
	\]
	from which Minkowski's integral inequality follows.

\bigskip
```

## CP-II-0255

- chapter line: 15896

```tex
\label{prob:cp-ii-0255}
$f_n(x)=x^n$ on $[0,1]$ (Not equicontinuous)

---
```

## CP-II-0258

- chapter line: 15938

```tex
\label{prob:cp-ii-0258}
Trigonometric example.

On $[0,\pi]$ let
\[
F(x,y) = \sin^2 x\,\sin^2 y.
\]
Since $\displaystyle \int_0^\pi \sin^2 t\,dt = \frac{\pi}{2}$,
\[
\int_0^\pi \Bigl|\int_0^\pi F(x,y)\,dy\Bigr|dx
= \frac{\pi^2}{4}
= \int_0^\pi\int_0^\pi F(x,y)\,dy\,dx.
\]

These examples illustrate how regular, smooth functions behave exactly
like simple functions when $p=1$ and $F\ge 0$: the inequality becomes an
equality.
```

## CP-II-0259

- chapter line: 15958

```tex
\label{prob:cp-ii-0259}
(Smooth bump in all $H^s$).

Let $b(x)=e^{-1/(1-x^2)}$ for $|x|<1$ and $b=0$ otherwise.
Then $b\in C_c^\infty(\mathbb R)$ and for every $N$,
$|\widehat b(\xi)|\le C_N(1+|\xi|)^{-N}$. Hence
$\|b\|_{H^s}<\infty$ for all $s\in\mathbb R$.

\clearpage
```

## CP-II-0261

- chapter line: 15970

```tex
\label{prob:cp-ii-0261}
\par\noindent\textbullet\quad \textbf{Dirichlet energy.} On $H^1(\Omega)$,
		$E(u)=\int_\Omega |\nabla u|^2\,dx$ is weakly l.s.c.; hence minimizing sequences
		have weakly convergent subsequences with $E$-limit $\ge$ the value at the weak limit
		(direct method of the calculus of variations).
```
