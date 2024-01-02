from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        with open("Snake_data.txt") as highscore_file:
            self.high_score = int(highscore_file.read())
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def reset_high(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Snake_data.txt",mode="w") as highscore_file:
                highscore_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()