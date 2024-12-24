# Initial assignment
myListOne = [1, 2, 3]
myListTwo = myListOne

# Changing myListOne to a string
myListOne = 'chai'

# Verifying the values
print("myListTwo:", myListTwo)  # Output: [1, 2, 3]
print("myListOne:", myListOne)  # Output: 'chai'

# Reassigning myListOne and myListTwo as separate lists
myListOne = [1, 2, 3]
myListTwo = [1, 2, 3]

# Modifying myListOne
myListOne[0] = 44

# Verifying the values after modification
print("myListOne:", myListOne)  # Output: [44, 2, 3]
print("myListTwo:", myListTwo)  # Output: [1, 2, 3]
