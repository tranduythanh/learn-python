



import numpy as np

def kt_cheo_troi(A):
    n = A.shape[0]
    i=0
    while i<n:
        sum = np.sum(np.abs(A[i])) - np.abs(A[i,i])
        if sum < np.abs(A[i,i]):
            i = i+1
            continue
        else:
            return False
            print("KHÔNG thỏa điều kiện ma trận chéo trội")
    print("Thỏa điều kiện ma trận chéo trội")
    return True


def gauss_seidel(A, b, e):
    n = A.shape[0]
    D = np.diag(np.diag(A))
    U = np.triu(A,1)
    L = np.tril(A,-1)

    invDL = np.linalg.inv(D+L)
    B = -invDL.dot(U)
    g = invDL.dot(b)

    normB = np.linalg.norm(B, ord=np.inf)
    q = normB/(1-normB)
    a = True
    x0 = g
    k=0
    while a:
        x = B.dot(x0)+g
        k = k+1
        print("k = {}\tx = {}".format(k, x.reshape(n,)))
        if q*np.linalg.norm(x-x0) < e:
            a = False
        else:
            x0 = x




A = np.array(  [[10,-1, 2],
                [1 ,10,-1],
                [2 ,3 ,10]])
b = np.array([0,5,-10]).reshape(3,1)
e = 0.000000000000000001

if kt_cheo_troi(A):
    gauss_seidel(A, b, e)
