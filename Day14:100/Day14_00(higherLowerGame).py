import random
from Day14_gameData import data
import Day14_art


def compare_followers(a, b):
    if a['follower_count'] > b['follower_count']:
        return "A"
    else:
        return "B"


def show_options(a, b):
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(Day14_art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")


def create_options(a=None):
    if a is None:
        a = data[random.randint(0, len(data))]
    b = data[random.randint(0, len(data))]
    while b == a:
        b = data[random.randint(0, len(data))]
    return a, b


def game():
    print(Day14_art.logo)
    score = 0
    play = True
    optionA, optionB = create_options()
    while play:
        show_options(optionA, optionB)
        guess = input("Who has more followers? Type 'A' or 'B': ")
        if guess == compare_followers(optionA, optionB):
            score += 1
            print(f"Correct! Current score: {score}")
            optionA = optionB
            optionA, optionB = create_options(optionA)
            print("\n" * 20)
            print(Day14_art.logo)
        else:
            play = False
    print(f"Game Over! Final score: {score}")


game()
