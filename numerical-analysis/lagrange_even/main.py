import math 

def fac(n):
    if n == 0:
        return 1
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

# C^k_n = n!/(k! (n-k)!)
def C(k, n):
    return fac(n)/fac(k)/fac(n-k)

def lagrange_even(n, a, b, ys, x):
    x_0 = a
    
    h = (b-a)/n
    t = (x-x_0)/h
    
    P = 1
    i = 0

    # t(t-1)(t-2)...(t-n)
    while i<= n:
        P *= (t-i)
        i += 1
    P /= fac(n)

    i = 0
    S = 0

    while i <= n:
        if (n-i)%2 == 0:
            S += C(i,n)*ys[i]/(t-i)
        else:
            S -= C(i,n)*ys[i]/(t-i)
        i += 1
    P *= S

    print(P)


lagrange_even(n=3, a=1.1, b=1.4, ys=[15, 18, 19, 24], x=1.25)