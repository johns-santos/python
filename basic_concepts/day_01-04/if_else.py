# # If (condition):
# #   do something
# # else:
# #   do something else


# print("\nWelcome to the rollercoaster!\n")
# height = int(input("What is your height in cm?\n"))

# if height > 120:
#     print("\nYou can ride the rollercoaster!\n")
# else:
#     print("\nSorry you need to grow taller befor you can ride.\n")



# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
# #Write your code below this line 👇
# if (number % 2 == 0):
#     print("This is a EVEN number!")
# else:
#     print("This is a ODD number!")




#### NESTED IF/ELSE STATEMENTS

print("\nWelcome to the rollercoaster!\n")
height = int(input("What is your height in cm?\n"))

if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("\nPlease enter your age: \n"))
    if age  < 12:
        print("\nPlease pay $5\n")
    elif age  <= 18:
        print("\nPlease pay $7\n")
    else:
        print("\nPlease pay $12\n")
else:
    print("\nSorry you need to grow taller befor you can ride.\n")

