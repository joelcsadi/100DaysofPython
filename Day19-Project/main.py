from turtle import Turtle, Screen
import random

is_race_on = False
screen= Screen()
screen.setup(width=500,height=400)
user_guess =screen.textinput(title="Make your bet",prompt="Which turtle will enter the race? Enter a color: ").lower()
colors = ['red','orange','yellow','green','blue','purple']
all_turtles = []
y_coord = -100


for turtle_i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fastest")
    new_turtle.color(turtle_i)
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_coord)
    y_coord += 40
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance =random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()