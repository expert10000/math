# Part II missing-solution batch 16

- problems: **20**
- IDs: CP-II-0398, CP-II-0399, CP-II-0402, CP-II-0403, CP-II-0404, CP-II-0408, CP-II-0409, CP-II-0412, CP-II-0414, CP-II-0418, CP-II-0419, CP-II-0420, CP-II-0422, CP-II-0423, CP-II-0427, CP-II-0431, CP-II-0432, CP-II-0439, CP-II-0440, CP-II-0442

## CP-II-0398

- chapter line: 18398

```tex
\label{prob:cp-ii-0398}
Suppose $A\subset\mathbb{R}^n$ and let $(f_i)_{i=0}^\infty$ with $f_i:A\to\mathbb{R}^m$ be a sequence of functions.
Assume $f_i\to f$ \emph{uniformly} on $A$. Show that if $B\subset A$, then $f_i\to f$ uniformly on $B$.

\textit{Solution.} By uniform convergence on $A$, for every $\varepsilon>0$ there exists $N\in\mathbb{N}$ such that
for all $i\ge N$ and all $x\in A$ we have $\|f_i(x)-f(x)\|<\varepsilon$. Since $B\subset A$, this inequality holds
for all $x\in B$ as well, with the \emph{same} $N$. Hence $f_i\to f$ uniformly on $B$. Equivalently,
\[
\sup_{x\in B}\|f_i(x)-f(x)\|\le \sup_{x\in A}\|f_i(x)-f(x)\|\xrightarrow{i\to\infty} 0.
\]
```

## CP-II-0399

- chapter line: 18411

```tex
\label{prob:cp-ii-0399}
\par\noindent\textbullet\quad Symmetrically, $\mathrm{id}:(X,\rho)\to(X,\tau)$ is continuous iff $\tau\subseteq\rho$.

\bigskip
```

## CP-II-0402

- chapter line: 18480

```tex
\label{prob:cp-ii-0402}
\par\noindent\textbullet\quad Start with \(Y=\mathbb{R}\) equipped with the usual metric \(|\cdot|\).
```

## CP-II-0403

- chapter line: 18485

```tex
\label{prob:cp-ii-0403}
Let $q\geq 2$ and $n\geq 1$. Define
\[
\mathcal{G}(\{x_1,\dots,x_q\}, \{y_1,\dots,y_q\})
= \inf \left\{ \Big(\sum_{j=1}^q |y_j - x_{\sigma(j)}|^2 \Big)^{1/2} : \sigma \text{ a permutation} \right\}.
\]

\subsection*{(i) $\mathcal{G}$ is a metric.}

	\par\noindent\textbullet\quad Non-negativity: sums of squares are nonnegative.
	\par\noindent\textbullet\quad Identity: $\mathcal{G}(X,Y)=0$ iff $X=Y$ as multisets.
	\par\noindent\textbullet\quad Symmetry: follows since $|y_j-x_{\sigma(j)}|=|x_{\sigma(j)}-y_j|$.
	\par\noindent\textbullet\quad Triangle inequality: For $X,Y,Z$, by MinkowskiĂ˘â‚¬â„˘s inequality,
	\[
	\Big(\sum_j |x_{\sigma(j)}-z_j|^2\Big)^{1/2}
	\leq \Big(\sum_j |x_{\sigma(j)}-y_{\tau(j)}|^2\Big)^{1/2} + \Big(\sum_j |y_{\tau(j)}-z_j|^2\Big)^{1/2}.
	\]
	Taking infima over permutations $\sigma,\tau$ proves the inequality.

Hence $\mathcal{G}$ is a metric on $Q$.

If $x_1\leq \dots \leq x_q$ and $y_1\leq \dots \leq y_q$, then by the rearrangement inequality the permutation minimizing
\[
\sum_{j=1}^q (x_{\sigma(j)}-y_j)^2
\]
is the identity permutation. Hence
\[
\mathcal{G}(\{x_1,\dots,x_q\}, \{y_1,\dots,y_q\})
= \Big(\sum_{j=1}^q (x_j-y_j)^2\Big)^{1/2}.
\]

	\par\noindent\textbullet\quad $X=\{0,1\}, Y=\{2,3\}$: $\mathcal{G}(X,Y)=\sqrt{8}$.
	\par\noindent\textbullet\quad $X=\{0,2\}, Y=\{1,3\}$: $\mathcal{G}(X,Y)=\sqrt{2}$.
```

