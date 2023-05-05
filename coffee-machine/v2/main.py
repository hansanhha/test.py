from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_open = True

MENU = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while is_open:
    command = input(f'What would you like? ({MENU.get_items()}) : ')

    if command == 'report':
        coffee_maker.report()
        money_machine.report()
    elif command == 'off':
        is_open = False
    else:
        choice = MENU.find_drink(command)
        if coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)


