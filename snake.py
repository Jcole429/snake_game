from turtle import Turtle
from constant import *
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    segments = []

    def __init__(self):
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            previous_seg_position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(previous_seg_position)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN_DEGREES:
            self.head.setheading(UP_DEGREES)

    def down(self):
        if self.head.heading() != UP_DEGREES:
            self.head.setheading(DOWN_DEGREES)

    def left(self):
        if self.head.heading() != RIGHT_DEGREES:
            self.head.setheading(LEFT_DEGREES)

    def right(self):
        if self.head.heading() != LEFT_DEGREES:
            self.head.setheading(RIGHT_DEGREES)
