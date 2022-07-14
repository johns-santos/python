# While Loop
# For loop


print("\n======== WHILE LOOP========\n")

# While "i" is less than the length of the string "meow" print "meow" 
sound = "meow"
i = 0
while i < len(sound):
    print(sound)
    i += 1

print("\n")


# While "X" is greater then "0" print "bark"
x = 4
while x > 0:
    print("bark")
    x -= 1



print("\n======== FOR LOOP ========\n")
# FOR LOOP

fruits = ['lemon', 'orange', 'pumpkin', 'grape']

for i in fruits:
    print(i)


print("\n======== WHILE & FOR LOOP used with User Input ========\n")

# Prompt user for number
while True:
    n = int(input("What's n?"))
    # Do not proceed until user provides a POSITIVE number
    if n % 2 == 0:
        #break out of WHILE LOOP
        break

# Take user provided number and use in FOR LOOP
for _ in range(n):
    # Print "meow" the number specified in FOR LOOP
    print("meow")

    