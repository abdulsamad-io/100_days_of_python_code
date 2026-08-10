"""
CHALLENGE 1.5 — Username Generator
Topic: string slicing, len(), input validation (Days 1-3)

TASK
----
Build a username from the first 3 letters of the name plus the
birth year, all lowercase.

RULES
-----
1. REJECT names shorter than 3 characters with a friendly message
   instead of a username. The rejection must happen — this is your
   first taste of validating input BEFORE using it.

SAMPLE RUNS
-----------
Enter your name: Abdulsamad
Enter your birth year: 1990
Your username is: abd1990

Enter your name: Al
Enter your birth year: 1990
Sorry, your name must be at least 3 characters long.

HINTS
-----
- len() for the length check
- name[0:3] or name[:3] for slicing
- .lower() for lowercase
"""

# --- write your code below this line ---
