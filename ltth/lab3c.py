import numpy as np

def bai01():
    A = np.array([[1,2],[-1,0],[2,1]])
    B = np.array([[1,3],[2,1],[-3,-2]])
    C = np.array([[2,5],[0,3],[4,2]])
    print("2*A - 3*B + 2*C = ", 2*A - 3*B + 2*C)

    A = np.array([[2, -1], [1, 0], [-3, 4]])
    B = np.array([[1, -2, 5], [3, 4, 0]])
    print("AB = ", A.dot(B))
    print("BA = ", B.dot(A))

    A = np.array([[1, -3, 2], [3, -4, 1], [2, -5, 3]])
    B = np.array([[2, 5, 6], [1, 2, 5], [1, 3, 2]])
    print("AB = ", A.dot(B))
    print("BA = ", B.dot(A))


def bai02():
    A = np.array([[2,0,1],[3,1,2],[0,-1,0]])
    print("A**2 - 5*A + 3 = ", A**2-5*A+3)


def bai03():
    A = np.array([[2,-1,3],[0,1,2]])
    B = np.array([[-2,1],[0,2],[1,-1]])
    C = np.array([[1,1],[0,1]])

    print("A=", A, "shape=", A.shape)
    print("B=", B, "shape=", B.shape)
    print("C=", C, "shape=", C.shape)

    print("các tích ma trận có thể có: AB, BA, CA, BC, ABC")

    print("AB=",A.dot(B))
    print("ABC=",A.dot(B).dot(C))

    C = A.dot(B)
    print("(AB)^3=", C.dot(C).dot(C))
    print("A^T=", A.T)
    print("(A^T)C=", A.T.dot(C))


def bai04():
    A = np.array([[1,-2,6],[4,3,-8],[2,-2,5]])
    I = np.identity(3)
    X = (I - 3*A)/2
    print("X=(I-3A)/2)=", X)


def bai05():
    A = np.array([[2,1],[1,2]])
    B = np.array([[1,-1],[1,1]])
    B2 = np.linalg.inv(B)
    C = B2.dot(A).dot(B)
    kq = C.dot(C).dot(C)
    print("(B'*A*B)^3=", kq)


def bai06():
    A = np.array([[5,4],[-4,-3]])
    I = np.identity(2)
    print("A^2-2A+I=", A.dot(A)-2*A+I)
    print('''
   A^2 - 2A + I  = 0
=> A*A - 2A      = -I
=> 2A  - A*A     = I
=>      A*(2I-A) = A*A^(-1)
=>          2I-A  = A^(-1)
''')
    A1 = 2*I-A
    print("A^(-1) = ", A1)
    print("Kiểm tra lại: A*A^(-1)=", A.dot(A1))


def bai07():
    A = np.array([[1,-1,1],[-1,2,1],[-2,3,1]])
    print("det(A)=", np.linalg.det(A))
    A1 = np.linalg.inv(A)
    print("A^(-1)=", A1)

    B = np.array([[1,2,-3],[2,1,-2],[2,-1,0]])
    print("det(B)=", np.linalg.det(B))
    B1 = np.linalg.inv(B)
    print("B^(-1)=", B1)

    C = np.array([[0,0,1,-1],[0,3,1,4],[1,-1,0,0],[0,0,1,1]])
    print("det(C)=", np.linalg.det(C))
    C1 = np.linalg.inv(C)
    print("C^(-1)=", C1)

    D = np.array([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])
    print("det(D)=", np.linalg.det(D))
    D1 = np.linalg.inv(D)
    print("D^(-1)=", D1)


def bai08():
    A = np.array([  [0.4, 0.2, 0.1],
                    [0.1, 0.3, 0.4],
                    [0.2, 0.2, 0.3]])
    I = np.identity(3)
    print("(I-A)^(-1)=", np.linalg.inv(I-A))


def bai09():
    A = np.array([[-3, 4, 6], [0, 1, 1], [-2, -3, -4]])
    B = np.array([[1,-1,2],[0,1,2]])
    A1 = np.linalg.inv(A)
    X = B.dot(A1)
    print("X=B*A^(-1)", X)


import sympy as sp
def bai10():
    a = sp.Symbol('a')
    b = sp.Symbol('b')
    ret = sp.solve([-2-b, 3-a],[a,b])
    print(ret)


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


if __name__ == "__main__":
    print("\n\n-------------------")
    bai01()
    print("\n\n-------------------")
    bai02()
    print("\n\n-------------------")
    bai03()
    print("\n\n-------------------")
    bai04()
    print("\n\n-------------------")
    bai05()
    print("\n\n-------------------")
    bai06()
    print("\n\n-------------------")
    bai07()
    print("\n\n-------------------")
    bai08()
    print("\n\n-------------------")
    bai09()
    print("\n\n-------------------")
    bai10()
