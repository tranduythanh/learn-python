import sympy as sp
import numpy as np

# bài 1
x = sp.symbols('x')
expr = 1/(4*x**2+9)
print("expr    :", expr)
print("integral:", sp.integrate(expr, x))

expr = 1/(3+2*sp.cos(x)+sp.sin(x))
print("expr    :", expr)
print("integral:", sp.integrate(expr, x))

# expr = sp.sin(x)/sp.sqrt(4+sp.cos(x)**2)
# print("expr    :", expr)
# print("integral:", sp.integrate(expr, x))

expr = x/(x**2-5*x+4)
print("expr    :", expr)
print("integral:", sp.integrate(expr, x))

expr = 1/(x**2-4*x+13)
print("expr    :", expr)
print("integral:", sp.integrate(expr, x))

expr = (2-sp.sin(x))/(2+sp.cos(x))
print("expr    :", expr)
print("integral:", sp.integrate(expr, x))

expr = x**5*sp.exp(-x)
print("expr    :", expr)
print("integral:", sp.integrate(expr, x))

# bài 3
import scipy

f = lambda x: np.cbrt(x-1)
print("integral:", scipy.integrate.quad(f, 2, 9))

f = lambda x: 1/np.cos(x)**2
print("integral:", scipy.integrate.quad(f, -np.pi/4, 0))

f = lambda x: 1/np.cos(x)**2
print("integral:", scipy.integrate.quad(f, -np.pi/4, 0))

# bài pt vi phân
x, y = sp.symbols('x y')
result = sp.integrate(x**2+1, y) - y**2+4
print(result)

result = sp.integrate(x*y, y) - 1-x**2
print(result)