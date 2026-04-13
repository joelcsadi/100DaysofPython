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
        with open("Day20_21-Project/data.txt") as file:
            self.highscore = int(file.read())
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
        self.write(f"Score:{self.score} High Score: {self.highscore}",align=ALIGNMENT, font=(FONT))

    def increase_score(self):
        """
        Increases the score by 1 and calls the update_scoreboard() method.
        """
        self.score +=1
        self.update_scoreboard()

    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Day20_21-Project/data.txt", mode="w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()


    

        
