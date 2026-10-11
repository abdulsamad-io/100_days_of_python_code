"""
CHALLENGE 3.1 — Dice Roller
Topic: random.randint, conditionals (Day 4)

BUILDS ON
---------
Topic 2 conditionals — the special-case checks are if/elif again.

TASK
----
Roll two six-sided dice. Print both rolls and the total.
Special messages:
    - both dice are 1        -> "Snake eyes!"
    - both dice equal (not 1) -> "Doubles!"
    - total is 7 or 11        -> "Lucky roll!"

SAMPLE RUNS
-----------
Die 1: 1  |  Die 2: 1  |  Total: 2
Snake eyes!

Die 1: 3  |  Die 2: 4  |  Total: 7
Lucky roll!

RULES
-----
1. Use random.randint (NOT random.choice on a list — know both tools).
2. Careful with order: double ones are ALSO doubles. Which check
   must come first so "Snake eyes!" wins?
"""

# --- write your code below this line ---
