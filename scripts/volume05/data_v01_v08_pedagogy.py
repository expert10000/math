DATA = {'V/01': {'examples': [{'after_section': 2,
                        'body': 'In $R=\\mathbb Z/12\\mathbb Z$, the ideal $(4)$ is $\\{0,4,8\\}$. The reduction map '
                                '$R\\to\\mathbb Z/4\\mathbb Z$ is surjective with kernel $(4)$, so $R/(4)\\cong\\mathbb '
                                'Z/4\\mathbb Z$.',
                        'title': 'Quotient arithmetic'},
                       {'after_section': 5,
                        'body': 'In $k[x,y]/(x,y^2)$ every class has a unique representative $a+by$. The class of $y$ is nonzero '
                                'but satisfies $y^2=0$, so the quotient exhibits a nilpotent direction explicitly.',
                        'title': 'Polynomial quotient'},
                       {'after_section': 7,
                        'body': 'Evaluation at $1$ gives $\\varphi:k[x]\\to k$. Polynomial division shows $\\ker\\varphi=(x-1)$, '
                                'and constants show surjectivity. Hence $k[x]/(x-1)\\cong k$.',
                        'title': 'Evaluation kernel'}],
          'exercises': {'application': [{'hint': 'Translate the situation into kernels, generated ideals, and quotient universal '
                                                 'properties.',
                                         'prompt': 'Explain quotient rings as arithmetic modulo $n$.',
                                         'solution': 'Equality of cosets is exactly congruence because differences lie in $(n)$.',
                                         'title': 'Congruence model'},
                                        {'hint': 'Translate the situation into kernels, generated ideals, and quotient universal '
                                                 'properties.',
                                         'prompt': 'Interpret $k[x,y]/(y)$.',
                                         'solution': 'It is the coordinate ring obtained by imposing the equation $y=0$.',
                                         'title': 'Coordinate restriction'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Commutative rings' and 'Examples' in one rigorous "
                                                 'argument.',
                                       'solution': 'The argument begins with A commutative ring has associative addition and '
                                                   'multiplication, a multiplicative identity, and commutative multiplication. '
                                                   'It then uses the later viewpoint: Polynomial rings, integer residue rings, '
                                                   'coordinate-style quotients, and product rings provide the main laboratory. '
                                                   'The bridge is supplied by the structural theorems proved in the chapter.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': 'Use one of the explicit counterexamples in the graded set and compare it with '
                                               'the theorem statement.',
                                       'prompt': 'Choose one theorem from the chapter and explain precisely what can fail if one '
                                                 'key hypothesis is removed.',
                                       'solution': "The theorem hypotheses are essential because the chapter's quotient, "
                                                   'localization, exactness, or finiteness mechanism can fail outside them. A '
                                                   'correct answer identifies the dropped hypothesis and exhibits a concrete '
                                                   'failure.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: For a ring homomorphism $\\varphi:A\\to B$, there is a natural isomorphism '
                                             '$A/\\ker\\varphi\\cong\\operatorname{im}\\varphi$.',
                                   'solution': 'Send the class of $a$ to $\\varphi(a)$. Equality of images is exactly equality '
                                               'modulo the kernel, so the map is well-defined and injective; surjectivity onto '
                                               'the image is immediate.',
                                   'title': 'First isomorphism theorem proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: Ideals of $A/I$ are in inclusion-preserving bijection with ideals '
                                             '$J\\subset A$ satisfying $I\\subseteq J$.',
                                   'solution': 'Take inverse image under the quotient map in one direction and quotient $J/I$ in '
                                               'the other. The two constructions are inverse by direct inspection.',
                                   'title': 'Correspondence theorem proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: If $I\\subseteq J\\subseteq A$ are ideals, then $(A/I)/(J/I)\\cong A/J$.',
                                   'solution': 'Apply the first isomorphism theorem to the homomorphism $A/I\\to A/J$ sending '
                                               '$a+I$ to $a+J$; its kernel is $J/I$.',
                                   'title': 'Third isomorphism theorem proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining First isomorphism theorem with Correspondence '
                                             'theorem. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes First isomorphism theorem and then applies '
                                               'Correspondence theorem; the conclusion follows after checking the shared '
                                               'hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use kernels, generated ideals, and quotient universal properties.',
                                      'prompt': 'Find $(18,30)$ in $\\mathbb Z$.',
                                      'solution': '$(18,30)=(6)$.',
                                      'title': 'Integer generated ideal'},
                                     {'hint': 'Use kernels, generated ideals, and quotient universal properties.',
                                      'prompt': 'How many classes are in $\\mathbb Z/(15)$?',
                                      'solution': 'There are $15$ classes.',
                                      'title': 'Residue quotient'},
                                     {'hint': 'Use kernels, generated ideals, and quotient universal properties.',
                                      'prompt': 'Reduce $x^4+2x+3$ modulo $(x^2)$.',
                                      'solution': 'The class is $2x+3$.',
                                      'title': 'Polynomial reduction'},
                                     {'hint': 'Use kernels, generated ideals, and quotient universal properties.',
                                      'prompt': 'Find the kernel of $\\mathbb Z\\to\\mathbb Z/7\\mathbb Z$.',
                                      'solution': 'The kernel is $7\\mathbb Z$.',
                                      'title': 'Kernel'},
                                     {'hint': 'Use kernels, generated ideals, and quotient universal properties.',
                                      'prompt': 'Describe $(x,2)$ in $\\mathbb Z[x]$.',
                                      'solution': 'It consists of $xf(x)+2g(x)$.',
                                      'title': 'Generated ideal'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: $2\\mathbb Z\\cup3\\mathbb Z$ is an ideal.',
                                  'solution': 'False: $2$ and $3$ belong but $5$ does not.',
                                  'title': 'Union test'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every ideal of $k[x,y]$ is principal.',
                                  'solution': 'False: $(x,y)$ is not principal.',
                                  'title': 'Principal ideal test'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: $\\mathbb Z/6\\mathbb Z$ is a field.',
                                  'solution': 'False: $2\\cdot3=0$ modulo $6$.',
                                  'title': 'Field quotient test'}]}},
 'V/02': {'examples': [{'after_section': 2,
                        'body': 'The zero ideal in $\\mathbb Z$ is prime because $\\mathbb Z$ is a domain, but it is not maximal '
                                'since $(0)\\subsetneq(2)\\subsetneq\\mathbb Z$.',
                        'title': 'Prime but not maximal'},
                       {'after_section': 5,
                        'body': 'In $k[x,y]$, evaluation at $(a,b)$ has kernel $(x-a,y-b)$ and image $k$. The quotient is a '
                                'field, so the kernel is maximal and therefore prime.',
                        'title': 'Maximal evaluation ideal'},
                       {'after_section': 7,
                        'body': 'The ideal $(6)$ is not prime because $2\\cdot3\\in(6)$ while neither factor belongs to $(6)$. '
                                'Equivalently, $\\mathbb Z/6\\mathbb Z$ is not a domain.',
                        'title': 'Nonprime integer ideal'}],
          'exercises': {'application': [{'hint': 'Translate the situation into prime and maximal quotient criteria.',
                                         'prompt': 'Interpret $(x-a,y-b)$ geometrically.',
                                         'solution': 'It records evaluation at the affine point $(a,b)$.',
                                         'title': 'Affine point'},
                                        {'hint': 'Translate the situation into prime and maximal quotient criteria.',
                                         'prompt': 'Explain why prime ideals model irreducible algebraic pieces.',
                                         'solution': 'The quotient domain has no nontrivial product equal to zero.',
                                         'title': 'Irreducible component'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Prime ideals' and 'Examples' in one rigorous "
                                                 'argument.',
                                       'solution': 'The argument begins with A proper ideal $\\mathfrak p$ is prime when '
                                                   '$ab\\in\\mathfrak p$ implies $a\\in\\mathfrak p$ or $b\\in\\mathfrak p$. It '
                                                   'then uses the later viewpoint: Prime and maximal ideals in $\\mathbb Z$, '
                                                   'polynomial rings, product rings, and localizations illustrate the '
                                                   'definitions. The bridge is supplied by the structural theorems proved in the '
                                                   'chapter.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': 'Use one of the explicit counterexamples in the graded set and compare it with '
                                               'the theorem statement.',
                                       'prompt': 'Choose one theorem from the chapter and explain precisely what can fail if one '
                                                 'key hypothesis is removed.',
                                       'solution': "The theorem hypotheses are essential because the chapter's quotient, "
                                                   'localization, exactness, or finiteness mechanism can fail outside them. A '
                                                   'correct answer identifies the dropped hypothesis and exhibits a concrete '
                                                   'failure.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: A proper ideal $\\mathfrak p$ is prime iff $A/\\mathfrak p$ is an integral '
                                             'domain.',
                                   'solution': 'The zero-divisor condition in the quotient is exactly the statement that '
                                               '$ab\\in\\mathfrak p$ forces one factor into $\\mathfrak p$.',
                                   'title': 'Prime quotient criterion proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: A proper ideal $\\mathfrak m$ is maximal iff $A/\\mathfrak m$ is a field.',
                                   'solution': 'Ideals in $A/\\mathfrak m$ correspond to ideals of $A$ containing $\\mathfrak '
                                               'm$. A quotient is a field exactly when its only ideals are zero and the whole '
                                               'ring.',
                                   'title': 'Maximal quotient criterion proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: Every maximal ideal in a commutative ring with identity is prime.',
                                   'solution': 'The quotient by a maximal ideal is a field, hence a domain; apply the prime '
                                               'quotient criterion.',
                                   'title': 'Maximal implies prime proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Prime quotient criterion with Maximal '
                                             'quotient criterion. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Prime quotient criterion and then applies '
                                               'Maximal quotient criterion; the conclusion follows after checking the shared '
                                               'hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use prime and maximal quotient criteria.',
                                      'prompt': 'Decide whether $(7)$ is prime in $\\mathbb Z$.',
                                      'solution': 'Yes, because $\\mathbb Z/7\\mathbb Z$ is a domain.',
                                      'title': 'Prime integer ideal'},
                                     {'hint': 'Use prime and maximal quotient criteria.',
                                      'prompt': 'Decide whether $(7)$ is maximal in $\\mathbb Z$.',
                                      'solution': 'Yes, because the quotient is a field.',
                                      'title': 'Maximal integer ideal'},
                                     {'hint': 'Use prime and maximal quotient criteria.',
                                      'prompt': 'Decide whether $(x-2)$ is maximal in $\\mathbb Q[x]$.',
                                      'solution': 'Yes, the quotient is $\\mathbb Q$.',
                                      'title': 'Polynomial maximal ideal'},
                                     {'hint': 'Use prime and maximal quotient criteria.',
                                      'prompt': 'Decide whether $(xy)$ is prime in $k[x,y]$.',
                                      'solution': 'No: the classes of $x$ and $y$ are nonzero zero divisors.',
                                      'title': 'Prime failure'},
                                     {'hint': 'Use prime and maximal quotient criteria.',
                                      'prompt': 'Give a prime chain in $k[x,y]$.',
                                      'solution': '$(0)\\subset(x)\\subset(x,y)$.',
                                      'title': 'Prime chain'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every prime ideal is maximal.',
                                  'solution': 'False: $(x)$ is prime but not maximal in $k[x,y]$.',
                                  'title': 'Prime maximality'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: The zero ideal is prime in every ring.',
                                  'solution': 'False: it is prime exactly in domains.',
                                  'title': 'Zero prime'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: The inverse image of a maximal ideal is always maximal.',
                                  'solution': 'False without surjectivity; use $\\mathbb Z\\hookrightarrow\\mathbb Q$.',
                                  'title': 'Preimage maximality'}]}},
 'V/03': {'examples': [{'after_section': 2,
                        'body': 'For $I=(12)\\subset\\mathbb Z$, an integer has a power in $I$ exactly when it is divisible by '
                                'both $2$ and $3$. Thus $\\sqrt{(12)}=(6)$.',
                        'title': 'Radical of an integer ideal'},
                       {'after_section': 5,
                        'body': 'In $k[x]/(x^3)$ the class of $x$ is nonzero and nilpotent. The nilradical is $(x)$ and the '
                                'reduced quotient is $k$.',
                        'title': 'Nilpotent quotient'},
                       {'after_section': 7,
                        'body': 'For $I=(x^2,y^3)\\subset k[x,y]$, both $x$ and $y$ lie in $\\sqrt I$, and a polynomial with '
                                'nonzero constant term cannot have a power in $I$. Hence $\\sqrt I=(x,y)$.',
                        'title': 'Monomial radical'}],
          'exercises': {'application': [{'hint': 'Translate the situation into radicals, nilpotents, and reduced quotients.',
                                         'prompt': 'Explain $R/\\sqrt{(0)}$.',
                                         'solution': 'It removes exactly nilpotent elements.',
                                         'title': 'Reduced structure'},
                                        {'hint': 'Translate the situation into radicals, nilpotents, and reduced quotients.',
                                         'prompt': 'Why does replacing $I$ by $\\sqrt I$ preserve common zeros?',
                                         'solution': 'An element and every positive power have the same zero set.',
                                         'title': 'Zero sets'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Nilpotent elements' and 'Examples' in one rigorous "
                                                 'argument.',
                                       'solution': 'The argument begins with An element $a$ is nilpotent if $a^n=0$ for some '
                                                   'positive integer $n$. It then uses the later viewpoint: Powers of principal '
                                                   'ideals, square-zero extensions, and polynomial quotients show how radicals '
                                                   'discard nilpotent thickening. The bridge is supplied by the structural '
                                                   'theorems proved in the chapter.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': 'Use one of the explicit counterexamples in the graded set and compare it with '
                                               'the theorem statement.',
                                       'prompt': 'Choose one theorem from the chapter and explain precisely what can fail if one '
                                                 'key hypothesis is removed.',
                                       'solution': "The theorem hypotheses are essential because the chapter's quotient, "
                                                   'localization, exactness, or finiteness mechanism can fail outside them. A '
                                                   'correct answer identifies the dropped hypothesis and exhibits a concrete '
                                                   'failure.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: For every ideal $I$, the set $\\sqrt I$ is an ideal containing $I$.',
                                   'solution': 'Closure under multiplication is immediate. If $a^m,b^n\\in I$, then every term '
                                               'in $(a+b)^{m+n}$ contains either at least $m$ copies of $a$ or at least $n$ '
                                               'copies of $b$, hence lies in $I$.',
                                   'title': 'Radical is an ideal proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: The nilradical of $A/I$ is $\\sqrt I/I$.',
                                   'solution': 'The class of $a$ is nilpotent modulo $I$ exactly when some power $a^n$ lies in '
                                               '$I$.',
                                   'title': 'Quotient nilradical identity proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: $\\sqrt I$ equals the intersection of all prime ideals containing $I$.',
                                   'solution': 'One inclusion follows because primes are radical. For the reverse, if '
                                               '$a\\notin\\sqrt I$, localize the quotient $A/I$ at powers of $a$ and choose a '
                                               'maximal ideal there; its contraction is a prime containing $I$ but avoiding $a$.',
                                   'title': 'Radical as intersection of primes proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Radical is an ideal with Quotient nilradical '
                                             'identity. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Radical is an ideal and then applies Quotient '
                                               'nilradical identity; the conclusion follows after checking the shared '
                                               'hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use radicals, nilpotents, and reduced quotients.',
                                      'prompt': 'Compute $\\sqrt{(72)}$ in $\\mathbb Z$.',
                                      'solution': 'The radical is $(6)$.',
                                      'title': 'Integer radical'},
                                     {'hint': 'Use radicals, nilpotents, and reduced quotients.',
                                      'prompt': 'Find the nilpotency index of $x$ in $k[x]/(x^4)$.',
                                      'solution': 'It is $4$.',
                                      'title': 'Nilpotency index'},
                                     {'hint': 'Use radicals, nilpotents, and reduced quotients.',
                                      'prompt': 'Reduce $k[x]/(x^5)$.',
                                      'solution': 'The reduced quotient is $k$.',
                                      'title': 'Reduced quotient'},
                                     {'hint': 'Use radicals, nilpotents, and reduced quotients.',
                                      'prompt': 'Is $xy\\in\\sqrt{(x^2y^2)}$?',
                                      'solution': 'Yes, because $(xy)^2=x^2y^2$.',
                                      'title': 'Radical membership'},
                                     {'hint': 'Use radicals, nilpotents, and reduced quotients.',
                                      'prompt': 'Find the nilradical of $k\\times k[t]/(t^2)$.',
                                      'solution': 'It is $0\\times(t)$.',
                                      'title': 'Product nilradical'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: $(x^2)$ is radical in $k[x]$.',
                                  'solution': 'False because $x^2$ lies in the ideal but $x$ does not.',
                                  'title': 'Radical ideal'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every reduced ring is a domain.',
                                  'solution': 'False: $k\\times k$ is reduced with zero divisors.',
                                  'title': 'Reduced domain'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every zero divisor is nilpotent.',
                                  'solution': 'False: $(1,0)$ in $k\\times k$ is idempotent.',
                                  'title': 'Zero divisor nilpotent'}]}},
 'V/04': {'examples': [{'after_section': 2,
                        'body': 'The congruences $x\\equiv2\\pmod3$ and $x\\equiv4\\pmod5$ have the unique solution '
                                '$x\\equiv14\\pmod{15}$. This is the concrete form of $\\mathbb Z/15\\cong\\mathbb '
                                'Z/3\\times\\mathbb Z/5$.',
                        'title': 'Integer CRT'},
                       {'after_section': 5,
                        'body': 'In $\\mathbb Z/12\\cong\\mathbb Z/3\\times\\mathbb Z/4$, the classes $4$ and $9$ correspond to '
                                '$(1,0)$ and $(0,1)$. They are orthogonal idempotents and sum to $1$.',
                        'title': 'Orthogonal idempotents'},
                       {'after_section': 7,
                        'body': 'Since $(x)+(x-1)=k[x]$, one has $k[x]/(x(x-1))\\cong k\\times k$. A polynomial class is '
                                'determined by its values at $0$ and $1$.',
                        'title': 'Polynomial CRT'}],
          'exercises': {'application': [{'hint': 'Translate the situation into comaximal ideals and Chinese remainder '
                                                 'decompositions.',
                                         'prompt': 'Why can CRT split modular arithmetic into components?',
                                         'solution': 'The product-ring isomorphism makes operations componentwise.',
                                         'title': 'Parallel arithmetic'},
                                        {'hint': 'Translate the situation into comaximal ideals and Chinese remainder '
                                                 'decompositions.',
                                         'prompt': 'Interpret CRT for distinct linear polynomial factors.',
                                         'solution': 'It prescribes independent values at distinct points.',
                                         'title': 'Interpolation'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Comaximal ideals' and 'Decomposition philosophy' in "
                                                 'one rigorous argument.',
                                       'solution': 'The argument begins with Ideals $I,J$ are comaximal when $I+J=A$. It then '
                                                   'uses the later viewpoint: Product rings are algebraic manifestations of '
                                                   'independent components. The bridge is supplied by the structural theorems '
                                                   'proved in the chapter.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': 'Use one of the explicit counterexamples in the graded set and compare it with '
                                               'the theorem statement.',
                                       'prompt': 'Choose one theorem from the chapter and explain precisely what can fail if one '
                                                 'key hypothesis is removed.',
                                       'solution': "The theorem hypotheses are essential because the chapter's quotient, "
                                                   'localization, exactness, or finiteness mechanism can fail outside them. A '
                                                   'correct answer identifies the dropped hypothesis and exhibits a concrete '
                                                   'failure.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: If $I+J=A$, then $A/(I\\cap J)\\cong A/I\\times A/J$.',
                                   'solution': 'The natural map has kernel $I\\cap J$. For surjectivity choose $u\\in I,v\\in J$ '
                                               'with $u+v=1$; the element $bv+au$ has prescribed residues $a$ modulo $I$ and $b$ '
                                               'modulo $J$.',
                                   'title': 'Two-ideal Chinese remainder theorem proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: If $I+J=A$, then $I\\cap J=IJ$.',
                                   'solution': 'The inclusion $IJ\\subseteq I\\cap J$ is automatic. If $x\\in I\\cap J$ and '
                                               '$1=u+v$ with $u\\in I,v\\in J$, then $x=xu+xv$ lies in $IJ$.',
                                   'title': 'Intersection-product equality proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: If $I_1,\\dots,I_n$ are pairwise comaximal, then $A/(I_1\\cdots '
                                             'I_n)\\cong\\prod_i A/I_i$.',
                                   'solution': 'Induct on $n$, using that the product of the first $n-1$ ideals is comaximal '
                                               'with $I_n$, then apply the two-ideal theorem and the product-intersection '
                                               'identity.',
                                   'title': 'Finite CRT proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Two-ideal Chinese remainder theorem with '
                                             'Intersection-product equality. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Two-ideal Chinese remainder theorem and then '
                                               'applies Intersection-product equality; the conclusion follows after checking the '
                                               'shared hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use comaximal ideals and Chinese remainder decompositions.',
                                      'prompt': 'Solve $x\\equiv1\\pmod4$ and $x\\equiv2\\pmod3$.',
                                      'solution': '$x\\equiv5\\pmod{12}$.',
                                      'title': 'Two congruences'},
                                     {'hint': 'Use comaximal ideals and Chinese remainder decompositions.',
                                      'prompt': 'Decompose $\\mathbb Z/35\\mathbb Z$.',
                                      'solution': '$\\mathbb Z/35\\cong\\mathbb Z/5\\times\\mathbb Z/7$.',
                                      'title': 'CRT decomposition'},
                                     {'hint': 'Use comaximal ideals and Chinese remainder decompositions.',
                                      'prompt': 'Are $(x)$ and $(x-2)$ comaximal when $2$ is invertible?',
                                      'solution': 'Yes.',
                                      'title': 'Comaximality'},
                                     {'hint': 'Use comaximal ideals and Chinese remainder decompositions.',
                                      'prompt': 'Compute $(3)\\cap(5)$ in $\\mathbb Z$.',
                                      'solution': 'It is $(15)$.',
                                      'title': 'Intersection'},
                                     {'hint': 'Use comaximal ideals and Chinese remainder decompositions.',
                                      'prompt': 'Find the class mod $15$ corresponding to $(1,0)$ mod $(3,5)$.',
                                      'solution': 'The class $10$.',
                                      'title': 'Idempotent'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: $\\mathbb Z/8\\cong\\mathbb Z/4\\times\\mathbb Z/2$.',
                                  'solution': 'False: the ideals are not comaximal.',
                                  'title': 'Noncomaximal CRT'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: $I\\cap J=IJ$ for all ideals.',
                                  'solution': 'False: take $I=J=(2)$ in $\\mathbb Z$.',
                                  'title': 'Intersection product'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: CRT works unchanged with repeated equal proper ideals.',
                                  'solution': 'False: the diagonal map is not surjective.',
                                  'title': 'Repeated factors'}]}},
 'V/05': {'examples': [{'after_section': 2,
                        'body': 'The set $S=\\{1,2,4,8,\\ldots\\}$ is multiplicatively closed. Inverting it produces $\\mathbb '
                                'Z[1/2]$, where $2$ is a unit but $3$ need not be.',
                        'title': 'Powers of two'},
                       {'after_section': 5,
                        'body': 'If $P$ is prime, then $R\\setminus P$ is multiplicatively closed. Otherwise two elements '
                                'outside $P$ could multiply into $P$, contradicting primality.',
                        'title': 'Prime complement'},
                       {'after_section': 7,
                        'body': 'For $S=\\{1,x,x^2,\\ldots\\}\\subset k[x,y]$, every ideal meeting $S$ becomes the unit ideal '
                                'after localization, while ideals disjoint from $S$ can survive.',
                        'title': 'Denominator saturation'}],
          'exercises': {'application': [{'hint': 'Translate the situation into multiplicative systems and denominator control.',
                                         'prompt': 'What does choosing $S$ control?',
                                         'solution': 'It specifies exactly which elements are forced to become units.',
                                         'title': 'Denominator design'},
                                        {'hint': 'Translate the situation into multiplicative systems and denominator control.',
                                         'prompt': 'Why use $S=R\\setminus P$?',
                                         'solution': 'It focuses algebra at $P$ by inverting everything outside it.',
                                         'title': 'Local study'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Multiplicative subsets' and 'Geometric preview' in "
                                                 'one rigorous argument.',
                                       'solution': 'The argument begins with A multiplicative set $S$ contains $1$ and is closed '
                                                   'under products; usually $0\\notin S$ for nontrivial localization. It then '
                                                   'uses the later viewpoint: Choosing $S=\\{1,f,f^2,\\dots\\}$ corresponds to '
                                                   'restricting attention to where $f$ is invertible. The bridge is supplied by '
                                                   'the structural theorems proved in the chapter.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': 'Use one of the explicit counterexamples in the graded set and compare it with '
                                               'the theorem statement.',
                                       'prompt': 'Choose one theorem from the chapter and explain precisely what can fail if one '
                                                 'key hypothesis is removed.',
                                       'solution': "The theorem hypotheses are essential because the chapter's quotient, "
                                                   'localization, exactness, or finiteness mechanism can fail outside them. A '
                                                   'correct answer identifies the dropped hypothesis and exhibits a concrete '
                                                   'failure.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: If $I$ is maximal among ideals disjoint from a multiplicative set $S$, then '
                                             '$I$ is prime.',
                                   'solution': 'If $ab\\in I$ with $a,b\\notin I$, then both $I+(a)$ and $I+(b)$ meet $S$. '
                                               'Multiplying corresponding elements of $S$ yields an element of $I+(ab)\\subseteq '
                                               'I$, contradicting disjointness.',
                                   'title': 'Maximal disjoint ideal is prime proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: If $\\mathfrak p$ is prime, then $A\\setminus\\mathfrak p$ is '
                                             'multiplicatively closed.',
                                   'solution': 'If $a,b\\notin\\mathfrak p$ but $ab\\in\\mathfrak p$, primality would force one '
                                               'factor into $\\mathfrak p$.',
                                   'title': 'Complement of prime is multiplicative proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: For any $f\\in A$, $S=\\{1,f,f^2,\\dots\\}$ is multiplicative.',
                                   'solution': 'The product $f^m f^n=f^{m+n}$ remains in the set and $1=f^0$ is included.',
                                   'title': 'Powers form a multiplicative set proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Maximal disjoint ideal is prime with '
                                             'Complement of prime is multiplicative. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Maximal disjoint ideal is prime and then applies '
                                               'Complement of prime is multiplicative; the conclusion follows after checking the '
                                               'shared hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use multiplicative systems and denominator control.',
                                      'prompt': 'Is the set of nonzero integers multiplicatively closed?',
                                      'solution': 'Yes.',
                                      'title': 'Closure'},
                                     {'hint': 'Use multiplicative systems and denominator control.',
                                      'prompt': 'List $1,6,6^2,6^3$.',
                                      'solution': '$1,6,36,216$.',
                                      'title': 'Generated system'},
                                     {'hint': 'Use multiplicative systems and denominator control.',
                                      'prompt': 'Is $\\mathbb Z\\setminus(5)$ multiplicatively closed?',
                                      'solution': 'Yes.',
                                      'title': 'Prime complement'},
                                     {'hint': 'Use multiplicative systems and denominator control.',
                                      'prompt': 'What if $0\\in S$?',
                                      'solution': 'The localization is the zero ring.',
                                      'title': 'Zero denominator'},
                                     {'hint': 'Use multiplicative systems and denominator control.',
                                      'prompt': 'If $I\\cap S\\ne\\varnothing$, compute $S^{-1}I$.',
                                      'solution': 'It is $S^{-1}R$.',
                                      'title': 'Meeting ideal'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: The complement of every proper ideal is multiplicatively closed.',
                                  'solution': 'False; the ideal must be prime.',
                                  'title': 'Ideal complement'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: The set of nonunits is always a multiplicative system.',
                                  'solution': 'Not as a general structural replacement for prime complements; local-ring '
                                              'behavior is special.',
                                  'title': 'Nonunits'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: A prime meeting $S$ survives as a proper prime after localization.',
                                  'solution': 'False: it extends to the whole localized ring.',
                                  'title': 'Prime visibility'}]}},
 'V/06': {'examples': [{'after_section': 2,
                        'body': 'Localizing $\\mathbb Z$ at powers of $6$ gives $\\mathbb Z[1/6]$. Fractions with denominators '
                                'dividing powers of $6$ occur, while $1/5$ does not.',
                        'title': 'Integer localization'},
                       {'after_section': 5,
                        'body': 'In $k[x,y]_x$, $x$ is a unit, so $(x,y)$ becomes the whole ring. The ideal $(y)$ remains proper '
                                'and records the part visible where $x$ is invertible.',
                        'title': 'Principal localization'},
                       {'after_section': 7,
                        'body': 'The ring $\\mathbb Z_{(5)}$ consists of $a/b$ with $5\\nmid b$. Its unique maximal ideal '
                                'consists of fractions whose numerator is divisible by $5$.',
                        'title': 'Prime localization'}],
          'exercises': {'application': [{'hint': 'Translate the situation into fraction localization and its universal property.',
                                         'prompt': 'Interpret $R_f$ geometrically.',
                                         'solution': 'It describes the region where $f$ is nonzero.',
                                         'title': 'Principal open'},
                                        {'hint': 'Translate the situation into fraction localization and its universal property.',
                                         'prompt': 'Why use $\\mathbb Z_{(p)}$?',
                                         'solution': 'All integers prime to $p$ become units.',
                                         'title': 'Arithmetic near $p$'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Fraction construction' and 'Localization at a "
                                                 "prime' in one rigorous argument.",
                                       'solution': 'The argument begins with Elements of $S^{-1}A$ are fractions $a/s$ modulo '
                                                   'the relation generated by cross-multiplication after multiplying by a '
                                                   'further denominator. It then uses the later viewpoint: $A_{\\mathfrak p}$ '
                                                   'inverts everything outside $\\mathfrak p$ and is a local ring. The bridge is '
                                                   'supplied by the structural theorems proved in the chapter.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': 'Use one of the explicit counterexamples in the graded set and compare it with '
                                               'the theorem statement.',
                                       'prompt': 'Choose one theorem from the chapter and explain precisely what can fail if one '
                                                 'key hypothesis is removed.',
                                       'solution': "The theorem hypotheses are essential because the chapter's quotient, "
                                                   'localization, exactness, or finiteness mechanism can fail outside them. A '
                                                   'correct answer identifies the dropped hypothesis and exhibits a concrete '
                                                   'failure.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: If $\\varphi:A\\to B$ sends every $s\\in S$ to a unit, there is a unique '
                                             'map $\\widetilde\\varphi:S^{-1}A\\to B$ with '
                                             '$\\widetilde\\varphi(a/s)=\\varphi(a)\\varphi(s)^{-1}$.',
                                   'solution': 'The formula respects the localization equivalence relation and is forced by the '
                                               'requirement that denominators become inverses, giving existence and uniqueness.',
                                   'title': 'Universal property of localization proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: Prime ideals of $S^{-1}A$ are in bijection with prime ideals $\\mathfrak '
                                             'p\\subset A$ satisfying $\\mathfrak p\\cap S=\\varnothing$.',
                                   'solution': 'Contraction of a prime avoids units, hence avoids $S$. For a prime disjoint from '
                                               '$S$, its extension consists of fractions with numerator in the prime and is '
                                               'prime; extension and contraction are inverse.',
                                   'title': 'Prime correspondence proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: For an ideal $I$, $S^{-1}(A/I)\\cong S^{-1}A/S^{-1}I$ after replacing $S$ '
                                             'by its image in $A/I$.',
                                   'solution': 'Both rings satisfy the same universal property: maps out correspond to maps from '
                                               '$A$ killing $I$ and inverting $S$.',
                                   'title': 'Localization commutes with quotient proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Universal property of localization with Prime '
                                             'correspondence. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Universal property of localization and then '
                                               'applies Prime correspondence; the conclusion follows after checking the shared '
                                               'hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use fraction localization and its universal property.',
                                      'prompt': 'Is $2$ a unit in $\\mathbb Z[1/2]$?',
                                      'solution': 'Yes, inverse $1/2$.',
                                      'title': 'Unit'},
                                     {'hint': 'Use fraction localization and its universal property.',
                                      'prompt': 'Compute $(2)\\mathbb Z[1/2]$.',
                                      'solution': 'It is the whole ring.',
                                      'title': 'Localized ideal'},
                                     {'hint': 'Use fraction localization and its universal property.',
                                      'prompt': 'Describe denominators in $\\mathbb Z_{(7)}$.',
                                      'solution': 'They are integers not divisible by $7$.',
                                      'title': 'Prime denominators'},
                                     {'hint': 'Use fraction localization and its universal property.',
                                      'prompt': 'Find the inverse of $x^3$ in $k[x,y]_x$.',
                                      'solution': 'It is $x^{-3}$.',
                                      'title': 'Polynomial inverse'},
                                     {'hint': 'Use fraction localization and its universal property.',
                                      'prompt': 'When is $a/s=0$?',
                                      'solution': 'When some denominator $u\\in S$ satisfies $ua=0$.',
                                      'title': 'Zero fraction'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: $R\\to S^{-1}R$ is always injective.',
                                  'solution': 'False: denominator torsion can map to zero.',
                                  'title': 'Injectivity'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every prime extends to a proper prime.',
                                  'solution': 'False if the prime meets $S$.',
                                  'title': 'Prime extension'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: A nonzero ring can never localize to zero.',
                                  'solution': 'False if $0$ is inverted.',
                                  'title': 'Collapse'}]}},
 'V/07': {'examples': [{'after_section': 2,
                        'body': 'Localizing $\\mathbb Z/12$ at powers of $2$ kills the $4$-primary part and leaves the '
                                '$3$-primary information. This is a concrete instance of denominators annihilating torsion.',
                        'title': 'Localized torsion'},
                       {'after_section': 5,
                        'body': 'For $M=R/(f)$, localization at powers of $f$ gives $M_f=0$: the relation $f\\cdot1=0$ and '
                                'invertibility of $f$ force $1=0$.',
                        'title': 'Module vanishing'},
                       {'after_section': 7,
                        'body': 'Localizing $0\\to\\mathbb Z\\xrightarrow{\\cdot2}\\mathbb Z\\to\\mathbb Z/2\\to0$ at powers of '
                                '$2$ turns the first map into an isomorphism and the localized cokernel into zero.',
                        'title': 'Exact sequence localization'}],
          'exercises': {'application': [{'hint': 'Translate the situation into localization of modules and exactness.',
                                         'prompt': 'Why check modules at all prime localizations?',
                                         'solution': 'A module is zero exactly when all prime localizations vanish.',
                                         'title': 'Local checking'},
                                        {'hint': 'Translate the situation into localization of modules and exactness.',
                                         'prompt': 'Interpret $M_f$.',
                                         'solution': 'It is module data restricted to the principal open where $f$ is '
                                                     'invertible.',
                                         'title': 'Restriction'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Module fractions' and 'Local detection' in one "
                                                 'rigorous argument.',
                                       'solution': 'The argument begins with $S^{-1}M$ consists of symbols $m/s$ modulo the '
                                                   'expected denominator equivalence. It then uses the later viewpoint: Many '
                                                   'module properties can be tested after localizing at all prime or maximal '
                                                   'ideals. The bridge is supplied by the structural theorems proved in the '
                                                   'chapter.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': 'Use one of the explicit counterexamples in the graded set and compare it with '
                                               'the theorem statement.',
                                       'prompt': 'Choose one theorem from the chapter and explain precisely what can fail if one '
                                                 'key hypothesis is removed.',
                                       'solution': "The theorem hypotheses are essential because the chapter's quotient, "
                                                   'localization, exactness, or finiteness mechanism can fail outside them. A '
                                                   'correct answer identifies the dropped hypothesis and exhibits a concrete '
                                                   'failure.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: There is a natural isomorphism $S^{-1}A\\otimes_A M\\cong S^{-1}M$ sending '
                                             '$(a/s)\\otimes m$ to $am/s$.',
                                   'solution': 'The formula is balanced and induces a homomorphism. Its inverse sends $m/s$ to '
                                               '$(1/s)\\otimes m$; the two composites are identities.',
                                   'title': 'Tensor description of localization proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': "Prove: If $0\\to M'\\to M\\to M''\\to0$ is exact, then $0\\to S^{-1}M'\\to "
                                             "S^{-1}M\\to S^{-1}M''\\to0$ is exact.",
                                   'solution': 'Surjectivity is immediate on fractions. For injectivity or kernel equality, if a '
                                               'localized element maps to zero, some denominator annihilates the relevant '
                                               'numerator, allowing the numerator to be moved into the preceding module before '
                                               'localization.',
                                   'title': 'Exactness of localization proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: For $N\\subset M$, $S^{-1}(M/N)\\cong S^{-1}M/S^{-1}N$.',
                                   'solution': 'Apply exactness to $0\\to N\\to M\\to M/N\\to0$.',
                                   'title': 'Localization commutes with quotient proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Tensor description of localization with '
                                             'Exactness of localization. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Tensor description of localization and then '
                                               'applies Exactness of localization; the conclusion follows after checking the '
                                               'shared hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use localization of modules and exactness.',
                                      'prompt': 'Compute $S^{-1}0$.',
                                      'solution': 'It is zero.',
                                      'title': 'Zero module'},
                                     {'hint': 'Use localization of modules and exactness.',
                                      'prompt': 'Compute $(R/(x))_x$.',
                                      'solution': 'It is zero.',
                                      'title': 'Killed quotient'},
                                     {'hint': 'Use localization of modules and exactness.',
                                      'prompt': 'Compute $S^{-1}(R^3)$.',
                                      'solution': 'It is $(S^{-1}R)^3$.',
                                      'title': 'Free module'},
                                     {'hint': 'Use localization of modules and exactness.',
                                      'prompt': 'When does $m/1$ vanish?',
                                      'solution': 'When some $s\\in S$ annihilates $m$.',
                                      'title': 'Element vanishing'},
                                     {'hint': 'Use localization of modules and exactness.',
                                      'prompt': 'Identify $S^{-1}(M/N)$.',
                                      'solution': 'It is $S^{-1}M/S^{-1}N$.',
                                      'title': 'Quotient localization'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Localization preserves every nonzero module.',
                                  'solution': 'False: $(R/(f))_f=0$.',
                                  'title': 'Nonzero preservation'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: $M\\to S^{-1}M$ is always injective.',
                                  'solution': 'False when $M$ has $S$-torsion.',
                                  'title': 'Module injectivity'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Localization can create support at primes meeting $S$.',
                                  'solution': 'False; those primes disappear.',
                                  'title': 'New support'}]}},
 'V/08': {'examples': [{'after_section': 2,
                        'body': 'In $\\mathbb Z_{(5)}$, $a/b$ is a unit exactly when $5\\nmid a$. The fractions with numerator '
                                'divisible by $5$ form the unique maximal ideal.',
                        'title': 'Integers at a prime'},
                       {'after_section': 5,
                        'body': 'The ring $k[x]_{(x)}$ consists of $f/g$ with $g(0)\\ne0$. Its maximal ideal is generated by '
                                '$x$, and a fraction is a unit exactly when its residue at $x=0$ is nonzero.',
                        'title': 'Polynomial local ring'},
                       {'after_section': 7,
                        'body': 'In $k[x,y]_{(x,y)}$, every polynomial with nonzero constant term becomes a unit. The maximal '
                                'ideal is generated by the images of $x$ and $y$.',
                        'title': 'Two-variable local ring'}],
          'exercises': {'application': [{'hint': 'Translate the situation into local rings, maximal ideals, and unit criteria.',
                                         'prompt': 'Why are local rings adapted to local algebra?',
                                         'solution': 'They invert everything away from one chosen prime.',
                                         'title': 'Near one prime'},
                                        {'hint': 'Translate the situation into local rings, maximal ideals, and unit criteria.',
                                         'prompt': 'What does the residue field measure?',
                                         'solution': 'It records scalars at the chosen local point.',
                                         'title': 'Residue measurement'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Local rings' and 'Local-global philosophy' in one "
                                                 'rigorous argument.',
                                       'solution': 'The argument begins with A local ring has exactly one maximal ideal. It then '
                                                   'uses the later viewpoint: Properties of modules and ideals are often checked '
                                                   'prime by prime using these local rings. The bridge is supplied by the '
                                                   'structural theorems proved in the chapter.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': 'Use one of the explicit counterexamples in the graded set and compare it with '
                                               'the theorem statement.',
                                       'prompt': 'Choose one theorem from the chapter and explain precisely what can fail if one '
                                                 'key hypothesis is removed.',
                                       'solution': "The theorem hypotheses are essential because the chapter's quotient, "
                                                   'localization, exactness, or finiteness mechanism can fail outside them. A '
                                                   'correct answer identifies the dropped hypothesis and exhibits a concrete '
                                                   'failure.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: A commutative ring is local iff its nonunits form an ideal; in that case '
                                             'this ideal is the unique maximal ideal.',
                                   'solution': 'Every proper ideal consists of nonunits. If nonunits form an ideal, it is proper '
                                               'and contains every proper ideal, hence is uniquely maximal. Conversely, in a '
                                               'local ring every element outside the maximal ideal generates the unit ideal and '
                                               'is therefore a unit.',
                                   'title': 'Nonunits characterize local rings proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: For a prime $\\mathfrak p$, the ring $A_{\\mathfrak p}$ is local with '
                                             'unique maximal ideal $\\mathfrak p A_{\\mathfrak p}$.',
                                   'solution': 'Prime ideals of the localization correspond to primes of $A$ contained in '
                                               '$\\mathfrak p$. The extension of $\\mathfrak p$ contains every such prime and is '
                                               'therefore the unique maximal ideal.',
                                   'title': 'Prime localization is local proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: The residue field of $A_{\\mathfrak p}$ is canonically isomorphic to the '
                                             'fraction field of $A/\\mathfrak p$.',
                                   'solution': 'Modulo $\\mathfrak p A_{\\mathfrak p}$, numerators and denominators descend to '
                                               '$A/\\mathfrak p$, and every denominator outside $\\mathfrak p$ becomes a nonzero '
                                               'class, hence invertible in the fraction field.',
                                   'title': 'Residue field identification proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Nonunits characterize local rings with Prime '
                                             'localization is local. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Nonunits characterize local rings and then '
                                               'applies Prime localization is local; the conclusion follows after checking the '
                                               'shared hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use local rings, maximal ideals, and unit criteria.',
                                      'prompt': 'Is $3/7$ a unit in $\\mathbb Z_{(5)}$?',
                                      'solution': 'Yes.',
                                      'title': 'Unit test'},
                                     {'hint': 'Use local rings, maximal ideals, and unit criteria.',
                                      'prompt': 'Is $10/3$ a unit in $\\mathbb Z_{(5)}$?',
                                      'solution': 'No.',
                                      'title': 'Nonunit test'},
                                     {'hint': 'Use local rings, maximal ideals, and unit criteria.',
                                      'prompt': 'Find the maximal ideal of $k[x]_{(x)}$.',
                                      'solution': 'It is $(x)k[x]_{(x)}$.',
                                      'title': 'Maximal ideal'},
                                     {'hint': 'Use local rings, maximal ideals, and unit criteria.',
                                      'prompt': 'Find the residue field of $\\mathbb Z_{(p)}$.',
                                      'solution': 'It is $\\mathbb F_p$.',
                                      'title': 'Residue field'},
                                     {'hint': 'Use local rings, maximal ideals, and unit criteria.',
                                      'prompt': 'Find $k[x,y]_{(x,y)}/(x,y)$.',
                                      'solution': 'It is $k$.',
                                      'title': 'Polynomial residue'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: A ring with two distinct maximal ideals is local.',
                                  'solution': 'False.',
                                  'title': 'Two maximals'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: A local ring has no nonmaximal prime ideals.',
                                  'solution': 'False.',
                                  'title': 'Prime spectrum'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: An element in the maximal ideal can be a unit.',
                                  'solution': 'False in a local ring.',
                                  'title': 'Unit residue'}]}}}
