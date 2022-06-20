def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

# Function with one parameter
# =======================
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the weather nice today {name}?")


# Function with more than 1 parameter
# =======================
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}")





print("\n")
greet()


print("\n")
greet_with_name("John")

print("\n")
greet_with_name("Bella")

print("\n")
greet_with("Bella", "SA TX")

print("\n")
#Print with keyword arguments to make sure argues are used in order by parameter.
greet_with(location="San Antonio, Tx", name="John")