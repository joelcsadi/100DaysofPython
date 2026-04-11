from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Paddle Creation
l_paddle = Paddle(pos=(-350,0))
r_paddle = Paddle(pos=(350,0))
ball = Ball()
scoreboard = Scoreboard()

# Paddle Movement
screen.listen()

# Left Paddle
screen.onkeypress(l_paddle.start_up, "w")
screen.onkeyrelease(l_paddle.stop_up, "w")
screen.onkeypress(l_paddle.start_down, "s")
screen.onkeyrelease(l_paddle.stop_down, "s")

# Right Paddle
screen.onkeypress(r_paddle.start_up, "Up")
screen.onkeyrelease(r_paddle.stop_up, "Up")
screen.onkeypress(r_paddle.start_down, "Down")
screen.onkeyrelease(r_paddle.stop_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # Enable user to hold key down instead of manual key press
    l_paddle.continuous_move()
    r_paddle.continuous_move()
    ball.move()
    screen.update()
    
    # Wall bouncing
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Paddle Bouncing
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("Made Contact")
        ball.x_bounce()
        ball.increase_speed()
    
    # Pong Scoring
    if ball.xcor() > 420:
        ball.reset_speed()
        ball.reset_ball()
        scoreboard.increase_l_score()

    if ball.xcor() < -420:
        ball.reset_speed()
        ball.reset_ball()
        scoreboard.increase_r_score()
    
    # Game Over by score
    if scoreboard.l_score >= 5  or scoreboard.r_score >= 5:
        scoreboard.game_over()
        game_is_on = False
    
screen.exitonclick()