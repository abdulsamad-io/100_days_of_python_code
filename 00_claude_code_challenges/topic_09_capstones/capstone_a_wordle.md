# Capstone A — Terminal Wordle

A console clone of Wordle using only days 1-14 skills.

## Skills this exercises
Topic 3 (random.choice), Topic 4 (loops), Topic 5 (functions that
return), Topic 6 (per-character string work — this is Caesar v2's
big sibling), Topic 7 (stats dict), Topic 8 (game loop + validation).

## Core requirements

1. **Word list module** — `words.py` with `WORDS = [...]`, 30+
   five-letter words, all lowercase. Import it like you imported
   your art files since day 7. Pick the answer with `random.choice`.

2. **Six guesses.** Each guess must be validated before it counts:
   exactly 5 letters, alphabetic only (`.isalpha()`), re-ask on
   invalid input without losing a guess (8.4 pattern).

3. **Feedback per letter** after each guess — build a feedback
   STRING with the loop-and-append pattern (6.1):
   - `[A]` right letter, right position
   - `(A)` in the word, wrong position
   - ` a ` not in the word

   Example, answer `crane`, guess `cargo`:
   ```
   [C](A)(R) g  o
   ```

4. **History display**: every previous guess + its feedback is
   reprinted each round (store them in a list, loop to print).

5. **Win/lose messages** with ASCII art — your signature move.
   Lose message reveals the word.

6. **Play-again loop** with a session stats dict:
   `{'played': 0, 'won': 0, 'streak': 0}` — update after each game,
   show after each game. Streak resets on a loss (think: where
   exactly does that line go?).

## Stretch goals (optional, in order of difficulty)

- **Repeated letters done right.** Answer `ERASE`, guess `SPEED`:
  how many E-markers should the guess get? Real Wordle: an answer
  letter can only be "consumed" once — `SPEED`'s first E gets a
  marker, the second shows as absent. This needs two passes over
  the guess (exact matches first!) and a working copy of the
  answer's letters that you cross off as you consume them
  (day 11's `cards.remove(11)` — same tool). Genuinely hard;
  whiteboard it first.
- **Hard mode**: revealed letters must appear in later guesses.
- **Guess distribution** in stats: how many games won in 1,2,...6.

## Definition of done

- [ ] Invalid input can never crash it or steal a guess
- [ ] Feedback correct for: all-right, all-wrong, mixed, and (if
      stretch) `SPEED` vs `ERASE`
- [ ] Stats survive multiple games in one session
- [ ] No print() inside the logic functions (only the game loop prints)
- [ ] Pushed, and Claude review requested
