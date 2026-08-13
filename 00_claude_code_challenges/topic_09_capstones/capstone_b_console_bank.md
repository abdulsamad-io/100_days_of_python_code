# Capstone B — Console Bank (ATM Simulator)

A menu-driven banking app. Closest to your infra/ops world, and
the direct big sibling of 7.4 (phone book), 7.5 (inventory) and
8.2 (PIN check) — you have already built every piece of this.

## Core requirements

1. **Data model** — nested dict, at least 3 pre-made accounts:
   ```python
   accounts = {
       '1001': {'name': 'Sam', 'pin': '4321', 'balance': 250.0, 'history': []},
       ...
   }
   ```
   Account numbers and PINs are STRINGS (leading zeros — the 7.4
   phone number lesson).

2. **Login** (8.2 grown up): account number + PIN, max 3 attempts
   total, then "Card retained." and the program ends. `login(accounts)`
   returns the account number on success — the caller keeps it as
   "who is logged in".

3. **Menu loop** after login:
   `balance / deposit / withdraw / history / transfer / quit`

4. **The money rules**:
   - withdrawals may not exceed the balance (7.5's stock rule)
   - deposits and withdrawals must be positive numbers
   - every operation appends a description string to that
     account's `history` list, e.g. `"deposit +50.00 -> 300.00"`
   - balances always DISPLAY with 2 decimals (1.4)

5. **Never crashes.** All numeric input via `get_int` (8.1) or a
   money-variant of it you write. Unknown menu choices re-ask.
   This is the hard requirement — I will try to break it in review
   with inputs like `ten`, `-50`, `1e9`, an empty line, and a
   withdrawal of exactly the balance.

6. **Functions return, menu prints** — `deposit(accounts, acc_no,
   amount)` returns the new balance or a failure signal; it does
   not print. The menu layer turns results into messages. (Day 11
   blackjack's compare() is your model.)

## Stretch goals

- **Transfer** between two accounts: validate the target exists,
  both histories get an entry. What if someone transfers to
  themselves? Decide and handle it.
- **Daily withdrawal limit** (e.g. 500): track withdrawn-today per
  account, reset on... hmm, no clock available without new
  imports — so "per session" is fine. Document the simplification.
- **Money formatting** everywhere: `EUR 1,234.56` — research the
  `,` in format specs: `f'{x:,.2f}'`.

## Definition of done

- [ ] Wrong PIN x3 locks out; correct PIN on attempt 2-3 works
- [ ] Cannot overdraw, cannot deposit -50, cannot crash with 'ten'
- [ ] History shows a readable line per operation
- [ ] Transfer updates BOTH accounts (if attempted)
- [ ] No global keyword — accounts dict passed as parameter
- [ ] Pushed, and Claude review requested
