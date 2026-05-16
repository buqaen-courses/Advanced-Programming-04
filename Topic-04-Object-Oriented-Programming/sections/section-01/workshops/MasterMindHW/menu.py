from colorama import init, Fore, Style
from mastermind import MasterMind

init(autoreset=True)

class Menu:
    """Colourful interactive menu for the Think & Guess game."""

    def __init__(self):
        # max_attempts: default max guesses, can be changed via menu option 2
        self.max_attempts = 10
        # mastermind: a MasterMind instance, created when starting a new game
        self.mastermind = None

    def _print_header(self, text: str):
        """Print a coloured banner with cyan lines and centred yellow text.

        Args:
            text (str): The title text to display.

        Example output:
            ==================================================
                      THINK & GUESS
            ==================================================
        """
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)
        print(Fore.YELLOW + Style.BRIGHT + text.center(50))
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)

    def _print_success(self, msg: str):
        """Print a green success message.

        Args:
            msg (str): The success text.

        Example output:
            ✓ Max attempts set to 15
        """
        print(Fore.GREEN + f"✓ {msg}")

    def _print_error(self, msg: str):
        """Print a red error message.

        Args:
            msg (str): The error text.

        Example output:
            ✗ Invalid choice. Enter 1, 2 or 0.
        """
        print(Fore.RED + f"✗ {msg}")

    def _print_info(self, msg: str):
        """Print a blue info message.

        Args:
            msg (str): The info text.

        Example output:
            ℹ Game finished. Returning to menu...
        """
        print(Fore.BLUE + f"ℹ {msg}")

    def start_new_game(self):
        """Create a MasterMind instance and start a new game.

        Flow:
            1. Create MasterMind(max_attempts=self.max_attempts).
            2. Call .start() which runs the full game loop.
            3. After game ends, print info message and return to menu.
        """
        self.mastermind = MasterMind(max_attempts=self.max_attempts)
        self.mastermind.start()
        self._print_info("Game finished. Returning to menu...")

    def set_max_attempts(self):
        """Prompt the user to change the maximum allowed attempts.

        Input:
            Prompts for an integer.

        Example:
            New max attempts (current = 10): 15
            ✓ Max attempts set to 15

        On error:
            New max attempts (current = 10): abc
            ✗ Please enter a valid integer.
        """
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
        """Main menu loop. Displays options and handles user choice.

        Options:
            1 — Start a new game
            2 — Change max attempts
            0 — Exit

        Example flow:
            ==================================================
                      🧠 THINK & GUESS 🧠
            ==================================================
            1. Start new game
            2. Set max attempts (current = 10)
            0. Exit

            Your choice: 1
        """
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


if __name__ == "__main__":
    menu = Menu()
    menu.run()
