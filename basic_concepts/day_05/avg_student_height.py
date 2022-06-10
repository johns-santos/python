# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

print(student_heights)

total_height = 0
for num in student_heights:
  total_height = num + total_height

total_students = 0
for s in student_heights:
    total_students += 1

avg_height = round(total_height / total_students)


# # SAA but much shorter
# number_of_students = len(student_heights)
# total_height = sum(student_heights)
# avg_height = round(total_height / number_of_students)



print(avg_height)