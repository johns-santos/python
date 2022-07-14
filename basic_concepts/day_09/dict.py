programming_dictionary = {
    "Bug":"An Error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again." 
}

#Retrieving items from dictionary.
print(programming_dictionary["Bug"])


print("\n")
#Adding new item to dictionary
programming_dictionary["Integer"] = "int - Whole number."

print(programming_dictionary)


print("\n")
#Print length of dictionary
print(len(programming_dictionary))

#Create an empty dictionary
student_grades = {}


print("\n")
#Edit a key/value in dictionary
programming_dictionary["Integer"] = "Whole number. Notated by (int)"
print(programming_dictionary["Integer"])


print("\n")
#Loop through a dictionary and return keys
for key in programming_dictionary:
    print(key)


print("\n")
#Loop through a dictionary and return key and value pair
for key in programming_dictionary:
    print(f"{key} - {programming_dictionary[key]}")


# print("\n")
# #Wipe/Empty an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)


print("\n")
print("\n")
print("\n")



#Create new empty array add students and translate SCORE to a GRADE
student_scores = {
    "Harry": 81,
    "Ron": 90,
    "Hermione" : 99,
    "Draco": 74,
    "Neville": 60,
}

for i in student_scores:
    student_grades[i] = student_scores[i]
    if student_grades[i] > 89:
        student_grades[i] = "A"
    elif student_grades[i] > 79:
        student_grades[i] = "B"
    elif student_grades[i] > 69:
        student_grades[i] = "C"
    elif student_grades[i] > 59:
        student_grades[i] = "D"
    else:
        student_grades[i] = "F"

print(student_grades)
