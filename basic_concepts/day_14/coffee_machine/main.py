from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

def coffeeReport():
    return coffee_machine.report()

def moneyReport():
    return money_machine.report()

def getMenu():
    return menu.get_items()

def findDrink(d):
    return menu.find_drink(d)

# Prompt user for input while "completed" equals 0
completed = 0
while completed == 0:
    options = getMenu()   
    userOrder = input(f"\nWhat would you like? ({options}) : ").lower()
    
    # Validate user input.
    if userOrder != "report" and userOrder != "off" and userOrder != "latte" and userOrder != "espresso" and userOrder != "cappuccino":
        print(f"\nInput not valid!\n")
    # Print reports if user types "report"
    elif userOrder == "report":
        coffeeReport()
        moneyReport()
    # Stop program when user types "off" by seting completed to 1
    elif userOrder == "off":
        completed += 1
    else:
        drink = findDrink(userOrder)
        # Check if there are sufficient resources to make drink
        if coffee_machine.is_resource_sufficient(drink):
             print("")
        # Count coins provided by customer and make drink if payment is sufficient.
        if money_machine.make_payment(drink.cost):
            print("")
            coffee_machine.make_coffee(drink)

    