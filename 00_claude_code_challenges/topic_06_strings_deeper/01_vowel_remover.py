"""
CHALLENGE 6.1 — Vowel Remover
Topic: building a new string character by character (Day 7)

BUILDS ON
---------
5.2 count_vowels — same loop, but instead of COUNTING the vowels
you now KEEP the non-vowels. Notice how one pattern morphs into
another.

TASK
----
Write remove_vowels(text) that returns the text without vowels.

SAMPLE RUN
----------
Enter a sentence: programming is fun
prgrmmng s fn

RULES
-----
1. Build the result with the += pattern you used for
   word_placeholder in hangman (day 7).
2. Case-insensitive removal — "Programming" loses the 'o' AND
   would lose an 'A'. But the kept letters must keep their
   original case: "PRGRMMNG" stays uppercase. (So where must the
   .lower() go — on the letter you TEST, or the letter you KEEP?)
3. Spaces and punctuation survive untouched — free hint for 6.5,
   where this "pass some characters through" idea is the entire
   challenge.
"""

# --- write your code below this line ---
