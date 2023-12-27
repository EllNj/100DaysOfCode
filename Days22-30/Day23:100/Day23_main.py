import time
from turtle import Screen
from Day23_player import Player
from Day23_car_manager import CarManager
from Day23_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()

scoreboard = Scoreboard()

car_manager = CarManager()

car_manager.new_car()

screen.listen()
screen.onkey(fun=player.move, key='w')


game_is_on = True
count = 0   # count to make the cars only spawn every 6th loop
while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()

    # checks the finish before continuing the code
    if player.check_finish():
        scoreboard.update_level()
        player.return_to_start()
        car_manager.increase_speed()

    # spawns new car every 6th time
    if count % 6 == 0:
        car_manager.new_car()

    car_manager.move_car()

    # checks for collisions
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
