import random
from Day12_art import logo


def guess_number_game():
    print("I'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if diff.lower() == 'hard':
        count = 5
    elif diff.lower() == 'easy':
        count = 10
    while count > 0:
        gos = 0
        print(f"You have {count} attempts remaining")
        if gos == 0:
            guess = int(input("Make a guess:\n"))
            gos += 1
        else:
            guess = int(input("Guess again:\n"))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            play_again()
            exit()
        elif guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")
        count -= 1
    print(f"The answer was {answer}, better luck next time.")
    play_again()
    exit()


def play_again():
    """Asks if the user wants to play again if y its runs the game again else it exits"""
    if input("Play again?(y or n)") == 'y':
        guess_number_game()


intro = "Welcome to the Number Guessing Game!"

print(logo)
print(intro)
guess_number_game()
