import random
from players import players as original_players

def new_game():
    players = dict(original_players)
    char_1 = random.choice(list(players.items()))
    players.pop(char_1[0])
    return players, char_1

def play_round(players, char_1):
    char_2 = random.choice(list(players.items()))
    players.pop(char_2[0])

    if char_1[1] > char_2[1]:
        higher = char_1
    else:
        higher = char_2

    return char_2, higher

def compare_player_answer(answer, char_1, char_2, higher):
    if answer == "a":
        chosen = char_1
    else:
        chosen = char_2

    if chosen[0] == higher[0]:
        return True
    else:
        return False

keep_playing = True

while keep_playing:
    players, char_1 = new_game()
    char_2, higher = play_round(players, char_1)
    game_not_over = True
    score = 0

    while game_not_over:
        user_choice = input(f'Type a for {char_1[0]} or b for {char_2[0]}: ')
        is_correct = compare_player_answer(user_choice, char_1, char_2, higher)

        if is_correct == True:
            score = score + 1
            print("Correct!")
            char_1 = higher

            if len(players) == 0:
                print(f"You've guessed every player! Final score: {score}")
                game_not_over = False
            else:
                char_2, higher = play_round(players, char_1)
        else:
            print(f"Wrong! Game over! Final score: {score}")
            game_not_over = False

    continue_play = input("Do you want to play again? (y/n): ")
    if continue_play == "y":
        keep_playing = True
    else:
        keep_playing = False

print("bye")