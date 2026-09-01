"""
CHALLENGE 7.1 — Letter Frequency Counter
Topic: building a dict inside a loop (Day 9)

BUILDS ON
---------
4.1 accumulator — but now you need MANY counters at once, one per
letter. That's exactly what a dict is for. (Your day-12 guessing
game already built a dict in a loop — guess_list — you've done
this without realising!)

TASK
----
Write letter_frequency(text) that returns a dict of letter -> count.
Ignore spaces and punctuation; case-insensitive.

SAMPLE RUN
----------
Enter a sentence: hello world
{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

RULES
-----
1. The core dilemma: the first time you see 'l' the key does not
   exist yet — my_dict['l'] += 1 would CRASH. Solve it with an
   if/else: "if letter already in dict: +1, else: set to 1".
   (The 'in' keyword works on dicts — it checks keys.)
2. Skip non-letters. Research .isalpha() — one line in a comment
   about what it returns for 'a', '7' and ' '.
3. Bonus question in a comment: your day-9 auction looped over a
   dict with "for key in bid_table". What do you get per turn —
   the key, the value, or both? How would you get the value too?
   (Research: .items() — you used it on day 14 already!)
"""

# --- write your code below this line ---
