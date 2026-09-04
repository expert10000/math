#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

GOALS = {
"I/01": [
"compute linear combinations in \\(\\mathbb R^n\\), polynomial spaces, and other concrete vector spaces;",
"decide whether a target vector lies in the span of a finite list by solving the coefficient equations;",
"rewrite a vector equation as a linear system and interpret its solution set in terms of linear combinations;",
"describe the set of all linear combinations of one, two, or three given vectors parametrically;",
"construct examples showing how the same abstract vector can have different coordinate descriptions;",
"identify when a proposed operation fails one of the vector-space axioms by producing a concrete counterexample;",
],
"I/02": [
"determine whether a subset is a subspace using both the three-condition and linear-combination tests;",
"compute sums and intersections of explicitly presented subspaces;",
"find all linear relations among a finite list;",
"extract a minimal generating list from a redundant spanning list;",
"construct a counterexample showing that a union of subspaces need not be a subspace;",
"translate between dependence relations and solutions of homogeneous systems;",
],
"I/03": [
"test whether a finite list is a basis by checking both spanning and independence;",
"extend an independent list to a basis and reduce a spanning list to a basis;",
"compute the dimension of a subspace from an explicit spanning set or homogeneous system;",
"prove that two bases of a finite-dimensional vector space have the same number of vectors;",
"apply the dimension formula to compute \\(\\dim(U+W)\\) or \\(\\dim(U\\cap W)\\);",
"decide whether an injective or surjective linear map can exist from dimension data alone;",
],
"I/04": [
"compute the coordinate vector of an abstract vector relative to a specified ordered basis;",
"construct a change-of-basis matrix from one ordered basis to another;",
"convert coordinate vectors between two bases using the change-of-basis matrix and its inverse;",
"derive the similarity relation between matrices of the same operator in different bases;",
"choose a basis adapted to a subspace or decomposition in order to simplify coordinates;",
"detect and correct an invalid change-of-basis computation by checking what the columns represent;",
],
"I/05": [
"verify or refute linearity by testing additivity and homogeneity;",
"determine a linear transformation uniquely from its values on a basis;",
"construct a linear map satisfying prescribed images of basis vectors;",
"compute compositions of linear transformations and identify when two maps commute;",
"decide whether a proposed inverse map is linear and actually inverts the original transformation;",
"translate geometric actions such as projections, reflections, and coordinate permutations into linear maps;",
],
"I/06": [
"compute bases for the kernel and image of a linear transformation;",
"use rank-nullity to determine missing dimensions and to test consistency of computed bases;",
"decide injectivity from the kernel and surjectivity from the image;",
"prove that a finite-dimensional map is an isomorphism from equivalent injective, surjective, or rank conditions;",
"construct an explicit isomorphism between two vector spaces of the same finite dimension;",
"relate solutions of \\(Tx=b\\) to one particular solution plus the kernel of \\(T\\);",
],
"I/07": [
"construct the matrix of a linear map from its action on a basis;",
"recover the action of a linear map from its matrix and coordinate conventions;",
"compute the matrix of a composition and explain why matrix multiplication appears in that order;",
"change the matrix of an operator when the basis changes;",
"identify the column space and null space of a matrix as image and kernel data of the associated map;",
"check a matrix representation by applying it to basis vectors and comparing the resulting coordinates;",
],
"I/08": [
"compute determinants efficiently using row operations, triangular form, or cofactor expansion;",
"track the effect of row swaps, row scalings, and row additions on the determinant;",
"use the determinant to decide invertibility and linear independence for square matrices;",
"prove and apply multiplicativity \\(\\det(AB)=\\det(A)\\det(B)\\);",
"compute traces and use cyclicity \\(\\operatorname{tr}(AB)=\\operatorname{tr}(BA)\\) in concrete identities;",
"interpret determinant and trace as basis-independent invariants of a linear operator;",
],
"I/09": [
"compute eigenvalues from the characteristic polynomial and compute a basis for each eigenspace;",
"distinguish algebraic multiplicity from geometric multiplicity in explicit examples;",
"prove that eigenvectors belonging to distinct eigenvalues are linearly independent;",
"decide whether a given vector or subspace is preserved by an operator using eigenvector information;",
"construct examples with repeated eigenvalues that are or are not diagonalizable;",
"check an eigenpair directly and diagnose arithmetic errors by substituting back into \\(Tv=\\lambda v\\);",
],
"I/10": [
"test whether a subspace is invariant under a given operator;",
"construct a basis adapted to an invariant subspace and derive the resulting block or triangular matrix form;",
"read eigenvalues from the diagonal of a triangular matrix;",
"prove that an operator is triangularizable when its characteristic polynomial splits over the scalar field;",
"build an invariant flag one subspace at a time from eigenvectors and quotient-space reasoning;",
"distinguish triangularizability from diagonalizability by giving explicit examples;",
],
"I/11": [
"decide diagonalizability from eigenspace dimensions and from the minimal polynomial;",
"construct a diagonalizing basis when enough independent eigenvectors exist;",
"compute the minimal polynomial from annihilating relations or a known canonical form;",
"use the minimal polynomial to reduce high powers or polynomial expressions in an operator;",
"prove that a split operator is diagonalizable exactly when its minimal polynomial has no repeated root;",
"compare characteristic and minimal polynomials without assuming that they are equal;",
],
"I/12": [
"compute generalized eigenspaces using kernels of powers of \\(T-\\lambda I\\);",
"construct Jordan chains and assemble them into a Jordan basis when the scalar field permits;",
"recover Jordan-block sizes from the growth of \\(\\dim\\ker(T-\\lambda I)^k\\);",
"write the Jordan form of a nilpotent operator from its chain lengths;",
"use canonical form to compute powers, exponentials, or polynomial functions of an operator;",
"explain which data are invariant under similarity and therefore belong to the operator rather than a chosen basis;",
],
"I/13": [
"verify that a proposed formula defines an inner product;",
"compute norms, distances, and angles from an inner product;",
"prove orthogonality statements using bilinearity or sesquilinearity and conjugate symmetry;",
"compute orthogonal complements of explicitly described subspaces;",
"apply Cauchy--Schwarz and the triangle inequality with equality conditions;",
"decompose a vector relative to an orthogonal direct sum and verify the Pythagorean identity;",
],
"I/14": [
"perform the Gram--Schmidt process on an independent list and verify that successive spans are preserved;",
"compute orthogonal projections onto lines and higher-dimensional subspaces from an orthonormal basis;",
"prove the best-approximation property by decomposing the error into orthogonal components;",
"construct a projection matrix and verify that it is idempotent and self-adjoint;",
"derive a reduced QR factorization from Gram--Schmidt;",
"solve a least-squares problem using projection, normal equations, or QR and compare the numerical consequences;",
],
"I/15": [
"test whether a real or complex matrix is orthogonal or unitary using \\(A^*A=I\\);",
"prove that orthogonal and unitary operators preserve inner products, norms, and angles;",
"compute the inverse of an orthogonal or unitary matrix from its adjoint;",
"classify simple planar orthogonal maps as rotations or reflections;",
"show that every eigenvalue of a unitary operator has modulus one;",
"construct examples distinguishing orthogonal/unitary operators from merely diagonalizable ones;",
],
"I/16": [
"recognize self-adjoint, normal, and unitary operators from matrix identities;",
"find an orthonormal eigenbasis for a concrete self-adjoint or normal matrix;",
"unitarily or orthogonally diagonalize an operator covered by the spectral theorem;",
"write a spectral decomposition in terms of eigenspace projections;",
"use orthogonal eigenspaces to simplify powers and functions of a normal operator;",
"identify precisely which hypothesis fails when an operator does not admit an orthonormal eigenbasis;",
],
"I/17": [
"associate a symmetric or Hermitian matrix with a quadratic form and recover the form from the matrix;",
"diagonalize a quadratic form by an orthogonal or unitary change of coordinates when appropriate;",
"classify a real quadratic form as positive definite, negative definite, semidefinite, or indefinite;",
"apply eigenvalues or Sylvester-type criteria to decide definiteness;",
"compute the signature and identify its invariance under congruence;",
"transform a quadratic expression to principal-axis form and interpret the resulting geometry;",
],
"I/18": [
"compute singular values from the eigenvalues of \\(A^*A\\);",
"construct left and right singular vectors and assemble a singular-value decomposition;",
"read rank, operator norm, and null-space information from the singular values;",
"compute the Moore--Penrose pseudoinverse from an SVD;",
"solve a least-squares problem with the pseudoinverse, including rank-deficient cases;",
"form and interpret the best low-rank approximation obtained by truncating the SVD;",
],
}

