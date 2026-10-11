"""
CHALLENGE 7.5 — Inventory System
Topic: dict values that change over time (Days 9-10)

BUILDS ON
---------
7.4 phone book (menu + CRUD), but values are now NUMBERS you do
math on — the bridge to Capstone B's account balances.

TASK
----
Start with:
    inventory = {'ssd': 12, 'ram': 30, 'cpu': 4, 'psu': 0}

Loop with commands: buy / sell / stock / quit
    buy  -> item + quantity, increases stock
    sell -> item + quantity, DECREASES stock, but never below 0:
            selling 10 cpus when you have 4 prints a warning and
            sells nothing (no partial sale)
    stock -> prints every item and quantity, one per line, plus a
             TOTAL count of all units (4.1 accumulator over
             dict values — research .values())

SAMPLE RUN
----------
Command (buy/sell/stock/quit): sell
Item: cpu
Quantity: 10
⚠ Only 4 cpu in stock — sale cancelled.
Command (buy/sell/stock/quit): buy
Item: gpu
Quantity: 2
gpu is new — added to inventory.

RULES
-----
1. Buying an item that doesn't exist yet ADDS it (like 7.1's
   "first time seeing this letter" logic — same pattern!).
2. Selling an item that doesn't exist = polite message, no crash.
3. Quantities must be positive whole numbers. Negative buy of -5
   would secretly be a sale — block it. (Validate first!)
4. Functions: buy(inventory, item, qty), sell(...), show_stock(...).
   Pass the dict IN as a parameter — no global keyword anywhere
   (day-12 scope lesson: your guessing game refactor already
   dropped a global; keep that habit).
"""

# --- write your code below this line ---
