"""
CHALLENGE 2.2 — Movie Ticket Pricing
Topic: nested if, combining conditions (Day 3)

BUILDS ON
---------
2.1 (if/elif chains) — now the conditions NEST.
Topic 1: format the final price with exactly 2 decimals (1.4 skill).

TASK
----
Ticket pricing rules:
    - child  (age < 12):        EUR 8
    - teen   (12 to 17):        EUR 10
    - adult  (18 to 64):        EUR 14
    - senior (65+):             EUR 9
    - Students get 20% off, but ONLY if they are adults (18-64).
      A 16-year-old student still pays the teen price.

Ask for age, then ask "Are you a student? (y/n)" ONLY when it
could matter. Print the final price with 2 decimals.

SAMPLE RUNS
-----------
How old are you? 25
Are you a student? (y/n): y
Your ticket costs EUR 11.20

How old are you? 16
Your ticket costs EUR 10.00

RULES
-----
1. The student question must NOT appear for children, teens
   or seniors (that's the nesting).
2. Return the price from a function; print outside.
"""

# --- write your code below this line ---
