from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()

def move_forwards():
    leo.forward(10)
def move_backwards():
    leo.backward(10)
def turn_left():
    leo.left(10)

def turn_right():
    leo.right(10)


def clear():
    leo.reset()

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear, key='c')

screen.exitonclick()
