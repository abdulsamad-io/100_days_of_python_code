"""
CHALLENGE 5.4 — Love Calculator v2
Topic: refactor print → return (Day 8 → Day 10 upgrade)

BUILDS ON
---------
Your day-8 task2.py — the love calculator that PRINTS its score.
This refactor is the exact fix from Claude's days 1-14 review.

TASK
----
Rewrite calculate_love_score(name1, name2) so that it:
    1. RETURNS an int (e.g. 47), never prints.
    2. Is case-insensitive: "TRUE"/"true", "Angela"/"angela"
       must give the same score. (Check: did your day-8 version
       handle 'T' in 'Angela' vs 't'? Test it!)

Scoring recap: count occurrences of the letters T,R,U,E in both
names combined -> first digit. Same for L,O,V,E -> second digit.
Combine: 4 and 7 -> 47.

SAMPLE RUN
----------
Enter name 1: Angela Yu
Enter name 2: Jack Bauer
Your love score is 53

RULES
-----
1. The combining step: your day-8 version glued two STRINGS
   together ('4' + '7' = '47'), which was fine for printing — but
   now you must return an INT. Two options: int('4' + '7'), or
   pure math: first * 10 + second. Use the math one and explain
   why it works in a comment.
2. Outside the function: if the score is > 50, print an extra
   "You match! 💘" line — the caller can make decisions like this
   precisely BECAUSE the function returns a number. That's the
   whole lesson.
"""

# --- write your code below this line ---
