fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit, fruits.index(fruit))

print("\n")
# Jump out of loop and start a new loop
for fruit in fruits:
    print(f"{fruit} Pie")

print("\n")
# Jump out of loop and print list
print(fruits)