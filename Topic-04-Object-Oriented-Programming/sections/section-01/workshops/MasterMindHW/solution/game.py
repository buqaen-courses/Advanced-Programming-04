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
        digits = []
        while len(digits) < 4:
            d = random.randint(0, 9)
            if d not in digits:
                digits.append(d)
        return ''.join(str(d) for d in digits)

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
