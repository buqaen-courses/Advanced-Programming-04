# 🐷 Pig Dice – Full Solution

Complete implementation of all classes with `pass` placeholders filled in.

---

## `player.py`

```python
class Player:
    """Represents a player with a score and current turn total."""

    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.is_ai = is_ai
        self.score = 0
        self.turn_total = 0
        self.advantages = 0
        self.shield_active = False

    def reset_turn(self):
        """Set turn_total = 0 after hold or pig-out."""
        self.turn_total = 0
```

---

## `dice.py`

```python
import random


class Dice:
    """A single six-sided die."""

    @staticmethod
    def roll() -> int:
        return random.randint(1, 6)
```

---

## `pig_display.py`

Instance-based display helper — instantiate with color/style defaults, then call methods for coloured output.

```python
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
        print(self.ai_color + f"\U0001f916 AI chooses to {text}.")

    def print_shield_offer(self, advantages: int):
        print(self.header_color + f"\U0001f6e1\ufe0f Rolled 6! Activate shield? (y/n): ", end="")

    def print_shield_activated(self, advantages: int):
        print(self.info_color + f"\U0001f6e1\ufe0f Shield active! Turn total protected (advantages left: {advantages})")

    def print_shield_saved(self, half: int):
        print(self.info_color + f"\U0001f6e1\ufe0f Shield saved you! Turn total halved to {half}.")

    def print_no_advantages(self):
        print(self.danger_color + "\u274c No advantages left! 6 added to turn total normally.")
```

---

## `pig_game.py`

All game logic + the full game loop. Uses `self.display` (PigDisplay) for coloured output.

```python
import math
import random
import time
from player import Player
from dice import Dice
from pig_display import PigDisplay


class PigGame:
    """All game logic + game loop. Uses PigDisplay for coloured output."""

    def __init__(self, target_score: int = 20):
        self.target_score = target_score
        self.players = [Player("Player 1"), Player("Player 2", is_ai=True)]
        self.dice = Dice()
        self.display = PigDisplay()
        self.current_index = 0
        self.game_over = False

    def roll(self) -> int:
        value = self.dice.roll()
        player = self.current_player
        if value == 1:
            if player.shield_active:
                player.shield_active = False
                player.turn_total = math.ceil(player.turn_total / 2)
            else:
                player.reset_turn()
                self.switch_player()
        else:
            player.turn_total += value
        return value

    def hold(self):
        player = self.current_player
        player.score += player.turn_total
        player.reset_turn()
        if player.score >= self.target_score:
            self.game_over = True
        else:
            self.switch_player()

    def switch_player(self):
        self.current_index = 1 - self.current_index

    def activate_shield(self) -> bool:
        player = self.current_player
        if player.advantages > 0:
            player.advantages -= 1
            player.shield_active = True
            return True
        return False

    def ai_decision(self) -> str:
        if self.current_player.turn_total == 0:
            return 'r'
        return random.choice(['r', 'h'])

    def ai_should_convert_six_to_shield(self) -> bool:
        player = self.current_player
        return player.is_ai and player.advantages == 0 and not player.shield_active

    def convert_six_to_shield(self):
        player = self.current_player
        player.advantages = 1
        player.shield_active = True

    @property
    def current_player(self):
        return self.players[self.current_index]

    @property
    def winner(self):
        if self.game_over:
            for p in self.players:
                if p.score >= self.target_score:
                    return p
        return None

    def play(self):
        """Run the full coloured game loop."""
        self.display.print_header("PIG DICE")
        print(Fore.CYAN + f"Target: {self.target_score} points\n")

        while not self.game_over:
            self.display.print_scoreboard(self.players[0], self.players[1])
            player = self.current_player
            label = " (AI)" if player.is_ai else ""
            shield = " \U0001f6e1\ufe0f" if player.shield_active else ""
            print(Fore.MAGENTA + f"\n--- {player.name}'s turn{label}{shield} ---")

            while not self.game_over:
                if player.is_ai:
                    choice = self.ai_decision()
                    self.display.print_ai_message(choice)
                    time.sleep(0.8)
                else:
                    choice = input(Fore.CYAN + "(r)oll or (h)old? " + Style.RESET_ALL).strip().lower()

                if choice == "r":
                    value = self.roll()

                    if value == 1:
                        if player.shield_active:
                            self.display.print_shield_saved(player.turn_total)
                        else:
                            self.display.print_pig_out()
                        break
                    elif value == 6:
                        use_shield = False
                        if player.is_ai and self.ai_should_convert_six_to_shield():
                            use_shield = True
                        elif not player.is_ai and player.advantages > 0:
                            self.display.print_shield_offer(player.advantages)
                            if input().strip().lower() == "y":
                                use_shield = True

                        if use_shield:
                            if player.is_ai:
                                self.convert_six_to_shield()
                            else:
                                self.activate_shield()
                            player.turn_total -= 6
                            self.display.print_shield_activated(player.advantages)
                        else:
                            self.display.print_die_roll(value, player.turn_total)
                    else:
                        self.display.print_die_roll(value, player.turn_total)

                    if player.is_ai:
                        continue
                elif choice == "h":
                    banked = player.turn_total
                    self.hold()
                    if banked > 0:
                        self.display.print_banked(banked)
                    break
                else:
                    if not player.is_ai:
                        print(Fore.RED + "Invalid. Enter 'r' to roll or 'h' to hold.")

        winner = self.winner
        if winner:
            self.display.print_winner(winner.name, winner.score)
```

---

## `menu.py`

(Identical to the fully implemented version in the homework file — see `menu.py`.)

---

## `main.py`

```python
from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    menu.run()
```
