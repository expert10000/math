# Part II missing-solution batch 09

- problems: **20**
- IDs: CP-II-0089, CP-II-0093, CP-II-0094, CP-II-0095, CP-II-0097, CP-II-0099, CP-II-0101, CP-II-0102, CP-II-0107, CP-II-0109, CP-II-0110, CP-II-0113, CP-II-0120, CP-II-0121, CP-II-0123, CP-II-0124, CP-II-0134, CP-II-0140, CP-II-0142, CP-II-0148

## CP-II-0089

- chapter line: 12737

```tex
\label{prob:cp-ii-0089}
\par\noindent\textbullet\quad \textbf{Exact uniform error.}
	For $P_n(x)=\sum_{j\le n}\gamma_j T_{3j}(x)$ with $\gamma_j\ge 0$,
	\[
	\|f-P_n\|_\infty = S_n:=\sum_{j>n}\gamma_j,
	\]
	and this value is attained at $x_k=\cos\!\big(\tfrac{k\pi}{3^{n+1}}\big)$.
```

## CP-II-0093

- chapter line: 12764

```tex
\label{prob:cp-ii-0093}
\par\noindent\textbullet\quad $F$ is \emph{lower semicontinuous (l.s.c.) at $x$} if
		$\displaystyle \liminf_{x'\to x} F(x') \ge F(x)$.
		Equivalently, each sublevel set $\{F\le \alpha\}$ is closed, or
		the epigraph $\operatorname{epi}F=\{(x,t):F(x)\le t\}$ is closed in $X\times\mathbb R$.
```

## CP-II-0094

- chapter line: 12772

```tex
\label{prob:cp-ii-0094}
Let $A\subset \mathbb{R}^n$ and $f,g:A\to\mathbb{R}$.

\renewcommand\labelenumi{(\alph{enumi})}
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

## CP-II-0095

- chapter line: 12806

```tex
\label{prob:cp-ii-0095}
\par\noindent\textbullet\quad \textbf{Strict inequality in weak l.s.c.} In a Hilbert space,
		let $(e_n)$ be an orthonormal sequence. Then $e_n\rightharpoonup 0$ but
		$\|0\|=0<\liminf_n\|e_n\|=1$.
```

## CP-II-0097

- chapter line: 12813

```tex
\label{prob:cp-ii-0097}
Let $f(x)=|x|^{-n/p}\mathbf{1}_{\{|x|\le 1\}}(x)$.
	Then for $\lambda>1$,
	\[
	\{|f|>\lambda\}=\{|x|<\lambda^{-p/n}\},\qquad
	\mu(\{|f|>\lambda\})=c_n\,\lambda^{-p}.
	\]
	Thus $f\in L^{p,\infty}(\mathbb{R}^n)$ with $\|f\|_{p,\infty}\sim c_n^{1/p}$,
	but $f\notin L^p(\mathbb{R}^n)$ since
	\[
	\int_{|x|\le1}|x|^{-n}\,dx=\infty.
	\]
	A tail variant $|x|^{-n/p}\mathbf{1}_{\{|x|\ge1\}}$
	is also in $L^{p,\infty}$ but not in $L^p$.
```

## CP-II-0099

- chapter line: 12830

```tex
\label{prob:cp-ii-0099}
Algebra and differentiation of regular distributions

\noindent
(a)\; Show that if $f_1,f_2\in C^0(\Omega)$ and $a\in C^\infty(\Omega)$, then
\[
aT_{f_1} + T_{f_2} = T_{a f_1 + f_2}.
\]

\medskip\noindent
(b)\; Show that if $f\in C^k(\Omega)$ then
\[
D^\alpha T_f = T_{D^\alpha f}
\qquad\text{for all multiindices }\alpha\text{ with }|\alpha|\le k.
\]
Deduce that $\iota\circ D^\alpha = D^\alpha\circ\iota$, where
$\iota:C^k(\Omega)\to\mathcal{D}'(\Omega)$ is the natural embedding
$f\mapsto T_f$.

