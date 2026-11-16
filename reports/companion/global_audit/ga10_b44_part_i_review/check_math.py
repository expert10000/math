"""Exact algebra checks for five scoped Part I reviews; requires SymPy."""
import sympy as S,json
from pathlib import Path
out={};t,s,a,b,c=S.symbols('t s a b c');A=S.Matrix([[1,1,1],[t,0,2],[3,t,5]]);rhs=S.Matrix([t,3,7]);x=S.Matrix([(1-2*t)/(t-6),(8-5*t)/(t-6),(t*t+t-9)/(t-6)])
assert S.factor(A.det())==(t-1)*(t-6)
assert all(S.cancel(z)==0 for z in A*x-rhs)
assert A.subs(t,1).rank()==A.subs(t,1).row_join(rhs.subs(t,1)).rank()==2
assert A.subs(t,1)*S.Matrix([3-2*s,s-2,s])==rhs.subs(t,1)
assert A.subs(t,6).rank()==2 and A.subs(t,6).row_join(rhs.subs(t,6)).rank()==3
out['CP-I-0010']={'determinant':str(S.factor(A.det())),'generic_residual':'zero','t1_ranks':[2,2],'t6_ranks':[2,3],'free_family_residual':'zero'}
v1=S.Matrix([S.Rational(1,3),S.Rational(2,3),S.Rational(2,3)]);v2=S.Matrix([0,1/S.sqrt(2),-1/S.sqrt(2)]);v3=S.sqrt(2)/6*S.Matrix([-4,1,1]);assert v1.cross(v2)==v3
for sign in [-1,1]:
 Q=S.Matrix.hstack(v1,v2,sign*v3);assert S.simplify(Q.T*Q)==S.eye(3)
out['CP-I-0011']={'cross_product':str(v3),'both_signs_QtQ':'identity','exhaustiveness':'In real dimension 3, the perpendicular complement of two orthonormal columns is a line; its unit vectors are exactly the two signs.'}
M=S.Matrix([[a,a*a,b*c],[b,b*b,c*a],[c,c*c,a*b]]);target=(a-b)*(b-c)*(c-a)*(a*b+b*c+c*a);assert S.expand(M.det()-target)==0
out['CP-I-0020']={'polynomial_residual':'zero','zero_and_repeated_parameters':'Covered by polynomial identity and multilinearity; no division by parameter differences is needed.'}
u,v,w,z=S.symbols('u v w z');T=S.Matrix([[u,v],[w,z]]);tr=S.trace(T);det=T.det();assert S.expand(T*T-tr*T+det*S.eye(2))==S.zeros(2)
alpha,beta=S.Integer(0),S.Integer(1)
for n in range(9):
 assert (T**n-alpha*T-beta*S.eye(2)).applyfunc(S.expand)==S.zeros(2)
 alpha,beta=S.expand(tr*alpha+beta),S.expand(-det*alpha)
# Repeated-root formula follows algebraically from N^2=0: all binomial terms of degree >=2 vanish.
# This derivation is characteristic-independent (integers act through the field).
out['CP-I-0039']={'cayley_hamilton_polynomial_residual':'zero','recurrence_exact_checks':'powers 0 through 8','general_argument':'Multiply alpha_n A + beta_n I by A and reduce A^2 using Cayley-Hamilton. For A=lambda I+N with N^2=0, only binomial degrees 0,1 survive; lambda=0 gives A^n=0 for n>=2.','limitation':'Finite power checks corroborate; the written induction and square-zero argument establish the general statement.'}
e=S.eye(4);edge=lambda i,j:e[:,i-1]+e[:,j-1];triangle=S.Matrix.hstack(edge(1,2),edge(1,3),edge(2,3));basis=S.Matrix.hstack(edge(1,2),edge(1,3),edge(1,4),edge(2,3));assert triangle.rank()==3 and basis.det()!=0;assert edge(1,2)+edge(3,4)-edge(2,4)-edge(1,3)==S.zeros(4,1)
out['CP-I-0057']={'triangle_rank':3,'basis_determinant':str(basis.det()),'four_cycle_residual':'zero','hypothesis':'Over R as stated; the inference 2a=0 => a=0 would fail in characteristic 2, outside the stated scope.'}
print(json.dumps({'sympy_version':S.__version__,'results':out},indent=2))
