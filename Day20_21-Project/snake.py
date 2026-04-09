from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0), (-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

OPPOSITES = {UP:DOWN, DOWN:UP, LEFT:RIGHT, RIGHT:LEFT}

class Snake:
    def __init__(self):
        """
        Initialise snake attributes such as its segments and the snake head
        and calls the create_snake(self) function to assign variables to its attributes.
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
        
    def create_snake(self):
        """
        Creates a snake with 3 white squares in constant positions on the screen
        and adds the square segments to the segments list. 
        """
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    def move(self):
        """
        Simulates movement of a snake. It loops through the segments from the end and 
        moves the 3rd segment to the 2nd segment pos, 2nd to the 1st and then the 
        head moves in the direction its heading by its constant MOVE_DISTANCE.
        """
        for seg_num in range(len(self.segments)-1,0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    
    def right(self):
        """
        Turns snake head right only if it's not facing left. The head can't turn into the tail.
        """
        if self.head.heading() != OPPOSITES[RIGHT]:
            self.head.setheading(RIGHT)

    def up(self):
        """
        Turns snake head up only if it's not facing down. The head can't turn into the tail.
        """
        if self.head.heading() != OPPOSITES[UP]:
            self.head.setheading(UP)

    def left(self):
        """
        Turns snake head left only if it's not facing right. The head can't turn into the tail.
        """
        if self.head.heading() != OPPOSITES[LEFT]:
            self.head.setheading(LEFT)

    
    def down(self):
        """
        Turns snake head down only if it's not facing up. The head can't turn into the tail.
        """
        if self.head.heading() != OPPOSITES[DOWN]:
            self.head.setheading(DOWN)
    

