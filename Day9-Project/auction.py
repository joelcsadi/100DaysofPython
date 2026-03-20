"""
This is a secret auction program that prompts a user in an
auction with their name and the price they want to bid.

This data is stored in a dictionary with {name: bid}
and bids are prompted until there are no more bidders.

If there's another bidder, the terminal is cleared so the secrecy
of the auction is maintained.

Then a function is called to see who has won the auction by bidding
the highest bid.
"""


import os
from art import logo

print("Welcome to the secret auction program.")
continue_bidding = True
auction = dict()

while continue_bidding:
    print(logo)
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction[name] = bid
    valid_input = False
    while not valid_input:
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
        if more_bidders == 'no':
            continue_bidding = False
            valid_input= True

        elif more_bidders == 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            valid_input = True
        else:
            print("Not a valid choice. Choose 'yes' or 'no'.")

def find_highest_bidder(auction):
    highest_bid = 0
    highest_bidder = ""
    for bidder,price in auction.items():
        if price > highest_bid:
            highest_bid = price
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

find_highest_bidder(auction)

