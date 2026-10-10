# GA-03f.3 — Imported-source comparison review

Evidence only. Similarity is not provenance. Inspect actual statements before editing mapping statuses.

- Candidate rows: 90
- Companion IDs: 18

## CP-V-0018

### Rank 1 — SEM-E58E8AA38E90 (0.4880)
- Evidence: **UNVERIFIED**; identical math spans: 1
- Source: `Downloads/theory-of-commutative-algebra-1.tex:541-578`
- Source excerpt: `\section*{Problem 4 — Tensor products of \(k\)-algebras} \textbf{Exact statement.} Calculate the following tensor products of rings, where \(k\) is a field: \begin{enumerate} \item[(a)] \(k \otimes_{k[x,y]} k[u,v]\), where \(k[x,y]\to k\) is \(x,y\mapsto 0\), and \(k[x,y]\to k[u,v]\) is \(x\mapsto u\), \(y\mapsto uv\), both the identity on \(k\). \item[(b)] \(k[v]\otimes_{k[x]} k[v]\), where both maps \(k[x]\to k[v]\) send \(x\mapsto v^2\) and are the identity on \(k\). \end{enumerate} \textbf{Solution.} \textbf{(a)} Since \(k\cong k[x,y]/(x,y)\), we use base change: \[ k\otimes_{k[x,y]} k[u,v]\ \cong\ (k[x,y]/(x,y))\otimes_{k[x,y]} k[u,v] \ \cong\ k[u,v]/(x,y)\,k[u,v]. \] Here \((x,y)\) acts on \(k[u,v]\) by \(x\mapsto u\), \(y\mapsto uv\), so \[ (x,y)\,k[u,v]=(u,uv)=(u), \] hence \[ k\ot ...`
- Companion excerpt: `\label{prob:cp-v-0018} Let \(k\) be a field. \textbf{(a)} Compute \[ k\otimes_{k[x,y]}k[u,v], \] where \(k[x,y]\to k\) sends \(x,y\mapsto0\), while \(k[x,y]\to k[u,v]\) sends \[ x\mapsto u,\qquad y\mapsto uv. \] \textbf{(b)} Compute \[ k[v]\otimes_{k[x]}k[v], \] where both copies are \(k[x]\)-algebras via \(x\mapsto v^2\). Describe separately the cases \(\operatorname{char}k\ne2\) and \(\operatorname{char}k=2\).`

