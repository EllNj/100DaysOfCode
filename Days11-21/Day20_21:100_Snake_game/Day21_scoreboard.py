from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)