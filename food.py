from turtle import Turtle
from constant import *
import random


def round_to_nearest_20(num):
    return 20 * round(num / 20)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = round_to_nearest_20(random.randint(LEFT_LIMIT, RIGHT_LIMIT))
        random_y = round_to_nearest_20(random.randint(BOTTOM_LIMIT, TOP_LIMIT))
        self.goto(random_x, random_y)
