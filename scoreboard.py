from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(COLOR)
        self.setposition((0, 270))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write("Score: {}".format(self.score), align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
