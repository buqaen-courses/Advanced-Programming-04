from colorama import init, Fore, Style
from game import Game

init(autoreset=True)


class MasterMind:
    """Presentation layer — colourful game output with colorama."""

    def __init__(self, max_attempts: int = 10):
        self.max_attempts = max_attempts
        self.game = None

    def _print_header(self, text: str):
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)
        print(Fore.YELLOW + Style.BRIGHT + text.center(50))
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)

    def _print_result(self, green: int, yellow: int, red: int):
        parts = [
            Fore.GREEN + f"\U0001f7e2-> {green}",
            Fore.YELLOW + f" / \U0001f7e1-> {yellow}",
            Fore.RED + f" / \U0001f534-> {red}"
        ]
        print("".join(parts))

    def _print_win(self, secret: str):
        print(Fore.GREEN + Style.BRIGHT + f"\n\U0001f389 YOU WON! The secret was {secret}.")

    def _print_lose(self, secret: str):
        print(Fore.RED + Style.BRIGHT + f"\n\U0001f480 GAME OVER! The secret was {secret}.")

    def start(self):
        self.game = Game(max_attempts=self.max_attempts)
        self.play()

    def play(self):
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
