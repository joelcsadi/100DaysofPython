from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """
        Player inherits the methods and attributes of the turtle Class.
        It calls the create_player() method
        """
        super().__init__()
        self.create_player()
    
    def create_player(self):
        """
        Creates the player as a turtle facing north.
        It calls setup_player() for position purposes.
        """
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.setup_player()

    def setup_player(self):
        """
        Moves the player to the starting position
        """
        self.goto(STARTING_POSITION)

    def move_player(self):
        """
        Moves the player by a distance.
        """
        self.forward(MOVE_DISTANCE)

    def check_finish(self):
        """
        Checks if the player has crossed the finish line
        :return boolean
        """
        if self.ycor() > FINISH_LINE_Y:
            self.setup_player()
            return True
        return False



    
        

    
