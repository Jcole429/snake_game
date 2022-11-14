from turtle import Turtle
from constant import *

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(COLOR)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition((0, SCOREBOARD_HEIGHT))
        self.clear()
        self.write("Score: {}".format(self.score), align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setposition((0, 0))
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
