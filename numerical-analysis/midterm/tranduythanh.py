import math

def f(x):
    return math.exp(-x**2)

if __name__ == "__main__":
    n = int(input("Nhập số phân hoạch n = "))
    a = 0
    b = 2
    h = (b-a)/n
    fa = f(a)
    fb = f(b)
    s = fa + fb
    i = 1
    while i < n:
        xi = a + h*i
        fxi = f(xi)
        s = s + 2*fxi
        i = i + 1
    s = s * h/2
    print(s)