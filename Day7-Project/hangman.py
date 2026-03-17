"""
This is hangman game where a random word is chosen and 
the player wins by guessing all the letters in that word.

If they choose a letter that's not in the word, they will
lose a life. There's 6 lives and when the gallows in ASCII
ART are completed with a whole person, its game over and you
lose!
"""
import os
import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

#Creating the mystery word as underscore placeholders
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Creating variables that will change over time in the game
game_over = False
correct_letters = set()
incorrect_letters = set()
display =""

while not game_over:

    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    # Clears terminal after each letter input. Suitable for both
    # Windows and Linux/MacOS terminals
    os.system('cls' if os.name == 'nt' else 'clear')


    # Don't take a life if the letter has already been guessed
    if guess in correct_letters or guess in incorrect_letters:
        print(f"{display}")
        print(f"'{guess}' has already been guessed")
        continue
    # Reset the display string each time so it doesn't duplicate
    display = ""

    # Go through every letter in the word and check if 
    # it matches the guessed word. We update the string as 
    # necessary and store the correct letters in a list.
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.add(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # Losing a life if chose the wrong letter
    if guess not in chosen_word:
        print(f"You guessed {guess},which is not in the word. You lost a life!")
        incorrect_letters.add(guess)
        lives -= 1

        # Running out of lives ie. 0 is game over!
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # You win when there's no more to guess ie. no more blanks
    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN****************************")

    # Stages is the list of ascii images representing the gallows stages
    print(stages[lives])