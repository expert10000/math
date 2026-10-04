# Part II missing-solution batch 21

- problems: **5**
- IDs: CP-II-0480, CP-II-0485, CP-II-0496, CP-II-0510, CP-II-0550

## CP-II-0480

- chapter line: 23440

```tex
\label{prob:cp-ii-0480}
— Embeddings, interpolation, and local $L^p$

\tighthrule
\begin{spacy}
	\textbf{Statement.}
	Let $(E,\mathcal E,\mu)$ be a measure space.

		\par\noindent\textbullet\quad If $\mu(E)<\infty$ and $f\in L^{p}(E)$ with $1\le q\le p\le\infty$, then $f\in L^{q}(E)$ and
		\[
		\|f\|_{L^{q}} \;\le\; \mu(E)^{\frac{p-q}{pq}}\;\|f\|_{L^{p}}.
		\]
		\par\noindent\textbullet\quad Suppose $f\in L^{p_{0}}(E)\cap L^{p_{1}}(E)$ with $0<p_{0}<p_{1}\le\infty$.
		For $0\le \theta\le 1$ define $p_{\theta}$ by
		\[
		\frac{1}{p_{\theta}}=\frac{1-\theta}{p_{0}}+\frac{\theta}{p_{1}}.
		\]
		Then $f\in L^{p_{\theta}}(E)$ and
		\[
		\|f\|_{L^{p_{\theta}}} \;\le\; \|f\|_{L^{p_{0}}}^{\,1-\theta}\,\|f\|_{L^{p_{1}}}^{\,\theta}.
		\]
		\par\noindent\textbullet\quad On $\mathbb R^{n}$ show that if $p_{1}\neq p_{2}$ then
		$L^{p_{1}}(\mathbb R^{n})\not\subset L^{p_{2}}(\mathbb R^{n})$.
		Determine for which $p_{1},p_{2}$ we have
		$L^{p_{1}}_{\mathrm{loc}}(\mathbb R^{n}) \subset L^{p_{2}}_{\mathrm{loc}}(\mathbb R^{n})$.

	\tighthrule

	\textbf{Theory (quick toolkit).}

		\par\noindent\textbullet\quad On sets of finite measure: for $1\le q\le p\le\infty$,
		\[
		\|h\|_{L^{q}(E)} \le \mu(E)^{\frac{1}{q}-\frac{1}{p}}\,\|h\|_{L^{p}(E)}.
		\]
		This is Hölder with exponents $\frac{p}{q}$ and $\frac{p}{p-q}$.
		\par\noindent\textbullet\quad Real interpolation for $L^p$:
		If $1\le p_{0}<p_{1}\le\infty$ and $\frac1{p_{\theta}}=\frac{1-\theta}{p_{0}}+\frac{\theta}{p_{1}}$, then
		\[
		L^{p_{0}}\cap L^{p_{1}} \hookrightarrow L^{p_{\theta}},\qquad
		\|f\|_{p_{\theta}}\le \|f\|_{p_{0}}^{1-\theta}\|f\|_{p_{1}}^{\theta}.
		\]
		\par\noindent\textbullet\quad On bounded $K\subset\mathbb R^{n}$: if $p_{1}\ge p_{2}$,
		\[
		\|h\|_{L^{p_{2}}(K)} \le |K|^{\frac1{p_{2}}-\frac1{p_{1}}}\,\|h\|_{L^{p_{1}}(K)}.
		\]
		Hence $L^{p_{1}}_{\mathrm{loc}}\subset L^{p_{2}}_{\mathrm{loc}}$ iff $p_{1}\ge p_{2}$.

	\tighthrule

	\textbf{Proof.}

	\emph{(a) Finite-measure embedding.}
	For $p<\infty$, apply Hölder to $|f|^{q}\cdot 1$ with exponents $\tfrac{p}{q}$ and $\tfrac{p}{p-q}$:
	\[
	\int_E |f|^{q}
	\le \Bigl(\int_E |f|^{p}\Bigr)^{q/p}\,\mu(E)^{1-\frac{q}{p}}.
	\]
	Taking the $q$th root gives
	$\|f\|_{q}\le \mu(E)^{\frac{p-q}{pq}}\|f\|_{p}$.
	For $p=\infty$, $\|f\|_{q}^{q}\le \|f\|_{\infty}^{q}\mu(E)$.

	\medskip

	\emph{(b) Interpolation between $L^{p_{0}}$ and $L^{p_{1}}$.}
	For $p_{1}<\infty$,
	\[
	|f|^{p_{\theta}}
	= \bigl(|f|^{p_{0}}\bigr)^{(1-\theta)\frac{p_{\theta}}{p_{0}}}
	\bigl(|f|^{p_{1}}\bigr)^{\theta\frac{p_{\theta}}{p_{1}}}.
	\]
	With Hölder exponents
	$a=\frac{p_{0}}{(1-\theta)p_{\theta}}$ and $b=\frac{p_{1}}{\theta p_{\theta}}$ (conjugate by the definition of $p_\theta$),
	\[
	\int |f|^{p_{\theta}}
	\le \Bigl(\int |f|^{p_{0}}\Bigr)^{(1-\theta)\frac{p_{\theta}}{p_{0}}}
	\Bigl(\int |f|^{p_{1}}\Bigr)^{\theta\frac{p_{\theta}}{p_{1}}},
	\]
	hence
	$\|f\|_{p_{\theta}}\le \|f\|_{p_{0}}^{1-\theta}\|f\|_{p_{1}}^{\theta}$.
	If $p_{1}=\infty$, replace the second factor by $\|f\|_{\infty}^{\theta p_{\theta}}$.

	\medskip

	\emph{(c) Global non-inclusion and local inclusion.}
	If $p_{1}>p_{2}$, choose $\alpha$ with $\frac{n}{p_{1}}<\alpha\le \frac{n}{p_{2}}$ and set
	$f(x)=(1+|x|)^{-\alpha}$. Then $f\in L^{p_{1}}(\mathbb R^{n})$ but $f\notin L^{p_{2}}(\mathbb R^{n})$.
	If $p_{1}<p_{2}$, choose $\beta$ with $\frac{n}{p_{2}}<\beta\le \frac{n}{p_{1}}$ and let
	$g(x)=|x|^{-\beta}\mathbf 1_{\{|x|\le1\}}$; then $g\in L^{p_{2}}$ but $g\notin L^{p_{1}}$.
	Thus for $p_{1}\ne p_{2}$, neither $L^{p_{1}}(\mathbb R^{n})$ nor $L^{p_{2}}(\mathbb R^{n})$ contains the other.

	For local spaces: on every bounded $K$, the finite-measure embedding yields
	$\|h\|_{L^{p_{2}}(K)}\le |K|^{\frac1{p_{2}}-\frac1{p_{1}}}\|h\|_{L^{p_{1}}(K)}$ when $p_{1}\ge p_{2}$.
	Therefore
	\[
	L^{p_{1}}_{\mathrm{loc}}(\mathbb R^{n}) \subset L^{p_{2}}_{\mathrm{loc}}(\mathbb R^{n})
	\quad\Longleftrightarrow\quad p_{1}\ge p_{2}.
	\]
\end{spacy}

\tighthrule
\begin{spacy}
	\textbf{Monotone Convergence Theorem (Beppo--Levi).}
	Let $(f_n)_{n\ge1}$ be measurable with $0\le f_1\le f_2\le\cdots$ and $f_n\uparrow f$ a.e.
	Then
	\[
	\int_E f\,d\mu \;=\; \lim_{n\to\infty}\int_E f_n\,d\mu \;\in [0,\infty].
	\]
	(No integrability assumption beyond nonnegativity.)

	\medskip

	\textbf{Fatou's Lemma.}
	For nonnegative measurable $f_n$,
	\[
	\int_E \liminf_{n\to\infty} f_n \, d\mu
	\;\le\;
	\liminf_{n\to\infty} \int_E f_n \, d\mu .
	\]

	\medskip

	\textbf{Reverse Fatou (with domination).}
	If $f_n$ are measurable and there exists $g\in L^1(E)$ with $f_n\ge -g$ for all $n$, then
	\[
	\limsup_{n\to\infty} \int_E f_n \, d\mu
	\;\le\;
	\int_E \limsup_{n\to\infty} f_n \, d\mu .
	\]

	\medskip

	\textbf{Dominated Convergence Theorem (Lebesgue).}
	Suppose $f_n \to f$ a.e.\ on $E$ and there exists $g\in L^1(E)$ with $|f_n|\le g$ a.e.\ for all $n$.
	Then $f\in L^1(E)$ and
	\[
	\int_E f_n \, d\mu \;\to\; \int_E f \, d\mu,
	\qquad\text{equivalently}\qquad
	\|f_n-f\|_{L^1}\to 0.
	\]

	\medskip

	\textbf{Bounded Convergence (finite measure case).}
	If $\mu(E)<\infty$, $f_n\to f$ a.e., and $|f_n|\le M$ a.e.\ for some $M<\infty$, then
	\[
	\int_E f_n \, d\mu \;\to\; \int_E f \, d\mu .
	\]
	(Apply DCT with $g\equiv M\mathbf 1_E$.)

	\medskip

	\textbf{Useful corollary (convergence in $L^1$).}
	If $|f_n|\le g\in L^1$ and $f_n\to f$ in measure (or a.e.), then $f\in L^1$ and
	$\|f_n-f\|_{L^1}\to 0$ (by extracting a subsequence a.e.\ and applying DCT).
\end{spacy}

\tighthrule
\begin{spacy}
	\textbf{Markov's inequality (nonnegative case).}
	If $X\ge0$ is measurable and $a>0$, then
	\[
	\mu(\{X\ge a\}) \;\le\; \frac{1}{a}\int_E X\,d\mu.
	\]
	In particular, taking $X=|f|^{p}$ and $a=t^{p}$ gives
	\[
	\mu(\{|f|\ge t\}) \;\le\; \frac{\|f\|_{L^{p}}^{p}}{t^{p}}\qquad (p>0).
	\]

	\medskip

	\textbf{Chebyshev's inequality (general $p$).}
	For $f\in L^{p}(E)$ with $p>0$ and $t>0$,
	\[
	\mu(\{|f|\ge t\}) \;\le\; \frac{\|f\|_{L^{p}}^{p}}{t^{p}}.
	\]
	(Obtained from Markov with $X=|f|^{p}$.)

	\medskip

	\textbf{Egorov's theorem (a.e.\ $\Rightarrow$ almost uniform on finite measure).}
	If $\mu(E)<\infty$ and $f_n\to f$ almost everywhere on $E$, then for every $\varepsilon>0$ there exists
	a measurable $A\subset E$ with $\mu(E\setminus A)<\varepsilon$ such that $f_n\to f$ uniformly on $A$.

	\medskip

	\textbf{Uniform integrability (UI).}
	A family $\mathcal F\subset L^{1}(E)$ is \emph{uniformly integrable} if
	for every $\epsilon>0$ there exists $\delta>0$ such that
	$\mu(A)<\delta \Rightarrow \sup_{f\in\mathcal F}\int_{A}|f|\,d\mu<\epsilon$.
	A sufficient condition is domination: if there exists $g\in L^{1}(E)$ with $|f|\le g$ a.e.\ for all $f\in\mathcal F$,
	then $\mathcal F$ is uniformly integrable.

	\medskip

	\textbf{Vitali convergence theorem.}
	Let $(f_n)\subset L^{1}(E)$ be uniformly integrable and suppose $f_n\to f$ in measure.
	Then $f\in L^{1}(E)$ and
	\[
	\|f_n-f\|_{L^{1}} \;\longrightarrow\; 0 .
	\]
	(With domination $|f_n|\le g\in L^{1}$, Vitali follows from DCT combined with subsequence arguments.)

\end{spacy}

\tighthrule
\begin{spacy}
	\textbf{Setup.}
	Assume $\mu(E)<\infty$, $f_n\to f$ a.e., and $|f_n|\le g\in L^1(E)$.

	\textbf{Step 1 (Egorov).}
	For any $\varepsilon>0$ there is $A\subset E$ with $\mu(E\setminus A)<\varepsilon$ such that
	$f_n\to f$ uniformly on $A$.

	\textbf{Step 2 (convergence on $A$).}
	Uniform convergence and $|f_n|,|f|\le g$ imply
	\[
	\int_{A} |f_n-f|\,d\mu \;\longrightarrow\; 0.
	\]

	\textbf{Step 3 (control on the complement).}
	By domination,
	\[
	\int_{E\setminus A} |f_n-f|\,d\mu
	\;\le\; \int_{E\setminus A} (|f_n|+|f|)\,d\mu
	\;\le\; 2\int_{E\setminus A} g\,d\mu.
	\]
	Choosing $\varepsilon$ so that $\int_{E\setminus A} g<\delta$ gives the desired small tail.

	\textbf{Conclusion.}
	$\displaystyle \int_E |f_n-f|\,d\mu \to 0$; that is, DCT holds via Egorov + small tail.

	\medskip

	\textbf{Remark (infinite measure).}
	If $\mu(E)=\infty$ (e.g.\ $E=\mathbb R^n$), take an increasing sequence of bounded sets $K_R\uparrow E$ with
	$\int_{E\setminus K_R} g$ arbitrarily small. Apply the argument on $K_R$ and then let $R\to\infty$.
\end{spacy}

\tighthrule
\begin{spacy}
	\textbf{Convexity.}
	A function $\varphi:I\to\mathbb R$ is convex if
	\[
	\varphi(\lambda x+(1-\lambda)y)\le \lambda\varphi(x)+(1-\lambda)\varphi(y)
	\quad (x,y\in I,\ 0\le\lambda\le1).
	\]

	\textbf{Jensen's inequality.}
	Let $(E,\mathcal E,\nu)$ be a probability space, $\varphi$ convex on an interval containing the range of $X$.
	If $X$ is integrable, then
	\[
	\varphi\!\Big(\int_E X\,d\nu\Big) \;\le\; \int_E \varphi(X)\,d\nu.
	\]
	For concave $\varphi$ the inequality reverses.

	\textbf{Power means via Jensen.}
	For $p\ge 1$, $\varphi(t)=|t|^{p}$ is convex; hence
	\[
	\Big|\int_E f\,d\nu\Big|^{p}\le \int_E |f|^{p}\,d\nu.
	\]

	\textbf{Young's inequality (via convex duality).}
	For conjugate exponents $p,q>1$ and $a,b\ge0$,
	\[
	ab \;\le\; \frac{a^{p}}{p}+\frac{b^{q}}{q}.
	\]
	(Equivalently, the Legendre transform of $\phi(t)=t^{p}/p$ is $\phi^{\*}(s)=s^{q}/q$.)

	\textbf{Hölder from Young/Jensen.}
	Normalize $f,g$ by $\alpha=\|f\|_{p}$, $\beta=\|g\|_{q}$; write
	\[
	\frac{|fg|}{\alpha\beta}
	\le \frac{|f|^{p}}{p\,\alpha^{p}} + \frac{|g|^{q}}{q\,\beta^{q}}.
	\]
	Integrate to obtain
	$\int |fg|\le \|f\|_{p}\|g\|_{q}$.

	\textbf{AM--GM and log-sum.}
	Since $\log$ is concave,
	\[
	\log\!\Big(\sum_{i} \lambda_i x_i\Big) \;\ge\; \sum_i \lambda_i \log x_i
	\quad\Rightarrow\quad
	\sum_i \lambda_i x_i \;\ge\; \prod_i x_i^{\lambda_i},
	\]
	for $\lambda_i\ge0$, $\sum_i\lambda_i=1$, $x_i>0$.

	\textbf{KL-divergence nonnegativity.}
	For probability densities $p,q$ with $p\ll q$,
	\[
	D_{\mathrm{KL}}(p\|q)=\int p\log\frac{p}{q}\,d\mu \;\ge\; 0,
	\]
	by Jensen with convex $\varphi(t)=t\log t$ (or concavity of $\log$).

\end{spacy}
```