## CP-II-0404

- chapter line: 18523

```tex
\label{prob:cp-ii-0404}
— Gibbs Phenomenon for a Square Wave

Suppose $f:\mathbb{R}\to\mathbb{R}$ is given by
\[
f(x) =
\begin{cases}
	-1, & -\tfrac12 \le x \le 0,\\[0.3em]
	1, & 0 < x \le \tfrac12,
\end{cases}
\qquad\text{and}\qquad
f(x+1) = f(x)\ \text{for all }x\in\mathbb{R}.
\]

\bigskip
\noindent\textbf{Theoretical background.}
The function $f$ is $1$-periodic, odd, and has jump discontinuities at
all half-integers.  For a $1$-periodic integrable function $f$, the
complex Fourier coefficients are
\[
\widehat f(k) = \int_{-1/2}^{1/2} f(x)e^{-2\pi i k x}\,dx,
\qquad k\in\mathbb{Z},
\]
and one formally has
\[
f(x) \sim \sum_{k\in\mathbb{Z}} \widehat f(k)e^{2\pi i k x}.
\]
Because $f$ is odd, only sine terms (and hence only odd harmonics)
appear in the real Fourier series.  Dirichlet's theorem implies that
the Fourier series converges to $f(x)$ at points of continuity, and to
the midpoint of the jump at discontinuities.  However, the convergence
is not uniform near a jump: the partial sums exhibit a persistent
overshoot known as the \emph{Gibbs phenomenon}.  This exercise
quantifies that overshoot for the square wave $f$.

\bigskip

We compute the complex Fourier coefficients
\[
\widehat f(k) = \int_{-1/2}^{1/2} f(x)e^{-2\pi i k x}\,dx.
\]
Since $f$ is odd, $\widehat f(k)=0$ for all even $k$.  For $k=2n+1$ we
have
\[
\widehat f(2n+1)
= \int_{-1/2}^{1/2} f(x)e^{-2\pi i (2n+1)x}\,dx
= \frac{2}{\pi i(2n+1)}.
\]
Therefore
\[
f(x)
= \sum_{n\in\mathbb{Z}} \widehat f(2n+1)e^{2\pi i(2n+1)x}
= \frac{1}{\pi i}\sum_{n=-\infty}^{\infty}
\frac{2}{2n+1}e^{2\pi i(2n+1)x}.
\]
Grouping conjugate terms and passing to the real sine series, we obtain
\[
f(x)
= \frac{4}{\pi}\sum_{n=0}^{\infty}
\frac{1}{2n+1}\,\sin\bigl(2\pi(2n+1)x\bigr),
\]
with convergence in $L^2([-1/2,1/2])$ and hence in
$L^2_{\mathrm{loc}}(\mathbb{R})$.

Define the partial sums
\[
S_N(x)
:= \frac{4}{\pi}\sum_{n=0}^{N-1}\frac{1}{2n+1}
\sin\bigl(2\pi(2n+1)x\bigr)
= 8\sum_{n=0}^{N-1} \frac{1}{2\pi(2n+1)}
\sin\bigl(2\pi(2n+1)x\bigr).
\]

\bigskip

Using
\[
\frac{d}{dt}\sin\bigl(2\pi(2n+1)t\bigr)
= 2\pi(2n+1)\cos\bigl(2\pi(2n+1)t\bigr),
\]
we write
\[
\sin\bigl(2\pi(2n+1)x\bigr)
= \int_0^x 2\pi(2n+1)
\cos\bigl(2\pi(2n+1)t\bigr)\,dt,
\]
and hence
\[
\frac{1}{2\pi(2n+1)}\sin\bigl(2\pi(2n+1)x\bigr)
= \int_0^x \cos\bigl(2\pi(2n+1)t\bigr)\,dt.
\]
Summing over $n$ gives
\[
S_N(x)
= 8\sum_{n=0}^{N-1}\int_0^x
\cos\bigl(2\pi(2n+1)t\bigr)\,dt
= 8\int_0^x \sum_{n=0}^{N-1}
\cos\bigl(2\pi(2n+1)t\bigr)\,dt.
\]

\bigskip

Recall the identity
\[
2\cos A\sin B = \sin(A+B)-\sin(A-B).
\]
Setting $A=2\pi(2n+1)t$, $B=2\pi t$, we find
\[
\cos\bigl(2\pi(2n+1)t\bigr)\sin(2\pi t)
= \frac12\Bigl(\sin\bigl(2\pi(2n+2)t\bigr)
-\sin(4\pi n t)\Bigr).
\]
Thus
\[
\sum_{n=0}^{N-1}\cos\bigl(2\pi(2n+1)t\bigr)
= \frac{1}{2\sin(2\pi t)}
\sum_{n=0}^{N-1}
\Bigl(\sin\bigl(2\pi(2n+2)t\bigr)
-\sin(4\pi n t)\Bigr).
\]
The sum on the right is telescoping and simplifies to $\sin(4\pi N t)$,
whence
\[
\sum_{n=0}^{N-1}\cos\bigl(2\pi(2n+1)t\bigr)
= \frac{\sin(4\pi N t)}{2\sin(2\pi t)}.
\]
Substituting this back into the formula in part~(b) yields
\[
S_N(x)
= 8\int_0^x \frac{\sin(4\pi N t)}{2\sin(2\pi t)}\,dt.
\]

\bigskip

Differentiating $S_N$ gives
\[
S_N'(x)
= 8\sum_{n=0}^{N-1}\cos\bigl(2\pi(2n+1)x\bigr)
= 4\,\frac{\sin(4\pi N x)}{\sin(2\pi x)}.
\]
Critical points occur when $\sin(4\pi N x)=0$ and $x\notin\mathbb{Z}$.
Near $x=0$ the first such zero is at $x=\tfrac{1}{4N}$; inspection of
the sign of $S_N'$ shows this is the first local maximum.

For small $t$ we have $\sin(2\pi t)\le 2\pi t$, hence
$2\sin(2\pi t)\le 4\pi t$ and so
\[
\frac{1}{2\sin(2\pi t)} \ge \frac{1}{4\pi t}.
\]
Thus
\[
S_N(x)
= 8\int_0^x \frac{\sin(4\pi N t)}{2\sin(2\pi t)}\,dt
\;\ge\;
8\int_0^x \frac{\sin(4\pi N t)}{4\pi t}\,dt.
\]
Taking $x=\tfrac{1}{4N}$ and substituting $s=4\pi N t$, so
$dt = \tfrac{ds}{4\pi N}$ and $s$ runs from $0$ to $\pi$, we obtain
\[
S_N\Bigl(\frac{1}{4N}\Bigr)
\ge 8\int_0^{1/(4N)} \frac{\sin(4\pi N t)}{4\pi t}\,dt
= \frac{2}{\pi}\int_0^{\pi} \frac{\sin s}{s}\,ds
\simeq 1.179\ldots
\]
for all $N$.

\bigskip

At the discontinuity $x=0$, Dirichlet's theorem implies that
\[
\lim_{N\to\infty} S_N(0)
= \frac{f(0^-)+f(0^+)}{2}
= 0.
\]
However, for $x_N = \tfrac{1}{4N}$ we have
\[
S_N(x_N) \gtrsim 1.179,
\]
while $f(x_N)\to 1$ as $N\to\infty$.  Hence
\[
\limsup_{N\to\infty}\sup_{x\in[-1/2,1/2]}
|S_N(x)-f(x)|
\ge \limsup_{N\to\infty}|S_N(x_N)-1|
\ge 1.179 - 1 > 0,
\]
so the Fourier series in part~(a) does \emph{not} converge uniformly on
any interval containing $0$.  This persistent overshoot near the jump is
the \emph{Gibbs phenomenon}.

\bigskip

Figure~\ref{fig:ex5-6-square-global} shows the global Fourier partial sums, while Figure~\ref{fig:ex5-6-square-gibbs} zooms in near $x=0$ to show the Gibbs overshoot.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.90\linewidth]{figures/part02/ex5_6_square_global.png}
  \caption{Global view of the square-wave Fourier partial sums.}
  \label{fig:ex5-6-square-global}
\end{figure}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.88\linewidth]{figures/part02/ex5_6_square_gibbs_zoom.png}
  \caption{Zoom near the jump at $x=0$, showing the persistent Gibbs overshoot.}
  \label{fig:ex5-6-square-gibbs}
\end{figure}

	\clearpage
```

