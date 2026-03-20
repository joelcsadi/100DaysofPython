"""
This is a program that simulates a calculator. It allows the user
to perform calculations such as addition, subtraction, multiplication
and division.

It prompts the user to enter two numbers and an operation 
and it calls one of the maths functions below.

It prompts the user whether to continue calculating with the
cumulative result, start a new calculation with the result wiped
or to quit the program as a whole.

Also implements error catching to improve user experience such 
as ZeroDivisionError, value error catching.
"""

from art import logo
def add(n1, n2):
    """
    Returns the sum of the two numbers.
    """
    return n1 + n2

def subtract(n1, n2):
    """
    Returns the difference of the two numbers.
    """
    return n1 - n2

def multiply(n1, n2):
    """
    Returns the product of the two numbers.
    """
    return n1 * n2

def divide(n1, n2):
    """
    Returns the division of the two numbers where n2 is the 
    denominator.
    """
    return n1 / n2

# Add these 4 functions into a dictionary

operations ={
    "+": add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
print(logo)
def calculator():
    """
    Provides calculator functions such as addition, subtraction,
    multiplication and division.
    """
    accumulate_answer = True
    try:
        num1 = float(input("Enter the first number: "))
        while accumulate_answer:
            operator = input("Enter the operation '+', '-', '*' or '/': ")
            if operator not in operations:
                print("Invalid operation, please try again.")
                continue
            next_num = float(input("Enter the second number: "))
            my_operation = operations[operator]
            result = my_operation(num1, next_num)
            print(f"{num1} {operator} {next_num} = {result}")

            valid_user_preference =False
            while not valid_user_preference:
                user_preference = input("Do you want to continue working with the "
                                       "the same result(type 'y'), start a new calculation(type 'n') or stop(type 's')?")
                if user_preference == "n":
                    accumulate_answer = False
                    valid_user_preference = True
                    calculator()
                elif user_preference == "y":
                    valid_user_preference = True
                    num1 = result
                elif user_preference == "s":
                    accumulate_answer = False
                    valid_user_preference = True
                    return
                else:
                    print("Invalid input, please try again.")
    except ValueError:
        print("Invalid input, please try again.")
        calculator()
    except ZeroDivisionError:
        print("Cannot divide a number by 0, please try another denominator(next_num).")
        calculator()


calculator()