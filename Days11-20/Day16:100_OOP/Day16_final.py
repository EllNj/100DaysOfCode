from Day16_menu import Menu, MenuItem
from Day16_coffeeMaker import CoffeeMaker
from Day16_moneyMachine import MoneyMachine


"""Had to turn this into a more object oriented program, mine was not too far off this before as 
I had split it into functions like this before"""


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

on = True
while on:
    drinks = menu.get_items()
    drink = input(f"What would you like? {drinks}: ")
    if drink == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink == "off":
        on = False
    else:
        drink = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
