"""
This is a rock paper scissors game that prompts the user
to enter a number (0 = Rock, 1 = Paper, 2 = Scissors).

A CPU also randomly chooses one of these numbers to challenge
the user.

A list of ASCII art is displayed representing each player's
choice. The choice is visualised in the console.

Based on the rules of rock paper scissors, the user can win,
lose or draw based on the choices.


"""

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)___)
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_decision = int(input("Welcome to rock paper scissors!\n"
                      "Type 0 for Rock, 1 for Paper, 2 for Scissors\n"
                      "What do you choose?\n"))

CPU_decision = random.randint(0,2)

image_list = [rock, paper, scissors]

if user_decision >= 3 or user_decision < 0:
    print("Invalid decision, You lose!")
    exit()
print(f"You chose: \n{image_list[user_decision]}")
print(f"CPU chose: \n{image_list[CPU_decision]}")

# Reduced checks by using cyclic modulus pattern, if difference % 3 == 1, User wins
# If difference % 3 == 2, User Loses
# If difference % 3 == 0 It's a draw, i.e. no difference between user and CPU decision
if (user_decision - CPU_decision) % 3 ==1:
    print("You win!")
elif user_decision == CPU_decision:
    print("Its a draw!")
else:
    print("You lose!")

# First brute force attempt with many checks

# if user_decision == 2 and CPU_decision == 0:
#     print(f"You lose!")
# elif user_decision == 0 and CPU_decision == 2:
#     print(f"You win!")
# elif user_decision >  CPU_decision:
#     print(f"You win!")
# elif user_decision < CPU_decision:
#     print(f"You lose!")
# elif user_decision == CPU_decision:
#     print(f"Its a draw!")


