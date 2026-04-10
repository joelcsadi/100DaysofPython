from turtle import Turtle
import random

class Food(Turtle):
    """
    This class creates a food object that the snake can eat to grow longer and increase the score.
    It inherits from the Turtle class and has a refresh method that randomly places the food on the screen
    
    """
    def __init__(self):
        """
        Initialise the food attributes such as its shape, color and speed and
        calls the refresh(self) function to randomly place the food on the screen.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

    
    def refresh(self):
        """
        Randomly places the food on the screen within the boundaries of the game."""
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280,280)
        self.goto(rand_x,rand_y)

    

        