print("\n\nbai 1 ==============================")
import sympy as sp
import numpy as np

A = np.array([[2,0,1],[3,2,-3],[-1,-3,5]])
print(np.linalg.det(A))

A = np.array([[1,0,0],[3,2,-4],[4,1,3]])
print(np.linalg.det(A))

A = np.array([[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]])
print(np.linalg.det(A))


a = sp.Symbol("a")
b = sp.Symbol("b")
c = sp.Symbol("c")
d = sp.Symbol("d")

A = np.array([[1,0,2,a],[2,0,b,0],[3,c,4,5],[d,0,0,0]])
A = sp.Matrix(A)
print(A.det())


a = sp.Symbol("a")
b = sp.Symbol("b")
c = sp.Symbol("c")
d = sp.Symbol("d")
e = sp.Symbol("e")
f = sp.Symbol("f")
g = sp.Symbol("g")
h = sp.Symbol("h")
y = sp.Symbol("y")
k = sp.Symbol("k")
u = sp.Symbol("u")
x = sp.Symbol("x")
v = sp.Symbol("v")
z = sp.Symbol("z")

A = np.array([
    [x,a,b,0,c],
    [0,y,0,0,d],
    [0,e,z,0,f],
    [g,h,k,u,1],
    [0,0,0,0,v]])
A = sp.Matrix(A)
print(A.det())


A = np.array([
    [2,1,1,1,1],
    [1,3,1,1,1],
    [1,1,4,1,1],
    [1,1,1,5,1],
    [1,1,1,1,6]])
print(np.linalg.det(A))

print("\n\nbai 2 ==============================")
import sympy as sp
import numpy as np

a, b, c = sp.symbols('a b c')
A = np.array([
    [a+b,c,1],
    [b+c,a,1],
    [c+a,b,1]])
A = sp.Matrix(A)
print(A.det(), A.det()==0)

x, y, z, p, q, r, a, b = sp.symbols('x y z p q r a b')
A = np.array([
    [x,p,a*x+b*p],
    [y,q,a*y+b*q],
    [z,r,a*z+b*r]])
A = sp.Matrix(A)
print(A.det(), A.det()==0)

a, b, c = sp.symbols('a b c')
A = np.array([
    [a*b,a**2+b**2,(a+b)**2],
    [b*c,b**2+c**2,(b+c)**2],
    [c*a,c**2+a**2,(c+a)**2]])
A = sp.Matrix(A)
print(A.det(), A.det()==0)

a, b, c = sp.symbols('a b c')
A = np.array([
    [a,b,c,1],
    [b,c,a,1],
    [c,a,b,1],
    [c+b,b+a,a+c,2]])
A = sp.Matrix(A)
print(A.det(), A.det()==0)

print("\n\nbai 3 ==============================")
import sympy as sp
import numpy as np

x = sp.symbols('x')
A = np.array([
    [1,x,x**2,x**3],
    [1,2,   4,   8],
    [1,3,   9,  27],
    [1,4,  16,  64]])
A = sp.Matrix(A)
detA = A.det()
ret = sp.solve(detA)
print("x must be one of", ret)

print("\n\nbai 3 ==============================")
import sympy as sp
import numpy as np

m = sp.symbols('m')
A = np.array([
    [1,2,2],
    [-2,m-2,m-5],
    [m,1,m+1]])
A = sp.Matrix(A)
detA = A.det()
ret = sp.solve(detA)
print("m must NOT be one of", ret)

print("\n\nbai 4 ==============================")
import sympy as sp
import numpy as np

m = sp.symbols('m')
A = np.array([
    [1,1,1,m],
    [1,1,m,1],
    [1,m,1,1],
    [m,1,1,1]])
A = sp.Matrix(A)
detA = A.det()
ret = sp.solve(detA)
print("m must NOT be one of", ret)

print("\n\nbai 5 ==============================")
import sympy as sp
import numpy as np

x = sp.symbols('x')
A = np.array([
    [1,x,   x-1,   x+2],
    [0,0,x**2-1,     0],
    [x,1,     x,   x-2],
    [0,0,x**5+1,x**100]])
A = sp.Matrix(A)
detA = A.det()
ret = sp.solve(detA)
print("m must be one of", ret)

print("\n\nbai 6 ==============================")
import sympy as sp
import numpy as np

def crammer(A,b):
    for i in range(A.shape[0]):
        Ai = np.append(A[:,0:i], b, axis=1)
        Ai = np.append(Ai, A[:,i+1:], axis=1)
        print("x_{} = {}".format(i+1,np.linalg.det(Ai)/np.linalg.det(A)))
    print("\n\n")

A  = np.array([
    [1, 1,-2],
    [2, 3,-7],
    [5, 2, 1]]) 
b = np.array([6,16,16]).reshape(3,1)
crammer(A,b)

A  = np.array([
    [ 7,  2, 3],
    [ 5, -3, 2],
    [10,-11, 5]]) 
b = np.array([15,15,36]).reshape(3,1)
crammer(A,b)

A  = np.array([
    [ 1,  1, 2],
    [ 2, -1, 2],
    [ 4,  1, 4]]) 
b = np.array([1,4,2]).reshape(3,1)
crammer(A,b)

A  = np.array([
    [ 3,  2, 1],
    [ 2,  3, 1],
    [ 2,  1, 3]]) 
