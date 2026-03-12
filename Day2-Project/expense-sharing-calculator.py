"""
This is an expense sharing calculator that prompts the user
for the total bill, the percent tip they want to add on, and
how many people want to split the bill.

It returns the price of how much each person has to pay
if they all paid an equal percentage.
"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percentage_tip = 1 + (tip / 100)
pay_per_person = round((bill / people) * percentage_tip,2)
print(f"Each person should pay ${pay_per_person}")