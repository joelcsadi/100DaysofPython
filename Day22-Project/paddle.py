from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, pos):
        """
        Initialise a paddle object that sets the moving_up/moving_down flags to false
        and then creates the paddle using that position.
        :param pos - The initial position that each paddle starts at
        """
        super().__init__()
        self.pos = pos
        self.moving_up = False
        self.moving_down = False
        self.create_paddle(pos)
    
    def create_paddle(self,pos):
        """
        Creates a white rectangular moving paddle at the position inputted.
        : param pos - The initial position that each paddle starts at
        
        """
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def start_up(self):
        """
        Flags whether the user is moving up with the respective key
        """
        self.moving_up = True

    def stop_up(self):
        """
        Flags whether the user stops moving up with the respective key
        """
        self.moving_up = False

    def start_down(self):
        """
        Flags whether the user is moving down with the respective key
        """
        self.moving_down = True

    def stop_down(self):
        """
        Flags whether the user stops moving down with the respective key
        """
        self.moving_down = False

    def continuous_move(self):
        """
        When a key is pressed up/down, update the position in their respective key pressed
        """
        if self.moving_up:
            self.sety(self.ycor() + 20)
        if self.moving_down:
            self.sety(self.ycor() - 20)