DATA = {'V/09': {'examples': [{'after_section': 2,
                        'body': 'Multiplication by $6$ gives a short exact sequence $0\\to\\mathbb Z\\to\\mathbb Z\\to\\mathbb '
                                'Z/6\\to0$. The kernel is zero and the cokernel is the residue module.',
                        'title': 'Kernel and cokernel'},
                       {'after_section': 5,
                        'body': 'The inclusion $k^2\\to k^3$ into the first two coordinates has cokernel $k$. Projection onto '
                                'the third coordinate completes a short exact sequence.',
                        'title': 'Matrix exactness'},
                       {'after_section': 7,
                        'body': 'The sequence $0\\to A\\to A\\oplus B\\to B\\to0$ splits via $b\\mapsto(0,b)$, exhibiting the '
                                'middle module as a direct sum.',
                        'title': 'Split sequence'}],
          'exercises': {'application': [{'hint': 'Translate the situation into kernels, cokernels, and exact sequences.',
                                         'prompt': 'How do exact sequences encode generators and relations?',
                                         'solution': 'A free surjection supplies generators and its kernel records relations.',
                                         'title': 'Presentations'},
                                        {'hint': 'Translate the situation into kernels, cokernels, and exact sequences.',
                                         'prompt': 'What do kernel and cokernel measure?',
                                         'solution': 'They measure failure of injectivity and surjectivity.',
                                         'title': 'Failure measures'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Modules' and 'Examples' in one rigorous argument.",
                                       'solution': 'The argument begins with An $A$-module is an abelian group with compatible '
                                                   'scalar multiplication by $A$. It then uses the later viewpoint: Ideals, '
                                                   'quotient modules, free modules, torsion abelian groups, and vector spaces '
                                                   'all fit the same language. The bridge is supplied by the structural theorems '
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
                                   'prompt': 'Prove: For an $A$-linear map $f:M\\to N$, $M/\\ker f\\cong\\operatorname{im}f$.',
                                   'solution': 'Send $m+\\ker f$ to $f(m)$. The same kernel argument as for groups and rings '
                                               'gives a well-defined bijective linear map onto the image.',
                                   'title': 'First isomorphism theorem for modules proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': "Prove: A short exact sequence $0\\to M'\\xrightarrow{i}M\\xrightarrow{p}M''\\to0$ "
                                             'splits iff $p$ has a section, equivalently iff $i$ has a retraction.',
                                   'solution': "A section $s$ gives $M=i(M')\\oplus s(M'')$. Conversely a direct-sum "
                                               'decomposition supplies both projection and inclusion maps realizing the section '
                                               'and retraction.',
                                   'title': 'Splitting criterion proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: Taking arbitrary direct sums of short exact sequences of modules preserves '
                                             'exactness.',
                                   'solution': 'All maps act componentwise. An element of a direct sum has finite support, so '
                                               'kernel and image membership can be checked component by component.',
                                   'title': 'Exactness of direct sums proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining First isomorphism theorem for modules with '
                                             'Splitting criterion. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes First isomorphism theorem for modules and then '
                                               'applies Splitting criterion; the conclusion follows after checking the shared '
                                               'hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use kernels, cokernels, and exact sequences.',
                                      'prompt': 'Find the kernel of multiplication by $4$ on $\\mathbb Z$.',
                                      'solution': 'It is zero.',
                                      'title': 'Kernel'},
                                     {'hint': 'Use kernels, cokernels, and exact sequences.',
                                      'prompt': 'Find its cokernel.',
                                      'solution': 'It is $\\mathbb Z/4$.',
                                      'title': 'Cokernel'},
                                     {'hint': 'Use kernels, cokernels, and exact sequences.',
                                      'prompt': 'Is multiplication by $2$ on $\\mathbb Z$ injective?',
                                      'solution': 'Yes.',
                                      'title': 'Injection'},
                                     {'hint': 'Use kernels, cokernels, and exact sequences.',
                                      'prompt': 'Find the rank of the projection $k^3\\to k^2$.',
                                      'solution': 'The rank is $2$.',
                                      'title': 'Matrix rank'},
                                     {'hint': 'Use kernels, cokernels, and exact sequences.',
                                      'prompt': 'Give a section of $A\\oplus B\\to B$.',
                                      'solution': '$b\\mapsto(0,b)$.',
                                      'title': 'Section'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every injective module map is surjective.',
                                  'solution': 'False: multiplication by $2$ on $\\mathbb Z$.',
                                  'title': 'Injective surjective'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every surjection is injective.',
                                  'solution': 'False: $\\mathbb Z\\to\\mathbb Z/2$.',
                                  'title': 'Surjective injective'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: $g\\circ f=0$ implies exactness at the middle term.',
                                  'solution': 'False: it gives only image contained in kernel.',
                                  'title': 'Zero composite'}]}},
 'V/10': {'examples': [{'after_section': 2,
                        'body': 'For positive integers $m,n$, $\\mathbb Z/m\\otimes\\mathbb Z/n\\cong\\mathbb Z/\\gcd(m,n)$. '
                                'Thus $\\mathbb Z/6\\otimes\\mathbb Z/15\\cong\\mathbb Z/3$.',
                        'title': 'Cyclic tensor product'},
                       {'after_section': 5,
                        'body': 'For an ideal $I$ and module $M$, $(R/I)\\otimes_RM\\cong M/IM$. Tensor relations force elements '
                                'of $I$ to act as zero.',
                        'title': 'Tensor with a quotient'},
                       {'after_section': 7,
                        'body': 'For a field extension $K/k$, $K\\otimes_k k^n\\cong K^n$. A $k$-basis becomes a $K$-basis after '
                                'scalar extension.',
                        'title': 'Extension of scalars'}],
          'exercises': {'application': [{'hint': 'Translate the situation into tensor products and their universal property.',
                                         'prompt': 'Why is $B\\otimes_AM$ extension of scalars?',
                                         'solution': 'It is universal for reinterpreting the $A$-action through $B$.',
                                         'title': 'Scalar extension'},
                                        {'hint': 'Translate the situation into tensor products and their universal property.',
                                         'prompt': 'Why do tensor products of algebras model product coordinates?',
                                         'solution': 'They combine independent coordinate functions over the base field.',
                                         'title': 'Affine products'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Balanced bilinear maps' and 'Multilinear extension' "
                                                 'in one rigorous argument.',
                                       'solution': 'The argument begins with An $A$-balanced map satisfies $b(am,n)=b(m,an)$ in '
                                                   'addition to additivity in each variable. It then uses the later viewpoint: '
                                                   'Exterior and symmetric powers are built by further quotienting tensor '
                                                   'powers. The bridge is supplied by the structural theorems proved in the '
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
                                   'prompt': 'Prove: For every balanced bilinear map $b:M\\times N\\to P$, there is a unique '
                                             'linear map $\\widetilde b:M\\otimes_A N\\to P$ with $\\widetilde b(m\\otimes '
                                             'n)=b(m,n)$.',
                                   'solution': 'Construct the tensor product as the free module on pairs modulo the subgroup '
                                               'generated by additivity and balancing relations. The relations are exactly those '
                                               'killed by every balanced bilinear map.',
                                   'title': 'Universal property proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: For an ideal $I\\subset A$, $(A/I)\\otimes_A M\\cong M/IM$.',
                                   'solution': 'Send $(a+I)\\otimes m$ to $am+IM$. The map is balanced and surjective; the '
                                               'universal properties on both sides show that its kernel is precisely the '
                                               'relations generated by $I M$.',
                                   'title': 'Quotient tensor identity proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': "Prove: If $M'\\to M\\to M''\\to0$ is exact, then $M'\\otimes N\\to M\\otimes N\\to "
                                             "M''\\otimes N\\to0$ is exact.",
                                   'solution': 'The tensor product is a left adjoint in either variable, so it preserves '
                                               'cokernels; directly, generators in the kernel of the final map differ by tensors '
                                               'coming from the preceding module.',
                                   'title': 'Right exactness of tensor proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Universal property with Quotient tensor '
                                             'identity. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Universal property and then applies Quotient '
                                               'tensor identity; the conclusion follows after checking the shared hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use tensor products and their universal property.',
                                      'prompt': 'Compute $R\\otimes_RM$.',
                                      'solution': 'It is $M$.',
                                      'title': 'Unit tensor'},
                                     {'hint': 'Use tensor products and their universal property.',
                                      'prompt': 'Compute $M\\otimes_R0$.',
                                      'solution': 'It is zero.',
                                      'title': 'Zero tensor'},
                                     {'hint': 'Use tensor products and their universal property.',
                                      'prompt': 'Compute $\\mathbb Z/4\\otimes\\mathbb Z/6$.',
                                      'solution': 'It is $\\mathbb Z/2$.',
                                      'title': 'Cyclic tensor'},
                                     {'hint': 'Use tensor products and their universal property.',
                                      'prompt': 'Compute $\\mathbb Z/4\\otimes\\mathbb Z/9$.',
                                      'solution': 'It is zero.',
                                      'title': 'Coprime tensor'},
                                     {'hint': 'Use tensor products and their universal property.',
                                      'prompt': 'Compute $(R/I)\\otimes_R(R/J)$.',
                                      'solution': 'It is $R/(I+J)$.',
                                      'title': 'Quotient tensor'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Tensoring always preserves injections.',
                                  'solution': 'False: tensor multiplication by $2$ with $\\mathbb Z/2$.',
                                  'title': 'Left exactness'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: A pure tensor is zero only if one factor is zero.',
                                  'solution': 'False: use $\\mathbb Z/2\\otimes\\mathbb Z/3=0$.',
                                  'title': 'Pure tensor'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Dimension multiplication holds for arbitrary modules.',
                                  'solution': 'False; it is a vector-space formula under suitable finiteness.',
                                  'title': 'Dimension rule'}]}},
 'V/11': {'examples': [{'after_section': 2,
                        'body': 'For $A\\to B$ and $I\\subset A$, one has $B\\otimes_AA/I\\cong B/IB$. Equations defining $I$ '
                                'are transported to the new coefficient ring.',
                        'title': 'Base change of a quotient'},
                       {'after_section': 5,
                        'body': 'Base changing $\\mathbb R[x]/(x^2+1)$ to $\\mathbb C$ gives $\\mathbb C[x]/((x-i)(x+i))$. A '
                                'polynomial irreducible over the original field can split after base change.',
                        'title': 'Field extension splitting'},
                       {'after_section': 7,
                        'body': 'For $0\\to N\\to M\\to M/N\\to0$, tensoring with a flat $A$-algebra $B$ preserves the injection '
                                'and gives a short exact base-changed sequence.',
                        'title': 'Flat base change'}],
          'exercises': {'application': [{'hint': 'Translate the situation into quotients and base change.',
                                         'prompt': 'Why extend the coefficient field?',
                                         'solution': 'It can reveal roots and factorizations while retaining canonical '
                                                     'base-change data.',
                                         'title': 'Solving equations'},
                                        {'hint': 'Translate the situation into quotients and base change.',
                                         'prompt': 'Interpret $M\\otimes_A\\kappa(P)$.',
                                         'solution': 'It is the fiber of $M$ at the prime $P$.',
                                         'title': 'Fiber module'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Scalar extension' and 'Compatibility with "
                                                 "quotients' in one rigorous argument.",
                                       'solution': 'The argument begins with For $A\\to B$, the base-changed module is '
                                                   '$B\\otimes_A M$. It then uses the later viewpoint: Cokernels commute with '
                                                   'base change because tensor is right exact. The bridge is supplied by the '
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
                                   'prompt': 'Prove: For $A\\to B$ and ideal $I\\subset A$, $B\\otimes_A A/I\\cong B/IB$.',
                                   'solution': 'Apply the quotient tensor identity to the $A$-module $B$; the submodule $IB$ is '
                                               'generated by images of elements of $I$.',
                                   'title': 'Quotient under base change proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: For $A\\to B\\to C$ and an $A$-module $M$, $C\\otimes_B(B\\otimes_A '
                                             'M)\\cong C\\otimes_A M$.',
                                   'solution': 'Send $c\\otimes(b\\otimes m)$ to $cb\\otimes m$. Balancedness gives a '
                                               'well-defined map, and the inverse sends $c\\otimes m$ to $c\\otimes(1\\otimes '
                                               'm)$.',
                                   'title': 'Transitivity of base change proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': "Prove: If $M'\\to M\\to Q\\to0$ is exact, then $B\\otimes_A M'\\to B\\otimes_A "
                                             'M\\to B\\otimes_A Q\\to0$ is exact.',
                                   'solution': 'This is the right exactness of tensor product with the $A$-module $B$.',
                                   'title': 'Base change of a cokernel proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Quotient under base change with Transitivity '
                                             'of base change. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Quotient under base change and then applies '
                                               'Transitivity of base change; the conclusion follows after checking the shared '
                                               'hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use quotients and base change.',
                                      'prompt': 'Compute $B\\otimes_AA/I$.',
                                      'solution': 'It is $B/IB$.',
                                      'title': 'Quotient base change'},
                                     {'hint': 'Use quotients and base change.',
                                      'prompt': 'Compute $K\\otimes_kk[x]$.',
                                      'solution': 'It is $K[x]$.',
                                      'title': 'Polynomial extension'},
                                     {'hint': 'Use quotients and base change.',
                                      'prompt': 'Compute $B\\otimes_AA^n$.',
                                      'solution': 'It is $B^n$.',
                                      'title': 'Free module'},
                                     {'hint': 'Use quotients and base change.',
                                      'prompt': 'Compute $(A/I)/(J/I)$.',
                                      'solution': 'It is $A/J$.',
                                      'title': 'Nested quotient'},
                                     {'hint': 'Use quotients and base change.',
                                      'prompt': 'Compute $(A/I)\\otimes_AM$.',
                                      'solution': 'It is $M/IM$.',
                                      'title': 'Module quotient'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every base change preserves injections.',
                                  'solution': 'False without flatness.',
                                  'title': 'Injectivity'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Irreducible polynomials remain irreducible after every field '
                                            'extension.',
                                  'solution': 'False: $x^2+1$ from $\\mathbb R$ to $\\mathbb C$.',
                                  'title': 'Irreducibility'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Ideal extension and contraction are always inverse.',
                                  'solution': 'False for arbitrary ring maps.',
                                  'title': 'Extension contraction'}]}},
 'V/12': {'examples': [{'after_section': 2,
                        'body': 'A map $\\mathbb Z/n\\to M$ is determined by the image of $1$, which must be killed by $n$. '
                                'Hence $\\operatorname{Hom}_{\\mathbb Z}(\\mathbb Z/n,M)\\cong M[n]$.',
                        'title': 'Hom from a cyclic module'},
                       {'after_section': 5,
                        'body': 'The cokernel of $\\operatorname{diag}(x,y):R^2\\to R^2$ is $R/(x)\\oplus R/(y)$. The diagonal '
                                'matrix records two independent relations.',
                        'title': 'Presentation matrix'},
                       {'after_section': 7,
                        'body': 'For finitely presented $M$, localization commutes with Hom in the first variable: the finite '
                                'presentation reduces the claim to kernels between finite powers.',
                        'title': 'Hom and localization'}],
          'exercises': {'application': [{'hint': 'Translate the situation into Hom and finite presentations.',
                                         'prompt': 'How does a presentation matrix encode a module?',
                                         'solution': 'Generators are free coordinates and matrix columns or rows encode '
                                                     'relations.',
                                         'title': 'Linear equations'},
                                        {'hint': 'Translate the situation into Hom and finite presentations.',
                                         'prompt': 'Why are finitely presented modules convenient under base change?',
                                         'solution': 'The same finite relation matrix can be transported coefficientwise.',
                                         'title': 'Stable base change'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Hom modules' and 'Matrix viewpoint' in one rigorous "
                                                 'argument.',
                                       'solution': 'The argument begins with For $A$-modules $M,N$, $\\operatorname{Hom}_A(M,N)$ '
                                                   'is an $A$-module under pointwise operations. It then uses the later '
                                                   'viewpoint: Maps between finite free modules are matrices, so finite '
                                                   'presentations translate module questions into matrix algebra. The bridge is '
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
                                   'prompt': 'Prove: $M$ is finitely presented iff there exists an exact sequence $A^m\\to '
                                             'A^n\\to M\\to0$ with finite $m,n$.',
                                   'solution': 'This is the definition translated into generators and relations: the second map '
                                               'chooses finitely many generators and the image of the first supplies finitely '
                                               'many generators for all relations.',
                                   'title': 'Finite presentation criterion proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': "Prove: For $0\\to N'\\to N\\to N''$, the sequence "
                                             "$0\\to\\operatorname{Hom}(M,N')\\to\\operatorname{Hom}(M,N)\\to\\operatorname{Hom}(M,N'')$ "
                                             'is exact.',
                                   'solution': "A map into $N$ lands in $N'$ exactly when its composite with $N\\to N''$ is "
                                               "zero. Injectivity follows because $N'\\to N$ is injective.",
                                   'title': 'Hom is left exact proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: If $M$ is finitely presented, then '
                                             '$S^{-1}\\operatorname{Hom}_A(M,N)\\cong\\operatorname{Hom}_{S^{-1}A}(S^{-1}M,S^{-1}N)$.',
                                   'solution': 'Choose a finite presentation of $M$, apply Hom to it, localize the resulting '
                                               'kernel description, and use exactness of localization together with the evident '
                                               'formula for finite free modules.',
                                   'title': 'Localization of Hom for finitely presented modules proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Finite presentation criterion with Hom is '
                                             'left exact. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Finite presentation criterion and then applies '
                                               'Hom is left exact; the conclusion follows after checking the shared hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use Hom and finite presentations.',
                                      'prompt': 'Compute $\\operatorname{Hom}_R(R,M)$.',
                                      'solution': 'It is $M$.',
                                      'title': 'Hom from ring'},
                                     {'hint': 'Use Hom and finite presentations.',
                                      'prompt': 'Compute $\\operatorname{Hom}_R(M,0)$.',
                                      'solution': 'It is zero.',
                                      'title': 'Hom to zero'},
                                     {'hint': 'Use Hom and finite presentations.',
                                      'prompt': 'Compute $\\operatorname{Hom}_{\\mathbb Z}(\\mathbb Z/6,\\mathbb Z/15)$.',
                                      'solution': 'It is isomorphic to $\\mathbb Z/3$.',
                                      'title': 'Cyclic Hom'},
                                     {'hint': 'Use Hom and finite presentations.',
                                      'prompt': 'Find the cokernel of multiplication by $f$ on $R$.',
                                      'solution': 'It is $R/(f)$.',
                                      'title': 'Cokernel'},
                                     {'hint': 'Use Hom and finite presentations.',
                                      'prompt': 'Present $R/(f,g)$ using finite free modules.',
                                      'solution': 'Use $R^2\\to R\\to R/(f,g)\\to0$.',
                                      'title': 'Presentation'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every finitely generated module is finitely presented over every '
                                            'ring.',
                                  'solution': 'False over non-Noetherian rings.',
                                  'title': 'Finite generation'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: $\\operatorname{Hom}(M,-)$ is always right exact.',
                                  'solution': 'False unless $M$ has extra projectivity.',
                                  'title': 'Hom exactness'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Localization commutes with Hom for every first module.',
                                  'solution': 'False in general; finite presentation is a standard sufficient hypothesis.',
                                  'title': 'Hom localization'}]}},
 'V/13': {'examples': [{'after_section': 2,
                        'body': 'If $e^2=e$, then $R=eR\\oplus(1-e)R$. Thus $eR$ is a direct summand of the free module $R$ and '
                                'is projective.',
                        'title': 'Idempotent projective'},
                       {'after_section': 5,
                        'body': 'A module $P$ is projective exactly when every surjection onto $P$ splits. Applying this to a '
                                'free surjection shows that projectives are precisely direct summands of free modules.',
                        'title': 'Splitting criterion'},
                       {'after_section': 7,
                        'body': 'A finitely generated projective module becomes free after localization at a prime. Its local '
                                'rank is the algebraic analogue of vector-bundle rank.',
                        'title': 'Local freeness'}],
          'exercises': {'application': [{'hint': 'Translate the situation into free modules, projective splittings, and '
                                                 'idempotents.',
                                         'prompt': 'Why do finite projectives model algebraic vector bundles?',
                                         'solution': 'They are locally free of finite rank.',
                                         'title': 'Vector bundles'},
                                        {'hint': 'Translate the situation into free modules, projective splittings, and '
                                                 'idempotents.',
                                         'prompt': 'Why are projectives useful in resolutions?',
                                         'solution': 'Surjections onto them split, eliminating lifting obstructions.',
                                         'title': 'Resolutions'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Free modules' and 'Examples' in one rigorous "
                                                 'argument.',
                                       'solution': 'The argument begins with A free module is a direct sum of copies of the ring '
                                                   'with a distinguished basis. It then uses the later viewpoint: Free modules, '
                                                   'ideals generated by idempotents, and vector bundles over affine rings '
                                                   'illustrate projectivity. The bridge is supplied by the structural theorems '
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
                                   'prompt': 'Prove: An $A$-module $P$ is projective iff it is a direct summand of a free '
                                             'module.',
                                   'solution': 'Choose a free module $F$ surjecting onto $P$. If $P$ is projective, the '
                                               'surjection splits, so $F\\cong P\\oplus K$. Conversely direct summands of free '
                                               'modules inherit the lifting property.',
                                   'title': 'Projective summand criterion proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: A module $P$ is projective iff every short exact sequence $0\\to K\\to '
                                             'M\\to P\\to0$ splits.',
                                   'solution': 'Projectivity lifts the identity map of $P$ through the surjection $M\\to P$, '
                                               'producing a section. Conversely apply the splitting property to pullbacks of '
                                               'arbitrary surjections.',
                                   'title': 'Splitting criterion proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: $P$ is projective iff $\\operatorname{Hom}_A(P,-)$ is an exact functor.',
                                   'solution': 'Hom is always left exact. Exactness on surjections is precisely the lifting '
                                               'property defining projectivity.',
                                   'title': 'Hom exactness criterion proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Projective summand criterion with Splitting '
                                             'criterion. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Projective summand criterion and then applies '
                                               'Splitting criterion; the conclusion follows after checking the shared '
                                               'hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use free modules, projective splittings, and idempotents.',
                                      'prompt': 'Is $R^5$ projective?',
                                      'solution': 'Yes.',
                                      'title': 'Free projective'},
                                     {'hint': 'Use free modules, projective splittings, and idempotents.',
                                      'prompt': 'If $R^4=P\\oplus Q$, is $P$ projective?',
                                      'solution': 'Yes.',
                                      'title': 'Direct summand'},
                                     {'hint': 'Use free modules, projective splittings, and idempotents.',
                                      'prompt': 'What complements $eR$ when $e^2=e$?',
                                      'solution': '$(1-e)R$.',
                                      'title': 'Idempotent complement'},
                                     {'hint': 'Use free modules, projective splittings, and idempotents.',
                                      'prompt': 'Compute $(R^n)_P$.',
                                      'solution': 'It is $R_P^n$.',
                                      'title': 'Localized free'},
                                     {'hint': 'Use free modules, projective splittings, and idempotents.',
                                      'prompt': 'What does a section of $F\\to P$ imply?',
                                      'solution': 'It makes $P$ a direct summand of $F$.',
                                      'title': 'Split quotient'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every projective module is free.',
                                  'solution': 'False over general rings; idempotent summands give examples.',
                                  'title': 'Projective free'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every submodule of a free module is projective over every ring.',
                                  'solution': 'False in general.',
                                  'title': 'Submodule free'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every projective module is finitely generated.',
                                  'solution': 'False: infinite-rank free modules are projective.',
                                  'title': 'Finite generation'}]}},
 'V/14': {'examples': [{'after_section': 2,
                        'body': 'For every multiplicative set $S$, $S^{-1}R$ is flat because $S^{-1}R\\otimes_RM\\cong S^{-1}M$ '
                                'and localization is exact.',
                        'title': 'Localization is flat'},
                       {'after_section': 5,
                        'body': 'Tensor $\\mathbb Z\\xrightarrow{\\cdot2}\\mathbb Z$ with $\\mathbb Z/2$. The induced map is '
                                'zero, so injectivity is lost and $\\mathbb Z/2$ is not flat.',
                        'title': 'Nonflat cyclic module'},
                       {'after_section': 7,
                        'body': 'Flatness can be tested by requiring $I\\otimes_RM\\to M$ to be injective for finitely generated '
                                'ideals $I$. This turns exactness into a relation test.',
                        'title': 'Ideal criterion'}],
          'exercises': {'application': [{'hint': 'Translate the situation into flatness and exactness under tensor product.',
                                         'prompt': 'Why is flatness associated with well-behaved families?',
                                         'solution': 'It prevents new kernel relations from appearing under base change.',
                                         'title': 'Families'},
                                        {'hint': 'Translate the situation into flatness and exactness under tensor product.',
                                         'prompt': 'Why can flatness be checked locally?',
                                         'solution': 'Flatness is local on the base ring.',
                                         'title': 'Local test'}],
                        'challenge': [{'hint': 'State the relevant map, ideal, module, or universal property before drawing the '
                                               'conclusion.',
                                       'prompt': "Connect the chapter ideas 'Definition of flatness' and 'Examples and failures' "
                                                 'in one rigorous argument.',
                                       'solution': 'The argument begins with An $A$-module $F$ is flat if $-\\otimes_A F$ is '
                                                   'exact. It then uses the later viewpoint: Quotient modules are generally not '
                                                   'flat; localization provides the basic positive example. The bridge is '
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
                                   'prompt': 'Prove: Every free $A$-module is flat.',
                                   'solution': 'Tensoring with a direct sum of copies of $A$ gives the corresponding direct sum '
                                               'of the original sequence. Direct sums preserve exactness in modules.',
                                   'title': 'Free implies flat proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: Every projective module is flat.',
                                   'solution': 'A projective module is a direct summand of a free module. Tensoring with the '
                                               'corresponding direct-sum decomposition shows the tensor functor for the '
                                               'projective summand is a direct summand of an exact functor and hence exact.',
                                   'title': 'Projective implies flat proof'},
                                  {'hint': 'Start from the chapter theorem hypotheses and identify the decisive algebraic map or '
                                           'containment.',
                                   'prompt': 'Prove: $S^{-1}A$ is flat as an $A$-module.',
                                   'solution': 'Tensoring with $S^{-1}A$ is localization of modules, and localization is exact.',
                                   'title': 'Localization is flat proof'},
                                  {'hint': 'Apply the first theorem to move to its structural description, then use the second '
                                           'theorem on that description.',
                                   'prompt': 'Prove a short corollary by combining Free implies flat with Projective implies '
                                             'flat. State every hypothesis you use.',
                                   'solution': 'A valid synthesis first invokes Free implies flat and then applies Projective '
                                               'implies flat; the conclusion follows after checking the shared hypotheses.',
                                   'title': 'Structural synthesis'}],
                        'standard': [{'hint': 'Use flatness and exactness under tensor product.',
                                      'prompt': 'Is $R^n$ flat?',
                                      'solution': 'Yes.',
                                      'title': 'Free flat'},
                                     {'hint': 'Use flatness and exactness under tensor product.',
                                      'prompt': 'Is $R_f$ flat over $R$?',
                                      'solution': 'Yes.',
                                      'title': 'Localization flat'},
                                     {'hint': 'Use flatness and exactness under tensor product.',
                                      'prompt': 'What must a flat tensor functor do to injections?',
                                      'solution': 'It must preserve them.',
                                      'title': 'Injection preservation'},
                                     {'hint': 'Use flatness and exactness under tensor product.',
                                      'prompt': 'Is $\\mathbb Z/3$ flat over $\\mathbb Z$?',
                                      'solution': 'No.',
                                      'title': 'Integer quotient'},
                                     {'hint': 'Use flatness and exactness under tensor product.',
                                      'prompt': 'Is a direct sum of flat modules flat?',
                                      'solution': 'Yes.',
                                      'title': 'Direct sum'}],
                        'test': [{'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Every flat module is projective.',
                                  'solution': 'False: $\\mathbb Q$ is flat but not projective over $\\mathbb Z$.',
                                  'title': 'Flat projective'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Torsion-free is equivalent to flat over every domain.',
                                  'solution': 'False in general.',
                                  'title': 'Torsion-free'},
                                 {'hint': 'Try a smallest standard ring or module from this chapter.',
                                  'prompt': 'Test the claim: Tensoring with any module is exact.',
                                  'solution': 'False: tensor is always right exact, not always left exact.',
                                  'title': 'Tensor exact'}]}}}