## CP-II-0408

- chapter line: 18734

```tex
\label{prob:cp-ii-0408}
Pointwise but not uniform (Not Cauchy)

$f_n(x)=x^n$ on $[0,1]$.
Pointwise limit discontinuous, not uniform, not Cauchy in sup norm.

---
```

## CP-II-0409

- chapter line: 18744

```tex
\label{prob:cp-ii-0409}
Gaussian.

Let $F(x,y)=e^{-x^2-y^2}$ on $\mathbb{R}$.  Then
\[
\int_{\mathbb{R}}F(x,y)\,dy = \sqrt{\pi}\,e^{-x^2}.
\]
Hence
\[
\int_{\mathbb{R}} \Bigl|\int_{\mathbb{R}}F(x,y)\,dy\Bigr|dx
= \sqrt{\pi}\int_{\mathbb{R}} e^{-x^2}dx
= \pi.
\]
Since $F\ge 0$,
\[
\int_{\mathbb{R}}\int_{\mathbb{R}}|F(x,y)|\,dy\,dx
= \pi.
\]
```

## CP-II-0412

- chapter line: 18765

```tex
\label{prob:cp-ii-0412}
\par\noindent\textbullet\quad On $(\mathbb{R},\mathcal B)$ with $\mu=m$ (Lebesgue) and $\nu=m+\delta_0$, we have
		$\nu_a=m$ and $\nu_s=\delta_0$.
```

