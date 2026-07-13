bid_table = {}

def user_bid():
    your_name = str(input('Please enter your name: '))
    your_bid = int(input('Please enter your bid: '))
    print(f'''
    Welcome, {your_name}!
    Your bid: {your_bid}''')
    bid_table[your_name] = your_bid

bidders_remaining = True
while bidders_remaining:
    user_bid()
    bidders_check = input('Are there other bidders left? Type "yes" or "no": ')
    if bidders_check == 'no':
        bidders_remaining = False
        print('Closing auction and computing winner')

highest_bid = 0

for key in bid_table:
    if bid_table[key] > highest_bid:
        highest_bid = bid_table[key]

for key in bid_table:
    if bid_table[key] == highest_bid:
        print(f'{key} with bid {bid_table[key]} is the winner!')

