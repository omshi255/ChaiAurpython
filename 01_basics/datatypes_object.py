a = 10
b = 20
print(a+b)
print(a*b)
print(2**3)

username  = "chai aur code"
print(len(username))
# Importing the math module and accessing the value of pi
import math
print(math.pi)  # Output: 3.141592653589793

# Importing the random module and generating random values
import random
print(random.random())  # Generates a random float between 0 and 1

# Using random.choice to pick a random element from a list
print(random.choice([1, 2, 3, 4, 5]))  # Picks a random number from the list

# Working with strings
username = "chai aur code"
print(len(username))  # Output: 13, length of the string

# Accessing characters in a string
print(username[0])  # Output: 'c', first character
print(username[-2])  # Output: 'd', second last character
print(username[1:3])  # Output: 'ha', substring from index 1 to 2

# Attempting to modify an immutable string (causes an error)
try:
    username[0] = 'A'  # This will raise a TypeError
except TypeError as e:
    print(e)  # Output: 'str' object does not support item assignment
# Working with a list
mylist = [123, "chai", 3.123]  # A list containing an integer, a string, and a float
print(mylist)  # Output: [123, 'chai', 3.123]
print(len(mylist))  # Output: 3, length of the list
print(mylist[0])  # Output: 123, accessing the first element

# Working with a dictionary
myD = {'one': 'lemontea', 'two': 'gingertea', 'three': 'masalatea'}  # A dictionary with string keys and values
print(myD)  # Output: {'one': 'lemontea', 'two': 'gingertea', 'three': 'masalatea'}
print(len(myD))  # Output: 3, number of key-value pairs in the dictionary
print(myD['three'])  # Output: 'masalatea', accessing the value associated with the key 'three'

# Working with a tuple
myTup = (1, 2, 3, 4)  # A tuple containing integers
print(myTup[0])  # Output: 1, accessing the first element of the tuple

