# Part II missing-solution batch 08

- problems: **20**
- IDs: CP-II-0042, CP-II-0045, CP-II-0046, CP-II-0049, CP-II-0050, CP-II-0051, CP-II-0053, CP-II-0054, CP-II-0056, CP-II-0058, CP-II-0060, CP-II-0065, CP-II-0067, CP-II-0068, CP-II-0074, CP-II-0078, CP-II-0079, CP-II-0081, CP-II-0084, CP-II-0087

## CP-II-0042

- chapter line: 12088

```tex
\label{prob:cp-ii-0042}
(Defective).

$A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ has $p_A(\lambda)=(\lambda-1)^2$. The eigenspace is $\ker(A-I)=\mathrm{span}\{(1,0)^\top\}$, so $m_a(1)=2$ but $m_g(1)=1$; $A$ is not diagonalizable and is already a Jordan block.
```

## CP-II-0045

- chapter line: 12171

```tex
\label{prob:cp-ii-0045}
\par\noindent\textbullet\quad For every multi-index $\alpha$ and every $1\le p<\infty$,
	\[
	D^\alpha f\in L^p(\mathbb{R}^n).
	\]
	Indeed, for each $N$ we have
	$|D^\alpha f(x)|\le C_{\alpha,N}(1+|x|)^{-N}$, and choosing
	$N$ with $Np>n$ gives $|D^\alpha f|^p\in L^1$.
```

## CP-II-0046

- chapter line: 12182

```tex
\label{prob:cp-ii-0046}
\par\noindent\textbullet\quad Parts (a)--(d) assume $F$ is a \emph{positive simple function}:
	a finite linear combination of characteristic functions.
	On these, one may freely permute and decompose integrals.
```

## CP-II-0049

- chapter line: 12189

```tex
\label{prob:cp-ii-0049}
\par\noindent (a)\quad Show $\displaystyle \int_{\mathbb{R}}\psi_{n_1,k_1}\psi_{n_2,k_2}=\delta_{n_1n_2}\delta_{k_1k_2}$.
```

## CP-II-0050

- chapter line: 12194

```tex
\label{prob:cp-ii-0050}
\par\noindent\textbullet\quad $f(x,y)=(e^x\cos y,\,e^x\sin y)$ on $\mathbb{R}^2$:
	$\det Df(x,y)=e^{2x}\ne0$, hence locally invertible at every point.

\hfill$\Box$
```

## CP-II-0051

- chapter line: 12202

```tex
\label{prob:cp-ii-0051}
— Powers preserve uniform convergence

Let $f_n:[0,1]\to\mathbb{R}$ satisfy $f_n\to f$ uniformly on $[0,1]$, and suppose $f$ is bounded.
Show that for any integer $m\ge1$, the functions $g_n(t)=f_n(t)^m$ converge uniformly on $[0,1]$
to $g(t)=f(t)^m$.

For all $a,b\in\mathbb{R}$ and $m\ge1$,
\[
a^m-b^m=(a-b)\sum_{k=0}^{m-1}a^{m-1-k}b^{k},
\]
hence if $|a|,|b|\le M$ then $|a^m-b^m|\le m M^{m-1}|a-b|$.
Uniform convergence $f_n\to f$ implies $\|f_n-f\|_\infty\to0$.

Let $M=\|f\|_\infty<\infty$. Since $f_n\to f$ uniformly, there exists $N$ with
$\|f_n-f\|_\infty\le 1$ for all $n\ge N$. Then for $n\ge N$,
\[
\|f_n\|_\infty \le \|f\|_\infty+\|f_n-f\|_\infty \le M+1=:M'.
\]
For any $t\in[0,1]$,
\[
|f_n(t)^m-f(t)^m|
\le |f_n(t)-f(t)| \sum_{k=0}^{m-1} |f_n(t)|^{m-1-k} |f(t)|^{k}
\le m(M')^{m-1}\,|f_n(t)-f(t)|.
\]
Taking sup over $t$ yields
\[
\|f_n^m-f^m\|_\infty \le m(M')^{m-1}\,\|f_n-f\|_\infty \xrightarrow[n\to\infty]{} 0.
\]
Therefore $f_n^m\to f^m$ uniformly on $[0,1]$.


	\par\noindent\textbullet\quad $f_n(t)=t+\tfrac1n$, $f(t)=t$, $m=3$:
	$\|f_n^3-f^3\|_\infty \le 12/n \to 0$.
	\par\noindent\textbullet\quad $f_n(t)=\sin(nt)/n$, $f\equiv0$: for any $m\ge1$,
	$\|f_n^m-f^m\|_\infty=\|f_n\|_\infty^m \le (1/n)^m \to 0$.
```

## CP-II-0053

- chapter line: 12241

