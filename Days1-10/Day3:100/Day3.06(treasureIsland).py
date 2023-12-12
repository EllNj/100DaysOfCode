print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[EllNj]
*******************************************************************************''')
print("Welcome to treasure island.\nYour mission is to find the treasure.")
first = input("You have came across a split in the road: will you go left or right?(L or R) ").lower()
if first == "r":
    print("You were eaten alive by ravenous koalas.\nGame Over.")
    exit()
elif first == "l":
    second = input("You've arrived at a rough river: do you want to swim or wait it out?(S or W) ").lower()
    if second == "s":
        print("Ouch! Too many piranhas.\nGame Over.")
        exit()
    elif second == "w":
        third = input("\nAfter waiting the river calmed and you've now arrived inside the Palace:\nwhich door will you select?(1, 2 or 3) ")
        if third == "1" or third == "3":
            print("The numbers were not in your favour.\nGame Over.")
        elif third == "2":
            print("Congratulations you have found the treasure enjoy your eternal riches")
        else:
            print("Incorrect input")
            exit()
    else:
        print("Incorrect input")
        exit()
else:
    print("Incorrect input")
    exit()