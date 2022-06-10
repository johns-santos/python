import random


states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts"]

# Select item inverse index location
print(states[-6])

# Update list item
states[1] = "Pencilvania"

print(states[1])

# Add item to end of list
states.extend(["Texas", "New Mexico"])

print(states)


states.append("Florida")

print(states)

states.insert(2, "California")

print(states)




print("\n\n\n")

####### Bill Pay Roulette #######

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")

# Will seperate string where coma
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

random_name = names[random.randint(0, (len(names)-1))]
print(f"\n{random_name} will pay the bill. Yay!!!!!\n")




# Alternative solution is "random.choice(list)"
print(random.choice(names))