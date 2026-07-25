import random

choose_difficulty = input("Choose difficulty: ")

print ('Welcome to Number Guessing game')
print ("I'm thinking of a number between 1 - 100")

guess_number = input("Guess a number: ")

comp_number = random.randint(1, 100)

def choose_diff(difficulty):
    global choose_difficulty
    if difficulty == "easy":
        return 10
    elif difficulty == "medium":
        return 7
    if difficulty == "hard":
        return 5


no_of_lives = choose_diff(choose_difficulty)
#print (no_of_lives)

def check_num (number) :
    global guess_number
    if number == guess_number:
        return "correct"
    if number > guess_number:
        return "too low"
    if number < guess_number:
        return "too high"

while no_of_lives > 0:
    guess_number = input("Guess a number: ")
    check_num(comp_number)
    if check_num(comp_number) == "too low" or check_num(comp_number) == "too high":
        no_of_lives -= 1
        print (f"You have {no_of_lives} lives left")


