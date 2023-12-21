import turtle as t

from random import *

t.colormode(255)
donny = t.Turtle()
donny.shape("turtle")
donny.color('Green')

# draw a square
# for i in range(4):
#     donatello.forward(100)
#     donatello.left(90)

# Dashed line
# for i in range(12):
#     donatello.down()
#     donatello.forward(10)
#     donatello.up()
#     donatello.forward(10)


# Making shapes from tri to dec with random colours
# def make_shape(sides):
#     angle = 360 / sides
#     for x in range(sides):
#         donatello.forward(150)
#         donatello.right(angle)
#
#
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "chocolate3", "DeepPink2", "azure2",
           "gold", "navy", "firebrick1", "LightSalmon", "pink1", "thistle"]
#
# for i in range(3, 11):
#     donatello.color(choice(colors))
#     make_shape(i)

# creating a random colour without creating a list (RGB)
def random_colour():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return(r, g, b)


# Random path with increased pen width
# directions = [0, 90, 180, 270]
# distance = randint(40,100)
# donatello.pensize(15)
# donatello.speed(10)
# for i in range(distance):
#     donatello.color(random_colour())
#     donatello.forward(20)
#     donatello.setheading(choice(directions))

# spirograph
# donatello.speed("fastest")
# for i in range(0, 360, 5):
#     donatello.color(random_colour())
#     donatello.circle(100)
#     donatello.setheading(i)




screen = t.Screen()
screen.exitonclick()
