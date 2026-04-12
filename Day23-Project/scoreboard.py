from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """
        Creates a Scoreboard that inherits from the Turtle Class.
        It has a level attribute and calls updates_scoreboard() initally.
        """
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
    
    def level_up(self):
        """
        Increases the level and calls update_scoreboard() to display it.
        """
        self.level +=1
        self.update_scoreboard() 
    
    def update_scoreboard(self):
        """
        Displays the level on the top left corner of the screen.
        It clears each time to prevent glitches.
        """
        self.goto(-280,260)
        self.clear()
        self.write(f"Level {self.level}", font=FONT)

    def game_over(self):
        """
        Displays a Game Over text in the center of the screen.
        """
        self.goto(0,0)
        self.color("black")
        self.write("GAME OVER",align="center", font=FONT)