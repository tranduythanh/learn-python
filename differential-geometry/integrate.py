import sympy as sp

# Define symbols
r, t = sp.symbols('r t')

# Define the function to be integrated
f = sp.sqrt(sp.sinh(r)**2 + 1)

# Calculate the indefinite integral
indefinite_integral = sp.integrate(f, r)

# Calculate the definite integral from a to b
definite_integral = sp.integrate(f, (r, 0, t))

# Display the original function, indefinite integral, and definite integral
print("Original function:")
sp.pprint(f)

print("\nIndefinite integral:")
sp.pprint(sp.cancel(indefinite_integral))

print("\nDefinite integral from a to b:")
sp.pprint(sp.cancel(definite_integral))