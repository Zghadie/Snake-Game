import time

from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard

screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game ")
"""my way of making a snake"""
# snake_avatar = Turtle(shape="square")
# snake_avatar.color("green")
# snake_avatar.goto(x=0, y=0)
# snake_avatar_1 = Turtle(shape="square")
# snake_avatar_1.color("green")
# snake_avatar_1.goto(x=-20, y=0)
# snake_avatar_2 = Turtle(shape="square")
# snake_avatar_2.color("green")
# snake_avatar_2.goto(x=-40, y=0)
"""profs way of making a snake, easy way"""
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# segments = []
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#
#     for seg_num in range(len(segments)-1, 0, -1):
#         new_x = segments[seg_num -1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x,new_y)
#     segments[0].forward(20)
"""prof making a snake calss to use"""
scoreboard = Scoreboard()
snake = Snake()
food =Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.0001)
    snake.move()
    #detec when snake touch food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        scoreboard.reset()

        #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


















screen.exitonclick()