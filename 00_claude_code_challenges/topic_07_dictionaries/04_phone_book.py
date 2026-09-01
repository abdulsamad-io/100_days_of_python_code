"""
CHALLENGE 7.4 — Phone Book
Topic: full CRUD on a dict (Days 9-10)

BUILDS ON
---------
Your day-9 secret auction (add entries in a loop) — extended to a
real menu with lookup and delete. This is the dress rehearsal for
Capstone B's bank menu.

TASK
----
A menu loop:
    1) add contact   2) look up   3) delete   4) list all   5) quit

All contacts live in ONE dict: name -> phone number (keep numbers
as STRINGS — why? What happens to '0612345678' as an int? Answer
in a comment).

SAMPLE RUN
----------
Choose (1-5): 1
Name: Sara
Number: 0612345678
Saved!
Choose (1-5): 2
Name: sara
Sara: 0612345678
Choose (1-5): 3
Name: Bob
No contact called 'Bob'.

RULES
-----
1. Look up and delete must handle missing names politely (no
   KeyError crash — membership check first, 7.2 rule).
2. Case-insensitive lookup: saving "Sara" then searching "sara"
   must work. Design hint: store keys in ONE consistent case
   (e.g. .title()) at ADD time — then lookups just normalise the
   same way. Fixing case at every lookup instead = pain.
3. Each menu action is its own function. The loop only routes.
   Delete: research the two ways (del d[k] vs d.pop(k)) — comment
   on the difference.
4. Adding a name that exists: warn before overwriting (y/n).
"""

# --- write your code below this line ---
