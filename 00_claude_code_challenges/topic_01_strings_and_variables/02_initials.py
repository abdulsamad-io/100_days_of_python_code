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
user_names = []

initials = ""

user_name = input('Give me your names, separated by a space: ').lower()

name_split = user_name.split()

for name in name_split:
    initials += name[0].upper() + "."

print (f'Your initials: {initials}')