b = np.array([5,1,11]).reshape(3,1)
crammer(A,b)

A  = np.array([
    [2, 1, 5, 1],
    [1, 1,-3,-4],
    [3, 6,-2, 1],
    [2, 2, 2,-3]]) 
b = np.array([5,-1,8,2]).reshape(4,1)
crammer(A,b)

A  = np.array([
    [1, 1,1,1],
    [1,-2,3,4],
    [4, 1,2,3],
    [3, 2,3,4]]) 
b = np.array([5,3,7,2]).reshape(4,1)
crammer(A,b)

A  = np.array([
    [2,-1, 3, 2],
    [3, 3, 3, 2],
    [3,-1,-1,-1],
    [3,-1, 3,-1]]) 
b = np.array([4,6,6,6]).reshape(4,1)
crammer(A,b)


print("\n\nbai 7 ==============================")
import sympy as sp
import numpy as np

#      Ax = b
# => A'Ax = A'b
# =>    x = A'b
A = np.array([
    [1,1,-3],
    [1,2,-3],
    [2,4,-5]])
b = np.array([-2,6,-6])
b = b.reshape(len(b), 1)
detA = np.linalg.det(A)
if detA != 0:
    x = np.linalg.inv(A).dot(b)
    print(x)
else:
    print("Can NOT solve this by inverse matrix")


A = np.array([
    [1, 1, 1, 1],
    [1, 1,-1,-1],
    [1,-1, 0, 0],
    [0, 0, 1,-1]])
b = np.array([1,1,-1,-1])
b = b.reshape(len(b), 1)
detA = np.linalg.det(A)
if detA != 0:
    x = np.linalg.inv(A).dot(b)
    print(x)
else:
    print("Can NOT solve this by inverse matrix")


A = np.array([
    [1, 1, 1, 1],
    [1, 1,-1,-1],
    [1,-1, 1,-1],
    [1,-1,-1, 1]])
b = np.array([-1,1,-1,1])
b = b.reshape(len(b), 1)
detA = np.linalg.det(A)
if detA != 0:
    x = np.linalg.inv(A).dot(b)
    print(x)
else:
    print("Can NOT solve this by inverse matrix")

print("\n\nbai 8 ==============================")
import sympy as sp
import numpy as np

print("UNIQUE solution <=> rank(A|b) = rank(A) = 3 <=> det(A)!=0")
m = sp.symbols('m')
A = np.array([
    [1,1,-1],
    [2,3,m],
    [1,m,3]])
A = sp.Matrix(A)
detA = A.det()
ret = sp.solve(detA)
print("so, m must NOT be one of", ret)

print("\n\nbai 9 ==============================")
import sympy as sp
import numpy as np

print("No solution <=> rank(A|b) != rank(A)")
# điều kiện cần là det(A)=0. Tìm k, sau đó thế từng giá trị của k vào và kiểm lại
k = sp.symbols('k')
A = np.array([
    [k,1,1],
    [1,k,1],
    [1,1,k]])
b = np.array([1,1,1]).reshape(3,1)
Ab = np.append(A, b, axis=1)
A = sp.Matrix(A)
Ab = sp.Matrix(Ab)
detA = A.det()
ret = sp.solve(detA)
for s in ret:
    rankA = A.subs(k, s).rank()
    rankAb = Ab.subs(k, s).rank()
    print("for k={}:\trankA={}\trankAb={}".format(s,  rankA, rankAb), end='')
    if rankA!=rankAb:
        print("\t: no solution")
    else:
        print("\t: solution exists")

print("\n\nbai 10 ==============================")
import sympy as sp
import numpy as np

print("Infinity solutions <=> rank(A|b) = rank(A) < 4")
# => điều kiện cần là det(A)=0 để A có hạng nhỏ hơn 4.
k = sp.symbols('k')
A = np.array([
    [5,-3, 2, 4],
    [4,-2, 3, 7],
    [8,-6,-1,-5],
    [7,-3, 7,17]])
b = np.array([3,1,9,k]).reshape(4,1)
Ab = np.append(A, b, axis=1)
A = sp.Matrix(A)
Ab = sp.Matrix(Ab)
detA = A.det()
print("detA=", detA)
rankA = A.rank()
rankAb = Ab.rank()
print("rankA={} != rankAb={} for any k,\nso any k would satisfy this requirement".format(rankA, rankAb))


print("\n\nbai 11 ==============================")
import sympy as sp
import numpy as np

print("No solution <=> rank(A|b) != rank(A)")
# điều kiện cần là det(A)=0. Tìm k, sau đó thế từng giá trị của k vào và kiểm lại
k = sp.symbols('k')
A = np.array([
    [3, 2, 5,  4],
    [2, 3, 6,  8],
    [1,-6,-9,-20],
    [4, 1, 4,  k]])
b = np.array([3,5,-11,2]).reshape(4,1)
Ab = np.append(A, b, axis=1)
A = sp.Matrix(A)
Ab = sp.Matrix(Ab)
rrefA = A.rref()
rrefAb = Ab.rref()
print(rrefA)
print(rrefAb)

print("because rankA={}=rankAb={}, so solution exists for a k!=0".format(A.rank(), Ab.rank()))
print("because rankA={} != rankAb={} for k=0, so no solution!".format(A.subs(k,0).rank(), Ab.subs(k,0).rank()))
