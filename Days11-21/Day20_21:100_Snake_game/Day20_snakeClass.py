from turtle import Turtle

STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.start_snake()
        self.head = self.segments[0]

    def start_snake(self):
        """Creates the start snake consisting of 3 squares in the centre of the scree"""
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        segment = Turtle(shape='square')
        segment.penup()
        segment.goto(x=position, y=0)
        segment.color('white')
        self.segments.append(segment)
    def grow(self):
        self.add_segment(self.segments[-1].xcor())
    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[i - 1].pos()
            self.segments[i].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
