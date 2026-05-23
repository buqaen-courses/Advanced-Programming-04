from colorama import init, Fore, Style
from pig_game import PigGame

init(autoreset=True)


class Menu:
    """Colourful interactive menu for the Pig Dice game."""

    def __init__(self):
        self.target_score = 20
        self.pig_game = None

    def _print_header(self, text: str):
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)
        print(Fore.YELLOW + Style.BRIGHT + text.center(50))
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)

    def _print_success(self, msg: str):
        print(Fore.GREEN + f"{msg}")

    def _print_error(self, msg: str):
        print(Fore.RED + f"{msg}")

    def _print_info(self, msg: str):
        print(Fore.BLUE + f"{msg}")

    def start_new_game(self):
        self.pig_game = PigGame(target_score=self.target_score)
        self.pig_game.play()
        self._print_info("Game finished. Returning to menu...")

    def set_target_score(self):
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
        while True:
            self._print_header("PIG DICE GAME")
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