BANNED_HINT = "Identify the definition or structural theorem in this chapter that directly controls the question, then reduce the calculation to that statement."

CHAPTER_FALLBACKS = {
"I/01": [
"Write the target as \\(a_1v_1+\\cdots+a_rv_r\\) and compare coordinates before solving for the coefficients.",
"Separate the scalar coefficients from the vectors first; the vector equation is a system of scalar equations.",
"Parameterize the coefficients rather than guessing individual vectors in the span.",
"Test the proposed identity componentwise; one failed coordinate is enough to refute it.",
"Translate the vector relation into an augmented matrix and row-reduce only after writing the correct columns.",
"Look for a coefficient choice that isolates one of the listed vectors or exposes a contradiction.",
"Check whether the alleged vector-space operation respects the zero vector before testing the harder axioms.",
"Use two different coefficient choices to decide whether the representation is unique.",
],
"I/02": [
"Take two arbitrary vectors from the intersection and test an arbitrary linear combination in every member of the family.",
"Assume neither subspace contains the other; choose \\(u\\in U\\setminus W\\) and \\(w\\in W\\setminus U\\), then test \\(u+w\\).",
"Write a general combination of the generators and eliminate the free coefficients to obtain equations for the span.",
"Set up one coefficient equation for each polynomial coefficient; a nonzero solution is exactly a dependence relation.",
"Give the zero vector coefficient \\(1\\) and every other vector coefficient \\(0\\).",
"Check whether one vector is a scalar multiple of the other before doing any row reduction.",
"Use the minimality property of span twice: first show the span lies in every containing subspace, then use that the span itself is one of them.",
"Translate column independence into the homogeneous system \\(Ax=0\\); free variables are the obstruction.",
],
"I/03": [
"Start with the spanning condition and the independence condition separately; a basis requires both.",
"Use the exchange lemma to remove one redundant vector without changing the span, then repeat.",
"Row-reduce a spanning matrix and count pivot columns rather than counting the original generators.",
"Begin with a basis of the smaller subspace and extend it to a basis of the larger one.",
"For the dimension formula, begin with a basis of \\(U\\cap W\\), then extend it separately inside \\(U\\) and \\(W\\).",
"Compare the size of an independent list with the size of a spanning list in the same finite-dimensional space.",
"To test whether a list can be a basis, compare its length with the dimension before doing any computation.",
"Use rank-nullity as a dimension count: injectivity kills the nullity and surjectivity forces full rank.",
],
"I/04": [
"Solve \\(v=a_1b_1+\\cdots+a_nb_n\\); the coefficients you obtain are the coordinate vector.",
"Build the change-of-basis matrix column by column from the new basis vectors written in the old coordinates.",
"Check the direction of the change-of-basis matrix by applying it to a coordinate vector whose answer you know.",
"The inverse change-of-basis matrix reverses the coordinate conversion; verify by composing the two conversions.",
"For an operator matrix, insert identity changes of coordinates on the domain and codomain before simplifying.",
"Similarity should appear as \\(P^{-1}AP\\); determine which side corresponds to changing input coordinates first.",
"An adapted basis should begin with a basis of the distinguished subspace and then be extended to the whole space.",
"Test a proposed formula on each basis vector; a matrix representation is determined by those columns.",
],
"I/05": [
"Check \\(T(u+v)=T(u)+T(v)\\) and \\(T(\\lambda u)=\\lambda T(u)\\) separately; one failure is enough.",
"Write each input vector in the chosen basis and use linearity to extend the prescribed basis values.",
"To construct the map, choose images of basis vectors first; linearity then forces every other value.",
"For a composition, compute the inner map first and keep track of which space each intermediate vector lies in.",
"To test invertibility, verify both \\(ST=I\\) and \\(TS=I\\); one-sided cancellation is not enough in an arbitrary setting.",
"Compare the effect of the two maps on a basis; equality on a basis implies equality everywhere.",
"For a geometric transformation, compute what it does to the standard basis before writing a general formula.",
"If a constant term survives when the input is zero, the map cannot be linear.",
],
"I/06": [
"Set \\(T(v)=0\\) and solve; a basis of the solution space is a basis of the kernel.",
"Generate the image from the images of a basis of the domain, then remove dependent vectors.",
"Use rank-nullity after computing either rank or nullity to check the other dimension.",
"Injectivity is equivalent to \\(\\ker T=\\{0\\}\\); try to prove or refute exactly that statement.",
"Surjectivity asks whether the image spans the codomain; compare its dimension with \\(\\dim W\\).",
"In equal finite dimensions, show that injective \\(\\Rightarrow\\) full rank \\(\\Rightarrow\\) surjective.",
"To build an isomorphism, send one basis bijectively to another basis and extend linearly.",
"For \\(Tx=b\\), subtract two solutions; their difference lies in the kernel.",
],
"I/07": [
"The \\(j\\)-th matrix column is the coordinate vector of \\(T(b_j)\\) in the codomain basis.",
"Multiply the matrix by a coordinate vector only after confirming which basis those coordinates use.",
"For composition, apply the rightmost matrix first; this mirrors the order of the functions.",
"Check matrix dimensions before multiplying; they encode the domain and codomain compatibility.",
"To change basis, convert input coordinates, apply the old matrix, then convert the output coordinates.",
"The null space and column space are just the kernel and image of the associated linear map.",
"Recover the map by applying the matrix to each standard basis vector and reading off the columns.",
"Test a proposed representation on basis vectors; if one column is wrong, the whole matrix is wrong.",
],
"I/08": [
"Use row operations to reach triangular form, but record which operations change the determinant and how.",
"Expand along a row or column with the most zeros rather than using a full permutation formula.",
"A square matrix is singular exactly when its determinant vanishes; connect that to a nontrivial kernel.",
"For \\(\\det(AB)\\), first handle the invertible case or use the effect of elementary matrices.",
"The determinant of a triangular matrix is the product of its diagonal entries.",
"For trace, write the diagonal entries of \\(AB\\) and interchange the summation indices to compare with \\(BA\\).",
"Similarity preserves determinant and trace because the factors \\(P\\) and \\(P^{-1}\\) cancel inside these invariants.",
"Use determinant as a quick consistency check for an alleged inverse: \\(\\det(A^{-1})=1/\\det(A)\\).",
],
"I/09": [
"Form \\(\\det(A-\\lambda I)\\) first; only after finding \\(\\lambda\\) should you solve \\((A-\\lambda I)v=0\\).",
"Substitute the proposed pair back into \\(Av=\\lambda v\\) before doing any further theory.",
"For a repeated eigenvalue, compute the eigenspace dimension; multiplicity in the polynomial alone does not decide diagonalizability.",
"To prove independence, apply a polynomial in \\(T\\) that kills all but one eigencomponent.",
"An eigenspace is a kernel: \\(E_\\lambda=\\ker(T-\\lambda I)\\). Use kernel methods to find a basis.",
"Distinct eigenvalues give distinct invariant directions; try a linear relation and apply \\(T\\).",
"Compare the sum of eigenspace dimensions with the dimension of the whole space.",
"For triangular matrices, read candidate eigenvalues from the diagonal before computing eigenvectors.",
],
"I/10": [
"Test invariance by applying \\(T\\) to a basis of the subspace; every image must remain in the subspace.",
"Choose a basis of the invariant subspace first and extend it to a basis of the whole space.",
"With an adapted basis, entries below the relevant block vanish because vectors in the invariant subspace cannot leave it.",
"For a triangular matrix, the characteristic polynomial is the product of \\((\\lambda-a_{ii})\\).",
"Build the invariant flag one eigenvector at a time; then pass to the induced map on a quotient.",
"Triangularizable does not mean diagonalizable: look for a nonzero Jordan off-diagonal entry.",
"Over a field where the characteristic polynomial splits, start with one eigenvector and induct on dimension.",
"Check whether the proposed subspace is generated by eigenvectors; such a span is automatically invariant.",
],
"I/11": [
"Compute the eigenspace dimension for each eigenvalue and compare the total with \\(\\dim V\\).",
"A split operator is diagonalizable exactly when the minimal polynomial has distinct linear factors.",
"To find the minimal polynomial, start from the characteristic polynomial and test lower-degree divisors that still annihilate the operator.",
"Reduce high powers of \\(T\\) modulo the minimal polynomial instead of multiplying matrices repeatedly.",
"If \\(T=PDP^{-1}\\), powers and polynomials of \\(T\\) are obtained by applying the same function to \\(D\\).",
"Repeated roots in the characteristic polynomial are harmless if the minimal polynomial has no repeated factor.",
"Use the smallest annihilating polynomial; the characteristic polynomial always annihilates by Cayley--Hamilton but need not be minimal.",
"To refute diagonalizability, exhibit either too few eigenvectors or a repeated factor in the minimal polynomial.",
],
"I/12": [
"Compute \\(\\ker(T-\\lambda I)^k\\) for successive \\(k\\); the growth records the generalized eigenvectors.",
"A Jordan chain satisfies \\((T-\\lambda I)v_1=0\\) and \\((T-\\lambda I)v_{j+1}=v_j\\).",
"For a nilpotent operator, the largest Jordan block size is the nilpotency index.",
"Use differences of successive kernel dimensions to count how many Jordan chains have length at least \\(k\\).",
"After finding chain generators, order each chain from eigenvector to highest generalized eigenvector before forming the basis.",
"To compute a matrix function on a Jordan block, separate the scalar part \\(\\lambda I\\) from the nilpotent part.",
"Similarity invariants include the eigenvalues and Jordan-block sizes, not the individual basis vectors in the chains.",
"Check the total sizes of all blocks against \\(\\dim V\\); this catches missing generalized eigenvectors.",
],
"I/13": [
"Verify positivity, conjugate symmetry, and linearity in the correct argument; do not assume symmetry in the complex case.",
"Compute the norm from \\(\\|v\\|^2=\\langle v,v\\rangle\\) before using an angle formula.",
"To show orthogonality, compute the inner product directly and simplify before normalizing anything.",
"Find \\(U^\\perp\\) by imposing \\(\\langle x,u_j\\rangle=0\\) for a basis \\(u_j\\) of \\(U\\).",
"For Cauchy--Schwarz, consider \\(\\|u-tv\\|^2\\ge0\\) and choose \\(t\\) to minimize the quadratic.",
"Equality in Cauchy--Schwarz occurs exactly when the two vectors are linearly dependent.",
"Use orthogonality to kill the cross term when expanding \\(\\|u+w\\|^2\\).",
"For a direct-sum decomposition, prove both orthogonality and that the dimensions add correctly.",
],
"I/14": [
"At each Gram--Schmidt step, subtract only the components along the orthonormal vectors already constructed.",
"For projection onto a line spanned by unit \\(u\\), start with \\(P(v)=\\langle v,u\\rangle u\\).",
"Compute the residual \\(v-P_Uv\\) and test its inner product with every basis vector of \\(U\\).",
"Decompose \\(v-u=(v-P_Uv)+(P_Uv-u)\\); then use orthogonality and Pythagoras.",
"In reduced QR for an \\(m\\times n\\) full-column-rank matrix, count the orthonormal columns of \\(Q\\) before deciding dimensions.",
"Compare \\(\\kappa(A^*A)\\) with \\(\\kappa(A)\\); forming the normal equations squares the condition number.",
"After one projection the vector is already in \\(U\\); apply \\(P\\) once more.",
"Use \\(v=P_Uv+(v-P_Uv)\\) and identify the second term as the \\(U^\\perp\\) component.",
],
"I/15": [
"Compute \\(A^*A\\); orthogonal or unitary means this product is exactly the identity.",
"Use \\(\\langle Ux,Uy\\rangle=\\langle x,y\\rangle\\) to deduce norm and angle preservation.",
"For a unitary matrix, the inverse is \\(A^*\\); verify both products equal \\(I\\).",
"In the plane, use determinant \\(\\pm1\\) together with the trace or fixed directions to distinguish rotations from reflections.",
"If \\(Uv=\\lambda v\\), compare \\(\\|Uv\\|\\) with \\(\\|v\\|\\) to constrain \\(|\\lambda|\\).",
"Columns of a unitary matrix form an orthonormal basis; test them with inner products.",
"Products of unitary operators remain unitary because the adjoint reverses multiplication order.",
"To disprove unitarity, it is enough to find one vector whose norm is not preserved.",
],
"I/16": [
"Check the adjoint identity first: self-adjoint means \\(A^*=A\\), normal means \\(A^*A=AA^*\\).",
"For a self-adjoint matrix, compute eigenspaces and then orthonormalize within repeated-eigenvalue eigenspaces.",
"Eigenvectors for distinct eigenvalues of a self-adjoint operator are orthogonal; use that before Gram--Schmidt.",
"Write the operator as \\(\\sum_\\lambda \\lambda P_\\lambda\\), where \\(P_\\lambda\\) projects onto the eigenspace.",
"To compute \\(f(T)\\), apply \\(f\\) to each eigenvalue in the spectral decomposition.",
"Normality is exactly the hypothesis for unitary diagonalization over \\(\\mathbb C\\).",
"Check that the chosen eigenvectors are not merely independent but orthonormal.",
"If a matrix is triangular and normal, compare off-diagonal norm contributions to show it must be diagonal.",
],
"I/17": [
"Write the quadratic form as \\(x^TAx\\) with \\(A\\) symmetric by averaging the mixed-term coefficients.",
"Diagonalize the symmetric matrix orthogonally; the diagonal entries are the principal quadratic coefficients.",
"For definiteness, inspect the signs of all eigenvalues rather than individual matrix entries.",
"Use leading principal minors only when the hypotheses of Sylvester's criterion apply.",
"Under a congruence transformation \\(A\\mapsto P^TAP\\), count positive and negative squares rather than eigenvalues themselves.",
"Complete the square one variable at a time if an orthogonal diagonalization is unnecessary.",
"The signature is the number of positive squares minus the number of negative squares after diagonalization.",
"Test the form on strategically chosen vectors to refute positive or negative definiteness quickly.",
],
"I/18": [
"Compute \\(A^*A\\); the singular values are the square roots of its nonnegative eigenvalues.",
"Choose orthonormal eigenvectors of \\(A^*A\\) as right singular vectors, then set \\(u_i=Av_i/\\sigma_i\\) for \\(\\sigma_i>0\\).",
"Count the nonzero singular values; that number is the rank.",
"The operator norm induced by the Euclidean norm is the largest singular value.",
"For the pseudoinverse, reciprocate only the nonzero singular values and transpose the SVD factors.",
"In a rank-deficient least-squares problem, the pseudoinverse selects the minimum-norm coefficient vector.",
"For best rank-\\(k\\) approximation, keep the \\(k\\) largest singular values and discard the rest.",
"Verify the SVD by multiplying \\(U\\Sigma V^*\\) and by checking that the columns of \\(U\\) and \\(V\\) are orthonormal.",
],
}

