#Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random

chosen_word = random.choice(word_list)
print(chosen_word)  # this was for testing that it would pick a or b
guess = input("Guess a letter:\n").lower()
if guess in list(chosen_word):
    print ('a')
else:
    print('b')

