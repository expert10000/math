DATA = {'V/19': {'examples': [{'after_section': 2,
                        'body': 'Let $A=k[t^2,t^3]\\subset k[t]$. The element $t$ is integral over $A$ because it satisfies the monic '
                                'equation $X^2-t^2=0$ with coefficient $t^2\\in A$.',
                        'title': 'Integral element over a subring'},
                       {'after_section': 5,
                        'body': 'The element $i$ is integral over $\\mathbb Z$ because it satisfies $X^2+1=0$. Consequently every '
                                'element of $\\mathbb Z[i]$ is integral over $\\mathbb Z$.',
                        'title': 'Gaussian integers'},
                       {'after_section': 7,
                        'body': 'If $b$ is integral over $A$, then $A[b]$ is generated as an $A$-module by $1,b,\\ldots,b^{n-1}$ for '
                                'a monic equation of degree $n$. Integrality converts an algebra extension into finite module data.',
                        'title': 'Finite-module criterion'}],
          'exercises': {'application': [{'hint': 'Translate the question into monic equations and finite module criteria.',
                                         'prompt': 'Why does integrality correspond to finite algebra behavior?',
                                         'solution': 'An integral finite-type algebra is finite as a module.',
                                         'title': 'Finite maps'},
                                        {'hint': 'Translate the question into monic equations and finite module criteria.',
                                         'prompt': 'Why is $k[t]$ integral over the cusp ring $k[t^2,t^3]$?',
                                         'solution': 'The missing parameter satisfies a monic relation over the cusp ring.',
                                         'title': 'Eliminating parameters'}],
                        'challenge': [{'hint': 'State the relevant ring map, module map, or complex before applying the structural '
                                               'theorem.',
                                       'prompt': "Connect 'Integral elements' with 'Examples' in one rigorous argument.",
                                       'solution': 'The opening idea is: An element $b$ of an $A$-algebra $B$ is integral over $A$ if '
                                                   'it satisfies a monic polynomial with coefficients in $A$. The later viewpoint is: '
                                                   'Algebraic integers, roots of monic equations, and normalization rings illustrate '
                                                   'integral dependence. A complete solution identifies the structural theorem that '
                                                   'links these descriptions and checks its hypotheses.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': "Use one of the chapter's explicit computations or counterexamples as the test case.",
                                       'prompt': 'Choose one theorem from the chapter, remove one essential hypothesis, and exhibit '
                                                 'or explain a concrete failure.',
                                       'solution': 'The solution must name the removed hypothesis, show exactly which proof step '
                                                   'breaks, and give a concrete algebraic object where the claimed conclusion fails.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: For $b\\in B$, $b$ is integral over $A$ iff $A[b]$ is finitely generated as an '
                                             '$A$-module.',
                                   'solution': 'A monic equation expresses every high power of $b$ in terms of lower powers. '
                                               'Conversely, if finitely many powers generate an $A$-module stable under '
                                               'multiplication by $b$, the determinant trick gives a monic polynomial annihilating '
                                               '$b$.',
                                   'title': 'Finite module criterion proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: If $B$ is a finite $A$-module and an $A$-algebra, then every $b\\in B$ is '
                                             'integral over $A$.',
                                   'solution': 'Multiplication by $b$ is an $A$-linear endomorphism of the finite module $B$. Apply '
                                               'the determinant trick or Cayley--Hamilton to obtain a monic polynomial with '
                                               'coefficients in $A$ annihilating $b$.',
                                   'title': 'Finite algebra implies integral proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: If $B$ is integral over $A$ and $C$ integral over $B$, then $C$ is integral over '
                                             '$A$.',
                                   'solution': 'For $c\\in C$, its monic equation uses finitely many coefficients from $B$. Those '
                                               'coefficients generate a finite $A$-algebra because they are integral; adjoining $c$ '
                                               'is finite over that finite algebra, hence finite over $A$, so $c$ is integral over '
                                               '$A$.',
                                   'title': 'Transitivity of integrality proof'},
                                  {'hint': 'Apply the first theorem to obtain its structural description, then verify the second '
                                           "theorem's hypotheses.",
                                   'prompt': 'Prove a corollary that genuinely uses both Finite module criterion and Finite algebra '
                                             'implies integral.',
                                   'solution': 'A correct proof explicitly invokes both results, verifies the common hypotheses, and '
                                               'derives a new consequence rather than merely restating either theorem.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use monic equations and finite module criteria.',
                                      'prompt': 'Is $\\sqrt2$ integral over $\\mathbb Z$?',
                                      'solution': 'Yes, it satisfies $X^2-2=0$.',
                                      'title': 'Square root'},
                                     {'hint': 'Use monic equations and finite module criteria.',
                                      'prompt': 'Is $1/2$ integral over $\\mathbb Z$?',
                                      'solution': 'No.',
                                      'title': 'Rational'},
                                     {'hint': 'Use monic equations and finite module criteria.',
                                      'prompt': 'Is $t$ integral over $k[t^2,t^3]$?',
                                      'solution': 'Yes.',
                                      'title': 'Cusp parameter'},
                                     {'hint': 'Use monic equations and finite module criteria.',
                                      'prompt': 'If $b^3+a_2b^2+a_1b+a_0=0$, which powers generate $A[b]$?',
                                      'solution': '$1,b,b^2$.',
                                      'title': 'Finite algebra'},
                                     {'hint': 'Use monic equations and finite module criteria.',
                                      'prompt': 'If $C$ is integral over $B$ and $B$ over $A$, what follows?',
                                      'solution': '$C$ is integral over $A$.',
                                      'title': 'Transitivity'}],
                        'test': [{'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Every element of the fraction field of an integral domain is integral '
                                            'over the domain.',
                                  'solution': 'False: $1/2$ over $\\mathbb Z$.',
                                  'title': 'Arbitrary fraction'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: A root of any polynomial with coefficients in $A$ is automatically '
                                            'integral.',
                                  'solution': 'False; the polynomial must be monic or an equivalent criterion must apply.',
                                  'title': 'Monic condition'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: The sum and product of integral elements need not be integral.',
                                  'solution': 'False: integral elements form a subring.',
                                  'title': 'Sum product'}]}},
 'V/20': {'examples': [{'after_section': 2,
                        'body': 'The cusp ring $A=k[t^2,t^3]$ is not integrally closed in $k(t)$ because $t$ is integral over $A$ but '
                                '$t\\notin A$. Its normalization is $k[t]$.',
                        'title': 'Normalization of a cusp'},
                       {'after_section': 5,
                        'body': 'The integral closure of $\\mathbb Z$ in $\\mathbb Q$ is $\\mathbb Z$. A rational number integral '
                                'over $\\mathbb Z$ must have denominator $1$ by the rational-root argument for a monic integer '
                                'polynomial.',
                        'title': 'Integers in the rationals'},
                       {'after_section': 7,
                        'body': 'A unique factorization domain is integrally closed. Thus $k[x,y]$ is normal, while the singular cusp '
                                'subring $k[t^2,t^3]$ provides a standard nonnormal contrast.',
                        'title': 'Normal domain check'}],
          'exercises': {'application': [{'hint': 'Translate the question into integral closure and normalization.',
                                         'prompt': 'What does normalization do to the cusp parametrization?',
                                         'solution': 'It replaces the nonnormal cusp coordinate ring by the regular parameter ring '
                                                     '$k[t]$.',
                                         'title': 'Singularity repair'},
                                        {'hint': 'Translate the question into integral closure and normalization.',
                                         'prompt': 'Why study integral closure in number fields?',
                                         'solution': 'It identifies the natural ring of algebraic integers inside the field.',
                                         'title': 'Arithmetic closure'}],
                        'challenge': [{'hint': 'State the relevant ring map, module map, or complex before applying the structural '
                                               'theorem.',
                                       'prompt': "Connect 'Integrally closed domains' with 'Conductor' in one rigorous argument.",
                                       'solution': 'The opening idea is: A domain is integrally closed when every element of its '
                                                   'fraction field integral over the ring already lies in the ring. The later '
                                                   'viewpoint is: The conductor measures the largest ideal shared by a ring and its '
                                                   'normalization. A complete solution identifies the structural theorem that links '
                                                   'these descriptions and checks its hypotheses.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': "Use one of the chapter's explicit computations or counterexamples as the test case.",
                                       'prompt': 'Choose one theorem from the chapter, remove one essential hypothesis, and exhibit '
                                                 'or explain a concrete failure.',
                                       'solution': 'The solution must name the removed hypothesis, show exactly which proof step '
                                                   'breaks, and give a concrete algebraic object where the claimed conclusion fails.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: Every unique factorization domain is integrally closed in its fraction field.',
                                   'solution': 'Write an integral element as $a/b$ in lowest terms. A monic equation implies $a^n$ is '
                                               'divisible by $b$; coprimality and unique factorization force $b$ to be a unit.',
                                   'title': 'UFDs are integrally closed proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: If $B$ is the integral closure of a domain $A$ in a field extension and '
                                             '$S\\subset A$ is multiplicative, then $S^{-1}B$ is the integral closure of $S^{-1}A$ in '
                                             'the same localized field.',
                                   'solution': 'Localization preserves monic equations, giving one inclusion. For the reverse, clear '
                                               'finitely many denominators in a monic equation to show a suitable multiple of the '
                                               'element is integral over $A$, hence lies in $B$.',
                                   'title': 'Localization of integral closure proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: The normalization of $k[t^2,t^3]$ in $k(t)$ is $k[t]$.',
                                   'solution': 'The element $t$ is integral because it satisfies $X^2-t^2=0$ with coefficient $t^2$ '
                                               'in the subring. Since $k[t]$ is a PID and therefore integrally closed, no larger '
                                               'integral subring inside $k(t)$ is needed.',
                                   'title': 'Normalization of a cusp ring proof'},
                                  {'hint': 'Apply the first theorem to obtain its structural description, then verify the second '
                                           "theorem's hypotheses.",
                                   'prompt': 'Prove a corollary that genuinely uses both UFDs are integrally closed and Localization '
                                             'of integral closure.',
                                   'solution': 'A correct proof explicitly invokes both results, verifies the common hypotheses, and '
                                               'derives a new consequence rather than merely restating either theorem.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use integral closure and normalization.',
                                      'prompt': 'Find the integral closure of $\\mathbb Z$ in $\\mathbb Q$.',
                                      'solution': 'It is $\\mathbb Z$.',
                                      'title': 'Integer closure'},
                                     {'hint': 'Use integral closure and normalization.',
                                      'prompt': 'Find the normalization of $k[t^2,t^3]$ in $k(t)$.',
                                      'solution': 'It is $k[t]$.',
                                      'title': 'Cusp closure'},
                                     {'hint': 'Use integral closure and normalization.',
                                      'prompt': 'Is $k[x]$ integrally closed?',
                                      'solution': 'Yes.',
                                      'title': 'Polynomial ring'},
                                     {'hint': 'Use integral closure and normalization.',
                                      'prompt': 'Is every UFD integrally closed?',
                                      'solution': 'Yes.',
                                      'title': 'UFD'},
                                     {'hint': 'Use integral closure and normalization.',
                                      'prompt': 'Give an element witnessing nonnormality of $k[t^2,t^3]$.',
                                      'solution': 'The element $t$.',
                                      'title': 'Witness'}],
                        'test': [{'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Every integral domain is integrally closed.',
                                  'solution': 'False.',
                                  'title': 'Domain normality'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: The integral closure of a domain in its fraction field is always the '
                                            'whole fraction field.',
                                  'solution': 'False.',
                                  'title': 'Integral closure field'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Normalization never changes a ring.',
                                  'solution': 'False; it changes the cusp ring to $k[t]$.',
                                  'title': 'Normalization trivial'}]}},
 'V/21': {'examples': [{'after_section': 2,
                        'body': 'For a prime $p$, write a nonzero rational number as $p^nu/v$ with $p\\nmid uv$. Then $v_p$ equals '
                                '$n$. The valuation ring consists of rationals with nonnegative $p$-adic valuation.',
                        'title': 'The $p$-adic valuation'},
                       {'after_section': 5,
                        'body': 'On $k(t)$, the order of vanishing at $t=0$ defines a valuation. The local ring $k[t]_{(t)}$ is its '
                                'valuation ring: a rational function belongs exactly when it has no pole at $0$.',
                        'title': 'The $t$-adic valuation'},
                       {'after_section': 7,
                        'body': 'A subring $V$ of a field $K$ is a valuation ring exactly when for every nonzero $x\\in K$, either '
                                '$x\\in V$ or $x^{-1}\\in V$. This total comparability forces ideals of $V$ to be linearly ordered.',
                        'title': 'Either $x$ or $x^{-1}$'}],
          'exercises': {'application': [{'hint': 'Translate the question into valuations, units, and ordered ideals.',
                                         'prompt': 'What geometric information does a discrete valuation record?',
                                         'solution': 'It records order of zero or pole along a local parameter.',
                                         'title': 'Order of vanishing'},
                                        {'hint': 'Translate the question into valuations, units, and ordered ideals.',
                                         'prompt': 'Why are valuation rings useful for divisibility?',
                                         'solution': 'The valuation totally orders divisibility by comparing numerical values.',
                                         'title': 'Divisibility'}],
                        'challenge': [{'hint': 'State the relevant ring map, module map, or complex before applying the structural '
                                               'theorem.',
                                       'prompt': "Connect 'Valuations' with 'Integral closure criterion' in one rigorous argument.",
                                       'solution': 'The opening idea is: A valuation assigns ordered-group values compatible with '
                                                   'products and satisfying a triangle inequality for sums. The later viewpoint is: '
                                                   'Integral closure of a domain can be recovered as an intersection of valuation '
                                                   'rings containing it. A complete solution identifies the structural theorem that '
                                                   'links these descriptions and checks its hypotheses.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': "Use one of the chapter's explicit computations or counterexamples as the test case.",
                                       'prompt': 'Choose one theorem from the chapter, remove one essential hypothesis, and exhibit '
                                                 'or explain a concrete failure.',
                                       'solution': 'The solution must name the removed hypothesis, show exactly which proof step '
                                                   'breaks, and give a concrete algebraic object where the claimed conclusion fails.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: If $V$ is a valuation ring of a field, its nonunits form an ideal and hence the '
                                             'unique maximal ideal.',
                                   'solution': 'For nonunits $a,b$, compare $a/b$ or $b/a$ when both are nonzero; one divides the '
                                               'other, so their sum is a multiple of one nonunit. Multiplication by arbitrary ring '
                                               'elements preserves nonunits.',
                                   'title': 'Valuation rings are local proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: For nonzero $a,b\\in V$, either $(a)\\subseteq(b)$ or $(b)\\subseteq(a)$.',
                                   'solution': 'Apply the valuation-ring condition to $a/b$: if $a/b\\in V$, then $a\\in(b)$; '
                                               'otherwise $b/a\\in V$, so $b\\in(a)$.',
                                   'title': 'Principal ideals are totally ordered proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: A valuation ring $V$ is integrally closed in its fraction field.',
                                   'solution': 'If $x$ is integral over $V$ but $x\\notin V$, then $x^{-1}\\in V$ and is a nonunit. '
                                               'Divide a monic equation for $x$ by the highest power of $x$ to express $1$ as an '
                                               'element of the maximal ideal generated by powers of $x^{-1}$, contradiction.',
                                   'title': 'Valuation rings are integrally closed proof'},
                                  {'hint': 'Apply the first theorem to obtain its structural description, then verify the second '
                                           "theorem's hypotheses.",
                                   'prompt': 'Prove a corollary that genuinely uses both Valuation rings are local and Principal '
                                             'ideals are totally ordered.',
                                   'solution': 'A correct proof explicitly invokes both results, verifies the common hypotheses, and '
                                               'derives a new consequence rather than merely restating either theorem.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use valuations, units, and ordered ideals.',
                                      'prompt': 'Compute $v_2(24/5)$.',
                                      'solution': 'It is $3$.',
                                      'title': 'Valuation'},
                                     {'hint': 'Use valuations, units, and ordered ideals.',
                                      'prompt': 'Compute $v_3(2/27)$.',
                                      'solution': 'It is $-3$.',
                                      'title': 'Negative valuation'},
                                     {'hint': 'Use valuations, units, and ordered ideals.',
                                      'prompt': 'When is an element of a valuation ring a unit?',
                                      'solution': 'When its valuation is zero.',
                                      'title': 'Unit criterion'},
                                     {'hint': 'Use valuations, units, and ordered ideals.',
                                      'prompt': 'Which elements lie in the maximal ideal for a discrete valuation?',
                                      'solution': 'Those with positive valuation.',
                                      'title': 'Maximal ideal'},
                                     {'hint': 'Use valuations, units, and ordered ideals.',
                                      'prompt': 'What is the $t$-adic valuation of $t^4(1+t)/(1-t)$?',
                                      'solution': 'It is $4$.',
                                      'title': 'Parameter valuation'}],
                        'test': [{'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Every local domain is a valuation ring.',
                                  'solution': 'False; ideals in a valuation ring must be totally ordered.',
                                  'title': 'Two-variable local ring'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: An element of negative valuation lies in the valuation ring.',
                                  'solution': 'False.',
                                  'title': 'Negative member'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Ideals of a valuation ring can be incomparable.',
                                  'solution': 'False: they are linearly ordered.',
                                  'title': 'Ideal ordering'}]}},
 'V/22': {'examples': [{'after_section': 2,
                        'body': 'The sequence $0\\to\\mathbb Z\\xrightarrow{\\cdot2}\\mathbb Z\\to0$ is a chain complex. Its '
                                'degree-zero homology is $\\mathbb Z/2\\mathbb Z$, while the preceding homology vanishes because '
                                'multiplication by $2$ is injective.',
                        'title': 'A two-term complex'},
                       {'after_section': 5,
                        'body': 'In any chain complex, $d_{n-1}d_n=0$, so every boundary is automatically a cycle. Homology measures '
                                'the quotient of cycles by those cycles already explained as boundaries.',
                        'title': 'Boundary squared is zero'},
                       {'after_section': 7,
                        'body': 'For a short exact sequence $0\\to A\\to B\\to C\\to0$ regarded as a complex, every homology group '
                                'vanishes. Exactness is precisely acyclicity for this finite complex.',
                        'title': 'Exact complex'}],
          'exercises': {'application': [{'hint': 'Translate the question into cycles, boundaries, and homology.',
                                         'prompt': 'What does homology measure?',
                                         'solution': 'It measures failure of exactness at each degree.',
                                         'title': 'Obstruction measure'},
                                        {'hint': 'Translate the question into cycles, boundaries, and homology.',
                                         'prompt': 'Why are chain complexes useful beyond algebra?',
                                         'solution': 'They encode boundary operators whose homology captures invariants of spaces and '
                                                     'resolutions.',
                                         'title': 'Topological bridge'}],
                        'challenge': [{'hint': 'State the relevant ring map, module map, or complex before applying the structural '
                                               'theorem.',
                                       'prompt': "Connect 'Chain complexes' with 'Examples' in one rigorous argument.",
                                       'solution': 'The opening idea is: A chain complex has modules $C_n$ and differentials '
                                                   '$d_n:C_n\\to C_{n-1}$ with $d_{n-1}d_n=0$. The later viewpoint is: Two-term '
                                                   'complexes, resolutions, Koszul-style complexes, and singular-like algebraic '
                                                   'complexes illustrate the formalism. A complete solution identifies the structural '
                                                   'theorem that links these descriptions and checks its hypotheses.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': "Use one of the chapter's explicit computations or counterexamples as the test case.",
                                       'prompt': 'Choose one theorem from the chapter, remove one essential hypothesis, and exhibit '
                                                 'or explain a concrete failure.',
                                       'solution': 'The solution must name the removed hypothesis, show exactly which proof step '
                                                   'breaks, and give a concrete algebraic object where the claimed conclusion fails.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: A chain map $f:C\\to D$ induces $H_n(f):H_n(C)\\to H_n(D)$.',
                                   'solution': 'Commutation with differentials sends cycles to cycles. It also sends boundaries to '
                                               'boundaries because $f_n d_{n+1}=d_{n+1}f_{n+1}$, so the map descends to the quotient.',
                                   'title': 'Chain maps induce homology maps proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: A chain complex is exact at every degree iff $H_n(C)=0$ for all $n$.',
                                   'solution': 'By definition, zero homology at degree $n$ means the cycle module equals the boundary '
                                               'module, which is exactly exactness at that term.',
                                   'title': 'Exactness equals zero homology proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: If $f-g=dh+hd$, then $f$ and $g$ induce the same homology maps.',
                                   'solution': 'For a cycle $z$, $(f-g)(z)=d h(z)$ because $d(z)=0$, so the difference of images is a '
                                               'boundary.',
                                   'title': 'Chain homotopic maps agree on homology proof'},
                                  {'hint': 'Apply the first theorem to obtain its structural description, then verify the second '
                                           "theorem's hypotheses.",
                                   'prompt': 'Prove a corollary that genuinely uses both Chain maps induce homology maps and '
                                             'Exactness equals zero homology.',
                                   'solution': 'A correct proof explicitly invokes both results, verifies the common hypotheses, and '
                                               'derives a new consequence rather than merely restating either theorem.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use cycles, boundaries, and homology.',
                                      'prompt': 'Compute the cokernel homology of $\\mathbb Z\\xrightarrow{\\cdot3}\\mathbb Z$.',
                                      'solution': 'It is $\\mathbb Z/3$.',
                                      'title': 'Homology'},
                                     {'hint': 'Use cycles, boundaries, and homology.',
                                      'prompt': 'Compute the kernel of multiplication by $3$ on $\\mathbb Z$.',
                                      'solution': 'It is zero.',
                                      'title': 'Kernel homology'},
                                     {'hint': 'Use cycles, boundaries, and homology.',
                                      'prompt': 'If all differentials are zero, what is homology?',
                                      'solution': 'It equals the chain modules themselves.',
                                      'title': 'Zero differential'},
                                     {'hint': 'Use cycles, boundaries, and homology.',
                                      'prompt': 'What is the homology of an exact complex?',
                                      'solution': 'It is zero in every degree.',
                                      'title': 'Exact complex'},
                                     {'hint': 'Use cycles, boundaries, and homology.',
                                      'prompt': 'Why is every boundary a cycle?',
                                      'solution': 'Because consecutive differentials compose to zero.',
                                      'title': 'Boundary inclusion'}],
                        'test': [{'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Any sequence of module maps is a chain complex.',
                                  'solution': 'False: consecutive maps must compose to zero.',
                                  'title': 'Arbitrary maps'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Every cycle is a boundary in every complex.',
                                  'solution': 'False; the quotient measures homology.',
                                  'title': 'Cycles boundaries'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Vanishing homology at one degree implies the whole complex is exact.',
                                  'solution': 'False; exactness must hold at every degree.',
                                  'title': 'Zero homology'}]}},
 'V/23': {'examples': [{'after_section': 2,
                        'body': 'A free resolution of $\\mathbb Z/n\\mathbb Z$ begins $0\\to\\mathbb Z\\xrightarrow{\\cdot n}\\mathbb '
                                'Z\\to\\mathbb Z/n\\mathbb Z\\to0$. It is exact and both nonzero resolving modules are free.',
                        'title': 'Resolution of a cyclic group'},
                       {'after_section': 5,
                        'body': 'For a nonzerodivisor $f\\in R$, the sequence $0\\to R\\xrightarrow{\\cdot f}R\\to R/(f)\\to0$ is a '
                                'free resolution of length one.',
                        'title': 'Resolution of a quotient ring'},
                       {'after_section': 7,
                        'body': 'Applying a right-exact functor to a free resolution converts derived questions into homology '
                                'calculations. Tensoring the resolution of $\\mathbb Z/n$ with $\\mathbb Z/m$ already reveals the '
                                'kernel that becomes $\\operatorname{Tor}_1$.',
                        'title': 'Computing after tensoring'}],
          'exercises': {'application': [{'hint': 'Translate the question into free resolutions and exact augmentations.',
                                         'prompt': 'Why resolve by free or projective modules?',
                                         'solution': 'Such modules make Hom and tensor computations tractable and define derived '
                                                     'functors.',
                                         'title': 'Derived computation'},
                                        {'hint': 'Translate the question into free resolutions and exact augmentations.',
                                         'prompt': 'What does minimal resolution length measure?',
                                         'solution': 'It contributes to projective dimension and homological complexity.',
                                         'title': 'Complexity'}],
                        'challenge': [{'hint': 'State the relevant ring map, module map, or complex before applying the structural '
                                               'theorem.',
                                       'prompt': "Connect 'Augmented complexes' with 'Examples' in one rigorous argument.",
                                       'solution': 'The opening idea is: A resolution ends in a surjection $F_0\\to M$ and is exact '
                                                   'before and at $M$. The later viewpoint is: Cyclic quotients and regular sequences '
                                                   'yield explicit short or structured resolutions. A complete solution identifies '
                                                   'the structural theorem that links these descriptions and checks its hypotheses.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': "Use one of the chapter's explicit computations or counterexamples as the test case.",
                                       'prompt': 'Choose one theorem from the chapter, remove one essential hypothesis, and exhibit '
                                                 'or explain a concrete failure.',
                                       'solution': 'The solution must name the removed hypothesis, show exactly which proof step '
                                                   'breaks, and give a concrete algebraic object where the claimed conclusion fails.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: Every module admits a free resolution.',
                                   'solution': 'Choose a free module surjecting onto the module. Take its kernel, choose a free '
                                               'module surjecting onto that kernel, and iterate indefinitely.',
                                   'title': 'Existence of free resolutions proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: A homomorphism $M\\to N$ lifts to a chain map from any projective resolution of '
                                             '$M$ to any resolution of $N$ ending in a surjection.',
                                   'solution': 'Lift degree zero using projectivity. Inductively, the image of the previous '
                                               'differential lands in the next kernel by the chain condition, and projectivity lifts '
                                               'through the corresponding surjection.',
                                   'title': 'Comparison theorem proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: Two chain maps between projective resolutions inducing the same module map are '
                                             'chain homotopic.',
                                   'solution': 'Construct the homotopy inductively. At each degree, the difference of the two maps '
                                               'has image in a kernel already identified with the image of the next differential, and '
                                               'projectivity provides a lift.',
                                   'title': 'Homotopy uniqueness of comparison maps proof'},
                                  {'hint': 'Apply the first theorem to obtain its structural description, then verify the second '
                                           "theorem's hypotheses.",
                                   'prompt': 'Prove a corollary that genuinely uses both Existence of free resolutions and Comparison '
                                             'theorem.',
                                   'solution': 'A correct proof explicitly invokes both results, verifies the common hypotheses, and '
                                               'derives a new consequence rather than merely restating either theorem.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use free resolutions and exact augmentations.',
                                      'prompt': 'Write a free resolution of $\\mathbb Z/5$ of length one.',
                                      'solution': '$0\\to\\mathbb Z\\xrightarrow{\\cdot5}\\mathbb Z\\to\\mathbb Z/5\\to0$.',
                                      'title': 'Cyclic resolution'},
                                     {'hint': 'Use free resolutions and exact augmentations.',
                                      'prompt': 'Resolve $R/(f)$ when $f$ is a nonzerodivisor.',
                                      'solution': '$0\\to R\\xrightarrow{\\cdot f}R\\to R/(f)\\to0$.',
                                      'title': 'Quotient resolution'},
                                     {'hint': 'Use free resolutions and exact augmentations.',
                                      'prompt': 'What upper bound follows from a length-one free resolution?',
                                      'solution': 'Projective dimension at most one.',
                                      'title': 'Projective dimension'},
                                     {'hint': 'Use free resolutions and exact augmentations.',
                                      'prompt': 'What resolution does a free module need?',
                                      'solution': 'Length zero.',
                                      'title': 'Free module'},
                                     {'hint': 'Use free resolutions and exact augmentations.',
                                      'prompt': 'What is the last map in a resolution called?',
                                      'solution': 'The augmentation onto the resolved module.',
                                      'title': 'Augmentation'}],
                        'test': [{'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: A module has a unique free resolution.',
                                  'solution': 'False; resolutions are highly nonunique.',
                                  'title': 'Unique resolution'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Every module has a finite free resolution.',
                                  'solution': 'False in general.',
                                  'title': 'Finite resolution'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: A resolution may have nonzero homology in positive degrees.',
                                  'solution': 'False; it is exact there.',
                                  'title': 'Resolution exactness'}]}},
 'V/24': {'examples': [{'after_section': 2,
                        'body': 'For the ideal $(x,y)\\subset k[x,y]$, the map $R^2\\to(x,y)$ sends $(a,b)$ to $ax+by$. The vector '
                                '$(-y,x)$ lies in the kernel, giving the basic syzygy $-yx+xy=0$.',
                        'title': 'A first syzygy'},
                       {'after_section': 5,
                        'body': 'If $R^m\\xrightarrow{A}R^n\\to M\\to0$ presents $M$, then the first syzygy module is $\\ker A$. A '
                                'second syzygy is obtained by presenting that kernel and taking the next kernel.',
                        'title': 'Syzygy from a presentation matrix'},
                       {'after_section': 7,
                        'body': 'For a regular pair $x,y$, the relation $(-y,x)$ generates the first relation among the two '
                                'generators of $(x,y)$. This is the opening step of the Koszul resolution.',
                        'title': 'Koszul relation'}],
          'exercises': {'application': [{'hint': 'Translate the question into kernels of presentation maps and relations among '
                                                 'generators.',
                                         'prompt': 'What does a syzygy encode computationally?',
                                         'solution': 'It records relations among chosen generators.',
                                         'title': 'Equation relations'},
                                        {'hint': 'Translate the question into kernels of presentation maps and relations among '
                                                 'generators.',
                                         'prompt': 'How do syzygies build a free resolution?',
                                         'solution': 'Resolve the relation module repeatedly by new free modules.',
                                         'title': 'Resolution building'}],
                        'challenge': [{'hint': 'State the relevant ring map, module map, or complex before applying the structural '
                                               'theorem.',
                                       'prompt': "Connect 'First syzygy' with 'Computational matrices' in one rigorous argument.",
                                       'solution': 'The opening idea is: Given a surjection $F_0\\to M$, the first syzygy module is '
                                                   'its kernel. The later viewpoint is: Syzygies are kernels of matrices and can be '
                                                   'studied algorithmically. A complete solution identifies the structural theorem '
                                                   'that links these descriptions and checks its hypotheses.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': "Use one of the chapter's explicit computations or counterexamples as the test case.",
                                       'prompt': 'Choose one theorem from the chapter, remove one essential hypothesis, and exhibit '
                                                 'or explain a concrete failure.',
                                       'solution': 'The solution must name the removed hypothesis, show exactly which proof step '
                                                   'breaks, and give a concrete algebraic object where the claimed conclusion fails.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: If $A$ is Noetherian and $M$ is finitely generated, then the kernel of a map '
                                             '$A^n\\to M$ is finitely generated.',
                                   'solution': 'The finite free module $A^n$ is Noetherian, so every submodule, including the kernel, '
                                               'is finitely generated.',
                                   'title': 'Syzygies over Noetherian rings are finite proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': "Prove: If $0\\to K\\to P\\to M\\to0$ and $0\\to K'\\to P'\\to M\\to0$ have projective "
                                             "$P,P'$, then $K\\oplus P'\\cong K'\\oplus P$.",
                                   'solution': "Form the pullback of $P\\to M$ and $P'\\to M$. Its two projections fit into short "
                                               "exact sequences that split because $P$ and $P'$ are projective, yielding the two "
                                               'decompositions.',
                                   'title': 'Schanuel lemma proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: If $0\\to\\Omega M\\to P\\to M\\to0$ with $P$ projective, then '
                                             '$\\operatorname{Tor}_{n}^A(M,N)\\cong\\operatorname{Tor}_{n-1}^A(\\Omega M,N)$ for '
                                             '$n\\ge2$.',
                                   'solution': 'Apply the long exact Tor sequence. Higher Tor of the projective module $P$ vanishes, '
                                               'so adjacent terms give the stated isomorphism.',
                                   'title': 'Dimension shifting for Tor proof'},
                                  {'hint': 'Apply the first theorem to obtain its structural description, then verify the second '
                                           "theorem's hypotheses.",
                                   'prompt': 'Prove a corollary that genuinely uses both Syzygies over Noetherian rings are finite '
                                             'and Schanuel lemma.',
                                   'solution': 'A correct proof explicitly invokes both results, verifies the common hypotheses, and '
                                               'derives a new consequence rather than merely restating either theorem.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use kernels of presentation maps and relations among generators.',
                                      'prompt': 'Give a syzygy between $x$ and $y$.',
                                      'solution': '$(-y,x)$.',
                                      'title': 'Basic relation'},
                                     {'hint': 'Use kernels of presentation maps and relations among generators.',
                                      'prompt': 'What is the first syzygy module in a presentation $F_1\\to F_0\\to M$?',
                                      'solution': 'The kernel of $F_0\\to M$, equivalently the image from $F_1$ in an exact '
                                                  'resolution.',
                                      'title': 'Kernel definition'},
                                     {'hint': 'Use kernels of presentation maps and relations among generators.',
                                      'prompt': 'What are the positive syzygies of a free module in a length-zero resolution?',
                                      'solution': 'They vanish.',
                                      'title': 'Free module'},
                                     {'hint': 'Use kernels of presentation maps and relations among generators.',
                                      'prompt': 'What is the first syzygy of $R/(f)$ in the standard presentation?',
                                      'solution': 'The principal submodule $fR\\cong R$ when $f$ is regular.',
                                      'title': 'Cyclic quotient'},
                                     {'hint': 'Use kernels of presentation maps and relations among generators.',
                                      'prompt': 'How is the second syzygy obtained?',
                                      'solution': 'As the kernel of a free map presenting the first syzygy.',
                                      'title': 'Iterated kernel'}],
                        'test': [{'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Every generating set has zero syzygy module.',
                                  'solution': 'False; relations are usually nontrivial.',
                                  'title': 'No relations'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: The concrete syzygy module is independent of the chosen presentation on '
                                            'the nose.',
                                  'solution': 'False; stable isomorphism phenomena replace literal equality.',
                                  'title': 'Generator dependence'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Every syzygy over every ring is finitely generated.',
                                  'solution': 'False without Noetherian or finiteness hypotheses.',
                                  'title': 'Finite syzygy'}]}},
 'V/25': {'examples': [{'after_section': 2,
                        'body': 'Over a local ring $(R,\\mathfrak m)$, a finite free resolution is minimal when every differential '
                                'matrix has entries in $\\mathfrak m$. Reducing modulo $\\mathfrak m$ then makes every differential '
                                'zero.',
                        'title': 'Minimality over a local ring'},
                       {'after_section': 5,
                        'body': 'If a differential matrix contains a unit entry, suitable row and column operations split off a '
                                'contractible summand $R\\xrightarrow{\\cong}R$. Removing it shortens the resolution, so a minimal '
                                'resolution cannot contain such a unit.',
                        'title': 'Cancellation of a unit'},
                       {'after_section': 7,
                        'body': 'For $R=k[x,y]_{(x,y)}$, the Koszul complex on $x,y$ gives a minimal free resolution of the residue '
                                'field $k$. Its Betti numbers are $1,2,1$.',
                        'title': 'Residue field over a regular local ring'}],
          'exercises': {'application': [{'hint': 'Translate the question into local minimality, maximal-ideal entries, and '
                                                 'cancellation.',
                                         'prompt': 'Why are ranks in a minimal resolution meaningful invariants?',
                                         'solution': 'Minimality prevents trivial cancellations, so the free ranks are intrinsic.',
                                         'title': 'Betti invariants'},
                                        {'hint': 'Translate the question into local minimality, maximal-ideal entries, and '
                                                 'cancellation.',
                                         'prompt': 'What does growth of Betti numbers indicate?',
                                         'solution': 'It measures increasing homological complexity of the module.',
                                         'title': 'Complexity'}],
                        'challenge': [{'hint': 'State the relevant ring map, module map, or complex before applying the structural '
                                               'theorem.',
                                       'prompt': "Connect 'Minimal free resolutions' with 'Computational significance' in one "
                                                 'rigorous argument.',
                                       'solution': 'The opening idea is: A free resolution is minimal when no contractible free '
                                                   'summand can be removed. The later viewpoint is: Minimal resolutions expose '
                                                   'generators, first relations, and higher relations without algebraic cancellation. '
                                                   'A complete solution identifies the structural theorem that links these '
                                                   'descriptions and checks its hypotheses.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': "Use one of the chapter's explicit computations or counterexamples as the test case.",
                                       'prompt': 'Choose one theorem from the chapter, remove one essential hypothesis, and exhibit '
                                                 'or explain a concrete failure.',
                                       'solution': 'The solution must name the removed hypothesis, show exactly which proof step '
                                                   'breaks, and give a concrete algebraic object where the claimed conclusion fails.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: A free resolution $F_\\bullet$ over a local ring is minimal iff '
                                             '$d(F_n)\\subseteq\\mathfrak mF_{n-1}$ for all $n$.',
                                   'solution': 'If a matrix entry is a unit, elementary basis changes split off an identity map '
                                               'between rank-one free summands, producing a contractible piece. Conversely, if all '
                                               'entries lie in the maximal ideal, no such unit cancellation is possible.',
                                   'title': 'Local minimality criterion proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: For a minimal free resolution of a finite module over a local ring with residue '
                                             'field $k$, $\\operatorname{Tor}_n^A(M,k)\\cong F_n\\otimes_A k$.',
                                   'solution': 'Tensor the minimal resolution with $k$. Every differential becomes zero because its '
                                               'entries lie in $\\mathfrak m$, so homology in degree $n$ is the entire vector space '
                                               '$F_n\\otimes k$.',
                                   'title': 'Betti numbers from Tor proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: Minimal free resolutions of a finite module over a local ring are isomorphic as '
                                             'complexes.',
                                   'solution': 'Comparison maps in both directions lift the identity of the module. Modulo the '
                                               'maximal ideal they are inverse isomorphisms on Tor, hence degreewise isomorphisms by '
                                               "Nakayama's lemma.",
                                   'title': 'Uniqueness of minimal resolutions proof'},
                                  {'hint': 'Apply the first theorem to obtain its structural description, then verify the second '
                                           "theorem's hypotheses.",
                                   'prompt': 'Prove a corollary that genuinely uses both Local minimality criterion and Betti numbers '
                                             'from Tor.',
                                   'solution': 'A correct proof explicitly invokes both results, verifies the common hypotheses, and '
                                               'derives a new consequence rather than merely restating either theorem.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use local minimality, maximal-ideal entries, and cancellation.',
                                      'prompt': 'Where must entries of a minimal differential lie over a local ring?',
                                      'solution': 'In the maximal ideal.',
                                      'title': 'Minimal entry'},
                                     {'hint': 'Use local minimality, maximal-ideal entries, and cancellation.',
                                      'prompt': 'What happens to minimal differentials modulo the maximal ideal?',
                                      'solution': 'They become zero.',
                                      'title': 'Reduction'},
                                     {'hint': 'Use local minimality, maximal-ideal entries, and cancellation.',
                                      'prompt': 'What are the Koszul Betti numbers for two generators?',
                                      'solution': '$1,2,1$.',
                                      'title': 'Betti numbers'},
                                     {'hint': 'Use local minimality, maximal-ideal entries, and cancellation.',
                                      'prompt': 'What does a unit entry signal?',
                                      'solution': 'A cancellable free summand.',
                                      'title': 'Unit entry'},
                                     {'hint': 'Use local minimality, maximal-ideal entries, and cancellation.',
                                      'prompt': 'What is the minimal resolution of a free module?',
                                      'solution': 'Length zero.',
                                      'title': 'Free module'}],
                        'test': [{'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: A resolution is minimal exactly when every differential is zero before '
                                            'reduction.',
                                  'solution': 'False; entries need only lie in the maximal ideal.',
                                  'title': 'Any field reduction'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Minimal resolutions have literally identical matrices for every basis '
                                            'choice.',
                                  'solution': 'False; they are unique only up to suitable chain isomorphism.',
                                  'title': 'Uniqueness matrices'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: A minimal local resolution may contain a unit entry in a differential.',
                                  'solution': 'False.',
                                  'title': 'Unit allowed'}]}},
 'V/26': {'examples': [{'after_section': 2,
                        'body': 'Resolve $\\mathbb Z/m$ by $0\\to\\mathbb Z\\xrightarrow{\\cdot m}\\mathbb Z\\to\\mathbb Z/m\\to0$ '
                                'and tensor with $\\mathbb Z/n$. The kernel of multiplication by $m$ on $\\mathbb Z/n$ is $\\mathbb '
                                'Z/\\gcd(m,n)$, so $\\operatorname{Tor}_1^{\\mathbb Z}(\\mathbb Z/m,\\mathbb Z/n)$ has that form.',
                        'title': 'Tor of cyclic groups'},
                       {'after_section': 5,
                        'body': 'If $F$ is flat, tensoring a projective resolution stays exact in positive degrees. Therefore '
                                '$\\operatorname{Tor}_i^R(M,F)=0$ for every $i>0$.',
                        'title': 'Flatness kills Tor'},
                       {'after_section': 7,
                        'body': 'Tensoring $0\\to\\mathbb Z\\xrightarrow{\\cdot2}\\mathbb Z\\to\\mathbb Z/2\\to0$ with $\\mathbb Z/2$ '
                                'destroys injectivity. The resulting kernel is exactly the nonzero $\\operatorname{Tor}_1$ term.',
                        'title': 'Tor detects lost injectivity'}],
          'exercises': {'application': [{'hint': 'Translate the question into tensoring resolutions and Tor homology.',
                                         'prompt': 'How does Tor measure flatness?',
                                         'solution': 'Nonzero $\\operatorname{Tor}_1$ records failure of tensoring to preserve '
                                                     'injections.',
                                         'title': 'Flatness test'},
                                        {'hint': 'Translate the question into tensoring resolutions and Tor homology.',
                                         'prompt': 'Why does Tor appear in geometric intersections?',
                                         'solution': 'It measures higher failure of naive tensor products to capture nontransverse '
                                                     'intersections.',
                                         'title': 'Intersection excess'}],
                        'challenge': [{'hint': 'State the relevant ring map, module map, or complex before applying the structural '
                                               'theorem.',
                                       'prompt': "Connect 'Definition' with 'Dimension shifting' in one rigorous argument.",
                                       'solution': 'The opening idea is: Choose a projective resolution $P_\\bullet\\to M$ and set '
                                                   '$\\operatorname{Tor}_n^A(M,N)=H_n(P_\\bullet\\otimes_A N)$. The later viewpoint '
                                                   'is: Syzygies reduce higher Tor computations to lower degrees. A complete solution '
                                                   'identifies the structural theorem that links these descriptions and checks its '
                                                   'hypotheses.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': "Use one of the chapter's explicit computations or counterexamples as the test case.",
                                       'prompt': 'Choose one theorem from the chapter, remove one essential hypothesis, and exhibit '
                                                 'or explain a concrete failure.',
                                       'solution': 'The solution must name the removed hypothesis, show exactly which proof step '
                                                   'breaks, and give a concrete algebraic object where the claimed conclusion fails.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: The modules $H_n(P_\\bullet\\otimes N)$ are independent of the chosen projective '
                                             'resolution of $M$ up to canonical isomorphism.',
                                   'solution': 'Comparison maps between projective resolutions are unique up to chain homotopy. '
                                               'Tensor preserves chain homotopies, and chain-homotopic maps induce the same homology '
                                               'maps, yielding canonical isomorphisms.',
                                   'title': 'Well-definedness of Tor proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: If $P$ is projective, then $\\operatorname{Tor}_n^A(P,N)=0$ for $n>0$.',
                                   'solution': 'Use the resolution concentrated in degree zero at $P$. The tensor complex has no '
                                               'positive-degree terms, so its positive homology vanishes.',
                                   'title': 'Projective vanishing proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: An $A$-module $F$ is flat iff $\\operatorname{Tor}_1^A(A/I,F)=0$ for every '
                                             'finitely generated ideal $I$ under the standard finite-ideal criterion, and in '
                                             'particular iff $\\operatorname{Tor}_1^A(M,F)=0$ for all $M$.',
                                   'solution': 'Apply Tor to $0\\to I\\to A\\to A/I\\to0$. Vanishing of the connecting kernel is '
                                               'exactly injectivity of $I\\otimes F\\to F$; the general criterion follows from the '
                                               'flatness tests and long exact sequences.',
                                   'title': 'Flatness via Tor proof'},
                                  {'hint': 'Apply the first theorem to obtain its structural description, then verify the second '
                                           "theorem's hypotheses.",
                                   'prompt': 'Prove a corollary that genuinely uses both Well-definedness of Tor and Projective '
                                             'vanishing.',
                                   'solution': 'A correct proof explicitly invokes both results, verifies the common hypotheses, and '
                                               'derives a new consequence rather than merely restating either theorem.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use tensoring resolutions and Tor homology.',
                                      'prompt': 'Compute $\\operatorname{Tor}_1^{\\mathbb Z}(\\mathbb Z/6,\\mathbb Z/15)$.',
                                      'solution': 'It is $\\mathbb Z/3$.',
                                      'title': 'Cyclic Tor'},
                                     {'hint': 'Use tensoring resolutions and Tor homology.',
                                      'prompt': 'Compute $\\operatorname{Tor}_1^{\\mathbb Z}(\\mathbb Z/4,\\mathbb Z/9)$.',
                                      'solution': 'It is zero.',
                                      'title': 'Coprime Tor'},
                                     {'hint': 'Use tensoring resolutions and Tor homology.',
                                      'prompt': 'Compute $\\operatorname{Tor}_1^R(R^n,M)$.',
                                      'solution': 'It is zero.',
                                      'title': 'Free argument'},
                                     {'hint': 'Use tensoring resolutions and Tor homology.',
                                      'prompt': 'Compute positive Tor with a flat second module.',
                                      'solution': 'It vanishes.',
                                      'title': 'Flat argument'},
                                     {'hint': 'Use tensoring resolutions and Tor homology.',
                                      'prompt': 'What is $\\operatorname{Tor}_0^R(M,N)$?',
                                      'solution': 'It is $M\\otimes_RN$.',
                                      'title': 'Degree zero'}],
                        'test': [{'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: $\\operatorname{Tor}_1$ always vanishes.',
                                  'solution': 'False.',
                                  'title': 'Always zero'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: A flat module can have nonzero positive Tor with some module.',
                                  'solution': 'False.',
                                  'title': 'Flat criterion'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Tor depends on the chosen projective resolution.',
                                  'solution': 'False up to canonical isomorphism.',
                                  'title': 'Resolution dependence'}]}},
 'V/27': {'examples': [{'after_section': 2,
                        'body': 'Applying $\\operatorname{Hom}_{\\mathbb Z}(-,\\mathbb Z/n)$ to the standard resolution of $\\mathbb '
                                'Z/m$ gives a cokernel of multiplication by $m$. Hence $\\operatorname{Ext}^1_{\\mathbb Z}(\\mathbb '
                                'Z/m,\\mathbb Z/n)\\cong\\mathbb Z/\\gcd(m,n)$.',
                        'title': 'Ext of cyclic groups'},
                       {'after_section': 5,
                        'body': 'If $P$ is projective, it has a length-zero projective resolution. Therefore '
                                '$\\operatorname{Ext}^i_R(P,N)=0$ for every $i>0$.',
                        'title': 'Projectives kill Ext'},
                       {'after_section': 7,
                        'body': 'Elements of $\\operatorname{Ext}^1_R(M,N)$ correspond to equivalence classes of short exact '
                                'sequences $0\\to N\\to E\\to M\\to0$. The zero class is represented by the split extension.',
                        'title': 'Extensions classified by Ext'}],
          'exercises': {'application': [{'hint': 'Translate the question into Hom on projective resolutions and extension classes.',
                                         'prompt': 'What does $\\operatorname{Ext}^1$ measure?',
                                         'solution': 'It measures equivalence classes of extensions and obstruction to splitting.',
                                         'title': 'Extension obstruction'},
                                        {'hint': 'Translate the question into Hom on projective resolutions and extension classes.',
                                         'prompt': 'Why does Ext occur in deformation theory?',
                                         'solution': 'Extension groups encode first-order gluing and obstruction data in many '
                                                     'algebraic settings.',
                                         'title': 'Deformation flavor'}],
                        'challenge': [{'hint': 'State the relevant ring map, module map, or complex before applying the structural '
                                               'theorem.',
                                       'prompt': "Connect 'Definition from projectives' with 'Duality preview' in one rigorous "
                                                 'argument.',
                                       'solution': 'The opening idea is: Choose a projective resolution $P_\\bullet\\to M$ and set '
                                                   '$\\operatorname{Ext}_A^n(M,N)=H^n(\\operatorname{Hom}_A(P_\\bullet,N))$. The '
                                                   'later viewpoint is: Ext groups appear in duality, canonical modules, and '
                                                   'deformation theory. A complete solution identifies the structural theorem that '
                                                   'links these descriptions and checks its hypotheses.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': "Use one of the chapter's explicit computations or counterexamples as the test case.",
                                       'prompt': 'Choose one theorem from the chapter, remove one essential hypothesis, and exhibit '
                                                 'or explain a concrete failure.',
                                       'solution': 'The solution must name the removed hypothesis, show exactly which proof step '
                                                   'breaks, and give a concrete algebraic object where the claimed conclusion fails.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: $H^n(\\operatorname{Hom}(P_\\bullet,N))$ is independent of the chosen projective '
                                             'resolution of $M$.',
                                   'solution': 'Comparison maps between resolutions are unique up to chain homotopy. Applying Hom '
                                               'turns chain homotopies into cochain homotopies, which induce identical cohomology '
                                               'maps.',
                                   'title': 'Well-definedness of Ext proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: If $P$ is projective, then $\\operatorname{Ext}_A^n(P,N)=0$ for $n>0$.',
                                   'solution': 'Use the projective resolution concentrated in degree zero. The resulting Hom cochain '
                                               'complex has no positive cohomology.',
                                   'title': 'Projective vanishing proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: Equivalence classes of short exact sequences $0\\to N\\to E\\to M\\to0$ form a '
                                             'group naturally isomorphic to $\\operatorname{Ext}_A^1(M,N)$.',
                                   'solution': 'Pull an extension back along a projective presentation of $M$ and choose a splitting '
                                               'over the projective term. The resulting map from the first syzygy to $N$ defines a '
                                               'degree-one cohomology class; changing the splitting changes it by a coboundary, and '
                                               'the construction is reversible via pushout.',
                                   'title': 'Ext one classifies extensions proof'},
                                  {'hint': 'Apply the first theorem to obtain its structural description, then verify the second '
                                           "theorem's hypotheses.",
                                   'prompt': 'Prove a corollary that genuinely uses both Well-definedness of Ext and Projective '
                                             'vanishing.',
                                   'solution': 'A correct proof explicitly invokes both results, verifies the common hypotheses, and '
                                               'derives a new consequence rather than merely restating either theorem.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use Hom on projective resolutions and extension classes.',
                                      'prompt': 'Compute $\\operatorname{Ext}^1_{\\mathbb Z}(\\mathbb Z/6,\\mathbb Z/15)$.',
                                      'solution': 'It is $\\mathbb Z/3$.',
                                      'title': 'Cyclic Ext'},
                                     {'hint': 'Use Hom on projective resolutions and extension classes.',
                                      'prompt': 'Compute $\\operatorname{Ext}^1_{\\mathbb Z}(\\mathbb Z/4,\\mathbb Z/9)$.',
                                      'solution': 'It is zero.',
                                      'title': 'Coprime Ext'},
                                     {'hint': 'Use Hom on projective resolutions and extension classes.',
                                      'prompt': 'Compute positive Ext from a free module.',
                                      'solution': 'It vanishes.',
                                      'title': 'Projective'},
                                     {'hint': 'Use Hom on projective resolutions and extension classes.',
                                      'prompt': 'What is $\\operatorname{Ext}^0_R(M,N)$?',
                                      'solution': 'It is $\\operatorname{Hom}_R(M,N)$.',
                                      'title': 'Degree zero'},
                                     {'hint': 'Use Hom on projective resolutions and extension classes.',
                                      'prompt': 'Which Ext class corresponds to a split short exact sequence?',
                                      'solution': 'The zero class.',
                                      'title': 'Split class'}],
                        'test': [{'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Every short exact sequence of modules splits.',
                                  'solution': 'False; nonzero Ext classes obstruct splitting.',
                                  'title': 'Always split'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: A projective first argument can have nonzero positive Ext.',
                                  'solution': 'False.',
                                  'title': 'Projective first variable'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Ext depends on arbitrary choices in a projective resolution.',
                                  'solution': 'False up to canonical isomorphism.',
                                  'title': 'Resolution dependence'}]}},
 'V/28': {'examples': [{'after_section': 2,
                        'body': 'Tensor product is right exact but may fail on kernels. Replacing an input by a projective resolution '
                                'and taking homology produces its left derived functors, the Tor groups.',
                        'title': 'Deriving a right-exact functor'},
                       {'after_section': 5,
                        'body': 'Hom in the second variable is left exact. Applying it to a projective resolution in the first '
                                'variable and taking cohomology produces Ext, which records the missing higher exactness.',
                        'title': 'Deriving a left-exact functor'},
                       {'after_section': 7,
                        'body': 'A short exact sequence of modules induces long exact sequences in Tor or Ext. The connecting '
                                'morphisms propagate the failure of exactness into neighboring derived degrees.',
                        'title': 'Long exact sequence'}],
          'exercises': {'application': [{'hint': 'Translate the question into resolutions, exactness defects, and derived functors.',
                                         'prompt': 'How do Tor and Ext fit one framework?',
                                         'solution': 'They are homology or cohomology of resolutions measuring failure of ordinary '
                                                     'functors to be exact.',
                                         'title': 'Unified viewpoint'},
                                        {'hint': 'Translate the question into resolutions, exactness defects, and derived functors.',
                                         'prompt': 'Why are resolutions central to derived methods?',
                                         'solution': 'They replace arbitrary modules by acyclic projective objects where the functor '
                                                     'is easier to compute.',
                                         'title': 'Computation strategy'}],
                        'challenge': [{'hint': 'State the relevant ring map, module map, or complex before applying the structural '
                                               'theorem.',
                                       'prompt': "Connect 'Exact and derived behavior' with 'Algebra-geometry bridge' in one rigorous "
                                                 'argument.',
                                       'solution': 'The opening idea is: Left or right exact functors lose information at kernels or '
                                                   'cokernels; derived functors measure that failure in higher degrees. The later '
                                                   'viewpoint is: Derived tensor and derived Hom underpin intersection theory, '
                                                   'deformation theory, and sheaf cohomology. A complete solution identifies the '
                                                   'structural theorem that links these descriptions and checks its hypotheses.',
                                       'title': 'Local-global synthesis'},
                                      {'hint': "Use one of the chapter's explicit computations or counterexamples as the test case.",
                                       'prompt': 'Choose one theorem from the chapter, remove one essential hypothesis, and exhibit '
                                                 'or explain a concrete failure.',
                                       'solution': 'The solution must name the removed hypothesis, show exactly which proof step '
                                                   'breaks, and give a concrete algebraic object where the claimed conclusion fails.',
                                       'title': 'Hypothesis audit'}],
                        'proof': [{'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: For fixed $N$, the homology of a projective resolution tensor $N$ gives the left '
                                             'derived functors of $-\\otimes_A N$.',
                                   'solution': 'Projective resolutions are acyclic for tensor in positive resolution degrees and '
                                               'comparison maps make the construction functorial and independent of resolution; '
                                               'degree zero recovers ordinary tensor.',
                                   'title': 'Tor is the left derived tensor functor proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: For fixed $N$, cohomology of $\\operatorname{Hom}(P_\\bullet,N)$ gives derived '
                                             'functors extending $\\operatorname{Hom}(-,N)$ contravariantly in the first variable.',
                                   'solution': 'Projective resolutions replace the first variable by Hom-acyclic objects. Comparison '
                                               'and homotopy yield functorial well-defined cohomology, and degree zero recovers Hom.',
                                   'title': 'Ext is a derived Hom functor proof'},
                                  {'hint': 'Start from the theorem hypotheses and identify the decisive algebraic construction.',
                                   'prompt': 'Prove: A short exact sequence in the appropriate variable induces a natural long exact '
                                             'sequence of derived functors.',
                                   'solution': 'Resolve compatibly or apply the functor to a short exact sequence of suitable '
                                               'resolutions. The resulting short exact sequence of complexes yields the standard long '
                                               'exact sequence in homology or cohomology via connecting morphisms.',
                                   'title': 'Derived functors produce long exact sequences proof'},
                                  {'hint': 'Apply the first theorem to obtain its structural description, then verify the second '
                                           "theorem's hypotheses.",
                                   'prompt': 'Prove a corollary that genuinely uses both Tor is the left derived tensor functor and '
                                             'Ext is a derived Hom functor.',
                                   'solution': 'A correct proof explicitly invokes both results, verifies the common hypotheses, and '
                                               'derives a new consequence rather than merely restating either theorem.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use resolutions, exactness defects, and derived functors.',
                                      'prompt': 'What are the left derived functors of tensor product?',
                                      'solution': 'They are the Tor functors.',
                                      'title': 'Tensor derived'},
                                     {'hint': 'Use resolutions, exactness defects, and derived functors.',
                                      'prompt': 'What are the right-derived-type groups associated with Hom in this '
                                                'projective-resolution viewpoint?',
                                      'solution': 'They are the Ext functors.',
                                      'title': 'Hom derived'},
                                     {'hint': 'Use resolutions, exactness defects, and derived functors.',
                                      'prompt': 'Identify $\\operatorname{Tor}_0$.',
                                      'solution': 'Tensor product.',
                                      'title': 'Degree zero Tor'},
                                     {'hint': 'Use resolutions, exactness defects, and derived functors.',
                                      'prompt': 'Identify $\\operatorname{Ext}^0$.',
                                      'solution': 'Hom.',
                                      'title': 'Degree zero Ext'},
                                     {'hint': 'Use resolutions, exactness defects, and derived functors.',
                                      'prompt': 'What happens to positive derived groups on projective inputs?',
                                      'solution': 'They vanish.',
                                      'title': 'Projective input'}],
                        'test': [{'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: An exact functor has nonzero higher derived functors.',
                                  'solution': 'False; higher derived functors vanish.',
                                  'title': 'Exact functor'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: Derived functors depend essentially on the chosen resolution.',
                                  'solution': 'False; comparison theorems give canonical invariance.',
                                  'title': 'Choice dependence'},
                                 {'hint': 'Use the smallest concrete ring, module, or resolution that can decide the claim.',
                                  'prompt': 'Test the claim: A short exact sequence yields only another short exact sequence after a '
                                            'nonexact functor.',
                                  'solution': 'False; derived functors organize the defect into a long exact sequence.',
                                  'title': 'Short sequence only'}]}}}
