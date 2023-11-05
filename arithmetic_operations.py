print(15 + 4)   # Adds 15 and 4, resulting in 19
print(15 - 4)   # Subtracts 4 from 15, resulting in 11
print(15 * 4)   # Multiplies 15 by 4, resulting in 60
print(15 / 4)   # Divides 15 by 4, resulting in 3.75 (floating-point division)
print(15 // 4)  # Divides 15 by 4, resulting in 3 (integer division, truncating the decimal)
print(15 % 4)   # Calculates the remainder of the division of 15 by 4, resulting in 3
print(15 ** 4)  # Raises 15 to the power of 4, resulting in 50625

x = 10
x = x + 3
print(x)
# Other option to increment variable by 3:
x = 5
x += 3
print(x)
# Or subtract by 3:
x = 5
x -= 3
print(x)
# Operator precedence
x = 5 + 6 * 2  # Should be 17
print(x)
# Exponentiation
# Multiplication or division
# Addition or subtraction
x = 4 + 3 * 2 ** 2  # Should be 16
print(x)
# Parenthesis = priority
x = (4 + 3) * 2 ** 2  # Should be 28
print(x)