## CP-II-0414

- chapter line: 18771

```tex
\label{prob:cp-ii-0414}
\par\noindent\textbullet\quad Surface measure on a smooth embedded manifold $M\subset\mathbb{R}^n$ is a Radon Borel measure on $M$ (subspace topology).
```

## CP-II-0418

- chapter line: 18798

```tex
\label{prob:cp-ii-0418}
\par\noindent\textbullet\quad For every multi-index $\gamma$ and $1\le p<\infty$,
	\[
	x^\gamma D^\alpha f(x)\in L^p(\mathbb{R}^n),
	\]
	since we may take $N$ large enough to dominate the polynomial
	growth of $x^\gamma$.
```

## CP-II-0419

- chapter line: 18808

```tex
\label{prob:cp-ii-0419}
\par\noindent\textbullet\quad Deduce that
		\[
		\widehat{K_\varepsilon^t}(\xi)
		= \left(1+\frac{i4t}{\varepsilon}\right)^{-\tfrac{n}{2}}
		e^{-\, i t|\xi|^2/(1+4it\varepsilon)}.
		\]
```

## CP-II-0420

- chapter line: 18818

```tex
\label{prob:cp-ii-0420}
a step function

Let $H(x)=\mathbf{1}_{[1/2,\,1]}(x)$. Then
\[
B_n[H](x)=\sum_{k=\lceil n/2\rceil}^{n}\binom{n}{k}\,x^k(1-x)^{n-k}.
\]
One has
\[
B_n[H](x)\to
\begin{cases}
	0, & x<\tfrac{1}{2},\\[2pt]
	\tfrac12, & x=\tfrac{1}{2},\\[2pt]
	1, & x>\tfrac{1}{2},
\end{cases}
\qquad (n\to\infty).
\]
Hence $B_n[H]\to H$ pointwise at all continuity points of $H$, but not uniformly.
Moreover, for each $1\le p<\infty$,
\[
\|B_n[H]-H\|_{L^p([0,1])}\longrightarrow 0,
\]
so $H$ is approximable by polynomials in $L^p$.

\bigskip

Dropping uniform convergence allows polynomial approximation of discontinuous functions:
 \setlength{\itemsep}{0.6em}
	\par\noindent\textbullet\quad pointwise convergence at continuity points (e.g.\ Bernstein polynomials),
	\par\noindent\textbullet\quad $L^p$-convergence for every $1\le p<\infty$ (polynomials are dense in $L^p$),
	\par\noindent\textbullet\quad often almost-everywhere convergence for suitable subsequences.

Uniform convergence on the whole interval still fails for discontinuous $f$.

Let $(p_n)$ be polynomials on $[0,1]$ converging to $f$ (pointwise, or in $L^p$, $1\le p<\infty$).
If $f$ is not a polynomial, then necessarily $\deg p_n\to\infty$.

\smallskip

\noindent\textbf{Proof (pointwise case).}
Assume $\deg p_n\le m$ for all $n$. Let $\mathcal P_{\le m}$ be the space of polynomials of degree $\le m$.
Choose distinct nodes $x_0,\dots,x_m\in[0,1]$. The evaluation map
\[
T:\mathcal P_{\le m}\to\mathbb{R}^{m+1}, \qquad T(p)=(p(x_0),\dots,p(x_m))
\]
is a linear isomorphism. Since $p_n(x_j)\to f(x_j)$ for each $j$, we have $T(p_n)\to v:=(f(x_0),\dots,f(x_m))$.
Let $p:=T^{-1}(v)\in\mathcal P_{\le m}$. By Lagrange interpolation, for each $x$ there exists a linear functional
$L_x:\mathbb{R}^{m+1}\to\mathbb{R}$ with $p_n(x)=L_x\!\big(T(p_n)\big)$; hence
$p_n(x)\to L_x(v)=p(x)$. Therefore the pointwise limit $f$ equals $p$, a polynomial of degree $\le m$.
Contradiction. Thus $\deg p_n$ cannot be bounded; hence $\deg p_n\to\infty$.


\smallskip

\noindent\textbf{Remark (normed convergences).}
For convergence in any norm (e.g.\ $L^p$), the same conclusion holds since
$\mathcal P_{\le m}$ is finite-dimensional and therefore closed; a limit of $(p_n)$ with $\deg p_n\le m$
must lie in $\mathcal P_{\le m}$.
```