```tex
\label{prob:cp-ii-0053}
\par\noindent (c)\quad Is such a phenomenon possible in $\ell^1$ or $\ell^2$ when the two norms are chosen
	from the standard norms on $\ell^1,\ell^2,\ell^\infty$?
	What about in $C([0,1])$ when the two norms are chosen from $L^1,L^2,L^\infty$?

\bigskip
```

## CP-II-0054

- chapter line: 12250

```tex
\label{prob:cp-ii-0054}
(*)

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad If $f:\mathbb{R}^n\to\mathbb{R}^m$ is continuous and $U$ open in $\mathbb{R}^m$, then $f^{-1}(U)$ is open.
\par\noindent\textbullet\quad If $f^{-1}(U)$ is open for every open $U\subset\mathbb{R}^m$, then $f$ is continuous on $\mathbb{R}^n$.
```

## CP-II-0056

- chapter line: 12259

```tex
\label{prob:cp-ii-0056}
In $H=\ell^2$, the canonical basis $(e_i)$ satisfies $e_i\rightharpoonup0$
	but $\|e_i\|=1$.  Thus weak convergence does not imply norm convergence.

	\bigskip
```

## CP-II-0058

- chapter line: 12357

```tex
\label{prob:cp-ii-0058}
$f_n(x)=\sin(x+n)$ on $[0,2\pi]$ (Subsequences converge uniformly)
```

## CP-II-0060

- chapter line: 12362

```tex
\label{prob:cp-ii-0060}
— Distributions annihilated by a power of $x$

Suppose $u\in\mathcal D'(\mathbb R)$ satisfies $x\,u=0$. Show that $u=c\,\delta_0$ for some $c\in\mathbb C$.
Find the most general $u\in\mathcal D'(\mathbb R)$ such that $x^k u=0$ for some $k\in\mathbb N$.

Since $\langle x u,\phi\rangle=\langle u,x\phi\rangle$, the condition $x u=0$ says $u$ vanishes on $x\mathcal D(\mathbb R)$.
Thus $\operatorname{supp}u\subset\{0\}$ and $u=\sum_{m=0}^{M} c_m\,\delta_0^{(m)}$.
Moreover,
\[
x\delta_0^{(m)}=-m\,\delta_0^{(m-1)} \qquad (m\ge1),\qquad x\delta_0=0.
\]
Hence $0=x u=\sum_{m=1}^{M} c_m(-m)\delta_0^{(m-1)}$ forces $c_m=0$ for $m\ge1$, so $u=c_0\delta_0$.

Iterating,
\[
x^k\delta_0^{(m)}=(-1)^k m(m-1)\cdots(m-k+1)\,\delta_0^{(m-k)},
\]
which is zero iff $m<k$. Therefore
\[
\{u\in\mathcal D'(\mathbb R):\,x^k u=0\}
=\operatorname{span}\{\delta_0,\,\delta_0',\,\dots,\,\delta_0^{(k-1)}\}.
\]

\bigskip

\textbf{Example 1 ($xu=0$ forces a pure mass at $0$).}
For $u=c_0\delta_0$,
\[
\langle x u,\phi\rangle=\langle u,x\phi\rangle=c_0\,x\phi(0)=0,
\]
so $x u=0$. Conversely, if $xu=0$ and $u=\sum_{m=0}^M c_m\delta_0^{(m)}$,
then using $x\delta_0^{(m)}=-m\,\delta_0^{(m-1)}$,
\[
0=xu=\sum_{m=1}^M c_m(-m)\,\delta_0^{(m-1)}
\quad\Rightarrow\quad c_m=0\ \ (m\ge1),
\]
hence $u=c_0\delta_0$.

\medskip

\textbf{Example 2 (all solutions of $x^2 u=0$).}
Write $u=a\,\delta_0+b\,\delta_0'+\sum_{m\ge2} c_m\delta_0^{(m)}$.
Since $x^2\delta_0=0$ and $x^2\delta_0' = x(-\delta_0)=0$, while
\[
x^2\delta_0^{(m)}=x\big(-m\,\delta_0^{(m-1)}\big)
=m(m-1)\,\delta_0^{(m-2)}\neq0 \quad \text{for } m\ge2,
\]
we must have $c_m=0$ for $m\ge2$. Therefore the solution space is
$\operatorname{span}\{\delta_0,\delta_0'\}$.

\medskip

\textbf{Example 3 (general $k$).}
Using $x^k\delta_0^{(m)}=(-1)^k m(m-1)\cdots(m-k+1)\,\delta_0^{(m-k)}$, the product vanishes
iff $m<k$. Hence precisely the linear span
\[
\{u:\ x^k u=0\}=\operatorname{span}\{\delta_0,\delta_0',\dots,\delta_0^{(k-1)}\}.
\]

\medskip

\textbf{Example 4 (failure when $m\ge k$).}
Take $k=3$ and $u=\delta_0^{(3)}$. Then
$x^3 u = (-1)^3 3\cdot 2\cdot 1\,\delta_0 = -6\,\delta_0\neq 0$, so $u$ is not a solution.

\bigskip

If $x^2 u=0$ then $u=a\,\delta_0+b\,\delta_0'$. If $x u=0$ then $u=c\,\delta_0$.

\bigskip
\bigskip
```

