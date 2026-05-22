# Think & Guess — Homework

## What You'll Build

A Mastermind-style number guessing game. The computer picks a secret 4-digit number with no repeats. You guess — it tells you how many digits are correct (green), misplaced (yellow), or wrong (red). Figure it out before you run out of attempts.

You'll create **3 Python files**. `Menu` is fully provided (copy-paste). The other two — `Game` and `MasterMind` — you'll build **method by method**, testing each one before moving on.

---

## Think Aloud – What Do We Need?

Before you write any code, think about the problem:

1. **Generate a secret** — 4 unique digits, random order. We'll use a list + while loop.
2. **Compare a guess** — count greens (right digit, right position), yellows (right digit, wrong position), reds (not in secret at all).
3. **Track the game** — how many attempts remain? Did the player win?
4. **Get player input** — validate: exactly 4 digits, all digits, no repeats.
5. **Show feedback** — coloured counts so the player can refine their next guess.
6. **Win / lose** — stop when they guess correctly or run out of attempts.

---

## Files You Need

| File | What to do |
|------|------------|
| `game.py` | **Build yourself** — pure logic, no colours |
| `mastermind.py` | **Build yourself** — presentation layer with colours |
| `menu.py` | **Copy-paste** — fully provided |

---

## Class Architecture

```
+---------------------------+          +-------------------------------+
|          Game             |          |          MasterMind           |
+---------------------------+          +-------------------------------+
| - max_attempts            |          | - max_attempts                |
| - secret: str             |          | - game: Game                  |
| - remaining_attempts: int |          +-------------------------------+
| - won: bool               |          | + _print_header(text)         |
+---------------------------+          | + _print_result(g, y, r)     |
| + _generate_secret()      |          | + _print_win(secret)          |
| + compare_guess(guess)    |          | + _print_lose(secret)         |
+---------------------------+          | + start()                     |
                                       | + play()                      |
                                       +-------------------------------+
```

```
+-------------------------------+
|            Menu               |
+-------------------------------+   <-- FULLY PROVIDED
| - max_attempts                |
| - mastermind: MasterMind      |
+-------------------------------+
| + start_new_game()            |
| + set_max_attempts()          |
| + run()                       |
+-------------------------------+
```

### Class Responsibilities

| Class | Status | Responsibility |
|-------|--------|---------------|
| `Game` | **You implement** | Pure logic — secret generation, guess comparison. No colours, no I/O. |
| `MasterMind` | **You implement** | Presentation — coloured output, game loop, input validation. Wraps Game. |
| `Menu` | Copy-paste | Interactive menu — start games, change max attempts, exit. |

---

## 1. Menu — Copy This

Create `menu.py` and paste this exactly:

```python
from colorama import init, Fore, Style
from mastermind import MasterMind

init(autoreset=True)


class Menu:
    """Colourful interactive menu for the Think & Guess game."""

    def __init__(self):
        self.max_attempts = 10
        self.mastermind = None

    def _print_header(self, text: str):
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)
        print(Fore.YELLOW + Style.BRIGHT + text.center(50))
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)

    def _print_success(self, msg: str):
        print(Fore.GREEN + f"\u2713 {msg}")

    def _print_error(self, msg: str):
        print(Fore.RED + f"\u2717 {msg}")

    def _print_info(self, msg: str):
        print(Fore.BLUE + f"\u2139 {msg}")

    def start_new_game(self):
        self.mastermind = MasterMind(max_attempts=self.max_attempts)
        self.mastermind.start()
        self._print_info("Game finished. Returning to menu...")

    def set_max_attempts(self):
        try:
            new_val = int(input(
                Fore.YELLOW + f"New max attempts (current = {self.max_attempts}): "
                + Style.RESET_ALL
            ).strip())
            if new_val < 1:
                self._print_error("Attempts must be >= 1")
            else:
                self.max_attempts = new_val
                self._print_success(f"Max attempts set to {self.max_attempts}")
        except ValueError:
            self._print_error("Please enter a valid integer.")

    def run(self):
        while True:
            self._print_header("\U0001f9e0 THINK & GUESS \U0001f9e0")
            print(Fore.MAGENTA + Style.BRIGHT + "1." + Fore.GREEN + " Start new game")
            print(Fore.MAGENTA + Style.BRIGHT + "2." + Fore.GREEN +
                  f" Set max attempts (current = {self.max_attempts})")
            print(Fore.RED + Style.BRIGHT + "0." + Fore.RED + " Exit")

            choice = input(Fore.CYAN + "\nYour choice: " + Style.RESET_ALL).strip()

            if choice == "1":
                self.start_new_game()
            elif choice == "2":
                self.set_max_attempts()
            elif choice == "0":
                self._print_info("Thanks for playing! Goodbye.")
                break
            else:
                self._print_error("Invalid choice. Enter 1, 2 or 0.")


if __name__ == "__main__":
    menu = Menu()
    menu.run()
```