## CP-II-0422

- chapter line: 18913

```tex
\label{prob:cp-ii-0422}
\begin{lemma}[Mollifiers in $\mathcal{D}'(\mathbb{R}^n)$]
	Let $(\phi_\varepsilon)_{\varepsilon>0}\subset \mathcal{D}(\mathbb{R}^n)$
	be a standard approximate identity as in Theorem~1.13, and let
	$T\in\mathcal{D}'(\mathbb{R}^n)$ be a distribution. Define the
	convolution $\phi_\varepsilon * T$ by
	\[
	\langle \phi_\varepsilon * T, \psi\rangle
	:= \big\langle T, \check{\phi}_\varepsilon * \psi \big\rangle,
	\qquad \psi\in\mathcal{D}(\mathbb{R}^n),
	\]
	where $\check{\phi}_\varepsilon(x):=\phi_\varepsilon(-x)$. Then
	$\phi_\varepsilon * T \in C^\infty(\mathbb{R}^n)$ for every
	$\varepsilon>0$, and
	\[
	\phi_\varepsilon * T \longrightarrow T
	\qquad\text{in }\mathcal{D}'(\mathbb{R}^n)\text{ as }\varepsilon\to0.
	\]
\end{lemma}
```

## CP-II-0423

- chapter line: 18935

```tex
\label{prob:cp-ii-0423}
\hfill

		\par\noindent\textbullet\quad Uniform: $f_n(x)=\dfrac{x}{n+x}$ on $[0,1]$; then
		$\sup_{[0,1]}|f_n|=\frac{1}{n+1}\to0$, so $f_n\to0$ uniformly.
		\par\noindent\textbullet\quad Nonuniform: $f_n(x)=x^n$ on $[0,1]$; then $f_n\to f$ pointwise with
		$f=\mathbf 1_{\{1\}}$, but not uniformly, since
		$\sup_{x\in[0,1)}|x^n-0|=1$ for all $n$.
```

