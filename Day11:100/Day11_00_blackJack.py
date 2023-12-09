from Day11_art import logo
import random
############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def dealCard(UserList):
    UserList.append(cards[random.randint(0, 12)])

def calculateScore(UserList):
    score = sum(UserList)
    if score == 21:
        score = 0
    if score > 21 and 11 in UserList:
        UserList[UserList.index(11)] = 1
        score = sum(UserList)
    return score
def wentBust(score):
    return score > 21
def compareScore(user,comp):
    if user == 0 and comp != 0:
        print("You have BlackJack \nYou win!")
    elif comp == 0 and user != 0:
        print("The Dealer has BlackJack \nYou Lose!")
    elif user <= 21 and user > comp:
        print(f"You have {user} Dealer has {comp}\nYou win!")
    elif comp > user and comp <= 21:
        print(f"You have {user} Dealer has {comp}\nYou lose!")
    elif comp == user:
        print(f"You have {user} Dealer has {comp}\nIts a tie!")
def playAgain():
    again = input("Would You like to play again?(y or n)")
    if again == 'y':
        blackJack()
    else:
        exit()
def blackJack():
    compNum = []
    userNum = []
    dealCard(compNum)
    dealCard(compNum)
    dealCard(userNum)
    dealCard(userNum)
    print(f"The dealers card is {compNum[0]}")
    userHand = f"Your cards are: {userNum}"
    userScore = calculateScore(userNum)
    wentBust(userScore)
    print(userHand)
    hit = input("Would you like to hit?(y or n)")
    while hit == 'y' and userScore != 0:
        dealCard(userNum)
        userScore = calculateScore(userNum)
        if wentBust(userScore):
            print(f"Your cards are: {userNum}")
            print("You went Bust \nYou Lose!")
            playAgain()
        print(f"Your cards are: {userNum}")
        hit = input("Would you like to hit?(y or n)")
    if hit == 'n':
        while calculateScore(compNum) < 17 and calculateScore(compNum) != 0:
            print(f"The dealer has: {compNum} and must hit")
            dealCard(compNum)
        compScore = calculateScore(compNum)
        if wentBust(compScore):
            print(f"The Dealers cards are: {compNum}")
            print("Dealer went Bust \nYou Win!")
            playAgain()
        print(f"The Dealer has: {compNum}")
    compareScore(userScore,compScore)
    playAgain()
print(logo)
blackJack()