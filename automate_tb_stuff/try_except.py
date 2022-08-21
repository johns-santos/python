def div42by(num):
    try:
        return 42/num
    except ZeroDivisionError: # except can be left blank
        print('Error: You tried to divide by zero')

div42by(12)
div42by(0)




def cat():
    numCats = input("How many cats do you have? ")
    try:
        if int(numCats) >= 4:
            print('That is a lot of cats.')
        else:
            print('This is not that many cats.')
    except ValueError:
        print('You did not enter a number')


print("\n")
cat()    