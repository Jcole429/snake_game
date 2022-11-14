from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)

    for seg_num in range(len(segments) - 1, 0, -1):
        previous_seg_position = segments[seg_num-1].position()
        segments[seg_num].goto(previous_seg_position)
    segments[0].forward(20)

screen.exitonclick()
