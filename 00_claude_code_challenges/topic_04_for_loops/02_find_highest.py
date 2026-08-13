"""
CHALLENGE 4.2 — Find the Highest (no max() allowed)
Topic: tracking "best so far" in a loop (Day 5)

BUILDS ON
---------
4.1 (accumulator — but now you track a champion, not a total).
Day 9 secret auction — you already wrote this logic once! This
time make it a reusable function.

TASK
----
Write find_highest(numbers) that returns the largest number from a
list without using max(). Then use it on comma-separated user input.

SAMPLE RUN
----------
Enter numbers separated by commas: 3, 99, 17, 42
The highest number is 99.0

RULES
-----
1. Must be a FUNCTION that takes a list and RETURNS the answer —
   your auction version was loose code wired to one dict; this one
   works for any list.
2. Trap from your auction code: you started highest_bid at 0.
   What happens if all numbers are NEGATIVE (-5, -2, -9)?
   Your function must return -2 there, not 0. Classic fix: start
   with the FIRST element instead of 0.
3. Bonus: also write find_lowest(numbers). Notice how similar it
   is — what exactly changed?
"""

# --- write your code below this line ---
