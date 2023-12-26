from turtle import Screen, Turtle
from Day22_paddle_class import Paddle
from Day22_ball_class import Ball
import time
from Day22_scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

# create both paddles given the location of the paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
# right paddle controls
screen.onkey(fun=r_paddle.pad_up, key='Up')
screen.onkey(fun=r_paddle.pad_down, key='Down')

# left paddle controls
screen.onkey(fun=l_paddle.pad_up, key='w')
screen.onkey(fun=l_paddle.pad_down, key='s')

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    # ball goes off screen
    if ball.xcor() > 380:
        print("point added")
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        print("point added")
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()