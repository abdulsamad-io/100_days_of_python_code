"""
CHALLENGE 5.1 — Temperature Converter
Topic: pure functions that return (Day 10)

BUILDS ON
---------
Your day-10 calculator functions (add/sub/mul/div) — same shape,
real-world formulas.

TASK
----
Write two functions:
    celsius_to_fahrenheit(c)  ->  returns c * 9/5 + 32
    fahrenheit_to_celsius(f)  ->  returns (f - 32) * 5/9

Then a small menu: ask which direction, ask the value, print the
result to 1 decimal.

SAMPLE RUN
----------
Convert (1) C->F or (2) F->C? 1
Temperature: 37
37.0°C = 98.6°F

RULES
-----
1. NO print() inside the two conversion functions. They compute
   and return. Only the menu code prints.
2. The round-trip test — add this at the bottom as a comment with
   the result you observed:
       print(fahrenheit_to_celsius(celsius_to_fahrenheit(25)))
   Feeding one function's OUTPUT into the other's INPUT should give
   back exactly 25.0. This "output becomes input" chaining is why
   return beats print — try doing that with a function that only
   prints!
"""

# --- write your code below this line ---
