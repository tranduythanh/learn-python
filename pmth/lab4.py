from scipy import linalg
import sympy as sp
import numpy as np

M = np.array([[0.8,0.3],[0.2,0.7]])
P, L, U = linalg.lu(M)
print(P)
print(L)
print(U)


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

A = np.array([[x,a,b,0,c],[0,y,0,0,d],[0,e,z,0,f],[g,h,k,u,1],[0,0,0,0,v]])
A = sp.Matrix(A)
print(A.det())


A = np.array([[2,1,1,1,1],[1,3,1,1,1],[1,1,4,1,1],[1,1,1,5,1],[1,1,1,1,6]])
print(np.linalg.det(A))

import sympy as sp
import numpy as np

m = sp.Symbol("m")
A = np.array([[1,2,2],[-2,m-2,m-5],[m,1,m+1]])
A = sp.Matrix(A)
det = A.det()
ret = sp.solve(det)
print("m must not be one of", ret)

A = np.array([[1,1,1,m],[1,1,m,1],[1,m,1,1],[m,1,1,1]])
A = sp.Matrix(A)
det = A.det()
ret = sp.solve(det)
print("m must not be one of", ret)

x = sp.Symbol("x")
A = np.array([[1,x,x-1,x+2],[0,0,x**2-1,0],[x,1,x,x-2],[0,0,x**2-1,x**100]])
A = sp.Matrix(A)
det = A.det()
ret = sp.solve(det)
print("m must be one of", ret)