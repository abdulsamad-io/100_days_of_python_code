"""
CHALLENGE 8.1 — get_int(): Your First Reusable Tool
Topic: while loops + validation (Days 11-14)

BUILDS ON
---------
Every crash you've ever had from int(input(...)). Days 2, 5, 10,
12 all die if the user types "ten". Today that ends, repo-wide.

TASK
----
Write get_int(prompt) that keeps re-asking until the user types a
valid whole number, then returns it as an int:

    def get_int(prompt):
        # loop until input is all digits, then return int(...)

    age = get_int('How old are you? ')   # CANNOT crash

SAMPLE RUN
----------
How old are you? ten
That's not a whole number — try again.
How old are you? 3O          <- that's a letter O!
That's not a whole number — try again.
How old are you? 30
(returns 30)

RULES
-----
1. Use .isdigit() for the check (try '42'.isdigit() and
   '4x'.isdigit() in the console). try/except comes later in the
   course — this is the loop-based way.
2. One known limit: '-5'.isdigit() is False, so get_int can't
   accept negatives yet. Fine for now — document it in the
   docstring ("known limitation: non-negative only").
3. Bonus: get_int_in_range(prompt, low, high) that also re-asks
   until the number is between low and high. Built ON TOP of
   get_int — call it, don't copy it. (Function composition, 5.5!)
4. Demo at the bottom: use it to ask for age and dice sides.

FROM NOW ON
-----------
Every challenge and capstone that reads a number MUST use get_int.
Copy it into each new file for now — when the course teaches you
imports properly (day 16+), you'll import it instead. You already
import your own art files, so you know the mechanics.
"""

# --- write your code below this line ---
