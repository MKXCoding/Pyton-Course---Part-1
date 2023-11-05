import math

x = 6.456
print(round(x, 2))  # Output 6.46 - takes up to 2 args - value and digits after .

x = 2.4
print(abs(-2.4))  # Absolute value

print(math.ceil(x))
print(math.floor(x))

# Useful tolerance check function from math module:
target = 20.00
result = 19.90

print(math.isclose(target, result, abs_tol=0.1))  # Absolute tolerance - 10 - 9.989 > 0.01
print(math.isclose(target, result, rel_tol=0.005))  # relative tolerance in % (1% = 0.01 in rel_tol)

# link - https://docs.python.org/3/library/math.html
