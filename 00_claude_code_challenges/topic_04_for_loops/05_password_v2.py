"""
CHALLENGE 4.5 — Password Generator v2 (hard mode)
Topic: refactoring your own code (Day 5)

BUILDS ON
---------
Your day-5 password generator. Same behaviour, tighter code.

TASK
----
Rebuild the day-5 password generator with constraints:
    1. ONE loop total (your original had three).
    2. NO intermediate lists like letters_rand / numbers_rand —
       build a single list, shuffle it, join it.
    3. Use string.ascii_letters and string.digits instead of typing
       out the alphabet (import string — then print
       string.ascii_letters once to see what you get).
    4. No debug prints of the password list — only the final
       password is shown (your original printed the list twice).

SAMPLE RUN
----------
How many letters? 4
How many symbols? 2
How many numbers? 2
Your password is: p#K2x!9m

HINT
----
One loop can do three jobs: for each of the three categories you
know HOW MANY you need and WHICH pool to draw from. Two parallel
lists — pools and counts — or three small "for _ in range(n)"
blocks feeding ONE list both satisfy rule 1's spirit; the real
target is: no three copies of the same append logic.

COMPARE WHEN DONE
-----------------
Put day 5's version and this one side by side. Which is easier to
read? Honestly? Write your answer as a comment — sometimes the
"clever" version is NOT the better one, and knowing that is a
senior-engineer skill.
"""

# --- write your code below this line ---
