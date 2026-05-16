from colorama import init, Fore, Back, Style
from game import Game

init(autoreset=True)


class MasterMind:
    """Presentation layer — colourful game output with colorama."""

    def __init__(self, max_attempts: int = 10):
        # max_attempts: max guesses allowed, passed to Game when created
        self.max_attempts = max_attempts
        # game: a Game instance, created when start() is called
        self.game = None

    def _print_header(self, text: str):
        """Print a coloured banner with cyan lines and centred yellow text.

        Args:
            text (str): The title text to display in the banner.

        Example output:
            ==================================================
                          THINK & GUESS
            ==================================================
        """
        pass

    def _print_result(self, green: int, yellow: int, red: int):
        """Display aggregated coloured result counts.

        Shows counts only — does NOT expose which digit maps to which colour.

        Args:
            green (int): Number of exact matches.
            yellow (int): Number of correct digits in wrong positions.
            red (int): Number of completely wrong digits.

        Example output:
            🟢-> 1 / 🟡-> 1 / 🔴-> 2
        """
        pass

    def _print_win(self, secret: str):
        """Print a green victory message revealing the secret.

        Args:
            secret (str): The secret number the player guessed.

        Example output:
            🎉 YOU WON! The secret was 1589.
        """
        pass

    def _print_lose(self, secret: str):
        """Print a red game-over message revealing the secret.

        Args:
            secret (str): The secret number the player failed to guess.

        Example output:
            💀 GAME OVER! The secret was 1589.
        """
        pass

    def start(self):
        """Create a Game instance and start the game loop.

        Flow:
            1. Create Game(max_attempts=self.max_attempts).
            2. Call self.play() to run the interactive loop.
        """
        pass

    def play(self):
        """Run the coloured game loop with input validation.

        Flow:
            1. Print coloured header and welcome message.
            2. Loop while self.game.remaining_attempts > 0 and not self.game.won:
               a. Print coloured "Attempts left:" prompt.
               b. Get guess with coloured input prompt.
               c. Validate: length=4, all digits, no repeats (coloured error).
               d. Call self.game.compare_guess(guess) -> (green, yellow, red).
               e. If green==4: set won=True, call _print_win().
               f. Else: call _print_result() with the counts.
               g. Decrement self.game.remaining_attempts.
            3. After loop, if not won, call _print_lose().

        Example interaction:
            ==================================================
                          THINK & GUESS
            ==================================================
            Attempts left: 10
            Your guess: 2571
            🟢-> 1 / 🟡-> 1 / 🔴-> 2
        """
        pass
