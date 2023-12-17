import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)  # this is based on pixels
# creating a pop up
user_bet = screen.textinput(title="Make your bet", prompt="Which Teenage Mutant Ninja Turtle will win the race?"
                                                          " Enter a colour(blue, purple, orange, red):")

tmnt_names = ["Leonardo", "Donatello", "Michelangelo", "Raphael"]
y_coords = [150, 50, -50, -150]
colours = ['blue', 'purple', 'orange', 'red']
racers = []
for i in range(len(tmnt_names)):
    name = tmnt_names[i]
    name = Turtle(shape='turtle')
    name.penup()
    name.goto(x=-225, y=y_coords[i])
    name.color(colours[i])
    racers.append(name)
if user_bet:
    race_on = True

while race_on:
    for racer in racers:
        if racer.xcor() > 230:
            winner = racer.pencolor()
            if winner == user_bet:
                print(f'I guess luck was on your side.\nThe winning Turtle was {winner}, {tmnt_names[colours.index(winner)]}.')
            else:
                print(f"Who would have guessed that you'd lose\nThe winning Turtle was {winner}, {tmnt_names[colours.index(winner)]}.")
            race_on = False

        distance = random.randint(0,10)
        racer.forward(distance)




screen.exitonclick()
