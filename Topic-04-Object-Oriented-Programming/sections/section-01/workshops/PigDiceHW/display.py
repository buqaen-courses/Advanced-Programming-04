from colorama import init, Fore, Style

init(autoreset=True)


class Display:
    """Helper class for coloured game output.

    Fully implemented — use from PigGame via self.display.print_*().
    """

    def __init__(self, header_color=Fore.CYAN, text_color=Fore.YELLOW,
                 success_color=Fore.GREEN, danger_color=Fore.RED,
                 info_color=Fore.BLUE, bright_style=Style.BRIGHT):
        self.header_color = header_color
        self.text_color = text_color
        self.success_color = success_color
        self.danger_color = danger_color
        self.info_color = info_color
        self.bright_style = bright_style

    def print_header(self, text: str):
        print(self.header_color + self.bright_style + "=" * 50)
        print(self.text_color + self.bright_style + text.center(50))
        print(self.header_color + self.bright_style + "=" * 50)

    def print_scoreboard(self, p1, p2):
        print(self.header_color + f"Score: {p1.name} = {p1.score} (\U0001f6e1\ufe0f:{p1.advantages}), {p2.name} = {p2.score} (\U0001f6e1\ufe0f:{p2.advantages})")

    def print_die_roll(self, value: int, turn_total: int):
        print(self.text_color + f"Rolled: \U0001f3b2 {value}  \u2192 turn total = {turn_total}")

    def print_pig_out(self):
        print(self.danger_color + "Rolled: \U0001f3b2 1  \u2192 \U0001f437 PIG! Lost all turn points.")

    def print_banked(self, banked: int):
        print(self.success_color + f"\u2705 Banked {banked} points!")

    def print_winner(self, name: str, score: int):
        print(self.success_color + self.bright_style + f"\n\U0001f3c6 {name} wins with {score} points!")

    def print_ai_message(self, decision: str):
        text = "roll" if decision == "r" else "hold"
        print(self.text_color + f"\U0001f916 AI chooses to {text}.")

    def print_shield_offer(self, advantages: int):
        print(self.header_color + f"\U0001f6e1\ufe0f Rolled 6! Activate shield? (y/n): ", end="")

    def print_shield_activated(self, advantages: int):
        print(self.info_color + f"\U0001f6e1\ufe0f Shield active! Turn total protected (advantages left: {advantages})")

    def print_shield_saved(self, half: int):
        print(self.info_color + f"\U0001f6e1\ufe0f Shield saved you! Turn total halved to {half}.")

    def print_no_advantages(self):
        print(self.danger_color + "\u274c No advantages left! 6 added to turn total normally.")