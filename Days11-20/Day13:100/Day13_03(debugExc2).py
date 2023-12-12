# Which year do you want to check?
year = int(input())     # error was the lack of an int() on this line so was being compared as a string

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
