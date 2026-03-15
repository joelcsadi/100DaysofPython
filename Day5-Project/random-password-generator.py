"""
This is a random password generator that prompts the user to
enter the desired amount of letters, numbers and symbols they
want to include in their password.

Using lists and the random module, we choose random characters
via for loops using random.choice and add them to the list
of chars.

We then shuffle the result in order to get a randomised
order.
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Version where its sequentially added
# First the letters -> symbols -> numbers

password = []
for letter in range(nr_letters):
    password.append(random.choice(letters))
for symbol in range(nr_symbols):
    password.append(random.choice(symbols))
for number in range(nr_numbers):
    password.append(random.choice(numbers))

print(password)

# Harder Version, we want to randomize the items in the list

random.shuffle(password)
print(password)

print(f"Your password is {''.join(password)} ")