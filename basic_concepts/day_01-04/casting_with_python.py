num_char = len(input("What is your name?\n"))
print(type(num_char))


# need to cast "num_char" to string
num_char = str(num_char)
print(type(num_char))


print("Your name contains " + num_char + " characters.\n")


# This will convert the "225.25" to a float then add it to 70
print(70 + float("225.25"))


############################
print("\n")
############################



# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(type(two_digit_number))
x = int(two_digit_number[0])
y = int(two_digit_number[1])
print(x + y)


