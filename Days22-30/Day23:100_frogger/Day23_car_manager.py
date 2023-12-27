import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        rand_y = random.randint(-250, 250)
        rand_color = random.randint(0, len(COLORS)-1)
        car = Turtle(shape='square')
        car.penup()
        car.color(COLORS[rand_color])
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.teleport(x=300, y=rand_y)
        car.setheading(180)
        self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
