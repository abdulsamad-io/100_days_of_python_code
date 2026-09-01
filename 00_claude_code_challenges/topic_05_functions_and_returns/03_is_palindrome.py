"""
CHALLENGE 5.3 — Palindrome Checker
Topic: functions returning booleans (Day 10)

BUILDS ON
---------
Your day-10 is_leap_year and day-12 is_prime — the is_something()
naming pattern for functions that return True/False.

TASK
----
Write is_palindrome(word) that returns True if the word reads the
same forwards and backwards, else False. Case must not matter:
"Level" is a palindrome.

SAMPLE RUNS
-----------
Enter a word: racecar
'racecar' is a palindrome! 🔁

Enter a word: python
'python' is not a palindrome.

RULES
-----
1. Returns True/False — the caller decides what to print. Note how
   your day-12 prime checker printed the raw True — here, turn the
   boolean into a friendly sentence outside the function.
2. Two ways to reverse: a for loop building a reversed string, or
   the slicing shortcut word[::-1]. Do it with the LOOP first (you
   are training loops), then add a comment showing the slice trick.
3. Test: "racecar", "Level", "python", and a single letter "x"
   (palindrome or not? decide and make sure your code agrees).
"""

# --- write your code below this line ---
