import turtle as t
from random import choice

colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73)]


t.colormode(255)
leo = t.Turtle()
leo.hideturtle()
leo.pensize(2)
leo.speed("fastest")
# 10 x 10 grid, 50 steps, 20 size
leo.up()

for column in range(10):
    leo.setheading(0)
    for row in range(10):
        leo.dot(20,choice(colors))
        leo.forward(50)
    leo.setheading(90)
    leo.forward(50)
    leo.setheading(180)
    leo.forward(500)


screen = t.Screen()
screen.exitonclick()