## CP-II-0427

- chapter line: 18964

```tex
\label{prob:cp-ii-0427}
— Fourier Series of the Sawtooth Function

Let
\[
f(x) = x \quad (|x|<\tfrac12),
\qquad f(x+1)=f(x).
\]

\bigskip
\noindent\textbf{Step 1: Complex Fourier coefficients}

For $1$-periodic $f$,
\[
\widehat f(n)
= \int_{-1/2}^{1/2} f(x)e^{-2\pi i n x}\,dx.
\]

For $n=0$:
\[
\widehat f(0)=0.
\]

For $n\neq 0$:
\[
\widehat f(n)
= \int_{-1/2}^{1/2} x e^{-2\pi i n x}\,dx
= \frac{i(-1)^n}{2\pi n}.
\]

Thus
\[
f(x)=\sum_{\substack{n\in\mathbb{Z}\\ n\ne 0}}
\frac{i(-1)^n}{2\pi n} e^{2\pi i n x}
\qquad\text{in } L^2_{\mathrm{loc}}.
\]

\bigskip
\noindent\textbf{Step 2: Real sine series}

Since $f$ is odd, only sine terms appear:
\[
f(x) = \sum_{n=1}^{\infty} b_n \sin(2\pi n x).
\]
Using $\widehat f(n)= -\frac{i}{2}b_n$ for $n>0$ gives
\[
b_n = \frac{2(-1)^{n+1}}{\pi n}.
\]

Therefore:
\[
f(x)
= \sum_{n=1}^{\infty}
\frac{(-1)^{n+1}}{n\pi}\,\sin(2\pi n x),
\qquad
\text{convergent in } L^2_{\mathrm{loc}}(\mathbb{R}).
\]

\clearpage

Figure~\ref{fig:ex5-3-weighted-comb} shows the weighted discrete ``$\delta$--comb'' supported at the points $x=2\pi g$, $g\in\mathbb{Z}$.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.82\linewidth]{figures/part02/ex5_3_weighted_comb.png}
  \caption{Weighted discrete $\delta$--comb supported at $x=2\pi g$, $g\in\mathbb{Z}$.}
  \label{fig:ex5-3-weighted-comb}
\end{figure}
```

## CP-II-0431

- chapter line: 19054

```tex
\label{prob:cp-ii-0431}
let $f_n$ be a narrow spike of height $1$ and width $1/n$. Then
	\[
	\|f_n\|_\infty=1 \quad \text{but} \quad \|f_n\|_1=\frac{1}{n}\to 0.
	\]
	Hence convergence in $\|\cdot\|_1$ does not imply convergence in $\|\cdot\|_\infty$.
```

## CP-II-0432

- chapter line: 19063

