"""
CHALLENGE 6.3 — Word Reverser
Topic: two patterns combined (Days 5, 7)

BUILDS ON
---------
5.3 is_palindrome (reversing with a loop) + 6.2 (looping over the
words of a sentence). Combine them.

TASK
----
Write reverse_words(sentence) that reverses each word but keeps
the word ORDER:

SAMPLE RUN
----------
Enter a sentence: hello world
olleh dlrow

RULES
-----
1. Loop over words, reverse each (your 5.3 loop or [::-1] — your
   pick this time, you earned it), collect the reversed words,
   ' '.join() them at the end. You joined with '' in day 5's
   password — joining with ' ' is the same tool.
2. Fun test when done: feed it its own output. Do you get your
   original sentence back? Should you? One-line comment why.
"""

# --- write your code below this line ---