\medskip\noindent
(c)\; Deduce that if $f\in C^k(\Omega)$ then
\[
\sum_{|\alpha|\le k} a_\alpha D^\alpha T_f = T_{Lf},
\]
where
\[
Lf := \sum_{|\alpha|\le k} a_\alpha D^\alpha f
\]
and $a_\alpha\in C^\infty(\Omega)$.

\bigskip

Let $f\in C^0(\Omega)$ and
\[
T_f(\varphi) := \int_\Omega f(x)\,\varphi(x)\,dx.
\]
For $a\in C^\infty(\Omega)$ and $T\in\mathcal{D}'(\Omega)$ define
$(aT)(\varphi):=T(a\varphi)$. For a multiindex $\alpha$,
\[
\langle D^\alpha T,\varphi\rangle
:= (-1)^{|\alpha|}\langle T,D^\alpha\varphi\rangle.
\]

If $f_1,f_2\in C^0(\Omega)$ and $a\in C^\infty(\Omega)$, show
\[
aT_{f_1} + T_{f_2} = T_{af_1+f_2}.
\]
```

## CP-II-0101

- chapter line: 12880

```tex
\label{prob:cp-ii-0101}
\par\noindent\textbullet\quad The set \((0.2,0.7]\) is \emph{not} open in \(X\)
		because the point \(0.7\) would need a right-hand neighborhood inside \(X\),
		which does not exist.
```

## CP-II-0102

- chapter line: 12887

```tex
\label{prob:cp-ii-0102}
— Weak-* limits of $\sin(nx)$ and $\sin^2(nx)$

Recall that $L^\infty(\mathbb R)=(L^1(\mathbb R))'$. Consider the sequence $(f_n)_{n\ge1}\subset L^\infty(\mathbb R)$ given by
\[
f_n(x)=\sin(nx).
\]
Show that $f_n \stackrel{*}{\rightharpoonup} 0$ in $L^\infty(\mathbb R)$.
Show further that $f_n^2 \stackrel{*}{\rightharpoonup} g$ for some $g\in L^\infty(\mathbb R)$, and determine $g$.

Identify $L^\infty(\mathbb R)$ with $(L^1(\mathbb R))'$ via the pairing
$\langle g,\varphi\rangle=\int_{\mathbb R} g(x)\,\varphi(x)\,dx$ for $\varphi\in L^1$.
Let $f_n(x)=\sin(nx)$.

\smallskip

\par\medskip\noindent\textbf{(a) $f_n \overset{*}\rightharpoonup 0$.}\quad
For any $\varphi\in L^1(\mathbb R)$,
\[
\int_{\mathbb R}\sin(nx)\,\varphi(x)\,dx \xrightarrow[n\to\infty]{} 0
\]
by the Riemann--Lebesgue lemma. Hence $f_n \overset{*}\rightharpoonup 0$ in $L^\infty$.

\smallskip

\par\medskip\noindent\textbf{(b) $f_n^2 \overset{*}\rightharpoonup \tfrac12$.}\quad
Using $\sin^2(nx)=\frac12(1-\cos(2nx))$,
\[
\int \sin^2(nx)\,\varphi
= \frac12\int \varphi - \frac12\int \varphi(x)\cos(2nx)\,dx
\longrightarrow \frac12\int \varphi(x)\,dx.
\]
Therefore $f_n^2 \overset{*}\rightharpoonup g$ with $g(x)\equiv \frac12$ in $L^\infty(\mathbb R)$.

\bigskip
\bigskip
```

## CP-II-0107

- chapter line: 13085

```tex
\label{prob:cp-ii-0107}
{Powers preserve uniform convergence (under a bound).}{powers-uniform}
	Let $f_n:[0,1]\to\mathbb R$ converge uniformly to $f$. Suppose $f$ is bounded.
	Show that for every positive integer $m$,
	\[
	g_n(t):=f_n(t)^m \quad\text{converges uniformly on }[0,1]\text{ to }\quad
	g(t):=f(t)^m.
	\]
