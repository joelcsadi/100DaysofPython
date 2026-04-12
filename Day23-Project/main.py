import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating the objects for gameplay
player = Player()
car = CarManager()
scoreboard= Scoreboard()

# Player Movement
screen.listen()
screen.onkey(player.move_player,"Up")

# Game Loop
game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    # Creates a car every 6 iterations
    if counter % 6 == 0:
        car.create_car()
    # Moves each car
    car.move_car()
    # Checks every vehicle if its close to the player
    for vehicle in car.cars_list:
        if player.distance(vehicle) < 20:
            scoreboard.game_over()
            screen.update()
            time.sleep(2)
            game_is_on = False
            break
        
    # If player levels up
    if player.check_finish():
        car.speed_up()
        scoreboard.level_up()