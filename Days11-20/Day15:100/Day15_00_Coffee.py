from Day15_data import *
from Day15_art import art

def payment(drink):
    price = MENU[drink]["cost"]
    print(f"The cost is {price}\nPlease insert coins")
    quarters = int(input("How many quarters?:")) * 0.25
    dimes = int(input("How many dimes?:")) * 0.10
    nickles = int(input("How many nickles?:")) * 0.05
    pennies = int(input("How many pennies?:")) * 0.01
    cash = quarters + dimes + nickles + pennies
    if cash < price:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        change = round(cash - price, 2)
        print(f"Here is ${change} in change")
        resources["money"] += price
        return True


def check_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def report():
    water, milk, coffee, money = resources["water"], resources["milk"], resources["coffee"], resources["money"]
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")


def make_drink(drink):
    """lowers the resources in accordance with the amount required for the drink, also prints drink statement"""
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink}, Enjoy")


def coffee_machine():
    on = True
    while on:
        print(art)
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink.lower() == "report":
            report()
        elif drink.lower() == "off":
            on = False
        else:
            if check_resources(drink):
                if payment(drink):
                    make_drink(drink)


coffee_machine()
