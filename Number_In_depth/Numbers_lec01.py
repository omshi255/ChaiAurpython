x=2
y=3
z=4
print(x+y)
print(x-y)
print(x**z)
print(x*y)
print(x/y)
print((x*y)+y+z)

# Comparisons
x, y, z = 1, 2, 3  # Example values for x, y, z
print(x < y < z)  # True
print(x < y and y < z)  # True

# Equality and comparison
print(1 == 2 < 3)  # False

# Math operations
import math
print(math.floor(2.3))  # 2

# Different number systems
print(0o20)  # Octal representation of 16
print(0x23)  # Hexadecimal representation of 35
print(0xFF)  # Hexadecimal representation of 255

# Binary representation and literals
print(0b100)  # Binary representation of 4

# Conversions
print(oct(67))  # Convert decimal to octal: '0o103'
print(hex(324))  # Convert decimal to hexadecimal: '0x144'
print(bin(78))  # Convert decimal to binary: '0b1001110'

# Using int() for conversions
print(int(3.14))  # Convert float to int: 3
print(int(45))  # Integer remains the same: 45

# Convert string representations of numbers with specific bases
print(int('67', 8))  # Interpret '67' as octal: 55
print(int('78', 16))  # Interpret '78' as hexadecimal: 120

# Invalid conversions
try:
    print(int('567', 2))  # '567' is not valid in binary, raises ValueError
except ValueError as e:
    print(e)

# Valid binary conversion
print(int('1000', 2))  # Interpret '1000' as binary: 8




# Importing Decimal from the decimal module
from decimal import Decimal

# Working with Decimal
result = Decimal(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))
print("Decimal result:", result)  # Output: Decimal('0.3')

# Importing Fraction from the fractions module
from fractions import Fraction

# Creating a Fraction
myFra = Fraction(2, 7)
print("Fraction:", myFra)  # Output: Fraction(2, 7)

# Set operations
setone = {2, 4, 6, 8}

# Intersection of sets
intersection_result = setone & {1, 2, 3, 4}
print("Intersection:", intersection_result)  # Output: {2, 4}

# Union of sets
union_result = setone | {1, 2, 3, 4}
print("Union:", union_result)  # Output: {1, 2, 3, 4, 6, 8}

# Difference of sets
difference_result = setone - {1, 2, 3, 4}
print("Difference:", difference_result)  # Output: {6, 8}

# Further difference
difference_result_2 = setone - {1, 2, 3, 4, 8, 0}
print("Further Difference:", difference_result_2)  # Output: {6}

# Subtracting all elements
difference_result_3 = setone - {1, 2, 3, 4, 8, 0, 6}
print("Empty set after subtraction:", difference_result_3)  # Output: set()

# Type of an empty dictionary
print("Type of {}:", type({}))  # Output: <class 'dict'>

# To create an empty set
empty_set = set()
print("Type of empty set:", type(empty_set))  # Output: <class 'set'>
