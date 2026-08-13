"""
CHALLENGE 7.3 — Grading Program v2
Topic: fix your own day-9 boundary bugs (Days 3, 9)

BUILDS ON
---------
Your day-9 task_1_grading_program.py — it has THREE real bugs.
2.1 BMI taught you the >= fix. Now apply it to your own old code.

THE BUGS IN YOUR DAY-9 VERSION (verify each one yourself first!)
----------------------------------------------------------------
1. Peter scored 0 — a valid (terrible) score — but your code says
   "Invalid Score". Why? Trace 0 through your conditions.
2. Two different brackets both award "Acceptable" (look at your
   70-81 and 0-71 branches). The lower one should be "Fail".
3. What happens to a score of exactly 100 vs 105? 105 slips into
   "Outstanding"... check: does it? Your first condition is
   90 < score < 101. So where does 105 land?

TASK
----
Rewrite with a function grade(score) that returns the grade:
    91-100: Outstanding | 81-90: Exceeds Expectations
    71-80:  Acceptable  | 0-70: Fail
    Anything below 0 or above 100: Invalid Score

RULES
-----
1. Check INVALID first (below 0 / above 100), then use descending
   >= checks — no "a < x < b" sandwiches, no gaps possible:
       if score >= 91: ...
       elif score >= 81: ...
2. Prove it: run grade() over this dict and print name -> grade:
   students = {'Harry': 88, 'Peter': 0, 'Ibti': 100, 'Last': 105,
               'Edge1': 91, 'Edge2': 90, 'Edge3': 71, 'Edge4': 70}
   Every Edge case lands exactly one bracket apart — if any two
   neighbours get the same grade, you still have a boundary bug.
"""

# --- write your code below this line ---