```tex
\label{prob:cp-ii-0432}
— Quickies (uniform convergence \& regularity)

If $(f_n)$ is a sequence of real functions on $[0,1]$ converging uniformly to a function $f$ on $[0,1]$, and if $f_n$ is continuous at $x_n\in[0,1]$ with $x_n\to x$, does it follow that $f$ is continuous at $x$?

  If $(f_n)$ is a sequence of continuous real functions on $[-1,1]$ converging pointwise to a continuous function $f$ on $[-1,1]$, and if the convergence is uniform on $[-r,r]$ for every $r\in(0,1)$, does it follow that the convergence is uniform on $[-1,1]$?

  If $(f_n)$ is a sequence of real functions on the interval $[0,1]$ converging uniformly to a function $f$ on $[0,1]$, and if each $f_n$ is continuous except at countably many points, does it follow that there exists a point at which $f$ is continuous?

  If $(f_n)$ is a sequence of differentiable functions on $[0,1]$ converging uniformly to a function $f$ on $[0,1]$, does it follow that there exists a point at which $f$ is differentiable?

\bigskip

	\par\noindent\textbullet\quad \textbf{Continuity at a point is preserved by uniform limits:} If $f_n\to f$ uniformly on a set $E$ and each $f_n$ is continuous at $x_0\in E$, then $f$ is continuous at $x_0$.
	\par\noindent\textbullet\quad \textbf{Uniform limit of continuous functions is continuous.}
	\par\noindent\textbullet\quad \textbf{Countable union of countable sets is countable.}
	\par\noindent\textbullet\quad \textbf{Local vs global uniformity:} Uniform convergence on $[-r,r]$ for every $r<1$ need not imply uniform convergence on $[-1,1]$.
	\par\noindent\textbullet\quad \textbf{Weierstrass phenomenon:} There exist continuous nowhere differentiable functions that are uniform limits of differentiable functions (e.g., partial sums of the Weierstrass series).

Let
\[
f(x)=\begin{cases}
	0,& x<\tfrac12,\\
	1,& x\ge \tfrac12,
\end{cases}
\qquad \text{and set } f_n=f \text{ for all } n.
\]
Then $f_n\to f$ uniformly. Define $x_n=\tfrac12+\tfrac1n\to x=\tfrac12$. For each $n$, $f_n$ is continuous at $x_n$ (indeed $f$ is continuous at all $x\ne \tfrac12$), but $f$ is discontinuous at $x=\tfrac12$. Hence the asserted implication fails.

For $n\ge1$, define
\[
f_n(x)=
\begin{cases}
	n(1-x),& x\in[1-\tfrac1n,\,1],\\
	0,& x\in[-1,\,1-\tfrac1n),
\end{cases}
\qquad\text{and let } f\equiv 0.
\]
Each $f_n$ is continuous on $[-1,1]$. For any fixed $x\in[-1,1)$, $f_n(x)=0$ for all large $n$, so $f_n(x)\to 0=f(x)$. Also $f_n(1)=0\to 0=f(1)$, hence $f_n\to f$ pointwise and $f$ is continuous. Given any $r\in(0,1)$, if $n>\frac1{1-r}$ then $[1-\frac1n,1]\subset (r,1]$, so $f_n\equiv 0$ on $[-r,r]$; thus convergence is uniform on $[-r,r]$. However,
\[
\sup_{x\in[-1,1]}|f_n(x)-f(x)|=\max_{x\in[-1,1]} f_n(x)=1 \quad\text{for all }n,
\]
so the convergence is not uniform on $[-1,1]$.

Let $D_n$ be the (countable) set of discontinuities of $f_n$ and $D=\bigcup_{n=1}^\infty D_n$, which is countable. Choose $x_0\in[0,1]\setminus D$. Then each $f_n$ is continuous at $x_0$. Since $f_n\to f$ uniformly, the continuity-at-a-point lemma implies $f$ is continuous at $x_0$. Therefore $f$ is continuous at (at least) one point.

Consider the Weierstrass function
\[
W(x)=\sum_{k=0}^\infty a^k\cos(b^k\pi x),
\]
with $0<a<1$, $b\in\mathbb{N}$ odd, and $ab>1$. Let $S_n(x)=\sum_{k=0}^n a^k\cos(b^k\pi x)$. Then each $S_n$ is differentiable on $[0,1]$, and $S_n\to W$ uniformly on $[0,1]$, while $W$ is continuous everywhere and nowhere differentiable. Thus there need not exist any point where $f$ is differentiable.
```

## CP-II-0439

- chapter line: 19163

```tex
\label{prob:cp-ii-0439}
\par\noindent\textbullet\quad On $\mathbb{R}^n$:
	\[
	\|x\|_1=\sum_{i=1}^n |x_i|,\qquad
	\|x\|_2=\Big(\sum_{i=1}^n x_i^2\Big)^{1/2},\qquad
	\|x\|_\infty=\max_{1\le i\le n}|x_i|.
	\]
	There exist constants $a,b>0$ such that
	\[
	\|x\|_\infty \le \|x\|_2 \le \|x\|_1 \le \sqrt{n}\,\|x\|_2.
	\]
	Thus all norms on $\mathbb{R}^n$ are equivalent.
```

## CP-II-0440

- chapter line: 19178

