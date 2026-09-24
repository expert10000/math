# Part III missing-solution batch 02

- problems: **11**
- IDs: CP-III-0015, CP-III-0018, CP-III-0019, CP-III-0022, CP-III-0002, CP-III-0007, CP-III-0012, CP-III-0020, CP-III-0024, CP-III-0025, CP-III-0009

## CP-III-0015

```tex
\label{prob:cp-iii-0015}
\begin{example}[Heat kernel (time domain)]
		For $u_t-\Delta u=\delta_{t=0}\delta_{x=0}$, the space--time Fourier transform gives
		$\widehat{G}(k,\omega)=\dfrac{1}{-i\omega+|k|^2}$, hence
		\[
		G(t,x)=\frac{\mathbf{1}_{t>0}}{(4\pi t)^{n/2}}\,e^{-\frac{|x|^2}{4t}}.
		\]
	\end{example}
```

## CP-III-0018

```tex
\label{prob:cp-iii-0018}
example coefficients $c_g=(1+|g|)^2$.  The vertical stems represent the
weights of the Dirac deltas.  The exercise shows that even with
polynomially growing coefficients such a series still defines a tempered
distribution in $\mathcal{S}'$.


\bigskip

\par\smallskip\noindent\textbf{Figure 2: Decay of the contributions $|c_g\varphi(2\pi g)|$.}\quad
Figure~\ref{fig:ex5-3-contributions} shows
$|c_g\varphi(2\pi g)|$ as a function of $g$ for the same polynomial
coefficients $c_g$ and a Schwartz function $\varphi(x)=e^{-x^2}$.
Although $|c_g|$ grows like $(1+|g|)^2$, the values $\varphi(2\pi g)$
decay faster than any power, so the product is summable.  This picture
reflects the key estimate used to prove convergence in $\mathcal{S}'$.


\bigskip

\par\smallskip\noindent\textbf{Figure 3: Periodic $L^p$ function and smooth approximation (Exercise 5.4).}\quad
In Figure~\ref{fig:ex5-4-periodic-approx} the original periodic function
$f$ is taken to be a square wave, while $f_\varepsilon$ is obtained by
periodic convolution with a narrow Gaussian kernel.  The resulting
$f_\varepsilon$ is smooth and periodic, and closely follows $f$ on each
period, visualising the construction in Exercise~5.4.


\bigskip

\par\smallskip\noindent\textbf{Figure 4: Fourier partial sums of the sawtooth (Exercise 5.5).}\quad
Figure~\ref{fig:ex5-5-fourier-global} shows the sawtooth function $f$
from Exercise~5.5 together with its Fourier partial sums $S_3$, $S_{10}$
and $S_{50}$.  As $N$ increases, $S_N$ converges to $f$ in $L^2$ and
visually away from the jump points, while oscillations appear near the
discontinuities.


\bigskip

\par\smallskip\noindent\textbf{Figure 5: Gibbs phenomenon near a jump.}\quad
Figure~\ref{fig:ex5-5-fourier-gibbs} zooms in near one jump of $f$ and
compares the partial sums $S_{10}$ and $S_{50}$.  The overshoot of the
Fourier partial sums does not vanish as $N\to\infty$, illustrating the
classical Gibbs phenomenon, even though convergence holds in
$L^2_{\mathrm{loc}}$.


\clearpage


\begin{figure}[ht]
	\centering
	\includegraphics[width=0.8\textwidth]{figures/part03/fig_ex5-3-contributions.png}
	\caption{The terms $|c_g\varphi(2\pi g)|$ for
		$c_g=(1+|g|)^2$ and $\varphi(x)=e^{-x^2}$, illustrating
		absolute convergence of the defining series.}
	\label{fig:ex5-3-contributions}
\end{figure}


\begin{figure}[ht]
	\centering
	\includegraphics[width=0.8\textwidth]{figures/part03/fig_ex5-4-periodic-approx.png}
	\caption{A periodic square wave $f$ and a smooth periodic
		approximation $f_\varepsilon$ obtained by mollification.
		This illustrates the approximation scheme of Exercise~5.4.}
	\label{fig:ex5-4-periodic-approx}
\end{figure}


\begin{figure}[ht]
	\centering
	\includegraphics[width=0.8\textwidth]{figures/part03/fig_ex5-5-fourier-gibbs.png}
	\caption{Zoom near a jump of the sawtooth function, showing the Gibbs
		oscillations of the partial sums $S_{10}$ and $S_{50}$.}
	\label{fig:ex5-5-fourier-gibbs}
\end{figure}


\begin{figure}[ht]
	\centering
	\includegraphics[width=0.8\textwidth]{figures/part03/fig_ex5-5-fourier-global.png}
	\caption{Global comparison of the sawtooth function $f$ and partial
		sums $S_N$ of its sine series for $N=3,10,50$.}
	\label{fig:ex5-5-fourier-global}
\end{figure}
```

## CP-III-0019

