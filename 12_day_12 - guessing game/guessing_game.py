import random

def play_game():
    guess_list = {}  # reset each game — no longer global
    print('Welcome to Number Guessing game')
    choose_difficulty = input("Choose difficulty: easy, medium, hard: ")

    def choose_diff(difficulty):
        if difficulty == "easy":
            return 10
        if difficulty == "medium":
            return 7
        if difficulty == "hard":
            return 5

    no_of_lives = choose_diff(choose_difficulty)
    print(f"You have {no_of_lives} lives total for {choose_difficulty.upper()} game level")
    comp_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 - 100")

    def check_num(number, guess):
        if guess == number:
            return "correct"
        elif guess < number:
            return "too low"
        else:
            return "too high"

    game_over = False
    while not game_over:
        guess_number = int(input("Guess a number: "))

        if guess_number in guess_list:
            print(f"Your guesses are ---> {guess_list}")
            print(f"You already guessed {guess_number} and it was {guess_list[guess_number]}. You still have {no_of_lives} lives left")
            continue  # skip the rest of the loop, don't deduct a life

        result = check_num(comp_number, guess_number)
        guess_list.update({guess_number: result})
        print(f"Your guesses are ---> {guess_list}")

        if result == "correct":
            print(f"{guess_number} is correct! You win!")
            game_over = True
        else:
            no_of_lives -= 1
            print(f"{guess_number} is {result}!")
            print(f"You have {no_of_lives} lives left")
            if no_of_lives == 0:
                print(f"Game over! The number was {comp_number}.")
                game_over = True

play_game()

continue_play = input("Do you want to play again? Type 'y' or 'n': ")
while continue_play == "y":
    play_game()
    continue_play = input("Do you want to play again? Type 'y' or 'n': ")