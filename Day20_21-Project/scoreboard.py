from turtle import Turtle

ALIGNMENT = "center"
TEXTCOLOR = 'white'
FONT = ('courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        """
        Initialise the scoreboard attributes such as its score, position and color and
        calls the increase_score(self) function to display the initial score on the screen.
        """

        super().__init__()
        self.score = -1
        self.goto(0,280)
        self.color(TEXTCOLOR)
        self.hideturtle()
        self.increase_score()

    def update_scoreboard(self):
        """
        Updates the scoreboard by clearing the previous score and
        writing the new score on the screen.
        """
        self.clear()
        self.write(f"Score:{self.score}",align=ALIGNMENT, font=(FONT))

    def increase_score(self):
        """
        Increases the score by 1 and calls the update_scoreboard() method.
        """
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        """
        Displays "GAME OVER" message on the center of the screen when the game ends.
        """
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    

        