```tex
\label{prob:cp-iii-0019}
Suppose that $u_0 \in \mathscr{S}(\mathbb{R}^n)$.
	Show that for $t>0$:
	\[
	u(t,x) = \int_{\mathbb{R}^n} u_0(y)\, K_t(x-y)\, dy,
	\]
	and deduce the dispersive estimate
	\[
	\sup_{x\in\mathbb{R}^n} |u(t,x)|
	\;\;\lesssim\;\;
	\frac{1}{(4\pi t)^{n/2}}\, \|u_0\|_{L^1(\mathbb{R}^n)}.
	\]
	(This type of estimate shows the decay of solutions to the Schrödinger equation.)


\par\medskip\noindent\textbf{Schrödinger Equation in $\mathbb{R}^n$ : Theory and Solutions}\quad

Recall that for $s\ge 0$ the Sobolev norm is
\[
\|f\|_{H^s(\mathbb{R}^n)}^2
= \int_{\mathbb{R}^n} (1+|\xi|^2)^s |\widehat{f}(\xi)|^2\,d\xi.
\]

% ---------- (a) ----------
\par\smallskip\noindent\textbf{(a) \; Existence, Uniqueness and Fourier Representation}\quad

\par\smallskip\noindent\textbf{\textbf{Idea.}}\quad
Take the Fourier transform in the spatial variable, which turns the PDE
\[
u_t = i\Delta u
\]
into an ODE in $t$ for each $\xi$.

\par\smallskip\noindent\textbf{\textbf{Derivation.}}\quad
Using $\widehat{\Delta u}(t,\xi) = -|\xi|^2\widehat{u}(t,\xi)$, we get
\[
\partial_t \widehat{u}(t,\xi) = i\widehat{\Delta u}(t,\xi)
= -i|\xi|^2\,\widehat{u}(t,\xi), \qquad
\widehat{u}(0,\xi) = \widehat{u_0}(\xi).
\]
Hence
\[
\widehat{u}(t,\xi)
= e^{-it|\xi|^2}\,\widehat{u_0}(\xi).
\]

\par\smallskip\noindent\textbf{\textbf{Regularity.}}\quad
Define
\[
u(t,x)
:= \frac{1}{(2\pi)^n} \int_{\mathbb{R}^n}
\widehat{u_0}(\xi)\,e^{-it|\xi|^2} e^{ix\cdot\xi}\,d\xi.
\]
Since $u_0\in H^2(\mathbb{R}^n)$, we have
$(1+|\xi|^2)^2\widehat{u_0}(\xi)\in L^2$, and the multiplier
$e^{-it|\xi|^2}$ is bounded for each $t$. Standard Fourier multiplier
arguments give
\[
u \in C^0([0,T];H^2(\mathbb{R}^n))
\cap C^1((0,T);L^2(\mathbb{R}^n)).
\]

\par\smallskip\noindent\textbf{\textbf{Uniqueness.}}\quad
If $v$ is another solution with the same regularity and $v(0)=u_0$, then
$\widehat{v}$ satisfies the same ODE with the same initial data and
hence $\widehat{v}=\widehat{u}$. Thus $v=u$ and the solution is unique.

\medskip
In particular,
\[
\widehat{u}(t,\xi) = \widehat{u_0}(\xi)\,e^{-it|\xi|^2},
\]
as required.

% ---------- (b) ----------
\par\smallskip\noindent\textbf{(b) \; Conservation of the $H^2$-norm}\quad

\par\smallskip\noindent\textbf{\textbf{Computation.}}\quad
Using the formula from part~(a),
\[
\|u(t,\cdot)\|_{H^2}^2
= \int_{\mathbb{R}^n} (1+|\xi|^2)^2\,|\widehat{u}(t,\xi)|^2\,d\xi
= \int (1+|\xi|^2)^2\,|e^{-it|\xi|^2}|^2\,|\widehat{u_0}(\xi)|^2\,d\xi.
\]
Since $|e^{-it|\xi|^2}|=1$,
\[
\|u(t,\cdot)\|_{H^2}^2
= \int (1+|\xi|^2)^2 |\widehat{u_0}(\xi)|^2\,d\xi
= \|u_0\|_{H^2}^2.
\]
Hence
\[
\|u(t,\cdot)\|_{H^2(\mathbb{R}^n)} = \|u_0\|_{H^2(\mathbb{R}^n)}
\quad \text{for all } t\in[0,T].
\]

% ---------- (c) ----------
\par\smallskip\noindent\textbf{(c) \; The Schrödinger Kernel $K_t$ and its Fourier Transform}\quad

For $t>0$, set
\[
K_t(x) := \frac{1}{(4\pi i t)^{n/2}} e^{\, i|x|^2 /4t},
\qquad
K_t^\varepsilon(x) := e^{-\varepsilon|x|^2}K_t(x),\quad \varepsilon>0.
\]

\par\smallskip\noindent\textbf{\textbf{(i) Convergence in $\mathscr{S}'$.}}\quad
Let $\varphi\in\mathscr{S}(\mathbb{R}^n)$. Then
\[
\langle T_{K_t^\varepsilon},\varphi\rangle
= \int_{\mathbb{R}^n} K_t(x)\,e^{-\varepsilon|x|^2}\,\varphi(x)\,dx.
\]
As $\varepsilon\to0$, $e^{-\varepsilon|x|^2}\to1$ pointwise, and
\[
|K_t(x)e^{-\varepsilon|x|^2}\varphi(x)|
\le |K_t(x)\varphi(x)|.
\]
Since $K_t$ has at most polynomial growth and $\varphi$ is rapidly
decreasing, $K_t\varphi\in L^1(\mathbb{R}^n)$, so dominated convergence
gives
\[
\langle T_{K_t^\varepsilon},\varphi\rangle
\longrightarrow \int K_t(x)\varphi(x)\,dx
= \langle T_{K_t},\varphi\rangle.
\]
Thus $T_{K_t^\varepsilon}\to T_{K_t}$ in $\mathscr{S}'$.

\par\smallskip\noindent\textbf{\textbf{(ii) Complex Gaussian integral.}}\quad
If $\Re(\sigma)>0$, then
\[
\int_{\mathbb{R}} e^{-\sigma x^2 - i\xi x}\,dx
= \sqrt{\frac{\pi}{\sigma}}\, e^{-\xi^2/(4\sigma)}.
\]
This follows by completing the square and deforming the integration path.

\par\smallskip\noindent\textbf{\textbf{(iii) Fourier transform of $K_t^\varepsilon$.}}\quad
We write
\[
K_t^\varepsilon(x)
= \frac{1}{(4\pi i t)^{n/2}}\exp\!\Bigl(-\sigma |x|^2\Bigr),
\qquad
\sigma := \varepsilon - \frac{i}{4t},\quad \Re(\sigma)>0.
\]
Using (ii) in each coordinate, we obtain
\[
\widehat{e^{-\sigma |x|^2}}(\xi)
= \left(\sqrt{\frac{\pi}{\sigma}}\right)^n
\exp\!\Bigl(-\frac{|\xi|^2}{4\sigma}\Bigr),
\]
hence
\[
\widehat{K_t^\varepsilon}(\xi)
= \frac{1}{(4\pi i t)^{n/2}}
\left(\frac{\pi}{\sigma}\right)^{n/2}
\exp\!\Bigl(-\frac{|\xi|^2}{4\sigma}\Bigr).
\]
A straightforward simplification yields
\[
\widehat{K_t^\varepsilon}(\xi)
= \bigl(1+4it\varepsilon\bigr)^{-n/2}
\exp\!\left(-\frac{it|\xi|^2}{1+4it\varepsilon}\right).
\]

\par\smallskip\noindent\textbf{\textbf{(iv) Limit as $\varepsilon\to0$.}}\quad
As $\varepsilon\to0$,
\[
1+4it\varepsilon \to 1,
\qquad
-\frac{it|\xi|^2}{1+4it\varepsilon} \to -it|\xi|^2.
\]
Thus
\[
\widehat{K_t^\varepsilon}(\xi) \longrightarrow e^{-it|\xi|^2}
\quad\text{pointwise in }\xi.
\]
By (i), $T_{K_t^\varepsilon}\to T_{K_t}$ in $\mathscr{S}'$ and the
Fourier transform is continuous on $\mathscr{S}'$, so we conclude
\[
\widehat{K_t}(\xi) = e^{-it|\xi|^2}.
\]

% ---------- (d) ----------
\par\smallskip\noindent\textbf{(d) \; Convolution Representation and Dispersive Estimate}\quad

Assume $u_0\in\mathscr{S}(\mathbb{R}^n)$. From part~(a),
\[
\widehat{u}(t,\xi) = e^{-it|\xi|^2}\,\widehat{u_0}(\xi),
\]
and from part~(c),
\[
\widehat{K_t}(\xi) = e^{-it|\xi|^2}.
\]
Hence
\[
\widehat{u}(t,\xi)
= \widehat{u_0}(\xi)\,\widehat{K_t}(\xi)
= \mathcal{F}(u_0 * K_t)(\xi),
\]
so by injectivity of the Fourier transform
\[
u(t,x) = (u_0 * K_t)(x)
= \int_{\mathbb{R}^n} u_0(y)\,K_t(x-y)\,dy.
\]

\par\smallskip\noindent\textbf{\textbf{Dispersive estimate.}}\quad
Since $|e^{i|z|^2/(4t)}| = 1$, we have
\[
|K_t(z)| = \frac{1}{(4\pi |t|)^{n/2}}
\quad\text{for all } z\in\mathbb{R}^n.
\]
Then
\[
|u(t,x)|
\le \int_{\mathbb{R}^n} |u_0(y)|\,|K_t(x-y)|\,dy
\le \frac{1}{(4\pi|t|)^{n/2}} \int_{\mathbb{R}^n} |u_0(y)|\,dy.
\]
Taking the supremum over $x\in\mathbb{R}^n$ yields
\[
\sup_{x\in\mathbb{R}^n} |u(t,x)|
\le \frac{1}{(4\pi|t|)^{n/2}}\,\|u_0\|_{L^1(\mathbb{R}^n)}.
\]

\par\smallskip\noindent\textbf{\textbf{Conclusion.}}\quad
The free Schrödinger evolution is given by
$u(t,\cdot)=e^{it\Delta}u_0=u_0*K_t$,
acts unitarily on $H^2(\mathbb{R}^n)$, and satisfies the dispersive
estimate above, which shows decay in $L^\infty$ for data in $L^1$.

\par\medskip\noindent\textbf{Sobolev Space $H^{s}(\mathbb{R}^n)$ used in Exercise 5.10}\quad

Throughout this section, $H^{s}(\mathbb{R}^n)$ denotes the $L^2$-based Sobolev
space. For $s \ge 0$ we define
\[
H^{s}(\mathbb{R}^n)
:= \Bigl\{ f \in \mathscr{S}'(\mathbb{R}^n)
: \int_{\mathbb{R}^n} (1+|\xi|^2)^s |\widehat{f}(\xi)|^2 \, d\xi
< \infty \Bigr\},
\]
with norm
\[
\|f\|_{H^{s}(\mathbb{R}^n)}^2
:= \int_{\mathbb{R}^n} (1+|\xi|^2)^s |\widehat{f}(\xi)|^2 \, d\xi.
\]

For integer $s = m \in \mathbb{N}$ this is equivalent to
\[
H^{m}(\mathbb{R}^n)
= \Bigl\{ f \in L^2(\mathbb{R}^n)
: D^\alpha f \in L^2(\mathbb{R}^n) \text{ for all } |\alpha|\le m \Bigr\},
\]
and
\[
\|f\|_{H^{m}(\mathbb{R}^n)}^2
\simeq \sum_{|\alpha|\le m} \|D^\alpha f\|_{L^2(\mathbb{R}^n)}^2.
\]

In particular, in Exercise~5.10 the assumption $u_0 \in H^2(\mathbb{R}^n)$
means that $u_0$ and all second-order derivatives of $u_0$ belong to
$L^2(\mathbb{R}^n)$, and the solution $u(t,\cdot)$ stays in $H^2$ for all
times $t$.


\par\medskip\noindent\textbf{Relation Between Sobolev Spaces and the Schwartz Space}\quad

Let $\mathscr{S}(\mathbb{R}^n)$ denote the Schwartz space of rapidly
decreasing smooth functions. Recall that for $s\in\mathbb{R}$ the
$L^2$--based Sobolev space $H^s(\mathbb{R}^n)$ is defined by
\[
H^s(\mathbb{R}^n)
:= \Bigl\{ f\in\mathscr{S}'(\mathbb{R}^n) :
\int_{\mathbb{R}^n} (1+|\xi|^2)^s \,|\widehat{f}(\xi)|^2 \, d\xi
< \infty \Bigr\}.
\]

\par\smallskip\noindent\textbf{Inclusion.}\quad
Since $\widehat{f}\in\mathscr{S}(\mathbb{R}^n)$ whenever
$f\in\mathscr{S}(\mathbb{R}^n)$, the quantity
$(1+|\xi|^2)^s|\widehat{f}(\xi)|^2$ decays faster than any power of
$|\xi|$. Hence
\[
\mathscr{S}(\mathbb{R}^n) \subset H^s(\mathbb{R}^n)
\quad\text{for all } s\in\mathbb{R}.
\]

\par\smallskip\noindent\textbf{Density.}\quad
For every $s\in\mathbb{R}$ the Schwartz space is dense in $H^s$:
\[
\overline{\mathscr{S}(\mathbb{R}^n)}^{\,H^s(\mathbb{R}^n)}
= H^s(\mathbb{R}^n).
\]
This follows from approximation by mollifiers and compactly supported
smooth functions, as in Exercise~5.8.

\par\smallskip\noindent\textbf{Intersection over all orders.}\quad
One has the characterization
\[
\mathscr{S}(\mathbb{R}^n)
= \bigcap_{s\in\mathbb{R}} H^s(\mathbb{R}^n),
\]
that is, a tempered distribution belongs to the Schwartz space if and
only if it lies in every Sobolev space $H^s(\mathbb{R}^n)$.

\par\smallskip\noindent\textbf{Remark.}\quad
The space
\[
H^\infty(\mathbb{R}^n)
:= \bigcap_{m\in\mathbb{N}} H^m(\mathbb{R}^n)
\]
consists of functions with all derivatives in $L^2$ and contains
$\mathscr{S}(\mathbb{R}^n)$ as a dense subspace. The additional
requirement that both $f$ and $\widehat{f}$ decay faster than any power
of $|x|$ and $|\xi|$ is what distinguishes the Schwartz space from
general elements of $H^\infty$.


\par\medskip\noindent\textbf{Exercise 5.11 : Radial Solutions of the Wave Equation in $\mathbb{R}^3$}\quad

Let $\mathbb{R}^3_* := \mathbb{R}^3\setminus\{0\}$ and
\[
S_{*,T} := (-T,T)\times\mathbb{R}^3_*,
\qquad
S_T := (-T,T)\times\mathbb{R}^3,
\qquad
\Sigma_0 := \{0\}\times\mathbb{R}^3.
\]
Write $r = |x|$. You may assume the formula for radial functions
$u=u(r,t)$:
\[
\Delta u(|x|,t) = \Delta u(r,t)
= \frac{\partial^2 u}{\partial r^2}(r,t)
+ \frac{2}{r}\frac{\partial u}{\partial r}(r,t).
\]

We consider the wave equation
\[
-\,\frac{\partial^2 u}{\partial t^2}(x,t)
+ \Delta u(x,t) = 0.
\]
```

## CP-III-0022

