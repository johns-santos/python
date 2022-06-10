# num = 2

# if(num == 2):
#     print("num is true")
# if(num != 5):
#     print("of course")
# if(num != 3):
#     print('lame')
# if(num % 2 == 0):
#     print("false")

print("\nWelcome to the rollercoaster!\n")
height = int(input("What is your height in cm?\n"))
bill = 0

if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("\nPlease enter your age: \n"))
    if age  < 12:
        bill = 5
        print("\nChild tickets are $5\n")
    elif age  <= 18:
        bill = 7
        print("\nChild tickets are $7\n")
    else:
        bill = 12
        print("\nAdults tickets are $12\n")

    wants_photo = input("Do you want a photo taken? Y or N. \n")
    if wants_photo == "Y":
        # Add $3 for photo
        bill += 3

        print(f"\nYour final bill is ${bill}\n")

else:
    print("\nSorry you need to grow taller befor you can ride.\n")

