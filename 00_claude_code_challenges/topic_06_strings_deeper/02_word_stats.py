"""
CHALLENGE 6.2 — Word Stats
Topic: split + loop + track-the-best (Days 5, 7)

BUILDS ON
---------
1.2 initials (.split()), 4.2 find_highest (track the champion) —
but the champion is now the LONGEST WORD, not the biggest number.

TASK
----
Write word_stats(sentence) that returns TWO things: the word count
and the longest word. Yes, a function can return two values:

    return count, longest        # caller: count, longest = word_stats(s)

That's new — play with it, it's very Python.

SAMPLE RUN
----------
Enter a sentence: the quick brown fox jumps over me
That's 7 words. Longest: 'jumps' (5 letters)

RULES
-----
1. No max(..., key=len) cleverness — track the longest with a loop
   (4.2 pattern: keep the best so far, replace when beaten).
2. Tie rule: if two words share the top length ('quick'/'brown'/
   'jumps' are all 5), which one does YOUR loop return — the first
   or the last? Run it, observe, and write the answer as a comment.
   (Knowing your code's tie behaviour = day-13 debugging mindset.)
3. Edge test before pushing: a one-word sentence, and a sentence
   with double spaces.
"""

# --- write your code below this line ---
