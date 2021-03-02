from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from MoneyMachine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
on = True
money_machine.report()
coffee_maker.report()

while on:
    options = menu.get_items()
    user_option = input(f"What do you like? {options}: ")
    if user_option == "report":
        money_machine.report()
        coffee_maker.report()

    elif user_option == "off":
        on = False
    drink = menu.find_drink(user_option)
    sufficient = coffee_maker.is_resource_sufficient(drink)
    if sufficient:
        if money_machine.make_payment(drink.cost) and coffee_maker.make_coffee(drink):
            coffee_maker.make_coffee(drink)