# P2/P3 source-grounded orphan review

## P2 — SOLSEM-7723F82AC385
- Review proposal: **EDITORIAL_REVIEW_POST_STRUCTURAL_FREEZE**
- Prior decision: `PRIOR_STRUCTURAL_RESCAN`
- Solution source: `Downloads/theory-of-complex-analysis-gamma.tex` `L1216-L1239`
- Source problem number: ``
- Refresh top1=0.4900 margin=0.0987

### Solution block
```text
\section*{Solution}
Split the integrand:
\[
\frac{(x+1)\cos x}{x^{2}+1}
=\frac{x\cos x}{x^{2}+1}+\frac{\cos x}{x^{2}+1}.
\]
The first term is odd, so its principal value integral over $\mathbb R$ is $0$.
Therefore
\[
\operatorname{PV}\!\int_{-\infty}^{\infty}\frac{(x+1)\cos x}{x^{2}+1}\,dx
=\int_{-\infty}^{\infty}\frac{\cos x}{x^{2}+1}\,dx
=\pi e^{-1}
=\frac{\pi}{e}.
\]

\paragraph{(Residue check, optional).}
Consider $f(z)=\dfrac{e^{iz}}{z^{2}+1}$ and integrate over the upper semicircle.
The only enclosed pole is at $z=i$, with residue $\mathrm{Res}(f;i)=\dfrac{e^{i\cdot i}}{2i}
=\dfrac{e^{-1}}{2i}$. Jordan’s lemma gives
\[
\int_{-\infty}^{\infty}\frac{e^{ix}}{x^{2}+1}\,dx=2\pi i\cdot\frac{e^{-1}}{2i}=\pi e^{-1}.
\]
Taking real parts yields $\displaystyle \int_{-\infty}^{\infty}\frac{\cos x}{x^{2}+1}\,dx=\pi e^{-1}$.

```

### Candidate #1 — IMP-DL-AD9EFCAF62-P020 — score 0.4900
- Source: `Downloads/theory-of-complex-analysis-2.tex` `L955-L1010`
- Problem number: `3.`
- lexical=0.7547 math=0.2177 number=0.0000 family=0.0000
```text
\paragraph{Problem 3. Evaluate the following integrals.}

\medskip
\emph{(a)} $\displaystyle \int_{0}^{\pi}\frac{d\theta}{4+\sin^{2}\theta}$.

Using $\displaystyle \int_{0}^{\pi}\frac{d\theta}{a+b\sin^{2}\theta}
=\frac{\pi}{\sqrt{a(a+b)}}$ for $a>0$, with $a=4$, $b=1$,
\[
\int_{0}^{\pi}\frac{d\theta}{4+\sin^{2}\theta}
=\frac{\pi}{\sqrt{4\cdot 5}}=\boxed{\frac{\pi}{2\sqrt5}}.
\]

\medskip
\emph{(b)} $\displaystyle \int_{0}^{\infty}\sin(x^{2})\,dx$.

By the Fresnel/Gaussian argument,
\[
\int_{0}^{\infty}\sin(x^{2})\,dx
=\int_{0}^{\infty}\cos(x^{2})\,dx
=\boxed{\frac{\sqrt{2\pi}}{4}=\frac{\sqrt{\pi}}{2\sqrt2}}.
\]

\medskip
\emph{(c)} $\displaystyle \int_{0}^{\infty}\frac{x^{2}}{(x^{2}+4)^{2}(x^{2}+9)}\,dx$.

Let $f(z)=\dfrac{z^{2}}{(z^{2}+4)^{2}(z^{2}+9)}$. The integrand is even; hence
\[
\int_{0}^{\infty}f(x)\,dx=\frac12\int_{-\infty}^{\infty}f(x)\,dx.
\]
Poles in the upper half-plane: $2i$ (double), $3i$ (simple).
\[
\Res(f;2i)=-\frac{13i}{200},\qquad \Res(f;3i)=\frac{3i}{50},\qquad
\Res(f;2i)+\Res(f;3i)=-\frac{i}{200}.
\]
Thus
\[
\int_{-\infty}^{\infty} f(x)\,dx
=2\pi i\!\left(-\frac{i}{200}\right)=\frac{\pi}{100},
\qquad
\int_{0}^{\infty} f(x)\,dx=\boxed{\frac{\pi}{200}}.
\]

\medskip
\emph{(d)} $\displaystyle \int_{0}^{\infty}\frac{\ln(x^{2}+1)}{x^{2}+1}\,dx$.

With $x=\tan t$ ($t\in[0,\pi/2)$), $x^{2}+1=\sec^{2}t$, $dx=\sec^{2}t\,dt$,
\[
\int_{0}^{\infty}\frac{\ln(x^{2}+1)}{x^{2}+1}\,dx
=\int_{0}^{\pi/2}\ln(\sec^{2}t)\,dt
=2\int_{0}^{\pi/2}\ln(\sec t)\,dt
=-2\int_{0}^{\pi/2}\ln(\cos t)\,dt
=\boxed{\pi\ln 2}.
\]
\qed

% ---------- Problem 4 (restated) ----------
```

### Candidate #2 — IMP-DL-336732908A-P010 — score 0.3913
- Source: `Downloads/theory-of-complex-analysis-next.tex` `L2327-L2333`
- Problem number: ``
- lexical=0.5938 math=0.1957 number=0.0000 family=0.0000
```text
\begin{problem}
	Let $f(z)=e^{-z^{2}}$. Using an appropriate contour and the Cauchy--Goursat theorem, show that for $b>0$,
	\[
	\int_{0}^{\infty} e^{-x^{2}}\cos(2bx)\,dx=\frac{\sqrt{\pi}}{2}\,e^{-b^{2}}.
	\]
	You may use $\int_{0}^{\infty} e^{-x^{2}}\,dx=\sqrt{\pi}/2$.
\end{problem}
```

### Candidate #3 — IMP-DL-AD9EFCAF62-P002 — score 0.3861
- Source: `Downloads/theory-of-complex-analysis-2.tex` `L297-L356`
- Problem number: `2.`
- lexical=0.5955 math=0.1698 number=0.0000 family=0.0000
```text
\paragraph{Problem 2.}
Find the Laurent expansion (in powers of $z$, i.e.\ about $0$) of
\[
\frac{1}{z^{2}-3z+2}=\frac{1}{(z-1)(z-2)}
\]
in the regions $\{|z|<1\}$, $\{1<|z|<2\}$, and $\{|z|\ge 2\}$.

\paragraph{Background.}
Partial fractions:
\[
\frac{1}{(z-1)(z-2)}=-\frac{1}{z-1}+\frac{1}{z-2}.
\]
Geometric expansions:
\[
\frac{1}{1-w}=\sum_{n=0}^{\infty}w^{n}\quad(|w|<1),\qquad
\frac{1}{z-a}=\frac{1}{z}\cdot\frac{1}{1-\frac{a}{z}}
=\sum_{n=0}^{\infty}\frac{a^{n}}{z^{n+1}}\quad(|z|>|a|).
\]

\paragraph{Solutions.}

\emph{(A) For $|z|<1$.}
\[
-\frac{1}{z-1}=\frac{1}{1-z}=\sum_{n=0}^{\infty}z^{n},\qquad
\frac{1}{z-2}=-\frac{1}{2}\frac{1}{1-\frac{z}{2}}
=-\sum_{n=0}^{\infty}\frac{z^{n}}{2^{\,n+1}}.
\]
Hence
\[
\boxed{\ \frac{1}{z^{2}-3z+2}=\sum_{n=0}^{\infty}\Big(1-2^{-(n+1)}\Big)z^{n},\quad |z|<1.\ }
\]

\medskip
\emph{(B) For $1<|z|<2$.}
\[
-\frac{1}{z-1}=-\frac{1}{z}\frac{1}{1-\frac{1}{z}}
=-\sum_{n=1}^{\infty} z^{-n},\qquad
\frac{1}{z-2}=-\sum_{n=0}^{\infty}\frac{z^{n}}{2^{\,n+1}}.
\]
Thus
\[
\boxed{\ \frac{1}{z^{2}-3z+2}
	=-\sum_{n=1}^{\infty} z^{-n}-\sum_{n=0}^{\infty}\frac{z^{n}}{2^{\,n+1}},
	\quad 1<|z|<2.\ }
\]

\medskip
\emph{(C) For $|z|>2$.}
\[
-\frac{1}{z-1}=-\sum_{m=1}^{\infty} z^{-m},\qquad
\frac{1}{z-2}=\frac{1}{z}\frac{1}{1-\frac{2}{z}}
=\sum_{m=1}^{\infty}\frac{2^{\,m-1}}{z^{m}}.
\]
Therefore
\[
\boxed{\ \frac{1}{z^{2}-3z+2}
	=\sum_{m=1}^{\infty}\big(2^{\,m-1}-1\big)z^{-m},\quad |z|>2.\ }
\]
\qed

```

### Candidate #4 — IMP-DL-20E278E436-R000804-D56B67A7 — score 0.3668
- Source: `Downloads/merged_exercises_FULL_v2 (1).tex` `L804-L809`
- Problem number: `5.3`
- lexical=0.5590 math=0.1772 number=0.0000 family=0.0000
```text
\subsection*{Exercise 5.3}
Show
\[
\lim_{k\to\infty}\sum_{j=0}^{k-1}\frac{k}{j^2+k^2}=\int_0^1\frac{1}{1+x^2}dx.
\]

```

### Candidate #5 — IMP-DL-336732908A-P002 — score 0.3601
- Source: `Downloads/theory-of-complex-analysis-next.tex` `L113-L135`
- Problem number: ``
- lexical=0.5143 math=0.2577 number=0.0000 family=0.0000
```text
\paragraph{Problem.}
Compute $\displaystyle \int_{0}^{2\pi} e^{\,e^{it}}\,dt$.

\paragraph{Path method.}
Let $z=e^{it}$ so that $|z|=1$ and $dt=\frac{dz}{iz}$. Then
\[
\int_{0}^{2\pi} e^{e^{it}}\,dt
=\frac1i\oint_{|z|=1}\frac{e^{z}}{z}\,dz.
\]
By Cauchy’s integral formula for $f(z)=e^{z}$,
\[
\oint_{|z|=1}\frac{e^{z}}{z}\,dz=2\pi i\,f(0)=2\pi i.
\]
Hence
\[
\boxed{\displaystyle \int_{0}^{2\pi} e^{\,e^{it}}\,dt=2\pi }.
\]

\paragraph{Remark (series check).}
Since $e^{e^{it}}=\sum_{n=0}^\infty \frac{e^{int}}{n!}$, the integral over $[0,2\pi]$
kills all terms with $n\neq0$ and equals $2\pi$.


```

### Editorial decision
- `ACCEPT <problem_id>`
- `NOT_A_PROBLEM`
- `MISSING_COMPANION_STATEMENT`
- `NO_GOOD_MATCH`
- `NEEDS_MANUAL_REVIEW`

---

## P2 — SOLSEM-94664AFC5677
- Review proposal: **EDITORIAL_REVIEW_POST_STRUCTURAL_FREEZE**
- Prior decision: `PRIOR_STRUCTURAL_RESCAN`
- Solution source: `Downloads/theory-of-commutative-algebra-12.tex` `L1185-L1213`
- Source problem number: ``
- Refresh top1=0.4720 margin=0.0289

### Solution block
```text
\textbf{Solution.}
The quotient
\[
k[s,t]/(s-a,t-b)
\]
is obtained by imposing the relations
\[
s=a,\qquad t=b.
\]
Hence every polynomial \(f(s,t)\) becomes the scalar \(f(a,b)\in k\). Equivalently, the evaluation homomorphism
\[
\varphi:k[s,t]\to k,\qquad f(s,t)\mapsto f(a,b)
\]
is surjective and has kernel
\[
\ker(\varphi)=(s-a,t-b).
\]
Therefore, by the First Isomorphism Theorem,
\[
k[s,t]/(s-a,t-b)\cong k.
\]

By contrast, a product ring such as \(k\times k\) appears when one quotients by an ideal corresponding to two separate points, for example
\[
k[t]/((t-a)(t-b))\cong k\times k
\qquad (a\neq b),
\]
via the Chinese Remainder Theorem. Thus \(k[s,t]/(s-a,t-b)\) is \(k\), not \(k\times k\).

```

### Candidate #1 — IMP-DL-B7B63B4C41-P011 — score 0.4720
- Source: `Downloads/theory-of-commutative-algebra-12.tex` `L3796-L3826`
- Problem number: ``
- lexical=0.5858 math=0.2174 number=0.0000 family=1.0000
```text
	\begin{example}[A union of two lines]
		In \(k[s,t]\), the principal ideal
		\[
		\bigl((s-a)(t-b)\bigr)
		\]
		forces only
		\[
		(s-a)(t-b)=0.
		\]
		This means
		\[
		s=a
		\qquad\text{or}\qquad
		t=b,
		\]
		so the zero set is the union of the two lines
		\[
		s=a
		\qquad\text{and}\qquad
		t=b.
		\]
		The quotient ring is
		\[
		k[s,t]/\bigl((s-a)(t-b)\bigr).
		\]
		This is \emph{not} a field, because in the quotient we have
		\[
		[s-a]\neq 0,\qquad [t-b]\neq 0,\qquad [s-a][t-b]=0.
		\]
		So the quotient has nonzero zero divisors.
	\end{example}
```

### Candidate #2 — IMP-DL-B7B63B4C41-P010 — score 0.4430
- Source: `Downloads/theory-of-commutative-algebra-12.tex` `L3780-L3794`
- Problem number: ``
- lexical=0.5321 math=0.2267 number=0.0000 family=1.0000
```text
	\begin{example}[A single point]
		In \(k[s,t]\), the ideal
		\[
		(s-a,t-b)
		\]
		forces
		\[
		s=a,\qquad t=b.
		\]
		Hence
		\[
		k[s,t]/(s-a,t-b)\cong k.
		\]
		This is the coordinate ring of one point.
	\end{example}
```

### Candidate #3 — IMP-DL-4DEBE28720-P033 — score 0.3917
- Source: `Downloads/theory-of-commutative-algebra-13.tex` `L902-L945`
- Problem number: `in`
- lexical=0.6084 math=0.1619 number=0.0000 family=0.0000
```text
\subsubsection{Example in \(k[s,t]\)}

Let
\[
A=k[s,t].
\]
Take the ideal
\[
I=((s-a)(t-b))
\]
and the prime ideal
\[
\mf p=(s-a,t-b).
\]

Then
\[
((s-a)(t-b))\subseteq (s-a,t-b).
\]

This is because the generator
\[
(s-a)(t-b)
\]
belongs to the ideal \((s-a,t-b)\): it is a multiple of \(s-a\), and any multiple of \(s-a\) lies in \((s-a,t-b)\).

Since the ideal \(((s-a)(t-b))\) consists of all multiples of \((s-a)(t-b)\), every element of it also lies in \((s-a,t-b)\).

So the point \((s-a,t-b)\) lies in
\[
V((s-a)(t-b)).
\]

Geometrically, this means that the point \((a,b)\) lies on the closed set defined by
\[
(s-a)(t-b)=0,
\]
that is, on the union of the two lines
\[
s=a
\qquad\text{and}\qquad
t=b.
\]

```

### Candidate #4 — IMP-DL-B7B63B4C41-P008 — score 0.3300
- Source: `Downloads/theory-of-commutative-algebra-12.tex` `L1584-L1616`
- Problem number: ``
- lexical=0.3286 math=0.2475 number=0.0000 family=1.0000
```text
\subsubsection{Example}

Take \(k=\mathbb{R}\), \(a=1\), \(b=2\). Then
\[
\mathbb{R}[s,t]/(s-1,t-2)\cong \mathbb{R},
\]
and the class of a polynomial is determined by its value at \((1,2)\).

For example:
\[
[s^2+t]\mapsto 1^2+2=3,
\]
\[
[s+t]\mapsto 1+2=3,
\]
so
\[
[s^2+t]=[s+t]
\]
in the quotient, because both polynomials have the same value at \((1,2)\).

\subsubsection{Final summary}

Therefore, saying that
\[
k[s,t]/(s-a,t-b)\cong k
\]
means that after imposing
\[
s=a,\qquad t=b,
\]
every polynomial reduces to its scalar value at that point, and the quotient ring is exactly the field \(k\) of those values.

```

### Candidate #5 — IMP-DL-4DEBE28720-P051 — score 0.3119
- Source: `Downloads/theory-of-commutative-algebra-13.tex` `L1872-L1891`
- Problem number: ``
- lexical=0.4719 math=0.1591 number=0.0000 family=0.0000
```text
\subsubsection{Example: \(k[s,t]\) at \((s-a,t-b)\)}

In
\[
k[s,t]_{(s-a,t-b)},
\]
one may divide by any polynomial \(g(s,t)\) with
\[
g(a,b)\neq 0.
\]

But one cannot divide by
\[
s-a
\qquad\text{or}\qquad
t-b.
\]

This is exactly the local picture of regularity near a point.

```

### Editorial decision
- `ACCEPT <problem_id>`
- `NOT_A_PROBLEM`
- `MISSING_COMPANION_STATEMENT`
- `NO_GOOD_MATCH`
- `NEEDS_MANUAL_REVIEW`

---

## P2 — SOLSEM-DE60695D66E5
- Review proposal: **EDITORIAL_REVIEW_POST_STRUCTURAL_FREEZE**
- Prior decision: `PRIOR_STRUCTURAL_RESCAN`
- Solution source: `Downloads/theory-of-commutative-algebra-9.tex` `L2603-L2652`
- Source problem number: ``
- Refresh top1=0.4018 margin=0.0283

### Solution block
```text
\textbf{Solution.}

Since \(g\) is minimal and surjective, part (a) gives
\[
\Ker(g)\subseteq \m F.
\]
But the sequence is exact, so
\[
\im(f)=\Ker(g).
\]
Hence
\[
f(K)\subseteq \m F.
\]

Now choose bases
\[
K\cong A^r,\qquad F\cong A^m.
\]
With respect to these bases, the map \(f\) is given by a matrix
\[
(c_{ij})
\]
with entries in \(A\).

Because \(f(K)\subseteq \m F\), each column of the matrix has all entries in \(\m\). Thus
\[
c_{ij}\in \m
\qquad\text{for all }i,j.
\]

By the note in the problem, the induced map
\[
f_*:\Ext_A^i(k,A^r)\to \Ext_A^i(k,A^m)
\]
is given by the same matrix \((c_{ij})\), now acting on
\[
\Ext_A^i(k,A^r)\cong \bigl(\Ext_A^i(k,A)\bigr)^r,
\qquad
\Ext_A^i(k,A^m)\cong \bigl(\Ext_A^i(k,A)\bigr)^m.
\]

But \(\Ext_A^i(k,A)\) is naturally a \(k=A/\m\)-vector space, so \(\m\) acts trivially on it. Therefore multiplication by each \(c_{ij}\in \m\) is zero on \(\Ext_A^i(k,A)\).

Hence every entry of the matrix acts by zero, so the whole matrix acts by zero. Therefore
\[
f_*=0.
\]
This proves the claim. \qed

```

### Candidate #1 — IMP-DL-3C59D9EE8B-P091 — score 0.4018
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex` `L2798-L2986`
- Problem number: `14(b)`
- lexical=0.5355 math=0.3802 number=0.0000 family=0.0000
```text
\section{Problem 14(b) --- Existence of a minimal map from a free module}

\textbf{Exact statement.}
Let \((A,\mathfrak m)\) be a local ring, let \(k=A/\mathfrak m\), and let \(M\) be a finitely generated \(A\)-module. Show that there exists a minimal homomorphism
\[
f:F\to M
\]
with \(F\) free.

\textbf{Solution.}
We want to construct a free \(A\)-module \(F\) and an \(A\)-linear map
\[
f:F\to M
\]
such that
\[
f\otimes_A k:\ F\otimes_A k \to M\otimes_A k
\]
is an isomorphism.

