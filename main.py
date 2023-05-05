import sys

profit = 0.0
resources = {
    'milk': 200,
    'water': 300,
    'coffee_beans': 100
}
MENU = {
    'latte': {
        'ingredients': {
            'milk': 100,
            'water': 100,
            'coffee_beans': 50,
        },
        'price': 0.8,
    },

    'capuccino': {
        'ingredients': {
            'milk': 150,
            'water': 100,
            'coffee_beans': 25,
        },
        'price': 0.95,
    },

    'espresso': {
        'ingredients': {
            'water': 100,
            'coffee_beans': 75,
        },
        'price': 0.5,
    }
}


def make_coffee(choice: str) -> str:
    global profit, resources

    for resource in resources:
        resources[resource] -= MENU[choice]['ingredients'][resource]

    profit += MENU[choice]['price']

    return choice


def check_resources(choice: str) -> bool:
    order_ingredients = MENU[choice]['ingredients']

    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f'Sorry there is not enough {item}.')
            return False

    return True


def check_money(choice: str) -> bool:
    print('Please insert coins.')

    quarters = int(input('how many quarters?: '))
    dime = int(input('how many dime?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))

    money_received = quarters * 1 + dime * 0.1 + nickles * 0.05 + pennies * 0.01

    if money_received < MENU[choice]['price']:
        print('Sorry that\'s not enough money. Money refunded.')
        return False
    else:
        change = round(money_received - MENU[choice]['price'], 2)
        print(f'Here is ${change} in change.')
    return True


def order(choice: str):
    if check_resources(choice) is False:
        return
    if check_money(choice) is False:
        return

    coffee = make_coffee(choice)

    print(f'Here is your {coffee} ☕️. Enjoy!')


def shut_down():
    sys.exit(0)


def report():
    print(f'''
        Water: {resources['water']}ml
        Milk: {resources['milk']}ml
        Coffee: {resources['coffee_beans']}g
        Money: ${profit}
    ''')


coffee_machine = {
    "off": shut_down,
    "report": report
}

while True:
    command = input('What would you like? (espresso/latte/cappuccino): ')

    if command in ('espresso', 'latte', 'capuccino'):
        order(command)
    else:
        coffee_machine[command]()