```tex
\label{prob:cp-ii-0440}
— Discontinuities under uniform limits

Let $(f_n)$ be a sequence of real-valued functions on $[0,1]$ converging uniformly to a function $f$.
For each $n$, let $D_n$ be the set of discontinuities of $f_n$, and let $D$ be the set of discontinuities of $f$.

We show that
\[
D \subseteq \bigcap_{n=1}^{\infty}\ \bigcup_{j=n}^{\infty} D_j
\qquad\text{(the limsup of the sets $D_j$).}
\]
Equivalently, we prove the contrapositive. Suppose $x\notin \limsup D_j$. Then there exists $N$ such that
$x\notin D_j$ for all $j\ge N$. Thus, for all $j\ge N$, the function $f_j$ is continuous at $x$.
Since $f_j \to f$ uniformly on $[0,1]$, the uniform-limit lemma implies that $f$ is continuous at $x$.
Hence $x\notin D$, proving the desired inclusion.

Assume there exists a finite $k$ such that each $f_n$ has at most $k$ discontinuities.
We claim that $f$ has at most $k$ discontinuities.

Suppose, for a contradiction, that $f$ has at least $k+1$ distinct discontinuities $x_1,\dots,x_{k+1}\in[0,1]$.
Let the oscillation of a function $g$ at $x$ be
\[
\omega_g(x)=\lim_{r\downarrow 0}\left(\sup_{|t-x|<r} g(t) - \inf_{|t-x|<r} g(t)\right).
\]
Then $g$ is continuous at $x$ iff $\omega_g(x)=0$. Moreover, if $\|g-h\|_\infty\le \varepsilon$, then
$\omega_g(x)\le\omega_h(x)+2\varepsilon$ and $\omega_h(x)\le\omega_g(x)+2\varepsilon$.

Since $x_i$ is a discontinuity of $f$, we have $\omega_f(x_i)>0$ for each $i$.
Choose $0<\varepsilon<\frac12\min_{1\le i\le k+1}\omega_f(x_i)$.
Because $f_n\to f$ uniformly, there exists $N$ such that $\|f_n-f\|_\infty<\varepsilon$ for all $n\ge N$.
For each $i$ and $n\ge N$,
\[
\omega_{f_n}(x_i)\ \ge\ \omega_f(x_i) - 2\varepsilon\ >\ 0,
\]
so $f_n$ is discontinuous at $x_i$. Hence $f_n$ has at least $k+1$ discontinuities for all $n\ge N$,
contradicting the hypothesis that each $f_n$ has at most $k$ discontinuities.
Therefore $f$ has at most $k$ discontinuities.

(1) From (a) we always have $D \subseteq \limsup D_n$, so if each $D_n$ is finite then $D$ is at most countable.

(2) The conclusion in (b) is stronger: if each $f_n$ has at most $k$ discontinuities for a fixed $k$, then $f$ has at most $k$ discontinuities.

(3) Example (sharpness for $k=1$).

Fix $c\in(0,1)$ and define $f=\mathbf{1}_{[c,1]}$ and $f_n=\mathbf{1}_{[c+1/n,\,1]}$.
Then $f_n\to f$ uniformly, each $f_n$ has exactly one discontinuity, and $f$ has exactly one discontinuity.

Let $k=1$. Fix a point $c\in(0,1)$ and define
\[
f(x) = \mathbf{1}_{[c,1]}(x) =
\begin{cases}
	0, & x < c,\\
	1, & x \ge c,
\end{cases}
\qquad\text{and}\qquad
f_n(x) = \mathbf{1}_{[\,c+1/n,\,1\,]}(x).
\]
Each $f_n$ has exactly one discontinuity (at $x=c+1/n$);
$f_n \to f$ uniformly on $[0,1]$,
and $f$ has exactly one discontinuity (at $x=c$).
This shows that the bound ``$\le k$'' is \emph{sharp}.
```

## CP-II-0442

- chapter line: 19242

```tex
\label{prob:cp-ii-0442}
Uniform convergence with oscillations (Cauchy)

$f_n(x)=\sin(nx)/n$ on $[0,\pi]$.
Uniform convergence to $f(x)=0$ since $\|f_n-0\|_\infty=1/n \to 0$.
```