Since
\[
M\otimes_A k \cong M/\mathfrak m M,
\qquad
F\otimes_A k \cong F/\mathfrak m F,
\]
it is enough to construct \(f\) so that the induced map
\[
\bar f:\ F/\mathfrak m F \to M/\mathfrak m M
\]
is an isomorphism.

Because \(M\) is finitely generated over \(A\), the quotient
\[
M/\mathfrak m M
\]
is a finite-dimensional vector space over
\[
k=A/\mathfrak m.
\]
Choose a \(k\)-basis
\[
\overline{m}_1,\dots,\overline{m}_r
\]
of \(M/\mathfrak m M\), and choose lifts
\[
m_1,\dots,m_r\in M.
\]

Now let
\[
F=A^r
\]
with basis \(e_1,\dots,e_r\), and define an \(A\)-linear map
\[
f:F\to M
\]
by
\[
f(e_i)=m_i
\qquad (1\le i\le r).
\]

Reducing modulo \(\mathfrak m\), we obtain a \(k\)-linear map
\[
\bar f:\ F/\mathfrak m F \to M/\mathfrak m M.
\]
Since
\[
F/\mathfrak m F \cong k^r
\]
with basis \(\bar e_1,\dots,\bar e_r\), the map \(\bar f\) sends \(\bar e_i\) to \(\overline{m}_i\). By construction, \(\overline{m}_1,\dots,\overline{m}_r\) form a basis of \(M/\mathfrak m M\). Therefore \(\bar f\) is an isomorphism.

Hence
\[
f\otimes_A k
\]
is an isomorphism, so \(f\) is minimal by definition.

\medskip

If one wishes, one can also reformulate this using part (a). Since \(\bar f\) is surjective,
\[
M=f(F)+\mathfrak m M.
\]
By Nakayama's lemma,
\[
M=f(F),
\]
so \(f\) is surjective. Then part (a) implies
\[
\ker f\subseteq \mathfrak m F.
\]
Thus \(f\) is minimal in the equivalent sense of part (a) as well.

\medskip

Therefore for every finitely generated \(A\)-module \(M\), there exists a minimal homomorphism
\[
f:F\to M
\]
with \(F\) free.

\section{Problem 14(c) --- Vanishing of the induced maps on \texorpdfstring{$\operatorname{Ext}$}{Ext} for a minimal presentation}

\textbf{Exact statement.}
Let \((A,\mathfrak m)\) be a local ring, \(k=A/\mathfrak m\), and suppose
\[
0\longrightarrow K \xrightarrow{\,f\,} F \xrightarrow{\,g\,} M \longrightarrow 0
\]
is exact, with \(g\) minimal and \(K,F\) free. Show that the homomorphisms
\[
f_*:\operatorname{Ext}_A^i(k,K)\longrightarrow \operatorname{Ext}_A^i(k,F)
\]
induced by \(f\) vanish for all \(i\).

\medskip

\textit{Note.} If \(K=A^n\), \(F=A^m\), and \(f\) is represented by a matrix \((c_{ij})\), then \(f_*\) is represented by the same matrix, now viewed as a map
\[
(\operatorname{Ext}_A^i(k,A))^n\to (\operatorname{Ext}_A^i(k,A))^m.
\]

\textbf{Solution.}
Since the sequence
\[
0\to K \xrightarrow{f} F \xrightarrow{g} M \to 0
\]
is exact and \(g\) is minimal, part (a) implies that \(g\) is surjective and
\[
\ker g\subseteq \mathfrak m F.
\]
But \(\operatorname{im}(f)=\ker g\), so
\[
\operatorname{im}(f)\subseteq \mathfrak m F.
\]

Choose bases so that
\[
K\cong A^n,\qquad F\cong A^m.
\]
Then \(f\) is represented by an \(m\times n\) matrix
\[
(c_{ij}).
\]
Since \(\operatorname{im}(f)\subseteq \mathfrak m F\), each column of this matrix lies in \(\mathfrak m A^m\), hence every entry satisfies
\[
c_{ij}\in \mathfrak m.
\]

We now claim that for every \(i\ge 0\),
\[
\mathfrak m\cdot \operatorname{Ext}_A^i(k,A)=0.
\]
Indeed, because \(A\) is commutative, the \(A\)-module structure on \(\operatorname{Ext}_A^i(k,A)\) may be viewed either from the second argument \(A\) or from the first argument \(k\), and these two actions agree. But if \(a\in \mathfrak m\), then multiplication by \(a\) on
\[
k=A/\mathfrak m
\]
is the zero map. Hence multiplication by \(a\) on \(\operatorname{Ext}_A^i(k,A)\) is also zero. Therefore
\[
\mathfrak m\cdot \operatorname{Ext}_A^i(k,A)=0.
\]

Now by the note, the induced homomorphism
\[
f_*:\operatorname{Ext}_A^i(k,K)\to \operatorname{Ext}_A^i(k,F)
\]
is represented by the same matrix \((c_{ij})\), now acting as
\[
(\operatorname{Ext}_A^i(k,A))^n\to (\operatorname{Ext}_A^i(k,A))^m.
\]
Since every \(c_{ij}\in \mathfrak m\), and \(\mathfrak m\) annihilates \(\operatorname{Ext}_A^i(k,A)\), each entry acts as zero. Thus the whole matrix defines the zero map.

Therefore
\[
f_*=0
\]
for every \(i\ge 0\).

\medskip

Hence
\[
\boxed{
	f_*:\operatorname{Ext}_A^i(k,K)\longrightarrow \operatorname{Ext}_A^i(k,F)
	\text{ is the zero map for all }i.
}
\]	

```

### Candidate #2 — IMP-DL-CAA415139D-P053 — score 0.3736
- Source: `Downloads/theory-of-commutative-algebra-10.tex` `L2876-L2898`
- Problem number: `5`
- lexical=0.3868 math=0.2885 number=0.0000 family=1.0000
```text
\subsubsection{Example 5: part (c) in the \(k[[x,y]]\) example}

Consider
\[
0\to A \xrightarrow{f} A^2 \xrightarrow{g} A \to k \to 0
\]
with
\[
f=\begin{pmatrix}-y\\x\end{pmatrix},\qquad g=(x\ \ y).
\]

Since
\[
f(A)\subseteq \m A^2,
\]
the induced map
\[
f_*:\Ext_A^i(k,A)\to \Ext_A^i(k,A^2)
\]
is zero for every \(i\).

This is exactly the statement of part (c) in a concrete case.

```

### Candidate #3 — IMP-DL-CAA415139D-P069 — score 0.3336
- Source: `Downloads/theory-of-commutative-algebra-10.tex` `L4120-L4171`
- Problem number: `2`
- lexical=0.3168 math=0.2910 number=0.0000 family=1.0000
```text
\subsection{Example 2: the residue field over a discrete valuation ring}

Let
\[
A=k[[t]],
\qquad
\mathfrak m=(t),
\qquad
M=A/(t)\cong k.
\]
A free resolution of \(M\) is
\[
0 \longrightarrow A \xrightarrow{\cdot t} A \longrightarrow A/(t) \longrightarrow 0.
\]

We check exactness carefully:

the map \(A\to A/(t)\) is the natural quotient map, whose kernel is \((t)\). Since \(A\) is a domain, multiplication by \(t\) gives an injective map
\[
A \xrightarrow{\cdot t} A
\]
whose image is exactly \((t)\). So the sequence is exact.

This resolution is minimal because the matrix entry \(t\) lies in \(\mathfrak m\).

Now tensor with \(k=A/\mathfrak m\). Since \(t\) becomes zero mod \(\mathfrak m\), the complex becomes
\[
0 \longrightarrow k \xrightarrow{0} k \longrightarrow 0.
\]
Therefore
\[
\Tor_0^A(k,M)\cong k,
\qquad
\Tor_1^A(k,M)\cong k,
\qquad
\Tor_i^A(k,M)=0 \text{ for } i\ge 2.
\]
Hence
\[
\operatorname{pd}_A(M)=1.
\]

This matches the formula:
\[
\operatorname{pd}_A(M)
=
\min \bigl\{\, i \;\big|\; \Tor_{i+1}^A(k,M)=0 \,\bigr\}
=
1,
\]
because \(\Tor_2^A(k,M)=0\) but \(\Tor_1^A(k,M)\neq 0\).

```

### Candidate #4 — IMP-DL-3C59D9EE8B-P093 — score 0.3308
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex` `L3248-L3459`
- Problem number: `17`
- lexical=0.4484 math=0.2944 number=0.0000 family=0.0000
```text
\section{Problem 17 --- Auslander--Buchsbaum formula}

\textbf{Exact statement.}
Let \(A\) be a Noetherian local ring and \(M\) a finitely generated \(A\)-module with
\[
\operatorname{pd}_A M<\infty.
\]
Show that
\[
\operatorname{pd}_A M+\operatorname{depth}(M)=\operatorname{depth}(A).
\]

\textbf{Solution.}
This is the Auslander--Buchsbaum formula.

We use the standard characterization of depth:
\[
\operatorname{depth}(N)
=
\min\{\,i\ge 0 \mid \operatorname{Ext}_A^i(k,N)\neq 0\,\},
\qquad k=A/\mathfrak m,
\]
for every nonzero finitely generated \(A\)-module \(N\).

Set
\[
s:=\operatorname{depth}(A),
\qquad
n:=\operatorname{pd}_A M.
\]
We prove that
\[
n+\operatorname{depth}(M)=s
\]
by induction on \(n\).

\medskip

\textbf{Case \(n=0\).}
If \(\operatorname{pd}_A M=0\), then \(M\) is projective. Since \(A\) is local and \(M\) is finitely generated, \(M\) is free. Thus
\[
M\cong A^r
\]
for some \(r>0\). Therefore
\[
\operatorname{Ext}_A^i(k,M)\cong \bigl(\operatorname{Ext}_A^i(k,A)\bigr)^r
\]
for all \(i\), and hence
\[
\operatorname{depth}(M)=\operatorname{depth}(A)=s.
\]
So
\[
\operatorname{pd}_A M+\operatorname{depth}(M)=0+s=s=\operatorname{depth}(A).
\]

\medskip

\textbf{Case \(n=1\).}
Assume \(\operatorname{pd}_A M=1\). Take a minimal free presentation
\[
0\longrightarrow K \xrightarrow{f} F \xrightarrow{g} M \longrightarrow 0
\]
with \(K\) and \(F\) free. Since \(K\) and \(F\) are free,
\[
\operatorname{depth}(K)=\operatorname{depth}(F)=s.
\]

By Problem 14(c), the induced maps
\[
f_*:\operatorname{Ext}_A^i(k,K)\to \operatorname{Ext}_A^i(k,F)
\]
are zero for all \(i\). Hence the long exact \(\operatorname{Ext}\)-sequence breaks into short exact sequences
\[
0\to \operatorname{Ext}_A^i(k,F)
\to \operatorname{Ext}_A^i(k,M)
\to \operatorname{Ext}_A^{i+1}(k,K)
\to 0
\]
for all \(i\ge 0\).

Now if \(i<s-1\), then
\[
\operatorname{Ext}_A^i(k,F)=0
\quad\text{and}\quad
\operatorname{Ext}_A^{i+1}(k,K)=0,
\]
so
\[
\operatorname{Ext}_A^i(k,M)=0.
\]
For \(i=s-1\), we have
\[
\operatorname{Ext}_A^{s-1}(k,F)=0,
\qquad
\operatorname{Ext}_A^s(k,K)\neq 0,
\]
hence
\[
\operatorname{Ext}_A^{s-1}(k,M)\neq 0.
\]
Therefore
\[
\operatorname{depth}(M)=s-1.
\]
So
\[
\operatorname{pd}_A M+\operatorname{depth}(M)=1+(s-1)=s=\operatorname{depth}(A).
\]

\medskip

\textbf{Induction step.}
Assume the formula holds for all finitely generated modules of projective dimension \(n-1\), and let \(\operatorname{pd}_A M=n>1\).

Take the beginning of a minimal free resolution:
\[
0\longrightarrow K \longrightarrow F \longrightarrow M \longrightarrow 0,
\]
where \(F\) is free and
\[
\operatorname{pd}_A K=n-1.
\]

By the induction hypothesis,
\[
\operatorname{depth}(K)=s-(n-1).
\]
Set
\[
t:=\operatorname{depth}(K)=s-n+1.
\]
Since \(n>1\), we have
\[
t<s.
\]
Also \(F\) is free, so
\[
\operatorname{depth}(F)=s.
\]

Apply \(\operatorname{Hom}_A(k,-)\) to the exact sequence
\[
0\to K\to F\to M\to 0.
\]
For each \(i\), the resulting long exact sequence contains
\[
\operatorname{Ext}_A^i(k,F)\to \operatorname{Ext}_A^i(k,M)\to \operatorname{Ext}_A^{i+1}(k,K)\to \operatorname{Ext}_A^{i+1}(k,F).
\]

Since \(\operatorname{depth}(F)=s>t\), we know that
\[
\operatorname{Ext}_A^j(k,F)=0
\qquad\text{for all }j\le t.
\]
Therefore, for \(i<t-1\), both outer terms vanish:
\[
\operatorname{Ext}_A^i(k,F)=0,
\qquad
\operatorname{Ext}_A^{i+1}(k,F)=0.
\]
Because also \(i+1<t\), we have
\[
\operatorname{Ext}_A^{i+1}(k,K)=0.
\]
Hence
\[
\operatorname{Ext}_A^i(k,M)=0
\qquad\text{for all }i<t-1.
\]

Now take \(i=t-1\). Since \(t<s\), we still have
\[
\operatorname{Ext}_A^{t-1}(k,F)=0,
\qquad
\operatorname{Ext}_A^{t}(k,F)=0.
\]
So the long exact sequence gives an isomorphism
\[
\operatorname{Ext}_A^{t-1}(k,M)\cong \operatorname{Ext}_A^t(k,K).
\]
But
\[
\operatorname{Ext}_A^t(k,K)\neq 0
\]
by the definition of \(t=\operatorname{depth}(K)\). Therefore
\[
\operatorname{Ext}_A^{t-1}(k,M)\neq 0.
\]
It follows that
\[
\operatorname{depth}(M)=t-1=s-n.
\]

Thus
\[
\operatorname{pd}_A M+\operatorname{depth}(M)
=
n+(s-n)=s=\operatorname{depth}(A).
\]

This completes the induction.

\medskip

Hence for every finitely generated \(A\)-module \(M\) of finite projective dimension,
\[
\boxed{
	\operatorname{pd}_A M+\operatorname{depth}(M)=\operatorname{depth}(A).
}
\]

```

### Candidate #5 — IMP-DL-CAA415139D-P052 — score 0.3030
- Source: `Downloads/theory-of-commutative-algebra-10.tex` `L2841-L2875`
- Problem number: `4`
- lexical=0.2785 math=0.2562 number=0.0000 family=1.0000
```text
\subsubsection{Example 4: \(k\) over \(A=k[[x,y]]\)}

Let
\[
A=k[[x,y]],\qquad \m=(x,y),\qquad M=k=A/\m.
\]

The quotient map
\[
A\to k
\]
is minimal, since its kernel is
\[
(x,y)\subseteq \m A.
\]

Now resolve \((x,y)\). It is generated by \(x\) and \(y\), so define
\[
A^2\to A,\qquad (a,b)\mapsto ax+by.
\]
Its kernel is generated by \((-y,x)\). Therefore we get the exact sequence
\[
0\to A \xrightarrow{\begin{pmatrix}-y\\x\end{pmatrix}} A^2 \xrightarrow{(x\ \ y)} A \to k \to 0.
\]

This is a minimal free resolution.

\paragraph{Why is it minimal?}

Both differentials have matrix entries in \(\m=(x,y)\):
\[
(x\ \ y),\qquad \begin{pmatrix}-y\\x\end{pmatrix}.
\]
So all entries lie in \(\m\), hence the resolution is minimal.

```

### Editorial decision
- `ACCEPT <problem_id>`
- `NOT_A_PROBLEM`
- `MISSING_COMPANION_STATEMENT`
- `NO_GOOD_MATCH`
- `NEEDS_MANUAL_REVIEW`

---

## P2 — SOLSEM-F0C1695725CA
- Review proposal: **EDITORIAL_REVIEW_POST_STRUCTURAL_FREEZE**
- Prior decision: `PRIOR_STRUCTURAL_RESCAN`
- Solution source: `Downloads/theory-of-real-analysis.tex` `L2238-L2244`
- Source problem number: `9.3`
- Refresh top1=0.3054 margin=0.0326

### Solution block
```text
\paragraph{Solution.}
Since $S$ has measure zero, the contribution of $f$ to any upper sum can be made arbitrarily small. 
Thus $f$ is Riemann integrable on $A$, and
\[
\int_A f(z)\,dz=0.
\]

```

### Candidate #1 — IMP-DL-20E278E436-R002160-7EC1330C — score 0.3054
- Source: `Downloads/merged_exercises_FULL_v2 (1).tex` `L2160-L2179`
- Problem number: `9.3`
- lexical=0.1432 math=0.1765 number=1.0000 family=1.0000
```text
\subsection*{Exercise 9.3}

Let $A=[-1,1]\times[-1,1]$ and define
\[
f(x,y)=
\begin{cases}
	1, & x\notin\mathbb{Q},\ y=0,\\[0.3em]
	0, & \text{otherwise}.
\end{cases}
\]

\paragraph{Background.}
- The function $f$ takes values only $0$ or $1$, so it is bounded.  
- It is nonzero only along the horizontal line segment
\[
S=\{(x,0): x\in[-1,1],\, x\notin\mathbb{Q}\}.
\]
- The set $S$ is a subset of a line in $\mathbb{R}^2$, and such sets have \emph{measure zero}.  
- For the Riemann integral, bounded functions supported on measure-zero sets are integrable with integral $0$.  

```

### Candidate #2 — IMP-DL-20E278E436-R001329-0167F814 — score 0.2729
- Source: `Downloads/merged_exercises_FULL_v2 (1).tex` `L1329-L1342`
- Problem number: `6.3`
- lexical=0.2663 math=0.1600 number=0.0000 family=1.0000
```text
\subsection*{Exercise 6.3}
Let $f:[a,b]\to\mathbb{R}^m$ be bounded.

\begin{enumerate}[label=\alph*)]
	\item Define what it means for $f$ to be Riemann integrable.
	\item Show that if each coordinate function $f_i:[a,b]\to\mathbb{R}$ is Riemann integrable, 
	then $f$ is integrable and
	\[
	\int_a^b f(x)\,dx = \left(\int_a^b f_1(x)\,dx,\;\dots,\;\int_a^b f_m(x)\,dx\right).
	\]
	\item Conversely, show that if $f$ is integrable then each coordinate $f_i$ is integrable 
	and the same equality holds.
\end{enumerate}

```

### Candidate #3 — IMP-DL-20E278E436-R001363-E6091540 — score 0.2312
- Source: `Downloads/merged_exercises_FULL_v2 (1).tex` `L1363-L1378`
- Problem number: `6.4`
- lexical=0.2025 math=0.1406 number=0.0000 family=1.0000
```text
\subsection*{Exercise 6.4}
Suppose $f,g:[a,b]\to\mathbb{R}^m$ are Riemann integrable and $\alpha,\beta\in\mathbb{R}$.

\begin{enumerate}[label=\alph*)]
	\item Show that $\alpha f+\beta g$ is integrable and
	\[
	\int_a^b (\alpha f(x)+\beta g(x))\,dx 
	= \alpha \int_a^b f(x)\,dx + \beta \int_a^b g(x)\,dx.
	\]
	
	\item Show that
	\[
	\left\|\int_a^b f(x)\,dx\right\| \leq \int_a^b \|f(x)\|\,dx.
	\]
\end{enumerate}

```

### Candidate #4 — IMP-DL-A11279CC33-P013 — score 0.2166
- Source: `Downloads/theory-of-commutative-algebra-6.tex` `L1636-L1641`
- Problem number: ``
- lexical=0.2928 math=0.1951 number=0.0000 family=0.0000
```text
	\subsubsection{Example: \(k[x]\)}
	Since \(k[x]\) is a domain, the zero ideal is prime. Thus
	\[
	\Min(k[x])=\{(0)\}.
	\]
	
```

