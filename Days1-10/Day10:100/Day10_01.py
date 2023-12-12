from Day10_calcFunctions import add, subtract, divide, multiply, ops
from Day10_art import logo

def calculator():
    print(logo)
    num1 = float(input("What is your first number?: "))
    num2 = float(input("What is your second number?: "))

    for key in ops:
        print(key)
    op = input("Pick an operation: ")

    answer = ops[op](num1,num2)
    print(f"{num1} {op} {num2} = {answer}")
    repeat = input(f"Would you like to continue with {answer}? (y or n)")
    while repeat.lower() == 'y':
        num1 = answer
        op = input('Pick an operation: ')
        num2 = float(input("What is your next number? "))
        answer = ops[op](num1, num2)
        print(f"{num1} {op} {num2} = {answer}")
        repeat = input(f"Would you like to continue with {answer}? (y or n)")
    calculator()
calculator()