```

## CP-II-0109

- chapter line: 13096

```tex
\label{prob:cp-ii-0109}
Which functions are (i) continuous, (ii) uniformly continuous on their domains?

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad $f:\mathbb{R}\to\mathbb{R}$, $x\mapsto e^x$: continuous, not uniformly continuous.
\par\noindent\textbullet\quad $f:(0,1)\to\mathbb{R}$, $x\mapsto e^x$: continuous, uniformly continuous (MVT and $e^c\le e$).
\par\noindent\textbullet\quad $f:\mathbb{R}\to\mathbb{R}$, $x\mapsto\sin x$: continuous, uniformly continuous ($|\sin x-\sin y|\le |x-y|$).
\par\noindent\textbullet\quad $f:[0,\infty)\to\mathbb{R}$, $x\mapsto \sqrt{x}$: continuous, uniformly continuous ($|\sqrt{x}-\sqrt{y}|\le \sqrt{|x-y|}$).
\par\noindent \textit{f)}\quad $f:\mathbb{R}^n\setminus\{0\}\to\mathbb{R}^n$, $x\mapsto x/\|x\|$: continuous, not uniformly continuous (fails near $0$).
```

## CP-II-0110

- chapter line: 13108

```tex
\label{prob:cp-ii-0110}
(solutions)

Let $s>\tfrac12$ and $u\in\mathcal S(\mathbb R^n)$, $x=(x',x_n)$, $\xi=(\xi',\xi_n)$.