## CP-II-0065

- chapter line: 12507

```tex
\label{prob:cp-ii-0065}
— Hat functions and piecewise–linear interpolation

For $n,r\in\mathbb{Z}$ and $n\ge1$, define $\Delta_{n,r}:[-1,1]\to\mathbb{R}$ by
\[
\Delta_{n,r}(x)=\max\{0,\; 1-n|x-rn^{-1}|\}.
\]
Sketch $\Delta_{n,r}$.
For $f:[-1,1]\to\mathbb{R}$, show that
\[
f_n(x)=\sum_{m=-n}^{n} f\!\left(\frac{m}{n}\right)\Delta_{n,m}(x)
\]
is piecewise linear with $f_n(r/n)=f(r/n)$.
Show that if $f$ is continuous, then $\|f_n-f\|_\infty\to0$ as $n\to\infty$.

Each $\Delta_{n,r}$ is a tent function supported on $[(r-1)/n,(r+1)/n]$ with value $1$
at $x=r/n$ and slopes $\pm n$. On each cell $[k/n,(k+1)/n]$, exactly two hats are nonzero,
$\Delta_{n,k}$ and $\Delta_{n,k+1}$, and they satisfy
$\Delta_{n,k}(x)+\Delta_{n,k+1}(x)=1$. If $f$ is continuous on $[-1,1]$, then its modulus
of continuity $\omega_f(\delta)=\sup_{|x-y|\le\delta}|f(x)-f(y)|$ obeys
$\omega_f(\delta)\to0$ as $\delta\downarrow0$.

\par\medskip\noindent\textbf{Sketch / explicit form of $\Delta_{n,r}$.}\quad
\[
\Delta_{n,r}(x)=
\begin{cases}
	n\big(x-\frac{r-1}{n}\big), & x\in\big[\frac{r-1}{n},\frac{r}{n}\big],\\[2pt]
	n\big(\frac{r+1}{n}-x\big), & x\in\big[\frac{r}{n},\frac{r+1}{n}\big],\\[2pt]
	0, & \text{otherwise.}
\end{cases}
\]

If $x\in[k/n,(k+1)/n]$, then
\[
\Delta_{n,k}(x)=\frac{k+1}{n}-x,\qquad
\Delta_{n,k+1}(x)=x-\frac{k}{n},
\]
and all other $\Delta_{n,m}(x)$ vanish. Hence
\[
f_n(x)=f\!\left(\frac{k}{n}\right)\Big(\frac{k+1}{n}-x\Big)
+f\!\left(\frac{k+1}{n}\right)\Big(x-\frac{k}{n}\Big),
\]
which is linear in $x$ on that interval. In particular,
$f_n(r/n)=f(r/n)$ for each $r$.

For $x\in[k/n,(k+1)/n]$ write $x=\lambda \frac{k}{n}+(1-\lambda)\frac{k+1}{n}$ with
$\lambda=\frac{k+1}{n}-x\in[0,1]$. Then
\[
f_n(x)=\lambda f\!\left(\frac{k}{n}\right)
+(1-\lambda)f\!\left(\frac{k+1}{n}\right),
\]
so
\[
|f(x)-f_n(x)|
\le \lambda\Big|f(x)-f\!\left(\frac{k}{n}\right)\Big|
+(1-\lambda)\Big|f(x)-f\!\left(\frac{k+1}{n}\right)\Big|
\le \omega_f\!\left(\frac{1}{n}\right).
\]
Therefore $\|f-f_n\|_\infty \le \omega_f(1/n)\to0$ as $n\to\infty$.

	\par\noindent\textbullet\quad $f(x)=x^2$: $f_n$ is the polygonal line through $\{(m/n,(m/n)^2)\}$;
	$\|f-f_n\|_\infty=\Theta(n^{-2})$.
	\par\noindent\textbullet\quad $f(x)=|x|$: convergence is uniform with $\|f-f_n\|_\infty=O(n^{-1})$ (Lipschitz $1$).
	\par\noindent\textbullet\quad $f=\operatorname{sign}(x)$ (discontinuous): $f_n$ does not converge uniformly to $f$;
	uniform convergence requires continuity.
```

## CP-II-0067

- chapter line: 12591

