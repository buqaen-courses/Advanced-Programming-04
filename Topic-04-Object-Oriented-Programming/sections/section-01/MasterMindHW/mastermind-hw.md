# 🎯 Exercise: Think & Guess – Mastermind-Style Number Guessing Game (OOP Design)

## 🎮 Sample Gameplay

Here's what a complete game looks like from start to finish:

```
==================================================
           🧠 THINK & GUESS 🧠
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
Your guess: 3482
🟢-> 0 / 🟡-> 2 / 🔴-> 2

Attempts left: 8
Your guess: 1589
🟢-> 4 / 🟡-> 0 / 🔴-> 0

🎉 YOU WON! The secret was 1589.
```

The computer picks a secret 4-digit number (e.g. `1589`). The player guesses, and after each try gets feedback: 🟢 green count (correct digit + position), 🟡 yellow count (correct digit, wrong position), 🔴 red count (not in secret). The player uses this to narrow down the answer before running out of attempts.

---

## 🤔 Think Aloud – What Do We Need?

Before diving into code, let's reason about the problem:

- We need to **generate a random 4-digit secret** with no repeated digits — so we need a way to pick digits and ensure uniqueness.
- We need to **get input from the player** — a 4-digit guess, validated for length, digits only, no repeats.
- We need to **compare** the guess against the secret — figure out which digits are correct and in the right position (green), which are correct but misplaced (yellow), and which are completely wrong (red).
- We need to **score it correctly** — count greens first, then yellows from the remaining unmatched digits.
- The player must **adjust their guess based on the result** — so we show feedback after each attempt.
- We need to **check if max attempts is reached** — stop the game when attempts run out.
- We need to **show a win message** when the player guesses correctly.

---

## 🧱 Three-Class Architecture

| Class | Responsibility |
|-------|---------------|
| `Game` | **Pure business logic only** — secret generation, guess comparison. No `colorama`, no game loop. |
| `MasterMind` | **Presentation layer** — wraps `Game`, handles colourful output with `colorama`, game loop, win/loss messages, aggregated result display. |
| `Menu` | **Interactive menu** — fully provided. Start games, change settings, exit. |

---

## 📋 Requirements – OOP Design

| Requirement | Algorithm / Data Structure |
|-------------|---------------------------|
| **Random secret** | Use an empty `list`, `while len(digits) < 4`, pick `random.randint(0, 9)`, check `if d not in digits` before appending. Join as string. |
| **Compare guess** | Count `green` via positional equality. For `yellow`, collect unmatched digits in two lists, then loop guess_remaining and remove matches from secret_remaining. `red = 4 - green - yellow`. |
| **Coloured display** | Show only **aggregated** counts: `🟢-> 1 / 🟡-> 1 / 🔴-> 2`. Never expose which digit maps to which colour. |
| **Attempt limit** | Stored as `self.max_attempts`. `remaining_attempts` starts equal to it and decrements each round. Game stops at 0. |
| **Game state** | Attributes: `secret` (str), `remaining_attempts` (int), `won` (bool). |
| **Menu system** | `Menu` class (fully provided) with colourful `colorama` console interface. |

---

## 🧩 Step-by-Step — What You Need to Implement

### Step 1: `Game` Class (Business Logic Only)

Create a file named `game.py` inside a folder called `MasterMindHW`.

```python
import random

class Game:
    """Pure business logic — no colours, no output formatting."""

    def __init__(self, max_attempts: int = 10):
        # Store max_attempts
        # Call _generate_secret() and store in self.secret
        # Set self.remaining_attempts = max_attempts
        # Set self.won = False
        pass
```

#### Method 1.1: `_generate_secret(self) -> str`

- **Data structure**: an empty `list` called `digits`.
- **Algorithm**: `while len(digits) < 4`: generate `d = random.randint(0, 9)`. If `d not in digits`, append it. At the end, join as a string.
- **Returns**: a 4-character string of unique digits (e.g. `"3824"`).

```python
def _generate_secret(self) -> str:
    """Generate a 4-digit string with no repeated digits."""
    ...
```

#### Method 1.2: `compare_guess(self, guess: str) -> tuple`

- **Input**: `guess` — a 4-digit string validated by the caller.
- **Algorithm**:
  1. `green = sum(1 for i in range(4) if guess[i] == self.secret[i])`
  2. Build two lists: `secret_remaining` and `guess_remaining` — collect digits where `guess[i] != self.secret[i]`.
  3. Loop through `guess_remaining`, if a digit exists in `secret_remaining`, increment `yellow` and remove that digit from `secret_remaining`.
  4. `red = 4 - green - yellow`
- **Returns**: tuple `(green, yellow, red)` — plain integers, no colours.

