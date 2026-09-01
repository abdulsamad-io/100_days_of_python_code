"""
CHALLENGE 6.5 — Caesar Cipher v2
Topic: upgrade your own day-8 cipher (Days 7-8)

BUILDS ON
---------
Your day-8 ceaser_cipher.py. Run it first with the message
"hello world" — watch it crash. Today you fix that.
Also: 6.1 taught you to pass some characters through untouched.

TASK
----
Rewrite caesar(text, shift, action) so that:
    1. Spaces, digits and punctuation pass through UNCHANGED
       (no crash on 'hello world!' or 'attack at 09:00').
    2. Uppercase letters stay uppercase after shifting:
       'Hello' -> 'Khoor', not 'khoor'.
    3. It still encrypts AND decrypts (decrypt = shift back).
    4. It RETURNS the result string (day-8 version printed).

SAMPLE RUN
----------
encrypt or decrypt? encrypt
Your message: Meet me at 10, Amsterdam!
Shift: 5
Result: Rjjy rj fy 10, Frxyjwifr!

HINTS
-----
- The crash: alphabet.index(' ') fails because ' ' is not in your
  alphabet list. So CHECK membership first: if the character is
  not a letter, append it as-is and move on (6.1 pattern).
- Uppercase: one approach — detect with .isupper(), work on the
  .lower() version, then .upper() the shifted letter before adding.
- Your day-8 version used THREE loops (indexes -> shifted indexes
  -> letters). One loop can do it all — transform each character
  completely before moving to the next (your fix commit on day 8
  was already heading this way).
- Keep the % 26 wrap-around — it was the best part of your v1. But
  test 'z' + shift 1 and 'Z' + shift 1 both.

FINAL CHECK
-----------
encrypt then decrypt the same message with the same shift — you
must get the original back EXACTLY, capitals and commas included.
(Round-trip testing, same as 5.1's temperature converter.)
"""

# --- write your code below this line ---
