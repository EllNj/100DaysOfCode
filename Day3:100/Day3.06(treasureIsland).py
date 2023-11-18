print("Welcome to treasure island.\nYour mission is to find the treasure.")
first = input("You have came across a split in the road: will you go left or right?(L or R) ")
if first == "R":
    print("You were eaten alive by ravenous koalas.\nGame Over.")
    exit()
elif first == "L":
    second = input("You've arrived at a rough river: do you want to swim or wait it out?(S or W) ")
    if second == "S":
        print("Ouch! Too many piranhas.\nGame Over.")
        exit()
    elif second == "W":
        third = input("after waiting the river calmed and you've now arrived inside the Palace:\nwhich door will you select?(1, 2 or 3) ")
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