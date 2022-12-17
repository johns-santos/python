def main():
    whatever = convertToPercentage()
    print(whatever)

def convertToPercentage():
    while True:
        try:
            return int(input("Input: "))       
        except (ValueError, ZeroDivisionError):
            print("Not a interger. Try again")
            pass

main()