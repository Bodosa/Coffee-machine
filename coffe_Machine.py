""" Coffee Machine in OOP """
from menu16 import Menu
from coffe_maker16 import CoffeeMaker
from money_machine16 import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()


running = True

while running:
    options = menu.get_items()
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_running = False

    elif choice == "report":
        coffe_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)

