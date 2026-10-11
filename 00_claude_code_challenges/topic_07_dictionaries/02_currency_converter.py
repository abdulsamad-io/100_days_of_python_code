"""
CHALLENGE 7.2 — Currency Converter
Topic: dict as a lookup table (Days 9-10)

BUILDS ON
---------
Your day-10 calculator's opr_dict — you mapped symbols to
FUNCTIONS there; here you map codes to NUMBERS. Same superpower:
data instead of if/elif chains.

TASK
----
RATES = {
    'USD': 1.09,
    'GBP': 0.86,
    'NGN': 1650.0,
    'JPY': 160.5,
}   # EUR -> currency

Ask which currency and how much EUR; convert(amount, currency)
returns the converted amount.

SAMPLE RUN
----------
Available: USD, GBP, NGN, JPY
Convert EUR to: ngn
Amount in EUR: 25
EUR 25.00 = NGN 41250.00

RULES
-----
1. NO if/elif per currency — the dict lookup does the work.
2. Accept lowercase input ('ngn') — normalise with .upper().
3. Unknown currency ('XYZ') must NOT crash. Check membership with
   'in' BEFORE looking up (1.5's validate-first rule).
4. Print the "Available:" line by getting the codes FROM the dict —
   don't hardcode the string. Research: what does ', '.join(RATES)
   give you? (Try it in the Python console first. Surprised?)
5. Both amounts formatted to 2 decimals (1.4 skill).
"""

# --- write your code below this line ---