RULES = [
    (r"union.*subspace|subspace.*union", "Assume neither subspace contains the other; choose one vector from each set difference and test whether their sum stays in the union."),
    (r"intersection.*subspace|subspace.*intersection", "Take two arbitrary vectors in the intersection and test an arbitrary linear combination inside every defining subspace."),
    (r"best.approx|closest|minimi[sz].*distance", "Decompose the error into the projection residual and a vector inside the subspace; orthogonality turns the norm square into a Pythagorean sum."),
    (r"gram.?schmidt", "At the next Gram--Schmidt step, subtract projections onto the orthonormal vectors already obtained before normalizing the residual."),
    (r"normal equations|least.?squares", "Use that the least-squares residual must be orthogonal to the column space, so apply \\(A^*\\) to \\(b-Ax\\)."),
    (r"projection.*idempot|p\^2|project.*again", "After the first projection, the vector already lies in the target subspace; project that vector one more time."),
    (r"i-p|u\^\\perp|orthogonal complement", "Use the orthogonal decomposition \\(v=P_Uv+(v-P_Uv)\\) and identify where the residual lies."),
    (r"determinant.*depend|depend.*determinant|linearly dependent.*matrix", "Place the vectors as columns and ask when the determinant vanishes; that is exactly the dependence condition in the square case."),
    (r"pivot|free variable|homogeneous system", "Translate the statement into \\(Ax=0\\). Pivot columns and free variables tell you whether a nonzero coefficient vector exists."),
    (r"minimal polynomial.*diagonal|diagonal.*minimal polynomial", "Factor the minimal polynomial. Diagonalizability requires the split factors to be distinct."),
    (r"distinct eigenvalues|eigenvectors.*independent", "Start with a shortest linear relation among the eigenvectors and apply \\(T-\\lambda I\\) for one of the eigenvalues."),
    (r"eigenvalue|eigenvector|eigenspace", "First determine \\(\\lambda\\) from \\(\\det(A-\\lambda I)=0\\), then solve \\((A-\\lambda I)v=0\\) for the eigenspace."),
    (r"unitary|orthogonal operator|orthogonal matrix", "Compute \\(A^*A\\) and compare it with \\(I\\); this single identity packages preservation of the inner product."),
    (r"spectral theorem|self-adjoint|normal matrix|normal operator", "Find the eigenspaces first and use orthogonality between distinct eigenspaces before assembling an orthonormal eigenbasis."),
    (r"quadratic form|positive definite|negative definite|signature", "Pass to the symmetric or Hermitian matrix of the form and inspect its eigenvalues or a valid definiteness criterion."),
    (r"singular value|svd|pseudoinverse", "Start from \\(A^*A\\): its orthonormal eigenvectors are right singular vectors and its eigenvalues are the squared singular values."),
    (r"rank-nullity|nullity|kernel.*dimension|image.*dimension", "Compute whichever of rank or nullity is easier, then use \\(\\dim V=\\operatorname{rank}T+\\operatorname{nullity}T\\) as the dimension check."),
    (r"kernel", "Set the output equal to zero and solve the resulting homogeneous equations; the solution vectors generate the kernel."),
    (r"image|range", "Apply the map to a basis of the domain and extract an independent spanning list from the resulting vectors."),
    (r"change.of.basis|coordinate.*basis|basis.*coordinate", "Write each new basis vector in the old coordinates and use those coordinate columns to build the conversion matrix."),
    (r"trace.*ab|tr\\(ab\\)|cyclic", "Write the diagonal entries of \\(AB\\) as a double sum and interchange the summation indices."),
    (r"determinant|\\bdet\\b", "Reduce to triangular form while recording how each row operation changes the determinant."),
    (r"invariant subspace|invariant", "Apply the operator to a basis of the proposed subspace; invariance means every resulting vector stays in its span."),
    (r"triangular", "Choose a basis adapted to the invariant flag; the vanishing entries below the diagonal encode preservation of the successive subspaces."),
    (r"jordan|generalized eigen", "Compute kernels of successive powers of \\(T-\\lambda I\\); their dimension growth reveals the generalized-eigenvector chains."),
    (r"inner product|cauchy|orthogonal", "Write the relevant inner products explicitly and use bilinearity or sesquilinearity before simplifying norms or angles."),
]

