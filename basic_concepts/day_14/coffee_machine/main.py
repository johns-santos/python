from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
# Prompt user for input while "completed" equals 0
completed = 0
while completed == 0:
    options = menu.get_items()
    
    while True:
        
        try:
            choice = input(f"\nWhat would you like? ({options}) : ").lower()
            if choice == "off":
                completed = 1
            elif choice == "report":
                coffee_machine.report()
                money_machine.report()
            else:
                drink = menu.find_drink(choice)
            if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
        except AttributeError:
            pass
        except ValueError: 
            pass
