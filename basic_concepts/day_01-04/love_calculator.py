# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# Combine names into one string and convert to lower case
long_name = name1.lower()+name2.lower()
# Create scores for TRUE and LOVE
true = 0
love = 0

total_t = long_name.count("t")
true += total_t

total_r = long_name.count("r")
true += total_r

total_u = long_name.count("u")
true += total_u

total_e = long_name.count("e")
true += total_e

total_l = long_name.count("l")
love += total_l

total_o = long_name.count("o")
love += total_o

total_v = long_name.count("v")
love += total_v

total_e = long_name.count("e")
love += total_e

# Combine TRUE + LOVE as string
trueLove = str(true) + str(love)
# Convert to INTEGER to be used in IF/ELSE logic
trueLove = int(trueLove)

if(trueLove < 10 or trueLove > 90):
    print(f"Your score is {trueLove},  go together like coke and mentos. ")
elif(trueLove >= 40 and trueLove <= 50):
    print(f"Your score is {trueLove}, you are alright together.")
else:
    print(f"Your score is {trueLove}")
