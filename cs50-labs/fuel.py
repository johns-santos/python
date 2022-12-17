def main():
    whatever = convertToPercentage()
    print(whatever)

def convertToPercentage():
    while True:
        try:    
            frac = (input("Fraction: "))  
            # Split input by division sign
            splitInput = frac.split("/")
            # convert x and y to interger
            x = int(splitInput[0])
            y = int(splitInput[1])
            # Convert fraction to percentage
            percentage = ((x / y) * 100 ) 
            # Round percentage to nearest tenth
            percentage = round(percentage)
            if percentage <= 1.0:
                return("Empty")
            elif percentage >= 95.0:
                return("Full")
            else:
                return(f"{percentage}%")          
        except (ValueError, ZeroDivisionError):
            print("Invalid entry. Enter a fraction '1/2'")
            pass
main()
