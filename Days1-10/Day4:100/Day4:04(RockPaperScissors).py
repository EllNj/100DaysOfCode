rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
num = int(input("Lets play Rock Paper Scissors!\nWhat do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
choice = [rock,paper,scissors]
cpuchoice = random.randint(0,2)
print(choice[num],'\n')
print("Computer chose:\n",choice[cpuchoice])

if num == 0:
    if cpuchoice == 1:
        print("Paper beats Rock\nYou lost, better luck next time")
    elif cpuchoice == 2:
        print("Rock beats Scissors\nYou won, in your face computer!")
if num == 1:
    if cpuchoice == 2:
        print("Scissors beats Paper\nYou lost, better luck next time")
    elif cpuchoice == 1:
        print("Paper beats Rock\nYou won, in your face computer!")
if num == 2:
    if cpuchoice == 0:
        print("Rock beats Scissors\nYou lost, better luck next time")
    elif cpuchoice == 1:
        print("Scissors beats Paper\nYou won, in your face computer!")