
i = 1
while i <= 10:
    print(f"{i} iteration")
    i += 1

print("")

test = False
while test != True:
    userInput = input("Enter a string: ")
    if userInput == "end":
        test = True