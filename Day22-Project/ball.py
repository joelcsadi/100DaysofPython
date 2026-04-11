from turtle import Turtle
STARTINGPOSITION= (0,0)

class Ball(Turtle):
    
    def __init__(self):
        """
        Initialise a ball object that starts centered at (0,0) on the screen with a 
        moving distance of 10 each frame it moves. It inherits from the Turtle class.
        """
        super().__init__()
        self.x = STARTINGPOSITION[0]
        self.y = STARTINGPOSITION[1]
        self.y_move_distance = 10
        self.x_move_distance = 10
        self.create_ball()  
    
    def create_ball(self):
        """
        Creates a white circular ball object at (0,0) and starts to move.
        """
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(STARTINGPOSITION)
        self.move()
        
    def move(self):
        """
        Moves the ball in the x and y direction its currently moving by the moving distance,
        which can be increased every paddle touch.
        """
        self.x = self.xcor() + self.x_move_distance
        self.y = self.ycor() + self.y_move_distance
        self.goto(self.x,self.y)

    def y_bounce(self):
        """
        Change y direction of the ball when it reaches the top and bottom walls of the screen.
        """
        self.y_move_distance *= -1
    
    def x_bounce(self):
        """
        Chang x direction of the ball when it reaches the paddle surface on either
        """
        self.x_move_distance *= -1

    def reset_ball(self):
        """
        After a point is scored, the ball move distance and position are reset to
        the initial attributes.
        """
        self.x_move_distance *= -1
        self.y_move_distance *= -1
        self.x = STARTINGPOSITION[0]
        self.y = STARTINGPOSITION[1]
        self.goto(self.x,self.y)

    def increase_speed(self):
        """
        Once a paddle hits the ball, the move distance is increased per frame
        which speeds up the ball until the point is scored.
        """
        if self.x_move_distance < 0:
              self.x_move_distance -= 1
        else:
             self.x_move_distance += 1
    
        if self.y_move_distance < 0:
              self.y_move_distance -= 1
        else:
             self.y_move_distance += 1
        
    def reset_speed(self):
        """
        Once a point is scored, the speed(move_distance per frame)
        is reset to its initial attribute.
        """
        self.x_move_distance = 10
        self.y_move_distance = 10