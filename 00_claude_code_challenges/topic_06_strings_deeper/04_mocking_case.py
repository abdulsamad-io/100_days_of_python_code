"""
CHALLENGE 6.4 — mOcKiNg CaSe Converter
Topic: position-based logic in a loop (Days 5, 7)

BUILDS ON
---------
6.1 (build a new string, transform per character) — now the
transformation depends on the character's POSITION.

TASK
----
Write mocking_case(text) that alternates lower/UPPER across the
letters: even positions lowercase, odd positions uppercase.

SAMPLE RUN
----------
Enter a sentence: python is amazing
pYtHoN Is aMaZiNg

RULES
-----
1. You need each character's position, not just the character.
   Two options — pick one:
       a) for i in range(len(text)): ... text[i] ...
       b) research enumerate() — the Pythonic way. One sentence in
          a comment about what it gives you per loop turn.
2. Even/odd position: that's the % operator from odd_or_even
   (day 13). Same tool, new context.
3. Decide: does the SPACE consume a position (making 'i' in 'is'
   swap parity) or do you only count letters? Both are valid
   designs — pick one and state it in the docstring. (Real
   engineering: ambiguous spec, document your choice.)
"""

# --- write your code below this line ---
