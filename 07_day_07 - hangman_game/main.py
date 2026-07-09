import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words_dict = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")

word = random.choice(words_dict)
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

hang_position = stages [6]
while not game_over:
    user_guess = input('enter a guess word: \n')
    word_blank = ''
    if user_guess not in word:
        print ('Guess is INCORRECT!')
        lives -= 1
        if lives == 0:
            game_over = True
            print ('You lose')
    else:
        if user_guess in word:
            print('Guess is CORRECT!')
        for letter in word:
            if user_guess == letter:
                word_blank += letter
                word_blank_list.append(user_guess)
            elif letter in word_blank_list:
                word_blank += letter
            else:
                word_blank += '-'
        if '-' not in word_blank:
            game_over = True
            print ('You win')
        print(word_blank)
    print(stages[lives])

