"""
CHALLENGE 8.3 — Reverse Guessing Game
Topic: binary search, by hand (Days 12+14)

BUILDS ON
---------
Your day-12 guessing game — with the roles REVERSED. You think of
a number 1-100; the COMPUTER guesses it. This is the thinking
challenge of Topic 8.

TASK
----
The computer guesses; after each guess you answer:
    h = my number is Higher    l = my number is Lower    c = Correct

The computer must ALWAYS win within 7 guesses. Strategy: keep a
low and high boundary, always guess the MIDDLE, and shrink the
half that's ruled out. (This is binary search — one of the most
famous algorithms in computing, and you're about to write it
from scratch.)

SAMPLE RUN (user thought of 73)
-------------------------------
I guess 50. (h/l/c): h
I guess 75. (h/l/c): l
I guess 62... wait, is that right? Think! low is now 51, high 74.
I guess 67. (h/l/c): h
...
Got it in 6 guesses! 😎

RULES
-----
1. Track low and high; middle = (low + high) // 2.
2. After 'h': which boundary moves, and to WHAT? (guess + 1 or
   guess? Off-by-one alert — if you get it wrong the computer
   eventually guesses the same number twice. That's your test:
   it may NEVER repeat a guess.)
3. Count guesses; print the count at the end. Play 5 rounds with
   sneaky numbers (1, 100, 50, 51, 99) — all must finish in <= 7.
4. Cheater detection (bonus): if low ever passes high, the user's
   answers contradict each other. Print "You're cheating! 🕵️" and
   end. (Your day-14 game trusted input too — games shouldn't.)
5. In a comment: WHY is 7 always enough for 1-100? What about
   1-1000? (Hint: 2^7 = 128.)
"""

# --- write your code below this line ---
