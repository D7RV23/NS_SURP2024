import ctypes

# Load the shared lib
ns_math_lib = ctypes.CDLL('./ns_math_lib.so')

# Set the return types and arg types
ns_math_lib.compute_dPdr.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
ns_math_lib.compute_dPdr.restypes = ctypes.c_double

# Example execution:

p = 1.0e16
rho = 1.0e5
r = 1.0e6
mr = 1.0e30

result = ns_math_lib.compute_dPdr(p, rho, r, mr)

print(f'dP/dr = {result:.3e}')
