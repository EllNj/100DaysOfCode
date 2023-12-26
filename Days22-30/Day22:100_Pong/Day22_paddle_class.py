from turtle import Turtle

left = [-350,'W','S']
right = [350, 'Up', 'Down']

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.turtlesize(stretch_len=4, stretch_wid=0.8)
        self.penup()
        self.goto(position)
        self.setheading(270)
    def right_paddle(self):
        self.goto(x=350,y=-350)

    def pad_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def pad_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)