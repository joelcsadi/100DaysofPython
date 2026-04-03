def calculate_money():
    """
    Calculates the sum of the coins entered by the user.
    Includes quarters, dimes, nickels and pennies.
    :return total_money_inserted: float
    """
    valid_money = False
    while not valid_money:
        try:
            quarters = int(input("How many quarters?")) * 0.25
            dimes = int(input("How many dimes?")) * 0.10
            nickels = int(input("How many nickels?")) *0.05
            pennies = int(input("How many pennies?")) * 0.01
            total_money_inserted =  round(quarters + dimes + nickels +pennies,2)
            print(f"You have inserted ${total_money_inserted:.2f}")
            return total_money_inserted
        except ValueError:
            print("Please enter a number")
    return None


def main():
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }

    continue_prompting = True
    while continue_prompting:
        # Reset for each order
        valid_user_prompt = False
        sufficient_resources = True

        # Input Validation for prompt
        # Choices ['latte', 'espresso', 'cappuccino', 'report','off']
        while not valid_user_prompt :
            user_prompt = input("What would you like?").lower()
            # Prompt result
            if user_prompt == "off":
                continue_prompting = False
                valid_user_prompt = True
                sufficient_resources = False
                break
            elif user_prompt == "report":
                print(resources)
                valid_user_prompt = True
                sufficient_resources = False

            elif user_prompt in MENU:
                for key in MENU[user_prompt]["ingredients"].keys():
                    if resources[key] < MENU[user_prompt]["ingredients"][key]:
                        print(f"Sorry, there's not enough {key}  ")
                        sufficient_resources = False
                valid_user_prompt = True

        if sufficient_resources:
            # Inputting money
            print("Please enter your coins")
            money_inserted = calculate_money()

            # Not enough Money
            if money_inserted < MENU[user_prompt]["cost"]:
                print("Sorry that's not enough money. Money Refunded")

            # No change scenario
            elif money_inserted == MENU[user_prompt]["cost"]:
                print("Thank you!")
                resources["money"] += money_inserted
                for key in MENU[user_prompt]["ingredients"].keys():
                    resources[key] -= MENU[user_prompt]["ingredients"][key]
                print(f"Here's your {user_prompt}, enjoy!")


            # Change required to give
            elif money_inserted > MENU[user_prompt]["cost"]:
                resources["money"] += MENU[user_prompt]["cost"]
                change = round(abs(money_inserted - MENU[user_prompt]["cost"]),2)
                for key in MENU[user_prompt]["ingredients"].keys():
                    resources[key] -=  MENU[user_prompt]["ingredients"][key]

                print(f"Thank you! Here's your change ${change:.2f}.")
                print(f"Here's your {user_prompt}, enjoy!")

main()