```tex
\label{prob:cp-iii-0022}
Consider the ODE
\begin{equation}
	-\phi''(x) + \phi(x) = f(x), \qquad f:\mathbb{R}\to\mathbb{C}.
\end{equation}

\par\smallskip\noindent\textbf{(a)}\quad
Assume $f\in\mathcal{S}(\mathbb{R})$.
Taking the Fourier transform of both sides gives
\[
\widehat{-\phi'' + \phi}(\xi)
= -\,\widehat{\phi''}(\xi) + \widehat{\phi}(\xi).
\]

Using the standard identities
\[
\widehat{g'}(\xi) = (2\pi i\xi)\,\widehat{g}(\xi),
\qquad
\widehat{g''}(\xi) = -(2\pi\xi)^{2}\widehat{g}(\xi)
= -4\pi^{2}\xi^{2}\widehat{g}(\xi),
\]
we obtain
\[
-\widehat{\phi''}(\xi) + \widehat{\phi}(\xi)
= 4\pi^{2}\xi^{2}\widehat{\phi}(\xi) + \widehat{\phi}(\xi)
= (4\pi^{2}\xi^{2} + 1)\widehat{\phi}(\xi).
\]

Thus the transformed equation is
\[
(4\pi^{2}\xi^{2} + 1)\,\widehat{\phi}(\xi) = \widehat{f}(\xi),
\]
and hence
\[
\boxed{
	\widehat{\phi}(\xi)
	= \frac{\widehat{f}(\xi)}{1 + 4\pi^{2}\xi^{2}}.
}
\]

Since the multiplier $(1+4\pi^{2}\xi^{2})^{-1}$ is smooth and rapidly decaying,
multiplication by it preserves the Schwartz class.
Thus $\phi\in\mathcal{S}(\mathbb{R})$.

The homogeneous equation $-\psi''+\psi=0$ has solutions
$\psi(x)=Ce^{x}+De^{-x}$, none of which lie in $\mathcal{S}$ unless $C=D=0$.
Hence the solution in $\mathcal{S}$ is unique.

\par\smallskip\noindent\textbf{(b)}\quad
Define the Green's function
\[
G(x) =
\begin{cases}
	\frac12 e^{x}, & x<0,\\[0.3em]
	\frac12 e^{-x}, & x\ge 0.
\end{cases}
\]
A direct calculation yields
\[
\widehat{G}(\xi)
= \frac{1}{1+4\pi^{2}\xi^{2}}.
\]
Thus from part (a),
\[
\widehat{\phi}(\xi)
= \widehat{f}(\xi)\,\widehat{G}(\xi)
= \widehat{\,f*G\,}(\xi).
\]
By injectivity of the Fourier transform,
\[
\boxed{
	\phi(x) = (f*G)(x)
	= \int_{\mathbb{R}} f(y)\,G(x-y)\,dy.
}
\]
```

## CP-III-0002

```tex
\label{prob:cp-iii-0002}
Show that if the coefficients $c_g$ satisfy
\[
|c_g| \le K(1+|g|)^N
\]
for some $K>0$ and some $N\in\mathbb{N}$, then the series of distributions
\[
\sum_{g\in\mathbb{Z}^n} c_g\,\delta_{2\pi g}
\]
converges in $\mathcal{S}'$.

\par\smallskip\noindent\textbf{Theory for Exercise 5.3}\quad

Let $\mathcal{S}(\mathbb{R}^n)$ denote the Schwartz space of rapidly
decreasing smooth functions and $\mathcal{S}'(\mathbb{R}^n)$ its
topological dual, the space of tempered distributions.  A series
$\sum_{k} T_k$ with $T_k\in\mathcal{S}'$ converges in $\mathcal{S}'$ if
and only if the partial sums converge pointwise on $\mathcal{S}$, i.e.
for every $\varphi\in\mathcal{S}$ the scalar series
$\sum_k T_k[\varphi]$ converges.

For $x\in\mathbb{R}^n$, the Dirac delta $\delta_x$ is the tempered
distribution defined by $\delta_x[\varphi]=\varphi(x)$.  In Exercise~5.3
one considers
\[
T = \sum_{g\in\mathbb{Z}^n} c_g\,\delta_{2\pi g},
\]
which formally acts on $\varphi\in\mathcal{S}$ by
\[
T[\varphi] = \sum_{g\in\mathbb{Z}^n} c_g\,\varphi(2\pi g).
\]
The growth condition $|c_g|\le K(1+|g|)^N$ means that the coefficients
grow at most polynomially.  On the other hand, for each
$\varphi\in\mathcal{S}$ and every $M\ge 0$ there exists $C_M>0$ such
that
\[
|\varphi(x)| \le \frac{C_M}{(1+|x|)^M}\qquad\text{for all }x\in\mathbb{R}^n.
\]
Evaluated at $x=2\pi g$ this yields
$|\varphi(2\pi g)|\le C_M(1+|g|)^{-M}$, so that
\[
\sum_{g\in\mathbb{Z}^n} |c_g\varphi(2\pi g)|
\le K C_M \sum_{g\in\mathbb{Z}^n} \frac{1}{(1+|g|)^{M-N}}.
\]
If $M-N$ is chosen large enough (e.g.\ $M-N>n+1$), Exercise~5.2 shows
that this lattice sum converges.  Thus $T[\varphi]$ is well-defined and
absolutely convergent for every $\varphi\in\mathcal{S}$.

Moreover, the estimate above shows that $|T[\varphi]|$ is bounded by a
constant multiple of the Schwartz seminorm
$\sup_x(1+|x|)^M|\varphi(x)|$, which is exactly the form of continuity
required for a tempered distribution.  Hence the weighted $\delta$--comb
$\sum c_g\delta_{2\pi g}$ converges in $\mathcal{S}'$.

\bigskip

\par\medskip\noindent\textbf{Exercise 5.3 — Convergence of $\displaystyle \sum_{g} c_g \delta_{2\pi g}$ in $\mathcal{S}'$}\quad

We assume
\[
|c_g| \le K(1+|g|)^N \qquad (g\in\mathbb{Z}^n)
\]
for some constants $K>0$, $N\in\mathbb{N}$, and want to show that
\[
T := \sum_{g\in\mathbb{Z}^n} c_g\,\delta_{2\pi g}
\]
converges in $\mathcal{S}'(\mathbb{R}^n)$.

\bigskip
\noindent\textbf{Step 1: Define $T$ on a test function}

Take arbitrary $\varphi\in\mathcal{S}(\mathbb{R}^n)$. Formally,
\[
T[\varphi]
= \sum_{g} c_g\,\delta_{2\pi g}[\varphi]
= \sum_{g} c_g\,\varphi(2\pi g).
\]
We must show this series converges absolutely and defines a continuous linear functional.

\bigskip
\noindent\textbf{Step 2: Use rapid decay of $\varphi$}

Since $\varphi$ is Schwartz, for every integer $M\ge 0$,
\[
\sup_{x\in\mathbb{R}^n} (1+|x|)^M |\varphi(x)| =: C_M < \infty.
\]
Hence for all $g\in\mathbb{Z}^n$,
\[
|\varphi(2\pi g)|
\le \frac{C_M}{(1+|2\pi g|)^M}
\le \frac{C_M'}{(1+|g|)^M},
\]
for some constant $C_M'$ depending on $M$ but not on $g$.

\bigskip
\noindent\textbf{Step 3: Absolute convergence}

Then
\[
\sum_{g} |c_g \varphi(2\pi g)|
\le K C_M' \sum_{g} \frac{1}{(1+|g|)^{M-N}}.
\]
Choose $M$ such that $M-N > n+1$.
By Exercise~5.2, the lattice sum converges.
Hence the series defining $T[\varphi]$ is absolutely convergent.

\bigskip
\noindent\textbf{Step 4: Continuity}

From the same estimate,
\[
|T[\varphi]|
\le C \sup_{x\in\mathbb{R}^n}(1+|x|)^M|\varphi(x)|
\]
for some constant $C>0$ independent of $\varphi$.
Thus $T$ is continuous on $\mathcal{S}$, so $T\in\mathcal{S}'$.

\bigskip
\noindent\textbf{Conclusion:}
The series $\displaystyle \sum_{g} c_g\,\delta_{2\pi g}$ converges in $\mathcal{S}'$.
```

## CP-III-0007

```tex
\label{prob:cp-iii-0007}
\par\smallskip\noindent\textbf{Example B: Heaviside function and Dirac mass.}\quad
Define the Heaviside function
\[
H(x) = \begin{cases}
	0, & x<0,\\[0.3em]
	1, & x\ge 0.
\end{cases}
\]
It induces a regular distribution
$T_H(\varphi)=\int_{\mathbb{R}} H(x)\varphi(x)\,dx$ of order $0$.
Using integration by parts one checks that
\[
\langle H',\varphi\rangle
:= -\langle H,\varphi'\rangle
= \varphi(0) = \langle\delta_0,\varphi\rangle,
\]
so in $\mathcal{D}'(\mathbb{R})$ we have $H'=\delta_0$. Both $T_H$ and
$\delta_0$ are tempered distributions.


\par\smallskip\noindent\textbf{Example C: principal value $\mathrm{P.V.}(1/x)$.}\quad
The distribution
\[
\left\langle \mathrm{P.V.}(1/x),\varphi\right\rangle
:= \lim_{\varepsilon\to 0^+}
\int_{|x|>\varepsilon} \frac{\varphi(x)}{x}\,dx
\]
is not given by a locally integrable function (since $1/x$ is not
integrable near $0$), hence it is not regular. However, the growth of
$1/x$ at infinity is only of order $|x|^{-1}$, so the functional is
continuous on the Schwartz space $\mathcal{S}(\mathbb{R})$, and thus
\[
\mathrm{P.V.}(1/x) \in \mathcal{S}'(\mathbb{R})
\]
is a tempered distribution.


\begin{center}
	\begin{tabular}{l|l|l|l}
		Object & Regular? & Tempered? & Order \\ \hline
		$f\in L^1_{\mathrm{loc}}$, moderate growth
		& yes ($T_f$) & yes & $0$ \\[0.2em]
		$H$ (Heaviside) & yes & yes & $0$ \\[0.2em]
		$\delta_0$ & no (not $L^1_{\mathrm{loc}}$)
		& yes & $0$ \\[0.2em]
		$\delta_0'$ & no & yes & $1$ \\[0.2em]
		$\mathrm{P.V.}(1/x)$ & no & yes & $1$ \\[0.2em]
		$e^{x^2}$ (as $T_f$) & yes & \emph{no} (too fast growth) & $0$
	\end{tabular}
\end{center}
```

## CP-III-0012

```tex
\label{prob:cp-iii-0012}
\par\smallskip\noindent\textbf{Example A: regular tempered distribution $T_f$.}\quad
Let $f(x)=\dfrac{\sin x}{1+x^2}$. Then $f\in L^1_{\mathrm{loc}}(\mathbb{R})$
and even $f\in\mathcal{S}(\mathbb{R})$, so the functional
\[
\langle T_f,\varphi\rangle := \int_{\mathbb{R}} f(x)\,\varphi(x)\,dx,
\qquad \varphi\in\mathcal{D}(\mathbb{R}),
\]
defines a regular distribution of order $0$. Since $f$ is rapidly
decreasing, $T_f$ is a tempered distribution as well
($T_f\in\mathcal{S}'(\mathbb{R})$).


\par\smallskip\noindent\textbf{Concrete action of a regular distribution.}\quad
Let
\[
f(x) = \frac{\sin x}{1+x^2},
\]
and let $\varphi\in C_c^\infty(\mathbb{R})$ be a smooth bump supported
in $(-2,2)$ (for instance
$\displaystyle \varphi(x) = C\exp\!\bigl(-1/(1-(x/2)^2)\bigr)$ for
$|x|<2$ and $0$ otherwise, with $C$ chosen so that $\int\varphi=1$).
The regular distribution $T_f$ acts by
\[
\langle T_f,\varphi\rangle
= \int_{\mathbb{R}} f(x)\,\varphi(x)\,dx.
\]
The integrand is the pointwise product $f(x)\varphi(x)$.
```

