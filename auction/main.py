import os
from art import logo

clear = lambda: os.system('clear')
bidding_finished = False
bids = {}

print(logo)
print('Welcome to the secret auction program.')

while not bidding_finished:
    name = input('What is your name?: ')
    price = input('What\'s your bid?: $')
    bids[name] = price

    should_continue = input('Are there any other bidders? Type \'yes\' or \'no\'. ')
    if should_continue == 'no':
        bidding_finished = True
    else:
        clear()

winner = max(bids)
print(f'The winner is {winner} with a bid of ${bids[winner]}')