### Candidate #5 — IMP-DL-20E278E436-P024 — score 0.2162
- Source: `Downloads/merged_exercises_FULL_v2 (1).tex` `L2190-L2250`
- Problem number: `9.4`
- lexical=0.1711 math=0.1538 number=0.0000 family=1.0000
```text
\subsection*{Exercise 9.4}

Let $A=[a_1,b_1]\times[a_2,b_2]$ and $|A|=(b_1-a_1)(b_2-a_2)$.  
Suppose $f,g:A\to\mathbb{R}$ are integrable.

\paragraph{Background.}
For a bounded function $f$ on $A$, let
\[
m=\inf_{x\in A} f(x), \quad M=\sup_{x\in A} f(x).
\]
Then $m\leq f(x)\leq M$ for all $x\in A$. Multiplying by the area $|A|$ and integrating yields inequalities for the integral.  
Key facts:
\begin{itemize}
	\item If $f\geq 0$, then $\int_A f\geq 0$.
	\item If $f\leq g$, then $\int_A f\leq \int_A g$.
	\item The triangle inequality: $\left|\int f\right|\leq \int |f|$.
\end{itemize}

\begin{enumerate}[label=\alph*)]
	
	\item For all $x\in A$, $\inf_A f\leq f(x)\leq \sup_A f$.  
	Integrating:
	\[
	|A|\inf_{x\in A} f(x)\;\leq\;\int_A f(x)\,dx\;\leq\;|A|\sup_{x\in A} f(x).
	\]
	
	\item Applying (a) to both $f$ and $-f$:
	\[
	-|A|\sup_{x\in A}|f(x)|\leq \int_A f(x)\,dx \leq |A|\sup_{x\in A}|f(x)|.
	\]
	Thus
	\[
	\left|\int_A f(x)\,dx\right|\leq |A|\sup_{x\in A}|f(x)|.
	\]
	
	\item If $f(x)\geq 0$, then $\inf_A f\geq 0$. By (a),
	\[
	0\leq \int_A f(x)\,dx.
	\]
	
	\item If $f(x)\leq g(x)$, then $0\leq g(x)-f(x)$.  
	By (c),
	\[
	0\leq \int_A (g-f)=\int_A g-\int_A f,
	\]
	so
	\[
	\int_A f \leq \int_A g.
	\]
	
	\item Since $-f(x)\leq |f(x)|$ and $f(x)\leq |f(x)|$, integrating gives
	\[
	-\int_A |f|\leq \int_A f \leq \int_A |f|.
	\]
	Thus
	\[
	\left|\int_A f(x)\,dx\right|\leq \int_A |f(x)|\,dx.
	\]
	
\end{enumerate}

```

### Editorial decision
- `ACCEPT <problem_id>`
- `NOT_A_PROBLEM`
- `MISSING_COMPANION_STATEMENT`
- `NO_GOOD_MATCH`
- `NEEDS_MANUAL_REVIEW`

---

## P2 — SOLSEM-8BD310C9A992
- Review proposal: **EDITORIAL_REVIEW_POST_STRUCTURAL_FREEZE**
- Prior decision: `PRIOR_STRUCTURAL_RESCAN`
- Solution source: `Downloads/theory-of-commutative-algebra-12.tex` `L2775-L2798`
- Source problem number: ``
- Refresh top1=0.2964 margin=0.0152

### Solution block
```text
\textbf{Solution.}
No, in general the quotient is not the same. Distinct real linear factors over \(\mathbb{R}\) lead to quotients such as
\[
\mathbb{R}\times \mathbb{R},
\]
whereas distinct irreducible quadratic factors with no real roots lead to quotients such as
\[
\mathbb{C}\times \mathbb{C}.
\]
These are not isomorphic as \(\mathbb{R}\)-algebras. In higher dimensions the difference persists: products of real linear factors describe unions of real hyperplanes, while products of irreducible quadratic factors may describe components with no real points and different residue fields.

\subsection{Why \(\mathbb{C}\) appears when we quotient \(\mathbb{R}[t]\) by \((t^2+1)\)}

A natural question is the following:

\medskip

Why do we suddenly obtain \(\mathbb{C}\) when starting from the real polynomial ring \(\mathbb{R}[t]\)?  
Why do we seem to ``shift'' from \(\mathbb{R}\) to \(\mathbb{C}\)?

\medskip

The answer is that we do \emph{not} arbitrarily change the base field. Rather, the quotient ring itself naturally becomes a field isomorphic to \(\mathbb{C}\).

```

### Candidate #1 — IMP-DL-B7B63B4C41-P002 — score 0.2964
- Source: `Downloads/theory-of-commutative-algebra-12.tex` `L384-L428`
- Problem number: `2`
- lexical=0.2903 math=0.2000 number=0.0000 family=1.0000
```text
\subsubsection{Example 2: affine line over \(\R\)}

Let
\[
X=\Spec(\R[t]).
\]

\paragraph{Real rational point}

Take
\[
\p=(t-a),\qquad a\in \R.
\]
Then
\[
\R[t]/(t-a)\cong \R,
\]
hence
\[
k(x)=\R.
\]

So these are the ordinary real points.

\paragraph{A closed point that is not \(\R\)-rational}

Now take
\[
\p=(t^2+1).
\]
Since \(t^2+1\) is irreducible in \(\R[t]\), this ideal is prime, in fact maximal. Then
\[
\R[t]/(t^2+1)\cong \C.
\]
Since this quotient is already a field, its fraction field is itself:
\[
k(x)=\Frac(\R[t]/(t^2+1))\cong \C.
\]

This is a very important example.  
It shows that a closed point of a scheme over \(\R\) does \emph{not} have to have residue field \(\R\).  
It may have residue field a finite algebraic extension of \(\R\).

Geometrically, the polynomial \(t^2+1\) has no real root, but scheme-theoretically it still defines a closed point of \(\Spec(\R[t])\).

```

### Candidate #2 — IMP-DL-B7B63B4C41-P009 — score 0.2812
- Source: `Downloads/theory-of-commutative-algebra-12.tex` `L3198-L3453`
- Problem number: ``
- lexical=0.2685 math=0.1896 number=0.0000 family=1.0000
```text
\subsubsection{Example: complexifying the crossing lines}

Let
\[
A=\mathbb{R}[s,t]/(st).
\]
Then
\[
A\otimes_{\mathbb{R}}\mathbb{C}
\cong
\mathbb{C}[s,t]/(st).
\]

Nothing new factors here, because \(st\) was already split into linear factors over \(\mathbb{R}\).  
So base change to \(\mathbb{C}\) does not simplify the equation further.

This contrasts with irreducible quadratic factors, which do split after complexification.

\subsubsection{Tensoring and residue fields}

If \(x\in \Spec(A)\) corresponds to a prime ideal \(\mathfrak p\), its residue field is
\[
k(x)=\Frac(A/\mathfrak p)
\]
in the affine domain case, or more generally
\[
k(x)=A_{\mathfrak p}/\mathfrak p A_{\mathfrak p}.
\]

When one tensors with a field extension \(K\), the residue field may enlarge or split.

For example, over \(\mathbb{R}\), the point defined by
\[
(t^2+1)
\]
has residue field
\[
\mathbb{R}[t]/(t^2+1)\cong \mathbb{C}.
\]
After base change to \(\mathbb{C}\), this point splits into two \(\mathbb{C}\)-points corresponding to
\[
(t-i)
\qquad\text{and}\qquad
(t+i).
\]

So tensoring explains geometrically why a non-\(\mathbb{R}\)-rational point may become several \(K\)-rational points after extending scalars.

\subsubsection{A key algebraic formula}

It is useful to record the central formula again:

\[
(A/I)\otimes_A B \cong B/IB.
\]

This may be specialized in several important ways.

\paragraph{Polynomial case.}
If \(A=k[x_1,\dots,x_n]\) and \(B=K[x_1,\dots,x_n]\), then
\[
\bigl(k[x_1,\dots,x_n]/I\bigr)\otimes_k K
\cong
K[x_1,\dots,x_n]/IK.
\]

\paragraph{One polynomial.}
If \(f\in k[t]\), then
\[
\bigl(k[t]/(f)\bigr)\otimes_k K
\cong
K[t]/(f).
\]

\paragraph{Residue field extension.}
If \(k(x)\) is the residue field of a point, then tensoring \(k(x)\) with a larger base field can reveal whether that point splits over the larger field.

\subsubsection{How ideals behave under tensoring}

Let \(I=(f_1,\dots,f_r)\subseteq k[x_1,\dots,x_n]\).  
After extending scalars to \(K\), the ideal becomes
\[
IK=(f_1,\dots,f_r)\subseteq K[x_1,\dots,x_n].
\]

So tensoring does not change the formal equations; it changes only the coefficient field in which one interprets them.

However, the behavior of those equations may change dramatically, because the larger field may contain new roots or allow new factorizations.

For example:

\[
(t^2+1)\subseteq \mathbb{R}[t]
\]
is prime, because \(t^2+1\) is irreducible over \(\mathbb{R}\).

But after extending scalars to \(\mathbb{C}\), we get
\[
(t^2+1)\subseteq \mathbb{C}[t],
\]
and now
\[
t^2+1=(t-i)(t+i),
\]
so the ideal is no longer prime.

Thus tensoring can turn a prime ideal into a reducible ideal after base change.

\subsubsection{Geometric meaning of tensoring}

From the geometric point of view, tensoring corresponds to changing the base field.

If \(X=\Spec(A)\) is a \(k\)-scheme and \(K/k\) is a field extension, then the base change of \(X\) to \(K\) is
\[
X_K = X\times_{\Spec(k)} \Spec(K),
\]
and on coordinate rings this corresponds to
\[
A\otimes_k K.
\]

So all the algebraic identities above are really descriptions of geometric base change.

For example:

\begin{itemize}
	\item
	\[
	\Spec(\mathbb{R}[t]/(t^2+1))
	\]
	is one closed point over \(\mathbb{R}\) with residue field \(\mathbb{C}\),
	
	\item after base change to \(\mathbb{C}\), we get
	\[
	\Spec(\mathbb{C}[t]/(t^2+1))
	\cong
	\Spec(\mathbb{C}\times \mathbb{C}),
	\]
	which is two \(\mathbb{C}\)-points.
\end{itemize}

This is one of the clearest examples of why tensor products are central in algebraic geometry.

\subsubsection{A compact summary of the main examples}

\paragraph{Example 1.}
\[
\mathbb{R}[t]/(t-a)\cong \mathbb{R}.
\]
Tensoring with \(\mathbb{C}\) gives
\[
\bigl(\mathbb{R}[t]/(t-a)\bigr)\otimes_{\mathbb{R}}\mathbb{C}
\cong
\mathbb{C}[t]/(t-a)
\cong
\mathbb{C}.
\]

\paragraph{Example 2.}
\[
\mathbb{R}[t]/(t^2+1)\cong \mathbb{C}.
\]
Tensoring with \(\mathbb{C}\) gives
\[
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}
\cong
\mathbb{C}[t]/(t^2+1)
\cong
\mathbb{C}\times \mathbb{C}.
\]

\paragraph{Example 3.}
\[
\mathbb{R}[t]/((t-1)(t-2))\cong \mathbb{R}\times \mathbb{R}.
\]
Tensoring with \(\mathbb{C}\) gives
\[
(\mathbb{R}\times\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}
\cong
\mathbb{C}\times \mathbb{C}.
\]

\paragraph{Example 4.}
\[
\mathbb{R}[s,t]/(st)
\]
describes two crossing real lines, and
\[
\bigl(\mathbb{R}[s,t]/(st)\bigr)\otimes_{\mathbb{R}}\mathbb{C}
\cong
\mathbb{C}[s,t]/(st).
\]

\paragraph{Example 5.}
\[
\mathbb{R}[t]/\bigl((t^2+1)(t^2+4)\bigr)\cong \mathbb{C}\times \mathbb{C},
\]
and after tensoring with \(\mathbb{C}\),
\[
\mathbb{C}[t]/\bigl((t^2+1)(t^2+4)\bigr)\cong \mathbb{C}^4.
\]

\subsubsection{Final conclusion}

Polynomial rings, ideals, quotients, and tensor products fit together through a single powerful principle:
\[
(A/I)\otimes_A B \cong B/IB.
\]

For polynomial rings this becomes:
\[
\bigl(k[x_1,\dots,x_n]/I\bigr)\otimes_k K
\cong
K[x_1,\dots,x_n]/IK.
\]

This explains:

\begin{itemize}
	\item why quotient rings change when the base field changes,
	\item why irreducible real polynomials may split over \(\mathbb{C}\),
	\item why residue fields may enlarge,
	\item why a point over \(\mathbb{R}\) may become several points over \(\mathbb{C}\),
	\item and why tensor products are fundamental in algebraic geometry.
\end{itemize}

\medskip

\textbf{Solution.}
To add tensoring to the theory of polynomial rings, ideals, and quotients, the key fact is that quotient and tensor product commute:
\[
(A/I)\otimes_A B \cong B/IB.
\]
Applied to polynomial rings, this gives
\[
\bigl(k[x_1,\dots,x_n]/I\bigr)\otimes_k K
\cong
K[x_1,\dots,x_n]/IK.
\]
Thus changing scalars from \(k\) to \(K\) simply replaces the coefficient field and transports the same equations. Over a larger field, irreducible polynomials may factor further, prime ideals may split, and points with residue fields larger than \(k\) may decompose into several \(K\)-rational points. This is exactly what happens with
\[
\mathbb{R}[t]/(t^2+1),
\]
which is one real closed point with residue field \(\mathbb{C}\), but after tensoring with \(\mathbb{C}\) becomes
\[
\mathbb{C}[t]/(t^2+1)\cong \mathbb{C}\times\mathbb{C}.
\]
So tensoring is the algebraic mechanism that makes base change visible.







	
```

### Candidate #3 — IMP-DL-A470D9BACB-R001506-FDCC2936 — score 0.1977
- Source: `Downloads/theory-of-geometry-1.tex` `L1506-L1511`
- Problem number: `11`
- lexical=0.3102 math=0.0741 number=0.0000 family=0.0000
```text
\subsection*{Problem 11 (Frobenius theorem via Brouwer fixed point)}

\textbf{Statement.} Let $A$ be an $n\times n$ real matrix with all entries nonnegative.
Show that $A$ has a nonnegative real eigenvalue.

\medskip
```

### Candidate #4 — IMP-DL-B7B63B4C41-P008 — score 0.1896
- Source: `Downloads/theory-of-commutative-algebra-12.tex` `L1584-L1616`
- Problem number: ``
- lexical=0.1161 math=0.1760 number=0.0000 family=1.0000
```text
\subsubsection{Example}

Take \(k=\mathbb{R}\), \(a=1\), \(b=2\). Then
\[
\mathbb{R}[s,t]/(s-1,t-2)\cong \mathbb{R},
\]
and the class of a polynomial is determined by its value at \((1,2)\).

For example:
\[
[s^2+t]\mapsto 1^2+2=3,
\]
\[
[s+t]\mapsto 1+2=3,
\]
so
\[
[s^2+t]=[s+t]
\]
in the quotient, because both polynomials have the same value at \((1,2)\).

\subsubsection{Final summary}

Therefore, saying that
\[
k[s,t]/(s-a,t-b)\cong k
\]
means that after imposing
\[
s=a,\qquad t=b,
\]
every polynomial reduces to its scalar value at that point, and the quotient ring is exactly the field \(k\) of those values.

```

### Candidate #5 — IMP-DL-B7B63B4C41-P001 — score 0.1779
- Source: `Downloads/theory-of-commutative-algebra-12.tex` `L334-L383`
- Problem number: `1`
- lexical=0.1129 math=0.1351 number=0.0000 family=1.0000
```text
\subsubsection{Example 1: affine line over a field}

Let
\[
X=\Spec(k[t]),
\]
where \(k\) is a field.

Prime ideals in \(k[t]\) are of two basic types:

\begin{itemize}[leftmargin=2em]
	\item the zero ideal \((0)\),
	\item ideals generated by irreducible polynomials.
\end{itemize}

\paragraph{Closed rational point}

Take the prime ideal
\[
\p=(t-a),\qquad a\in k.
\]
Then
\[
k[t]/(t-a)\cong k,
\]
so
\[
k(x)=\Frac(k[t]/(t-a))\cong \Frac(k)\cong k.
\]

Thus the point \(t=a\) is a \(k\)-rational point.

\paragraph{Generic point}

Take
\[
\p=(0).
\]
Then
\[
k(x)=\Frac(k[t]/(0))=\Frac(k[t])=k(t).
\]

So the generic point of the affine line has residue field \(k(t)\), the rational function field in one variable.

\paragraph{Closed non-rational point}

If \(k\) is not algebraically closed, there may be maximal ideals generated by irreducible polynomials of degree \(>1\).  
For example, over \(\R\), the ideal \((t^2+1)\) is maximal, and its residue field is \(\C\); this is treated in detail below.

```

### Editorial decision
- `ACCEPT <problem_id>`
- `NOT_A_PROBLEM`
- `MISSING_COMPANION_STATEMENT`
- `NO_GOOD_MATCH`
- `NEEDS_MANUAL_REVIEW`

---

## P3 — SOLSEM-75628998F7B0
- Review proposal: **STRONG_CANDIDATE_EDITORIAL_CHECK**
- Prior decision: ``
- Solution source: `Downloads/theory-of-analysis-FD2.tex` `L2757-L2797`
- Source problem number: `4.5`
- Refresh top1=0.7062 margin=0.1139

### Solution block
```text
\subsection*{Solution to Exercise 4.5}

We consider the inhomogeneous Helmholtz equation
\[
-\Delta\phi + k^{2}\phi = f, \qquad f\in\mathcal{S}(\mathbb{R}^3).
\]

Taking Fourier transforms and using
$\widehat{-\Delta\phi}(\xi)=|\xi|^2\widehat{\phi}(\xi)$, we obtain
\[
(|\xi|^2 + k^{2})\widehat{\phi}(\xi) = \widehat{f}(\xi).
\]
Hence
\[
\widehat{\phi}(\xi) = \frac{\widehat{f}(\xi)}{|\xi|^2 + k^{2}}.
\]
Since $f\in\mathcal{S}$, we have $\widehat{f}\in\mathcal{S}$.  The multiplier
$(|\xi|^2 + k^{2})^{-1}$ is smooth with at most polynomial growth, so
$\mathcal{S}$ is stable under multiplication by it.  Thus
$\widehat{\phi}\in\mathcal{S}$ and $\phi\in\mathcal{S}$.  Uniqueness follows:
if $f=0$ then $(|\xi|^2+k^{2})\widehat{\phi}=0$, so $\widehat{\phi}=0$ and
$\phi=0$.

From Exercise~4.4 we know that
\[
\widehat{G}(\xi) = \frac{1}{|\xi|^2 + k^{2}},
\]
where $G(x)=e^{-k|x|}/(4\pi|x|)$.  Therefore
\[
\widehat{\phi}(\xi)
= \widehat{f}(\xi)\,\widehat{G}(\xi)
= \widehat{f*G}(\xi).
\]
By injectivity of the Fourier transform on $\mathcal{S}$, we obtain
$\phi = f*G$, that is
\[
\phi(x) = \int_{\mathbb{R}^3} f(y)G(x-y)\,dy.
\]

\bigskip

```

### Candidate #1 — IMP-DL-11EDF39EA7-P010 — score 0.7062
- Source: `Downloads/theory-of-analysis-FD2.tex` `L1499-L1575`
- Problem number: `4.1`
- lexical=0.9050 math=0.4219 number=0.0000 family=1.0000
```text
\subsection*{Exercise 4.1}

Consider the ODE
\begin{equation}
	-\phi''(x) + \phi(x) = f(x), \qquad f:\mathbb{R}\to\mathbb{C}.
\end{equation}

\paragraph{(a)}
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

\paragraph{(b)}
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

### Candidate #2 — IMP-DL-11EDF39EA7-P011 — score 0.5923
- Source: `Downloads/theory-of-analysis-FD2.tex` `L1576-L2058`
- Problem number: `4.1`
- lexical=0.7931 math=0.2178 number=0.0000 family=1.0000
```text
\subsection*{Exercise 4.1}

