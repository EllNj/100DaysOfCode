import turtle

james = turtle.Turtle()
# imported a module and used a class from the module with () to initialise an object called james

# to make it cleaner could use from turtle import Turtle
james.shape("turtle")
james.color("DeepSkyBlue")
print(james)
james.forward(100)
james.left(90)
james.forward(100)
james.left(90)
james.forward(100)
james.left(90)
james.forward(100)
for i in range(0,51):   # decided to make a little square
    james.left(90)
    james.forward(1)
    james.left(90)
    james.forward(100)
    james.right(90)
    james.forward(1)
    james.right(90)
    james.forward(100)

james.color("DarkMagenta")
james.left(90)
james.forward(100)
james.left(90)
james.forward(100)
james.left(90)
james.forward(100)
james.left(90)
james.forward(100)
for i in range(0,51):
    james.left(90)
    james.forward(1)
    james.left(90)
    james.forward(100)
    james.right(90)
    james.forward(1)
    james.right(90)
    james.forward(100)


my_screen = turtle.Screen()
print(my_screen.canvheight)
# object.attribute


my_screen.exitonclick()
# object.method()



