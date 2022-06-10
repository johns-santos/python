######## FORMULA (BMI = weight / height-squared) ########
# 1) Take height and weight and return BMI as a WHOLE number. No need to round.




## Round number
# print("\n")
# print(8/3)
# print(round(8/3)) # This rounds up
# #FLOOR DIVISION - This rounds down
# print((8//3))

# # SHORT HAND
# print("\n")
# score = 8
# score /= 2
# print(score) # this resturns shorthand result above

# print("\n")
# level = 0
# level += 1
# print(level)


# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x = float(height) #height typical not a whole number
y = int(weight) #Weight can be entered as whole num
bmi =  int(y/(x ** 2))
print(bmi)


print("\n")
#  line with formated values


if  bmi < 18.5:
    print(f"Your BMI equals: {bmi}. You are underweight.\n")
elif bmi < 25:
    print(f"Your BMI equals: {bmi}. You are normal weight.\n")
elif bmi < 30:
    print(f"Your BMI equals: {bmi}. You are overwight.")
elif bmi < 35:
    print(f"Your BMI equals: {bmi}. You are obese.\n")
else:
    print(f"Your BMI equals: {bmi}. You are clinically obese.\n")