## CP-III-0020

```tex
\label{prob:cp-iii-0020}
\par\smallskip\noindent\textbf{Example A (one–dimensional box).}\quad
Let $f(x)=\mathbf 1_{[-R,R]}(x)$. Then $\|f\|_{L^1}=2R$ and
\[
\widehat f(\xi)=\int_{-R}^{R} e^{-ix\xi}\,dx
=\frac{2\sin(R\xi)}{\xi}, \qquad \widehat f(0)=2R .
\]
For $k\in\mathbb N$,
\[
\widehat f^{(k)}(\xi)=\int_{-R}^{R} (-ix)^k e^{-ix\xi}\,dx,
\]
so
\[
\sup_{\xi\in\mathbb R}\big|\widehat f^{(k)}(\xi)\big|
\le \int_{-R}^{R} |x|^k\,dx
=\frac{2}{k+1}\,R^{k+1}
\le 2R^{k+1}
= R^{k}\,\|f\|_{L^1}.
\]
Thus the bound in Problem~9 holds (even with the sharper factor $\tfrac{2}{k+1}R^{k+1}$).
Explicitly,
\[
\widehat f(\xi)=\frac{2\sin(R\xi)}{\xi},\qquad
\widehat f'(\xi)=2\,\frac{R\xi\cos(R\xi)-\sin(R\xi)}{\xi^2},
\]
and similarly for higher derivatives; all are continuous at $\xi=0$ by removing the singularity.

\bigskip

\par\smallskip\noindent\textbf{Example B (smooth compactly supported bump).}\quad
Let
\[
f(x)=
\begin{cases}
	\exp\!\big(-\frac{1}{1-x^2}\big), & |x|<1,\\[2pt]
	0, & |x|\ge 1.
\end{cases}
\]
Then $R=1$, $\|f\|_{L^1}=\int_{-1}^{1} e^{-1/(1-x^2)}\,dx<\infty$, and for each $k$,
\[
\widehat f^{(k)}(\xi)=\int_{-1}^{1} (-ix)^k f(x)\,e^{-ix\xi}\,dx
\quad\Rightarrow\quad
\sup_{\xi} |\widehat f^{(k)}(\xi)|
\le \int_{-1}^{1} |x|^{k} f(x)\,dx
\le \|f\|_{L^1}.
\]
Hence $\sup_{\xi} |\widehat f^{(k)}(\xi)| \le 1^{k}\|f\|_{L^1}$, which matches the Problem~9 estimate with $R=1$.
(In fact $\widehat f$ is Schwartz: all derivatives decay faster than any power.)

\bigskip

\par\smallskip\noindent\textbf{Example C (indicator of a ball in $\mathbb R^n$).}\quad
For $f=\mathbf 1_{B_R(0)}$, one has the radial formula
\[
\widehat f(\xi)
= |B_R|\;\frac{2\,J_{n/2}(R|\xi|)}{(R|\xi|)^{n/2}},
\]
where $J_\nu$ is the Bessel function. This is an entire function of $\xi$.
Moreover,
\[
\sup_{\xi\in\mathbb R^n} \big|D_\xi^\alpha \widehat f(\xi)\big|
\le R^{|\alpha|}\,\|f\|_{L^1}
= R^{|\alpha|}\,|B_R|,
\]
in agreement with Problem~9.


\medskip

\noindent\textit{Interpretation.}
The top panel shows a compactly supported function in space; the bottom shows how compact support translates into entire,
oscillatory behavior in the frequency domain.
The oscillations of $J_1(R|\xi|)/(R|\xi|)$ illustrate the uncertainty principle:
a sharp spatial cutoff produces infinitely extended, slowly decaying oscillations in frequency.
The bound $\pi R^{|\alpha|+2}$ controls the amplitude of all derivatives of $\widehat f$ uniformly over~$\xi$.

\clearpage


\par\medskip\noindent\textbf{Powered modulus as a distribution and its PDE uses}\quad

\par\smallskip\noindent\textbf{Regular and singular regimes.}\quad
For $f_\alpha(x)=|x|^{-\alpha}$ on $\mathbb{R}^n$ one has
\[
f_\alpha\in L^1_{\mathrm{loc}}(\mathbb{R}^n)\ \iff\ \alpha<n.
\]
Hence, for $\alpha<n$ the distribution $u_\alpha$ is regular:
\[
u_\alpha[\phi]=\int_{\mathbb{R}^n}|x|^{-\alpha}\,\phi(x)\,dx,\qquad \phi\in\mathcal{D}(\mathbb{R}^n).
\]
At $\alpha=n$ one defines the homogeneous principal value $\operatorname{pv}(|x|^{-n})\in\mathcal{S}'$;
for $\alpha>n$ one obtains higher–order homogeneous distributions (finite sums of derivatives of principal values).

\bigskip

\par\smallskip\noindent\textbf{Distributional derivatives and homogeneity.}\quad
For $\alpha<n$ the classical identities
\[
\partial_i(|x|^{-\alpha})=-\alpha\,\frac{x_i}{|x|^{\alpha+2}},\qquad
\partial_{ij}(|x|^{-\alpha})=\alpha(\alpha+2)\frac{x_i x_j}{|x|^{\alpha+4}}
-\alpha\,\frac{\delta_{ij}}{|x|^{\alpha+2}}
\]
hold pointwise away from $0$ and define homogeneous distributions of degrees $-\alpha-1$ and $-\alpha-2$.
In general,
\[
\partial_i u_\alpha[\phi] = -\,u_\alpha[\partial_i\phi],\qquad \phi\in\mathcal{D},
\]
so the derivative is meaningful even when the right–hand sides are not locally integrable.

\bigskip

\par\smallskip\noindent\textbf{Fundamental appearance in PDE.}\quad
For $n\ge3$,
\[
E_n(x)=c_n\,|x|^{2-n},\qquad -\Delta E_n=\delta_0 \ \text{ in } \mathcal{D}'(\mathbb{R}^n),
\]
and for $n=2$, $E_2(x)=c\,\log|x|$.
Thus $u=E_n*f$ is a weak solution of $-\Delta u=f$.
More generally, Riesz potentials
\[
I_\alpha f(x)=c_{n,\alpha}\int_{\mathbb{R}^n}\frac{f(y)}{|x-y|^{n-\alpha}}\,dy
\]
use the kernel $|x|^{-(n-\alpha)}$ and realize $(-\Delta)^{-\alpha/2}$.
The fractional Laplacian employs a principal value kernel $|x|^{-n-2s}$:
\[
(-\Delta)^s u(x)=c_{n,s}\,\mathrm{pv}\!\int_{\mathbb{R}^n}\frac{u(x)-u(y)}{|x-y|^{n+2s}}\,dy .
\]

\bigskip

\par\smallskip\noindent\textbf{Benefit of multiplying by test functions.}\quad
Let $\chi\in\mathcal{D}(\mathbb{R}^n)$ be a cutoff. Then $\chi\,|x|^{-\alpha}\in L^1$ for all $\alpha<n$, which localizes the singularity and ensures finiteness of integrals.
Moreover, integration by parts transfers derivatives from the singular kernel to the smooth test function:
\[
\partial_i u_\alpha[\phi] = -\,u_\alpha[\partial_i\phi],
\]
allowing weak formulations such as
\[
\int_{\mathbb{R}^n}\nabla u\cdot\nabla\phi \,dx = \langle f,\phi\rangle,\qquad \phi\in\mathcal{D},
\]
where $f$ may be a distribution (e.g.\ a finite measure or a sum of Dirac masses).
This mechanism underlies Newtonian potentials, Sobolev embeddings (Hardy--Littlewood--Sobolev), and Calder\'on--Zygmund theory.


\par\medskip\noindent\textbf{What integration by parts reveals (distributional viewpoint)}\quad

\par\smallskip\noindent\textbf{Set--up.}\quad
Given $u\in\mathcal D'(\mathbb R^n)$ and $\phi\in\mathcal D(\mathbb R^n)$, the distributional derivative is
\[
\partial_i u[\phi] \;:=\; -\,u[\partial_i\phi].
\]
Passing derivatives to the smooth test $\phi$ is the essence of the weak formulation and the
integration--by--parts (IBP) principle.

\bigskip

\par\smallskip\noindent\textbf{1. Legitimizing singular objects.}\quad
The IBP identity defines $\partial_i u$ for \emph{every} distribution $u$ (including measures and singular kernels).
In particular, for $u_\alpha[\phi]=\int |x|^{-\alpha}\phi$ with $\alpha<n$, one has
\[
\partial_i u_\alpha[\phi] = -\int_{\mathbb R^n} |x|^{-\alpha}\,\partial_i\phi(x)\,dx,
\]
which remains meaningful even though $\partial_i(|x|^{-\alpha})$ may fail to be locally integrable.

\smallskip

\par\smallskip\noindent\textbf{2. Weak solutions with minimal regularity.}\quad
For Poisson on $\Omega\subset\mathbb R^n$,
\[
-\Delta u=f \quad\Longleftrightarrow\quad
\int_\Omega \nabla u\cdot\nabla\phi \,dx \;=\; \langle f,\phi\rangle,
\qquad \forall\,\phi\in\mathcal D(\Omega).
\]
The right--hand side allows $f\in\mathcal D'(\Omega)$, and the left requires only $\nabla u\in L^2_{\mathrm{loc}}$.

\smallskip

\par\smallskip\noindent\textbf{3. Boundary terms and natural conditions.}\quad
For smooth $u,\phi$ on a bounded $\Omega$ with unit outer normal $\nu$,
\[
\int_\Omega \nabla u\cdot\nabla\phi
= -\int_\Omega (\Delta u)\,\phi \,dx + \int_{\partial\Omega} \partial_\nu u\,\phi\,dS.
\]
Choosing $\phi$ that vanishes or not on $\partial\Omega$ exhibits Dirichlet vs.\ Neumann data as boundary distributions.

\smallskip

\par\smallskip\noindent\textbf{4. Energy and coercivity.}\quad
Testing with $\phi=u$ gives
\[
\int_\Omega |\nabla u|^2\,dx \;=\; \langle f,u\rangle
\;\le\; \|f\|_{H^{-1}(\Omega)} \,\|u\|_{H_0^1(\Omega)},
\]
yielding the a priori bound $\|u\|_{H_0^1}\le \|f\|_{H^{-1}}$.

\smallskip

\par\smallskip\noindent\textbf{5. Symmetry and conservation.}\quad
For smooth $u,v$,
\[
\int_\Omega \nabla u\cdot\nabla v
= \int_\Omega u(-\Delta v)
= \int_\Omega v(-\Delta u),
\]
displaying self--adjointness of $-\Delta$; for transport $b\cdot\nabla u$, IBP reveals $\int u\,\operatorname{div}(b\phi)$ and the role of $\operatorname{div}b$.

\smallskip

\par\smallskip\noindent\textbf{6. Detecting concentrated sources.}\quad
For $n\ge3$ and $E(x)=c_n|x|^{2-n}$,
\[
\langle -\Delta E,\phi\rangle
= \lim_{\varepsilon\downarrow0}\!\!\int_{|x|=\varepsilon} c_n\,\partial_\nu(|x|^{2-n})\,\phi\,dS
= \phi(0),
\]
so $-\Delta E=\delta_0$ in $\mathcal D'$. The Dirac mass is revealed \emph{only} after IBP.

\smallskip

\par\smallskip\noindent\textbf{7. Cancellation in singular integrals.}\quad
For the Riesz kernel $K_i(x)=x_i/|x|^{n+1}$,
\[
\Big\langle \mathrm{pv}\,K_i,\,\phi\Big\rangle
= -c_n \lim_{\varepsilon\to0}\int_{|x|>\varepsilon} |x|^{-(n-1)}\,\partial_i\phi(x)\,dx,
\]
so derivatives on $\phi$ expose the oddness/cancellation that underlies $L^p$-boundedness.

\smallskip

\par\smallskip\noindent\textbf{8. Variational structure and Euler--Lagrange.}\quad
For $J(u)=\int_\Omega F(x,u,\nabla u)\,dx$,
the first variation satisfies
\[
J'(u)[\phi]
= \int_\Omega \big(F_u\,\phi + F_{\nabla u}\cdot\nabla\phi\big)\,dx
= \int_\Omega \Big( F_u - \operatorname{div}F_{\nabla u} \Big)\phi\,dx
\]
after IBP. Thus the Euler--Lagrange operator becomes explicit and weak solutions are characterized by $J'(u)[\phi]=0$.

\smallskip

\par\smallskip\noindent\textbf{9. Compatibility with weak limits.}\quad
If $u_k\rightharpoonup u$ in $H^1(\Omega)$, then
\[
\int_\Omega \nabla u_k\cdot\nabla\phi \;\longrightarrow\; \int_\Omega \nabla u\cdot\nabla\phi,
\qquad \forall\,\phi\in\mathcal D(\Omega),
\]
so the weak formulation is stable under weak convergence, enabling compactness methods.

\smallskip

\par\smallskip\noindent\textbf{10. Localization by cutoffs.}\quad
With $\chi\in\mathcal D$,
\[
\chi\,|x|^{-\alpha}\in L^1(\mathbb R^n)\quad\text{for all }\alpha<n,
\]
so testing with $\chi\phi$ isolates a singularity and yields finite quantities that quantify its order.

\bigskip
\bigskip

\par\smallskip\noindent\textbf{Worked sketch A (delta from a Newtonian kernel).}\quad
Let $n\ge3$, $E(x)=c_n|x|^{2-n}$. For $\phi\in\mathcal D(\mathbb R^n)$,
\[
\langle -\Delta E,\phi\rangle
= \langle E,-\Delta\phi\rangle
= \lim_{\varepsilon\downarrow0}\int_{|x|>\varepsilon} E(-\Delta\phi)\,dx
= \lim_{\varepsilon\downarrow0}\int_{|x|=\varepsilon} \partial_\nu E\,\phi\,dS
= \phi(0).
\]

\smallskip

\par\smallskip\noindent\textbf{Worked sketch B (energy from the weak Poisson form).}\quad
If $u\in H_0^1(\Omega)$ solves $\int_\Omega \nabla u\cdot\nabla\phi=\langle f,\phi\rangle$, taking $\phi=u$ gives
\[
\|\nabla u\|_{L^2(\Omega)}^2
= \langle f,u\rangle
\le \|f\|_{H^{-1}(\Omega)}\,\|u\|_{H_0^1(\Omega)}.
\]

\smallskip

\par\smallskip\noindent\textbf{Worked sketch C (Riesz transform cancellation).}\quad
With $K_i(x)=x_i/|x|^{n+1}$ and $\phi\in\mathcal D$,
\[
\Big\langle \mathrm{pv}\,K_i,\,\phi\Big\rangle
= \lim_{\varepsilon\to0}\int_{|x|>\varepsilon} \frac{x_i}{|x|^{n+1}}\,\phi(x)\,dx
= -c_n \lim_{\varepsilon\to0}\int_{|x|>\varepsilon} |x|^{-(n-1)}\,\partial_i\phi(x)\,dx,
\]
making the near--zero cancellation explicit after IBP.

\par\medskip\noindent\textbf{Regular distributions and weak solutions of the Laplacian}\quad

\par\smallskip\noindent\textbf{Regular distributions.}\quad

\smallskip

A distribution $u\in\mathcal D'(\mathbb R^n)$ is \emph{regular} if there exists
$f\in L^1_{\mathrm{loc}}(\mathbb R^n)$ such that
\[
u[\phi]=\int_{\mathbb R^n} f(x)\,\phi(x)\,dx,
\qquad \forall\,\phi\in\mathcal D(\mathbb R^n).
\]
In this case we write $u=u_f$ and view $f$ as the \emph{representative} of $u$.
Since test functions have compact support, $u_f$ is continuous on $\mathcal D$.
(Analogously, any finite Radon measure $\mu$ defines the distribution
$u_\mu[\phi]=\int \phi\,d\mu$.)

\bigskip

\par\smallskip\noindent\textbf{Weak solutions of $-\Delta u=f$ on $\Omega$.}\quad

\smallskip

Let $\Omega\subset\mathbb R^n$ be open and let $f\in\mathcal D'(\Omega)$.
A function $u\in H^1_{\mathrm{loc}}(\Omega)$ is a \emph{weak solution} of
\[
-\Delta u=f \quad\text{in }\Omega
\]
if
\[
\int_{\Omega} \nabla u(x)\cdot \nabla \phi(x)\,dx
\;=\; \langle f,\phi\rangle,
\qquad \forall\,\phi\in\mathcal D(\Omega).
\]
If $f\in H^{-1}(\Omega)$ and $u\in H^1(\Omega)$, the right--hand side denotes the
$H^{-1}$--$H_0^1$ duality pairing.

\smallskip

With \emph{homogeneous Dirichlet} boundary condition we require $u\in H_0^1(\Omega)$ and
\[
\int_{\Omega} \nabla u\cdot \nabla \phi\,dx = \langle f,\phi\rangle
\qquad \forall\,\phi\in H_0^1(\Omega).
\]
The case $f=0$ yields weakly harmonic functions:
\[
\int_{\Omega} \nabla u\cdot\nabla \phi\,dx = 0
\qquad \forall\,\phi\in \mathcal D(\Omega) \ \ (\text{or }H_0^1(\Omega)).
\]


\medskip

\noindent\textit{Verification (numeric).} For smooth bumps $\phi$ supported inside $(-1,1)$ we observe
$\int u'(x)\phi'(x)\,dx \approx \int f(x)\phi(x)\,dx$ up to discretization error (see the accompanying text file).

\par\medskip\noindent\textbf{Interpretation of the weak solution example}\quad

\par\smallskip\noindent\textbf{1. The problem.}\quad
We consider the one--dimensional Poisson equation
\[
-\,u''(x)=f(x), \qquad x\in(-1,1),
\]
with homogeneous Dirichlet boundary conditions
\[
u(-1)=u(1)=0,
\]
and with right--hand side
\[
f(x)=
\begin{cases}
	1, & |x|\le \tfrac12,\\[3pt]
	0, & |x|> \tfrac12.
\end{cases}
\]
Hence $f$ is a two--valued step function, equal to $1$ on the interval $[-0.5,0.5]$ and $0$ elsewhere.

\bigskip

\par\smallskip\noindent\textbf{2. Meaning of ``negated second derivative''.}\quad
Formally, the equation $-u''=f$ requires $u''=-f$.
Since $f$ is discontinuous, its classical antiderivatives cannot be twice continuously differentiable.
Thus $u$ cannot be a classical $C^2$ solution.
Instead, we interpret the equation in the \emph{weak sense}:
\[
\int_{-1}^{1} u'(x)\,\phi'(x)\,dx
=\int_{-1}^{1} f(x)\,\phi(x)\,dx,
\qquad \forall\,\phi\in C_c^\infty(-1,1).
\]
This means that the \emph{distributional second derivative} of $u$ equals $-f$.

\bigskip

\par\smallskip\noindent\textbf{3. Shape of the solution.}\quad
The weak solution $u$ is continuous, piecewise $C^1$, and piecewise quadratic:
\[
u(x)=
\begin{cases}
	\frac{1}{2}(x+1)(1.5-x), & 0.5<x\le1,\\[6pt]
	-\tfrac{1}{2}x^2 + \tfrac{1}{2}, & |x|\le0.5,\\[6pt]
	\frac{1}{2}(1-x)(1.5+x), & -1\le x<-0.5.
\end{cases}
\]
The graph of $u$ is symmetric, flat in the center region where $f=1$, and joins linearly to zero at the endpoints $x=\pm1$.
It satisfies $u\in H_0^1(-1,1)$ and $u'\in C([-1,1])$.

\bigskip

\par\smallskip\noindent\textbf{4. Distributional meaning.}\quad
The classical second derivative of $u$ does not exist at $x=\pm0.5$ (the slopes jump there),
but in the sense of distributions one has
\[
u'' = -f + c_1\delta_{-0.5} + c_2\delta_{0.5},
\]
for suitable constants $c_1,c_2$ that ensure continuity of $u'$.
When the weak formulation is tested against functions $\phi$ vanishing at the boundary of the support of $f$,
the Dirac terms cancel and the identity $\langle u'',\phi\rangle=-\!\int f\phi$ holds.
Hence $u''=-f$ \emph{as a distribution}.

\bigskip

\par\smallskip\noindent\textbf{5. What this example demonstrates.}\quad
\begin{itemize}
	\item The right--hand side $f$ is merely $L^2$ (discontinuous), yet a weak solution exists.
	\item $u$ is not twice differentiable, but $u'\in C^0$ and $u''$ exists as a distribution.
	\item The weak formulation captures precisely the integral identity that defines $u$.
	\item This illustrates how weak derivatives extend the notion of differentiability to piecewise smooth functions.
\end{itemize}

\bigskip

\par\smallskip\noindent\textbf{6. Summary of the interpretation.}\quad
The function $u$ constructed above satisfies
\[
\int_{-1}^{1} u'(x)\,\phi'(x)\,dx = \int_{-1}^{1} f(x)\,\phi(x)\,dx
\quad \forall \phi\in C_c^\infty(-1,1),
\]
so that $u''=-f$ in the distributional sense.
In words:
\begin{itemize}
	\item the \emph{negated second derivative} of $u$ reproduces the two--level forcing $f$;
	\item the boundary conditions are encoded in $u\in H_0^1(-1,1)$;
	\item although $u''$ is not classically defined, the weak equation carries the full physical meaning of the Poisson problem.
\end{itemize}
This makes the example a canonical illustration of a weak solution that is not twice classically differentiable but perfectly valid in the variational framework.

\par\medskip\noindent\textbf{Explicit weak solutions via the Dirichlet Green's function on $(-1,1)$}\quad

\par\smallskip\noindent\textbf{Dirichlet Green's function on $(-1,1)$.}\quad
For $-1<x,y<1$ the Green's function is
\[
G(x,y)=
\begin{cases}
	\dfrac{(x+1)(1-y)}{2}, & x\le y,\\[6pt]
	\dfrac{(y+1)(1-x)}{2}, & y\le x,
\end{cases}
\qquad
G(\pm1,y)=0,
\]
and solves $-\,\partial_{xx}G(\cdot,y)=\delta_y$ in $\mathcal D'(-1,1)$.

\bigskip

\par\smallskip\noindent\textbf{Example 1: block forcing $f=\mathbf 1_{[-\frac12,\frac12]}$.}\quad
The weak solution of $-u''=f$ with $u(\pm1)=0$ is
\[
u(x)=\int_{-1/2}^{1/2} G(x,y)\,dy .
\]
Evaluating the integral piecewise in $x$ yields the explicit formula
\[
u(x)=
\begin{cases}
	\dfrac{1}{2}(1+x), & -1\le x<-\dfrac12,\\[8pt]
	-\dfrac{x^2}{2}+\dfrac{3}{8}, & |x|\le\dfrac12,\\[8pt]
	\dfrac{1}{2}(1-x), & \dfrac12<x\le 1.
\end{cases}
\]
Hence $u$ is continuous, $u'\in C([-1,1])$ (piecewise linear), $u''=-1$ on $(-\tfrac12,\tfrac12)$ and
$u''=0$ on the complement, in the \emph{distributional} sense; at $x=\pm\frac12$ the classical second derivative
does not exist but the weak identity
\[
\int_{-1}^1 u'(x)\,\phi'(x)\,dx = \int_{-1}^1 \mathbf 1_{[-1/2,\,1/2]}(x)\,\phi(x)\,dx
\quad\forall \phi\in C_c^\infty(-1,1)
\]
holds. In particular, $u\in H_0^1(-1,1)$ and $-u''=f$ in $\mathcal D'(-1,1)$.

\bigskip

\par\smallskip\noindent\textbf{Example 2: point source $f=\delta_0$ (tent solution).}\quad
The weak solution of $-u''=\delta_0$ with $u(\pm1)=0$ is simply the Green's function at $y=0$:
\[
u(x)=G(x,0)=
\begin{cases}
	\dfrac{x+1}{2}, & x\le 0,\\[6pt]
	\dfrac{1-x}{2}, & x\ge 0,
\end{cases}
\qquad\text{i.e.}\qquad
u(x)=\dfrac{1-|x|}{2}.
\]
Then $u$ is continuous and piecewise linear with
\[
u'(x)=\begin{cases}\dfrac12,& x<0,\\[2pt]-\dfrac12,& x>0,\end{cases}
\qquad
u'' = -\,\delta_0 \ \ \text{in }\mathcal D'(-1,1),
\]
since the jump in $u'$ at $0$ equals $(-\tfrac12)-(\tfrac12)=-1$.
Equivalently,
\[
\int_{-1}^1 u'(x)\,\phi'(x)\,dx=\phi(0)\qquad \forall\,\phi\in C_c^\infty(-1,1),
\]
so indeed $-u''=\delta_0$ in the weak sense.

\bigskip

\par\smallskip\noindent\textbf{Remarks.}\quad
Both examples illustrate how the Green's representation
\[
u(x)=\int_{-1}^1 G(x,y)\,f(y)\,dy
\]
automatically enforces the boundary conditions and yields $u\in H_0^1(-1,1)$ with $-u''=f$ in $\mathcal D'$,
even when $f$ is discontinuous (block) or singular (Dirac).

\clearpage

\par\medskip\noindent\textbf{Green's function on $(-1,1)$ and a block-forcing example}\quad

\par\smallskip\noindent\textbf{Dirichlet Green's function.}\quad
For $-1<x,y<1$,
\[
G(x,y)=
\begin{cases}
	\dfrac{(x+1)(1-y)}{2}, & x\le y,\\[6pt]
	\dfrac{(y+1)(1-x)}{2}, & x\ge y,
\end{cases}
\qquad G(\pm1,y)=0,
\]
and $-\partial_{xx}G(\cdot,y)=\delta_y$ in $\mathcal D'(-1,1)$.

\bigskip

\par\smallskip\noindent\textbf{Example 1 (block forcing).}\quad
Let $f(x)=\mathbf 1_{[-1/2,\,1/2]}(x)$.
The weak solution with $u(\pm1)=0$ is given by
\[
u(x)=\int_{-1/2}^{1/2} G(x,y)\,dy,
\]
which yields after a straightforward split of the integral at $y=x$:
\[
u(x)=
\begin{cases}
	\dfrac{1+x}{2}, & -1\le x<-\dfrac12,\\[8pt]
	-\dfrac{x^2}{2}+\dfrac{3}{8}, & |x|\le \dfrac12,\\[8pt]
	\dfrac{1-x}{2}, & \dfrac12<x\le 1.
\end{cases}
\]
Hence $u\in H_0^1(-1,1)$, $u'$ is continuous and piecewise linear, and in the distributional sense
\[
u'' = -\,\mathbf 1_{[-1/2,\,1/2]}.
\]

\bigskip

\par\smallskip\noindent\textbf{Figures.}\quad


\noindent\emph{Interpretation.} The heatmap and slices display the triangular structure of $G$.
Convolution with the block forcing integrates those triangles over $y\in[-\tfrac12,\tfrac12]$,
producing a piecewise quadratic $u$ that is linear outside the support of $f$ and concave on it.


\clearpage
```

