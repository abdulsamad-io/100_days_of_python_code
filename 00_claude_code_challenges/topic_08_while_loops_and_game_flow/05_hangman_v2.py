"""
CHALLENGE 8.5 — Hangman v2
Topic: debug and refactor your own day-7 game (Days 7, 13)

BUILDS ON
---------
Your day-7 hangman + the day-13 debugging discipline. This is a
BUG-FIX mission on real code: your own. Copy your day-7 main.py
content below the marker and fix it here (leave day 7's folder
untouched — it's history, and git remembers anyway).

THE 4 CONFIRMED ISSUES (from Claude's days 1-14 review)
-------------------------------------------------------
1. SPOILER: print(word) near the top reveals the answer. There
   are also debug prints of word_list and word_placeholder. Kill
   them all.
2. DEAD CODE: player_life, letter_range, hang_position and
   word_blank_list-vs-word_placeholder overlap — several variables
   are assigned but never (meaningfully) used. Delete every one
   your program doesn't need. (Proof it still runs after each
   deletion = day-13 technique: change ONE thing, re-test.)
3. REPEAT PENALTY: guessing the same WRONG letter twice deducts
   a life twice. Your day-12 guessing game already solved exactly
   this (the guess_list check + continue). Port that fix here:
   keep ONE list/set of all guessed letters; repeats of any kind
   cost nothing and print "already guessed".
4. FIRST IMPRESSION: the gallows art only appears after the first
   guess. Show stage art AND the blanked word BEFORE asking for
   the first letter.

RULES
-----
1. Fix all 4, then test these paths start-to-finish:
   win, lose, repeat-wrong-letter, repeat-right-letter.
2. Structure bonus (optional but recommended): pull the display
   logic into a function show_state(lives, blanked_word) — your
   day-14 refactor proves you can.
3. Commit message idea: "fix: hangman v2 - lives, repeats, spoiler,
   dead code" — a commit that says WHAT and WHY, like your recent
   ones.
"""

# --- write your code below this line ---