def clean_text(s: str) -> str:
    s = re.sub(r"%.*", "", s)
    s = re.sub(r"\\label\{[^}]+\}", "", s)
    return re.sub(r"\s+", " ", s).strip()

def replace_learning_goals(text: str, code: str) -> str:
    goals = GOALS[code]
    block = [
        r"\section*{Learning goals}",
        "After this chapter, the reader should be able to:",
        r"\begin{itemize}",
    ]
    block += [rf"\item {g}" for g in goals]
    block += [r"\end{itemize}", ""]
    replacement = "\n".join(block)
    pattern = re.compile(
        r"\\section\*\{Learning goals\}.*?(?=\\section\*\{Conceptual roadmap\})",
        re.S,
    )
    if not pattern.search(text):
        raise RuntimeError(f"{code}: learning-goals block not found")
    return pattern.sub(lambda m: replacement, text, count=1)

def make_hint(code: str, idx: int, exercise: str, solution: str) -> str:
    hay = (clean_text(exercise) + " " + clean_text(solution)).lower()
    fallback = CHAPTER_FALLBACKS[code][idx - 1]
    for pat, hint in RULES:
        if re.search(pat, hay, re.I):
            # Pair a theorem/algorithmic cue with the unique exercise-specific
            # fallback. This preserves mathematical usefulness and guarantees
            # globally distinct hint text.
            return hint + " " + fallback
    return fallback

