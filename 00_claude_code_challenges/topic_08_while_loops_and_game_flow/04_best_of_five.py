"""
CHALLENGE 8.4 — Rock Paper Scissors: Best of Five
Topic: refactor day 4 into a scored match (Days 4, 10, 12, 14)

BUILDS ON
---------
Your day-4 rock_paper_scissors.py — everything you now know
applied to your oldest game code. Compare the two files when done;
that diff IS your progress since day 4.

TASK
----
Best-of-five match: first to 3 round wins takes the match.
Draws replay the round (they don't count).

SAMPLE RUN
----------
Round score You 2 - 2 CPU | rock/paper/scissors: rock
CPU played scissors — you win the round!
🏆 MATCH OVER: You win 3 - 2!

RULES (each fixes a day-4 weakness)
-----------------------------------
1. play_round(user_move, cpu_move) returns 'win'/'lose'/'draw'.
   No printing inside. (Day 4 decided AND printed in one blob.)
2. Don't overwrite the move with ASCII art like day 4 did —
   user_move stays 'rock'; art is looked up separately when
   printing. A dict {'rock': rock_art, ...} beats the day-4
   if/elif chain (7.2 lookup-table lesson).
3. cpu picks with random.choice(['rock','paper','scissors']) —
   compare moves as STRINGS. Day 4 compared giant art strings —
   it worked, but explain in a comment why it was fragile.
4. Invalid input re-asks WITHOUT costing a round or advancing
   the game (day 4 just declared you the loser!). Loop until the
   move is valid — get_int's pattern, string edition.
5. Track both scores; first to 3 ends the match (day-14 outer
   loop pattern: match loop OUTSIDE, round loop INSIDE).
"""

# --- write your code below this line ---
