import sympy as sp


# bai 1
x = sp.symbols('x')
expr = abs((-1)**(x+1)/x)   
print("Expression : {}".format(expr))
print("Limit x->oo : {}".format(sp.limit(expr, x, sp.oo))) 

expr = (2*x)/(x**3+1)
print("Expression : {}".format(expr))
print("Limit x->oo : {}".format(sp.limit(expr, x, sp.oo))) 

expr = abs( (-1)**x * (0.999)**x )
print("Expression : {}".format(expr))
print("Limit x->oo : {}".format(sp.limit(expr, x, sp.oo)))

# bai 2
x = sp.symbols('x')
expr = (x-1)*(x-2)*(x-3)/(3*x**3)
print("Expression : {}".format(expr))
print("Limit x->oo : {}".format(sp.limit(expr, x, sp.oo))) 

expr = ((sp.sqrt(x**2+1)+2*x)**2) / (sp.cbrt(x**6+2))
print("Expression : {}".format(expr))
print("Limit x->oo : {}".format(sp.limit(expr, x, sp.oo))) 

# bai 4
x = sp.symbols('x')
expr = (x**2+1)*(sp.exp(x)+2)
print("Expression : {}".format(expr))
print("Derivative : {}".format(sp.diff(expr, x)))

# bai 5
import numpy as np
import sympy as sp
x = sp.symbols('x')
expr = sp.cos(x)**2/(1+sp.sin(x)**2)
deriv = sp.diff(expr, x)
print("Expression : {}".format(expr))
print("Derivative : {}".format(deriv))
ld = sp.lambdify(x, deriv)
print(ld(np.pi/4))