## CP-III-0024

```tex
\label{prob:cp-iii-0024}
\par\smallskip\noindent\textbf{Statement.}\quad
Let $u:\mathcal S(\mathbb R^n)\to\mathbb C$ be linear. Show that $u$ is continuous if and only if there exist $N,k\in\mathbb N$ and $C>0$ such that
\[
|u[\phi]|\le C\,\sup_{x\in\mathbb R^n,\;|\alpha|\le k}\bigl(1+|x|\bigr)^N\,\bigl|D^\alpha\phi(x)\bigr|
\qquad\text{for all }\phi\in\mathcal S(\mathbb R^n).
\]

\par\smallskip\noindent\textbf{Proof.}\quad

The topology of $\mathcal S(\mathbb R^n)$ is generated by the seminorms
\[
p_{N,k}(\phi)=\sup_{x\in\mathbb R^n,\;|\alpha|\le k} (1+|x|)^N\,|D^\alpha\phi(x)|.
\]

($\Rightarrow$) If $u$ is continuous at $0$, there exist finitely many seminorms $p_{N_j,k_j}$ and constants $C_j$ with
$|u[\phi]|\le \sum_j C_j\,p_{N_j,k_j}(\phi)$. Let $N=\max_j N_j$, $k=\max_j k_j$, $C=\sum_j C_j$. Since $p_{N_j,k_j}\le p_{N,k}$,
\[
|u[\phi]|\le C\,p_{N,k}(\phi).
\]

($\Leftarrow$) Conversely, if $|u[\phi]|\le C\,p_{N,k}(\phi)$ for all $\phi$, then $u$ is continuous because it is dominated by a continuous seminorm. This characterizes continuous linear functionals on $\mathcal S$ (tempered distributions).

% ==========================
% Problem 6 — Examples
% ==========================
\par\smallskip\noindent\textbf{Examples.}\quad

\bigskip

\textbf{Example 1 (integration against polynomially growing functions).}
Let $f$ satisfy $|f(x)|\le C_f(1+|x|)^M$. Define $u_f[\phi]=\int_{\mathbb R^n} f(x)\phi(x)\,dx$.
Then for $N=M$ and $k=0$,
\[
|u_f[\phi]|
\le \int |f(x)|\,|\phi(x)|\,dx
\le C_f \int (1+|x|)^N |\phi(x)|\,dx
\le C\, \sup_{x} (1+|x|)^N |\phi(x)|
= C\,p_{N,0}(\phi),
\]
where the last inequality uses that $\phi\in\mathcal S(\mathbb R^n)$ decays rapidly. Thus $u_f$ is continuous.

\medskip

\textbf{Example 2 (derivatives of the Dirac delta).}
For $\beta\in\mathbb N^n$, $u=\partial^\beta\delta$ satisfies
\[
|u[\phi]|=|\partial^\beta\phi(0)|
\le \sup_{x} \sum_{|\alpha|\le |\beta|} |D^\alpha\phi(x)|
\le p_{0,|\beta|}(\phi).
\]
Hence the criterion holds with $N=0$, $k=|\beta|$.

\medskip

\textbf{Example 3 (moment functionals).}
Fix a multi-index $\gamma$. Define $m_\gamma[\phi]=\int_{\mathbb R^n} x^\gamma \phi(x)\,dx$.
Since $|x^\gamma|\le (1+|x|)^{|\gamma|}$,
\[
|m_\gamma[\phi]|
\le \int (1+|x|)^{|\gamma|} |\phi(x)|\,dx
\le C\, p_{|\gamma|,0}(\phi).
\]
Thus $m_\gamma$ is continuous with $N=|\gamma|$, $k=0$.

\medskip

\textbf{Example 4 (finite order differential operators with polynomial coefficients).}
Let $P(x,D)=\sum_{|\alpha|\le m} a_\alpha(x) D^\alpha$, with $|a_\alpha(x)|\le C(1+|x|)^M$.
Define $u_P[\phi]=\int_{\mathbb R^n} (P(x,D)\phi)(x)\,dx$.
Then by Leibniz' rule and the polynomial bound on $a_\alpha$,
\[
|u_P[\phi]|
\le \sum_{|\alpha|\le m} \int |a_\alpha(x)|\,|D^\alpha\phi(x)|\,dx
\le C'\,\sup_{x,\,|\alpha|\le m} (1+|x|)^M |D^\alpha\phi(x)|
= C'\,p_{M,m}(\phi),
\]
so $u_P$ is continuous.

\medskip

\textbf{Example 5 (a non-example by violating the bound).}
If $L:\mathcal S(\mathbb R)\to\mathbb C$ is a discontinuous linear functional (e.g. defined on a Hamel basis),
then no choice of $N,k,C$ can satisfy the inequality, because such a bound would force continuity with respect to the Schwartz topology. Therefore the criterion is sharp: it characterizes exactly the continuous linear maps $\mathcal S\to\mathbb C$.


\par\smallskip\noindent\textbf{Examples.}\quad

If $f$ has at most polynomial growth, $u_f[\phi]=\int_{\mathbb R^n} f(x)\phi(x)\,dx$ satisfies the bound with some $N$ and $k=0$.
For $u=\partial^\beta\delta$, one has $|u[\phi]|=|\partial^\beta\phi(0)|\le p_{0,|\beta|}(\phi)$.


\par\medskip\noindent\textbf{The three duals below the diagram}\quad

\par\smallskip\noindent\textbf{$\mathcal E'(\mathbb R^n)$: compactly supported distributions.}\quad
This is the continuous dual of $\mathcal E(\mathbb R^n)=C^\infty(\mathbb R^n)$ with its Fr\'echet topology.
A distribution $u$ belongs to $\mathcal E'$ if and only if $\operatorname{supp}u$ is compact.
Equivalently, every $u\in\mathcal E'$ is of finite order and acts by
\[
u[\phi]=\sum_{|\alpha|\le m}\int_{\mathbb R^n} f_\alpha(x)\,D^\alpha\phi(x)\,dx,
\qquad f_\alpha\in C_c(\mathbb R^n).
\]
Convolution with $\psi\in C_c^\infty$ preserves $C_c^\infty$, and $u$ has finite order.
\emph{Paley--Wiener:} $\widehat{u}$ is an entire function on $\mathbb C^n$ of exponential type with polynomial growth on horizontal strips.
Examples include finite linear combinations of $\delta_a$ and their derivatives, and $f\in C_c^\infty$ as regular distributions.

\bigskip

\par\smallskip\noindent\textbf{$\mathcal S'(\mathbb R^n)$: tempered distributions.}\quad
This is the continuous dual of the Schwartz space $\mathcal S(\mathbb R^n)$.
A linear functional $u$ is tempered iff there exist $N,k\in\mathbb N$ and $C>0$ with
\[
|u[\phi]|\le C\,\sup_{x\in\mathbb R^n,\;|\alpha|\le k}(1+|x|)^N\,|D^\alpha\phi(x)|,
\qquad \phi\in\mathcal S(\mathbb R^n).
\]
Thus $u$ has at most polynomial growth at infinity. The space $\mathcal S'$ is closed under differentiation, translation,
multiplication by polynomials, and the Fourier transform $\mathcal F:\mathcal S'\to\mathcal S'$ is a topological isomorphism.
Examples: $\mathcal E'$ (hence Dirac and its derivatives), polynomials, finite Borel measures,
locally integrable functions with polynomial growth, and principal value distributions such as $\operatorname{pv}(1/x)$.

\bigskip

\par\smallskip\noindent\textbf{$\mathcal D'(\mathbb R^n)$: all distributions.}\quad
This is the continuous dual of $\mathcal D(\mathbb R^n)=C_c^\infty(\mathbb R^n)$ with its LF topology.
Locally (on each compact $K$), there exist $m$ and $C$ such that
\[
|u[\phi]|\le C\sum_{|\alpha|\le m}\sup_{x\in K}|D^\alpha\phi(x)|,
\qquad \text{for all }\phi\in\mathcal D(\mathbb R^n)\text{ with }\operatorname{supp}\phi\subset K.
\]
We have strict inclusions $\mathcal E'(\mathbb R^n)\subset \mathcal S'(\mathbb R^n)\subset \mathcal D'(\mathbb R^n)$.
The space $\mathcal D'$ is stable under differentiation, multiplication by $C^\infty$ functions,
and convolution with $C_c^\infty$ test functions.
It also contains distributions of super-polynomial growth at infinity.

\bigskip

\par\smallskip\noindent\textbf{Duality picture and topologies.}\quad
The inclusions $\mathcal D\subset\mathcal S\subset\mathcal E$ induce the reversed inclusions
\[
\mathcal E'(\mathbb R^n)\subset \mathcal S'(\mathbb R^n)\subset \mathcal D'(\mathbb R^n),
\]
each endowed with the weak-$^\ast$ topology:
$\sigma(\mathcal E',\mathcal E)$, $\sigma(\mathcal S',\mathcal S)$, and $\sigma(\mathcal D',\mathcal D)$.


\par\medskip\noindent\textbf{Distributions and the LF topology}\quad

\par\smallskip\noindent\textbf{Definition (distributions on $\mathbb R^n$).}\quad
Let $\mathcal D(\mathbb R^n)=C_c^\infty(\mathbb R^n)$ be the space of test functions with its LF topology (see below).
A \emph{distribution} on $\mathbb R^n$ is a continuous linear functional $u:\mathcal D(\mathbb R^n)\to\mathbb C$.
Continuity means: for every compact $K\subset\mathbb R^n$ there exist $m\in\mathbb N$ and $C>0$ such that
\[
|u[\phi]|\le C \sum_{|\alpha|\le m}\sup_{x\in K}|D^\alpha\phi(x)|
\qquad\text{whenever }\operatorname{supp}\phi\subset K.
\]
The distributional derivative is defined by
\[
D^\alpha u[\phi]=(-1)^{|\alpha|}\,u[D^\alpha\phi],\qquad \phi\in\mathcal D(\mathbb R^n).
\]
The (local) \emph{order} of $u$ on $K$ is the least such $m$.

\bigskip

\par\smallskip\noindent\textbf{Examples of distributions.}\quad

\bigskip

\textbf{Regular distributions.}
For $f\in L^1_{\mathrm{loc}}(\mathbb R^n)$ define
\[
u_f[\phi]=\int_{\mathbb R^n} f(x)\,\phi(x)\,dx .
\]

\medskip

\textbf{Dirac masses and derivatives.}
At $a\in\mathbb R^n$,
\[
\delta_a[\phi]=\phi(a),
\qquad
D^\alpha\delta_a[\phi]=(-1)^{|\alpha|}\,\partial^\alpha\phi(a).
\]

\medskip

\textbf{Principal values.}
In one dimension,
\[
\operatorname{pv}\!\left(\frac{1}{x}\right)[\phi]
=\lim_{\varepsilon\downarrow0}\int_{|x|>\varepsilon}\frac{\phi(x)}{x}\,dx .
\]

\medskip

\textbf{Finite Borel measures.}
For a finite measure $\mu$,
\[
\mu[\phi]=\int_{\mathbb R^n}\phi\,d\mu .
\]

\medskip

\textbf{Compactly supported distributions.}
Elements of $\mathcal E'(\mathbb R^n)$ satisfy $\operatorname{supp}u\Subset\mathbb R^n$.

\medskip

\textbf{Surface distributions.}
If $\Sigma$ is a smooth submanifold with surface measure $d\sigma$,
\[
u[\phi]=\int_{\Sigma}\phi\,d\sigma ,
\]
and one may also consider normal–derivative distributions supported on $\Sigma$.

\medskip

\textbf{Fundamental solutions.}
For the Laplacian,
\[
\Delta E_n=\delta_0,\qquad
E_2(x)=c\,\log|x|,\qquad
E_n(x)=c_n\,|x|^{2-n}\quad(n\ge3).
\]

\medskip

\textbf{Tempered/oscillatory examples.}
In $\mathcal S'$, plane waves arise as limits of cutoffs:
\[
u[\phi]=\lim_{\varepsilon\downarrow0}\int_{\mathbb R^n}
e^{i\langle\xi,x\rangle}\,\chi(\varepsilon x)\,\phi(x)\,dx ,
\]
with $\chi\in C_c^\infty$ and $\chi(0)=1$.


\bigskip

\par\smallskip\noindent\textbf{Convergence patterns in $\mathcal D$ (useful for testing).}\quad
Mollifiers $\eta_\varepsilon=\varepsilon^{-n}\eta(\cdot/\varepsilon)$ with $\eta\in\mathcal D$ and $\int\eta=1$ satisfy $\eta_\varepsilon\to\delta$ in $\mathcal D'$.
For $f\in L^1_{\mathrm{loc}}$, $f\ast\eta_\varepsilon\to f$ in $L^1_{\mathrm{loc}}$ and hence $u_{f\ast\eta_\varepsilon}\to u_f$ in $\mathcal D'$.
Difference quotients obey $\Delta_i^h u\to D_i u$ in the weak-$^\ast$ topology $\sigma(\mathcal D',\mathcal D)$.

\bigskip

\par\smallskip\noindent\textbf{Definition (LF spaces and the LF topology).}\quad

\smallskip

An \emph{LF space} is a locally convex space $E$ that is the (countable) inductive limit of Fr\'echet spaces:
\[
E=\varinjlim_{m\in\mathbb N} E_m, \qquad
E_1 \subset E_2 \subset \cdots \subset E, \ \text{each $E_m$ Fr\'echet.}
\]

\smallskip

The \emph{LF topology} on $E$ is the finest locally convex topology for which each inclusion
$E_m \hookrightarrow E$ is continuous.

\smallskip

A net $(x_\nu)$ converges to $x$ in $E$ iff it is eventually contained in some $E_m$
and converges there in the Fr\'echet topology.

\smallskip

Bounded subsets of $E$ are those absorbed by some $E_m$ and bounded in that $E_m$.

\smallskip

If the inclusions $E_m \hookrightarrow E_{m+1}$ are topologically strict (e.g.\ compact),
one speaks of a \emph{strict} LF space.

\bigskip

\par\smallskip\noindent\textbf{Examples of LF spaces.}\quad

\smallskip

The test function space $\mathcal D(\mathbb R^n)
= \varinjlim_m \mathcal D_{K_m}$, where $\{K_m\}$ exhausts $\mathbb R^n$
and each $\mathcal D_{K}$ is Fr\'echet with seminorms
\[
p_{K,k}(\phi)=\sup_{x\in K,\;|\alpha|\le k} |D^\alpha \phi(x)|.
\]

\smallskip

For a smooth manifold $M$, one has
\[
C_c^\infty(M)=\varinjlim_{K} C^\infty_{K}(M) \quad \text{(LF).}
\]

\smallskip

The space of polynomials
\[
\mathcal P(\mathbb R^n)=\varinjlim_m \mathcal P_{\le m}
\]
(with finite-dimensional Fr\'echet steps) is LF.

\smallskip

The strong dual $\mathcal E'(\mathbb R^n)$ of the Fr\'echet space $\mathcal E(\mathbb R^n)$
is a (DFS) space, i.e.\ an LF-type dual arising as an inductive limit of Banach (or Fr\'echet) steps.

\medskip


\par\smallskip\noindent\textbf{Why LF matters for distributions.}\quad
The LF structure of $\mathcal D$ reduces continuity to uniform estimates on a single compact step $\mathcal D_K$;
convergence in $\mathcal D$ means supports eventually lie in a fixed compact and all derivatives converge uniformly on that compact.
This is precisely the mechanism used to define and manipulate distributions, their derivatives, and approximations by mollifiers.

\par\medskip\noindent\textbf{Locally integrable functions and regular distributions}\quad

\par\smallskip\noindent\textbf{Definition ($L^1_{\mathrm{loc}}(\mathbb R^n)$).}\quad
A function $f:\mathbb R^n\to\mathbb C$ is in $L^1_{\mathrm{loc}}(\mathbb R^n)$ if
\[
\int_K |f(x)|\,dx<\infty \quad \text{for every compact } K\subset\mathbb R^n .
\]
Equivalently, $\int_{B(0,R)} |f|<\infty$ for every $R>0$. No condition at infinity is imposed.

\bigskip

\par\smallskip\noindent\textbf{Regular distributions from $L^1_{\mathrm{loc}}$.}\quad
If $f\in L^1_{\mathrm{loc}}(\mathbb R^n)$, then
\[
u_f[\phi]=\int_{\mathbb R^n} f(x)\,\phi(x)\,dx ,\qquad \phi\in\mathcal D(\mathbb R^n),
\]
defines a continuous linear functional on $\mathcal D(\mathbb R^n)$, i.e.\ a distribution.
Distributional derivatives are given by
\[
D^\alpha f[\phi]=(-1)^{|\alpha|}\int_{\mathbb R^n} f(x)\,D^\alpha\phi(x)\,dx .
\]

\bigskip

\par\smallskip\noindent\textbf{Local integrability tests (polar form near $0$).}\quad
If $f(x)\sim |x|^{-\alpha}$ as $x\to 0$,
\[
\int_{B(0,\varepsilon)} |f(x)|\,dx \;\approx\; C_n\!\int_0^\varepsilon r^{n-1-\alpha}\,dr,
\quad\text{finite $\iff$ } \alpha<n .
\]
Thus $|x|^{-\alpha}\in L^1_{\mathrm{loc}}$ near $0$ exactly when $\alpha<n$.

\bigskip

\par\smallskip\noindent\textbf{Concrete one-dimensional examples ($n=1$).}\quad
(1) $f(x)=|x|^{-1/2}$: $\displaystyle \int_0^\varepsilon x^{-1/2}dx=2\varepsilon^{1/2}<\infty$, hence $f\in L^1_{\mathrm{loc}}(\mathbb R)$.
\medskip

(2) $f(x)=|x|^{-1}$: $\displaystyle \int_0^\varepsilon x^{-1}dx=\infty$, hence $f\notin L^1_{\mathrm{loc}}(\mathbb R)$.
\medskip

(3) $f(x)=\dfrac{1}{1+|x|}$: continuous and bounded on compacts, so $f\in L^1_{\mathrm{loc}}(\mathbb R)$ (indeed $f\in L^1$).
\medskip

(4) $f(x)=\log|x|$: $\displaystyle \int_0^\varepsilon |\log x|\,dx=\varepsilon|\log\varepsilon|-\varepsilon\to0$, hence $\log|x|\in L^1_{\mathrm{loc}}(\mathbb R)$.

\bigskip

\par\smallskip\noindent\textbf{Higher-dimensional examples.}\quad
For $f(x)=|x|^{-\alpha}$ on $\mathbb R^n$,
\[
|x|^{-\alpha}\in L^1_{\mathrm{loc}}(\mathbb R^n) \ \text{near }0
\quad\Longleftrightarrow\quad \alpha<n .
\]
In particular, $|x|^{-1}\in L^1_{\mathrm{loc}}$ for $n\ge2$ but not for $n=1$.

\bigskip

\par\smallskip\noindent\textbf{Extensions.}\quad
The space $L^p_{\mathrm{loc}}(\mathbb R^n)$ is defined by $\int_K |f|^p<\infty$ for all compact $K$.
Elements of $L^1_{\mathrm{loc}}$ always define regular distributions by integration against test functions.
At the borderline $\alpha=n$, principal value distributions (e.g.\ $\operatorname{pv}(1/x)$ in $\mathbb R$) arise, which are tempered but not regular.


\par\medskip\noindent\textbf{Beyond powers: other locally integrable (and non-integrable) examples}\quad

\par\smallskip\noindent\textbf{Log--power families.}\quad
Near $x=0$ in $\mathbb R^n$:
\[
f(x)=|\log|x||^\beta \quad\Rightarrow\quad
\int_{B(0,\varepsilon)} |\log|x||^\beta\,dx
= C_n\!\int_0^\varepsilon r^{\,n-1}|\log r|^\beta\,dr<\infty
\]
for every $\beta\in\mathbb R$. Hence $|\log|x||^\beta\in L^1_{\mathrm{loc}}$.
For $f(x)=|x|^{-\alpha}\,|\log|x||^\beta$ the integrability threshold remains $\alpha<n$; the logarithm does not change the cutoff.

\bigskip

\par\smallskip\noindent\textbf{Oscillatory factors.}\quad
For $\gamma>0$,
\[
f(x)=\frac{\sin(1/|x|^\gamma)}{|x|^\alpha}
\]
is locally integrable near $0$ if and only if $\alpha<n$.
Oscillation does not improve absolute integrability. In one dimension, $\sin(1/x)$ is bounded and thus belongs to $L^1_{\mathrm{loc}}$.

\bigskip

\par\smallskip\noindent\textbf{Exponential-type singularities.}\quad
If
\[
f(x)=\exp\!\big(1/|x|^p\big)\qquad (p>0),
\]
then
\[
\int_{B(0,\varepsilon)} e^{1/|x|^p}\,dx
= C_n\!\int_0^\varepsilon r^{\,n-1} e^{1/r^p}\,dr=\infty,
\]
so $f\notin L^1_{\mathrm{loc}}$.
Conversely, $f(x)=\exp\!\big(-1/|x|^p\big)$ is smooth and bounded near $0$, hence in $L^1_{\mathrm{loc}}$.

\bigskip

\par\smallskip\noindent\textbf{Rational functions.}\quad
If $f(x)=P(x)/Q(x)$ and $Q$ has no zeros on a compact $K$, then $f$ is bounded on $K$ and thus $L^1_{\mathrm{loc}}$.
If $Q$ vanishes at $a$, one has the local model $|x-a|^{-m}$; integrability near $a$ reduces to the power test with exponent $\alpha=m$.

\bigskip

\par\smallskip\noindent\textbf{Piecewise and measure-theoretic examples.}\quad
Jump functions (e.g.\ the sign or Heaviside function) and piecewise constants are bounded and therefore lie in $L^1_{\mathrm{loc}}$.
For a measurable set $E$, the indicator $\mathbf 1_E$ belongs to $L^1_{\mathrm{loc}}$ iff $m(E\cap K)<\infty$ for every compact $K$.
Removable singularities, such as $\frac{\sin x}{x}$ extended by continuity at $0$, yield locally integrable functions.

\bigskip

\par\smallskip\noindent\textbf{Behaviour at infinity.}\quad
Membership in $L^1_{\mathrm{loc}}$ imposes no restriction at infinity: functions such as $e^{|x|^2}$ or $(1+|x|)^p$ belong to $L^1_{\mathrm{loc}}$ even though they may fail to be in $L^1(\mathbb R^n)$.

\bigskip

\par\smallskip\noindent\textbf{Distributional viewpoint.}\quad
Each $f\in L^1_{\mathrm{loc}}(\mathbb R^n)$ defines a regular distribution
\[
u_f[\phi]=\int_{\mathbb R^n} f(x)\,\phi(x)\,dx,\qquad \phi\in\mathcal D(\mathbb R^n).
\]
Borderline non-integrable cases (e.g.\ $|x|^{-n}$ or $e^{1/|x|^p}$) may still yield distributions via renormalization (principal values), but they are not regular distributions.
```

