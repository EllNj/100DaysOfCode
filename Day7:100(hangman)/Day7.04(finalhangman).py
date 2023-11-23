# Step 4

import random
from Day7_hangman_art import *
from Day7_hangmanWordlist import word_list

# DO-1: - Update the word list to use the 'word_list' from hangman_words.py - done
# DO-2: - Import the stages from hangman_art.py and make this error go away. - done
chosen_word = random.choice(word_list)

lives = 6
# DO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = list('_' * len(chosen_word))

# DO-4: - If the user has entered a letter they've already guessed, print the letter and let them know. - done
# DO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word. - done
lives -= 1
used = []
while "_" in display:
    print(stages[lives])
    guess = input("Guess a letter: ").lower()
    if guess in used:
        print(f"You already used this letter: {guess}")
        continue
# Check guessed letter
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            display[index] = letter
    if guess not in display:
        lives -= 1
        used.append(guess)
        print(guess)
    if lives == 0:
        print(stages[lives])
        print(f"You Lost! Better look next time.\nThe word was {chosen_word}")
        exit()
    print(display)
print("You got the word! Well Done.")
