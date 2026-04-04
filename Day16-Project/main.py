from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    """
    Simulates a coffee machine by utilising external classes and modules to abstract
    the process of ordering, paying and receiving a coffee.
    """
    # Creating the Objects required for the Coffee Machine 
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True
    while is_on:
        user_choice = input(f"What would you like? {menu.get_items()} ").lower()
        if user_choice == "off":
            is_on = False
        elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        # If the choice is on the menu
        elif menu.find_drink(user_choice):
            drink = menu.find_drink(user_choice)
            # Check if sufficient resources for the drink
            sufficient_resources = coffee_maker.is_resource_sufficient(drink)
            if sufficient_resources:
                cost = drink.cost
                sufficient_funds = money_machine.make_payment(cost)
                # If enough money accepted
                if sufficient_funds:
                    coffee_maker.make_coffee(drink)

main()
