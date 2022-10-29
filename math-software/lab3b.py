import numpy as np


A = np.array([[1,2],[-1,0],[2,1]])
B = np.array([[1,3],[2,1],[-3,-2]])
C = np.array([[2,5],[0,3],[4,2]])


print(2*A - 3*B + 2*C)

A = np.array([[2, -1], [1, 0], [-3, 4]])
B = np.array([[1, -2, 5], [3, 4, 0]])

print(A.dot(B))
print(B.dot(A))

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = A.T

print((A+B).T == A.T+B.T)
print((A.dot(B)).T ==B.T.dot(A.T))


def nhap_ma_tran():
    # Nhập kích thước ma trận từ bàn phím
    str = input("Nhập kích thước ma trận: ").strip()
    kich_thuoc = [int(x) for x in str.split()]

    hang_str = input("Nhập tất cả phần tử của ma trận từ trái sang phải từ trên xuống dưới: ")
    hang = [float(x) for x in hang_str.split()]
    ma_tran = np.array(hang).reshape(kich_thuoc)

    return ma_tran

def tich_ma_tran(A, B):
    if A.shape[1] != B.shape[0]:
        print("size of A and B mismatch")
        return None
    return A.dot(B)

A = nhap_ma_tran()
B = nhap_ma_tran()
C = tich_ma_tran(A, B)
print(C)

import sympy

x = sympy.Symbol(x)
y = sympy.Symbol(y)
z = sympy.Symbol(z)