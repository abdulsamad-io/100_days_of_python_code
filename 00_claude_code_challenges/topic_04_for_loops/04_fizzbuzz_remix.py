"""
CHALLENGE 4.4 — FizzBuzz Remix
Topic: loops + conditionals combined (Day 5 + Day 13)

BUILDS ON
---------
Your day-13 fizzbuzz.py — but backwards and with new rules, so
copy-paste won't save you. 😄

TASK
----
Count DOWN from 50 to 1. For each number print:
    - "PingPong"  if divisible by both 4 and 7
    - "Ping"      if divisible by 4
    - "Pong"      if divisible by 7
    - the number  otherwise

SAMPLE OUTPUT (first lines)
---------------------------
50
49 -> no wait, 49 is 7x7... what should 49 print?
48 is divisible by 4...
(work it out — that's the exercise; 28 is the interesting one)

RULES
-----
1. range() can count backwards — figure out the three arguments.
   Check both ENDS of your output: does it start at 50 AND reach 1?
2. Same order lesson as your day-13 version: the "both" check must
   come first. In a comment, explain what would happen to 28 if you
   checked "divisible by 4" first.
3. Keep it a function fizz_buzz_remix(start) like day 13's.
"""

# --- write your code below this line ---
