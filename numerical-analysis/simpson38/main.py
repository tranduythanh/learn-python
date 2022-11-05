def he_so(i, n):
    if i == 0 or i == n:
        return 1
    if i % 3 == 0:
        return 2
    return 3

def f(x):
    return 1/(x**2+1)

def simpson38(a, b, n):
    h = (b-a)/n

    sum = 0
    i = 0

    while (i <= n):
        m = he_so(i, n)
        xi = a + h*i
        yi = f(xi)
        part = m*yi
        sum += part
        i += 1
    
    return 3*h/8*sum

if __name__ == "__main__":
    print(simpson38(-3, 6, 10000000))