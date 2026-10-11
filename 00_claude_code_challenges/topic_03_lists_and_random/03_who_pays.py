"""
CHALLENGE 3.3 — Who Pays the Bill?
Topic: split a string into a list, random.choice (Day 4)

BUILDS ON
---------
1.2 initials (.split() — but note the separator is different here!)

TASK
----
Ask for names separated by commas, pick one random person to pay.

SAMPLE RUN
----------
Enter all names separated by commas: Abdul, Sara, Mike, Jen
Mike is going to buy the meal today! 💸

RULES
-----
1. No loops allowed — random.choice does the work.
2. Watch the spaces: "Abdul, Sara".split(',') gives ' Sara' with a
   leading space. Find the fix (hint: .split() can take an argument
   like ', ' — OR look up .strip()). Test with and without spaces
   after the commas; both must print clean names.
"""

# --- write your code below this line ---
