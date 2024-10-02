from turtle import Screen, Turtle
from Paddle import Paddle
from Pong import Pong
from scoreboard import ScoreBoard
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAMEEE!!!")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong = Pong()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
bot_speed = 8
bot_delay_chance = 0.6

while game_is_on:
    time.sleep(pong.move_speed)
    screen.update()
    pong.move()

    # Detect collision for the pong
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.y_bounce()

    # Detect collision with paddles
    if pong.distance(r_paddle) < 50 and pong.xcor() > 320 or pong.distance(l_paddle) < 50 and pong.xcor() < -320:
        pong.x_bounce()

    # Detect R paddle misses
    if pong.xcor() > 380:
        pong.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if pong.xcor() < -380:
        pong.reset_position()
        scoreboard.r_point()


    if random.random() > bot_delay_chance:  # Only move the bot sometimes
        if r_paddle.ycor() < pong.ycor():
            new_y = r_paddle.ycor() + bot_speed
            if new_y > 280:  # Prevent the paddle from going out of bounds
                new_y = 280
            r_paddle.goto(r_paddle.xcor(), new_y)
        elif r_paddle.ycor() > pong.ycor():
            new_y = r_paddle.ycor() - bot_speed
            if new_y < -280:  # Prevent the paddle from going out of bounds
                new_y = -280
            r_paddle.goto(r_paddle.xcor(), new_y)

screen.exitonclick()
