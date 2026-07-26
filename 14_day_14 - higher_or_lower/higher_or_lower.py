import random

players = {
    "Cristiano Ronaldo": 677,
    "Lionel Messi": 514,
    "Neymar Jr": 242,
    "Kylian Mbappé": 136,
    "Erling Haaland": 75,
}

char_1 = random.choice(list(players.items()))
print(f'char_1 is {char_1}')
print(f'to remove {char_1[0]}')
#print(players)

players.pop(char_1[0])  # removes the key in-place, don't reassign players to the result
#print(players)

char_2 = random.choice(list(players.items()))
print(f'char_2 is {char_2}')

a = 0
b = 0

def compare_char (character_1 , character_2):
    global a,b
    character_1[1] = a
    character_1[1] = b