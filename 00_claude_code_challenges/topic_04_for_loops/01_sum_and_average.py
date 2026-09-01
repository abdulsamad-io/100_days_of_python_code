"""
CHALLENGE 4.1 — Sum and Average (no sum() allowed)
Topic: the accumulator pattern (Day 5)

BUILDS ON
---------
3.3 (comma-separated input into a list) — reuse it, but this time
the items must become NUMBERS, not stay strings.

TASK
----
Ask for numbers separated by commas. Print their total and average
WITHOUT using the built-in sum() (or statistics module).

SAMPLE RUN
----------
Enter numbers separated by commas: 10, 20, 30, 45
Total: 105.0
Average: 26.25

RULES
-----
1. The accumulator pattern: start a variable at 0 before the loop,
   add to it inside the loop. You already used this pattern in
   day-8's love calculator (check1_count) — recognise it!
2. "10" + "20" is "1020" in Python — if your total looks glued
   together instead of added, you forgot a conversion.
3. Average must show decimals when needed (26.25, not 26).
"""

# --- write your code below this line ---
