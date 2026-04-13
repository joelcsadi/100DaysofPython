from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating Snake Body (3 squares, each square is 20x20)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

# Snake Controls
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
is_game_on = True

# Gameplay 
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        print("Nom Nom Nom")
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        scoreboard.reset()
        snake.reset()

    # Detect Collision with tail segments(ie. not head with head) so we slice from index 1 not 0
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()