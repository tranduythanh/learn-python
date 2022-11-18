# Bài 1
# Câu a: Có thể tính được các tích ma trận sau:  AB, BA, CA, BC 
# Câu b:
import sympy as sp
import numpy as np

A = np.array(   [[2,-1,3],
                 [0,1 ,2]])
B = np.array([  [-2,1],
                [0 ,2],
                [1 ,-1]])
C = np.array([  [1,1],
                [0,1]])

ab = A.dot(B)
abc = A.dot(B).dot(C)

print("AB=", ab)
print("ABC=", abc)
# Câu c
print("(AB)^3=", ab.dot(ab).dot(ab))

# Câu d
at = A.T
print("Ma trận chuyển vị của A là: ", at)
atc = A.T.dot(C)
print("A^T * C=", atc)



# Bài 2:
import sympy as sp
import numpy as np

a, b = sp.symbols('a b')
A = sp.matrices.Matrix(np.array([[1, -2],[3, -4]]))
B = sp.matrices.Matrix(np.array([[1,  b],[a, -4]]))

ret = sp.solve(A - B, (a, b))
print("kết quả: ", ret)

# Bài 3

import sympy as sp
import numpy as np

x = sp.symbols('x')

A = np.array([  [1, x, x**2, x**3],
                [1, 2,    4,    8],
                [1, 3,    9,   27],
                [1, 4,   16,   64]])
A = sp.Matrix(A)
ret = sp.solve(A.det(), x)
print("x phải là một trong số các giá trị sau: ", ret)

# Bài 4
import sympy as sp
import numpy as np

def replaceMatrixColumn(A, i, b):
    bi = b.reshape(A.shape[0], 1)
    Ai = np.append(A[:,0:i], bi, axis=1)
    Ai = np.append(Ai, A[:,i+1:], axis=1)
    return Ai

def solveAb(A, b):
    detA = np.linalg.det(A)
    for i in range(A.shape[0]):
        Ai = replaceMatrixColumn(A, i, b)
        detAi = np.linalg.det(Ai)
        x = detAi/detA
        print("x{} = {}".format(i+1, x))

print("câu 4a")
A = np.array([  [1,1,-2],
                [2,3,-7],
                [5,2, 1]])
b = np.array([6,16,16])
solveAb(A, b)

print("\ncâu 4b")
A = np.array([  [7,   2, 3],
                [5,  -3, 2],
                [10,-11, 5]])
b = np.array([15,15,36])
solveAb(A, b)



# Bài 5

# Hệ có nghiệm duy nhất khi A có hạng bằng 3, tức là det(A) phải khác không.
import sympy as sp
import numpy as np

m = sp.symbols('m')

A = np.array([  [1, 1, -1],
                [2, 3,  m],
                [1, m,  3]])
A = sp.Matrix(A)
ret = sp.solve(A.det(), m)
print("m phải KHÁC các giá trị sau: ", ret)


# Bài 7
import sympy as sp
import numpy as np

x = sp.symbols('x')

print("Câu 7a:")
expr = (sp.sqrt(x+2) - sp.cbrt(x+20)) / ((x+9)**(1/4) - 2)
stop = 7
print("Biểu thức gốc : {}".format(expr))
print("Giới hạn khi x->{} : {}".format(stop, sp.limit(expr, x, stop)))


print("\nCâu 7b:")
expr = (sp.sqrt(sp.cos(x*2)) - sp.cbrt(sp.cos(x))) / (x**2)
stop = 0
print("Biểu thức gốc : {}".format(expr))
print("Giới hạn khi x->{} : {}".format(stop, sp.limit(expr, x, stop)))


# Bài 8
import scipy
import math

def f(x):
    return 1/(3*x**2 - 12*x + 39)

print("kết quả tích phân:", scipy.integrate.quad(f, -1, math.inf))

# Bài 6
import sympy as sp
import numpy as np

def safeZones(M):
    zones = []
    for i in range(M.shape[0]):
        for k in range(M.shape[1]):
            if M[i, k] <= 5:
                zones.append([i, k])
    return zones

A = np.array([  [1,1,0,0,1], # cháy rừng
                [3,1,0,1,1],
                [5,2,0,1,2],
                [2,0,1,2,3]])
B = np.array([  [1,1,2,2,1], # lú quét
                [2,2,2,0,2],
                [0,1,2,4,2],
                [1,4,1,2,2]])
C = np.array([  [0,5,1,1,1], # sạt lở
                [0,1,1,1,3],
                [1,3,1,3,1],
                [0,1,3,3,0]])
D = np.array([  [3,1,1,0,1], # bệnh dịch
                [5,0,0,3,7],
                [7,0,0,3,5],
                [5,0,3,5,3]])
E = np.array([  [0,0,0,10,0], # lộ bí mật
                [0,0,15,0,0],
                [0,5,15,5,0],
                [0,20,5,0,0]])

ret = E
print("a. An toàn ngắn hạn 1-2 ngày    :{}\n".format(safeZones(ret)), ret)
ret = A+B+C+D
print("\nb. An toàn tập luyện thời bình:{}\n".format(safeZones(ret)), ret)
ret = A+D
print("\nc. An toàn trong mùa khô      :{}\n".format(safeZones(ret)), ret)
ret = B+C+D
print("\nd. An toàn trong mùa mưa      :{}\n".format(safeZones(ret)), ret)
ret = A+B+C+D+E
print("\ne. An toàn trong 8 tháng      :{}\n".format(safeZones(ret)), ret)