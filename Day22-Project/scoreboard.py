from turtle import Turtle
LEFT_SCORE_POS = (-100,200)
RIGHT_SCORE_POS = (100,200)
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        """
        Initialises a scoreboard object that sets initial player scores and 
        calls the update_scoreboard() function to visualise the current scores
        per player.
        """
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def increase_l_score(self):
        """
        When the right player concedes, the left score is increased and is updated on the
        screen.
        """
        self.l_score +=1
        self.update_scoreboard()

    def increase_r_score(self):
        """
        When the left player concedes, the right score is increased and is updated on the
        screen.
        """
        self.r_score +=1
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clears the previous scores and rewrites the scores at their respective constant
        positions with large font. This is called each time a point is scored.
        """
        self.clear()
        self.goto(LEFT_SCORE_POS)
        self.write(self.l_score, align="center", font= (FONT))
        self.goto(RIGHT_SCORE_POS)
        self.write(self.r_score, align="center", font= (FONT))

    def game_over(self):
        """
        Once a player wins by scoring 5 points, Game Over is written
        on the screen.
        """
        self.goto(0,0)
        self.write("GAME OVER", align= "center", font= (FONT))