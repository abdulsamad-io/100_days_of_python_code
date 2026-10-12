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


def is_leap_year(year):
    """Returns True if the given year is a leap year, False otherwise."""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


years_to_test = input("Enter years to test: ")

print(is_leap_year(int(years_to_test)))

""""
Then answer in a comment, in your own words:
    1. Why does "year % 4 == 0 and year % 100 != 0 or year % 400 == 0"
       work without any parentheses? (Which binds tighter, and or or?) - this works because the 'and' operator has a higher precedence than the 'or' operator. This means that the expression "year % 4 == 0 and year % 100 != 0" is evaluated first, and then the result is combined with "year % 400 == 0" using the 'or' operator.
    2. Would it still be correct with parentheses placed like this:
       "year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)"? - Yes, it would still be correct with the parentheses placed like that. The parentheses explicitly group the conditions for the 'or' operator, but since 'and' has higher precedence, the logic remains the same. Testing both versions with the years 1900, 2000, 2024, and 2025 confirms that they yield the same results: 1900 -> False, 2000 -> True, 2024 -> True, 2025 -> False.
       Test both with 1900, 2000, 2024, 2025 before you answer!
"""