Don't run it yet — `MasterMind` doesn't exist.

---

## 2. Build Game — Method by Method

Open `game.py`. Start with an empty file.

### 2a. `__init__`

**What we need**

A Game stores:

```
┌─────────────────────┬──────────┬──────────────────────────────────┐
│ Attribute           │ Type     │ What it's for                    │
├─────────────────────┼──────────┼──────────────────────────────────┤
│ max_attempts        │ int      │ How many guesses allowed         │
│ secret              │ str      │ The 4-digit target (generated)   │
│ remaining_attempts  │ int      │ Guesses left (starts = max)      │
│ won                 │ bool     │ Did the player guess correctly?  │
└─────────────────────┴──────────┴──────────────────────────────────┘
```

**Write the code**

```python
import random


class Game:
    """Pure business logic — no colours, no output formatting."""

    def __init__(self, max_attempts: int = 10):
        self.max_attempts = max_attempts
        self.secret = self._generate_secret()
        self.remaining_attempts = max_attempts
        self.won = False
```

We call `_generate_secret()` in `__init__`, so we need to write that next. For now, make it a placeholder so the code runs:

```python
    def _generate_secret(self) -> str:
        return "0000"  # temporary — we'll fix this next
```

**Test it**

Add this at the bottom:

```python
if __name__ == "__main__":
    print("=== Test __init__ ===")
    g = Game()
    print(f"Secret: {g.secret}")             # 0000 (temp)
    print(f"Max attempts: {g.max_attempts}") # 10
    print(f"Remaining: {g.remaining_attempts}") # 10
    print(f"Won: {g.won}")                   # False
```

Run `python game.py`:
```
=== Test __init__ ===
Secret: 0000
Max attempts: 10
Remaining: 10
Won: False
```

---

### 2b. `_generate_secret`

**What we need**

Build a 4-digit string with no repeated digits:

```
                    while len(digits) < 4
                           │
                           ▼
                    ┌──────────────┐
                    │ pick random  │
                    │ digit 0-9    │
                    └──────┬───────┘
                           │
                    ┌──────▼──────┐
               No   │ digit in    │
         ┌─────────│ digits[]?   │
         │         └─────────────┘
         │               │ Yes
         │               ▼
         │          (skip it)
         │
         ▼
  ┌────────────┐
  │ append to  │
  │ digits[]   │
  └────────────┘
         │
         ▼
  (back to top until len=4)

  Then: ''.join(str(d) for d in digits)
```

**Write the code** (replace the temporary version):

```python
    def _generate_secret(self) -> str:
        digits = []
        while len(digits) < 4:
            d = random.randint(0, 9)
            if d not in digits:
                digits.append(d)
        return ''.join(str(d) for d in digits)
```

**Test it**

Update the test block:

```python
if __name__ == "__main__":
    print("=== Test _generate_secret ===")
    g = Game()
    print(f"Secret: {g.secret}")                # 4 unique digits
    print(f"Length: {len(g.secret)}")            # 4
    print(f"Unique: {len(set(g.secret)) == 4}")  # True
    print(f"Is digits: {g.secret.isdigit()}")    # True
    print(f"\nSecrets across 5 games:")
    for i in range(5):
        print(f"  Game {i+1}: {Game().secret}")
```

Run it. Every secret should be exactly 4 unique digits.

---

### 2c. `compare_guess`

**What we need**

Compare a guess against the secret and count:

- **Green** → same digit, same position (`guess[i] == secret[i]`)
- **Yellow** → same digit, different position (in guess_remaining AND secret_remaining, cross-checked with removal)
- **Red** → everything else

Algorithm step by step:

