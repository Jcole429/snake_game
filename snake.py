from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    segments = []

    def __init__(self):
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            previous_seg_position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(previous_seg_position)
        self.segments[0].forward(MOVE_DISTANCE)
