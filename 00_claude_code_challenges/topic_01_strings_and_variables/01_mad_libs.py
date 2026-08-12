"""
CHALLENGE 1.1 — Mad Libs Generator
Topic: variables, input(), f-strings (Days 1-2)

TASK
----
Ask the user for a noun, a verb, an adjective and a place.
Print a short funny story that uses all four words.

RULES
-----
1. The story must be built with ONE single f-string.
   (A triple-quoted f-string counts as one: f'''...''')
2. No '+' string concatenation anywhere in the file.

SAMPLE RUN
----------
Give me a noun: firewall
Give me a verb: dancing
Give me an adjective: sleepy
Give me a place: Amsterdam
------------------------------------
One day in Amsterdam, a sleepy firewall was caught dancing
in the data center...

(Your story can be anything you like, as long as all 4 words appear.)
"""

# --- write your code below this line ---


def user_story(noun, verb, adjective, place):
    """This functions returns a randomly made up story"""
    return f'In the beginning, the {noun} {verb} a {adjective} food in his {place} kitchen'

user_noun = input('Give me a noun: ')
user_verb = input('Give me a verb in past tense: ')
user_adjective = input('Give me a adjective: ')
user_place = input('Give me a place: ')

print(user_story(user_noun, user_verb, user_adjective, user_place))