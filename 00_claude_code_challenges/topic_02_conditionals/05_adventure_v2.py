"""
CHALLENGE 2.5 — Adventure Game v2
Topic: nested conditionals at scale (Day 3)

BUILDS ON
---------
Your day-3 treasure hunt — this is the remake that fixes its bug.

TASK
----
Build a choose-your-own-adventure with:
    - at least 3 decision levels (choice inside choice inside choice)
    - at least 4 different endings (at least 1 win)
    - a story of your own (not the course's crossroad/river/doors)

RULES
-----
1. Fix the day-3 bug: your original used input(print('...')) which
   makes Python print "None" as the prompt. Use input('...') directly.
2. Accept choices in any case: "LEFT", "left" and "Left" all work
   (.lower() — you used this correctly on day 3 already).
3. Handle the "none of the offered choices" case at every level:
   typing something random must give a sensible ending, not fall
   into an else that pretends the user chose option B.

SAMPLE RUN (structure, not story)
---------------------------------
You wake up in a server room. Go LEFT or RIGHT? left
A door blocks you. Type the PASSCODE or FORCE it? force
The alarm goes off... GAME OVER.

CHECK BEFORE PUSHING
--------------------
Walk every path once and count your endings — do you really
have 4+? (Draw the decision tree on paper first. Seriously.)
"""

# --- write your code below this line ---