```tex
\label{prob:cp-ii-0067}
\par\noindent (a)\quad For each fixed $x\in\mathbb{R}^n$ the translation operator
		$\tau_x:\mathcal{E}(\mathbb{R}^n)\to\mathcal{E}(\mathbb{R}^n)$,
		defined by $(\tau_x\phi)(y)=\phi(y-x)$, is continuous.
		Moreover, if $x_l\to 0$ in $\mathbb{R}^n$ and $\phi\in\mathcal{E}$,
		then
		\[
		\tau_{x_l}\phi \longrightarrow \phi
		\quad\text{in }\mathcal{E}(\mathbb{R}^n).
		\]
```

## CP-II-0068

- chapter line: 12604

```tex
\label{prob:cp-ii-0068}
A sequence with $L^p$ convergence to $0$ but no pointwise limit

Construct a sequence $(f_j)$ of measurable functions on $I=(0,1)$ such that
\[
f_j \to 0 \quad \text{in } L^p(I)\ \text{for every } 1\le p<\infty,
\]
but for every $x\in(0,1)$ the numeric sequence $(f_j(x))$ does \emph{not} converge.
Also determine whether an analogous construction is possible for $p=\infty$.

\textbf{Setup.} Let $I=(0,1)$ and $1\le p<\infty$. Fix an irrational $\alpha\in(0,1)$ and define
\[
a_j=\{j\alpha\}\in[0,1), \qquad
I_j=(a_j,a_j+1/j)\ (\mathrm{mod}\ 1), \qquad
f_j=\mathbf 1_{I_j}.
\]

\textbf{$L^p$ convergence.} $\|f_j\|_{L^p(I)} = |I_j|^{1/p} = (1/j)^{1/p}\to 0$.

\textbf{No pointwise convergence anywhere.}
By DirichletĂ˘â‚¬â„˘s approximation, for every $x\in(0,1)$ there are infinitely many $j$ with
$\|j\alpha-x\|<1/j$, hence $x\in I_j$ infinitely often.
Therefore $f_j(x)$ takes the values $1$ and $0$ infinitely often and does not converge at any $x$.

\textbf{Case $p=\infty$.} If $\|f_j\|_{L^\infty}\to 0$ then $|f_j(x)|\le \|f_j\|_{L^\infty}\to 0$
for each $x$, so $f_j(x)\to 0$ everywhere. Thus no such sequence exists in $L^\infty$.

\bigskip\hrule\bigskip
```

## CP-II-0074

- chapter line: 12666

```tex
\label{prob:cp-ii-0074}
Trigonometric series

$f_i(x)=\dfrac{\sin(ix)}{i^2}$, $x\in[0,2\pi]$.
Bounded by $1/i^2$, series $\sum 1/i^2$ converges $\Rightarrow$ uniform convergence.

---
```

## CP-II-0078

- chapter line: 12676

```tex
\label{prob:cp-ii-0078}
\par\noindent\textbullet\quad This identity shows that multiplication by $g\in L^q$ defines a
	bounded linear functional on $L^p$ with operator norm $\|g\|_{L^q}$
	--- the starting point of $L^p$ duality.

\bigskip
```

## CP-II-0079

- chapter line: 12685

```tex
\label{prob:cp-ii-0079}
\par\noindent\textbullet\quad Use (A) to pass $x\to 1^-$ or to prove uniform convergence on $[r,1]$.
```

## CP-II-0081

- chapter line: 12711

```tex
\label{prob:cp-ii-0081}
\par\noindent\textbullet\quad \textbf{Moving bump (vanishing locally).}
		In $L^{p}(\mathbb R)$, $f_j=\mathbf 1_{(j,j+1)}$. Then $\|f_j\|_{p}=1$ and for any bounded $E$,
		eventually $\int_E f_j=0$, hence $f_j\rightharpoonup 0$ (but not strongly).
```

## CP-II-0084

- chapter line: 12718

```tex
\label{prob:cp-ii-0084}
\par\noindent\textbullet\quad \textbf{Uniform convergence on all of $X$.}
	Uniform convergence on $X=\mathbb{R}\setminus\mathbb{N}$ would require
	\[
	\sup_{x\in X}\ \sum_{m>n} (x-m)^{-2}\ \longrightarrow\ 0\qquad (n\to\infty).
	\]
	This fails because near $x=n+1$ the tail contains $(x-(n+1))^{-2}$, which can be arbitrarily large.
```

## CP-II-0087

- chapter line: 12728

```tex
\label{prob:cp-ii-0087}
\par\noindent\textbullet\quad no pathological behaviour can occur.

Once the inequality is established for simple functions, one extends it
to general measurable functions (continuous, $C^\infty$, polynomials,
Gaussians, trigonometric functions, etc.) by:
```
