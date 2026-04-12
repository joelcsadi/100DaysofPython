from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X_POS = 300

class CarManager():

    def __init__(self):
        """
        Creates a car manager class that has a list of the cars on screen and 
        the speed that all cars will move at.
        """
        self.cars_list = []
        self.car_speed= STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        Creates the car using the turtle class facing west(right) that is randomly
        placed on the y axis. Each car is (40,20) px. Each car created is added to the list 
        of the cars list.

        """
        new_car = Turtle()
        new_car.setheading(180) 
        y_car_pos = random.randint(-250,250) # 50 px from top and bottom spawn no cars
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.goto(STARTING_X_POS, y_car_pos)
        self.cars_list.append(new_car)

    def move_car(self):
        """
        Moves every car in the car manager list by the car speed
        If the car is off the screen, the car is removed to prevent overloading the list
        """
        for car in self.cars_list[:]:
            car.forward(self.car_speed)
            if car.xcor() < -340:
                car.hideturtle()
                self.cars_list.remove(car)
    
    def speed_up(self):
        """
        Increase the speed of the cars by the MOVE_INCREMENT constant.
        """
        self.car_speed += MOVE_INCREMENT 