### Rank 2 — SEM-7EA1EEB82A49 (0.4050)
- Evidence: **UNVERIFIED**; identical math spans: 3
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2103-2161`
- Source excerpt: `\subsection{Example (a)} Compute \[ k\otimes_{k[x,y]} k[u,v], \] where \(k[x,y]\to k\) sends \(x,y\mapsto 0\), and \(k[x,y]\to k[u,v]\) sends \[ x\mapsto u,\qquad y\mapsto uv. \] \subsubsection*{Step 1: rewrite \(k\) as a quotient} Since \[ k\cong k[x,y]/(x,y), \] we have \[ k\otimes_{k[x,y]} k[u,v] \cong \big(k[x,y]/(x,y)\big)\otimes_{k[x,y]} k[u,v]. \] By base change, \[ \big(k[x,y]/(x,y)\big)\otimes_{k[x,y]} k[u,v] \cong k[u,v]/(x,y)k[u,v]. \] \subsubsection*{Step 2: compute the extended ideal} The ideal \((x,y)\) acts on \(k[u,v]\) via \[ x\mapsto u,\qquad y\mapsto uv. \] Hence \[ (x,y)k[u,v]=(u,uv). \] But \[ (u,uv)=(u), \] since \(uv\) is already a multiple of \(u\). Therefore \[ k\otimes_{k[x,y]} k[u,v]\cong k[u,v]/(u)\cong k[v]. \] So the result is \[ \boxed{ k\otimes_{k[x,y]} k[u, ...`
- Companion excerpt: `\label{prob:cp-v-0018} Let \(k\) be a field. \textbf{(a)} Compute \[ k\otimes_{k[x,y]}k[u,v], \] where \(k[x,y]\to k\) sends \(x,y\mapsto0\), while \(k[x,y]\to k[u,v]\) sends \[ x\mapsto u,\qquad y\mapsto uv. \] \textbf{(b)} Compute \[ k[v]\otimes_{k[x]}k[v], \] where both copies are \(k[x]\)-algebras via \(x\mapsto v^2\). Describe separately the cases \(\operatorname{char}k\ne2\) and \(\operatorname{char}k=2\).`

### Rank 3 — SEM-770D84002162 (0.3721)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-15.tex:696-696`
- Source excerpt: `\item The map \(A^2 \to A\) sends \((a,b)\mapsto ax+by\).`
- Companion excerpt: `\label{prob:cp-v-0018} Let \(k\) be a field. \textbf{(a)} Compute \[ k\otimes_{k[x,y]}k[u,v], \] where \(k[x,y]\to k\) sends \(x,y\mapsto0\), while \(k[x,y]\to k[u,v]\) sends \[ x\mapsto u,\qquad y\mapsto uv. \] \textbf{(b)} Compute \[ k[v]\otimes_{k[x]}k[v], \] where both copies are \(k[x]\)-algebras via \(x\mapsto v^2\). Describe separately the cases \(\operatorname{char}k\ne2\) and \(\operatorname{char}k=2\).`

### Rank 4 — SEM-3551086F7AB3 (0.3115)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2511-2516`
- Source excerpt: `\subsubsection*{Example 8} View \(k\) as a \(k[x]\)-module via \(x\mapsto 0\). Then \[ k\otimes_{k[x]} k[x]\cong k. \]`
- Companion excerpt: `\label{prob:cp-v-0018} Let \(k\) be a field. \textbf{(a)} Compute \[ k\otimes_{k[x,y]}k[u,v], \] where \(k[x,y]\to k\) sends \(x,y\mapsto0\), while \(k[x,y]\to k[u,v]\) sends \[ x\mapsto u,\qquad y\mapsto uv. \] \textbf{(b)} Compute \[ k[v]\otimes_{k[x]}k[v], \] where both copies are \(k[x]\)-algebras via \(x\mapsto v^2\). Describe separately the cases \(\operatorname{char}k\ne2\) and \(\operatorname{char}k=2\).`

### Rank 5 — SEM-23B73A43B163 (0.2680)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-15.tex:697-702`
- Source excerpt: `\item The map \(A \to A^2\) sends \(c\mapsto (-cy,cx)\). \end{itemize} \textbf{Interpretation.} This says: \begin{itemize}`
- Companion excerpt: `\label{prob:cp-v-0018} Let \(k\) be a field. \textbf{(a)} Compute \[ k\otimes_{k[x,y]}k[u,v], \] where \(k[x,y]\to k\) sends \(x,y\mapsto0\), while \(k[x,y]\to k[u,v]\) sends \[ x\mapsto u,\qquad y\mapsto uv. \] \textbf{(b)} Compute \[ k[v]\otimes_{k[x]}k[v], \] where both copies are \(k[x]\)-algebras via \(x\mapsto v^2\). Describe separately the cases \(\operatorname{char}k\ne2\) and \(\operatorname{char}k=2\).`

## CP-V-0019

### Rank 1 — SEM-A25A89BD404F (0.5002)
- Evidence: **UNVERIFIED**; identical math spans: 1
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2719-2732`
- Source excerpt: `\subsubsection*{Example 3: polynomial rings} As an \(A\)-module, \[ A[x]\cong \bigoplus_{n\ge 0} A\cdot x^n. \] So \(A[x]\) is free over \(A\), hence flat. More generally, \[ A[x_1,\dots,x_n] \] is flat over \(A\).`
- Companion excerpt: `\label{prob:cp-v-0019} Let \(A\) be a ring. \textbf{(a)} Prove that \(A[x]\) is a free \(A\)-module. \textbf{(b)} Deduce that \(A[x]\) is flat over \(A\). \textbf{(c)} More generally, prove that \[ A[x_1,\dots,x_n] \] is flat over \(A\). \textbf{(d)} Explain why this gives an elementary example of a faithfully flat extension \(A\to A[x]\).`

### Rank 2 — SEM-8BA7C831CDD6 (0.3473)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-1.tex:579-590`
- Source excerpt: `\section*{Problem 5 — \(A[x]\) is flat over \(A\)} \textbf{Exact statement.} Let \(A[x]\) denote the polynomial ring in one variable over a ring \(A\). Show that \(A[x]\) is a flat \(A\)-module. \textbf{Solution.} As an \(A\)-module, \[ A[x]\cong \bigoplus_{n\ge 0} A\cdot x^n, \] so \(A[x]\) is free with basis \(\{1,x,x^2,\dots\}\). Every free module is flat. Hence \(A[x]\) is flat over \(A\).`
- Companion excerpt: `\label{prob:cp-v-0019} Let \(A\) be a ring. \textbf{(a)} Prove that \(A[x]\) is a free \(A\)-module. \textbf{(b)} Deduce that \(A[x]\) is flat over \(A\). \textbf{(c)} More generally, prove that \[ A[x_1,\dots,x_n] \] is flat over \(A\). \textbf{(d)} Explain why this gives an elementary example of a faithfully flat extension \(A\to A[x]\).`

### Rank 3 — SEM-D9A0367D0C90 (0.3106)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-14.tex:1180-1187`
- Source excerpt: `\paragraph{Example 11: \(\mathbb Q\) is flat over \(\mathbb Z\).} Since \[ \mathbb Q = \mathbb Z_{(0)} \] is the localization of \(\mathbb Z\) at all nonzero integers, it is flat over \(\mathbb Z\).`
- Companion excerpt: `\label{prob:cp-v-0019} Let \(A\) be a ring. \textbf{(a)} Prove that \(A[x]\) is a free \(A\)-module. \textbf{(b)} Deduce that \(A[x]\) is flat over \(A\). \textbf{(c)} More generally, prove that \[ A[x_1,\dots,x_n] \] is flat over \(A\). \textbf{(d)} Explain why this gives an elementary example of a faithfully flat extension \(A\to A[x]\).`

### Rank 4 — SEM-3AAA71F6F743 (0.2972)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-14.tex:1155-1179`
- Source excerpt: `\paragraph{Example 10: localizations are flat.} For every multiplicative set \(S\subseteq A\), the localization \[ S^{-1}A \] is flat over \(A\). In particular, for every prime ideal \(\mathfrak p\), \[ A_{\mathfrak p} \] is flat over \(A\). Examples: \[ \mathbb Z_{(p)} \text{ is flat over } \mathbb Z, \] \[ k[x]_{(x)} \text{ is flat over } k[x], \] \[ k[x,y]_{(x,y)} \text{ is flat over } k[x,y]. \]`
- Companion excerpt: `\label{prob:cp-v-0019} Let \(A\) be a ring. \textbf{(a)} Prove that \(A[x]\) is a free \(A\)-module. \textbf{(b)} Deduce that \(A[x]\) is flat over \(A\). \textbf{(c)} More generally, prove that \[ A[x_1,\dots,x_n] \] is flat over \(A\). \textbf{(d)} Explain why this gives an elementary example of a faithfully flat extension \(A\to A[x]\).`

### Rank 5 — SEM-1F745EB961B5 (0.2892)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2749-2752`
- Source excerpt: `\subsubsection*{Example 5: direct sums} A direct sum of flat modules is flat.`
- Companion excerpt: `\label{prob:cp-v-0019} Let \(A\) be a ring. \textbf{(a)} Prove that \(A[x]\) is a free \(A\)-module. \textbf{(b)} Deduce that \(A[x]\) is flat over \(A\). \textbf{(c)} More generally, prove that \[ A[x_1,\dots,x_n] \] is flat over \(A\). \textbf{(d)} Explain why this gives an elementary example of a faithfully flat extension \(A\to A[x]\).`

## CP-V-0020

### Rank 1 — SEM-EF3E51780266 (0.3230)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:918-941`
- Source excerpt: `\subsubsection*{Example 2: failure when ideals are not comaximal} Let \[ A=\mathbb Z,\qquad I=(4),\qquad J=(6). \] Then \[ (4)+(6)=(2)\neq \mathbb Z. \] Also \[ (4)\cap(6)=(12),\qquad (4)(6)=(24). \] So \[ (4)\cap(6)\neq (4)(6). \] The map \[ \mathbb Z/(24)\to \mathbb Z/(4)\times \mathbb Z/(6) \] is neither injective nor surjective.`
- Companion excerpt: `\label{prob:cp-v-0020} Let \[ A=A_1\times A_2, \qquad M_1=A_1\times0, \qquad M_2=0\times A_2, \] where \(A_1,A_2\ne0\). \textbf{(a)} Prove that \(M_1\) and \(M_2\) are projective \(A\)-modules. \textbf{(b)} Show that neither \(M_1\) nor \(M_2\) is free. \textbf{(c)} Interpret the decomposition using the idempotents \[ e_1=(1,0),\qquad e_2=(0,1). \]`

### Rank 2 — SEM-FB51E69ADF03 (0.2866)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-8.tex:3380-3392`
- Source excerpt: `\textbf{Problem.} Let \[ A=A_1\times A_2 \] be a direct product ring. Show that the \(A\)-modules \[ M_1=A_1\times 0, \qquad M_2=0\times A_2 \] are projective. If \(A_1\neq 0\) and \(A_2\neq 0\), then they are not free. This gives a basic example showing that projective modules need not be free.`
- Companion excerpt: `\label{prob:cp-v-0020} Let \[ A=A_1\times A_2, \qquad M_1=A_1\times0, \qquad M_2=0\times A_2, \] where \(A_1,A_2\ne0\). \textbf{(a)} Prove that \(M_1\) and \(M_2\) are projective \(A\)-modules. \textbf{(b)} Show that neither \(M_1\) nor \(M_2\) is free. \textbf{(c)} Interpret the decomposition using the idempotents \[ e_1=(1,0),\qquad e_2=(0,1). \]`

### Rank 3 — SEM-4D918DAEC3A7 (0.2822)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:1074-1084`
- Source excerpt: `\subsubsection*{Example 9: over \((\mathbb Z/p\mathbb Z)[x]\)} Let \[ A=(\mathbb Z/p\mathbb Z)[x]. \] Then \[ A/(x(x-1))\cong A/(x)\times A/(x-1)\cong \mathbb Z/p\mathbb Z\times \mathbb Z/p\mathbb Z. \]`
- Companion excerpt: `\label{prob:cp-v-0020} Let \[ A=A_1\times A_2, \qquad M_1=A_1\times0, \qquad M_2=0\times A_2, \] where \(A_1,A_2\ne0\). \textbf{(a)} Prove that \(M_1\) and \(M_2\) are projective \(A\)-modules. \textbf{(b)} Show that neither \(M_1\) nor \(M_2\) is free. \textbf{(c)} Interpret the decomposition using the idempotents \[ e_1=(1,0),\qquad e_2=(0,1). \]`

### Rank 4 — SEM-1B1A4B26FA6B (0.2273)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:999-1021`
- Source excerpt: `\subsubsection*{Example 5: two points} Let \[ A=k[x],\qquad I=(x),\qquad J=(x-1). \] Then \[ x-(x-1)=1, \] so \(I+J=A\). Hence \[ I\cap J=IJ=(x(x-1)), \] and \[ k[x]/(x(x-1))\cong k[x]/(x)\times k[x]/(x-1)\cong k\times k. \] The map is \[ f(x)\mapsto (f(0),f(1)). \]`
- Companion excerpt: `\label{prob:cp-v-0020} Let \[ A=A_1\times A_2, \qquad M_1=A_1\times0, \qquad M_2=0\times A_2, \] where \(A_1,A_2\ne0\). \textbf{(a)} Prove that \(M_1\) and \(M_2\) are projective \(A\)-modules. \textbf{(b)} Show that neither \(M_1\) nor \(M_2\) is free. \textbf{(c)} Interpret the decomposition using the idempotents \[ e_1=(1,0),\qquad e_2=(0,1). \]`

### Rank 5 — SEM-4652ACCE8F76 (0.2174)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-6.tex:792-823`
- Source excerpt: `\subsubsection{Example: \(A=k[x,y]/(xy)\)} Here \(I=(xy)\). Then: \[ \bar x=x+(xy),\qquad \bar y=y+(xy). \] Also \[ \overline{x+xy}=\bar x \] because \[ (x+xy)-x=xy\in(xy). \] Moreover, \[ \overline{xy}=0,\qquad \overline{x^2y}=0, \] since \(xy,x^2y\in(xy)\). However, \[ \bar x\neq 0,\qquad \bar y\neq 0, \] because \(x,y\notin(xy)\). Thus in this quotient ring, \[ \bar x\bar y=0 \] while neither \(\bar x\) nor \(\bar y\) is zero.`
- Companion excerpt: `\label{prob:cp-v-0020} Let \[ A=A_1\times A_2, \qquad M_1=A_1\times0, \qquad M_2=0\times A_2, \] where \(A_1,A_2\ne0\). \textbf{(a)} Prove that \(M_1\) and \(M_2\) are projective \(A\)-modules. \textbf{(b)} Show that neither \(M_1\) nor \(M_2\) is free. \textbf{(c)} Interpret the decomposition using the idempotents \[ e_1=(1,0),\qquad e_2=(0,1). \]`

## CP-V-0021

### Rank 1 — SEM-A10AE7B0559C (0.5026)
- Evidence: **UNVERIFIED**; identical math spans: 1
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:2657-2797`
- Source excerpt: `\section{Problem 14(a) --- Characterization of minimal homomorphisms over a local ring} \textbf{Exact statement.} Let \((A,\mathfrak m)\) be a local ring, let \(k=A/\mathfrak m\), and let \[ f:M\to N \] be an \(A\)-module homomorphism between finitely generated modules. We say that \(f\) is \emph{minimal} if the induced map \[ f\otimes \mathrm{id}_k:\ M\otimes_A k \to N\otimes_A k \] is an isomorphism. Show that \(f\) is minimal if and only if \(f\) is surjective and \[ \ker f\subseteq \mathfrak m M. \] \textbf{Solution.} For any \(A\)-module \(L\), there is a natural isomorphism \[ L\otimes_A k \cong L/\mathfrak m L. \] Hence the map \[ f\otimes k:\ M\otimes_A k \to N\otimes_A k \] identifies with the induced map \[ \bar f:\ M/\mathfrak m M \to N/\mathfrak m N. \] Thus \(f\) is minimal if ...`
- Companion excerpt: `\label{prob:cp-v-0021} Let \((A,\mathfrak m)\) be a local ring, let \[ k=A/\mathfrak m, \] and let \(M\) be a finitely generated \(A\)-module. \textbf{(a)} Let \(f:F\to M\) be a homomorphism with \(F\) finitely generated and free. Prove that the following are equivalent: \[ f\otimes_A k:F\otimes_A k\longrightarrow M\otimes_A k \] is an isomorphism, and \[ f\text{ is surjective with }\ker f\subseteq\mathfrak m F. \] \textbf{(b)} Prove that there exists such a map \(f:F\to M\). \textbf{(c)} Show that the rank of \(F\) in any such minimal free cover is \[ \dim_k(M/\mathfrak mM). \]`

### Rank 2 — SEM-03576857677B (0.4154)
- Evidence: **UNVERIFIED**; identical math spans: 1
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:3819-3877`
- Source excerpt: `\item conclude that depth equals dimension. \end{itemize} This is one of the most concrete ways to prove Cohen--Macaulayness. \bigskip \section{4. Problem 14 theory: minimal maps over local rings} \subsection*{4.1. Why local rings simplify module theory} Over a local ring \((A,\mathfrak m)\), the quotient \[ M/\mathfrak m M \] is a vector space over \[ k=A/\mathfrak m. \] This quotient measures the minimal number of generators of \(M\). Indeed, by Nakayama's lemma, a set of elements generates \(M\) if and only if their images generate \(M/\mathfrak mM\). So studying a module modulo \(\mathfrak m\) is extremely powerful. \subsection*{4.2. Minimal homomorphisms} A homomorphism \[ f:M\to N \] between finitely generated \(A\)-modules is called \emph{minimal} if \[ f\otimes_A k: M\otimes_A k \t ...`
- Companion excerpt: `\label{prob:cp-v-0021} Let \((A,\mathfrak m)\) be a local ring, let \[ k=A/\mathfrak m, \] and let \(M\) be a finitely generated \(A\)-module. \textbf{(a)} Let \(f:F\to M\) be a homomorphism with \(F\) finitely generated and free. Prove that the following are equivalent: \[ f\otimes_A k:F\otimes_A k\longrightarrow M\otimes_A k \] is an isomorphism, and \[ f\text{ is surjective with }\ker f\subseteq\mathfrak m F. \] \textbf{(b)} Prove that there exists such a map \(f:F\to M\). \textbf{(c)} Show that the rank of \(F\) in any such minimal free cover is \[ \dim_k(M/\mathfrak mM). \]`

### Rank 3 — SEM-9A2BF2C983F4 (0.3866)
- Evidence: **UNVERIFIED**; identical math spans: 1
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:2798-2986`
- Source excerpt: `\section{Problem 14(b) --- Existence of a minimal map from a free module} \textbf{Exact statement.} Let \((A,\mathfrak m)\) be a local ring, let \(k=A/\mathfrak m\), and let \(M\) be a finitely generated \(A\)-module. Show that there exists a minimal homomorphism \[ f:F\to M \] with \(F\) free. \textbf{Solution.} We want to construct a free \(A\)-module \(F\) and an \(A\)-linear map \[ f:F\to M \] such that \[ f\otimes_A k:\ F\otimes_A k \to M\otimes_A k \] is an isomorphism. Since \[ M\otimes_A k \cong M/\mathfrak m M, \qquad F\otimes_A k \cong F/\mathfrak m F, \] it is enough to construct \(f\) so that the induced map \[ \bar f:\ F/\mathfrak m F \to M/\mathfrak m M \] is an isomorphism. Because \(M\) is finitely generated over \(A\), the quotient \[ M/\mathfrak m M \] is a finite-dimensi ...`
- Companion excerpt: `\label{prob:cp-v-0021} Let \((A,\mathfrak m)\) be a local ring, let \[ k=A/\mathfrak m, \] and let \(M\) be a finitely generated \(A\)-module. \textbf{(a)} Let \(f:F\to M\) be a homomorphism with \(F\) finitely generated and free. Prove that the following are equivalent: \[ f\otimes_A k:F\otimes_A k\longrightarrow M\otimes_A k \] is an isomorphism, and \[ f\text{ is surjective with }\ker f\subseteq\mathfrak m F. \] \textbf{(b)} Prove that there exists such a map \(f:F\to M\). \textbf{(c)} Show that the rank of \(F\) in any such minimal free cover is \[ \dim_k(M/\mathfrak mM). \]`

### Rank 4 — SEM-4EAAC68D5F21 (0.3768)
- Evidence: **UNVERIFIED**; identical math spans: 2
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:2987-3247`
- Source excerpt: `\section{Problem 15 --- Existence of minimal free resolutions over a Noetherian local ring} \textbf{Exact statement.} Let \((A,\mathfrak m)\) be a local ring, \(k=A/\mathfrak m\), and let \[ F^\bullet \to M \to 0 \] be a free resolution of a finitely generated \(A\)-module \(M\) by finitely generated free modules, with maps \[ f_i:F_{i+1}\to F_i. \] We say this free resolution is \emph{minimal} if all the maps \[ f_i\otimes \mathrm{id}_k:\ F_{i+1}\otimes_A k \to F_i\otimes_A k \] are zero. Show that if \(A\) is Noetherian, then minimal resolutions exist. \textbf{Solution.} We construct a minimal free resolution inductively, using Problem 14(b). \medskip Since \(M\) is finitely generated, Problem 14(b) gives a minimal homomorphism \[ \varepsilon_0:F_0\to M \] with \(F_0\) finitely generated ...`
- Companion excerpt: `\label{prob:cp-v-0021} Let \((A,\mathfrak m)\) be a local ring, let \[ k=A/\mathfrak m, \] and let \(M\) be a finitely generated \(A\)-module. \textbf{(a)} Let \(f:F\to M\) be a homomorphism with \(F\) finitely generated and free. Prove that the following are equivalent: \[ f\otimes_A k:F\otimes_A k\longrightarrow M\otimes_A k \] is an isomorphism, and \[ f\text{ is surjective with }\ker f\subseteq\mathfrak m F. \] \textbf{(b)} Prove that there exists such a map \(f:F\to M\). \textbf{(c)} Show that the rank of \(F\) in any such minimal free cover is \[ \dim_k(M/\mathfrak mM). \]`

### Rank 5 — SEM-73254E812808 (0.3271)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-1.tex:3362-3520`
- Source excerpt: `\section*{Problem 3 --- Basic properties of support} \textbf{Exact statement.} Show the following statements about the support of an \(A\)-module: \begin{enumerate}[label=(\alph*)] \item If \(0\to M_1\to M_2\to M_3\to 0\) is exact, then \[ \operatorname{Supp}(M_2)=\operatorname{Supp}(M_1)\cup \operatorname{Supp}(M_3). \] \item If \(M=\sum_i M_i\) for submodules \(M_i\subseteq M\), then \[ \operatorname{Supp}(M)=\bigcup_i \operatorname{Supp}(M_i). \] \item For \(\mathfrak p\subseteq A\) a prime ideal, write \[ k(\mathfrak p):=A_{\mathfrak p}/\mathfrak p A_{\mathfrak p}. \] If \(M\) is finitely generated, show that \[ \mathfrak p\in \operatorname{Supp}(M)\iff M\otimes_A k(\mathfrak p)\neq 0. \] \item If \(M,N\) are finitely generated \(A\)-modules, then \[ \operatorname{Supp}(M\otimes_A N)=\ ...`
- Companion excerpt: `\label{prob:cp-v-0021} Let \((A,\mathfrak m)\) be a local ring, let \[ k=A/\mathfrak m, \] and let \(M\) be a finitely generated \(A\)-module. \textbf{(a)} Let \(f:F\to M\) be a homomorphism with \(F\) finitely generated and free. Prove that the following are equivalent: \[ f\otimes_A k:F\otimes_A k\longrightarrow M\otimes_A k \] is an isomorphism, and \[ f\text{ is surjective with }\ker f\subseteq\mathfrak m F. \] \textbf{(b)} Prove that there exists such a map \(f:F\to M\). \textbf{(c)} Show that the rank of \(F\) in any such minimal free cover is \[ \dim_k(M/\mathfrak mM). \]`

## CP-V-0022

### Rank 1 — SEM-D2A0B35D4E15 (0.2390)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2517-2525`
- Source excerpt: `\subsubsection*{Example 9} \[ k\otimes_{k[x]} k[x]/(x^2) \cong k[x]/(x)\otimes_{k[x]} k[x]/(x^2) \cong k[x]/(x,x^2)\cong k. \]`
- Companion excerpt: `\label{prob:cp-v-0022} Let \(A\) be a ring, let \(I\subseteq A\) be an ideal, and let \(M\) be an \(A\)-module. Prove that there is a natural isomorphism \[ (A/I)\otimes_A M \cong M/IM. \] Describe explicitly the mutually inverse maps.`

### Rank 2 — SEM-A10AE7B0559C (0.2257)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:2657-2797`
- Source excerpt: `\section{Problem 14(a) --- Characterization of minimal homomorphisms over a local ring} \textbf{Exact statement.} Let \((A,\mathfrak m)\) be a local ring, let \(k=A/\mathfrak m\), and let \[ f:M\to N \] be an \(A\)-module homomorphism between finitely generated modules. We say that \(f\) is \emph{minimal} if the induced map \[ f\otimes \mathrm{id}_k:\ M\otimes_A k \to N\otimes_A k \] is an isomorphism. Show that \(f\) is minimal if and only if \(f\) is surjective and \[ \ker f\subseteq \mathfrak m M. \] \textbf{Solution.} For any \(A\)-module \(L\), there is a natural isomorphism \[ L\otimes_A k \cong L/\mathfrak m L. \] Hence the map \[ f\otimes k:\ M\otimes_A k \to N\otimes_A k \] identifies with the induced map \[ \bar f:\ M/\mathfrak m M \to N/\mathfrak m N. \] Thus \(f\) is minimal if ...`
- Companion excerpt: `\label{prob:cp-v-0022} Let \(A\) be a ring, let \(I\subseteq A\) be an ideal, and let \(M\) be an \(A\)-module. Prove that there is a natural isomorphism \[ (A/I)\otimes_A M \cong M/IM. \] Describe explicitly the mutually inverse maps.`

### Rank 3 — SEM-46BDD23BA0F7 (0.1914)
- Evidence: **UNVERIFIED**; identical math spans: 1
- Source: `Downloads/theory-of-commutative-algebra-1.tex:406-540`
- Source excerpt: `\section*{Problem 2 — Tensoring with \(A/I\) kills \(IM\)} \textbf{Exact statement.} Let \(A\) be a ring, \(I\subseteq A\) an ideal, and \(M\) an \(A\)-module. Show that \[ (A/I)\otimes_A M \cong M/IM. \] \textbf{Solution.} Define \(\Psi:(A/I)\otimes_A M\to M/IM\) on pure tensors by \[ \Psi(\overline{a}\otimes m)=am+IM. \] This is well-defined: if \(a-a'\in I\), then \((a-a')m\in IM\), so \(am+IM=a'm+IM\). It is \(A\)-balanced, hence induces an \(A\)-module homomorphism. It is surjective since \(\Psi(\overline{1}\otimes m)=m+IM\). Define \(\Theta:M\to (A/I)\otimes_A M\) by \(\Theta(m)=\overline{1}\otimes m\). If \(m\in IM\), say \(m=\sum_k i_k m_k\) with \(i_k\in I\), then \[ \Theta(m)=\sum_k \overline{1}\otimes i_k m_k=\sum_k \overline{i_k}\otimes m_k=0, \] so \(IM\subseteq \ker\Theta\).  ...`
- Companion excerpt: `\label{prob:cp-v-0022} Let \(A\) be a ring, let \(I\subseteq A\) be an ideal, and let \(M\) be an \(A\)-module. Prove that there is a natural isomorphism \[ (A/I)\otimes_A M \cong M/IM. \] Describe explicitly the mutually inverse maps.`

### Rank 4 — SEM-9A2BF2C983F4 (0.1857)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:2798-2986`
- Source excerpt: `\section{Problem 14(b) --- Existence of a minimal map from a free module} \textbf{Exact statement.} Let \((A,\mathfrak m)\) be a local ring, let \(k=A/\mathfrak m\), and let \(M\) be a finitely generated \(A\)-module. Show that there exists a minimal homomorphism \[ f:F\to M \] with \(F\) free. \textbf{Solution.} We want to construct a free \(A\)-module \(F\) and an \(A\)-linear map \[ f:F\to M \] such that \[ f\otimes_A k:\ F\otimes_A k \to M\otimes_A k \] is an isomorphism. Since \[ M\otimes_A k \cong M/\mathfrak m M, \qquad F\otimes_A k \cong F/\mathfrak m F, \] it is enough to construct \(f\) so that the induced map \[ \bar f:\ F/\mathfrak m F \to M/\mathfrak m M \] is an isomorphism. Because \(M\) is finitely generated over \(A\), the quotient \[ M/\mathfrak m M \] is a finite-dimensi ...`
- Companion excerpt: `\label{prob:cp-v-0022} Let \(A\) be a ring, let \(I\subseteq A\) be an ideal, and let \(M\) be an \(A\)-module. Prove that there is a natural isomorphism \[ (A/I)\otimes_A M \cong M/IM. \] Describe explicitly the mutually inverse maps.`

### Rank 5 — SEM-3ED9DD52ACD0 (0.1851)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-13.tex:780-784`
- Source excerpt: `\item Describe the closed sets of \[ \Spec(\mathbb Z). \]`
- Companion excerpt: `\label{prob:cp-v-0022} Let \(A\) be a ring, let \(I\subseteq A\) be an ideal, and let \(M\) be an \(A\)-module. Prove that there is a natural isomorphism \[ (A/I)\otimes_A M \cong M/IM. \] Describe explicitly the mutually inverse maps.`

## CP-V-0023

### Rank 1 — SEM-9BC82134F39C (0.3398)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:2100-2100`
- Source excerpt: `\item \textbf{\(\operatorname{Hom}_A(M,N)\):} the module of \(A\)-linear maps \(M\to N\).`
- Companion excerpt: `\label{prob:cp-v-0023} Let \(A\) be a ring, \(S\subseteq A\) a multiplicatively closed set, \(N\) an \(A\)-module, and \(M\) a finitely presented \(A\)-module. Prove that \[ S^{-1}\!\operatorname{Hom}_A(M,N) \cong \operatorname{Hom}_{S^{-1}A}(S^{-1}M,S^{-1}N). \] Give the explicit formula for the canonical map.`

### Rank 2 — SEM-3D2122F6FF35 (0.3159)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:1331-1390`
- Source excerpt: `\item a presentation of \(M\) localizes to a presentation of \(S^{-1}M\). \end{itemize} \subsection*{1.6. The \texorpdfstring{$\operatorname{Hom}$}{Hom} functor} For \(A\)-modules \(M,N\), the set of \(A\)-linear maps \(M\to N\) is denoted \[ \operatorname{Hom}_A(M,N). \] If \(A\) is commutative, this is naturally an \(A\)-module. Important special cases: \[ \operatorname{Hom}_A(A,N)\cong N, \qquad \operatorname{Hom}_A(A^n,N)\cong N^n. \] The functor \(\operatorname{Hom}_A(-,N)\) is \emph{contravariant} and \emph{left exact}. That is exactly why kernels appear in Problem 1. \subsection*{1.7. Why finite presentation matters in Problem 1} The isomorphism \[ S^{-1}\operatorname{Hom}_A(M,N)\cong \operatorname{Hom}_{S^{-1}A}(S^{-1}M,S^{-1}N) \] is not true for arbitrary \(M\). The crucial hypot ...`
- Companion excerpt: `\label{prob:cp-v-0023} Let \(A\) be a ring, \(S\subseteq A\) a multiplicatively closed set, \(N\) an \(A\)-module, and \(M\) a finitely presented \(A\)-module. Prove that \[ S^{-1}\!\operatorname{Hom}_A(M,N) \cong \operatorname{Hom}_{S^{-1}A}(S^{-1}M,S^{-1}N). \] Give the explicit formula for the canonical map.`

### Rank 3 — SEM-CC3B7C4E0746 (0.3103)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:2099-2099`
- Source excerpt: `\item \textbf{Finitely presented module:} the cokernel of a map \(A^{n_1}\to A^{n_2}\).`
- Companion excerpt: `\label{prob:cp-v-0023} Let \(A\) be a ring, \(S\subseteq A\) a multiplicatively closed set, \(N\) an \(A\)-module, and \(M\) a finitely presented \(A\)-module. Prove that \[ S^{-1}\!\operatorname{Hom}_A(M,N) \cong \operatorname{Hom}_{S^{-1}A}(S^{-1}M,S^{-1}N). \] Give the explicit formula for the canonical map.`

### Rank 4 — SEM-00612A5AA777 (0.2743)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:1221-1221`
- Source excerpt: `\item \textbf{Problem 1:} localization and how it interacts with modules and \(\operatorname{Hom}\).`
- Companion excerpt: `\label{prob:cp-v-0023} Let \(A\) be a ring, \(S\subseteq A\) a multiplicatively closed set, \(N\) an \(A\)-module, and \(M\) a finitely presented \(A\)-module. Prove that \[ S^{-1}\!\operatorname{Hom}_A(M,N) \cong \operatorname{Hom}_{S^{-1}A}(S^{-1}M,S^{-1}N). \] Give the explicit formula for the canonical map.`

### Rank 5 — SEM-F4D83E272792 (0.2574)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:4160-4160`
- Source excerpt: `\item \textbf{\(\operatorname{Ext}_A^i(M,N)\):} the cohomology obtained by applying \(\operatorname{Hom}_A(-,N)\) to a free resolution of \(M\).`
- Companion excerpt: `\label{prob:cp-v-0023} Let \(A\) be a ring, \(S\subseteq A\) a multiplicatively closed set, \(N\) an \(A\)-module, and \(M\) a finitely presented \(A\)-module. Prove that \[ S^{-1}\!\operatorname{Hom}_A(M,N) \cong \operatorname{Hom}_{S^{-1}A}(S^{-1}M,S^{-1}N). \] Give the explicit formula for the canonical map.`

## CP-V-0025

### Rank 1 — SEM-1203ECDE336C (0.2537)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2710-2718`
- Source excerpt: `\subsubsection*{Example 2: projective modules} Every projective module is flat, since every projective module is a direct summand of a free module, and direct summands of flat modules are flat. Thus \[ \text{free} \Longrightarrow \text{projective} \Longrightarrow \text{flat}. \]`
- Companion excerpt: `\label{prob:cp-v-0025} Let \(R\) be a ring and \(P\) an \(R\)-module. Prove that the following are equivalent. \textbf{(i)} \(P\) is projective. \textbf{(ii)} Every surjection \[ E\twoheadrightarrow P \] splits. \textbf{(iii)} Every short exact sequence \[ 0\longrightarrow K\longrightarrow E\longrightarrow P\longrightarrow0 \] splits. Use this criterion to prove that \[ R/(x) \] is not projective over \(R=k[x]\).`

### Rank 2 — SEM-F7FD9E94196B (0.2437)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-14.tex:276-315`
- Source excerpt: `\paragraph{Example 1: \(A=\mathbb Z\), \(\mathfrak p=(5)\).} We have \[ \mathbb Z_{(5)} = \left\{ \frac{a}{b}\in \mathbb Q : 5\nmid b \right\}. \] The local ring sequence is \[ 0 \longrightarrow 5\mathbb Z_{(5)} \longrightarrow \mathbb Z_{(5)} \longrightarrow \mathbb F_{5} \longrightarrow 0. \] Also the canonical map \[ \mathbb Z\longrightarrow \mathbb Z_{(5)} \] is injective, so there is an exact sequence \[ 0 \longrightarrow \mathbb Z \longrightarrow \mathbb Z_{(5)} \longrightarrow \mathbb Z_{(5)}/\mathbb Z \longrightarrow 0. \]`
- Companion excerpt: `\label{prob:cp-v-0025} Let \(R\) be a ring and \(P\) an \(R\)-module. Prove that the following are equivalent. \textbf{(i)} \(P\) is projective. \textbf{(ii)} Every surjection \[ E\twoheadrightarrow P \] splits. \textbf{(iii)} Every short exact sequence \[ 0\longrightarrow K\longrightarrow E\longrightarrow P\longrightarrow0 \] splits. Use this criterion to prove that \[ R/(x) \] is not projective over \(R=k[x]\).`

### Rank 3 — SEM-4E78BCA7D457 (0.2259)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-13.tex:2841-2864`
- Source excerpt: `\subsubsection{Example 1: the basic quotient sequence} Let \(A\) be a ring and \(I\subseteq A\) an ideal. Then there is always a short exact sequence \[ 0 \longrightarrow I \longrightarrow A \longrightarrow A/I \longrightarrow 0. \] Here: \begin{itemize} \item the map \(I\to A\) is the inclusion, \item the map \(A\to A/I\) is the quotient map \(a\mapsto a+I\). \end{itemize} This is exact because: \begin{itemize} \item the inclusion \(I\hookrightarrow A\) is injective, \item the quotient map \(A\to A/I\) is surjective, \item the kernel of \(A\to A/I\) is exactly \(I\). \end{itemize} This is the most basic exact sequence attached to an ideal.`
- Companion excerpt: `\label{prob:cp-v-0025} Let \(R\) be a ring and \(P\) an \(R\)-module. Prove that the following are equivalent. \textbf{(i)} \(P\) is projective. \textbf{(ii)} Every surjection \[ E\twoheadrightarrow P \] splits. \textbf{(iii)} Every short exact sequence \[ 0\longrightarrow K\longrightarrow E\longrightarrow P\longrightarrow0 \] splits. Use this criterion to prove that \[ R/(x) \] is not projective over \(R=k[x]\).`

### Rank 4 — SEM-CBC82F79254A (0.2216)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-13.tex:3419-3438`
- Source excerpt: `\subsubsection{Example 1: the basic quotient sequence over \(\mathbb Z\)} For any integer \(n\geq 1\), there is a short exact sequence \[ 0 \longrightarrow \mathbb Z \xrightarrow{\cdot n} \mathbb Z \longrightarrow \mathbb Z/n\mathbb Z \longrightarrow 0. \] This is exact because: \begin{itemize} \item the map \(m\mapsto nm\) is injective, \item its image is \(n\mathbb Z\), \item the quotient of \(\mathbb Z\) by \(n\mathbb Z\) is \(\mathbb Z/n\mathbb Z\). \end{itemize} Equivalently, one may write \[ 0 \longrightarrow (n) \longrightarrow \mathbb Z \longrightarrow \mathbb Z/(n) \longrightarrow 0. \]`
- Companion excerpt: `\label{prob:cp-v-0025} Let \(R\) be a ring and \(P\) an \(R\)-module. Prove that the following are equivalent. \textbf{(i)} \(P\) is projective. \textbf{(ii)} Every surjection \[ E\twoheadrightarrow P \] splits. \textbf{(iii)} Every short exact sequence \[ 0\longrightarrow K\longrightarrow E\longrightarrow P\longrightarrow0 \] splits. Use this criterion to prove that \[ R/(x) \] is not projective over \(R=k[x]\).`

### Rank 5 — SEM-CFCDE079D383 (0.2052)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-15.tex:216-228`
- Source excerpt: `\subsubsection*{Example 1: \(A/(x)\)} We have an exact sequence \[ 0 \longrightarrow A \xrightarrow{\cdot x} A \longrightarrow A/(x) \longrightarrow 0. \] Since \(A/(x)\cong k\), this can also be written as \[ 0 \longrightarrow k[x] \xrightarrow{\cdot x} k[x] \longrightarrow k \longrightarrow 0. \] So \(k\) has a free resolution of length \(1\) as a \(k[x]\)-module.`
- Companion excerpt: `\label{prob:cp-v-0025} Let \(R\) be a ring and \(P\) an \(R\)-module. Prove that the following are equivalent. \textbf{(i)} \(P\) is projective. \textbf{(ii)} Every surjection \[ E\twoheadrightarrow P \] splits. \textbf{(iii)} Every short exact sequence \[ 0\longrightarrow K\longrightarrow E\longrightarrow P\longrightarrow0 \] splits. Use this criterion to prove that \[ R/(x) \] is not projective over \(R=k[x]\).`

## CP-V-0044

### Rank 1 — SEM-83B38370CAB2 (0.5325)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-9.tex:4667-4690`
- Source excerpt: `\subsection{Example 1: free modules} Let \(A\) be any Noetherian local ring, and let \[ M=A^r \qquad (r\ge 1). \] Then \[ \operatorname{pd}_A(M)=0, \qquad \operatorname{depth}(M)=\operatorname{depth}(A). \] Hence \[ \operatorname{pd}_A(M)+\operatorname{depth}(M) = 0+\operatorname{depth}(A) = \operatorname{depth}(A). \] So the formula is immediate in the free case.`
- Companion excerpt: `\label{prob:cp-v-0044} Let \(A\) be a Noetherian local ring and let \(M\ne0\) be a finitely generated \(A\)-module with finite projective dimension. Prove the Auslander--Buchsbaum formula \[ \operatorname{pd}_A M+\operatorname{depth}(M) = \operatorname{depth}(A). \] You may use the characterization \[ \operatorname{depth}(N) = \min\left\{ i\ge0: \operatorname{Ext}_A^i(k,N)\ne0 \right\}, \qquad k=A/\mathfrak m. \]`

### Rank 2 — SEM-00B03F59D1DB (0.5237)
- Evidence: **UNVERIFIED**; identical math spans: 1
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:3248-3459`
- Source excerpt: `\section{Problem 17 --- Auslander--Buchsbaum formula} \textbf{Exact statement.} Let \(A\) be a Noetherian local ring and \(M\) a finitely generated \(A\)-module with \[ \operatorname{pd}_A M<\infty. \] Show that \[ \operatorname{pd}_A M+\operatorname{depth}(M)=\operatorname{depth}(A). \] \textbf{Solution.} This is the Auslander--Buchsbaum formula. We use the standard characterization of depth: \[ \operatorname{depth}(N) = \min\{\,i\ge 0 \mid \operatorname{Ext}_A^i(k,N)\neq 0\,\}, \qquad k=A/\mathfrak m, \] for every nonzero finitely generated \(A\)-module \(N\). Set \[ s:=\operatorname{depth}(A), \qquad n:=\operatorname{pd}_A M. \] We prove that \[ n+\operatorname{depth}(M)=s \] by induction on \(n\). \medskip \textbf{Case \(n=0\).} If \(\operatorname{pd}_A M=0\), then \(M\) is projective. ...`
- Companion excerpt: `\label{prob:cp-v-0044} Let \(A\) be a Noetherian local ring and let \(M\ne0\) be a finitely generated \(A\)-module with finite projective dimension. Prove the Auslander--Buchsbaum formula \[ \operatorname{pd}_A M+\operatorname{depth}(M) = \operatorname{depth}(A). \] You may use the characterization \[ \operatorname{depth}(N) = \min\left\{ i\ge0: \operatorname{Ext}_A^i(k,N)\ne0 \right\}, \qquad k=A/\mathfrak m. \]`

### Rank 3 — SEM-04644C405E22 (0.5033)
- Evidence: **UNVERIFIED**; identical math spans: 1
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:4047-4100`
- Source excerpt: `\item as the first place where \(\operatorname{Tor}\) vanishes. \end{itemize} So projective dimension is visible both from resolutions and from derived functors. \bigskip \section{7. Problem 17 theory: depth and the Auslander--Buchsbaum formula} \subsection*{7.1. Depth revisited} For a finitely generated module \(M\) over a Noetherian local ring, \[ \operatorname{depth}(M) \] measures how many independent non-zero-divisors one can find on \(M\). Equivalently, \[ \operatorname{depth}(M) = \min\{\,i\ge 0\mid \operatorname{Ext}_A^i(k,M)\neq 0\,\}. \] So depth may be understood either through regular sequences or through homological algebra. \subsection*{7.2. Why free modules have full depth} If \(F\cong A^r\) is a nonzero free module, then \[ \operatorname{Ext}_A^i(k,F)\cong \bigl(\operatorna ...`
- Companion excerpt: `\label{prob:cp-v-0044} Let \(A\) be a Noetherian local ring and let \(M\ne0\) be a finitely generated \(A\)-module with finite projective dimension. Prove the Auslander--Buchsbaum formula \[ \operatorname{pd}_A M+\operatorname{depth}(M) = \operatorname{depth}(A). \] You may use the characterization \[ \operatorname{depth}(N) = \min\left\{ i\ge0: \operatorname{Ext}_A^i(k,N)\ne0 \right\}, \qquad k=A/\mathfrak m. \]`

### Rank 4 — SEM-0802B243F68B (0.4051)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:4191-4196`
- Source excerpt: `\item For finite projective dimension, \[ \operatorname{pd}_A M = \min\{\,i\ge 0\mid \operatorname{Tor}_{i+1}^A(k,M)=0\,\}. \]`
- Companion excerpt: `\label{prob:cp-v-0044} Let \(A\) be a Noetherian local ring and let \(M\ne0\) be a finitely generated \(A\)-module with finite projective dimension. Prove the Auslander--Buchsbaum formula \[ \operatorname{pd}_A M+\operatorname{depth}(M) = \operatorname{depth}(A). \] You may use the characterization \[ \operatorname{depth}(N) = \min\left\{ i\ge0: \operatorname{Ext}_A^i(k,N)\ne0 \right\}, \qquad k=A/\mathfrak m. \]`

### Rank 5 — SEM-CCA8081CE402 (0.3969)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:4173-4177`
- Source excerpt: `\item \textbf{Depth:} maximal length of a regular sequence in \(\mathfrak m\), equivalently \[ \operatorname{depth}(M)=\min\{i\mid \operatorname{Ext}_A^i(k,M)\neq 0\}. \]`
- Companion excerpt: `\label{prob:cp-v-0044} Let \(A\) be a Noetherian local ring and let \(M\ne0\) be a finitely generated \(A\)-module with finite projective dimension. Prove the Auslander--Buchsbaum formula \[ \operatorname{pd}_A M+\operatorname{depth}(M) = \operatorname{depth}(A). \] You may use the characterization \[ \operatorname{depth}(N) = \min\left\{ i\ge0: \operatorname{Ext}_A^i(k,N)\ne0 \right\}, \qquad k=A/\mathfrak m. \]`

## CP-V-0045

### Rank 1 — SEM-9A2BF2C983F4 (0.4143)
- Evidence: **UNVERIFIED**; identical math spans: 3
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:2798-2986`
- Source excerpt: `\section{Problem 14(b) --- Existence of a minimal map from a free module} \textbf{Exact statement.} Let \((A,\mathfrak m)\) be a local ring, let \(k=A/\mathfrak m\), and let \(M\) be a finitely generated \(A\)-module. Show that there exists a minimal homomorphism \[ f:F\to M \] with \(F\) free. \textbf{Solution.} We want to construct a free \(A\)-module \(F\) and an \(A\)-linear map \[ f:F\to M \] such that \[ f\otimes_A k:\ F\otimes_A k \to M\otimes_A k \] is an isomorphism. Since \[ M\otimes_A k \cong M/\mathfrak m M, \qquad F\otimes_A k \cong F/\mathfrak m F, \] it is enough to construct \(f\) so that the induced map \[ \bar f:\ F/\mathfrak m F \to M/\mathfrak m M \] is an isomorphism. Because \(M\) is finitely generated over \(A\), the quotient \[ M/\mathfrak m M \] is a finite-dimensi ...`
- Companion excerpt: `\label{prob:cp-v-0045} Let \((A,\mathfrak m)\) be a local ring with residue field \[ k=A/\mathfrak m, \] and suppose \[ 0\longrightarrow K\xrightarrow{\,f\,}F\xrightarrow{\,g\,}M\longrightarrow0 \] is exact, where \(K\) and \(F\) are finite free \(A\)-modules and \(g\) is a minimal free cover. Prove that for every \(i\ge0\), the induced homomorphism \[ f_*:\operatorname{Ext}_A^i(k,K)\longrightarrow \operatorname{Ext}_A^i(k,F) \] is zero.`

### Rank 2 — SEM-ED8D0031F8B7 (0.4038)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-14.tex:351-377`
- Source excerpt: `\paragraph{Example 3: \(A=k[x,y]\), \(\mathfrak p=(x,y)\).} Then \[ A_{\mathfrak p}=k[x,y]_{(x,y)}. \] Its maximal ideal is \[ (x,y)A_{\mathfrak p}, \] and the residue field is \[ A_{\mathfrak p}/(x,y)A_{\mathfrak p}\cong k. \] Hence \[ 0 \longrightarrow (x,y)A_{\mathfrak p} \longrightarrow A_{\mathfrak p} \longrightarrow k \longrightarrow 0. \]`
- Companion excerpt: `\label{prob:cp-v-0045} Let \((A,\mathfrak m)\) be a local ring with residue field \[ k=A/\mathfrak m, \] and suppose \[ 0\longrightarrow K\xrightarrow{\,f\,}F\xrightarrow{\,g\,}M\longrightarrow0 \] is exact, where \(K\) and \(F\) are finite free \(A\)-modules and \(g\) is a minimal free cover. Prove that for every \(i\ge0\), the induced homomorphism \[ f_*:\operatorname{Ext}_A^i(k,K)\longrightarrow \operatorname{Ext}_A^i(k,F) \] is zero.`

### Rank 3 — SEM-7323972DB4F0 (0.3944)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-8.tex:4669-4702`
- Source excerpt: `\textbf{Problem 12.} A free resolution of \[ A/\mathfrak m \quad\text{for } A=k[x,y]/(xy),\ \mathfrak m=(x,y) \] is \[ \cdots \longrightarrow A^2 \xrightarrow{\begin{pmatrix}x&0\\0&y\end{pmatrix}} A^2 \xrightarrow{\begin{pmatrix}y&0\\0&x\end{pmatrix}} A^2 \xrightarrow{\begin{pmatrix}x&y\end{pmatrix}} A \longrightarrow A/\mathfrak m \longrightarrow 0. \] From this one gets \[ \boxed{\Ext_A^2(A/\mathfrak m,A)=0} \] and \[ \boxed{\Tor_0^A(A/\mathfrak m,A/\mathfrak m)\cong A/\mathfrak m,} \] \[ \boxed{\Tor_i^A(A/\mathfrak m,A/\mathfrak m)\cong (A/\mathfrak m)^2 \text{ for all } i\ge 1.} \] \medskip`
- Companion excerpt: `\label{prob:cp-v-0045} Let \((A,\mathfrak m)\) be a local ring with residue field \[ k=A/\mathfrak m, \] and suppose \[ 0\longrightarrow K\xrightarrow{\,f\,}F\xrightarrow{\,g\,}M\longrightarrow0 \] is exact, where \(K\) and \(F\) are finite free \(A\)-modules and \(g\) is a minimal free cover. Prove that for every \(i\ge0\), the induced homomorphism \[ f_*:\operatorname{Ext}_A^i(k,K)\longrightarrow \operatorname{Ext}_A^i(k,F) \] is zero.`

### Rank 4 — SEM-545A55F64703 (0.3922)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-9.tex:486-491`
- Source excerpt: `\begin{example} Thus a free resolution of \(A/(x,y)\) is \[ 0\longrightarrow A \xrightarrow{\begin{pmatrix}-y\\x\end{pmatrix}} A^2 \xrightarrow{(x\ \ y)} A \longrightarrow A/(x,y)\longrightarrow 0. \] \end{example}`
- Companion excerpt: `\label{prob:cp-v-0045} Let \((A,\mathfrak m)\) be a local ring with residue field \[ k=A/\mathfrak m, \] and suppose \[ 0\longrightarrow K\xrightarrow{\,f\,}F\xrightarrow{\,g\,}M\longrightarrow0 \] is exact, where \(K\) and \(F\) are finite free \(A\)-modules and \(g\) is a minimal free cover. Prove that for every \(i\ge0\), the induced homomorphism \[ f_*:\operatorname{Ext}_A^i(k,K)\longrightarrow \operatorname{Ext}_A^i(k,F) \] is zero.`

### Rank 5 — SEM-00B03F59D1DB (0.3788)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:3248-3459`
- Source excerpt: `\section{Problem 17 --- Auslander--Buchsbaum formula} \textbf{Exact statement.} Let \(A\) be a Noetherian local ring and \(M\) a finitely generated \(A\)-module with \[ \operatorname{pd}_A M<\infty. \] Show that \[ \operatorname{pd}_A M+\operatorname{depth}(M)=\operatorname{depth}(A). \] \textbf{Solution.} This is the Auslander--Buchsbaum formula. We use the standard characterization of depth: \[ \operatorname{depth}(N) = \min\{\,i\ge 0 \mid \operatorname{Ext}_A^i(k,N)\neq 0\,\}, \qquad k=A/\mathfrak m, \] for every nonzero finitely generated \(A\)-module \(N\). Set \[ s:=\operatorname{depth}(A), \qquad n:=\operatorname{pd}_A M. \] We prove that \[ n+\operatorname{depth}(M)=s \] by induction on \(n\). \medskip \textbf{Case \(n=0\).} If \(\operatorname{pd}_A M=0\), then \(M\) is projective. ...`
- Companion excerpt: `\label{prob:cp-v-0045} Let \((A,\mathfrak m)\) be a local ring with residue field \[ k=A/\mathfrak m, \] and suppose \[ 0\longrightarrow K\xrightarrow{\,f\,}F\xrightarrow{\,g\,}M\longrightarrow0 \] is exact, where \(K\) and \(F\) are finite free \(A\)-modules and \(g\) is a minimal free cover. Prove that for every \(i\ge0\), the induced homomorphism \[ f_*:\operatorname{Ext}_A^i(k,K)\longrightarrow \operatorname{Ext}_A^i(k,F) \] is zero.`

## CP-V-0047

### Rank 1 — SEM-65CD64552357 (0.5860)
- Evidence: **UNVERIFIED**; identical math spans: 1
- Source: `Downloads/theory-of-commutative-algebra-11.tex:3028-3043`
- Source excerpt: `\subsubsection*{Example 2} \[ \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z) \cong \mathbb Z/\gcd(n,m)\mathbb Z. \] In particular, \[ \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,\mathbb Z/3)=0, \] while \[ \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,\mathbb Z/4)\cong \mathbb Z/2. \]`
- Companion excerpt: `\label{prob:cp-v-0047} Let \(n,m\ge1\). \textbf{(a)} Prove that for every abelian group \(N\), \[ \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n\mathbb Z,N) \cong N[n] := \{x\in N:nx=0\}. \] \textbf{(b)} Deduce that \[ \operatorname{Tor}_1^{\mathbb Z} (\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z) \cong \mathbb Z/\gcd(n,m)\mathbb Z. \] \textbf{(c)} Compare this with \[ (\mathbb Z/n\mathbb Z)\otimes_{\mathbb Z} (\mathbb Z/m\mathbb Z). \]`

### Rank 2 — SEM-35FB0D44C8A1 (0.5264)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:3072-3078`
- Source excerpt: `\subsubsection*{Example 4} \[ \operatorname{Tor}_1^{k[x]}(k[x]/(x),k[x]/(x)) \cong k[x]/(x)\cong k. \]`
- Companion excerpt: `\label{prob:cp-v-0047} Let \(n,m\ge1\). \textbf{(a)} Prove that for every abelian group \(N\), \[ \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n\mathbb Z,N) \cong N[n] := \{x\in N:nx=0\}. \] \textbf{(b)} Deduce that \[ \operatorname{Tor}_1^{\mathbb Z} (\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z) \cong \mathbb Z/\gcd(n,m)\mathbb Z. \] \textbf{(c)} Compare this with \[ (\mathbb Z/n\mathbb Z)\otimes_{\mathbb Z} (\mathbb Z/m\mathbb Z). \]`

### Rank 3 — SEM-F752F65D3EAF (0.4803)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:4187-4190`
- Source excerpt: `\item In a minimal free resolution, \[ \operatorname{Tor}_i^A(k,M)\cong F_i\otimes_A k. \]`
- Companion excerpt: `\label{prob:cp-v-0047} Let \(n,m\ge1\). \textbf{(a)} Prove that for every abelian group \(N\), \[ \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n\mathbb Z,N) \cong N[n] := \{x\in N:nx=0\}. \] \textbf{(b)} Deduce that \[ \operatorname{Tor}_1^{\mathbb Z} (\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z) \cong \mathbb Z/\gcd(n,m)\mathbb Z. \] \textbf{(c)} Compare this with \[ (\mathbb Z/n\mathbb Z)\otimes_{\mathbb Z} (\mathbb Z/m\mathbb Z). \]`

### Rank 4 — SEM-B10E3119E21C (0.4421)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2449-2454`
- Source excerpt: `\subsubsection*{Example 1} For any abelian group \(M\), \[ \mathbb Z\otimes_{\mathbb Z} M\cong M. \]`
- Companion excerpt: `\label{prob:cp-v-0047} Let \(n,m\ge1\). \textbf{(a)} Prove that for every abelian group \(N\), \[ \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n\mathbb Z,N) \cong N[n] := \{x\in N:nx=0\}. \] \textbf{(b)} Deduce that \[ \operatorname{Tor}_1^{\mathbb Z} (\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z) \cong \mathbb Z/\gcd(n,m)\mathbb Z. \] \textbf{(c)} Compare this with \[ (\mathbb Z/n\mathbb Z)\otimes_{\mathbb Z} (\mathbb Z/m\mathbb Z). \]`

### Rank 5 — SEM-E403C92C8E28 (0.3817)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:3120-3126`
- Source excerpt: `\subsubsection*{Example 6} Let \(A=k[x]\) and \(M=A/(x)\). Since \[ \operatorname{Tor}_1^A(A/(x),A/(x))\cong k\neq 0, \] the module \(A/(x)\) is not flat.`
- Companion excerpt: `\label{prob:cp-v-0047} Let \(n,m\ge1\). \textbf{(a)} Prove that for every abelian group \(N\), \[ \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n\mathbb Z,N) \cong N[n] := \{x\in N:nx=0\}. \] \textbf{(b)} Deduce that \[ \operatorname{Tor}_1^{\mathbb Z} (\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z) \cong \mathbb Z/\gcd(n,m)\mathbb Z. \] \textbf{(c)} Compare this with \[ (\mathbb Z/n\mathbb Z)\otimes_{\mathbb Z} (\mathbb Z/m\mathbb Z). \]`

## CP-V-0048

### Rank 1 — SEM-35FB0D44C8A1 (0.4730)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:3072-3078`
- Source excerpt: `\subsubsection*{Example 4} \[ \operatorname{Tor}_1^{k[x]}(k[x]/(x),k[x]/(x)) \cong k[x]/(x)\cong k. \]`
- Companion excerpt: `\label{prob:cp-v-0048} Let \(A\) be a ring and let \(I,J\subseteq A\) be ideals. Prove the natural isomorphism \[ \operatorname{Tor}_1^A(A/I,A/J) \cong \frac{I\cap J}{IJ}. \] Use it to compute: \textbf{(a)} \[ \operatorname{Tor}_1^{k[x]} \bigl(k[x]/(x),k[x]/(x)\bigr); \] \textbf{(b)} \[ \operatorname{Tor}_1^{k[x]} \bigl(k[x]/(x),k[x]/(x-1)\bigr). \]`

### Rank 2 — SEM-65CD64552357 (0.4432)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:3028-3043`
- Source excerpt: `\subsubsection*{Example 2} \[ \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z) \cong \mathbb Z/\gcd(n,m)\mathbb Z. \] In particular, \[ \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,\mathbb Z/3)=0, \] while \[ \operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,\mathbb Z/4)\cong \mathbb Z/2. \]`
- Companion excerpt: `\label{prob:cp-v-0048} Let \(A\) be a ring and let \(I,J\subseteq A\) be ideals. Prove the natural isomorphism \[ \operatorname{Tor}_1^A(A/I,A/J) \cong \frac{I\cap J}{IJ}. \] Use it to compute: \textbf{(a)} \[ \operatorname{Tor}_1^{k[x]} \bigl(k[x]/(x),k[x]/(x)\bigr); \] \textbf{(b)} \[ \operatorname{Tor}_1^{k[x]} \bigl(k[x]/(x),k[x]/(x-1)\bigr). \]`

### Rank 3 — SEM-E82AA2CEF10C (0.4162)
- Evidence: **UNVERIFIED**; identical math spans: 2
- Source: `Downloads/theory-of-commutative-algebra-11.tex:3681-3761`
- Source excerpt: `\subsection{Example over \(k[x]\): coprime quotients} Let \[ A=k[x], \qquad M=A/(x), \qquad N=A/(x-1). \] Again resolve \(M\) by \[ 0\to A \xrightarrow{\cdot x} A \to A/(x)\to 0. \] Tensor with \(N=A/(x-1)\). Then \[ 0\to A/(x-1)\xrightarrow{\cdot x}A/(x-1)\to 0. \] But in \(A/(x-1)\), the class of \(x\) is equal to \(1\). Thus multiplication by \(x\) is an isomorphism. Therefore the kernel is \(0\), so \[ \operatorname{Tor}_1^{k[x]}(A/(x),A/(x-1))=0. \] This reflects the fact that \((x)\) and \((x-1)\) are coprime ideals. \subsection{A very useful formula for quotient modules} Let \(A\) be a commutative ring and let \(I,J\subseteq A\) be ideals. Then \[ \operatorname{Tor}_1^A(A/I,A/J)\cong \frac{I\cap J}{IJ}. \] \medskip \textbf{Proof.} Start with the exact sequence \[ 0\to I \to A \to A/ ...`
- Companion excerpt: `\label{prob:cp-v-0048} Let \(A\) be a ring and let \(I,J\subseteq A\) be ideals. Prove the natural isomorphism \[ \operatorname{Tor}_1^A(A/I,A/J) \cong \frac{I\cap J}{IJ}. \] Use it to compute: \textbf{(a)} \[ \operatorname{Tor}_1^{k[x]} \bigl(k[x]/(x),k[x]/(x)\bigr); \] \textbf{(b)} \[ \operatorname{Tor}_1^{k[x]} \bigl(k[x]/(x),k[x]/(x-1)\bigr). \]`

### Rank 4 — SEM-8218DF1F6F29 (0.3857)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:3762-3799`
- Source excerpt: `\subsection{Example in \(k[x,y]\): transversal ideals} Let \[ A=k[x,y], \qquad I=(x), \qquad J=(y). \] Then \[ I\cap J=(xy), \qquad IJ=(xy), \] so \[ \frac{I\cap J}{IJ}=0. \] Hence \[ \operatorname{Tor}_1^{k[x,y]}(A/(x),A/(y))=0. \] This matches the direct computation: resolving \(A/(x)\) by \[ 0\to A\xrightarrow{\cdot x}A\to A/(x)\to 0 \] and tensoring with \(A/(y)\cong k[x]\), we get multiplication by \(x\) on \(k[x]\), which is injective. So again \[ \operatorname{Tor}_1^{k[x,y]}(A/(x),A/(y))=0. \]`
- Companion excerpt: `\label{prob:cp-v-0048} Let \(A\) be a ring and let \(I,J\subseteq A\) be ideals. Prove the natural isomorphism \[ \operatorname{Tor}_1^A(A/I,A/J) \cong \frac{I\cap J}{IJ}. \] Use it to compute: \textbf{(a)} \[ \operatorname{Tor}_1^{k[x]} \bigl(k[x]/(x),k[x]/(x)\bigr); \] \textbf{(b)} \[ \operatorname{Tor}_1^{k[x]} \bigl(k[x]/(x),k[x]/(x-1)\bigr). \]`

### Rank 5 — SEM-E403C92C8E28 (0.3616)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:3120-3126`
- Source excerpt: `\subsubsection*{Example 6} Let \(A=k[x]\) and \(M=A/(x)\). Since \[ \operatorname{Tor}_1^A(A/(x),A/(x))\cong k\neq 0, \] the module \(A/(x)\) is not flat.`
- Companion excerpt: `\label{prob:cp-v-0048} Let \(A\) be a ring and let \(I,J\subseteq A\) be ideals. Prove the natural isomorphism \[ \operatorname{Tor}_1^A(A/I,A/J) \cong \frac{I\cap J}{IJ}. \] Use it to compute: \textbf{(a)} \[ \operatorname{Tor}_1^{k[x]} \bigl(k[x]/(x),k[x]/(x)\bigr); \] \textbf{(b)} \[ \operatorname{Tor}_1^{k[x]} \bigl(k[x]/(x),k[x]/(x-1)\bigr). \]`

## CP-V-0058

### Rank 1 — SEM-917E6A31A4E1 (0.2206)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-8.tex:2210-2231`
- Source excerpt: `\textbf{Example 1: \(\Gamma=\mathbb Z\).} Then the basis elements are \[ \dots,\ z^{-2},\ z^{-1},\ 1,\ z,\ z^2,\dots \] and \[ z^m z^n = z^{m+n}. \] So \[ k[\mathbb Z]\cong k[z,z^{-1}], \] the Laurent polynomial ring in one variable. Typical elements are \[ 3z^{-2}+5+7z^4, \qquad z^{-10}-2z^3. \]`
- Companion excerpt: `\label{prob:cp-v-0058} Let \(A\) be a ring and let \(F=A^n\). Suppose \[ x_1,\dots,x_n \] generate \(F\). Prove that they form a basis.`

### Rank 2 — SEM-4EC499BB0FC3 (0.1986)
- Evidence: **UNVERIFIED**; identical math spans: 1
- Source: `Downloads/theory-of-commutative-algebra-1.tex:1652-1785`
- Source excerpt: `\section*{Problem 9 — Any \(n\) generators of \(A^n\) form a basis} \textbf{Exact statement.} Let \(A\) be a ring. Let \(F\) be the free \(A\)-module \[ F=A^n. \] Show that every set of \(n\) generators \[ x_1,\dots,x_n \] of \(F\) is a basis of \(F\). Equivalently, if \[ \sum_{i=1}^n a_i x_i = 0, \] then \[ a_i=0 \qquad\text{for all }i. \] \bigskip \textbf{Solution.} Define an \(A\)-linear map \[ \varphi:A^n\longrightarrow F \] by \[ \varphi(e_i)=x_i, \] where \(e_1,\dots,e_n\) is the standard basis of \(A^n\). Since \(x_1,\dots,x_n\) generate \(F\), the map \(\varphi\) is surjective. We must show that \(\varphi\) is injective. \medskip \textbf{Step 1: localize at a maximal ideal.} Let \(\mathfrak m\) be a maximal ideal of \(A\). Localizing gives a surjective map \[ \varphi_{\mathfrak m}: ...`
- Companion excerpt: `\label{prob:cp-v-0058} Let \(A\) be a ring and let \(F=A^n\). Suppose \[ x_1,\dots,x_n \] generate \(F\). Prove that they form a basis.`

### Rank 3 — SEM-16D480FA1BC5 (0.1687)
- Evidence: **UNVERIFIED**; identical math spans: 1
- Source: `Downloads/theory-of-commutative-algebra-9.tex:3111-3113`
- Source excerpt: `\begin{example} Over \(A=k[[x_1,\dots,x_n]]\), the minimal free resolution of \(k\) is the Koszul complex on \(x_1,\dots,x_n\). \end{example}`
- Companion excerpt: `\label{prob:cp-v-0058} Let \(A\) be a ring and let \(F=A^n\). Suppose \[ x_1,\dots,x_n \] generate \(F\). Prove that they form a basis.`

### Rank 4 — SEM-325ED120291E (0.1586)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:3895-3895`
- Source excerpt: `\item lift those basis elements to \(M\),`
- Companion excerpt: `\label{prob:cp-v-0058} Let \(A\) be a ring and let \(F=A^n\). Suppose \[ x_1,\dots,x_n \] generate \(F\). Prove that they form a basis.`

### Rank 5 — SEM-006D0FDCB875 (0.1548)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:1670-1670`
- Source excerpt: `\item the nonunits of \(A\) form an ideal,`
- Companion excerpt: `\label{prob:cp-v-0058} Let \(A\) be a ring and let \(F=A^n\). Suppose \[ x_1,\dots,x_n \] generate \(F\). Prove that they form a basis.`

## CP-V-0095

### Rank 1 — SEM-D2A0B35D4E15 (0.7616)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2517-2525`
- Source excerpt: `\subsubsection*{Example 9} \[ k\otimes_{k[x]} k[x]/(x^2) \cong k[x]/(x)\otimes_{k[x]} k[x]/(x^2) \cong k[x]/(x,x^2)\cong k. \]`
- Companion excerpt: `\label{prob:cp-v-0095} Compute \(\mathbb C\otimes_{\mathbb R}\mathbb C\).`

### Rank 2 — SEM-3F5F92B00751 (0.6450)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2460-2477`
- Source excerpt: `\subsubsection*{Example 3} \[ \mathbb Z/n\mathbb Z\otimes_{\mathbb Z}\mathbb Z/m\mathbb Z \cong \mathbb Z/\gcd(n,m)\mathbb Z. \] In particular, \[ \mathbb Z/2\mathbb Z\otimes_{\mathbb Z}\mathbb Z/3\mathbb Z=0, \] while \[ \mathbb Z/2\mathbb Z\otimes_{\mathbb Z}\mathbb Z/4\mathbb Z \cong \mathbb Z/2\mathbb Z. \]`
- Companion excerpt: `\label{prob:cp-v-0095} Compute \(\mathbb C\otimes_{\mathbb R}\mathbb C\).`

### Rank 3 — SEM-B10E3119E21C (0.5078)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2449-2454`
- Source excerpt: `\subsubsection*{Example 1} For any abelian group \(M\), \[ \mathbb Z\otimes_{\mathbb Z} M\cong M. \]`
- Companion excerpt: `\label{prob:cp-v-0095} Compute \(\mathbb C\otimes_{\mathbb R}\mathbb C\).`

### Rank 4 — SEM-F752F65D3EAF (0.4252)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:4187-4190`
- Source excerpt: `\item In a minimal free resolution, \[ \operatorname{Tor}_i^A(k,M)\cong F_i\otimes_A k. \]`
- Companion excerpt: `\label{prob:cp-v-0095} Compute \(\mathbb C\otimes_{\mathbb R}\mathbb C\).`

### Rank 5 — SEM-3551086F7AB3 (0.3774)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2511-2516`
- Source excerpt: `\subsubsection*{Example 8} View \(k\) as a \(k[x]\)-module via \(x\mapsto 0\). Then \[ k\otimes_{k[x]} k[x]\cong k. \]`
- Companion excerpt: `\label{prob:cp-v-0095} Compute \(\mathbb C\otimes_{\mathbb R}\mathbb C\).`

## CP-V-0096

### Rank 1 — SEM-D2A0B35D4E15 (0.5888)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2517-2525`
- Source excerpt: `\subsubsection*{Example 9} \[ k\otimes_{k[x]} k[x]/(x^2) \cong k[x]/(x)\otimes_{k[x]} k[x]/(x^2) \cong k[x]/(x,x^2)\cong k. \]`
- Companion excerpt: `\label{prob:cp-v-0096} Show that \((k[x]/(f))\otimes_k K\cong K[x]/(f)\) for a field extension \(K/k\).`

### Rank 2 — SEM-C01F84DFBA6F (0.5176)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-13.tex:3202-3226`
- Source excerpt: `\subsubsection{Example 15: tensoring a quotient sequence over a field} Now take a field \(k\), and consider \[ 0 \longrightarrow (x) \longrightarrow k[x] \longrightarrow k \longrightarrow 0. \] Tensor with a field extension \(K/k\). Since tensoring over a field is exact, we get \[ 0 \longrightarrow (x)\otimes_k K \longrightarrow k[x]\otimes_k K \longrightarrow k\otimes_k K \longrightarrow 0. \] Using \[ k[x]\otimes_k K \cong K[x], \qquad k\otimes_k K \cong K, \] this becomes \[ 0 \longrightarrow (x)K[x] \longrightarrow K[x] \longrightarrow K \longrightarrow 0. \] So over a field, extension of scalars preserves short exact sequences of vector spaces and free modules much better than tensoring over \(\mathbb Z\).`
- Companion excerpt: `\label{prob:cp-v-0096} Show that \((k[x]/(f))\otimes_k K\cong K[x]/(f)\) for a field extension \(K/k\).`

### Rank 3 — SEM-3F5F92B00751 (0.4434)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2460-2477`
- Source excerpt: `\subsubsection*{Example 3} \[ \mathbb Z/n\mathbb Z\otimes_{\mathbb Z}\mathbb Z/m\mathbb Z \cong \mathbb Z/\gcd(n,m)\mathbb Z. \] In particular, \[ \mathbb Z/2\mathbb Z\otimes_{\mathbb Z}\mathbb Z/3\mathbb Z=0, \] while \[ \mathbb Z/2\mathbb Z\otimes_{\mathbb Z}\mathbb Z/4\mathbb Z \cong \mathbb Z/2\mathbb Z. \]`
- Companion excerpt: `\label{prob:cp-v-0096} Show that \((k[x]/(f))\otimes_k K\cong K[x]/(f)\) for a field extension \(K/k\).`

### Rank 4 — SEM-B10E3119E21C (0.3685)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2449-2454`
- Source excerpt: `\subsubsection*{Example 1} For any abelian group \(M\), \[ \mathbb Z\otimes_{\mathbb Z} M\cong M. \]`
- Companion excerpt: `\label{prob:cp-v-0096} Show that \((k[x]/(f))\otimes_k K\cong K[x]/(f)\) for a field extension \(K/k\).`

### Rank 5 — SEM-CB06743B4E48 (0.3114)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-13.tex:4057-4092`
- Source excerpt: `\subsubsection{Example 5: \(A=\mathbb F_p[x]\), \(\mf p=(f)\) with \(f\) irreducible} Let \[ A=\mathbb F_p[x], \qquad \mf p=(f), \] where \(f(x)\in \mathbb F_p[x]\) is irreducible of degree \(d\). Then \[ A_{\mf p}=\mathbb F_p[x]_{(f)}, \qquad \mf p A_{\mf p}=f\mathbb F_p[x]_{(f)}. \] The residue field is \[ k(\mf p)\cong \mathbb F_p[x]/(f)\cong \mathbb F_{p^d}. \] So the exact sequence is \[ 0 \longrightarrow f\mathbb F_p[x]_{(f)} \longrightarrow \mathbb F_p[x]_{(f)} \longrightarrow \mathbb F_{p^d} \longrightarrow 0. \] This is the finite-field-extension version of the local residue field sequence.`
- Companion excerpt: `\label{prob:cp-v-0096} Show that \((k[x]/(f))\otimes_k K\cong K[x]/(f)\) for a field extension \(K/k\).`

## CP-V-0105

### Rank 1 — SEM-9BC82134F39C (0.2896)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:2100-2100`
- Source excerpt: `\item \textbf{\(\operatorname{Hom}_A(M,N)\):} the module of \(A\)-linear maps \(M\to N\).`
- Companion excerpt: `\label{prob:cp-v-0105} Let \(M\) be a finitely presented \(A\)-module and let \((N_i)_{i\in I}\) be a filtered direct system of \(A\)-modules. Prove that the canonical map \[ \varinjlim_i \operatorname{Hom}_A(M,N_i) \longrightarrow \operatorname{Hom}_A\!\left(M,\varinjlim_i N_i\right) \] is an isomorphism.`

### Rank 2 — SEM-3D2122F6FF35 (0.2783)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:1331-1390`
- Source excerpt: `\item a presentation of \(M\) localizes to a presentation of \(S^{-1}M\). \end{itemize} \subsection*{1.6. The \texorpdfstring{$\operatorname{Hom}$}{Hom} functor} For \(A\)-modules \(M,N\), the set of \(A\)-linear maps \(M\to N\) is denoted \[ \operatorname{Hom}_A(M,N). \] If \(A\) is commutative, this is naturally an \(A\)-module. Important special cases: \[ \operatorname{Hom}_A(A,N)\cong N, \qquad \operatorname{Hom}_A(A^n,N)\cong N^n. \] The functor \(\operatorname{Hom}_A(-,N)\) is \emph{contravariant} and \emph{left exact}. That is exactly why kernels appear in Problem 1. \subsection*{1.7. Why finite presentation matters in Problem 1} The isomorphism \[ S^{-1}\operatorname{Hom}_A(M,N)\cong \operatorname{Hom}_{S^{-1}A}(S^{-1}M,S^{-1}N) \] is not true for arbitrary \(M\). The crucial hypot ...`
- Companion excerpt: `\label{prob:cp-v-0105} Let \(M\) be a finitely presented \(A\)-module and let \((N_i)_{i\in I}\) be a filtered direct system of \(A\)-modules. Prove that the canonical map \[ \varinjlim_i \operatorname{Hom}_A(M,N_i) \longrightarrow \operatorname{Hom}_A\!\left(M,\varinjlim_i N_i\right) \] is an isomorphism.`

### Rank 3 — SEM-CC3B7C4E0746 (0.2650)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:2099-2099`
- Source excerpt: `\item \textbf{Finitely presented module:} the cokernel of a map \(A^{n_1}\to A^{n_2}\).`
- Companion excerpt: `\label{prob:cp-v-0105} Let \(M\) be a finitely presented \(A\)-module and let \((N_i)_{i\in I}\) be a filtered direct system of \(A\)-modules. Prove that the canonical map \[ \varinjlim_i \operatorname{Hom}_A(M,N_i) \longrightarrow \operatorname{Hom}_A\!\left(M,\varinjlim_i N_i\right) \] is an isomorphism.`

### Rank 4 — SEM-7C19550B2D95 (0.2244)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2753-2756`
- Source excerpt: `\subsubsection*{Example 6: direct limits} Filtered direct limits of flat modules are flat.`
- Companion excerpt: `\label{prob:cp-v-0105} Let \(M\) be a finitely presented \(A\)-module and let \((N_i)_{i\in I}\) be a filtered direct system of \(A\)-modules. Prove that the canonical map \[ \varinjlim_i \operatorname{Hom}_A(M,N_i) \longrightarrow \operatorname{Hom}_A\!\left(M,\varinjlim_i N_i\right) \] is an isomorphism.`

### Rank 5 — SEM-00612A5AA777 (0.2225)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:1221-1221`
- Source excerpt: `\item \textbf{Problem 1:} localization and how it interacts with modules and \(\operatorname{Hom}\).`
- Companion excerpt: `\label{prob:cp-v-0105} Let \(M\) be a finitely presented \(A\)-module and let \((N_i)_{i\in I}\) be a filtered direct system of \(A\)-modules. Prove that the canonical map \[ \varinjlim_i \operatorname{Hom}_A(M,N_i) \longrightarrow \operatorname{Hom}_A\!\left(M,\varinjlim_i N_i\right) \] is an isomorphism.`

## CP-V-0106

### Rank 1 — SEM-98947BF4D339 (0.7372)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2815-2830`
- Source excerpt: `\subsubsection*{Example 11: torsion-free modules over a PID} If \(A\) is a principal ideal domain, then an \(A\)-module is flat if and only if it is torsion-free. In particular, over \(\mathbb Z\), an abelian group is flat if and only if it has no torsion. Thus \[ \mathbb Z,\qquad \mathbb Z^r,\qquad \mathbb Q,\qquad \mathbb Z_{(p)} \] are flat over \(\mathbb Z\), while \[ \mathbb Z/n\mathbb Z,\qquad \mathbb Q/\mathbb Z \] are not.`
- Companion excerpt: `\label{prob:cp-v-0106} Let \(A\) be a principal ideal domain and \(M\) an \(A\)-module. Prove that \(M\) is flat if and only if \(M\) is torsion-free.`

### Rank 2 — SEM-0C93CF8CCD08 (0.5254)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-14.tex:1197-1214`
- Source excerpt: `\paragraph{Example 13: over a PID, torsion-free implies flat.} Over a principal ideal domain such as \[ \mathbb Z \quad\text{or}\quad k[x], \] every torsion-free module is flat. Thus: \[ \mathbb Q,\quad \mathbb Z_{(p)},\quad (x)\subseteq k[x] \] are flat. This is an important source of examples of flat modules that are not free.`
- Companion excerpt: `\label{prob:cp-v-0106} Let \(A\) be a principal ideal domain and \(M\) an \(A\)-module. Prove that \(M\) is flat if and only if \(M\) is torsion-free.`

### Rank 3 — SEM-75641C32842E (0.5016)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2831-2842`
- Source excerpt: `\subsubsection*{Example 12: principal ideals in a domain} If \(A\) is an integral domain and \(a\neq 0\), then the principal ideal \[ (a)\subseteq A \] is isomorphic to \(A\) as an \(A\)-module via \[ A\to (a),\qquad r\mapsto ra. \] Hence \((a)\) is free of rank \(1\), and therefore flat.`
- Companion excerpt: `\label{prob:cp-v-0106} Let \(A\) be a principal ideal domain and \(M\) an \(A\)-module. Prove that \(M\) is flat if and only if \(M\) is torsion-free.`

### Rank 4 — SEM-6C534CC843EE (0.3145)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:2843-2855`
- Source excerpt: `\subsubsection*{Example 13: local criterion} If \(M\) is flat over \(A\), then for every prime ideal \(\mathfrak p\), \[ M_{\mathfrak p} \] is flat over the local ring \[ A_{\mathfrak p}. \] Moreover, over a local ring, finitely generated flat modules are free.`
- Companion excerpt: `\label{prob:cp-v-0106} Let \(A\) be a principal ideal domain and \(M\) an \(A\)-module. Prove that \(M\) is flat if and only if \(M\) is torsion-free.`

### Rank 5 — SEM-8BA7C831CDD6 (0.2941)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-1.tex:579-590`
- Source excerpt: `\section*{Problem 5 — \(A[x]\) is flat over \(A\)} \textbf{Exact statement.} Let \(A[x]\) denote the polynomial ring in one variable over a ring \(A\). Show that \(A[x]\) is a flat \(A\)-module. \textbf{Solution.} As an \(A\)-module, \[ A[x]\cong \bigoplus_{n\ge 0} A\cdot x^n, \] so \(A[x]\) is free with basis \(\{1,x,x^2,\dots\}\). Every free module is flat. Hence \(A[x]\) is flat over \(A\).`
- Companion excerpt: `\label{prob:cp-v-0106} Let \(A\) be a principal ideal domain and \(M\) an \(A\)-module. Prove that \(M\) is flat if and only if \(M\) is torsion-free.`

## CP-V-0113

### Rank 1 — SEM-4BDBA5056144 (0.6069)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:3728-3728`
- Source excerpt: `\item \(\operatorname{Ext}\) and \(\operatorname{Tor}\) are computed from resolutions,`
- Companion excerpt: `\label{prob:cp-v-0113} Compute \[ \operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z). \]`

### Rank 2 — SEM-0E408713D3BD (0.4921)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:3470-3470`
- Source excerpt: `\item \textbf{Problem 12:} explicit free resolutions, and computations of \(\operatorname{Ext}\) and \(\operatorname{Tor}\).`
- Companion excerpt: `\label{prob:cp-v-0113} Compute \[ \operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z). \]`

### Rank 3 — SEM-7D304AA75A0F (0.4695)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:3705-3725`
- Source excerpt: `\item define \[ \operatorname{Ext}_A^i(M,N)=H^i(\operatorname{Hom}_A(F_\bullet,N)). \] \end{itemize} One has \[ \operatorname{Ext}_A^0(M,N)=\operatorname{Hom}_A(M,N). \] The group \(\operatorname{Ext}_A^1(M,N)\) classifies extensions \[ 0\to N\to E\to M\to 0, \] and higher \(\operatorname{Ext}\) measures deeper homological complexity. \subsection*{2.7. Meaning of Problem 12} Problem 12 teaches several important principles at once: \begin{itemize}`
- Companion excerpt: `\label{prob:cp-v-0113} Compute \[ \operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z). \]`

### Rank 4 — SEM-F4D83E272792 (0.4577)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:4160-4160`
- Source excerpt: `\item \textbf{\(\operatorname{Ext}_A^i(M,N)\):} the cohomology obtained by applying \(\operatorname{Hom}_A(-,N)\) to a free resolution of \(M\).`
- Companion excerpt: `\label{prob:cp-v-0113} Compute \[ \operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z). \]`

### Rank 5 — SEM-85AC86E2F160 (0.4531)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:4211-4211`
- Source excerpt: `\item \textbf{Problem 12} shows how explicit resolutions let us compute \(\operatorname{Ext}\) and \(\operatorname{Tor}\).`
- Companion excerpt: `\label{prob:cp-v-0113} Compute \[ \operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z). \]`

## CP-V-0114

### Rank 1 — SEM-00B03F59D1DB (0.3137)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:3248-3459`
- Source excerpt: `\section{Problem 17 --- Auslander--Buchsbaum formula} \textbf{Exact statement.} Let \(A\) be a Noetherian local ring and \(M\) a finitely generated \(A\)-module with \[ \operatorname{pd}_A M<\infty. \] Show that \[ \operatorname{pd}_A M+\operatorname{depth}(M)=\operatorname{depth}(A). \] \textbf{Solution.} This is the Auslander--Buchsbaum formula. We use the standard characterization of depth: \[ \operatorname{depth}(N) = \min\{\,i\ge 0 \mid \operatorname{Ext}_A^i(k,N)\neq 0\,\}, \qquad k=A/\mathfrak m, \] for every nonzero finitely generated \(A\)-module \(N\). Set \[ s:=\operatorname{depth}(A), \qquad n:=\operatorname{pd}_A M. \] We prove that \[ n+\operatorname{depth}(M)=s \] by induction on \(n\). \medskip \textbf{Case \(n=0\).} If \(\operatorname{pd}_A M=0\), then \(M\) is projective. ...`
- Companion excerpt: `\label{prob:cp-v-0114} Let \[ 0\to A'\to A\to A''\to0 \] be a short exact sequence of \(R\)-modules. Explain why the long exact sequence of \(\operatorname{Tor}\) measures the failure of tensor product to be left exact, while the long exact sequence of \(\operatorname{Ext}\) measures the failure of \(\operatorname{Hom}\) to be right exact.`

### Rank 2 — SEM-709E8FDB149B (0.3080)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:3679-3702`
- Source excerpt: `\item define \[ \operatorname{Tor}_i^A(M,N)=H_i(F_\bullet\otimes_A N). \] \end{itemize} The first term is \[ \operatorname{Tor}_0^A(M,N)\cong M\otimes_A N. \] Higher \(\operatorname{Tor}\) detects hidden relations between \(M\) and \(N\). In Problem 12, after tensoring with \(k\), all differentials vanish because \(x\) and \(y\) act by zero on \(k\). This makes the calculation very transparent. \subsection*{2.6. The functor \texorpdfstring{$\operatorname{Ext}$}{Ext}} Given \(A\)-modules \(M,N\), the groups \[ \operatorname{Ext}_A^i(M,N) \] measure the failure of \(\operatorname{Hom}_A(-,N)\) to be exact in the first variable. Construction: \begin{itemize}`
- Companion excerpt: `\label{prob:cp-v-0114} Let \[ 0\to A'\to A\to A''\to0 \] be a short exact sequence of \(R\)-modules. Explain why the long exact sequence of \(\operatorname{Tor}\) measures the failure of tensor product to be left exact, while the long exact sequence of \(\operatorname{Ext}\) measures the failure of \(\operatorname{Hom}\) to be right exact.`

### Rank 3 — SEM-E82AA2CEF10C (0.2998)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:3681-3761`
- Source excerpt: `\subsection{Example over \(k[x]\): coprime quotients} Let \[ A=k[x], \qquad M=A/(x), \qquad N=A/(x-1). \] Again resolve \(M\) by \[ 0\to A \xrightarrow{\cdot x} A \to A/(x)\to 0. \] Tensor with \(N=A/(x-1)\). Then \[ 0\to A/(x-1)\xrightarrow{\cdot x}A/(x-1)\to 0. \] But in \(A/(x-1)\), the class of \(x\) is equal to \(1\). Thus multiplication by \(x\) is an isomorphism. Therefore the kernel is \(0\), so \[ \operatorname{Tor}_1^{k[x]}(A/(x),A/(x-1))=0. \] This reflects the fact that \((x)\) and \((x-1)\) are coprime ideals. \subsection{A very useful formula for quotient modules} Let \(A\) be a commutative ring and let \(I,J\subseteq A\) be ideals. Then \[ \operatorname{Tor}_1^A(A/I,A/J)\cong \frac{I\cap J}{IJ}. \] \medskip \textbf{Proof.} Start with the exact sequence \[ 0\to I \to A \to A/ ...`
- Companion excerpt: `\label{prob:cp-v-0114} Let \[ 0\to A'\to A\to A''\to0 \] be a short exact sequence of \(R\)-modules. Explain why the long exact sequence of \(\operatorname{Tor}\) measures the failure of tensor product to be left exact, while the long exact sequence of \(\operatorname{Ext}\) measures the failure of \(\operatorname{Hom}\) to be right exact.`

### Rank 4 — SEM-7D304AA75A0F (0.2942)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-5-professional-v2.tex:3705-3725`
- Source excerpt: `\item define \[ \operatorname{Ext}_A^i(M,N)=H^i(\operatorname{Hom}_A(F_\bullet,N)). \] \end{itemize} One has \[ \operatorname{Ext}_A^0(M,N)=\operatorname{Hom}_A(M,N). \] The group \(\operatorname{Ext}_A^1(M,N)\) classifies extensions \[ 0\to N\to E\to M\to 0, \] and higher \(\operatorname{Ext}\) measures deeper homological complexity. \subsection*{2.7. Meaning of Problem 12} Problem 12 teaches several important principles at once: \begin{itemize}`
- Companion excerpt: `\label{prob:cp-v-0114} Let \[ 0\to A'\to A\to A''\to0 \] be a short exact sequence of \(R\)-modules. Explain why the long exact sequence of \(\operatorname{Tor}\) measures the failure of tensor product to be left exact, while the long exact sequence of \(\operatorname{Ext}\) measures the failure of \(\operatorname{Hom}\) to be right exact.`

### Rank 5 — SEM-9EF0BFC990E5 (0.2773)
- Evidence: **UNVERIFIED**; identical math spans: 0
- Source: `Downloads/theory-of-commutative-algebra-11.tex:3891-4083`
- Source excerpt: `\subsection{Example over the dual numbers} Let \[ A=k[\varepsilon]/(\varepsilon^2), \qquad k=A/(\varepsilon). \] This ring is not regular, and here higher Tor groups do not stop in degree \(1\). Consider the infinite complex \[ \cdots \xrightarrow{\cdot \varepsilon} A \xrightarrow{\cdot \varepsilon} A \xrightarrow{\cdot \varepsilon} A \to k\to 0. \] This is a free resolution of \(k\). Indeed, in \(A\), \[ \ker(\cdot \varepsilon)=(\varepsilon) \] and \[ \operatorname{im}(\cdot \varepsilon)=(\varepsilon), \] because \(\varepsilon^2=0\). Now tensor this resolution with \(k\). Since \(\varepsilon\) acts as \(0\) on \(k\), every differential becomes \(0\). So we get \[ \cdots \to k \xrightarrow{0} k \xrightarrow{0} k \xrightarrow{0} k \to 0. \] Therefore every homology group is \(k\): \[ \opera ...`
- Companion excerpt: `\label{prob:cp-v-0114} Let \[ 0\to A'\to A\to A''\to0 \] be a short exact sequence of \(R\)-modules. Explain why the long exact sequence of \(\operatorname{Tor}\) measures the failure of tensor product to be left exact, while the long exact sequence of \(\operatorname{Ext}\) measures the failure of \(\operatorname{Hom}\) to be right exact.`

