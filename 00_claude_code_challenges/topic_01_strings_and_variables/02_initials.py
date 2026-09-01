"""
CHALLENGE 1.2 — Initials Extractor
Topic: strings, .split(), indexing, loops (Days 1-2 + Day 5)

TASK
----
Ask for a full name and print the initials in uppercase,
each followed by a dot.

RULES
-----
1. Must work for ANY number of names (2, 3 or 4 words) —
   no hardcoding three parts.

SAMPLE RUNS
-----------
Enter your full name: abdul samad kazeem
Your initials: A.S.K.

Enter your full name: angela yu
Your initials: A.Y.

HINTS
-----
- .split() turns a sentence into a list of words
- word[0] gets the first letter of a word
- build the result string with += in a for loop,
  like you built word_placeholder in hangman

EDGE-CASE TEST (do this before pushing!)
----------------------------------------
Try the input "  abdul   samad  " (extra spaces everywhere).
If your code survives without crashing or printing weird dots,
you have done it properly.
"""

# --- write your code below this line ---
# characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-']

user_names = []

# enter_name = True

initials = ""

user_name = input('Give me your names, separated by a space: ').lower()

name_split = user_name.split()

for name in name_split:
    initials += name[0].upper() + "."

print (f'Your initials: {initials}')




# while enter_name:
#     user_name = input('Give me your name, one at a time: ').lower()

#     error_chars = []
#     for char in user_name:
#         if char not in characters:
#             error_chars.append(char)

#     if error_chars:
#         print(f'The following characters are invalid, please try again: {error_chars}')
#     else:
#         user_names.append(user_name)

#     continue_user_input = input('Do you want to continue with another name? (y/n): ').lower()
#     if continue_user_input == 'n':
#         enter_name = False

# print(user_names)

# initials = [name.split()[0][0].upper() for name in user_names]

