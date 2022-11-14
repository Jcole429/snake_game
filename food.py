from turtle import Turtle
from constant import *
import random


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
        random_x = random.randint(LEFT_LIMIT, RIGHT_LIMIT)
        random_y = random.randint(BOTTOM_LIMIT, TOP_LIMIT)
        self.goto(random_x, random_y)
