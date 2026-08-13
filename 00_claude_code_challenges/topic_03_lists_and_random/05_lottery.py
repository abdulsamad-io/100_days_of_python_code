"""
CHALLENGE 3.5 — Lottery Numbers
Topic: research task — random.sample (Day 4+)

BUILDS ON
---------
1.4 receipt (researching something new on your own — that's the
real skill this challenge trains).

TASK
----
Generate 6 UNIQUE lottery numbers between 1 and 49, print them
sorted from low to high.

SAMPLE RUN
----------
Your lucky numbers: 3, 17, 22, 31, 40, 49

RULES
-----
1. "Unique" is the trap: random.randint six times can repeat.
   The clean tool is random.sample — read its documentation
   yourself (python docs or help(random.sample) in the Python
   console). That's the challenge.
2. Sort before printing (look up: sorted() or .sort() — and leave
   a comment on the difference between the two, in your own words).
3. Print them comma-separated WITHOUT the square brackets.
   Hint: you joined a list of characters into a string in day 5's
   password generator... but ','.join() only works on strings —
   what are your numbers? One more small research task.
"""

# --- write your code below this line ---
