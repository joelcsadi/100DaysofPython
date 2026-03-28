from art import *
from game_data import *
import random
import os


def choose_character():
    """
    Choose a random entity to be included in the game round.
    If a character is already in the list, it randomly selects another until
    they're unique.
    """
    duplicated_characters = True
    while duplicated_characters:
        character_selection = random.choice(data)
        if character_selection not in round_characters:
            round_characters.append(character_selection)
            duplicated_characters = False


def display_stats():
    """
    Display statistics about the game round and its players.
    """
    print(f"Compare A: {round_characters[0]['name']}, a {round_characters[0]['description']}, from {round_characters[0]['country']}")
    print(vs)
    print(f"Against B: {round_characters[1]['name']}, a {round_characters[1]['description']}, from {round_characters[1]['country']}")

def increase_score(current_score):
    """
    Increase score of the player if they win.
    :param current_score: current score of the player
    :return final_score: int
    """
    final_score = current_score +1
    return final_score

def remove_character_from_list():
    """
    Remove the first character from the round characters list.
    """
    round_characters.pop(0)

round_characters = []
score =0
continue_game = True
for character in range(2):
    choose_character()

while continue_game:
    print(logo)
    if score >0:
        print(f"You're right! Current Score: {score}")
    display_stats()
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_guess == 'A':
        if round_characters[0]["follower_count"] >= round_characters[1]["follower_count"]:
            os.system("cls" if os.name =="nt" else "clear")
            score =increase_score(score)
            remove_character_from_list()
            choose_character()
        else:
            os.system("cls" if os.name =="nt" else "clear")
            print(logo)
            print("---GAME OVER---")
            print(f"Wrong! Final Score: {score} ")
            continue_game = False
    elif user_guess == 'B':
        if round_characters[0]["follower_count"] <= round_characters[1]["follower_count"]:
            os.system("cls" if os.name =="nt" else "clear")
            score =increase_score(score)
            remove_character_from_list()
            choose_character()

        else:
            os.system("cls" if os.name =="nt" else "clear")
            print(logo)
            print("---GAME OVER---")
            print(f"Wrong! Final Score: {score} ")
            continue_game = False
    
    


