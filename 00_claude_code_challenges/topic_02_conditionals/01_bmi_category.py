"""
CHALLENGE 2.1 — BMI Category
Topic: if/elif/else, comparison operators, boundaries (Day 3)

BUILDS ON
---------
Topic 1: f-strings for output, and the 1.1 habit — put the logic
in a function that RETURNS, print outside.

TASK
----
Ask for weight (kg) and height (m). Compute BMI = weight / height²
and print the category:

    under 18.5          -> underweight
    18.5 to under 25    -> normal weight
    25 to under 30      -> overweight
    30 and above        -> obese

RULES
-----
1. Write a function bmi_category(bmi) that RETURNS the category
   string. All printing happens outside the function.
2. Boundary check: a BMI of exactly 25 must be "overweight" and
   exactly 18.5 must be "normal weight". Remember the day-9 grading
   program bug (score 0 fell through the cracks) — use >= style so
   there are NO gaps.
3. Show the BMI rounded to 1 decimal in the output (you learned
   :.2f in challenge 1.4 — what would 1 decimal be?).

SAMPLE RUN
----------
Your weight in kg: 78
Your height in m: 1.76
Your BMI is 25.2 - you are overweight.
"""

# --- write your code below this line ---
