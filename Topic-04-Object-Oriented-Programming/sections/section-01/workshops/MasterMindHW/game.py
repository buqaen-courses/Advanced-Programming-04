import random


class Game:
    """Pure business logic — no colours, no output formatting."""

    def __init__(self, max_attempts: int = 10):
        # max_attempts: max number of guesses allowed (default 10)
        self.max_attempts = max_attempts
        # secret: the 4-digit random string the player must guess
        self.secret = self._generate_secret()
        # remaining_attempts: starts equal to max_attempts, decrements each round
        self.remaining_attempts = max_attempts
        # won: becomes True when player guesses correctly
        self.won = False

    def __repr__(self):
        status = "WON" if self.won else "playing"
        return (f"Game(secret={self.secret}, "
                f"remaining={self.remaining_attempts}, "
                f"status={status})")

    def _generate_secret(self) -> str:
        """Generate a 4-digit string with no repeated digits.

        Returns:
            str: A 4-character string of unique digits 0-9.

        Example output:
            "3824", "5901", "7146"
        """
        pass

    def compare_guess(self, guess: str):
        """Compare guess with secret and return colour counts.

        Args:
            guess (str): A 4-digit string entered by the player.

        Returns:
            tuple: (green, yellow, red) where each is an int.

        Example:
            secret = "1589"
            compare_guess("1234") -> (1, 0, 3)
            compare_guess("1589") -> (4, 0, 0)
            compare_guess("8519") -> (0, 4, 0)
            compare_guess("2571") -> (0, 2, 2)
        """
        pass
