"""
This is a game script that simulates fixed scenarios of a treasure hunt.
You make choices and based on conditionals, you either find the treasure
or lost and its game over.
"""

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're in a cave on the island and have to choose which cave to go in "
                  "(Left or Right?)\n").lower()

if direction == "left":
    action = input("In the cave, you can wait for the cave boat or go for a swim."
                   " (Wait or Swim?)\n").lower()
    if action == "wait":
        door = input("You're waiting and a boat arrives and brings you to a secret hideout. "
              "Which door do you choose? (Yellow, Red or Blue)\n").lower()
        if door == "yellow":
            print("You found the treasure full of gold and diamonds!")
        elif door == "red":
            print("Game over, the undead pirates awake from their sleep and stab you!")
        elif door == "blue":
            print("Game over, the goblins hear you approaching and attack you!")
        else:
            print("Wrong door! You fell into a trap, Game over!")
    else:
        print("Game over! A shark comes up behind you and devours you")

else:
    print("Game over, The dragon inside burnt you with its flames")