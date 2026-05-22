# MasterMind - Full Solution

Complete implementation of all classes with `pass` placeholders filled in.

---

## `game.py`

```python
import random


class Game:
    """Pure business logic — no colours, no output formatting."""

    def __init__(self, max_attempts: int = 10):
        self.max_attempts = max_attempts
        self.secret = self._generate_secret()
        self.remaining_attempts = max_attempts
        self.won = False

    def __repr__(self):
        status = "WON" if self.won else "playing"
        return (f"Game(secret={self.secret}, "
                f"remaining={self.remaining_attempts}, "
                f"status={status})")

    def _generate_secret(self) -> str:
        """Generate a 4-digit string with no repeated digits."""
        digits = []
        while len(digits) < 4:
            d = random.randint(0, 9)
            if d not in digits:
                digits.append(d)
        return ''.join(str(d) for d in digits)

    def compare_guess(self, guess: str):
        """Compare guess with secret and return (green, yellow, red)."""
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

---

## `mastermind.py`

```python
from colorama import init, Fore, Style
from game import Game

init(autoreset=True)


class MasterMind:
    """Presentation layer — colourful game output with colorama."""

    def __init__(self, max_attempts: int = 10):
        self.max_attempts = max_attempts
        self.game = None

    def _print_header(self, text: str):
        """Print a coloured banner."""
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)
        print(Fore.YELLOW + Style.BRIGHT + text.center(50))
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)

    def _print_result(self, green: int, yellow: int, red: int):
        """Display aggregated coloured result counts."""
        parts = [
            Fore.GREEN + f"\U0001f7e2-> {green}",
            Fore.YELLOW + f" / \U0001f7e1-> {yellow}",
            Fore.RED + f" / \U0001f534-> {red}"
        ]
        print("".join(parts))

    def _print_win(self, secret: str):
        """Print a green victory message."""
        print(Fore.GREEN + Style.BRIGHT + f"\n\U0001f389 YOU WON! The secret was {secret}.")

    def _print_lose(self, secret: str):
        """Print a red game-over message."""
        print(Fore.RED + Style.BRIGHT + f"\n\U0001f480 GAME OVER! The secret was {secret}.")

    def start(self):
        """Create a Game instance and start the game loop."""
        self.game = Game(max_attempts=self.max_attempts)
        self.play()

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

---

## `menu.py`

(Identical to the fully provided version in the homework file — see `menu.py`.)

---

## `main.py`

```python
from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    menu.run()
```
