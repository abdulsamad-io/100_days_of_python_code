import random
import hangman_stages
from hangman_acsii import hangman_ascii
import hangman_word

print(hangman_ascii)

word = random.choice(hangman_word.words_dict)
print (word)

word_list = list (word)
print (word_list)

player_life = len(word)

word_placeholder = ''
for i in range (0,len(word)):
    word_placeholder += '-'
print (word_placeholder)

lives = 6
game_over = False
letter_range = 0

word_blank_list = []

hang_position = hangman_stages.stages [6]
while not game_over:
    user_guess = input('enter a guess word: \n').lower()
    word_blank = ''
    display = ""
    if user_guess not in word:
        print ('Guess is INCORRECT!')
        lives -= 1
        print (f'******* YOU HAVE {lives} LIVES LEFT*******')
        if lives == 0:
            game_over = True
            print ('You lose')
            print ('The right word was : ', word)
    else:
        if user_guess in word:
            print('Guess is CORRECT!')
        if user_guess in word_blank_list:
            print(f"You've already guessed {user_guess}")
        for letter in word:
            if user_guess == letter:
                word_blank += letter
                word_blank_list.append(user_guess)
            elif letter in word_blank_list:
                word_blank += letter
            elif letter in word_blank:
               print('you already guessed this word')
            else:
                word_blank += '-'
        print(f'******* YOU HAVE {lives} LIVES LEFT*******')
        if '-' not in word_blank:
            game_over = True
            print ('You win')
        print(word_blank)
    print(hangman_stages.stages[lives])
