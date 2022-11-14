from turtle import Turtle
from constant import *


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(RIGHT_LIMIT + 10, BOTTOM_LIMIT - 10)
        self.pendown()
        self.setposition(RIGHT_LIMIT + 10, TOP_LIMIT + 10)
        self.setposition(LEFT_LIMIT - 10, TOP_LIMIT + 10)
        self.setposition(LEFT_LIMIT - 10, BOTTOM_LIMIT - 10)
        self.setposition(RIGHT_LIMIT + 10, BOTTOM_LIMIT - 10)
