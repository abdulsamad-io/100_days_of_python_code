"""
CHALLENGE 5.5 — Days in a Month
Topic: functions calling functions (Day 10)

BUILDS ON
---------
2.4 (your one-line is_leap_year) — copy it into this file and
BUILD ON it. Functions composing functions is how real programs
grow.

TASK
----
Write days_in_month(year, month) that returns 28/29/30/31.
February must use is_leap_year(year) to decide 28 vs 29.

SAMPLE RUNS
-----------
Year: 2024
Month: 2
February 2024 has 29 days.

Year: 2025
Month: 2
February 2025 has 28 days.

RULES
-----
1. Store the days per month in a LIST:
   month_days = [31, 28, 31, 30, ...] and index into it — no
   12-branch if/elif chain! Careful: month 1 lives at index 0.
   (This list-as-lookup-table idea returns in Topic 7 with dicts.)
2. Reject nonsense: month 0, 13 or negative returns something the
   caller can recognise as invalid — decide what and document it
   in the docstring. (Peek at your day-11 blackjack: calculate_score
   returns 0 as a special "blackjack!" signal — same idea.)
3. Bonus: print the month NAME in the output like the samples.
   Another list gets you there.
"""

# --- write your code below this line ---
