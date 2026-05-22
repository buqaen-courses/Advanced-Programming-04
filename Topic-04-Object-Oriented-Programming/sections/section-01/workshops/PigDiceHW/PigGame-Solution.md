# Pig Dice - Full Solution

Complete implementation of all classes with `pass` placeholders filled in.

---

## `display.py`

(Identical to the fully provided version in the homework file — see `display.py`.)

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

    def __repr__(self):
        shield = "\U0001f6e1\ufe0f" if self.shield_active else "\U0001f513"
        return (f"Player({self.name}, score={self.score}, "
                f"turn={self.turn_total}, adv={self.advantages}, {shield})")

    def reset_turn(self):
        """Set turn_total = 0 after hold or pig-out."""
        self.turn_total = 0
```

---

## `pig_game.py`

All game logic + game loop. Uses `self.display` (the `Display` helper) for coloured output.

```python
import math
import random
import time
from player import Player
from display import Display


class PigGame:
    """All game logic + game loop. Uses Display for coloured output."""

    def __init__(self, target_score: int = 20):
        self.target_score = target_score
        self.players = [Player("Player 1"), Player("Player 2", is_ai=True)]
        self.display = Display()
        self.current_index = 0
        self.game_over = False

    def _roll_die(self) -> int:
        return random.randint(1, 6)

    def roll(self) -> int:
        value = self._roll_die()
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
