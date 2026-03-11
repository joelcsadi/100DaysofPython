"""
    Creates a greeting .
    Ask the user for the city that they grew up in and store it in a variable.
    Ask the user for the name of a pet and store it in a variable.
    Combines the name of their city and pet and show them their band name.
"""
print("Welcome to the Band Name Generator")
city_name = input("What city did you grow up in?\n")
pet_name = input("What's your pet's name?\n")
print("Your band name could be " + city_name + " " + pet_name)
