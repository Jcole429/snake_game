from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
from constant import *
import time

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
border = Border()

screen.listen()
screen.onkey(snake.up, UP_TEXT)
screen.onkey(snake.down, DOWN_TEXT)
screen.onkey(snake.left, LEFT_TEXT)
screen.onkey(snake.right, RIGHT_TEXT)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(SCREEN_REFRESH_RATE)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > RIGHT_LIMIT or snake.head.xcor() < LEFT_LIMIT or snake.head.ycor() > TOP_LIMIT or snake.head.ycor() < BOTTOM_LIMIT:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
