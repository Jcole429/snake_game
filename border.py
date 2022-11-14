from turtle import Turtle
from constant import *


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(RIGHT_LIMIT, BOTTOM_LIMIT)
        self.pendown()
        self.setposition(RIGHT_LIMIT, TOP_LIMIT)
        self.setposition(LEFT_LIMIT, TOP_LIMIT)
        self.setposition(LEFT_LIMIT, BOTTOM_LIMIT)
        self.setposition(RIGHT_LIMIT, BOTTOM_LIMIT)
