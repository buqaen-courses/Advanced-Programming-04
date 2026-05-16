from colorama import init, Fore, Style

init(autoreset=True)


class PigDisplay:
    """Coloured display for the Pig Dice game.

    Instantiate with optional color/style defaults.
    """

    def __init__(self, header_color=Fore.CYAN, text_color=Fore.YELLOW,
                 success_color=Fore.GREEN, danger_color=Fore.RED,
                 info_color=Fore.BLUE, ai_color=Fore.YELLOW,
                 bright_style=Style.BRIGHT):
        self.header_color = header_color
        self.text_color = text_color
        self.success_color = success_color
        self.danger_color = danger_color
        self.info_color = info_color
        self.ai_color = ai_color
        self.bright_style = bright_style

    def print_header(self, text: str):
        """Print a coloured banner with cyan lines and centred yellow text.

        Args:
            text (str): The title text to display.

        Example output:
            ==================================================
                       PIG DICE
            ==================================================
        """
        print(self.header_color + self.bright_style + "=" * 50)
        print(self.text_color + self.bright_style + text.center(50))
        print(self.header_color + self.bright_style + "=" * 50)

    def print_scoreboard(self, p1, p2):
        """Display both players' scores and advantages.

        Args:
            p1 (Player): First player.
            p2 (Player): Second player.

        Example output:
            Score: Player 1 = 3 (🛡️:1), Player 2 = 10 (🛡️:0)
        """
        print(self.header_color + f"Score: {p1.name} = {p1.score} (\U0001f6e1\ufe0f:{p1.advantages}), {p2.name} = {p2.score} (\U0001f6e1\ufe0f:{p2.advantages})")

    def print_die_roll(self, value: int, turn_total: int):
        """Show the die roll result and updated turn total in yellow.

        Args:
            value (int): The die value rolled (2–6).
            turn_total (int): The current turn total after this roll.

        Example output:
            Rolled: 🎲 5  → turn total = 5
        """
        print(self.text_color + f"Rolled: \U0001f3b2 {value}  \u2192 turn total = {turn_total}")

    def print_pig_out(self):
        """Show pig-out message in red.

        Example output:
            Rolled: 🎲 1  → 🐷 PIG! Lost all turn points.
        """
        print(self.danger_color + "Rolled: \U0001f3b2 1  \u2192 \U0001f437 PIG! Lost all turn points.")

    def print_banked(self, banked: int):
        """Show banked points in green.

        Args:
            banked (int): The number of points banked.

        Example output:
            ✅ Banked 10 points!
        """
        print(self.success_color + f"\u2705 Banked {banked} points!")

    def print_winner(self, name: str, score: int):
        """Show the winner in bright green.

        Args:
            name (str): The winner's name.
            score (int): The winner's final score.

        Example output:
            🏆 Player 1 wins with 100 points!
        """
        print(self.success_color + self.bright_style + f"\n\U0001f3c6 {name} wins with {score} points!")

    def print_ai_message(self, decision: str):
        """Show the AI's decision in yellow.

        Args:
            decision (str): 'r' for roll or 'h' for hold.

        Example output:
            🤖 AI chooses to roll.
            🤖 AI chooses to hold.
        """
        text = "roll" if decision == "r" else "hold"
        print(self.ai_color + f"\U0001f916 AI chooses to {text}.")

    def print_shield_offer(self, advantages: int):
        """Prompt the player to use a shield on rolling a 6.

        Args:
            advantages (int): How many shields remaining.

        Example output:
            🛡️ Rolled 6! Activate shield? (y/n):
        """
        print(self.header_color + f"\U0001f6e1\ufe0f Rolled 6! Activate shield? (y/n): ", end="")

    def print_shield_activated(self, advantages: int):
        """Show shield activation message in blue.

        Args:
            advantages (int): Shields remaining after activation.

        Example output:
            🛡️ Shield active! Turn total protected (advantages left: 2)
        """
        print(self.info_color + f"\U0001f6e1\ufe0f Shield active! Turn total protected (advantages left: {advantages})")

    def print_shield_saved(self, half: int):
        """Show that the shield halved the damage from rolling a 1.

        Args:
            half (int): The halved turn total after protection.

        Example output:
            🛡️ Shield saved you! Turn total halved to 4.
        """
        print(self.info_color + f"\U0001f6e1\ufe0f Shield saved you! Turn total halved to {half}.")

    def print_no_advantages(self):
        """Show message when player has no advantages left.

        Example output:
            ❌ No advantages left! 6 added to turn total normally.
        """
        print(self.danger_color + "\u274c No advantages left! 6 added to turn total normally.")