## CP-III-0025

```tex
\label{prob:cp-iii-0025}
$\displaystyle \int_{\mathbb{R}^n}\phi(x)\,dx = 1$.
For $\varepsilon>0$ we set
\[
\phi_\varepsilon(x)
:= \frac{1}{\varepsilon^n}\,\phi\!\left(\frac{x}{\varepsilon}\right).
\]
Each $\phi_\varepsilon$ is smooth and compactly supported, hence
\[
\phi_\varepsilon \in C_c^\infty(\mathbb{R}^n)
= \mathcal{D}(\mathbb{R}^n).
\]
Thus, in the framework of $\mathcal{D}'(\mathbb{R}^n)$, \emph{standard
	mollifiers are particular test functions} which additionally satisfy
the approximate identity properties
\[
\phi_\varepsilon \ge 0,\qquad
\int \phi_\varepsilon = 1,\qquad
\phi_\varepsilon \to \delta_0 \ \text{in }\mathcal{D}'.
\]

\par\smallskip\noindent\textbf{Gaussian mollifiers.}\quad
One often also uses the Gaussian kernels
\[
\eta_\varepsilon(x)
:= \frac{1}{(2\pi\varepsilon^2)^{n/2}}
e^{-\frac{|x|^2}{2\varepsilon^2}},\qquad \varepsilon>0.
\]
These functions are smooth and rapidly decaying, but not compactly
supported. Hence
\[
\eta_\varepsilon \notin \mathcal{D}(\mathbb{R}^n),
\]
where compact support is required, but
\[
\eta_\varepsilon \in \mathcal{S}(\mathbb{R}^n),
\]
the Schwartz space of rapidly decreasing smooth functions.  They also
form an approximate identity, now in the sense of tempered
distributions.

\par\smallskip\noindent\textbf{Relation to tempered test functions and tempered distributions.}\quad
Recall that
\[
\mathcal{D}(\mathbb{R}^n) = C_c^\infty(\mathbb{R}^n)
\]
is the test function space for \emph{distributions}
$\mathcal{D}'(\mathbb{R}^n)$, while
\[
\mathcal{S}(\mathbb{R}^n)
\]
is the test function space for \emph{tempered distributions}
$\mathcal{S}'(\mathbb{R}^n)$ (distributions of at most polynomial
growth).
```

## CP-III-0009

```tex
\label{prob:cp-iii-0009}
\begin{example}[Laplace]
		$L=-\Delta\ \Rightarrow\ L(k)=|k|^2$. Then
		\[
		G(x)=\mathcal{F}^{-1}\!\Big(\frac{1}{|k|^2}\Big)=
		\begin{cases}
			\dfrac{1}{(n-2)\omega_n}\,|x|^{2-n}, & n\ge3,\\[8pt]
			-\dfrac{1}{2\pi}\log|x|, & n=2,
		\end{cases}
		\]
		reproducing the fundamental solutions.
	\end{example}
```
