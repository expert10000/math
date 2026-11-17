"""Exact algebra for the illustrative angle and the two plotted quadrics."""
import sympy as s
I=s.eye(3)
i=s.Matrix([1,0,0]);minus=s.Matrix([s.sqrt(3)/2,-s.Rational(1,2),0]);plus=s.Matrix([s.sqrt(3)/2,s.Rational(1,2),0])
H=lambda n:I-2*n*n.T
R=s.Matrix([[s.Rational(1,2),-s.sqrt(3)/2,0],[s.sqrt(3)/2,s.Rational(1,2),0],[0,0,1]])
assert s.simplify(H(i)*H(minus)-R)==s.zeros(3)
assert s.simplify(H(plus)*H(i)-R)==s.zeros(3)
assert H(minus)*i==s.Matrix([-s.Rational(1,2),s.sqrt(3)/2,0])
u,v=s.symbols('u v',real=True)
U=s.cos(u)*s.cos(v)/s.sqrt(2);V=s.cos(u)*s.sin(v)/s.sqrt(3);W=s.sin(u)/s.sqrt(6)
assert s.trigsimp(2*U**2+3*V**2+6*W**2)==1
beta=s.sqrt(s.Rational(2,3))*s.cos(u);gamma=s.sqrt(s.Rational(2,3))*s.sin(u)
assert s.trigsimp(beta**2+gamma**2)==s.Rational(2,3)
print('PASS: both reflection orders, intermediate vector, ellipsoid wireframe and cylinder cross-sections.')
