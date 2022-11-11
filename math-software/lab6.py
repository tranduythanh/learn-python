import sympy as sp
import numpy as np


def lim(expr, x, stop):
    print("Expression : {}".format(expr))
    print("Limit x->{} : {}".format(stop, sp.limit(expr, x, stop)))     

# bai 1
x = sp.symbols('x')
expr = abs((-1)**(x+1)/x)   
lim(expr, x, sp.oo)

expr = (2*x)/(x**3+1)
lim(expr, x, sp.oo)

expr = abs( (-1)**x * (0.999)**x )
lim(expr, x, sp.oo)

# bai 2
x = sp.symbols('x')
expr = (x-1)*(x-2)*(x-3)/(3*x**3)
lim(expr, x, sp.oo) 

expr = ((sp.sqrt(x**2+1)+2*x)**2) / (sp.cbrt(x**6+2))
lim(expr, x, sp.oo) 

expr = (2**(x+1)+3**(x+2))/(2**x + 3**(x+1))
lim(expr, x, sp.oo)

# biến đổi rồi sau đó mới nhập liệu
expr = x*(x-1)/2/(x**2)
lim(expr, x, sp.oo)

# tử là cấp số cộng công bội 1/2
# mẫu là cấp số cộng công bội 1/3
expr = 2*(1-1/2**x) / (3*(1-1/3**x))
lim(expr, x, sp.oo)

# đơn giản biểu thức còn lại 1-1/x
expr = 1-1/x
lim(expr, x, sp.oo)

# sử dụng limit_seq để tính giới hạn của chuỗi. Dùng sp.Sum để cộng các phần tử của dãy (sequence) thành chuỗi
k, n = sp.symbols('k n')
series = sp.Product(1-1/k**2, (k, 2, n))
print("Expression : {}".format(series))
print("Limit n->oo : {}".format(sp.limit_seq(series, n)))

a, q = sp.symbols('a, q')
expr = a*0.9**n
lim(expr, n, sp.oo)

# bài 3
k, m, n, x = sp.symbols('k m n x')
expr = (sp.sqrt(1+2*x)-3) / (sp.sqrt(x)-2)
stop = 4
lim(expr, x, stop)

expr = (x**(1/m)-1) / (x**(1/n)-1)
stop = 1
lim(expr, x, stop)

expr = sp.sqrt(x+sp.sqrt(x+sp.sqrt(x)))-sp.sqrt(x)
stop = sp.oo
lim(expr, x, stop)

expr = x**2/((1+5*x)**(1/5) - (1+x))
stop = 0
lim(expr, x, stop)

a, b = sp.symbols('a b')
expr = sp.sqrt((x+a)*(x+b)) - x
stop = sp.oo
lim(expr, x, stop)

expr = sp.sin(5*x)/sp.tan(8*x)
stop = 0
lim(expr, x, stop)

expr = 1/sp.sin(x) - sp.cot(x)
stop = 0
lim(expr, x, stop)

expr = (1 - sp.sqrt(sp.cos(x)) ) / x**2
stop = 0
lim(expr, x, stop)

expr = ( sp.sqrt(1+sp.sin(x)) - sp.sqrt(1-sp.sin(x)) ) / x
stop = 0
lim(expr, x, stop)

expr = sp.ln(sp.cos(x))/x**2
stop = 0
lim(expr, x, stop)

expr = ( sp.cbrt(x*sp.cos(x)) - sp.sqrt(sp.cos(x)) ) / x**2
stop = 0
lim(expr, x, stop)

expr = 1/x * sp.ln( (sp.exp(x)-1) / x )
stop = sp.oo
lim(expr, x, stop)

expr = 1/x * sp.ln( (sp.exp(x)-1) / x )
stop = sp.oo
lim(expr, x, stop)

expr = (sp.sqrt(1 + x + x**2) - sp.sqrt(7 + 2*x - x**2)) / (x**2 -2)
stop = 2
lim(expr, x, stop)

expr = (x**x - 1) / (x * sp.ln(x))
stop = 1
lim(expr, x, stop)

expr = (5**x - 4**x) / (x**2 + 2*x)
stop = 0
lim(expr, x, stop)

expr = sp.cos(x)**(1/x**2)
stop = 0
lim(expr, x, stop)

expr = sp.cos(x)**(1/sp.sin(x))
stop = 0
lim(expr, x, stop)

expr = (1+sp.sin(2*x))**(1/x)
stop = 0
lim(expr, x, stop)

# bai 4
x = sp.symbols('x')
expr = (x**2+1)*(sp.exp(x)+2)
print("Expression : {}".format(expr))
print("Derivative : {}".format(sp.diff(expr, x)))

# bai 5
x = sp.symbols('x')
expr = sp.cos(x)**2/(1+sp.sin(x)**2)
deriv = sp.diff(expr, x)
print("Expression : {}".format(expr))
print("Derivative : {}".format(deriv))
ld = sp.lambdify(x, deriv)
print(ld(np.pi/4))

# bài 6
x = sp.symbols('x')
expr = x**2*sp.exp(-x/2)
deriv = sp.diff(expr, x)
print("Expression : {}".format(expr))
print("Derivative : {}".format(deriv))
ld = sp.lambdify(x, deriv)
print(ld(0))

# bài 7
x = sp.symbols('x')
expr = sp.ln((1+x) / (1-x))
deriv = sp.diff(expr, x, 10)
print("Expression : {}".format(expr))
print("Derivative : {}".format(deriv))
ld = sp.lambdify(x, deriv)
print(ld(0))

# bài 8
x, m, n = sp.symbols('x m n')
expr = 1 + x**m * (x-1)**n
deriv = sp.diff(expr, x)

ret = sp.solve(deriv, x)
print("Expression : {}".format(expr))
print("Derivative : {}".format(deriv))
print("Result:      {}".format(ret))

# bài 10
x = sp.symbols('x')

expr = sp.sin(x)
deriv = sp.diff(expr, x, 2)
print("Expression : {}".format(expr))
print("Derivative : {}".format(deriv))

expr = sp.sin(2 * x) + sp.cos(3 * x)
deriv = sp.diff(expr, x, 2)
print("Expression : {}".format(expr))
print("Derivative : {}".format(deriv))

expr = 1/(x**2 - 5*x + 6)
deriv = sp.diff(expr, x, 2)
print("Expression : {}".format(expr))
print("Derivative : {}".format(deriv))