"""
This is a blackjack game project that was a capstone project.
This was done from scratch without any hints or exterior help.

A user is asked to play blackjack. Once he agrees, 2 cards
are drawn for user and CPU. Only the CPU's first card is visible.

The possible cards are represented by an array of ints. Where 
an ace is either 11 or 1(only if above 21), normal numbers remain 
the same and the royal cards(King, Queen, Jack) give a score of 10.

If someone gets 21 in the first roll, they win automatically.
The user is prompted to either hit or stand. If they go over 21
they bust and lose! If the user does not bust and stands before 21,
the CPU is then prompted to draw cards until they bust or their
score is greater than 17.

If no one busts, whoever has the score closest to 21 wins!

The user is then prompted if they want to play again.

"""


from art import logo
import random
import os

def draw_card(hand):
    """
    Draws a card from the deck and adds it to deck.
    Updates the hand inplace.
    :param hand: list
    :return: None
    """
    new_card = random.choice(cards)
    hand.append(new_card)

def calculate_score(hand):
    """
    Calculates the score of the hand.
    :param hand: list
    :return: score: int
    """
    score = sum(hand)
    while score >21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def bust(score):
    """
    Checks if the hand is bust or not.
    :param score:
    :return: is_bust: bool
    """
    return score > 21

def display_score():
    """
    Displays the hand of the user, user score,
    and CPU first card.
    :return: None
    """
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {CPU_cards[0]}\n")

def display_final_score():
    """
    Displays the final hand of the user, user score,
    and CPU final hand and CPU score.
    :return: None
    """
    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(f"CPU final cards: {CPU_cards}, final score: {CPU_score}\n")

play_blackjack = input("Do you want to play blackjack? Type 'y' or 'n' ").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Deck of cards
if play_blackjack == "y":
    while play_blackjack == "y":
        game_over =False
        print(logo)
        # Randomly generating the cards for user
        user_cards = list()
        CPU_cards = list()

        # Card Selection for CPU and user
        for card in range(2):
            draw_card(user_cards)
            draw_card(CPU_cards)
        user_score = calculate_score(user_cards)
        CPU_score = calculate_score(CPU_cards)
        display_score()

        if user_score == 21 or CPU_score == 21:
            game_over = True

        # User deciding to hit or stand
        if not game_over:
            hit_or_stand = input("Type 'y' to get another card(hit) or type 'n' to pass(stand)").lower()
            while hit_or_stand == "y":
                draw_card(user_cards)
                user_score = calculate_score(user_cards)
                display_score()

                if bust(user_score) or user_score == 21:
                    break
                hit_or_stand = input("Type 'y' to get another card(hit) or type 'n' to pass(stand)").lower()

            # CPU drawing until bust or at least 17
            if not bust(user_score):
                while bust(CPU_score) == False and CPU_score <17 :
                    draw_card(CPU_cards)
                    CPU_score = calculate_score(CPU_cards)


        # Deciding the outcome of the match
        print("\n--- GAME OVER ---\n")

        if bust(user_score):
            print("Bust! You lose")
        elif bust(CPU_score):
            print("CPU busted! You win!")
        elif user_score > CPU_score:
            print("You win! You got closer or equal to 21!")
        elif user_score < CPU_score:
            print("You lose! CPU got closer or equal to 21!")
        else:
            print("Its a draw!")
        display_final_score()

        # Play another round?
        play_blackjack = input("Do you want to play blackjack? Type 'y' or 'n' ").lower()
        os.system('cls' if os.name == "nt" else 'clear')
