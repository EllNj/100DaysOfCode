print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
names = name1 + name2
true = names.lower().count('t') + names.lower().count('r') + names.lower().count('u') + names.lower().count('e')
love = names.lower().count('l') + names.lower().count('o') + names.lower().count('v') + names.lower().count('e')
score = str(true) + str(love)
if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) > 40 and int(score) < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")