colors = ['red', 'blue', 'white', 'yellow', 'green']

print(len(colors))

# Update items in 1, 2, 3 place of index.
colors[1:3] = ['pink', 'red', 'indigo']

print(colors)

# print items up to 3 - but DONOT include 3
print(colors[:3])

# print all items starting at index of 3 to the end
print(colors[3:])


# Delete index 2 (red)
del colors[2]

print(colors)


colors2 = ['orange','grey','purple']

# concate two list
colors1 = colors + colors2
print(colors1)


# Looks for string match in list - EVALUATE to TRUE (STRING not in LIST)
not_in_list = 'gray' not in colors1
print(not_in_list)

# Look for string match in list - EVALUATE to FALSE (STRING is in LIST)
not_in_list = 'grey' not in colors1
print(not_in_list)


print(" ")
# locate index location of item in list
print(colors1.index('orange'))

print("")
# Add value to end of list
colors.append('salmon')
print(colors) 

# Insert value in specific location moving all values up
colors.insert(1,'maroon')
print(colors)


print("")
# Remove value from list
print(colors.remove('yellow'))
print(colors)


print("")
# Sort list by first letter and upper case letters.
colors.sort()
print(colors)


print("")
# Sort alphabetically, however UPPER case comes before LOWER case.
char = ['a', 'b','c','d','E','f','G']
char.sort()
print(char)

# Ignore case and sort alphabetically
char.sort(key=str.lower)
print(char)