We have
\[
\widehat{Tu}(\xi')
= \int_{\mathbb R^{n-1}} e^{-ix'\cdot\xi'}u(x',0)\,dx'.
\]
Using the inverse Fourier representation of $u$,
\[
u(x',0)
= \frac{1}{(2\pi)^n}\int_{\mathbb R^{n-1}}\!\int_{\mathbb R}
e^{i(x'\cdot\eta'+0\cdot\eta_n)}\widehat u(\eta',\eta_n)\,d\eta_n d\eta',
\]
we obtain
\[
\widehat{Tu}(\xi')
= \frac{1}{(2\pi)^n}\int_{\mathbb R^{n-1}}\!\int_{\mathbb R}
\left(\int_{\mathbb R^{n-1}} e^{-ix'\cdot\xi'}e^{ix'\cdot\eta'}dx'\right)
\widehat u(\eta',\eta_n)\,d\eta_n d\eta'.
\]
The inner integral equals $(2\pi)^{n-1}\delta(\eta'-\xi')$, hence
\[
\widehat{Tu}(\xi') = \frac{1}{2\pi}\int_{\mathbb R}\widehat u(\xi',\xi_n)\,d\xi_n.
\]

From (a),
\[
\widehat{Tu}(\xi')
= \frac{1}{2\pi}\int_{\mathbb R}
(1+|\xi|^2)^{\frac{s}{2}}\widehat u(\xi',\xi_n)\,
(1+|\xi|^2)^{-\frac{s}{2}}\,d\xi_n.
\]
By the Cauchy--Schwarz inequality,
\[
\bigl|\widehat{Tu}(\xi')\bigr|^2
\le \frac{1}{(2\pi)^2}
\left(\int_{\mathbb R}(1+|\xi|^2)^s |\widehat u(\xi',\xi_n)|^2 d\xi_n\right)
\left(\int_{\mathbb R}\frac{d\xi_n}{(1+|\xi|^2)^s}\right).
\]

Set
\[
I(\xi'):=\int_{\mathbb R}\frac{d\xi_n}{(1+|\xi'|^2+\xi_n^2)^s}.
\]
With $L=\sqrt{1+|\xi'|^2}$ and $\xi_n=Lt$,
\[
I(\xi')=L^{1-2s}\int_{\mathbb R}\frac{dt}{(1+t^2)^s}
= C_s(1+|\xi'|^2)^{\frac12-s},
\]
where $C_s<\infty$ for $s>\tfrac12$. Using (b),
\[
\begin{aligned}
	\|Tu\|_{H^{s-\frac12}(\mathbb R^{n-1})}^2
	&= \int_{\mathbb R^{n-1}}(1+|\xi'|^2)^{s-\frac12}|\widehat{Tu}(\xi')|^2\,d\xi'\\
	&\le \frac{1}{(2\pi)^2}\int_{\mathbb R^{n-1}}(1+|\xi'|^2)^{s-\frac12}
	\left(\int_{\mathbb R}(1+|\xi|^2)^s|\widehat u(\xi',\xi_n)|^2 d\xi_n\right) I(\xi')\,d\xi'\\
	&= \frac{C_s}{(2\pi)^2}\iint_{\mathbb R^{n-1}\times\mathbb R}(1+|\xi|^2)^s
	|\widehat u(\xi',\xi_n)|^2 d\xi_n d\xi' \\
	&= C(s)\,\|u\|_{H^s(\mathbb R^n)}^2.
\end{aligned}
\]
Thus $\|Tu\|_{H^{s-\frac12}}\le C(s)\|u\|_{H^s}$.

The map $T:\mathcal S(\mathbb R^n)\to H^{s-\frac12}(\mathbb R^{n-1})$ is bounded by (c).
Since $\mathcal S(\mathbb R^n)$ is dense in $H^s(\mathbb R^n)$, $T$ extends uniquely by continuity to a bounded linear operator
\[
T:H^s(\mathbb R^n)\longrightarrow H^{s-\frac12}(\mathbb R^{n-1}),\quad s>\tfrac12.
\]

Let $\nu\in\mathcal S(\mathbb R^{n-1})$ and $\phi\in C_c^\infty(\mathbb R)$ satisfy
$\int_{\mathbb R}\phi(t)dt=\sqrt{2\pi}$. Define
\[
\widehat u(\xi',\xi_n)
:=\frac{\widehat\nu(\xi')}{\sqrt{1+|\xi'|^2}}\,
\phi\!\left(\frac{\xi_n}{\sqrt{1+|\xi'|^2}}\right).
\]
Then
\[
\begin{aligned}
	\|u\|_{H^s(\mathbb R^n)}^2
	&= \iint_{\mathbb R^{n-1}\times\mathbb R}
	(1+|\xi|^2)^s |\widehat u(\xi',\xi_n)|^2\,d\xi_n d\xi'\\
	&= \int_{\mathbb R^{n-1}} \frac{|\widehat\nu(\xi')|^2}{1+|\xi'|^2}
	\left(\int_{\mathbb R}(1+|\xi'|^2+\xi_n^2)^s
	\Bigl|\phi\!\Bigl(\frac{\xi_n}{\sqrt{1+|\xi'|^2}}\Bigr)\Bigr|^2 d\xi_n\right)d\xi'.
\end{aligned}
\]
With $L=\sqrt{1+|\xi'|^2}$ and $\xi_n=Lt$,
\[
\int_{\mathbb R}(1+|\xi'|^2+\xi_n^2)^s
\Bigl|\phi\!\Bigl(\frac{\xi_n}{L}\Bigr)\Bigr|^2 d\xi_n
= L^{2s+1}\int_{\mathbb R}(1+t^2)^s|\phi(t)|^2 dt
\le C_\phi (1+|\xi'|^2)^{s+\frac12},
\]
where $C_\phi:=\int_{\mathbb R}(1+t^2)^s|\phi(t)|^2dt$.
Hence
\[
\|u\|_{H^s(\mathbb R^n)}^2
\le C_\phi \int_{\mathbb R^{n-1}}|\widehat\nu(\xi')|^2(1+|\xi'|^2)^{s-\frac12}d\xi'
= C_\phi\,\|\nu\|_{H^{s-\frac12}(\mathbb R^{n-1})}^2.
\]

Using (a),
\[
\widehat{Tu}(\xi')
= \frac{1}{2\pi}\int_{\mathbb R}\widehat u(\xi',\xi_n)\,d\xi_n
= \frac{\widehat\nu(\xi')}{2\pi\sqrt{1+|\xi'|^2}}
\int_{\mathbb R}\phi\!\left(\frac{\xi_n}{\sqrt{1+|\xi'|^2}}\right)d\xi_n.
\]
With $\xi_n=Lt$, $L=\sqrt{1+|\xi'|^2}$,
\[
\int_{\mathbb R}\phi\!\left(\frac{\xi_n}{L}\right)d\xi_n
= L\int_{\mathbb R}\phi(t)dt = L\sqrt{2\pi}.
\]
Thus
\[
\widehat{Tu}(\xi') = \frac{\widehat\nu(\xi')}{2\pi\sqrt{1+|\xi'|^2}}L\sqrt{2\pi}
= \widehat\nu(\xi'),
\]
so $Tu=\nu$.
By density, this defines a bounded extension operator
$E:H^{s-\frac12}(\mathbb R^{n-1})\to H^s(\mathbb R^n)$ with $T\circ E = \mathrm{Id}$.
Therefore $T:H^s(\mathbb R^n)\to H^{s-\frac12}(\mathbb R^{n-1})$ is surjective.
```

## CP-II-0113

- chapter line: 13238

```tex
\label{prob:cp-ii-0113}
\par\noindent\textbullet\quad \textbf{Absolutely continuous:}
		If $f\in L^1(m)$ on $\mathbb R^n$ and $\nu(A)=\int_A f\,dm$, then $\nu\ll m$.
		Moreover, for every $\varepsilon>0$ there exists $\delta>0$ such that
		$\mu(A)<\delta\Rightarrow \nu(A)<\varepsilon$.
```

## CP-II-0120

- chapter line: 13556

```tex
\label{prob:cp-ii-0120}
Probability (sum of random variables).

Let $f$ be the density of a random variable $X$ and $g$ the density of an
independent random variable $Y$. Then the density of $X+Y$ is $f*g$:
\[
(f*g)(x)
= \int_{\mathbb{R}} f(x-y)\,g(y)\,dy.
\]

\medskip
\noindent$\Rightarrow$ \emph{Effect:} convolution describes the law of
sums of independent random variables.

\clearpage
```

## CP-II-0121

- chapter line: 13574

```tex
\label{prob:cp-ii-0121}
\par\noindent\textbullet\quad More generally, for the Dirac mass at $a\in\mathbb{R}^n$,
	\[
	(\delta_a*\phi)(x)
	= \langle\delta_a,\phi(x-\cdot)\rangle
	= \phi(x-a).
	\]
```

## CP-II-0123

- chapter line: 13584

```tex
\label{prob:cp-ii-0123}
\par\noindent\textbullet\quad $f(x)=x^3$ on $\mathbb{R}$: $Df(x)=3x^2$, invertible for $x\ne0$.
	Locally invertible near $x=1$ with inverse $f^{-1}(y)=y^{1/3}$.
```

## CP-II-0124

- chapter line: 13590

```tex
\label{prob:cp-ii-0124}
\par\noindent (a)\quad Show that $\|\cdot\|_{I}$ is a norm on $\mathcal{P}$.
```

## CP-II-0134

- chapter line: 13712

```tex
\label{prob:cp-ii-0134}
\par\noindent\textbullet\quad The classical Minkowski inequality
	\[
	\|f+g\|_{L^p}
	\le
	\|f\|_{L^p} + \|g\|_{L^p}
	\]
	is the triangle inequality for the $L^p$--norm.  Hölder's inequality
	is the main tool in its proof.
```

## CP-II-0140

- chapter line: 13724

```tex
\label{prob:cp-ii-0140}
\par\noindent\textbullet\quad If $y\in B_1(x_0,r)$, then $\|y-x_0\|_1 < r$.
	Hence $\|y-x_0\|_2 < br$, so $y\in B_2(x_0,br)$.
	Thus $B_1(x_0,r)\subseteq B_2(x_0,br)$.
```

## CP-II-0142

- chapter line: 13807

```tex
\label{prob:cp-ii-0142}
\par\noindent\textbullet\quad If $\|f\|_{L^p}=\|g\|_{L^q}=1$, the right side equals $1$.
```

## CP-II-0148

- chapter line: 13852

```tex
\label{prob:cp-ii-0148}
\par\noindent\textbullet\quad $\operatorname{supp}\phi \subset B(0,1)$,
```
