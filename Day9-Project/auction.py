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

