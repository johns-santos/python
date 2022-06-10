
print("\nWelcome to the rollercoaster!\n")

age = int(input("\nPlease enter your age: \n"))
bill = 0


if(age < 12):
    bill += 5
    print("\nPlease pay $5\n")
elif (age < 18):
    bill += 7
    print("\nPlease pay $7\n") 
elif (age >= 45 and age <= 55): # Logical AND operator
    print("You are in a midlife crisis. Seek help.")
else:
    print("\nPlease pay $12\n")
    bill +=12

wants_a_photo = input("Do you want a photo? Y or N. ")
if wants_a_photo == "Y":
    bill += 3

print(f"Your total bill is: ${bill}")
