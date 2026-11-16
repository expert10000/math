"""Exact checks supporting scoped reviews; requires SymPy, not a proof assistant."""
import sympy as S,json
x,y,t,a,b,c,d,th=S.symbols('x y t a b c d theta',real=True);out={}
# 1: eigenvalues of A^T A are nonnegative, op^2=max and F^2=sum.
out['CP-I-0001']={'argument':'For nonnegative squared singular values, max <= sum <= n*max. Equality max=sum iff rank<=1. Homogeneity and Euclidean Cauchy-Schwarz give the other claims.','zero_operator':'Both norms zero, so equality included.','dependencies':['finite-dimensional Riesz representation','singular value decomposition; positive source dimension n']}
f=x**3+y**3-3*x*y;q=x*x+y*y-x*y-x-y+1
assert S.expand((x+y+1)*q-(f+1))==0
assert S.expand(q-((x-1)**2+(y-1)**2-(x-1)*(y-1)))==0
assert S.Matrix([[1,-S.Rational(1,2)],[-S.Rational(1,2),1]]).eigenvals()=={S.Rational(1,2):1,S.Rational(3,2):1}
assert S.solve([S.diff(f,x),S.diff(f,y)],[x,y])==[(0,0),(1,1)]
xr=3*t/(1+t**3);yr=3*t*t/(1+t**3);assert S.cancel(f.subs({x:xr,y:yr},simultaneous=True))==0
out['CP-I-0002']={'confirmed_error':'At c=-1 the quadratic factor vanishes only at (1,1); the level is line x+y+1=0 union isolated point (1,1), not a nondegenerate ellipse.','quadratic_eigenvalues':['1/2','3/2'],'c0':'Nodal cubic x^3+y^3=3xy, tangent cone -3xy=0. Rational parametrization x=3t/(1+t^3), y=3t^2/(1+t^3) (t!=-1), with origin separately. Current description locates the singularity but does not describe the loop/unbounded branch.'}
A=S.Matrix([[0,a,b],[c,0,d],[x,y,0]]);B=S.diag(0,1,2);C=S.Matrix(3,3,lambda i,j:0 if i==j else A[i,j]/(B[i,i]-B[j,j]));assert B*C-C*B==A
out['CP-I-0003']={'check':'Generic 3x3 zero-diagonal commutator identity holds.','general_reason':'If all vectors are eigenvectors, linearity forces a scalar operator; real trace zero forces scalar zero. Projection to ker f gives a trace-zero endomorphism of dimension n-1, completing induction. Distinct real diagonal entries allow the commutator construction.','zero_and_small_dimensions':'Zero map trivial; nonzero trace-zero map cannot occur in dimension one.'}
A=S.Matrix([[a,b],[c,d]]);assert A.det()==a*d-b*c
out['CP-I-0004']={'hypothesis':'Integer matrix, including singular and negative determinant. Integral homology with standard coordinate-circle basis.','argument':'Integer entries preserve the lattice. Quotient universal property gives continuity. H1 action is A; natural identification H2=exterior^2 H1 gives det A even when singular. H0 identity by connectedness.','source_dependency':'The source invokes degree=det without deriving it; correct with this standard theorem dependency, not an arithmetic error.'}
out['CP-I-0005']={'confirmed_error':'Mixed signs with a zero eigenvalue need not give a hyperboloid: diag(1,-1,0) gives the hyperbolic cylinder u1^2-u2^2=1.','classification':{'(3,0,0)':'ellipsoid','(2,1,0)':'one-sheet hyperboloid','(1,2,0)':'two-sheet hyperboloid','(2,0,1)':'elliptic cylinder','(1,1,1)':'hyperbolic cylinder','(1,0,2)':'two parallel planes','no_positive_eigenvalues':'empty'},'convention':'Triples are counts (positive,negative,zero); all have total 3. Orthogonal coordinate changes and positive rescalings give the listed equations. Positive definite semi-axes stated in source are correct.'}
n=S.Matrix([S.cos(th),S.sin(th),0]);H=S.eye(3)-2*n*n.T;assert (H*H-S.eye(3)).applyfunc(S.trigsimp)==S.zeros(3);assert S.trigsimp(H.det())==-1
H1=S.diag(-1,1,1);prod=(H1*H).applyfunc(S.trigsimp)
assert S.trigsimp(prod[0,0]-S.cos(2*th))==0 and S.trigsimp(prod[0,1]-S.sin(2*th))==0
out['CP-I-0006']={'reflection_checks':'H^2=I and det H=-1 for generic unit normal (cos theta,sin theta,0); general proof uses orthogonal decomposition. -H fixes normal axis and negates its complement.','qualification_required':'When n2=+/-n1 the reflecting planes coincide, their intersection is a plane rather than a unique line, and the composition is I. State this separately. For distinct planes the axis claim holds; rotation sign depends on order/orientation (H(e1)H(n(theta)) has planar angle -2theta in the tested convention).'}
A=S.Matrix([[3,2],[1,1]]);assert S.expand(A.charpoly().as_expr())==S.Symbol('lambda')**2-4*S.Symbol('lambda')+1;assert A.det()==1 and (A-S.eye(2)).det()==-2
for p in [S.Matrix([0,0]),S.Matrix([0,S.Rational(1,2)])]:assert all(v.is_integer for v in (A-S.eye(2))*p)
out['CP-I-0007']={'eigenvalues':['2-sqrt(3)','2+sqrt(3)'],'fixed_points':['(0,0)','(0,1/2)'],'exhaustiveness':'Integer x and 2y integer modulo Z^2 gives exactly these two. det(I-A)=-2 ensures nondegeneracy.'}
matrices=[S.Matrix([[2,1],[1,2]]),S.Matrix([[0,1],[1,0]]),S.Matrix([[1,0],[2,0]]),S.Matrix([[1,1,0],[0,1,1],[1,0,1]])];vectors=[S.Matrix([1,1]),S.Matrix([1,1]),S.Matrix([0,1]),S.ones(3,1)]
for M,v,lam in zip(matrices,vectors,[3,1,0,2]):assert M*v==lam*v
assert list(matrices[3].T*S.ones(3,1))==[2,2,2]
out['CP-I-0008']={'eigenpairs':'All four stated pairs have zero residual.','normalization':'For A4 every simplex point has denominator 2 (column sums 2), so F is globally continuous on the simplex. (1/3,1/3,1/3) is fixed. The zero eigenvalue example for A3 is allowed and is not normalized via F.'}
Ps=[S.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]]),S.diag(1,2,S.Rational(1,2),1),S.Matrix([[1,0,0,0],[1,1,0,0],[0,1,1,0],[0,0,1,1]]),S.Matrix([[1,-1,1,-1],[0,1,-1,1],[0,0,1,-1],[0,0,0,1]])]
Ds=[Ps[0],S.diag(1,S.Rational(1,2),2,1),S.Matrix([[1,0,0,0],[-1,1,0,0],[1,-1,1,0],[-1,1,-1,1]]),S.Matrix([[1,1,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,1]])]
for P,D in zip(Ps,Ds):assert D*P==S.eye(4)
out['CP-I-0009']={'check':'All four displayed dual coefficient matrices D satisfy DP=I exactly. Rows of P^-1, rather than columns, correctly give coefficients of eta_i in xi_k.'}
print(json.dumps({'sympy_version':S.__version__,'results':out},indent=2))
