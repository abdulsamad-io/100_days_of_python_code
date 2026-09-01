"""
CHALLENGE 8.2 — ATM PIN Check
Topic: attempt counters, loop exit conditions (Days 11-12)

BUILDS ON
---------
8.1 get_int (use it for the PIN entry!) and your day-12 guessing
game's lives counter — same pattern, security flavour.

TASK
----
CORRECT_PIN = '4321'  (a constant — and a STRING: PINs like 0042
lose their leading zero as ints; same lesson as 7.4's phone
numbers).

Give the user 3 attempts. Correct -> "Welcome!". Three failures ->
"Card retained. Contact your bank."

SAMPLE RUN
----------
Enter PIN (3 attempts left): 1111
Wrong PIN.
Enter PIN (2 attempts left): 4321
Welcome! 💳

RULES
-----
1. The prompt must show attempts REMAINING, counting down.
2. Exactly 3 attempts — not 2, not 4. Off-by-one check: wrong,
   wrong, wrong -> retained. Wrong, wrong, right -> welcome.
   Test both paths!
3. Structure it as a function verify_pin() that returns True or
   False; the welcome/retained printing happens outside (the
   caller decides — this is how Capstone B's login() will work).
4. Think in a comment: your hangman decremented lives, your
   guessing game decremented lives, this counts attempts — it's
   all the same counter pattern. Where does YOURS start and stop?
"""

# --- write your code below this line ---
