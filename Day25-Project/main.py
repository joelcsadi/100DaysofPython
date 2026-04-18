import turtle
import pandas as pd

# Reading in dataset and extracting columns as lists
states_data =pd.read_csv("Day25-Project/50_states.csv")
all_states = states_data["state"].to_list()

# Setting up turtle screen and background
screen = turtle.Screen()
screen.title("U.S.A States Game")
image = "Day25-Project/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
correct_guesses_list = []

score = 0
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 guessed correct states",prompt="Guess state name").title()
    # Game finishes when user guesses all states
    if len(correct_guesses_list) > 50:
        game_is_on = False
    
    # Game finishes and creates a csv with missing states
    elif answer_state == "Exit":
        game_is_on = False
        learn_states = [state for state in all_states if state not in correct_guesses_list]
        state_dict = {"State" : learn_states}
        df = pd.DataFrame(state_dict)
        df.to_csv("Day25-Project/states_to_learn.csv")

    # User guesses correct state they have not yet guessed already.
    elif answer_state in all_states and answer_state not in correct_guesses_list:
        correct_guesses_list.append(answer_state)
        chosen_state_row = states_data[states_data["state"] == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(chosen_state_row.x.item(),chosen_state_row.y.item())
        t.write(answer_state)
        score +=1






    