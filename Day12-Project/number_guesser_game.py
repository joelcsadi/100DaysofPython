from art import logo
import random



def lose_life(lives):
    """
    Decrements the lives counter of the player
    :Param lives:int
    :return lives -1:int
    """
    return lives -1

def check_lives(lives):
    """
    Checks whether the lives counter of the player has reached 0
    :Param lives:int
    :return :bool
    """
    return lives == 0

def choose_difficulty():
    """
    Selects the lives the user starts with based on input difficulty.
    It prompts until the user selects a valid choice.
    :return lives:int
    """
    difficulty = ""
    valid_difficulty = ['easy','hard']
    while difficulty not in valid_difficulty:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            lives = 10
        elif difficulty == "hard":
            lives = 5
    return lives

def play_guess_the_number():
    """
    A guessing game where the user has to guess a number
    from 1-100 inclusive that the CPU has randomly chosen.  

    Depending on user's choice, the difficulty will vary the amount
    of lives the user has.

    If the user guesses the wrong number, he loses a life.
    The user also is guided whether he should go higher or lower
    than his current guess.

    The game ends when the user guesses the right number or
    runs out of lives.  

    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1,100)

    print("I am thinking of a number between 1 and 100.")
    lives = choose_difficulty()
    game_over = False

    while lives > 0 and game_over == False:
        print(f"You have {lives} lives left to guess the number!")
        guess = int(input("Make a guess: "))
        if guess == number:
            game_over = True
            print(f"You guessed the answer. The number was {number} ")
        elif guess > number:
            lives =lose_life(lives)
            print("Too High.\nGuess again. ")
            if check_lives(lives):
                game_over = True
                break
        else:
            lives =lose_life(lives)
            if check_lives(lives):
                game_over = True
                break
            print("Too Low.\nGuess again. ")
    if check_lives(lives):
        print(f"Game Over. You have no more lives! The number was {number}")


while True:
    play_guess_the_number()
    play_again = input("Do you want to play again Type ('yes' or 'no')? ").lower()
    if play_again == "no":
        break