```python
def compare_guess(self, guess: str):
    """Compare guess with secret. Returns (green, yellow, red)."""
    ...
```

---

### Step 2: `MasterMind` Class (Presentation Layer)

Create `mastermind.py` in the same folder.

```python
from colorama import init, Fore, Back, Style
from game import Game

init(autoreset=True)

class MasterMind:
    """Presentation layer — colourful game output with colorama."""

    def __init__(self, max_attempts: int = 10):
        self.max_attempts = max_attempts
        self.game = None
```

#### Helper Methods (you implement these)

- **`_print_header(self, text: str)`** — print a coloured banner using `Fore.CYAN + Style.BRIGHT` with `"=" * 50` lines and centred yellow text.
- **`_print_result(self, green: int, yellow: int, red: int)`** — display aggregated result: `🟢-> N / 🟡-> N / 🔴-> N` with each emoji in its respective `Fore.GREEN` / `Fore.YELLOW` / `Fore.RED`. Do **not** show per-digit colours.
- **`_print_win(self, secret: str)`** — green victory message with the secret.
- **`_print_lose(self, secret: str)`** — red game-over message with the secret.

#### Method: `start(self)`

- **Algorithm**:
  - Create `self.game = Game(max_attempts=self.max_attempts)`.
  - Call `self.play()` to run the interactive loop.

```python
def start(self):
    """Create a Game instance and start the game loop."""
    ...
```

#### Method: `play(self)`

This is the **main game loop** — it lives in `MasterMind`, not in `Game`.

- **Algorithm**:
  - Print coloured header and welcome message.
  - Loop while `self.game.remaining_attempts > 0 and not self.game.won`:
    - Print coloured "Attempts left:" message.
    - Get guess with coloured input prompt.
    - **Validate**: `len(guess) == 4`, `guess.isdigit()`, `len(set(guess)) == 4`. If invalid, print coloured error and `continue`.
    - Call `self.game.compare_guess(guess)` → `(green, yellow, red)`.
    - If `green == 4`: set `won = True`, call `_print_win()`.
    - Else: call `_print_result(green, yellow, red)`.
    - Decrement `self.game.remaining_attempts`.
  - After loop, if not won, call `_print_lose()`.

```python
def play(self):
    """Run the coloured game loop with input validation."""
    ...
```

---

### Step 3: `Menu` Class — Fully Implemented ✅

Create `menu.py` in the same folder. This one is **fully provided** — copy it as-is.

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
        print(Fore.GREEN + f"✓ {msg}")

    def _print_error(self, msg: str):
        print(Fore.RED + f"✗ {msg}")

    def _print_info(self, msg: str):
        print(Fore.BLUE + f"ℹ {msg}")

    def start_new_game(self):
        self.mastermind = MasterMind(max_attempts=self.max_attempts)
        self.mastermind.start()
        self._print_info("Game finished. Returning to menu...")

    def set_max_attempts(self):
        try:
            new_val = int(input(Fore.YELLOW + f"New max attempts (current = {self.max_attempts}): " + Style.RESET_ALL).strip())
            if new_val < 1:
                self._print_error("Attempts must be >= 1")
            else:
                self.max_attempts = new_val
                self._print_success(f"Max attempts set to {self.max_attempts}")
        except ValueError:
            self._print_error("Please enter a valid integer.")

    def run(self):
        while True:
            self._print_header("🧠 THINK & GUESS 🧠")
            print(Fore.MAGENTA + Style.BRIGHT + "1." + Fore.GREEN + " Start new game")
            print(Fore.MAGENTA + Style.BRIGHT + "2." + Fore.GREEN + f" Set max attempts (current = {self.max_attempts})")
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
```

---

## ✅ Final Integration

Create a `main.py` file that ties everything together:

```python
from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    menu.run()
```

---

## 📤 Expected Gameplay Example

```
==================================================
           🧠 THINK & GUESS 🧠
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

## 📌 Evaluation Criteria

| Criterion | What to check |
|-----------|---------------|
| `_generate_secret()` | Uses empty-list + `while` loop + `random.randint` + uniqueness check. |
| `compare_guess()` | Returns correct `(green, yellow, red)` — no colours, no strings attached. |
| `Game` has no `colorama` | No colour imports, no coloured output, no game loop in `game.py`. |
| `MasterMind.play()` | Validates input, tracks attempts, stops on win or 0 attempts, coloured output. |
| `MasterMind` result display | Shows aggregated `🟢-> / 🟡-> / 🔴->` counts only — no per-position colours. |
| `Menu` works | Uses `MasterMind`, changes max attempts, exits cleanly. |
| Input validation | Rejects wrong length, non-digits, repeated digits. |

Good luck! 🚀