TRIAD = re.compile(
    r"(\\begin\{exercise\}\\label\{(?P<label>exr:i(?P<ch>\d{2})-(?P<idx>\d{2}))\}(?P<exercise>.*?)\\end\{exercise\}\s*)"
    r"(\\begin\{hint\}(?P<hint>.*?)\\end\{hint\}\s*)"
    r"(\\begin\{solution\}(?P<solution>.*?)\\end\{solution\})",
    re.S,
)

def replace_hints(text: str, code: str) -> tuple[str, int]:
    changed = 0
    def repl(m):
        nonlocal changed
        idx = int(m.group("idx"))
        if int(m.group("ch")) != int(code.split("/")[1]):
            return m.group(0)
        new_hint = make_hint(code, idx, m.group("exercise"), m.group("solution"))
        changed += 1
        return (
            m.group(1)
            + "\\begin{hint}\n"
            + new_hint
            + "\n\\end{hint}\n"
            + m.group(8)
        )
    out = TRIAD.sub(repl, text)
    return out, changed

def read_status(repo: Path):
    path = repo / "editorial" / "CHAPTER_STATUS.tsv"
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def canonical_paths(repo: Path):
    rows = read_status(repo)
    found = {}
    for row in rows:
        code = row.get("chapter_code", "")
        if code in GOALS:
            if row.get("status") != "FROZEN" or row.get("next_action") != "COMPLETE":
                raise RuntimeError(f"{code}: expected FROZEN/COMPLETE")
            found[code] = repo / row["canonical_path"]
    missing = sorted(set(GOALS) - set(found))
    if missing:
        raise RuntimeError(f"Missing Volume I status rows: {missing}")
    return found

def apply(repo: Path, mode: str, start: int, end: int):
    paths = canonical_paths(repo)
    summary = []
    for n in range(start, end + 1):
        code = f"I/{n:02d}"
        p = paths[code]
        text = p.read_text(encoding="utf-8-sig")
        before = text
        hint_count = 0
        if mode in ("goals", "all"):
            text = replace_learning_goals(text, code)
        if mode in ("hints", "all"):
            text, hint_count = replace_hints(text, code)
            if hint_count != 8:
                raise RuntimeError(f"{code}: expected 8 exercise hints, changed {hint_count}")
        if text != before:
            p.write_text(text.rstrip() + "\n", encoding="utf-8")
        summary.append({"chapter_code": code, "changed": text != before, "hints_replaced": hint_count})
    return summary

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--mode", choices=("goals", "hints", "all"), required=True)
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--end", type=int, default=18)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    summary = apply(repo, args.mode, args.start, args.end)
    print(json.dumps(summary, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