Consider the ODE
\begin{equation}
	-\phi''(x) + \phi(x) = f(x), \qquad f:\mathbb{R}\to\mathbb{C}.
\end{equation}

\paragraph{(a)}
Consider the ODE
\begin{equation}
	-\phi''(x) + \phi(x) = f(x), \qquad f:\mathbb{R}\to\mathbb{C}.
\end{equation}

\paragraph{(a)}
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

\medskip
\noindent
It comes from the Fourier transform of derivatives.  
Start with
\[
-\phi''(x)+\phi(x)=f(x).
\]
Taking the Fourier transform in $x$ and using linearity,
\[
\widehat{-\phi''+\phi}(\xi)
= -\,\widehat{\phi''}(\xi) + \widehat{\phi}(\xi).
\]

We use the standard identity (with the convention
$\widehat{g}(\xi)=\int_{\mathbb{R}} e^{-2\pi i x\xi} g(x)\,dx$):
\[
\widehat{g'}(\xi) = (2\pi i\xi)\,\widehat{g}(\xi).
\]
Applying it twice gives
\[
\widehat{g''}(\xi)
= (2\pi i\xi)^2 \widehat{g}(\xi)
= -4\pi^{2}\xi^{2}\widehat{g}(\xi).
\]

Taking $g=\phi$, we obtain
\[
\widehat{\phi''}(\xi) = -4\pi^{2}\xi^{2}\widehat{\phi}(\xi).
\]

Substituting this into the transformed equation,
\[
\widehat{-\phi''+\phi}(\xi)
= -\,\widehat{\phi''}(\xi) + \widehat{\phi}(\xi)
= -\big(-4\pi^{2}\xi^{2}\widehat{\phi}(\xi)\big) + \widehat{\phi}(\xi)
= (4\pi^{2}\xi^{2}+1)\widehat{\phi}(\xi).
\]

\paragraph{(b)}
Define the Green's function
\[
G(x)=
\begin{cases}
	\frac12 e^{x}, & x<0,\\[0.3em]
	\frac12 e^{-x}, & x\ge 0.
\end{cases}
\]
A direct calculation yields
\[
\widehat{G}(\xi) = \frac{1}{1+4\pi^{2}\xi^{2}}.
\]
Thus
\[
\widehat{\phi}(\xi)
= \widehat{f}(\xi)\,\widehat{G}(\xi)
= \widehat{f*G}(\xi),
\]
and by injectivity of the Fourier transform,
\[
\boxed{
	\phi(x) = (f*G)(x)
	= \int_{\mathbb{R}} f(y)\,G(x-y)\,dy.
}
\]

\bigskip

\subsubsection*{Illustrations}

\paragraph{1. Compactly supported bump function and its Fourier transform.}

\begin{figure}[h!]
	\centering
	\includegraphics[width=0.47\textwidth]{bump_function.png}
	\hfill
	\includegraphics[width=0.47\textwidth]{bump_fourier_magnitude.png}
	\caption{Left: $f(x)=e^{-1/(1-x^{2})}$ on $|x|<1$. 
		Right: numerical magnitude of $\widehat{f}(\xi)$.}
\end{figure}

\paragraph{2. Green's function for $-\phi''+\phi=f$.}

\begin{figure}[h!]
	\centering
	\includegraphics[width=0.65\textwidth]{greens_function.png}
	\caption{Green's function $G(x)=\frac12 e^{-|x|}$.}
\end{figure}

\paragraph{3. Example convolution $f*G$.}

\begin{figure}[h!]
	\centering
	\includegraphics[width=0.70\textwidth]{convolution_example.png}
	\caption{Convolution of $G$ with $f(x)=e^{-x^{2}}$.}
\end{figure}

\clearpage

\subsection*{Exercise 4.2 (Radial Fourier Transform in $\mathbb{R}^{3}$)}

Suppose $f \in L^{1}(\mathbb{R}^{3})$ is a radial function, i.e.\ $f(Rx) = f(x)$
whenever $R \in SO(3)$ is a rotation.

\begin{enumerate}[(a)]
	\item Show that $\widehat{f}$ is radial.
	
	\item Suppose that $\xi = (0,0,\zeta)$. By writing the Fourier integral in
	spherical coordinates, show that
	\[
	\widehat{f}(\xi)
	= \int_{r=0}^{\infty}\int_{\theta=0}^{\pi}\int_{\phi=0}^{2\pi}
	f(r)\,e^{-i\zeta r \cos\theta}\,r^{2}\sin\theta\,d\phi\,d\theta\,dr.
	\]
	
	\item Making the substitution $s=\cos\theta$, and using the fact that
	$\widehat{f}$ is radial, deduce that
	\[
	\widehat{f}(\xi)
	= 4\pi \int_{0}^{\infty}
	f(r)\,\frac{\sin(r|\xi|)}{r|\xi|}\,r^{2}\,dr
	\]
	for any $\xi \in \mathbb{R}^{3}$.
\end{enumerate}


Suppose $f\in L^{1}(\mathbb{R}^{3})$ is a radial function, i.e.\ $f(Rx)=f(x)$ for all rotations
$R\in SO(3)$.

\paragraph{(a)}
To show that $\widehat{f}$ is radial, take any $R\in SO(3)$:
\[
\widehat{f}(R\xi)
= \int_{\mathbb{R}^{3}} f(x)e^{-2\pi i x\cdot (R\xi)}\,dx.
\]
With the substitution $x=Ry$ (Jacobian $=1$),
\[
\widehat{f}(R\xi)
= \int_{\mathbb{R}^{3}} f(Ry)e^{-2\pi i (Ry)\cdot (R\xi)}\,dy.
\]
Since $f$ is radial, $f(Ry)=f(y)$, and rotations preserve dot products:
$(Ry)\cdot (R\xi)=y\cdot\xi$. Hence
\[
\widehat{f}(R\xi)=\int_{\mathbb{R}^{3}} f(y)e^{-2\pi i y\cdot\xi}\,dy=\widehat{f}(\xi),
\]
showing that $\widehat{f}$ is radial.

\paragraph{(b)}
Since $\widehat{f}$ is radial, we may assume $\xi=(0,0,\zeta)$ with
$\zeta=|\xi|$. In spherical coordinates
$x=(r,\theta,\phi)$, one has
\[
x\cdot\xi=r\zeta\cos\theta,
\qquad
dx=r^{2}\sin\theta\,dr\,d\theta\,d\phi,
\qquad
f(x)=f(r).
\]
Thus
\[
\widehat{f}(\xi)
=\int_{0}^{\infty}\int_{0}^{\pi}\int_{0}^{2\pi}
f(r)e^{-i\zeta r\cos\theta}\,
r^{2}\sin\theta\;d\phi\,d\theta\,dr.
\]

\paragraph{(c)}
Substituting $s=\cos\theta$ gives
\[
\int_{0}^{\pi} e^{-i\zeta r\cos\theta}\sin\theta\,d\theta
=\int_{-1}^{1} e^{-i\zeta r s}\,ds
=2\frac{\sin(\zeta r)}{\zeta r}.
\]
Since $\int_{0}^{2\pi} d\phi = 2\pi$, we obtain
\[
\widehat{f}(\xi)
=4\pi \int_{0}^{\infty}
f(r)\,\frac{\sin(r|\xi|)}{r|\xi|}\,r^{2}\,dr.
\]
Thus $\widehat{f}$ is radial and given by
\[
\boxed{
	\widehat{f}(\xi)
	=4\pi\int_{0}^{\infty} f(r)\,\frac{\sin(r|\xi|)}{r|\xi|}\,r^{2}\,dr.
}
\]


\subsubsection*{Theory: Radial Fourier transform in $\mathbb{R}^3$}

A function $f:\mathbb{R}^{3}\to\mathbb{C}$ is called \emph{radial} if
there is $F:[0,\infty)\to\mathbb{C}$ such that
\[
f(x) = F(|x|)\qquad\text{for all }x\in\mathbb{R}^{3}.
\]
Equivalently, $f$ is invariant under all rotations:
\[
f(Rx) = f(x)\qquad\text{for all }R\in SO(3).
\]

\paragraph{Fourier transform and rotations.}
The Fourier transform in $\mathbb{R}^{3}$ is
\[
\widehat{f}(\xi)
= \int_{\mathbb{R}^{3}} f(x)\,e^{-2\pi i x\cdot\xi}\,dx.
\]
For any rotation $R\in SO(3)$, one has
\[
\widehat{f\circ R}(\xi)
= \widehat{f}(R^{-1}\xi).
\]
Indeed,
\[
\widehat{f\circ R}(\xi)
= \int_{\mathbb{R}^{3}} f(Rx)e^{-2\pi i x\cdot\xi}\,dx
= \int_{\mathbb{R}^{3}} f(y)e^{-2\pi i (Ry)\cdot\xi}\,dy
= \int_{\mathbb{R}^{3}} f(y)e^{-2\pi i y\cdot (R^{-1}\xi)}\,dy
= \widehat{f}(R^{-1}\xi),
\]
where we used the change of variables $x=Ry$ and the fact that rotations
preserve dot products. If $f$ is radial, then $f\circ R=f$ for all $R$, hence
\[
\widehat{f}(R\xi) = \widehat{f}(\xi)\qquad\forall R\in SO(3),
\]
and thus $\widehat{f}$ is radial as well.

\paragraph{Spherical coordinates.}
Since $\widehat{f}$ is radial, its value at $\xi$ depends only on $|\xi|$.
Given $\xi\in\mathbb{R}^{3}$ with $|\xi|>0$, we choose a rotation $R$ such that
\[
R\xi = (0,0,|\xi|).
\]
Using radiality of $\widehat{f}$ we may compute $\widehat{f}(R\xi)$ instead of
$\widehat{f}(\xi)$; in spherical coordinates $x=(r,\theta,\phi)$ we have
\[
x\cdot R\xi = r|\xi|\cos\theta,
\qquad
dx = r^{2}\sin\theta\,dr\,d\theta\,d\phi,
\qquad
f(x)=f(r).
\]
Therefore,
\begin{equation}\label{eq:radial-FT-spherical}
	\widehat{f}(\xi)
	= \int_{0}^{\infty}\int_{0}^{\pi}\int_{0}^{2\pi}
	f(r)\,e^{-i r|\xi|\cos\theta}\,r^{2}\sin\theta\,
	d\phi\,d\theta\,dr.
\end{equation}

\paragraph{Angular integration and the 3D radial kernel.}
The $\phi$--integral is trivial:
\[
\int_{0}^{2\pi} d\phi = 2\pi.
\]
For the $\theta$--integral we use the substitution $s=\cos\theta$,
$ds=-\sin\theta\,d\theta$, which gives
\[
\int_{0}^{\pi} e^{-i r|\xi|\cos\theta}\sin\theta\,d\theta
= \int_{-1}^{1} e^{-i r|\xi| s}\,ds
= 2\,\frac{\sin(r|\xi|)}{r|\xi|}.
\]
Inserting these into \eqref{eq:radial-FT-spherical} yields
\[
\widehat{f}(\xi)
= 4\pi \int_{0}^{\infty}
f(r)\,\frac{\sin(r|\xi|)}{r|\xi|}\,r^{2}\,dr,
\]
which is the standard formula for the Fourier transform of a radial
$L^{1}$-function in $\mathbb{R}^{3}$.

\paragraph{Remark (connection with Bessel functions).}
In general dimension $n$, the Fourier transform of a radial function involves
Bessel functions and can be written as
\[
\widehat{f}(\xi)
= (2\pi)^{n/2}|\xi|^{-(n/2-1)}
\int_{0}^{\infty} f(r)\,
J_{n/2-1}(2\pi r|\xi|)\,r^{n/2}\,dr.
\]
For $n=3$ this reduces to the above formula, since the corresponding Bessel
function combination is
\[
\frac{\sin(r|\xi|)}{r|\xi|},
\]
the spherical Bessel function of order $0$.

\subsubsection*{Examples of radial Fourier transforms in $\mathbb{R}^3$}

\paragraph{Example 1 (Indicator of a ball).}
Let
\[
f(x) = \mathbf{1}_{\{|x|\le a\}}(x), \qquad a>0.
\]
Then $f$ is radial with $f(r)=1$ for $0\le r\le a$ and $0$ otherwise, and the
radial Fourier transform formula gives
\[
\widehat{f}(\xi)
=4\pi\int_0^a \frac{\sin(r|\xi|)}{r|\xi|}\,r^2\,dr
=\frac{4\pi}{|\xi|}\int_0^a r\sin(r|\xi|)\,dr.
\]
Using
\[
\int r\sin(\rho r)\,dr
= -\frac{r\cos(\rho r)}{\rho}
+\frac{\sin(\rho r)}{\rho^2} + C,
\]
we obtain, with $\rho=|\xi|$,
\[
\int_0^a r\sin(\rho r)\,dr
= -\frac{a\cos(\rho a)}{\rho}
+\frac{\sin(\rho a)}{\rho^2}.
\]
Hence
\[
\widehat{f}(\xi)
=4\pi\left(
\frac{\sin(a|\xi|)}{|\xi|^3}
-\frac{a\cos(a|\xi|)}{|\xi|^2}
\right),
\qquad \xi\neq 0.
\]
The value at $\xi=0$ is given by continuity and equals the volume of the ball,
$\widehat{f}(0)=\frac{4\pi a^3}{3}$.

\paragraph{Example 2 (Gaussian).}
Consider the radial Gaussian
\[
f(x)=e^{-|x|^2}, \qquad x\in\mathbb{R}^3.
\]
Using the one-dimensional identity
\[
\int_{\mathbb{R}} e^{-x^2} e^{-i x\xi}\,dx
= \sqrt{\pi}\,e^{-\xi^2/4},
\]
and the factorisation $e^{-|x|^2}=e^{-x_1^2}e^{-x_2^2}e^{-x_3^2}$, we obtain
\[
\widehat{f}(\xi)
= \bigl(\sqrt{\pi} e^{-\xi_1^2/4}\bigr)
\bigl(\sqrt{\pi} e^{-\xi_2^2/4}\bigr)
\bigl(\sqrt{\pi} e^{-\xi_3^2/4}\bigr)
= \pi^{3/2} e^{-|\xi|^2/4}.
\]
Thus
\[
\boxed{
	\widehat{e^{-|x|^2}}(\xi)
	= \pi^{3/2} e^{-|\xi|^2/4},
}
\]
which is manifestly radial. This is consistent with the radial integral
\[
\widehat{f}(\xi)
= 4\pi\int_0^\infty e^{-r^2}
\frac{\sin(r|\xi|)}{r|\xi|}\,r^2\,dr.
\]

\paragraph{Example 3 (Yukawa kernel).}
Let
\[
f(x) = \frac{e^{-|x|}}{|x|}, \qquad x\in\mathbb{R}^3,
\]
so that $f(r)=e^{-r}/r$ is radial and integrable. Then
\[
\widehat{f}(\xi)
= 4\pi\int_0^\infty \frac{e^{-r}}{r}\,
\frac{\sin(r|\xi|)}{r|\xi|}\,r^2\,dr
= 4\pi\frac{1}{|\xi|}
\int_0^\infty e^{-r}\sin(r|\xi|)\,dr.
\]
Using the Laplace transform identity
\[
\int_0^\infty e^{-r}\sin(\rho r)\,dr
= \frac{\rho}{1+\rho^2},
\]
with $\rho=|\xi|$, we find
\[
\widehat{f}(\xi)
= \frac{4\pi}{1+|\xi|^2}.
\]
This radial function is (up to constants) the Fourier symbol of the resolvent
$(-\Delta+1)^{-1}$.

\subsubsection*{Figures: Yukawa Kernel and its Fourier Transform}

\begin{figure}[h!]
	\centering
	\includegraphics[width=0.60\textwidth]{yukawa_function.png}
	\caption{Radial Yukawa kernel in $\mathbb{R}^3$:
		$f(r)=e^{-r}/r$. The function decays exponentially and
		has a singularity of order $1/r$ at $r=0$.}
\end{figure}

\begin{figure}[h!]
	\centering
	\includegraphics[width=0.60\textwidth]{yukawa_fourier.png}
	\caption{Fourier transform of the Yukawa kernel:
		$\widehat f(\xi)=\dfrac{4\pi}{1+|\xi|^{2}}$.
		This is the symbol of the resolvent $(-\Delta+1)^{-1}$.}
\end{figure}

\subsubsection*{Comparison: Coulomb Kernel vs. Yukawa Kernel}

The Coulomb kernel in $\mathbb{R}^3$ is
\[
K_{\mathrm{C}}(x) = \frac{1}{|x|},
\]
and the Yukawa kernel is
\[
K_{\mathrm{Y}}(x) = \frac{e^{-|x|}}{|x|}.
\]
Both are radial functions of $r=|x|$. The Yukawa kernel introduces exponential
screening of the long-range $1/r$ interaction.

\begin{figure}[h!]
	\centering
	\includegraphics[width=0.70\textwidth]{coulomb_vs_yukawa_linear.png}
	\caption{Linear-scale comparison of the Coulomb kernel $1/r$ and the Yukawa
		kernel $e^{-r}/r$. The Yukawa potential coincides with Coulomb near $r=0$ but
		decays exponentially for large $r$.}
\end{figure}

\begin{figure}[h!]
	\centering
	\includegraphics[width=0.70\textwidth]{coulomb_vs_yukawa_loglog.png}
	\caption{Log--log comparison. The Coulomb kernel exhibits pure algebraic decay
		$r^{-1}$, while the Yukawa kernel decays as $e^{-r}/r$, much faster at large
		distances.}
\end{figure}

```

### Candidate #3 — IMP-DL-11EDF39EA7-P014 — score 0.5337
- Source: `Downloads/theory-of-analysis-FD2.tex` `L2408-L2604`
- Problem number: `4.3`
- lexical=0.6778 math=0.2523 number=0.0000 family=1.0000
```text
\subsection*{Exercise 4.3 (Fourier--Plancherel Transform) -- Solutions}

We use the convention
\[
\mathcal{F}[f](\xi) = \widehat{f}(\xi)
:= \int_{\mathbb{R}^n} f(x)e^{-ix\cdot\xi}\,dx,
\qquad
\mathcal{F}^{-1}[g](x)
= \frac{1}{(2\pi)^n}\int_{\mathbb{R}^n} g(\xi)e^{ix\cdot\xi}\,d\xi.
\]

\paragraph{(a) Plancherel identity.}
For $f,g\in\mathcal{S}(\mathbb{R}^n)$, using inversion we write
\[
f(x) = \frac{1}{(2\pi)^n}
\int_{\mathbb{R}^n} \widehat{f}(\xi)e^{ix\cdot\xi}\,d\xi,
\]
so
\[
(f,g)
= \int_{\mathbb{R}^n} f(x)\,\overline{g(x)}\,dx
= \frac{1}{(2\pi)^n}
\int_{\mathbb{R}^n}
\widehat{f}(\xi)\left(\int_{\mathbb{R}^n} e^{ix\cdot\xi}
\overline{g(x)}\,dx\right)d\xi.
\]
The inner integral equals $\overline{\widehat{g}(\xi)}$, hence
\[
(f,g) = \frac{1}{(2\pi)^n}
\int_{\mathbb{R}^n} \widehat{f}(\xi)\,
\overline{\widehat{g}(\xi)}\,d\xi
= \frac{1}{(2\pi)^n}(\widehat{f},\widehat{g}).
\]
By density of $\mathcal{S}$ in $L^2$ and continuity of $\mathcal{F}$ on
$L^2$, the formula extends to arbitrary $f,g\in L^2(\mathbb{R}^n)$.

\paragraph{(b) Double transform and bijectivity.}
For $f\in\mathcal{S}$,
\[
\widehat{f}(\xi) = \int_{\mathbb{R}^n} f(x)e^{-ix\cdot\xi}\,dx,
\]
and
\[
\mathcal{F}[\widehat{f}](y)
= \int_{\mathbb{R}^n} \widehat{f}(\xi)e^{-iy\cdot\xi}\,d\xi
= \int_{\mathbb{R}^n}\!\!\int_{\mathbb{R}^n}
f(x)e^{-ix\cdot\xi}e^{-iy\cdot\xi}\,dx\,d\xi.
\]
Swapping the integrals and using that
$\int_{\mathbb{R}^n}e^{-i(x+y)\cdot\xi}\,d\xi = (2\pi)^n\delta(x+y)$ gives
\[
\mathcal{F}[\widehat{f}](y)
= (2\pi)^n f(-y)
= (2\pi)^n \check{f}(y).
\]
By continuity this identity holds for all $f\in L^2$.  In particular,
$\mathcal{F}$ is injective and its range is all of $L^2$; thus
$\mathcal{F}:L^2\to L^2$ is a bijection.  The inverse is bounded by the
Plancherel identity.

\paragraph{(c) Truncated integrals in $L^2$.}
For $R>0$ set
\[
\widehat{f}_R(\xi)
:= \int_{B_R(0)} f(x)e^{-ix\cdot\xi}\,dx
= \mathcal{F}[\chi_{B_R}f](\xi).
\]
Then
\[
\widehat{f}_R - \widehat{f}
= \mathcal{F}[(\chi_{B_R}-1)f],
\]
and by Plancherel,
\[
\|\widehat{f}_R - \widehat{f}\|_{L^2}
= (2\pi)^{n/2}\,\|(\chi_{B_R}-1)f\|_{L^2}.
\]
Since $\chi_{B_R}\to 1$ pointwise and $|\chi_{B_R}|\le 1$, dominated
convergence gives $\|(\chi_{B_R}-1)f\|_{L^2}\to 0$ as $R\to\infty$, hence
$\widehat{f}_R\to\widehat{f}$ in $L^2(\mathbb{R}^n)$.

\paragraph{(d) Differentiation.}
First assume $f\in\mathcal{S}(\mathbb{R}^n)$.  Then
\[
\mathcal{F}[D_j f](\xi)
= \int_{\mathbb{R}^n} (\partial_{x_j}f(x))e^{-ix\cdot\xi}\,dx
= -\int_{\mathbb{R}^n} f(x)\,\partial_{x_j}(e^{-ix\cdot\xi})\,dx
= i\xi_j\widehat{f}(\xi),
\]
since boundary terms vanish due to rapid decay.  For
$f\in C^1(\mathbb{R}^n)$ with $f,D_j f\in L^2$, choose a sequence
$f_k\in\mathcal{S}$ such that $f_k\to f$ and $D_j f_k\to D_j f$ in $L^2$.
The identity for $f_k$, together with the boundedness of $\mathcal{F}$ on
$L^2$, allows passage to the limit and yields
\[
\mathcal{F}[D_j f](\xi) = i\xi_j\widehat{f}(\xi)
\]
and hence $\xi_j\widehat{f}\in L^2$.

\paragraph{(e) The function $f(x)=\sin x/x$.}
\subparagraph*{(i) $f\in L^2(\mathbb{R})$.}
Near $x=0$ one has $\sin x\sim x$, so $\sin x/x$ is bounded and continuous.
For large $|x|$,
\[
\left|\frac{\sin x}{x}\right|
\le \frac{1}{|x|},
\]
hence
\[
\left|\frac{\sin x}{x}\right|^2 \le \frac{1}{x^2},
\]
and $\int_{|x|>1} x^{-2}\,dx<\infty$.  Therefore $f\in L^2(\mathbb{R})$.

\subparagraph*{(ii) Fourier transform.}
Let $g(\xi)=\mathbf{1}_{(-1,1)}(\xi)$.  Then
\[
\mathcal{F}^{-1}[g](x)
= \frac{1}{2\pi}\int_{-1}^{1} e^{ix\xi}\,d\xi
= \frac{1}{2\pi}\left(\frac{e^{ix}-e^{-ix}}{ix}\right)
= \frac{1}{\pi}\frac{\sin x}{x}.
\]
Thus
\[
\frac{\sin x}{x}
= \pi\,\mathcal{F}^{-1}[\mathbf{1}_{(-1,1)}](x).
\]
Applying $\mathcal{F}$ and using $\mathcal{F}\circ\mathcal{F}^{-1}=\mathrm{Id}$
on $L^2$, we obtain
\[
\mathcal{F}\left[\frac{\sin x}{x}\right](\xi)
= \pi\,\mathbf{1}_{(-1,1)}(\xi)
=
\begin{cases}
	\pi, & -1<\xi<1,\\[0.3em]
	0,   & |\xi|\ge 1.
\end{cases}
\]

\paragraph{(f) Convolution.}
\subparagraph*{(i) Pointwise bound.}
For $x\in\mathbb{R}^n$,
\[
(f*g)(x) = \int_{\mathbb{R}^n} f(x-y)g(y)\,dy.
\]
By Cauchy--Schwarz,
\[
|f*g(x)|
\le \left(\int_{\mathbb{R}^n} |f(x-y)|^2 dy\right)^{1/2}
\left(\int_{\mathbb{R}^n} |g(y)|^2 dy\right)^{1/2}
= \|f\|_{L^2}\|g\|_{L^2}.
\]

\subparagraph*{(ii) Continuity and Fourier representation.}
For $h\in\mathbb{R}^n$,
\[
(f*g)(x+h)-(f*g)(x)
= \int_{\mathbb{R}^n} [f(x+h-y)-f(x-y)]g(y)\,dy.
\]
Again by Cauchy--Schwarz,
\[
|(f*g)(x+h)-(f*g)(x)|
\le \|f(\cdot+h)-f\|_{L^2}\,\|g\|_{L^2},
\]
and since translations are continuous in $L^2$, the right-hand side tends to
$0$ as $h\to 0$, so $f*g$ is continuous.

If $f,g\in\mathcal{S}$, the convolution theorem gives
\[
\mathcal{F}[f*g](\xi) = \widehat{f}(\xi)\,\widehat{g}(\xi),
\]
and thus
\[
f*g = \mathcal{F}^{-1}[\widehat{f}\,\widehat{g}].
\]
For $f,g\in L^2$, one approximates by Schwartz functions and uses the
boundedness of $\mathcal{F}$ and density of $\mathcal{S}$ in $L^2$ to extend
this identity.

\subsection*{Exercise 4.4 (Yukawa Green's function in $\mathbb{R}^3$)}

Work in $\mathbb{R}^3$. For $k>0$, define
\[
G(x) = \frac{e^{-k|x|}}{4\pi |x|}, \qquad x\in\mathbb{R}^3\setminus\{0\}.
\]

\begin{enumerate}[(a)]
	\item Show that $G \in L^{1}(\mathbb{R}^3)$.
	
	\item Show that
	\[
	\widehat{G}(\xi) = \frac{1}{|\xi|^2 + k^2},
	\qquad \xi\in\mathbb{R}^3.
	\]
\end{enumerate}

\noindent\emph{Hint:} Use Exercise~4.2, part (c).

```

### Candidate #4 — IMP-DL-11EDF39EA7-P031 — score 0.5309
- Source: `Downloads/theory-of-analysis-FD2.tex` `L4927-L5238`
- Problem number: ``
- lexical=0.6693 math=0.2610 number=0.0000 family=1.0000
```text
	\item Let $\alpha$ be a multiindex with $|\alpha| = k$. 
	Show that the distributional derivative
	\[
	D^\alpha : H^{s+k}(\mathbb{R}^n) \longrightarrow H^{s}(\mathbb{R}^n)
	\]
	is a bounded linear operator.
	
\end{enumerate}


% ------------------------------------------------------------
\subsection*{Theory and Solutions}

\paragraph{Sobolev norm.}
For $s\ge 0$,
\[
\|f\|_{H^s(\mathbb{R}^n)}^2
= \int_{\mathbb{R}^n} (1+|\xi|^2)^s |\widehat{f}(\xi)|^2 \, d\xi.
\]

% ------------------ (a) ---------------------
\subsubsection*{(a) \; Approximation by Smooth Functions}

\paragraph{\textbf{Goal.}}  
Show $\eta_\varepsilon * f \to f$ in $H^s$.

\paragraph{\textbf{Key fact.}}  
$\widehat{\eta_\varepsilon}(\xi)=\widehat{\eta}(\varepsilon\xi)$ and $\widehat{\eta}(0)=1$.

\paragraph{\textbf{Proof.}}
\[
\widehat{\eta_\varepsilon * f}(\xi)
= \widehat{\eta}(\varepsilon\xi)\widehat{f}(\xi).
\]
Thus,
\[
\|\eta_\varepsilon * f - f\|_{H^s}^2
= \int (1+|\xi|^2)^s 
|\widehat{\eta}(\varepsilon\xi)-1|^2 |\widehat{f}(\xi)|^2 d\xi.
\]
Since $\widehat{\eta}\in \mathscr{S}$ and $\widehat{\eta}(\varepsilon\xi)\to 1$, and  
$(1+|\xi|^2)^s|\widehat{f}(\xi)|^2\in L^1$, dominated convergence gives the result.

% ------------------ (b) ---------------------
\subsubsection*{(b) \; Approximation by Compactly Supported Smooth Functions}

\paragraph{\textbf{Idea.}}
First mollify, then cut off.

\paragraph{\textbf{Construction.}}
Let $g_\varepsilon = \eta_\varepsilon * f \to f$ in $H^s$.

Let $\chi_R\in C_0^\infty$ be a smooth cutoff with $\chi_R=1$ on $B_R$.
Define
\[
\varphi_{\varepsilon,R}(x)= \chi_R(x)\, g_\varepsilon(x).
\]
Multiplication by $\chi_R$ is bounded on $H^s$, and 
$\chi_R g_\varepsilon \to g_\varepsilon$ as $R\to\infty$.
A diagonal argument produces $\varphi_j\to f$ in $H^s$.

% ------------------ (c) ---------------------
\subsubsection*{(c) \; Monotonicity of Sobolev Norms and $L^2$ Estimate}

\paragraph{\textbf{Claim.}}
If $t\ge s$, then 
\[
(1+|\xi|^2)^s \le (1+|\xi|^2)^t,
\]
hence
\[
\|f\|_{H^s}^2 \le \|f\|_{H^t}^2.
\]

\paragraph{\textbf{$L^2$ estimate.}}
Since
\[
\|f\|_{L^2}^2 
= \frac{1}{(2\pi)^n}\int |\widehat{f}(\xi)|^2 d\xi
\le \frac{1}{(2\pi)^n} \int (1+|\xi|^2)^s |\widehat{f}(\xi)|^2 d\xi,
\]
we obtain
\[
\|f\|_{L^2} \le \frac{1}{(2\pi)^{n/2}} \|f\|_{H^s}.
\]

% ------------------ (d) ---------------------
\subsubsection*{(d) \; Boundedness of Derivatives}

\paragraph{\textbf{Goal.}}  
Show $D^\alpha : H^{s+k} \to H^{s}$ is bounded.

\paragraph{\textbf{Fourier representation.}}
\[
\widehat{D^\alpha f}(\xi) = (i\xi)^\alpha \widehat{f}(\xi).
\]

\paragraph{\textbf{Estimate.}}
Since $|\xi^\alpha| \le (1+|\xi|^2)^{k/2}$,
\[
\|D^\alpha f\|_{H^{s}}^2
= \int (1+|\xi|^2)^s |\xi^\alpha|^2 |\widehat{f}(\xi)|^2 d\xi
\le \int (1+|\xi|^2)^{s+k} |\widehat{f}(\xi)|^2 d\xi
= \|f\|_{H^{s+k}}^2.
\]
Thus $D^\alpha$ is bounded.


\subsection*{5.9 \quad Heat equation: energy estimate and heat kernel}

Suppose that \(u_0 \in L^1(\mathbb{R}^n) \cap L^2(\mathbb{R}^n)\), and let
\(u(t,x)\) be the solution of the heat equation
\[
\partial_t u - \Delta u = 0,
\qquad t>0,\ x\in\mathbb{R}^n,
\]
with initial condition \(u(0,x) = u_0(x)\).
In terms of the Fourier transform, \(u\) is given by
\[
u(t,x)
= \frac{1}{(2\pi)^n} \int_{\mathbb{R}^n}
\widehat{u_0}(\xi)\,e^{-t|\xi|^2}\,e^{i\xi\cdot x}\,d\xi,
\qquad t>0.
\]

\paragraph{\textbf{(a) Problem.}}
Show that
\[
\|u(t,\cdot)\|_{L^2(\mathbb{R}^n)}
\le \|u_0\|_{L^2(\mathbb{R}^n)}
\quad\text{for all } t>0.
\]

\paragraph{\textbf{(b) Problem.}}
Show that
\[
u(t,x) = (u_0 * K_t)(x),
\]
where the heat kernel is defined by
\[
K_t(x)
= \frac{1}{(4\pi t)^{n/2}} \exp\!\left(-\frac{|x|^2}{4t}\right),
\qquad t>0,\ x\in\mathbb{R}^n.
\]

\paragraph{\textbf{(c) Problem.}}
Assume that \(u_0 \ge 0\).
Show that \(u(t,x) \ge 0\) for all \(t>0\) and
\[
\|u(t,\cdot)\|_{L^1(\mathbb{R}^n)}
= \|u_0\|_{L^1(\mathbb{R}^n)}
\quad\text{for all } t>0.
\]

\bigskip
\paragraph{\textbf{Theory.}}
Taking the Fourier transform in the spatial variables for the heat equation
\(\partial_t u - \Delta u = 0\) yields the ODE
\[
\partial_t \widehat{u}(t,\xi) + |\xi|^2 \widehat{u}(t,\xi) = 0,
\]
whose solution is
\[
\widehat{u}(t,\xi)
= e^{-t|\xi|^2} \widehat{u_0}(\xi).
\]
Using Plancherel's theorem one obtains energy estimates in \(L^2\). The factor
\(e^{-t|\xi|^2}\) is precisely the Fourier transform of the Gaussian heat kernel
\[
K_t(x)
= \frac{1}{(4\pi t)^{n/2}} e^{-|x|^2/(4t)},
\]
and hence
\(\widehat{K_t}(\xi) = e^{-t|\xi|^2}\).
By the convolution theorem, this implies
\(u(t,\cdot) = u_0 * K_t\).
The kernel \(K_t\) is nonnegative and normalized
\(\int_{\mathbb{R}^n} K_t(x)\,dx = 1\),
so convolution with \(K_t\) preserves positivity and total mass
(\(L^1\)-norm).

\bigskip
\subsubsection*{Solution to (a): \(L^2\)-energy estimate}

\paragraph{\textbf{Step 1: Fourier representation.}}
From the theory above,
\[
\widehat{u}(t,\xi)
= e^{-t|\xi|^2} \widehat{u_0}(\xi).
\]

\paragraph{\textbf{Step 2: Use Plancherel.}}
By Plancherel's theorem,
\[
\|u(t,\cdot)\|_{L^2(\mathbb{R}^n)}^2
= \frac{1}{(2\pi)^n} \int_{\mathbb{R}^n}
|\widehat{u}(t,\xi)|^2\,d\xi
= \frac{1}{(2\pi)^n} \int_{\mathbb{R}^n}
e^{-2t|\xi|^2} |\widehat{u_0}(\xi)|^2\,d\xi.
\]
Since \(e^{-2t|\xi|^2} \le 1\),
\[
\|u(t,\cdot)\|_{L^2}^2
\le \frac{1}{(2\pi)^n} \int_{\mathbb{R}^n}
|\widehat{u_0}(\xi)|^2\,d\xi
= \|u_0\|_{L^2}^2.
\]
Taking square roots gives
\[
\|u(t,\cdot)\|_{L^2(\mathbb{R}^n)}
\le \|u_0\|_{L^2(\mathbb{R}^n)},
\]
as required.

\bigskip
\subsubsection*{Solution to (b): convolution with the heat kernel}

\paragraph{\textbf{Step 1: Gaussian heat kernel.}}
Define
\[
K_t(x)
:= \frac{1}{(4\pi t)^{n/2}} \exp\!\left(-\frac{|x|^2}{4t}\right),
\qquad t>0.
\]
A standard Fourier transform computation (see Lemma~1.9) shows that
\[
\widehat{K_t}(\xi) = e^{-t|\xi|^2}.
\]

\paragraph{\textbf{Step 2: Convolution theorem.}}
We already know that
\[
\widehat{u}(t,\xi)
= e^{-t|\xi|^2} \widehat{u_0}(\xi)
= \widehat{u_0}(\xi)\,\widehat{K_t}(\xi).
\]
By the convolution theorem,
\[
\mathcal{F}\bigl(u_0 * K_t\bigr)(\xi)
= \widehat{u_0}(\xi)\,\widehat{K_t}(\xi)
= \widehat{u}(t,\xi).
\]
Since the Fourier transform is injective, we conclude
\[
u(t,x) = (u_0 * K_t)(x)
= \int_{\mathbb{R}^n} u_0(y)\,K_t(x-y)\,dy.
\]

\bigskip
\subsubsection*{Solution to (c): positivity and conservation of mass}

Assume \(u_0 \ge 0\).

\paragraph{\textbf{Positivity.}}
From part (b),
\[
u(t,x) = \int_{\mathbb{R}^n} u_0(y)\,K_t(x-y)\,dy.
\]
Both \(u_0(y)\) and \(K_t(x-y)\) are nonnegative, hence the integral is
nonnegative:
\[
u(t,x) \ge 0
\quad\text{for all } t>0,\ x\in\mathbb{R}^n.
\]

\paragraph{\textbf{Conservation of the \(L^1\)-norm.}}
Integrating over \(\mathbb{R}^n\) and using Fubini's theorem,
\[
\int_{\mathbb{R}^n} u(t,x)\,dx
= \int_{\mathbb{R}^n} \int_{\mathbb{R}^n}
u_0(y)\,K_t(x-y)\,dy\,dx
= \int_{\mathbb{R}^n} u_0(y)
\left( \int_{\mathbb{R}^n} K_t(x-y)\,dx \right) dy.
\]
The inner integral equals \(1\), since
\[
\int_{\mathbb{R}^n} K_t(x-y)\,dx
= \int_{\mathbb{R}^n} K_t(z)\,dz = 1,
\]
by the normalization of the Gaussian.
Therefore
\[
\int_{\mathbb{R}^n} u(t,x)\,dx
= \int_{\mathbb{R}^n} u_0(y)\,dy,
\]
which shows
\[
\|u(t,\cdot)\|_{L^1(\mathbb{R}^n)}
= \|u_0\|_{L^1(\mathbb{R}^n)}.
\]

\paragraph{\textbf{Conclusion.}}
The heat semigroup \(e^{t\Delta}\) is \(L^2\)-contractive,
admits the Gaussian kernel representation, and for nonnegative data
preserves both positivity and the total mass.


\section*{Exercise 5.10 : The Schrödinger Equation in $\mathbb{R}^n$}

Consider the Schrödinger equation
\[
\begin{cases}
	u_t = i \Delta u & \text{in } (0,T)\times \mathbb{R}^n, \\
	u = u_0 & \text{on } \{0\}\times \mathbb{R}^n,
\end{cases}
\tag{3}
\]

and suppose that $u_0 \in H^2(\mathbb{R}^n)$.

\begin{enumerate}[label=\textnormal{(\alph*)}]
	
```

### Candidate #5 — IMP-DL-11EDF39EA7-P007 — score 0.5034
- Source: `Downloads/theory-of-analysis-FD2.tex` `L905-L914`
- Problem number: `3.5.`
- lexical=0.6200 math=0.2660 number=0.0000 family=1.0000
```text
\subsection*{Exercise 3.5. Fourier transforms of some $L^1$ functions}

We use the convention
\[
\widehat{f}(\xi) = \int_{\mathbb{R}} e^{-i x\xi} f(x)\,dx.
\]

\paragraph{(a)}
Let $f(x)=\dfrac{\sin x}{1+x^2}$. Compute $\widehat{f}$.

```

### Editorial decision
- `ACCEPT <problem_id>`
- `NOT_A_PROBLEM`
- `MISSING_COMPANION_STATEMENT`
- `NO_GOOD_MATCH`
- `NEEDS_MANUAL_REVIEW`

---

## P3 — SOLSEM-2ECC5725FBED
- Review proposal: **CONTENT_MATCH_EDITORIAL_CHECK**
- Prior decision: ``
- Solution source: `Downloads/theory-of-geometry-IV.tex` `L2992-L3038`
- Source problem number: `2`
- Refresh top1=0.5915 margin=0.2072

### Solution block
```text
	\subsubsection*{Solution (a): right triangle, $C=\pi/2$}
	Assume $C=\pi/2$ so $\cos(C)=0$ and $\sin(C)=1$.
	
	\paragraph{Step 1: apply the cosine formula (sides) to $c$.}
	From the side-cosine formula for $c$ we get
	\[
	\cosh(c)=\cosh(a)\cosh(b)-\sinh(a)\sinh(b)\cos(C)
	=\cosh(a)\cosh(b).
	\tag{1}
	\]
	
	\paragraph{Step 2: apply the cosine formula (sides) to $b$ and eliminate $\cosh(c)$.}
	Use the side-cosine formula for $b$:
	\[
	\cosh(b)=\cosh(c)\cosh(a)-\sinh(c)\sinh(a)\cos(B).
	\]
	Insert $\cosh(c)=\cosh(a)\cosh(b)$ from (1):
	\[
	\cosh(b)=\cosh(a)\cosh(b)\cosh(a)-\sinh(c)\sinh(a)\cos(B)
	=\cosh(b)\cosh^2(a)-\sinh(c)\sinh(a)\cos(B).
	\]
	Rearranging gives
	\[
	\sinh(c)\sinh(a)\cos(B)=\cosh(b)\bigl(\cosh^2(a)-1\bigr)=\cosh(b)\sinh^2(a).
	\]
	Hence
	\[
	\cos(B)=\cosh(b)\,\frac{\sinh(a)}{\sinh(c)}.
	\tag{2}
	\]
	
	\paragraph{Step 3: apply the cosine formula (angles) to $B$ (using $C=\pi/2$).}
	From the angle-cosine formula for $B$ and $C=\pi/2$ we obtain
	\[
	\cos(B)=-\cos(C)\cos(A)+\sin(C)\sin(A)\cosh(b)=\sin(A)\cosh(b).
	\tag{3}
	\]
	Comparing (2) and (3) and cancelling $\cosh(b)>0$ yields
	\[
	\sin(A)=\frac{\sinh(a)}{\sinh(c)}.
	\]
	Equivalently,
	\[
	\sin(A)\,\sinh(c)=\sinh(a),
	\]
	which is exactly the desired identity.
	
```

### Candidate #1 — IMP-DL-D4351A3BBD-P032 — score 0.5915
- Source: `Downloads/theory-of-geometry-IV.tex` `L2952-L2991`
- Problem number: `6`
- lexical=0.7776 math=0.2521 number=0.0000 family=1.0000
```text
	\subsection*{Problem 6 (Hyperbolic law of sines)}
	
\subsubsection*{problem}
		Fix a hyperbolic triangle $\Delta\subset \HH^2$ with interior angles $A,B,C$ and side lengths
		(in the hyperbolic metric) $a,b,c$, where $a$ is opposite the vertex with angle $A$, etc.
		\begin{enumerate}
			\item Suppose that $C$ is a right angle. By applying the \emph{hyperbolic cosine formula} in two different ways,
			prove that
			\[
			\sin(A)\,\sinh(c)=\sinh(a).
			\]
			\item Deduce that for a general hyperbolic triangle,
			\[
			\frac{\sin(A)}{\sinh(a)}=\frac{\sin(B)}{\sinh(b)}=\frac{\sin(C)}{\sinh(c)}.
			\]
		\end{enumerate}

	
	\subsubsection*{Theory: the cosine formulae in $\HH^2$}
	For a hyperbolic triangle with side lengths $a,b,c$ opposite angles $A,B,C$ one has:
	
	\begin{itemize}
		\item \textbf{Cosine formula (sides):}
		\begin{align*}
			\cosh(a)&=\cosh(b)\cosh(c)-\sinh(b)\sinh(c)\cos(A),\\
			\cosh(b)&=\cosh(c)\cosh(a)-\sinh(c)\sinh(a)\cos(B),\\
			\cosh(c)&=\cosh(a)\cosh(b)-\sinh(a)\sinh(b)\cos(C).
		\end{align*}
		
		\item \textbf{Cosine formula (angles):}
		\begin{align*}
			\cos(A)&=-\cos(B)\cos(C)+\sin(B)\sin(C)\cosh(a),\\
			\cos(B)&=-\cos(C)\cos(A)+\sin(C)\sin(A)\cosh(b),\\
			\cos(C)&=-\cos(A)\cos(B)+\sin(A)\sin(B)\cosh(c).
		\end{align*}
	\end{itemize}
	
	(These are dual to each other; one clean way to see the duality is via the \emph{polar triangle}
	in constant curvature $-1$ geometry.)
	
```

### Candidate #2 — IMP-DL-0A181AC273-P017 — score 0.3843
- Source: `Downloads/theory-of-complex-analysis.tex` `L653-L666`
- Problem number: `5.`
- lexical=0.6017 math=0.1471 number=0.0000 family=0.0000
```text
\paragraph{Problem 5.}
(i) Verify directly that $e^{z}, \cos z, \sin z$ satisfy the Cauchy--Riemann equations everywhere.\\
(ii) Find all $z$ with $|e^{iz}|>1$, and describe the set where $|e^{z}|\le e^{|z|}$.\\
(iii) Find the zeros of $1+e^{z}$ and of $\cosh z$.

\paragraph{Background.}
For $z=x+iy$,
\[
e^{z}=e^{x}(\cos y+i\sin y),\qquad
\sin z=\sin x\cosh y+i\cos x\sinh y,\qquad
\cos z=\cos x\cosh y-i\sin x\sinh y.
\]
If $f=u+iv$, the CR equations are $u_x=v_y$ and $u_y=-v_x$.

```

### Candidate #3 — IMP-DL-E88547CF67-P021 — score 0.3074
- Source: `Downloads/theory-of-geometry-3.tex` `L2985-L3037`
- Problem number: `8`
- lexical=0.4483 math=0.1975 number=0.0000 family=0.0000
```text
	\subsection*{Problem 8 (Weierstrass data for catenoid and helicoid)}
	We use the Weierstrass representation in the $(f,g)$-form:
	\[
	X(z)=\Re\int^z \Big(\tfrac12 f(1-g^2),\ \tfrac{i}{2}f(1+g^2),\ fg\Big)\,dz,
	\]
	where $g$ is meromorphic, $f$ is holomorphic, and the resulting parametrization is conformal and minimal.
	
	\medskip
	\textbf{Choice of complex parameter.}
	For the given real parameters $(u,v)$, the catenoid/helicoid are conformal in $(u,v)$, and it is convenient to set
	\[
	z=v+iu.
	\]
	Thus a suitable domain is the strip
	\[
	D=\{z=v+iu\in\mathbb{C}:\ v\in\mathbb{R},\ 0<u<2\pi\}.
	\]
	
	\medskip
	\textbf{Catenoid.}
	Take
	\[
	g(z)=e^{z},\qquad f(z)=a e^{-z}.
	\]
	Then
	\[
	\tfrac12 f(1-g^2)=\frac{a}{2}(e^{-z}-e^{z})=-a\sinh z,\qquad
	\tfrac{i}{2}f(1+g^2)=\frac{ia}{2}(e^{-z}+e^{z})=i a\cosh z,
	\]
	and $fg=a$. Hence
	\[
	X(z)=\Re\bigl(-a\cosh z,\ i a\sinh z,\ a z\bigr).
	\]
	With $z=v+iu$ this becomes (up to a rigid motion in the $xy$-plane)
	\[
	X(u,v)=\bigl(a\cosh v\cos u,\ a\cosh v\sin u,\ a v\bigr),
	\]
	which is exactly the given catenoid parametrization (possibly after rotating by $\pi$ about the $z$-axis).
	
	\medskip
	\textbf{Helicoid.}
	Keep the same $g(z)=e^{z}$ but replace $f$ by $if$:
	\[
	g(z)=e^{z},\qquad f(z)= i a e^{-z}.
	\]
	This is the classical associate surface construction. Substituting yields a parametrization which, after a rigid motion
	and a harmless shift of $u$, is the given helicoid
	\[
	\phi(u,v)=\bigl(a\sinh v\cos u,\ a\sinh v\sin u,\ a u\bigr).
	\]
	(Geometrically: multiplying $f$ by $i$ rotates the Weierstrass integrand by $90^\circ$ in the associate family.)
	
	\bigskip
```

### Candidate #4 — IMP-DL-AD9EFCAF62-P024 — score 0.2927
- Source: `Downloads/theory-of-complex-analysis-2.tex` `L1238-L1583`
- Problem number: `7`
- lexical=0.4543 math=0.1215 number=0.0000 family=0.0000
```text
\paragraph{Problem 7 (cotangent trick and square contour).}
Let $N\in\mathbb N$ and let $\gamma_N$ be the square contour with vertices
$(\pm1\pm i)\bigl(N+\tfrac12\bigr)$, oriented positively.
\begin{enumerate}[label=(\roman*)]
	\item Show that there exists a constant $C>0$, independent of $N$, such that
	\[
	|\cot(\pi z)|<C \qquad \text{for all } z\in\gamma_N .
	\]
	\item By integrating $\displaystyle \frac{\pi\cot(\pi z)}{z^{2}+1}$ around $\gamma_N$,
	prove that
	\[
	\sum_{n=0}^{\infty}\frac{1}{n^{2}+1}\;=\;\frac{1+\pi\coth\pi}{2}\, .
	\]
	\item Evaluate the alternating series
	\[
	\sum_{n=0}^{\infty}\frac{(-1)^{n}}{n^{2}+1}\, .
	\]
\end{enumerate}

% (Place your solution from before here.)

\paragraph{7. (i) Uniform bound for $|\cot \pi z|$ on $\gamma_N$.}
With $z=x+iy$ one has
\[
|\sin(\pi z)|^{2}=\sin^{2}(\pi x)+\sinh^{2}(\pi y),\qquad
|\cos(\pi z)|^{2}=\cos^{2}(\pi x)+\sinh^{2}(\pi y).
\]
On the \emph{vertical} sides $x=\pm(N+\tfrac12)$ we get
$\sin(\pi x)=\pm1$, $\cos(\pi x)=0$, hence
\[
\cot(\pi z)=-i\,\tanh(\pi y),\qquad |\cot(\pi z)|\le 1.
\]
On the \emph{horizontal} sides $y=\pm(N+\tfrac12)$,
\[
|\cot(\pi z)|^{2}
=\frac{\cos^{2}(\pi x)+\sinh^{2}(\pi y)}{\sin^{2}(\pi x)+\sinh^{2}(\pi y)}
\le 1+\frac{1}{\sinh^{2}(\pi|y|)}
\le 1+\frac{1}{\sinh^{2}(\pi/2)}.
\]
Thus there is a constant
$C=\max\!\big\{1,\sqrt{1+\sinh^{-2}(\pi/2)}\big\}$, independent of $N$, such that
$|\cot \pi z|<C$ on $\gamma_N$.

\medskip
\paragraph{(ii) $\displaystyle \sum_{n=0}^{\infty}\frac{1}{n^{2}+1}$.}
Let $F(z)=\dfrac{\pi\cot(\pi z)}{z^{2}+1}$. Then on $\gamma_N$,
$|F(z)|\lesssim C/|z|^{2}$, so $\int_{\gamma_N}F(z)\,dz\to0$ as $N\to\infty$.
Residues:
\[
\Res(F;n)=\frac{1}{n^{2}+1}\quad(n\in\mathbb Z),
\qquad
\Res(F;i)=\Res(F;-i)=\frac{\pi\cot(\pi i)}{2i}.
\]
Since $\cot(\pi i)=-i\,\coth\pi$, we have
$\Res(F;i)+\Res(F;-i)=-\pi\coth\pi$.
Hence, letting $N\to\infty$,
\[
0=\int_{\gamma_N}F
=2\pi i\!\left(\sum_{n\in\mathbb Z}\frac{1}{n^{2}+1}-\pi\coth\pi\right)
\ \Rightarrow\ 
\sum_{n\in\mathbb Z}\frac{1}{n^{2}+1}=\pi\coth\pi.
\]
By symmetry,
\[
\boxed{\ \sum_{n=0}^{\infty}\frac{1}{n^{2}+1}=\frac{1+\pi\coth\pi}{2}\ }.
\]

\medskip
\paragraph{(iii) $\displaystyle \sum_{n=0}^{\infty}\frac{(-1)^{n}}{n^{2}+1}$.}
Set $G(z)=\dfrac{\pi\csc(\pi z)}{z^{2}+1}$.
Again $\int_{\gamma_N}G\to0$ and
\[
\Res(G;n)=\frac{(-1)^{n}}{n^{2}+1}\quad(n\in\mathbb Z),
\qquad
\csc(\pi i)=\frac{1}{\sin(\pi i)}=\frac{1}{i\sinh\pi}=-i\,\mathrm{csch}\,\pi.
\]
Therefore
\[
\Res(G;i)+\Res(G;-i)
=\frac{\pi\csc(\pi i)}{2i}+\frac{\pi\csc(-\pi i)}{-2i}
=-\pi\,\mathrm{csch}\,\pi.
\]
Thus
\[
\sum_{n\in\mathbb Z}\frac{(-1)^{n}}{n^{2}+1}
=\pi\,\mathrm{csch}\,\pi,
\qquad
\boxed{\ \sum_{n=0}^{\infty}\frac{(-1)^{n}}{n^{2}+1}
	=\frac{1+\pi\,\mathrm{csch}\,\pi}{2}\ }.
\]
\qed

\paragraph{Complex cotangent: identities and geometry.}

\emph{Core identities.} For $z=x+iy$,
\[
\sin(\pi z)=\sin(\pi x)\cosh(\pi y)+i\cos(\pi x)\sinh(\pi y),\quad
\cos(\pi z)=\cos(\pi x)\cosh(\pi y)-i\sin(\pi x)\sinh(\pi y),
\]
hence
\[
|\sin(\pi z)|^2=\sin^2(\pi x)+\sinh^2(\pi y),\qquad
|\cos(\pi z)|^2=\cos^2(\pi x)+\sinh^2(\pi y).
\]
Also
\[
\cot z=i\,\coth(iz)=i\,\frac{e^{2iz}+1}{e^{2iz}-1}.
\]

\emph{Poles, residues, partial fractions.}
$\cot$ has simple poles at $k\pi$ with residue $1$; $\pi\cot(\pi z)$ has simple poles at integers with residue $1$.
\[
\pi\cot(\pi z)=\sum_{n\in\mathbb Z}\frac{1}{z-n}.
\]

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Write
\[
\cot(x+iy)=\frac{\sin 2x - i\,\sinh 2y}{\cosh 2y - \cos 2x}=u(x)+iv(x).
\]
Eliminating $x$ yields the circle
\[
\boxed{\ u^2+\big(v+\coth 2y\big)^2=\csch^2 2y\ },
\]
i.e.\ for fixed $y$ the image is a circle centered at $-i\,\coth 2y$ with radius $\csch 2y$ (orthogonal to the imaginary axis). As $y\to\pm\infty$ this circle collapses to the point $\mp i$; as $y\to0$ it expands and approaches the real axis.

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$, as $y$ varies,
\[
\cot(x+iy)\to -\,i\ (y\to+\infty),\qquad \cot(x+iy)\to +\,i\ (y\to-\infty),
\]
and $\cot(x+0i)=\cot x\in\mathbb R$. Thus the image is a circular arc joining $\pm i$ and crossing the real axis at $\cot x$ (orthogonal to the family in the previous paragraph).

\medskip
\paragraph{Strips, bands, and Möbius viewpoint.}
Because $\cot z=\tan(\tfrac{\pi}{2}-z)$, the vertical strip $\{0<\Re z<\pi\}$ is mapped bijectively onto $\mathbb C$, and periodicity $\cot(z+\pi)=\cot z$ tiles the plane by such strips.
Via $e^{2iz}=e^{-2y}e^{2ix}$ a horizontal strip $y\in(y_1,y_2)$ maps to an annulus; the Möbius map $w\mapsto i\frac{w+1}{w-1}$ then sends annuli to circular bands bounded by the circles $u^2+(v+\coth 2y)^2=\csch^2 2y$.

\medskip
\paragraph{Bounds on large squares (for residue summations).}
On the square with vertices $(\pm1\pm i)(N+\tfrac12)$,
\[
|\cot(\pi z)|\le 1 \ \text{on vertical edges},\qquad
|\cot(\pi z)|^2\le 1+\frac{1}{\sinh^2(\pi/2)} \ \text{on horizontal edges},
\]
so there is a constant $C$ independent of $N$ with $|\cot(\pi z)|<C$ on the boundary.

\medskip
\emph{Asymptotics and symmetries.}
$\cot(-z)=-\cot z$, $\overline{\cot(\bar z)}=\cot z$, and $\cot(x+iy)\to\mp i$ as $y\to\pm\infty$.
These give quick qualitative sketches of level sets and images.
	
\paragraph{Short derivation of the horizontal-circle equation.}
Let $z=x+iy$ and set
\[
\cot z=\frac{\sin 2x-i\,\sinh 2y}{\cosh 2y-\cos 2x}=u+iv,\qquad
D:=\cosh 2y-\cos 2x,\ S:=\sinh 2y,\ C:=\cosh 2y.
\]
Then
\[
u=\frac{\sin 2x}{D},\qquad v=-\frac{S}{D}\ \Longrightarrow\ D=-\frac{S}{v}.
\]
Hence
\[
\sin 2x=uD=-\frac{uS}{v},\qquad \cos 2x = C - D = C+\frac{S}{v}.
\]
Now
\[
u^{2}+\Bigl(v+\frac{C}{S}\Bigr)^{2}
=\frac{1}{D^{2}}\!\left[\sin^{2}2x+\frac{(1-C\cos 2x)^{2}}{S^{2}}\right].
\]
Using $D=C-\cos 2x$ and $\cosh^{2}2y-\sinh^{2}2y=1$ we get
\[
S^{2}\sin^{2}2x+(1-C\cos 2x)^{2}=(C-\cos 2x)^{2}=D^{2}.
\]
Therefore
\[
\boxed{\,u^{2}+\bigl(v+\coth 2y\bigr)^{2}=\csch^{2}2y\,},
\]
i.e.\ for fixed $y$ the image is a circle centered at $-i\,\coth(2y)$ with radius $\csch(2y)$.
	
	
\paragraph{Hyperbolic cosecant.}
\[
\csch x=\frac{1}{\sinh x}=\frac{2}{e^{x}-e^{-x}},\qquad
\sech x=\frac{1}{\cosh x},\quad
\coth x=\frac{\cosh x}{\sinh x}.
\]
Parity and derivatives:
\[
\csch(-x)=-\csch x,\qquad
\frac{d}{dx}\csch x=-\csch x\,\coth x,\qquad
\frac{d}{dx}\coth x=-\csch^{2}x.
\]
Identity and asymptotics:
\[
\coth^{2}x-\csch^{2}x=1,\qquad
\csch x\sim 2e^{-|x|}\quad (|x|\to\infty).
\]


\paragraph{Background and geometry for $\sin z$.}

\emph{Core identities.} For $z=x+iy$,
\[
\sin z=\sin x\,\cosh y+i\,\cos x\,\sinh y,\qquad
|\sin z|^{2}=\sin^{2}x+\sinh^{2}y.
\]
Symmetries: $\overline{\sin\bar z}=\sin z$, $\sin(-z)=-\sin z$, $\sin(z+2\pi)=\sin z$.
Zeros are simple at $z=n\pi$ ($n\in\mathbb Z$) since $\sin'(n\pi)=\cos(n\pi)\neq0$.

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Let $w=\sin z=u+iv$. For fixed $y$,
\[
u=\sin x\,\cosh y,\qquad v=\cos x\,\sinh y.
\]
Eliminating $x$ gives the ellipse
\[
\boxed{\ \Big(\tfrac{u}{\cosh y}\Big)^{2}+\Big(\tfrac{v}{\sinh y}\Big)^{2}=1\ }.
\]
Thus the image is an ellipse centered at $0$ with semiaxes $\cosh y$ (real axis) and $\sinh y$ (imaginary axis).
Since $\cosh^{2}y-\sinh^{2}y=1$, the foci lie at $\pm1$, and
\[
|w-1|+|w+1|=2\cosh y.
\]

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$,
\[
u=\sin x\,\cosh y,\qquad v=\cos x\,\sinh y
\]
and eliminating $y$ using $\cosh^{2}y-\sinh^{2}y=1$ yields
\[
\boxed{\ \Big(\tfrac{u}{\sin x}\Big)^{2}-\Big(\tfrac{v}{\cos x}\Big)^{2}=1\ } \quad
(\sin x\,\cos x\ne0).
\]
Hence the image is a hyperbola with the same foci $\pm1$.
Degenerate cases:
$x=n\pi$ gives $u=0$ (imaginary axis) and $x=\frac{\pi}{2}+n\pi$ gives $v=0$ (real axis).

\medskip
\paragraph{Strips and periodicity.}
One may take the fundamental strip $S=\{\,0<\Re z<\pi\,\}$. On $x=0$ or $x=\pi$
the image is purely imaginary; in the interior the images of horizontal/vertical lines
form the orthogonal confocal families of ellipses and hyperbolas with foci $\pm1$.
(Branches of $\arcsin$ use the slits $(-\infty,-1]\cup[1,\infty)$.)


\paragraph{Background and geometry for $\cos z$.}

\emph{Core identities.} For $z=x+iy$,
\[
\cos z=\cos x\,\cosh y - i\,\sin x\,\sinh y,\qquad
|\cos z|^{2}=\cos^{2}x+\sinh^{2}y.
\]
Symmetries: $\overline{\cos\bar z}=\cos z$, $\cos(-z)=\cos z$, $\cos(z+2\pi)=\cos z$.
Zeros are simple at $z=\tfrac{\pi}{2}+n\pi$ since $\cos'(z)=-\sin z$.

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Let $w=\cos z=u+iv$. For fixed $y$,
\[
u=\cos x\,\cosh y,\qquad v=-\,\sin x\,\sinh y.
\]
Eliminating $x$ gives the ellipse
\[
\boxed{\ \Big(\tfrac{u}{\cosh y}\Big)^{2}+\Big(\tfrac{v}{\sinh y}\Big)^{2}=1\ }.
\]
Thus the image is an ellipse centered at $0$ with semiaxes $\cosh y$ (real axis) and $\sinh y$ (imaginary axis); since $\cosh^{2}y-\sinh^{2}y=1$, the foci are $\pm1$ and
\[
|w-1|+|w+1|=2\cosh y.
\]

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$,
\[
u=\cos x\,\cosh y,\qquad v=-\,\sin x\,\sinh y.
\]
Eliminating $y$ using $\cosh^{2}y-\sinh^{2}y=1$ yields
\[
\boxed{\ \Big(\tfrac{u}{\cos x}\Big)^{2}-\Big(\tfrac{v}{\sin x}\Big)^{2}=1\ } \quad
(\sin x\,\cos x\ne0),
\]
a hyperbola with the same foci $\pm1$.
Degenerate cases:
$x=n\pi$ gives $v=0$ (real axis) and $x=\tfrac{\pi}{2}+n\pi$ gives $u=0$ (imaginary axis).

\medskip
\paragraph{Strips and periodicity.}
A fundamental strip is $S=\{\,0<\Re z<\pi\,\}$. On $x=0$ or $x=\pi$ the image is real; inside $S$ the images of horizontal/vertical lines form orthogonal confocal ellipses and hyperbolas with foci $\pm1$.
(Branches of $\arccos$ use the slits $(-\infty,-1]\cup[1,\infty)$.)
	
	
\paragraph{Background and geometry for $\tan z$.}

\emph{Core identities.} For $z=x+iy$,
\[
\tan z=\frac{\sin z}{\cos z}
=\frac{\sin 2x + i\,\sinh 2y}{\cos 2x+\cosh 2y}.
\]
Thus, writing $w=\tan z=u+iv$,
\[
u=\frac{\sin 2x}{\cos 2x+\cosh 2y},\qquad
v=\frac{\sinh 2y}{\cos 2x+\cosh 2y}.
\]

\emph{Zeros, poles, residues.}
$\tan z$ has simple zeros at $z=n\pi$ and simple poles at $z=\tfrac{\pi}{2}+n\pi$ ($n\in\mathbb Z$).
At each pole, $\mathrm{Res}(\tan;z_0)=1$. The partial fraction expansion is
\[
\pi\,\tan(\pi z)=\sum_{n\in\mathbb Z}\frac{1}{\,z-(n+\tfrac12)\,}.
\]
Symmetries: $\tan(-z)=-\tan z$, $\overline{\tan\bar z}=\tan z$, and $\tan(z+\pi)=\tan z$.
As $|y|\to\infty$, $\tan(x+iy)\to i\,\mathrm{sgn}(y)$.

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Fix $y$ and set $C=\cosh(2y)$, $S=\sinh(2y)$, $D=\cos(2x)+C$. Then
\[
u=\frac{\sin 2x}{D},\qquad v=\frac{S}{D}.
\]
Eliminating $x$ (using $D=S/v$) yields the circle
\[
\boxed{\ u^{2}+\Bigl(v-\frac{\cosh(2y)}{\sinh(2y)}\Bigr)^{2}=\frac{1}{\sinh^{2}(2y)}\ }.
\]
Hence the image is a circle centered at $-i\,\dfrac{\cosh(2y)}{\sinh(2y)}$ on the imaginary axis (note the sign in $u+iv$) with radius $\dfrac{1}{|\sinh(2y)|}$.
As $y\to\pm\infty$ the circle shrinks to $\pm i$; as $y\to0$ it expands toward the real axis.

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$, as $y$ varies,
\[
\tan(x+iy)\to i \ (y\to+\infty),\qquad \tan(x+iy)\to -i \ (y\to-\infty),
\]
and $\tan(x+0i)=\tan x\in\mathbb R$. Thus the image is a circular arc joining $\pm i$ and crossing the real axis at $\tan x$ (orthogonal to the family above).

\medskip
\paragraph{Strips and periodicity.}
The vertical strip $S=\{\, -\tfrac{\pi}{2}<\Re z<\tfrac{\pi}{2}\,\}$ is mapped bijectively onto $\mathbb C$ by $\tan$; its boundary lines map to $\infty$ (simple poles). Periodicity $\tan(z+\pi)=\tan z$ tiles the plane by translates of $S$.


```

### Candidate #5 — IMP-DL-40BD8D3E26-P005 — score 0.2639
- Source: `Downloads/theory-of-geometry-2.tex` `L766-L862`
- Problem number: `2`
- lexical=0.2004 math=0.1987 number=1.0000 family=0.0000
```text
	\subsubsection*{Example 2: Helix (constant curvature and torsion)}
	Let $a>0$ and $b\in\mathbb{R}$ and define
	\[
	\alpha(t)=\big(a\cos t,\;a\sin t,\;bt\big).
	\]
	Compute derivatives:
	\[
	\alpha'(t)=(-a\sin t,\;a\cos t,\;b),\qquad
	\alpha''(t)=(-a\cos t,\;-a\sin t,\;0),\qquad
	\alpha^{(3)}(t)=(a\sin t,\;-a\cos t,\;0).
	\]
	The speed is constant:
	\[
	\|\alpha'(t)\|^2=a^2\sin^2 t+a^2\cos^2 t+b^2=a^2+b^2,
	\qquad
	\|\alpha'(t)\|=\sqrt{a^2+b^2}.
	\]
	
	\medskip
	\noindent\textbf{Cross product.}
	\[
	\alpha'(t)\times\alpha''(t)=
	\begin{vmatrix}
		\mathbf i & \mathbf j & \mathbf k\\
		-a\sin t & a\cos t & b\\
		-a\cos t & -a\sin t & 0
	\end{vmatrix}
	=(ab\sin t,\;-ab\cos t,\;a^2).
	\]
	Hence
	\[
	\|\alpha'(t)\times\alpha''(t)\|^2
	=a^2b^2(\sin^2 t+\cos^2 t)+a^4=a^2b^2+a^4=a^2(a^2+b^2),
	\]
	so
	\[
	\|\alpha'(t)\times\alpha''(t)\|=a\sqrt{a^2+b^2}.
	\]
	
	\medskip
	\noindent\textbf{Curvature.}
	For a general parameter $t$,
	\[
	k(t)=\frac{\|\alpha'(t)\times\alpha''(t)\|}{\|\alpha'(t)\|^3}
	=\frac{a\sqrt{a^2+b^2}}{(\sqrt{a^2+b^2})^3}
	=\frac{a}{a^2+b^2}.
	\]
	
	\medskip
	\noindent\textbf{Torsion.}
	Using
	\[
	\tau(t)=\frac{\det(\alpha'(t),\alpha''(t),\alpha^{(3)}(t))}{\|\alpha'(t)\times\alpha''(t)\|^2}
	=\frac{\langle \alpha'(t)\times\alpha''(t),\alpha^{(3)}(t)\rangle}{\|\alpha'(t)\times\alpha''(t)\|^2},
	\]
	we compute
	\[
	\langle \alpha'(t)\times\alpha''(t),\alpha^{(3)}(t)\rangle
	=
	\langle (ab\sin t,-ab\cos t,a^2),(a\sin t,-a\cos t,0)\rangle
	\]
	\[
	=(ab\sin t)(a\sin t)+(-ab\cos t)(-a\cos t)+a^2\cdot 0
	=a^2b(\sin^2 t+\cos^2 t)=a^2b.
	\]
	Therefore
	\[
	\tau(t)=\frac{a^2b}{a^2(a^2+b^2)}=\frac{b}{a^2+b^2}.
	\]
	Thus a helix has constant curvature $k=\frac{a}{a^2+b^2}$ and constant torsion $\tau=\frac{b}{a^2+b^2}$.
	
	\medskip
	\noindent\textbf{Unit-speed reparametrization (optional).}
	Since $\|\alpha'(t)\|=\sqrt{a^2+b^2}$, arc length satisfies $s=\sqrt{a^2+b^2}\,t$, i.e.
	$t=s/\sqrt{a^2+b^2}$. Substituting yields a unit-speed helix $\alpha(s)$ with the same constants
	$k=\frac{a}{a^2+b^2}$ and $\tau=\frac{b}{a^2+b^2}$.
	
	\medskip
	\noindent\textbf{Wedge/triple-product interpretation (used in the torsion step).}
	In $\mathbb{R}^3$ the exterior product $u\wedge v$ encodes the oriented parallelogram spanned by $u,v$ and satisfies
	\[
	\|u\wedge v\|=\|u\times v\|.
	\]
	Moreover, the pairing with a vector gives the scalar triple product (oriented volume):
	\[
	\langle u\wedge v,\;w\rangle := \det(u,v,w)=\langle u\times v,\;w\rangle.
	\]
	Thus in the torsion formula one may write equivalently
	\[
	\det(\alpha',\alpha'',\alpha^{(3)})=\big\langle \alpha'\wedge \alpha'',\;\alpha^{(3)}\big\rangle,
	\qquad
	\|\alpha'\times\alpha''\|^2=\|\alpha'\wedge\alpha''\|^2.
	\]
	So (up to the chosen sign/orientation convention) the usual determinant formula and the wedge-product formula
	for torsion are the same.
	
	
```

### Editorial decision
- `ACCEPT <problem_id>`
- `NOT_A_PROBLEM`
- `MISSING_COMPANION_STATEMENT`
- `NO_GOOD_MATCH`
- `NEEDS_MANUAL_REVIEW`

---

## P3 — SOLSEM-A3E4B3F720CA
- Review proposal: **CONTENT_MATCH_EDITORIAL_CHECK**
- Prior decision: ``
- Solution source: `Downloads/theory-of-analysis - Copy.tex` `L699-L704`
- Source problem number: ``
- Refresh top1=0.5708 margin=0.0915

### Solution block
```text
\section*{Solution (ii)}
By part (i), $f_x$ is continuous. Since $K$ is connected, its continuous image $f_x(K)$ must also be connected.  
As $\partial D$ is the unit circle, the connected subsets of $\partial D$ are either single points or arcs. Therefore $f_x(K)$ is connected in $\partial D$. \qed

---

```

### Candidate #1 — IMP-DL-15679DEE8D-P004 — score 0.5708
- Source: `Downloads/theory-of-analysis - Copy.tex` `L627-L629`
- Problem number: `7`
- lexical=0.7342 math=0.2708 number=0.0000 family=1.0000
```text
\section*{Problem 7 (ii)}
With $f_x : K \to \partial D$ defined as above, prove that if $K$ is connected, then $f_x(K)$ is connected in $\partial D$.

```

### Candidate #2 — IMP-DL-15679DEE8D-P006 — score 0.4794
- Source: `Downloads/theory-of-analysis - Copy.tex` `L671-L677`
- Problem number: `7`
- lexical=0.5927 math=0.2317 number=0.0000 family=1.0000
```text
\section*{Problem 7}
(i) Let $x$ be a point in the closed unit disc $D=\{z\in\mathbb{R}^2 : \|z\|\leq 1\}$, let $K\subseteq D$ be compact not containing $x$, and define $f_x:K\to \partial D$ as follows: for $y\in K$, take the line segment from $x$ to $y$ and extend it until it first hits the boundary $\partial D$. Call this point $f_x(y)$. Prove that $f_x$ is continuous.  

(ii) Show that if $K$ is connected, then $f_x(K)$ is connected in $\partial D$.  

---

```

### Candidate #3 — IMP-DL-15679DEE8D-P002 — score 0.3612
- Source: `Downloads/theory-of-analysis - Copy.tex` `L504-L506`
- Problem number: `7`
- lexical=0.4011 math=0.2025 number=0.0000 family=1.0000
```text
\section*{Problem 7 (i)}
Let $x$ be a point in the closed unit disc $D=\{z\in\mathbb{R}^2 : \|z\|\leq 1\}$, let $K\subseteq D$ be compact not containing $x$, and define $f_x:K\to \partial D$ as follows: for $y\in K$, take the line segment from $x$ to $y$ and extend it until it first hits the boundary $\partial D$. Call this point $f_x(y)$. Prove that $f_x$ is continuous.

```

### Candidate #4 — IMP-DL-15679DEE8D-P005 — score 0.2693
- Source: `Downloads/theory-of-analysis - Copy.tex` `L635-L670`
- Problem number: ``
- lexical=0.2710 math=0.1339 number=0.0000 family=1.0000
```text
\section*{Example}
If $K$ is a line segment inside $D$ not containing $x$, then $f_x(K)$ is the arc of the circle that subtends the segment with respect to $x$.  
If $K=D\setminus \{x\}$, then $f_x(K)=\partial D$.

\begin{figure}[h]
	\centering
	\begin{tikzpicture}[scale=2]
		% Unit circle
		\draw[thick] (0,0) circle (1);
		
		% Points inside
		\coordinate (X) at (-0.3,-0.2);
		\coordinate (A) at (0.2,0.1);
		\coordinate (B) at (0.3,0.5);
		
		% Images on boundary (approximate positions)
		\coordinate (FA) at (0.95,0.47);
		\coordinate (FB) at (0.52,0.85);
		
		% Draw rays
		\draw[dashed] (X) -- (FA);
		\draw[dashed] (X) -- (FB);
		
		% Fill points
		\fill[blue] (X) circle (0.03) node[below left]{$x$};
		\fill[red] (A) circle (0.03) node[right]{$y_1$};
		\fill[red] (B) circle (0.03) node[right]{$y_2$};
		\fill[green!70!black] (FA) circle (0.03) node[right]{$f_x(y_1)$};
		\fill[green!70!black] (FB) circle (0.03) node[above]{$f_x(y_2)$};
		
		% Arc between FA and FB
		\draw[thick,green!70!black] (FA) arc[start angle=27,end angle=59,radius=1];
	\end{tikzpicture}
	\caption{If $K$ is connected (here, a line segment), then $f_x(K)$ is a connected arc of $\partial D$.}
\end{figure}

```

### Candidate #5 — IMP-DL-D6E9B3BC73-PSR004085-E0CA1B49 — score 0.2613
- Source: `Downloads/theory-of-algebraic-topology-1.tex` `L4085-L4125`
- Problem number: `2`
- lexical=0.3914 math=0.1429 number=0.0000 family=0.0000
```text
\subsubsection{Example 2: locally path connected but not connected, hence not path connected}

Let
\[
X=[0,1]\cup[2,3]\subset \mathbb{R}.
\]

We first show that \(X\) is locally path connected.

Indeed, if \(x\in X\), then there exists a sufficiently small open interval
\[
(x-\varepsilon,x+\varepsilon)
\]
in \(\mathbb{R}\) such that
\[
(x-\varepsilon,x+\varepsilon)\cap X
\]
is either an interval in \([0,1]\) or an interval in \([2,3]\). Any interval is path connected, so each point has arbitrarily small path connected neighbourhoods in the subspace topology. Hence \(X\) is locally path connected.

However, \(X\) is not connected, because
\[
[0,1]
\qquad\text{and}\qquad
[2,3]
\]
are disjoint nonempty open-and-closed subsets in the subspace topology on \(X\), and
\[
X=[0,1]\cup[2,3].
\]

Since path connected spaces are connected, \(X\) cannot be path connected.

Thus \(X\) is an example of a space that is
\[
\text{locally path connected but not connected,}
\]
and therefore also
\[
\text{locally path connected but not path connected.}
\]

```

### Editorial decision
- `ACCEPT <problem_id>`
- `NOT_A_PROBLEM`
- `MISSING_COMPANION_STATEMENT`
- `NO_GOOD_MATCH`
- `NEEDS_MANUAL_REVIEW`

---

## P3 — SOLSEM-AD6A0593A50F
- Review proposal: **CONTENT_MATCH_EDITORIAL_CHECK**
- Prior decision: ``
- Solution source: `Downloads/theory-of-geometry-2.tex` `L220-L331`
- Source problem number: ``
- Refresh top1=0.5202 margin=0.0986

### Solution block
```text
\subsection*{Solution}
\noindent\textbf{(i)}
Let $\alpha:I\to\mathbb{R}^3$ be parametrized by arc length. Set
\[
T(s)=\alpha'(s),\qquad |T(s)|=1.
\]
Then $\alpha''(s)\perp \alpha'(s)$ and the curvature is $k(s)=|\alpha''(s)|\neq 0$.
Define
\[
N(s)=\frac{\alpha''(s)}{k(s)},\qquad 
B(s)=T(s)\times N(s).
\]
Since $|T|=1$ and $T\perp \alpha''$, we have $|T\times \alpha''|=|T|\,|\alpha''|=k$, hence
\[
B=\frac{\alpha'\times \alpha''}{k}.
\]
Differentiate:
\[
B'=\left(\frac{\alpha'\times \alpha''}{k}\right)'
=\frac{(\alpha'\times \alpha'')'}{k}-\frac{k'}{k^2}(\alpha'\times \alpha'').
\]
Now
\[
(\alpha'\times \alpha'')'=\alpha''\times \alpha''+\alpha'\times \alpha'''
=\alpha'\times \alpha''',
\]
so
\[
B'=\frac{\alpha'\times \alpha'''}{k}-\frac{k'}{k^2}(\alpha'\times \alpha'').
\]
By the Frenet--Serret formula $B'=-\tau N$, we have
\[
\tau=-\langle B',N\rangle.
\]
Using $N=\alpha''/k$,
\[
\langle B',N\rangle
=
\left\langle
\frac{\alpha'\times \alpha'''}{k}-\frac{k'}{k^2}(\alpha'\times \alpha''),
\frac{\alpha''}{k}
\right\rangle.
\]
The second term vanishes because $\alpha'\times\alpha''\perp\alpha''$, hence
\[
\langle B',N\rangle=\frac{1}{k^2}\,\langle \alpha'\times \alpha''',\alpha''\rangle.
\]
Using the scalar triple product identities,
\[
\langle \alpha'\times \alpha''',\alpha''\rangle
=\det(\alpha',\alpha''',\alpha'')
=-\det(\alpha',\alpha'',\alpha''')
=-\langle \alpha'\times\alpha'',\alpha'''\rangle,
\]
we obtain
\[
\tau
=-\langle B',N\rangle
=-\frac{1}{k^2}\big(-\langle \alpha'\times\alpha'',\alpha'''\rangle\big)
=
\frac{\langle \alpha'\times\alpha'',\alpha'''\rangle}{k^2}.
\]
Identifying $\alpha'\wedge\alpha''$ with $\alpha'\times\alpha''$ up to the chosen convention,
this is equivalently written as
\[
\tau(s)=-\,\frac{\big\langle \alpha'(s)\wedge \alpha''(s),\,\alpha^{(3)}(s)\big\rangle}{|k(s)|^2},
\]
which matches the stated formula (the overall sign depends only on the orientation convention for $B$
and for the identification $\wedge\leftrightarrow\times$).

\medskip
\noindent\textbf{(ii)}
The fundamental theorem of space curves gives uniqueness up to Euclidean motion only when $k(s)>0$ everywhere.
If $k$ vanishes on an interval, one can ``twist'' a later part of the curve around the straight segment
without changing $k,\tau$ on the curved parts.

Let $\beta:[0,1]\to\mathbb{R}^3$ be a smooth curve which is exactly a straight segment on a middle interval, e.g.
\[
\beta(s)=(s,0,0)\qquad \text{for } s\in[1/3,2/3],
\]
but is not a straight line for $s<1/3$ and for $s>2/3$ (so $k\neq 0$ on those parts).
Let $R_\theta$ be a rotation about the $x$--axis by a fixed angle $\theta\neq 0$, and define
\[
\widetilde\beta(s)=
\begin{cases}
	\beta(s), & 0\le s\le 2/3,\\
	R_\theta(\beta(s)), & 2/3\le s\le 1.
\end{cases}
\]
(Choose $\beta$ to be straight on an open neighborhood of $[1/3,2/3]$ so that all derivatives match at $2/3$;
then $\widetilde\beta$ is smooth.)

On $(2/3,1]$ the map $R_\theta$ is a Euclidean motion, hence it preserves curvature and torsion:
\[
k_{\widetilde\beta}(s)=k_\beta(s),\qquad \tau_{\widetilde\beta}(s)=\tau_\beta(s)
\quad \text{whenever }k_\beta(s)\neq 0.
\]
On $[1/3,2/3]$ we have $k_\beta=0$, so the requirement ``$\tau=\widetilde\tau$ whenever $k\neq 0$''
imposes no condition there.

Moreover, $\beta(s)=\widetilde\beta(s)$ for all $s\in[0,2/3]$.
If a single Euclidean motion $M$ satisfied $M(\beta(s))=\widetilde\beta(s)$ for all $s\in[0,1]$,
then $M$ would fix the non-straight arc $\beta([0,1/3])$ pointwise, forcing $M=\mathrm{Id}$.
But then $\beta=\widetilde\beta$ on $(2/3,1]$, contradicting $\theta\neq 0$.
Hence $\beta$ and $\widetilde\beta$ are not related by a Euclidean motion.

Finally, if one wants unit-speed curves, note that $|\beta'(s)|=|\widetilde\beta'(s)|$ for all $s$
(rotation preserves derivative norms on the rotated part).
Thus the same arc-length reparametrization applied to both produces curves
$\alpha,\widetilde\alpha:[0,1]\to\mathbb{R}^3$ parametrized by arc length with the same properties.


```

### Candidate #1 — IMP-DL-40BD8D3E26-P005 — score 0.5202
- Source: `Downloads/theory-of-geometry-2.tex` `L766-L862`
- Problem number: `2`
- lexical=0.6352 math=0.2992 number=0.0000 family=1.0000
```text
	\subsubsection*{Example 2: Helix (constant curvature and torsion)}
	Let $a>0$ and $b\in\mathbb{R}$ and define
	\[
	\alpha(t)=\big(a\cos t,\;a\sin t,\;bt\big).
	\]
	Compute derivatives:
	\[
	\alpha'(t)=(-a\sin t,\;a\cos t,\;b),\qquad
	\alpha''(t)=(-a\cos t,\;-a\sin t,\;0),\qquad
	\alpha^{(3)}(t)=(a\sin t,\;-a\cos t,\;0).
	\]
	The speed is constant:
	\[
	\|\alpha'(t)\|^2=a^2\sin^2 t+a^2\cos^2 t+b^2=a^2+b^2,
	\qquad
	\|\alpha'(t)\|=\sqrt{a^2+b^2}.
	\]
	
	\medskip
	\noindent\textbf{Cross product.}
	\[
	\alpha'(t)\times\alpha''(t)=
	\begin{vmatrix}
		\mathbf i & \mathbf j & \mathbf k\\
		-a\sin t & a\cos t & b\\
		-a\cos t & -a\sin t & 0
	\end{vmatrix}
	=(ab\sin t,\;-ab\cos t,\;a^2).
	\]
	Hence
	\[
	\|\alpha'(t)\times\alpha''(t)\|^2
	=a^2b^2(\sin^2 t+\cos^2 t)+a^4=a^2b^2+a^4=a^2(a^2+b^2),
	\]
	so
	\[
	\|\alpha'(t)\times\alpha''(t)\|=a\sqrt{a^2+b^2}.
	\]
	
	\medskip
	\noindent\textbf{Curvature.}
	For a general parameter $t$,
	\[
	k(t)=\frac{\|\alpha'(t)\times\alpha''(t)\|}{\|\alpha'(t)\|^3}
	=\frac{a\sqrt{a^2+b^2}}{(\sqrt{a^2+b^2})^3}
	=\frac{a}{a^2+b^2}.
	\]
	
	\medskip
	\noindent\textbf{Torsion.}
	Using
	\[
	\tau(t)=\frac{\det(\alpha'(t),\alpha''(t),\alpha^{(3)}(t))}{\|\alpha'(t)\times\alpha''(t)\|^2}
	=\frac{\langle \alpha'(t)\times\alpha''(t),\alpha^{(3)}(t)\rangle}{\|\alpha'(t)\times\alpha''(t)\|^2},
	\]
	we compute
	\[
	\langle \alpha'(t)\times\alpha''(t),\alpha^{(3)}(t)\rangle
	=
	\langle (ab\sin t,-ab\cos t,a^2),(a\sin t,-a\cos t,0)\rangle
	\]
	\[
	=(ab\sin t)(a\sin t)+(-ab\cos t)(-a\cos t)+a^2\cdot 0
	=a^2b(\sin^2 t+\cos^2 t)=a^2b.
	\]
	Therefore
	\[
	\tau(t)=\frac{a^2b}{a^2(a^2+b^2)}=\frac{b}{a^2+b^2}.
	\]
	Thus a helix has constant curvature $k=\frac{a}{a^2+b^2}$ and constant torsion $\tau=\frac{b}{a^2+b^2}$.
	
	\medskip
	\noindent\textbf{Unit-speed reparametrization (optional).}
	Since $\|\alpha'(t)\|=\sqrt{a^2+b^2}$, arc length satisfies $s=\sqrt{a^2+b^2}\,t$, i.e.
	$t=s/\sqrt{a^2+b^2}$. Substituting yields a unit-speed helix $\alpha(s)$ with the same constants
	$k=\frac{a}{a^2+b^2}$ and $\tau=\frac{b}{a^2+b^2}$.
	
	\medskip
	\noindent\textbf{Wedge/triple-product interpretation (used in the torsion step).}
	In $\mathbb{R}^3$ the exterior product $u\wedge v$ encodes the oriented parallelogram spanned by $u,v$ and satisfies
	\[
	\|u\wedge v\|=\|u\times v\|.
	\]
	Moreover, the pairing with a vector gives the scalar triple product (oriented volume):
	\[
	\langle u\wedge v,\;w\rangle := \det(u,v,w)=\langle u\times v,\;w\rangle.
	\]
	Thus in the torsion formula one may write equivalently
	\[
	\det(\alpha',\alpha'',\alpha^{(3)})=\big\langle \alpha'\wedge \alpha'',\;\alpha^{(3)}\big\rangle,
	\qquad
	\|\alpha'\times\alpha''\|^2=\|\alpha'\wedge\alpha''\|^2.
	\]
	So (up to the chosen sign/orientation convention) the usual determinant formula and the wedge-product formula
	for torsion are the same.
	
	
```

### Candidate #2 — IMP-DL-40BD8D3E26-P004 — score 0.4216
- Source: `Downloads/theory-of-geometry-2.tex` `L716-L765`
- Problem number: `1`
- lexical=0.4875 math=0.2454 number=0.0000 family=1.0000
```text
	\subsubsection*{Example 1: Circle (planar, torsion $=0$)}
	Let $R>0$ and consider the circle parametrized by arc length
	\[
	\alpha(s)=\big(R\cos(s/R),\;R\sin(s/R),\;0\big).
	\]
	Then
	\[
	\alpha'(s)=\left(-\sin(s/R),\;\cos(s/R),\;0\right),
	\qquad
	|\alpha'(s)|^2=\sin^2(s/R)+\cos^2(s/R)=1,
	\]
	so $\alpha$ is unit speed. Next,
	\[
	\alpha''(s)=\left(-\frac{1}{R}\cos(s/R),\;-\frac{1}{R}\sin(s/R),\;0\right),
	\qquad
	\alpha^{(3)}(s)=\left(\frac{1}{R^2}\sin(s/R),\;-\frac{1}{R^2}\cos(s/R),\;0\right).
	\]
	
	\medskip
	\noindent\textbf{Velocity $\perp$ acceleration.}
	\[
	\langle \alpha'(s),\alpha''(s)\rangle
	=
	\left\langle (-\sin,\cos,0),\left(-\frac{1}{R}\cos,-\frac{1}{R}\sin,0\right)\right\rangle
	=
	\frac{1}{R}\sin\cos-\frac{1}{R}\cos\sin=0.
	\]
	
	\medskip
	\noindent\textbf{Curvature.}
	Since $\alpha$ is unit speed, $k(s)=|\alpha''(s)|$:
	\[
	k(s)=\sqrt{\frac{1}{R^2}\cos^2(s/R)+\frac{1}{R^2}\sin^2(s/R)}=\frac{1}{R}.
	\]
	
	\medskip
	\noindent\textbf{Torsion.}
	Using the triple-product formula
	\[
	\tau(s)=\frac{\det(\alpha'(s),\alpha''(s),\alpha^{(3)}(s))}{\|\alpha'(s)\times\alpha''(s)\|^2},
	\]
	note that $\alpha'(s),\alpha''(s),\alpha^{(3)}(s)$ all lie in the plane $z=0$, hence they are coplanar and
	\[
	\det(\alpha'(s),\alpha''(s),\alpha^{(3)}(s))=0,
	\]
	so
	\[
	\tau(s)=0.
	\]
	
```

### Candidate #3 — IMP-DL-40BD8D3E26-P006 — score 0.3743
- Source: `Downloads/theory-of-geometry-2.tex` `L863-L882`
- Problem number: `2`
- lexical=0.3982 math=0.2639 number=0.0000 family=1.0000
```text
	\subsection*{Problem 2}
	Let $\alpha:I\to\mathbb{R}^3$ be a curve parametrized by arc length with $\tau(s)\neq 0$ and $\dot{k}(s)\neq 0$
	for all $s\in I$. Show that a necessary and sufficient condition for $\alpha(I)$ to lie on a sphere is that
	\[
	R^2 + (R')^2 T^2
	\quad\text{is constant,}
	\]
	where $R=1/k$ and $T=1/\tau$.
	
	\subsection*{Theory (for Problems 2--3)}
	Assume $\alpha$ is unit speed, so $T=\alpha'$ and $|T|=1$. If $k(s)\neq 0$, define
	\[
	k(s)=|\alpha''(s)|,\qquad N(s)=\frac{\alpha''(s)}{k(s)},\qquad B(s)=T(s)\times N(s).
	\]
	The Frenet--Serret formulas are
	\[
	T'=kN,\qquad N'=-kT+\tau B,\qquad B'=-\tau N.
	\]
	In particular, if $R=1/k$, then $k=1/R$.
	
```

### Candidate #4 — IMP-DL-40BD8D3E26-P002 — score 0.3478
- Source: `Downloads/theory-of-geometry-2.tex` `L184-L190`
- Problem number: ``
- lexical=0.3834 math=0.1893 number=0.0000 family=1.0000
```text
		\item Let $\alpha:I\to\mathbb{R}^3$ be a curve parametrized by arc length with curvature $k(s)\neq 0$ for all $s\in I$.
		Show that the torsion $\tau$ of $\alpha$ is given by
		\[
		\tau(s)=-\,\frac{\big\langle \alpha'(s)\wedge \alpha''(s),\,\alpha^{(3)}(s)\big\rangle}{|k(s)|^2},
		\]
		where $\alpha^{(3)}$ denotes the third derivative with respect to $s$.
		
```

### Candidate #5 — IMP-DL-E88547CF67-P013 — score 0.2881
- Source: `Downloads/theory-of-geometry-3.tex` `L950-L1070`
- Problem number: `12`
- lexical=0.3750 math=0.2943 number=0.0000 family=0.0000
```text
	\subsection*{Problem 12 — Gauss curvature via the map $fN$; curvature of an ellipsoid}
	
	\textbf{Problem.}
	Let $S\subset\mathbb R^3$ be an oriented smooth surface with Gauss map (unit normal) $N$.
	Let $V\subset S$ be open and let $f:V\to\mathbb R$ be smooth and nowhere zero.
	Let $v_1,v_2$ be smooth tangent vector fields on $V$ such that at each point they are orthonormal and oriented,
	i.e.\ $v_1\wedge v_2=N$ (equivalently $v_1\times v_2=N$).
	
	\begin{enumerate}
		\item Prove that the Gaussian curvature $K$ on $V$ is
		\[
		K \;=\; \frac{\big\langle D(fN)(v_1)\wedge D(fN)(v_2),\, fN\big\rangle}{f^3}.
		\]
		\item Let $f$ be the restriction to the ellipsoid
		\[
		E:\qquad \frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1
		\]
		of the function
		\[
		f(x,y,z)=\sqrt{\frac{x^2}{a^4}+\frac{y^2}{b^4}+\frac{z^2}{c^4}}.
		\]
		Show that the Gaussian curvature of $E$ is
		\[
		K=\frac{1}{a^2b^2c^2\, f^4}.
		\]
	\end{enumerate}
	
	\medskip
	\textbf{Theory.}
	For an oriented orthonormal basis $(v_1,v_2)$ of $T_pS$,
	\[
	K(p)=\det(S_p)=\big\langle dN_p(v_1)\times dN_p(v_2),\,N(p)\big\rangle,
	\]
	because $S=-dN$ and $\det(-S)=\det(S)$. Also $\langle N\times X,\,N\rangle=0$ for all $X$.
	
	\medskip
	\textbf{Solution.}
	
	\textbf{(i)} Set $F=fN:V\to\mathbb R^3$. For any $v\in T_pS$,
	\[
	dF_p(v)=v(f)\,N(p)+f(p)\,dN_p(v).
	\]
	Hence
	\[
	dF(v_1)\times dF(v_2)
	=
	\big(v_1(f)N+f\,dN(v_1)\big)\times\big(v_2(f)N+f\,dN(v_2)\big)
	\]
	\[
	= f^2\,dN(v_1)\times dN(v_2)
	+ f\,v_1(f)\,N\times dN(v_2)
	+ f\,v_2(f)\,dN(v_1)\times N.
	\]
	Taking the dot product with $fN$ kills the mixed terms since
	$\langle N\times dN(v_2),N\rangle=0$ and $\langle dN(v_1)\times N,N\rangle=0$.
	Thus
	\[
	\big\langle dF(v_1)\times dF(v_2),\,fN\big\rangle
	=
	f^3\,\big\langle dN(v_1)\times dN(v_2),\,N\big\rangle.
	\]
	But for an oriented orthonormal pair $(v_1,v_2)$, the Gauss curvature is
	\[
	K=\big\langle dN(v_1)\times dN(v_2),\,N\big\rangle.
	\]
	Therefore
	\[
	K=\frac{\big\langle dF(v_1)\times dF(v_2),\,fN\big\rangle}{f^3}
	=
	\frac{\big\langle D(fN)(v_1)\wedge D(fN)(v_2),\,fN\big\rangle}{f^3}.
	\]
	
	\medskip
	\textbf{(ii)} Let $\Phi(x,y,z)=\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}$, so $E=\{\Phi=1\}$ and
	\[
	\nabla\Phi=\left(\frac{2x}{a^2},\frac{2y}{b^2},\frac{2z}{c^2}\right),\qquad
	\|\nabla\Phi\|=2\sqrt{\frac{x^2}{a^4}+\frac{y^2}{b^4}+\frac{z^2}{c^4}}=2f.
	\]
	Hence the unit normal is
	\[
	N=\frac{\nabla\Phi}{\|\nabla\Phi\|}=\frac1f\left(\frac{x}{a^2},\frac{y}{b^2},\frac{z}{c^2}\right),
	\quad\text{so}\quad
	fN=\left(\frac{x}{a^2},\frac{y}{b^2},\frac{z}{c^2}\right).
	\]
	Write $A=\mathrm{diag}\!\left(\frac1{a^2},\frac1{b^2},\frac1{c^2}\right)$. Then $fN=Ax$ and thus
	\[
	D(fN)(v)=Av.
	\]
	Applying (i),
	\[
	K=\frac{\langle (Av_1)\times(Av_2),\,fN\rangle}{f^3}.
	\]
	Use the identity $(Au)\times(Av)=\det(A)\,A^{-T}(u\times v)$. Since $A$ is diagonal, $A^{-T}=A^{-1}$, and
	$v_1\times v_2=N$, we obtain
	\[
	(Av_1)\times(Av_2)=\det(A)\,A^{-1}N.
	\]
	Therefore
	\[
	\langle (Av_1)\times(Av_2),\,fN\rangle
	=\det(A)\,\langle A^{-1}N,\,fN\rangle.
	\]
	But $N=\frac1f Ax$, hence $A^{-1}N=\frac1f x$, and $fN=Ax$, so
	\[
	\langle A^{-1}N,\,fN\rangle
	=\left\langle \frac1f x,\,Ax\right\rangle
	=\frac1f\left(\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}\right)
	=\frac1f
	\]
	on $E$. Also $\det(A)=\frac1{a^2b^2c^2}$. Hence
	\[
	\langle (Av_1)\times(Av_2),\,fN\rangle=\frac{1}{a^2b^2c^2\,f},
	\qquad
	K=\frac{1}{a^2b^2c^2\,f^4}.
	\]
	
	\medskip
	\textbf{Example (sphere check).}
	If $a=b=c=R$, then $f=1/R$ on $E$, so $K=\frac{1}{R^6(1/R^4)}=\frac1{R^2}$.
	
	
```

### Editorial decision
- `ACCEPT <problem_id>`
- `NOT_A_PROBLEM`
- `MISSING_COMPANION_STATEMENT`
- `NO_GOOD_MATCH`
- `NEEDS_MANUAL_REVIEW`

---