## CP-II-0485

- chapter line: 23737

```tex
\label{prob:cp-ii-0485}
\par\noindent\textbullet\quad \textbf{Closed-form analysis (geometric $\gamma$).}
	For $\gamma_j=r^j$, $0<r<1$,
	\[
	f(x)=\frac{rT_3(x)-r^2}{1-2rT_3(x)+r^2},\quad
	R_n(x)=\frac{r^{n+1}\big(T_{n+1}(T_3(x))-r\,T_n(T_3(x))\big)}{1-2rT_3(x)+r^2}.
	\]

	Given nonnegative coefficients $\gamma_j$, we approximate
	$f(x)=\sum_{j\ge1}\gamma_j T_{3j}(x)$ by the partial sum
	$P_n(x)=\sum_{j=1}^{n}\gamma_j T_{3j}(x)$.
	The points $x_k=\cos\!\big(\frac{k\pi}{3^{n+1}}\big)$ are used to
	\emph{certify the error}:
	\[
	f(x_k)-P_n(x_k)=(-1)^k S_n,\qquad S_n=\sum_{j>n}\gamma_j=\|f-P_n\|_\infty.
	\]
	They are \emph{not} interpolation nodes. Interpolation would require constructing
	a polynomial $Q$ such that $Q(y_i)=f(y_i)$ at prescribed nodes $y_i$.

Write $x=\cos\theta$ and expand
\[
f(x)=\sum_{m=0}^\infty a_m T_m(x),
\quad
a_m=\frac{2}{\pi}\int_{0}^{\pi} f(\cos\theta)\cos(m\theta)\,d\theta\ (m\ge1),\quad
a_0=\frac{1}{\pi}\int_{0}^{\pi} f(\cos\theta)\,d\theta.
\]
Set $\gamma_j:=a_{3j}$ so that
\[
f(x)=\sum_{j\ge1}\gamma_j T_{3j}(x)+a_0 T_0(x)
\quad\text{(with $a_m=0$ for $m\not\equiv 0\!\!\!\pmod 3$ if the expansion is exact).}
\]
Given nonnegative $\gamma_j$, the $n$-term truncation $P_n(x)=\sum_{j=1}^n\gamma_j T_{3j}(x)$
has uniform error
\[
\|f-P_n\|_\infty = S_n:=\sum_{j>n}\gamma_j,
\]
attained at $x_k=\cos\!\big(\frac{k\pi}{3^{n+1}}\big)$, where
$f(x_k)-P_n(x_k)=(-1)^k S_n$.

For example,
\[
f(x)=e^x,\quad f(x)=\sinh x,\quad\text{or any continuous function you can evaluate.}
\]

Use the cosine change of variable $x=\cos\theta$.
The Chebyshev expansion is
\[
f(x)=\sum_{m=0}^{\infty} a_m T_m(x),
\]
where the coefficients are given by
\[
a_0=\frac{1}{\pi}\int_0^{\pi} f(\cos\theta)\,d\theta,
\qquad
a_m=\frac{2}{\pi}\int_0^{\pi} f(\cos\theta)\cos(m\theta)\,d\theta,
\quad (m\ge1).
\]
In practice, these integrals are evaluated efficiently using a
\emph{Discrete Cosine Transform (DCT)}.

\[
\gamma_j := a_{3j}, \qquad j=1,2,\dots
\]
Now you have the nonnegative (if $f$ satisfies the theoremĂ˘â‚¬â„˘s assumption) sequence $\gamma_j$.

\[
P_n(x)=\sum_{j=1}^{n}\gamma_j\,T_{3j}(x).
\]
This $P_n$ is your $n$-term Chebyshev approximation to $f$.

\[
S_n=\sum_{j=n+1}^{\infty}\gamma_j.
\]
In practice, $S_n$ is approximated by summing until $\gamma_j$ become negligible.

\[
x_k=\cos\!\Big(\frac{k\pi}{3^{n+1}}\Big),
\qquad k=0,1,\dots,3^{n+1}.
\]
At these points, the error has the explicit alternating form
\[
f(x_k)-P_n(x_k)=(-1)^k\,S_n,
\]
so that $\|f-P_n\|_\infty=S_n$.

\bigskip

\begin{center}
	\renewcommand{\arraystretch}{1.3}
	\begin{tabular}{>{$}l<{$} | l}
		\hline
		\textbf{Symbol} & \textbf{Meaning} \\ \hline
		f(x) & Given continuous function on $[-1,1]$ \\
		T_m(x) & Chebyshev polynomial of degree $m$ \\
		a_m & Chebyshev coefficients of $f$ \\
		\gamma_j = a_{3j} & Extracted subsequence (used in this theorem) \\
		P_n(x)=\sum_{j=1}^{n}\gamma_j T_{3j}(x) & $n$-term approximation \\
		R_n(x)=f(x)-P_n(x) & Remainder (error) \\
		S_n=\sum_{j>n}\gamma_j & Uniform error magnitude \\
		x_k=\cos\frac{k\pi}{3^{n+1}} & Alternation points of $R_n$ \\
		f(x_k)-P_n(x_k)=(-1)^k S_n & Alternating error pattern \\ \hline
	\end{tabular}
\end{center}
```

