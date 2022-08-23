

# Print value of i starting at 0 to length of 4.
for i in range(4):
    print(i)
# 0
# 1
# 2
# 3


# create a list containing 4 items in position starting at 0
print(list(range(0,4)))
# [0,1,2,3]


print(" ")


supplies = ['pens', 'staplers', 'flame-throwers', 'bin']
for x in range(len(supplies)):
    print('Index ' + str(x) + ' in supplies is: ' + supplies[x])



# Assign value to item list referring to index location
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(size, color)

print(" ")
size, color, disposition = 'skinny', 'black', 'sneaky'

print(" ")
print(size)
dog = size, color, disposition
print(dog)