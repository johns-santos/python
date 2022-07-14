# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Declare and initiliaze bill variable
bill = 0

# Logic to handle cost of pizza based on selected size
if (size == "S"):
    bill += 15
elif (size == "M"):
    bill += 20
else: 
    bill += 25

# Logic handeling pepperoni selection based on pizza size
if(add_pepperoni == "Y"):
    if(size == "S"):
        bill += 2
    else:
        bill += 3

 # Logic handeling extra cheese selection   
if (extra_cheese == "Y"):
    bill += 1

print(f"\nYour final bill is: ${bill}\n")



