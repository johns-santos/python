# Regular division prints precise answer
print(8/3) # returns 2.6666666666666665
# Division returns a float
print(type(8/3)) # retuns <class 'float'>


print(int(8/3)) # returns 2 - rounds down

# ROUND
print(round(8/3)) # returns 3 - rounds up
# ROUND with percision
print(round(8/3, 3)) # returns 2.667 - round specified location after decimal


# FLOOR DIVISION (//)
print((8//3)) # returns 2 - rounds down
# Floor division returns a INTEGER
print(type(8//3)) # retuns <class 'int'>

# F string (f"string") concantenates strings and varialbes  
print("\n")
score = 0
print(f"Score is equal to {score}")