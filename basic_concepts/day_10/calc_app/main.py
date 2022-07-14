from replit import clear

from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operation_sym = {
    "+":add,
    "-":subtract, 
    "*":multiply,
    "/":divide
    }

def calculator():
    print(logo)
    n1 = float(input("What's the first number?: "))
    print("OPERATIONS LIST:")
    for symbol in operation_sym:
        print(symbol)
    cont = True

    while cont == True:
        sign = input("Pick an operation: ")
        n2 = float(input("What's the second number?: "))
        operation = operation_sym[sign]
        answer = operation(n1,n2)

        print(f"{n1} {sign} {n2} = {answer}")

        how_continue = input(f"Type 'y' to save result and continue calculating with {answer}  \nor 'n' to start new calculation, \nor press any other key to exit:\n")

        if how_continue == 'y':
            n1 = answer
        elif how_continue == 'n':
            cont = False
            calculator()
        else:
            break

calculator()






