import random

players = {
    "Cristiano Ronaldo": 677,
    "Lionel Messi": 514,
    "Neymar Jr": 242,
    "Kylian Mbappé": 136,
    "Erling Haaland": 75,
}

char_1 = random.choice(list(players.items()))
players.pop(char_1[0])

char_2 = ()
higher = ()

def play_game():
    global char_2
    global higher
    char_2 = random.choice(list(players.items()))
    players.pop(char_2[0])
    def compare_char(character_1, character_2):
        if character_1[1] > character_2[1]:
            return character_1
        else:
            return character_2
    higher = compare_char(char_1, char_2)

def compare_player_answer(answer):
    global game_not_over
    global char_1
    chosen = char_1 if answer == "a" else char_2
    if chosen[0] == higher[0]:
        char_1 = higher
        return "Correct"
    else:
        game_not_over = False
        return "Wrong"

play_game()
game_not_over = True
score = 0

while game_not_over:
    user_choice = input(f'Type a for {char_1[0]} or b for {char_2[0]}: ')
    result = compare_player_answer(user_choice)
    print(result)

    if result == "Correct":
        score += 1
        if not players:
            print(f"You've guessed every player! Final score: {score}")
            game_not_over = False
        else:
            play_game()  # only set up the next round if players are left
    else:
        print(f"Game over! Final score: {score}")