## CP-II-0496

- chapter line: 23842

```tex
\label{prob:cp-ii-0496}
{Polynomial approximation of $1/z$ on a semicircle}{poly-1-over-z-semi}
	Construct a sequence of polynomials that converges uniformly to $1/z$ on
	\[
	K=\{\,z\in\mathbb C:\ |z|=1,\ \Re z\ge 0\,\}.
	\]
```

## CP-II-0510

- chapter line: 23851

```tex
\label{prob:cp-ii-0510}
ChebyshevĂ˘â‚¬â„˘s inequality and weak-$L^p$

\textbf{(a)} Prove that for $f\in L^p(\mathbb{R}^n)$ and $\lambda>0$,
\[
\big|\{x\in\mathbb{R}^n:\ |f(x)|>\lambda\}\big|
\;\le\; \frac{\|f\|_{L^p}^p}{\lambda^p}.
\]

\medskip
\textbf{(b)} Define the weak-$L^p$ space $L^{p,\mathrm{w}}(\mathbb{R}^n)$ to be the set of measurable
$f$ for which there exists $C>0$ such that
\[
\big|\{x\in\mathbb{R}^n:\ |f(x)|>\lambda\}\big|
\;\le\; \frac{C}{\lambda^p}\qquad\text{for all }\lambda>0.
\]
Show that $L^p(\mathbb{R}^n)\subset L^{p,\mathrm{w}}(\mathbb{R}^n)$ and that this inclusion is proper by
exhibiting an explicit function in $L^{p,\mathrm{w}}(\mathbb{R}^n)\setminus L^p(\mathbb{R}^n)$.

For $f\in L^p(\mathbb{R}^n)$ and $\lambda>0$,
\[
\big|\{x:\,|f(x)|>\lambda\}\big|
\;\le\; \frac{\|f\|_{L^p}^p}{\lambda^p}.
\]
\emph{Proof.} On $\{|f|>\lambda\}$, $|f|^p\ge \lambda^p$, hence
$\|f\|_p^p \ge \int_{\{|f|>\lambda\}} |f|^p \ge \lambda^p\,|\{|f|>\lambda\}|$.

We say $f\in L^{p,\mathrm{w}}(\mathbb{R}^n)$ if there exists $C$ such that
\[
\big|\{x:\,|f(x)|>\lambda\}\big| \;\le\; \frac{C}{\lambda^p}
\qquad\forall\,\lambda>0.
\]
By Chebyshev, $L^p(\mathbb{R}^n)\subset L^{p,\mathrm{w}}(\mathbb{R}^n)$ with $C=\|f\|_p^p$.

\emph{Properness.} Let $f(x)=|x|^{-n/p}\mathbf 1_{\{|x|\le 1\}}(x)$. Then, for $\lambda>1$,
\[
\{ |f|>\lambda \}=\{ |x|<\lambda^{-p/n}\}, \qquad
\big|\{|f|>\lambda\}\big| = c_n\,\lambda^{-p},
\]
so $f\in L^{p,\mathrm{w}}$. However
$\displaystyle \int_{|x|\le1}|f|^p=\int_{|x|\le1} |x|^{-n}\,dx=\infty$,
hence $f\notin L^p$. Therefore $L^p(\mathbb{R}^n)\subsetneq L^{p,\mathrm{w}}(\mathbb{R}^n)$.

\clearpage

\clearpage
```

