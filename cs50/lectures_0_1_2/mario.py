print("#")
print("#")
print("#")


print("\n")


# Range with integer
for _ in range(3):
    print("#")


print("\n")

# Create functions using for loop and  range that can be reused, and edited producing the same output
def print_column(height):
    for _ in range(height):
        print("#")

print_column(3)


print("\n")

# Another function that can be reused and changed
def print_row(width):
    print("?" * width)

print_row(3)


print("\n")

def print_square(size):
    for _ in range(size):
        print("# " * 3)

print_square(3)
