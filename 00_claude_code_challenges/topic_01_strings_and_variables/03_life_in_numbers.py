"""
CHALLENGE 1.3 — Life in Numbers
Topic: data types, int conversion, math operators (Day 2)

TASK
----
Ask for the user's age. Print how many DAYS, HOURS and MINUTES
that person has lived. Use 365 days per year (ignore leap years).

RULES
-----
1. The numbers must print as whole numbers — 10950, not 10950.0.
   Think about WHY you would get a .0 and which conversion fixes it.

SAMPLE RUN
----------
What is your current age? 30
You have lived for:
  10950 days
  262800 hours
  15768000 minutes
"""

# --- write your code below this line ---


user_age = int(input('What is your current age? '))

days_lived = user_age * 365
hours_lived = days_lived * 24
minutes_lived = hours_lived * 60

print(f'You have lived for:\n  {days_lived} days\n  {hours_lived} hours\n  {minutes_lived} minutes')
