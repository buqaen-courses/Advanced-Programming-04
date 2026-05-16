from colorama import init, Fore, Style
from pig_game import PigGame

init(autoreset=True)


class Menu:
    """Colourful interactive menu for the Pig Dice game."""

    def __init__(self):
        # target_score: points needed to win, configurable via menu option 2
        self.target_score = 20
        # pig_game: a PigGame instance, created when starting a new game
        self.pig_game = None

    def _print_header(self, text: str):
        """Print a coloured banner with cyan lines and centred yellow text.

        Args:
            text (str): The title text to display.

        Example output:
            ==================================================
                      PIG DICE GAME
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
            ✓ Target score set to 150
        """
        print(Fore.GREEN + f"\u2713 {msg}")

    def _print_error(self, msg: str):
        """Print a red error message.

        Args:
            msg (str): The error text.

        Example output:
            ✗ Target score must be >= 10
        """
        print(Fore.RED + f"\u2717 {msg}")

    def _print_info(self, msg: str):
        """Print a blue info message.

        Args:
            msg (str): The info text.

        Example output:
            ℹ Game finished. Returning to menu...
        """
        print(Fore.BLUE + f"\u2139 {msg}")

    def start_new_game(self):
        """Create a PigGame instance and start a new game.

        Flow:
            1. Create PigGame(target_score=self.target_score).
            2. Call .play() which runs the full game loop.
            3. After game ends, print info message and return to menu.
        """
        self.pig_game = PigGame(target_score=self.target_score)
        self.pig_game.play()
        self._print_info("Game finished. Returning to menu...")

    def set_target_score(self):
        """Prompt the user to change the target winning score.

        Input:
            Prompts for an integer >= 10.

        Example:
            New target score (current = 20): 50
            ✓ Target score set to 50

        On error:
            New target score (current = 20): abc
            ✗ Please enter a valid integer.
        """
        try:
            new_val = int(input(
                Fore.YELLOW + f"New target score (current = {self.target_score}): "
                + Style.RESET_ALL
            ).strip())
            if new_val < 10:
                self._print_error("Target score must be >= 10")
            else:
                self.target_score = new_val
                self._print_success(f"Target score set to {self.target_score}")
        except ValueError:
            self._print_error("Please enter a valid integer.")

    def run(self):
        """Main menu loop. Displays options and handles user choice.

        Options:
            1 — Start a new game
            2 — Change target score
            0 — Exit

        Example flow:
            ==================================================
                      🐷 PIG DICE GAME 🐷
            ==================================================
            1. Start new game
            2. Set target score (current = 20)
            0. Exit

            Your choice: 1
        """
        while True:
            self._print_header("\U0001f437 PIG DICE GAME \U0001f437")
            print(Fore.MAGENTA + Style.BRIGHT + "1." + Fore.GREEN + " Start new game")
            print(Fore.MAGENTA + Style.BRIGHT + "2." + Fore.GREEN +
                  f" Set target score (current = {self.target_score})")
            print(Fore.RED + Style.BRIGHT + "0." + Fore.RED + " Exit")

            choice = input(Fore.CYAN + "\nYour choice: " + Style.RESET_ALL).strip()

            if choice == "1":
                self.start_new_game()
            elif choice == "2":
                self.set_target_score()
            elif choice == "0":
                self._print_info("Thanks for playing! Goodbye.")
                break
            else:
                self._print_error("Invalid choice. Enter 1, 2 or 0.")


if __name__ == "__main__":
    menu = Menu()
    menu.run()
