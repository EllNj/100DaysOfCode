# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# DO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = list('_' * len(chosen_word))


while "_" in display:
    print(stages[lives])
    guess = input("Guess a letter: ").lower()

# Check guessed letter
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            display[index] = letter
    if guess not in display:
        lives -= 1
    if lives == 0:
        print(stages[lives])
        print("You Lost! Better look next time.")
        exit()
    print(display)
print("You got the word! Well Done.")

# DO-2: - If guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop, and it should print "You lose."

# Check if user has got all letters.
# DO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives'
# the user has remaining.
