import sympy as sp
from sympy.vector import CoordSys3D

sp.init_printing()

# Define the coordinate system and the parameter t
N = CoordSys3D('N')
t = sp.symbols('t')
p = sp.symbols('p')

# Define the curve α(t)
x = (1+t)**(3/2)
y = (1-t)**(3/2)
z = 2*sp.sqrt(2)*t

alpha = x * N.i + y * N.j + z * N.k

# Compute the first and second derivatives of α(t)
alpha_prime = alpha.diff(t)
print("alpha'")
sp.pprint(sp.cancel(alpha_prime))

alpha_double_prime = alpha_prime.diff(t)
print("alpha''")
sp.pprint(sp.cancel(alpha_double_prime))

# Calculate the unit tangent vector T
T = alpha_prime.normalize()
print("Unit tangent vector T:")
sp.pprint(sp.cancel(T))

# Calculate the curvature κ
kappa = alpha_prime.magnitude() / (alpha_prime.cross(alpha_double_prime)).magnitude()

# Calculate the unit normal vector N
N_vector = alpha_prime.cross(alpha_double_prime).normalize()

# Calculate the binormal vector B
B = T.cross(N_vector)

# Calculate the torsion τ
torsion_numerator = (alpha_prime.cross(alpha_double_prime)).dot(alpha_double_prime.cross(alpha_double_prime.diff(t)))
torsion_denominator = (alpha_prime.cross(alpha_double_prime)).magnitude() ** 2
tau = torsion_numerator / torsion_denominator

# Display the results

print("\nUnit normal vector N:")
sp.pprint(sp.cancel(N_vector))
print("\nBinormal vector B:")
sp.pprint(sp.cancel(B))
print("\nCurvature κ:")
sp.pprint(sp.cancel(kappa))
print("\nTorsion τ:")
sp.pprint(sp.cancel(tau))