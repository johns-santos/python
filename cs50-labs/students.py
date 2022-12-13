
##### iterate over lines in CSV file (students.csv) and print output
#######################################################
with open("students.csv") as file:
    for line in file:
        #Remove new line and split by comma
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")



print("\n")


##### Alternative way to do the same "unpack"
#######################################################
with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

print("\n")


##### Sort by newly created list which includes new string
#######################################################
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
        print(students)

    for student in sorted(students):
        print(student)


print("\n")



##### sort by name - using a listed dictionary 
# Reverse order by name
#######################################################
students1 = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student1 = {"name": name, "house": house}
        students1.append(student1)
    
def get_name(student1):
    return student1["name"]

for student1 in sorted(students1, key=get_name, reverse=True):
    print(f"{student1['name']} is in {student1['house']} ")



print("\n")


# DO same above with a LAMBDA or ANONYMOUS function
#######################################################
students1 = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student1 = {"name": name, "house": house}
        students1.append(student1)
    
# LAMBDA function used here....... 
for student1 in sorted(students1, key=lambda student1: student1["name"]):
    print(f"{student1['name']} is in {student1['house']} ")