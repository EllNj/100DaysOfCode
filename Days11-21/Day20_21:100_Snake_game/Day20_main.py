from turtle import Screen
import time
from Day20_snakeClass import Snake
from Day21_foodClass import Food
from Day21_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # check if hit food
    if snake.head.distance(food) < 15:
        food.respawn()
        scoreboard.increase_score()
        snake.grow()
        scoreboard.update_scoreboard()
    # check if hit border
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    # check collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()









screen.exitonclick()
