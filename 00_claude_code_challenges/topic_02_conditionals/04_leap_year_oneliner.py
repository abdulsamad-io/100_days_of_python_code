"""
CHALLENGE 2.4 — Leap Year, One Line
Topic: and/or logic, operator precedence (Day 3 + Day 10)

BUILDS ON
---------
Your own repo! You already wrote this two ways:
    - day 13: nested if version (leap_year_checker.py)
    - day 10: compact version (leap_year_calculator.py)

TASK
----
Write is_leap_year(year) whose body is a SINGLE return statement
using and/or — no if at all:

    return <one boolean expression>

Then answer in a comment, in your own words:
    1. Why does "year % 4 == 0 and year % 100 != 0 or year % 400 == 0"
       work without any parentheses? (Which binds tighter, and or or?)
    2. Would it still be correct with parentheses placed like this:
       "year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)"?
       Test both with 1900, 2000, 2024, 2025 before you answer!

RULES
-----
1. Verify all four test years and put the expected results in a
   comment: 1900 -> False, 2000 -> True, 2024 -> True, 2025 -> False.
2. No if/else anywhere in the function.
"""

# --- write your code below this line ---
