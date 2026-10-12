"""
CHALLENGE 2.3 — Triangle Classifier
Topic: validate first, then classify (Day 3)

BUILDS ON
---------
1.5 (reject bad input before using it) — now the validation rule
is mathematical, not just a length check.

TASK
----
Ask for three side lengths. First decide whether they can form a
triangle at all: every pair of sides added together must be
GREATER than the remaining side. If not valid, say so and stop.
If valid, classify:
    - equilateral: all three sides equal
    - isosceles:  exactly two sides equal
    - scalene:    all sides different

SAMPLE RUNS
-----------
Side a: 3
Side b: 4
Side c: 5
This is a valid scalene triangle.

Side a: 1
Side b: 2
Side c: 10
These sides cannot form a triangle.

RULES
-----
1. The validity check comes FIRST — classifying an impossible
   triangle is the bug.
2. Test with (1, 2, 3): the sum of two sides EQUALS the third.
   Valid or not? Look up the rule, decide, and leave a comment
   explaining your choice.
"""

# --- write your code below this line ---

# get side lengths from user
a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

def triangle_type(a, b, c):
   """Classifies the triangle based on side lengths."""
   if a == b == c:
      return "This is a valid equilateral triangle."
   elif a == b or b == c or a == c:
      return "This is a valid isosceles triangle."
   else:
      return "This is a valid scalene triangle."

# check if the sides can form a triangle
# The triangle inequality theorem states that the sum of the lengths of any two sides must be greater than the length of the remaining side.
if a + b > c and a + c > b and b + c > a:
   # classify the triangle
   result = triangle_type(a, b, c)
   print(result)
else:
   print("These sides cannot form a triangle.")