## CP-II-0550

- chapter line: 23900

```tex
\label{prob:cp-ii-0550}
(for part (b) \& Minkowski): \boldmath $F(x,y)=f(x)\,h(y)$

Take
\[
f(x)=(1+|x|)^{-\alpha}\quad (\alpha>1,\ \text{so } f\in L^1(\mathbb{R})),
\qquad
h(y)=e^{-|y|}\in L^p(\mathbb{R})\ (1\le p<\infty),
\]
and define $F(x,y)=f(x)\,h(y)$. Then
\[
G(y) \;=\; \int_{\mathbb{R}} F(x,y)\,dx \;=\; \Bigl(\int_{\mathbb{R}} f(x)\,dx\Bigr) h(y) \;=\; \|f\|_{L^1}\,h(y).
\]

\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
\|f\|_{L^1}
\;=\; \int_{\mathbb{R}}(1+|x|)^{-\alpha}\,dx
\;=\; 2\!\int_{0}^{\infty} (1+x)^{-\alpha}\,dx
\;=\; \boxed{\ \tfrac{2}{\alpha-1}\ },
\qquad
\|h\|_{L^p}
\;=\; \Bigl(\int_{\mathbb{R}} e^{-p|y|}\,dy\Bigr)^{\!1/p}
\;=\; \boxed{\ \bigl(\tfrac{2}{p}\bigr)^{1/p}\ }.
$}
\end{center}

\par\medskip\noindent\textbf{Inequality with a given $g\in L^q$, $\|g\|_{L^q}\le1$.}\quad
\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
\int_{\mathbb{R}} |G(y)|\,|g(y)|\,dy
\;=\; \|f\|_{L^1} \int_{\mathbb{R}} |h(y)|\,|g(y)|\,dy
\;\le\; \|f\|_{L^1}\,\|h\|_{L^p}\,\|g\|_{L^q}
\;\le\; \|f\|_{L^1}\,\|h\|_{L^p}.
$}
\end{center}

\[
\int_{\mathbb{R}} \Bigl(\int_{\mathbb{R}} |F(x,y)|^p\,dy\Bigr)^{\!1/p} dx
\;=\; \int_{\mathbb{R}} |f(x)|\,\|h\|_{L^p}\,dx
\;=\; \|f\|_{L^1}\,\|h\|_{L^p}.
\]
Hence we obtain equality and MinkowskiĂ˘â‚¬â„˘s integral inequality:
\[
\|G\|_{L_y^p}
\;=\; \|\|f\|_{L^1}\,h\|_{L_y^p}
\;=\; \|f\|_{L^1}\,\|h\|_{L^p}
\;\le\; \int_{\mathbb{R}} \Bigl(\int_{\mathbb{R}} |F(x,y)|^p\,dy\Bigr)^{\!1/p} dx.
\]
Equality occurs for the Hölder extremizer $g(y)=h(y)^{p-1}/\|h\|_{L^p}^{\,p-1}$ (since $h\ge 0$).

\clearpage
```
