with open("names.csv") as file:
    for line in file:
        # row = line.rstrip().split(",") # split string at ','
        # print(f"{row[0]} is {row[1]} years old.")

        # same as above but not using key-pair index
        name, age = line.rstrip().split(",") # split string at ','
        print(f"{name} is {age} years old.")


print("\n")
# Take data from CSV and place in list to SORT

people = []

with open("names.csv") as file:
    for line in file:
        name, age = line.rstrip().split(",")
        person = {"name": name, "age": age}
        people.append(person)

# Create function to return name
def get_name(person):
    return person["name"]

# Use SORTED function with "get_name" function as KEY (places in alphabetical by name)
for person in sorted(people, key=get_name, reverse=True):
    print(f"{person['name']} is in {person['age']} old.")


print("\n")


