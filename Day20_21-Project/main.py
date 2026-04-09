from turtle import Turtle, Screen
from snake import Snake
import time
# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating Snake Body (3 squares, each square is 20x20)
snake = Snake()
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
    
screen.exitonclick()