# bai them
import sympy as sp
import numpy as np

m=sp.symbols('m')
A=[]
print("Matrix:")
R = int(input("Số hàng: "))
C = int(input("Số cột: "))
A =sp.Matrix([[input() for x in range (C)] for y in range(R)])
detA = A.det()
ret = sp.solve(detA)
print("so, m must be one of", ret)