```
1. Count green:
   for i in 0..3:
       if guess[i] == secret[i] → green++

2. Build remaining lists (where guess[i] != secret[i]):
   secret_remaining = [secret[i] for i where guess[i] != secret[i]]
   guess_remaining  = [guess[i]  for i where guess[i] != secret[i]]

3. Count yellow:
   for each g in guess_remaining:
       if g in secret_remaining:
           yellow++
           remove g from secret_remaining

4. red = 4 - green - yellow
```

**Write the code**

```python
    def compare_guess(self, guess: str):
        green = sum(1 for i in range(4) if guess[i] == self.secret[i])

        secret_remaining = []
        guess_remaining = []
        for i in range(4):
            if guess[i] != self.secret[i]:
                secret_remaining.append(self.secret[i])
                guess_remaining.append(guess[i])

        yellow = 0
        for g in guess_remaining:
            if g in secret_remaining:
                yellow += 1
                secret_remaining.remove(g)

        red = 4 - green - yellow
        return (green, yellow, red)
```

**Test it**

```python
if __name__ == "__main__":
    # --- _generate_secret ---
    print("=== Test _generate_secret ===")
    g = Game()
    print(f"Secret: {g.secret}")
    print(f"Length: {len(g.secret)}")
    print(f"Unique: {len(set(g.secret)) == 4}")
    print(f"Is digits: {g.secret.isdigit()}")

    # --- compare_guess ---
    print("\n=== Test compare_guess ===")
    # Force a known secret for testing
    g.secret = "1589"
    print(f"Secret = {g.secret}")
    tests = [
        ("1589", (4, 0, 0)),  # exact match
        ("1234", (1, 0, 3)),  # only 1 at pos 0 matches
        ("8519", (0, 4, 0)),  # all correct, all misplaced
        ("2571", (0, 2, 2)),  # 5 and 1 exist but misplaced
        ("7777", (0, 0, 4)),  # nothing matches
    ]
    for guess, expected in tests:
        result = g.compare_guess(guess)
        status = "✓" if result == expected else "✗"
        print(f"  {status} {guess} -> {result} (expected {expected})")
```

Run it. Every test should show `✓`.

---

## 3. Build MasterMind — Method by Method

Open `mastermind.py`. Start empty.

### 3a. `__init__`

**What we need**

Just store `max_attempts` and set `self.game = None` (the Game is created when `start()` is called).

```python
from colorama import init, Fore, Style
from game import Game

init(autoreset=True)


class MasterMind:
    """Presentation layer — colourful game output with colorama."""

    def __init__(self, max_attempts: int = 10):
        self.max_attempts = max_attempts
        self.game = None
```

No test yet — nothing to verify.

---

### 3b. `_print_header`

**What we need**

A coloured banner:

```
==================================================
              THINK & GUESS
==================================================
```

**Write the code**

```python
    def _print_header(self, text: str):
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)
        print(Fore.YELLOW + Style.BRIGHT + text.center(50))
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)
```

**Test it**

```python
if __name__ == "__main__":
    m = MasterMind()
    m._print_header("THINK & GUESS")
    print("Does it look right? (y/n) ", end="")
    input()
```

Run it. You should see the banner. Type y and press Enter to pass.

---

### 3c. `_print_result`

**What we need**

Show aggregated counts with coloured emojis:

```
🟢-> 1 / 🟡-> 1 / 🔴-> 2
```

Each segment in its colour: green emoji, yellow emoji, red emoji.

**Write the code**

```python
    def _print_result(self, green: int, yellow: int, red: int):
        parts = [
            Fore.GREEN + f"\U0001f7e2-> {green}",
            Fore.YELLOW + f" / \U0001f7e1-> {yellow}",
            Fore.RED + f" / \U0001f534-> {red}"
        ]
        print("".join(parts))
```

**Test it**

```python
if __name__ == "__main__":
    m = MasterMind()
    m._print_header("TEST: _print_result")
    print("Expected:  🟢-> 1 / 🟡-> 1 / 🔴-> 2")
    m._print_result(1, 1, 2)
    print("\nExpected:  🟢-> 4 / 🟡-> 0 / 🔴-> 0")
    m._print_result(4, 0, 0)
```

Run it and compare visually.

---

### 3d. `_print_win` and `_print_lose`

**What we need**

Win: bright green celebration with the secret. Lose: bright red game-over with the secret.

**Write the code**

