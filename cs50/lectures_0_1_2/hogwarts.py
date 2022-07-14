

students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

print(len(students))

print("\n Manually print student name ")
print(students[0])
print(students[1])
print(students[2])


print("\n FOR loop print each name of student")

for student in students:
    print(student)



print("\n Use FOR loop with a number provided by length of list ")

# 'range' allows you to return length of list to be used in for loop - RANGE expects an integer value
for i in range(len(students)):
    print(i, students[i])



# DICTIONARY
print("\n === DICTIONARY ======\n")


students2 = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco": "Slytherin"
}

#Use first property as KEY 
print(students2["Hermione"]) # returns HOUSE



# Only returns KEYS
for student2 in students2:
    print(student2)

# Use KEY name to return house
for student2 in students2:
    print(student2, students2[student2], sep=", ")




print("\n")
students3 = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell"},
    {"name": "Draco", "house":"Slytherin", "patronus": None}
]

for student3 in students3:
    print(student3["name"], student3["house"], sep=", ")



print("\n")

# Use index KEY for the entire dictionary
print(students3[0])

# Use KEY, PAIR
print(students3[0]["patronus"])

