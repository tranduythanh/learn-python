import sympy as sp
import numpy as np
import scipy

# bài 1
x, y = sp.symbols('x y')
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

# bài 2
f = lambda x: sp.exp(x)
print("integral:", scipy.integrate.quad(f, 0, 1))

f = lambda x: np.cos(x)
print("integral:", sp.integrate(expr, (x, 0, np.pi/2)))

# bài 3
f = lambda x: np.cbrt(x-1)
print("integral:", scipy.integrate.quad(f, 2, 9))

f = lambda x: 1/np.cos(x)**2
print("integral:", scipy.integrate.quad(f, -np.pi/4, 0))

f = lambda x: 1/np.cos(x)**2
print("integral:", scipy.integrate.quad(f, -np.pi/4, 0))

f = lambda x: 1/(x * (1+sp.ln(x)**2))
print("integral:", scipy.integrate.quad(f, 1, np.e))

f = lambda x: 1/(1 + np.sqrt(3*x-2))
print("integral:", scipy.integrate.quad(f, 1, 6))

f = lambda x: 1/np.sqrt(np.exp(x)+1)
print("integral:", scipy.integrate.quad(f, sp.ln(3), sp.ln(8)))

f = lambda x: sp.exp(x-sp.exp(x))
print("integral:", scipy.integrate.quad(f, 0, 1))

f = lambda x: np.sin(x)**4 / (np.sin(x)**4 + np.cos(x)**4)
print("integral:", scipy.integrate.quad(f, 0, np.pi/2))

f = lambda x: sp.ln(x)**2
print("integral:", scipy.integrate.quad(f, 1, np.e))

f = lambda x: x**2 * np.cos(x)
print("integral:", scipy.integrate.quad(f, 0, np.pi/2))

f = lambda x: 1 / (3+2*np.cos(x))
print("integral:", scipy.integrate.quad(f, 0, 2))

f = lambda x: 1 / ((2*x + 1)*(np.sqrt(x**2+1)))
print("integral:", scipy.integrate.quad(f, 0, 1))

# bài 4
f = lambda x: x / (1+np.sin(x))
print("integral:", scipy.integrate.quad(f, 0, np.pi))

f = lambda x: x*np.sin(x) / (1+np.cos(x)**2)
print("integral:", scipy.integrate.quad(f, 0, np.pi))

# bài 5
f = lambda x: 1/ (1+x**2)**2
print("integral:", scipy.integrate.quad(f, 0, 1))

f = lambda x: np.sin(x)**2 * np.cos(x) / (1+np.sin(x)**2)**2
print("integral:", scipy.integrate.quad(f, 0, np.pi/2))

f = lambda x: sp.ln(1+np.tan(x))
print("integral:", scipy.integrate.quad(f, 0, np.pi/4))

f = lambda x: sp.ln(1+x) / (1+x**2)
print("integral:", scipy.integrate.quad(f, 0, 1))

f = lambda x: x*np.sin(x) / (9+4*np.cos(x)**4)
print("integral:", scipy.integrate.quad(f, 0, np.pi))

f = lambda x: 1 / ((1+x**2)*(sp.exp(x)+1))
print("integral:", scipy.integrate.quad(f, -1, 1))

# bài 6
f = lambda x: np.arctan(x) / (1+x**2)
print("integral:", scipy.integrate.quad(f, -1, sp.oo))

f = lambda x: 1 / (4+x**2)
print("integral:", scipy.integrate.quad(f, -sp.oo, 0))

f = lambda x: sp.exp(-2*x)
print("integral:", scipy.integrate.quad(f, 0, sp.oo))

f = lambda x: 1 / (x * np.sqrt(4+x**2))
print("integral:", scipy.integrate.quad(f, 1, sp.oo))

f = lambda x: x * sp.exp(-2*x)
print("integral:", scipy.integrate.quad(f, 0, sp.oo))

f = lambda x: (2*x -1) / sp.exp(3*x)
print("integral:", scipy.integrate.quad(f, 0, sp.oo))

expr = 1 / (x * sp.ln(x)**2)
print("expr    :", expr)
print("integral:", sp.integrate(expr, (x, sp.E, sp.oo)))

f = lambda x: 1 / (x**2 - 4*x + 8)
print("integral:", scipy.integrate.quad(f, -sp.oo, sp.oo))

# bài 7
fx = x/(x**2+1)
fy = 1/(y**2+1)
ret = sp.integrate(fx, x) + sp.integrate(fy, y)
print(ret)

fx = (1-x**2)/x
fy = y
ret = - sp.integrate(fx, x) + sp.integrate(fy, y)
print(ret)

fx = 1/sp.cos(x)
fy = 1/y
ret = - sp.integrate(fx, x) + sp.integrate(fy, y)
print(ret)

fx = (x+1)/sp.sqrt(x**2 + 4*x + 13)
fy = (3*y+12) / (4 + y**2)
ret = sp.integrate(fx, x) - sp.integrate(fy, y)
print(ret)

fx = 1
fy = 1/(y**2 - 3*y +4)
ret = - sp.integrate(fx, x) + sp.integrate(fy, y)
print(ret)

# bài 8
import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model1(y,x):
    dydx = np.exp(1-2*x)
    return dydx

y0 = 1
x = np.linspace(0,10)
y = odeint(model1,y0,x)
plt.plot(x,y)
plt.xlabel('Truc x')
plt.ylabel('Truc y')
plt.show()

def model2(y,x):
    dydx = np.cos(x)**2 - y*np.tan(x)
    return dydx

y0 = -1
x = np.linspace(-np.pi/2,np.pi/2)
y = odeint(model2,y0,x)
plt.plot(x,y)
plt.xlabel('Truc x')
plt.ylabel('Truc y')
plt.show()

def model3(y,x):
    dydx = y**2 + 1
    return dydx

y1 = 0
x = np.linspace(0,100)
y = odeint(model3,y1,x)
plt.plot(x,y)
plt.xlabel('Truc x')
plt.ylabel('Truc y')
plt.show()

def model4(u,t):
    dudt = (2*t + 1/np.cos(t)**2) / (2*u)
    return dudt

u0 = -5
t = np.linspace(0,100)
u = odeint(model4,u0,t)
plt.plot(t,u)
plt.xlabel('Truc u')
plt.ylabel('Truc t')
plt.show()