```python
    def _print_win(self, secret: str):
        print(Fore.GREEN + Style.BRIGHT + f"\n\U0001f389 YOU WON! The secret was {secret}.")

    def _print_lose(self, secret: str):
        print(Fore.RED + Style.BRIGHT + f"\n\U0001f480 GAME OVER! The secret was {secret}.")
```

**Test them**

```python
if __name__ == "__main__":
    m = MasterMind()
    m._print_header("TEST: win/lose")
    m._print_win("1589")
    m._print_lose("1589")
```

Run it. Win should be green, lose should be red.

---

### 3e. `start`

**What we need**

Create a `Game` instance and call `play()`.

```python
    def start(self):
        """Create a Game instance and start the game loop."""
        self.game = Game(max_attempts=self.max_attempts)
        self.play()
```

---

### 3f. `play` — The Game Loop

**What we need**

The full game loop:

```
1. Print header "THINK & GUESS"
2. Print "Max attempts: N"
3. Print "Secret is a 4-digit number with no repeated digits."

4. Loop while remaining_attempts > 0 and not won:
   │
   ├── Print "Attempts left: N"
   ├── Prompt "Your guess: "
   │
   ├── Validate:
   │   ├── len(guess) == 4?
   │   ├── guess.isdigit()?
   │   └── len(set(guess)) == 4?
   │   └── If any fail → print error, continue
   │
   ├── Call game.compare_guess(guess) → (g, y, r)
   │
   ├── If g == 4:
   │   ├── won = True
   │   └── _print_win()
   │
   │   Else:
   │       _print_result(g, y, r)
   │
   └── remaining_attempts--

5. If not won → _print_lose()
```

**Write the code**

```python
    def play(self):
        """Run the coloured game loop with input validation."""
        self._print_header("THINK & GUESS")
        print(Fore.CYAN + f"Max attempts: {self.game.max_attempts}")
        print(Fore.CYAN + "Secret is a 4-digit number with no repeated digits.\n")

        while self.game.remaining_attempts > 0 and not self.game.won:
            print(Fore.MAGENTA + f"Attempts left: {self.game.remaining_attempts}")

            guess = input(Fore.CYAN + "Your guess: " + Style.RESET_ALL).strip()

            if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
                print(Fore.RED + "Invalid guess. Enter exactly 4 non-repeating digits (0-9).")
                continue

            green, yellow, red = self.game.compare_guess(guess)

            if green == 4:
                self.game.won = True
                self._print_win(self.game.secret)
            else:
                self._print_result(green, yellow, red)

            self.game.remaining_attempts -= 1

        if not self.game.won:
            self._print_lose(self.game.secret)
```

**Test it**

```python
if __name__ == "__main__":
    m = MasterMind(max_attempts=5)
    m.start()
```

Run `python mastermind.py`. You should be able to play a full game with 5 attempts.

---

## 4. Run the Game!

Create `main.py`:

```python
from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    menu.run()
```

Run it:

```
python main.py
```

---

## How It Should Look

```
==================================================
            THINK & GUESS
==================================================
1. Start new game
2. Set max attempts (current = 10)
0. Exit

Your choice: 1

==================================================
              THINK & GUESS
==================================================
Max attempts: 10
Secret is a 4-digit number with no repeated digits.

Attempts left: 10
Your guess: 2571
🟢-> 1 / 🟡-> 1 / 🔴-> 2

Attempts left: 9
Your guess: 1589
🟢-> 4 / 🟡-> 0 / 🔴-> 0

🎉 YOU WON! The secret was 1589.
```

---

## Evaluation Checklist

| Criterion | What to check |
|-----------|---------------|
| `_generate_secret()` | Empty-list + while + randint + uniqueness check |
| `compare_guess()` | Returns correct `(green, yellow, red)` |
| Game has no colorama | No colour imports in game.py |
| `_print_header` | Cyan banner with centred yellow text |
| `_print_result` | Aggregated `🟢-> / 🟡-> / 🔴->` counts |
| `_print_win` | Green win message with secret |
| `_print_lose` | Red game-over message with secret |
| `MasterMind.start()` | Creates Game and calls play() |
| `MasterMind.play()` | Validates input, tracks attempts, stops on win or 0 |
| `Menu` works | Uses MasterMind, changes max attempts, exits cleanly |
| Input validation | Rejects wrong length, non-digits, repeated digits |
