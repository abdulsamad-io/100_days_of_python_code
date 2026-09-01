"""
CHALLENGE 3.4 — Team Picker
Topic: random.shuffle, list slicing (Day 4)

BUILDS ON
---------
3.3 (comma-separated names into a clean list) — reuse that code!
1.5 (slicing strings) — slicing LISTS works exactly the same way.

TASK
----
Take comma-separated names and split them randomly into two fair
teams (sizes differ by at most 1 when the count is odd).

SAMPLE RUN
----------
Enter all names separated by commas: Abdul, Sara, Mike, Jen, Tom
Team A: ['Mike', 'Abdul', 'Jen']
Team B: ['Tom', 'Sara']

RULES
-----
1. random.shuffle first, then slice the list in two. You'll need
   the middle index — len() and the // operator (integer division,
   from day 2) get you there.
2. Run it twice with the same input: the teams must differ
   (that's the shuffle working).
3. Test with an ODD number of names — nobody may disappear!
   (Check: len(team_a) + len(team_b) == total names.)
"""

# --- write your code below this line ---
