# 🎯 Exercise: Pig Dice Game (2-Player)

## 🎮 Sample Gameplay

```
==================================================
            🐷 PIG DICE GAME 🐷
==================================================
1. Start new game
2. Set target score (current = 20)
0. Exit

Your choice: 1

==================================================
               PIG DICE
==================================================
Target: 20 points
Player 1 goes first.

--- Player 1's turn ---
Rolled: 🎲 5  → turn total = 5
(r)oll or (h)old? r
Rolled: 🎲 6
🛡️ Rolled 6! Activate shield? (y/n): y
🛡️ Shield active! Turn total stays at 5 (advantages left: 1)
(r)oll or (h)old? r
Rolled: 🎲 1
🛡️ Shield saved you! Turn total halved to 3 (ceil(5/2)).
(r)oll or (h)old? h
✅ Banked 3 points!
Score: Player 1 = 3 (🛡️:1), Player 2 = 0 (🛡️:0)

--- Player 2's turn (AI) ---
🤖 AI chooses to roll.
Rolled: 🎲 6
🛡️ AI converts first 6 to a shield! (advantages: 1)
🤖 AI chooses to roll.
Rolled: 🎲 4  → turn total = 4
🤖 AI chooses to roll.
Rolled: 🎲 6  → turn total = 10
🤖 AI chooses to hold.
✅ Banked 10 points!
Score: Player 1 = 3 (🛡️:1), Player 2 = 10 (🛡️:1)
...
```

You (Player 1) vs the **AI system** (Player 2). Roll a die - roll as many times as you want, but a 1 wipes your turn's points (unless you have a shield!). **When you roll a 6**, you may spend one **advantage** (you start with 0 - earn more by rolling 6s!) to activate a **shield** 🛡️. The shield protects your next pig-out: instead of losing everything, your turn total is **halved** (using `ceil`). First to reach the target score (default 20) wins.

---

## 🤔 Think Aloud – What Do We Need?

- A **die** that produces random values 1–6.
- A **player** that tracks their total score, current turn total, and **advantages** (shields).
- **Turn logic**: player decides to roll again or hold. A roll of 1 loses the turn's points. Holding banks them.
- **Shield mechanic**: rolling a 6 lets you spend an advantage to activate a shield. When shielded and you roll a 1, turn total is **halved** instead of zeroed. The shield is consumed upon use.
- **AI opponent**: Player 2 is the computer - randomly decides roll/hold. Has a simple shield strategy: converts the **first 6** it rolls into a shield, then adds subsequent 6s to total normally.
- A **win check**: after banking, check if any player reached the target score.
- **Visual feedback**: show die rolls, turn totals, scores, shield status, AI decisions, and who won with colours.

---

## 🧱 Class Architecture

| Class | Responsibility |
|-------|---------------|
| `Player` | Holds `score`, `turn_total`, `is_ai`, `advantages` (default 0), `shield_active`. Resets `turn_total` each turn. |
| `Dice` | `roll()` returns a random int 1–6. |
| `PigGame` | **All game logic + game loop** - players, dice, roll/hold/shield, AI decision, win check, `play()` method. Uses `self.display` (PigDisplay) for coloured output. |
| `PigDisplay` | **Coloured output helper** - instantiated with color/style defaults. Instance methods for all display. |
| `Menu` | **Interactive menu** - fully provided. Start game, set target score, exit. |

---

## 📋 Requirements – OOP Design

### `Player`
- **State:** `score`, `turn_total`, `is_ai`, `advantages` (int, default 0), `shield_active` (bool).
- **Method:** `reset_turn()` → sets `turn_total = 0`.

### `Dice`
- **Method:** `roll()` → returns `random.randint(1, 6)`.

### `PigGame`
- **Roll action:** Roll die. If 1 + shield_active: `turn_total = ceil(turn_total / 2)`, clear shield. If 1 + no shield: pig-out + switch. Else: add to turn total.
- **Hold action:** Add turn_total to score. If score ≥ target → game over. Else → switch player.
- **Switch player:** Toggle `current_index` between 0 and 1.
- **Shield activation:** When rolling a 6, human may spend 1 advantage → `shield_active = True`, the 6 is NOT added to turn total.
- **AI decision:** If `turn_total == 0` always roll. Else `random.choice(['r', 'h'])`.
- **AI shield:** First 6 → `convert_six_to_shield()` (advantages=1, shield_active=True). Later 6s → add to total.
- **Win check:** After each hold, compare each player's score to `target_score`.

### `PigDisplay`
- **Constructor:** Stores color/style defaults (`header_color`, `text_color`, `success_color`, `danger_color`, `info_color`, `ai_color`, `bright_style`).
- **Methods:** `print_header()`, `print_scoreboard()`, `print_die_roll()`, `print_pig_out()`, `print_banked()`, `print_winner()`, `print_ai_message()`, `print_shield_offer()`, `print_shield_activated()`, `print_shield_saved()`, `print_no_advantages()` - each uses `self.*_color` for coloured output.

### `Menu`
- **Options:** Start new game (creates `PigGame` and calls `.play()`), set target score, exit.
- **Validation:** Rejects non-integer or < 10 target scores.

---

## 🧩 Step-by-Step - What You Need to Implement

### Step 1: `Player` Class

Create `player.py` in `PigDiceHW/`.

```python
class Player:
    """Represents a player with a score and current turn total."""

    def __init__(self, name: str, is_ai: bool = False):
        pass

    def reset_turn(self):
        """Reset turn_total to 0 at the start of a new turn."""
        pass
```

| Method | Algorithm |
|--------|-----------|
| `__init__` | Store `name` and `is_ai`. Set `score = 0`, `turn_total = 0`, `advantages = 0`, `shield_active = False`. |
| `reset_turn` | Set `self.turn_total = 0` after hold (points banked) or pig-out. |

---

### Step 2: `Dice` Class

Create `dice.py` in `PigDiceHW/`.

```python
import random


class Dice:
    """A single six-sided die."""

    @staticmethod
    def roll() -> int:
        """Roll the die and return a value 1–6."""
        pass
```

| Method | Algorithm |
|--------|-----------|
| `roll` | Return `random.randint(1, 6)`. |

---

### Step 3: `PigGame` Class (All Logic + Game Loop)

Create `pig_game.py` in `PigDiceHW/`.

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
        pass

    def roll(self) -> int:
        """Roll the die and process the result.

        Returns:
            int: The die value (1–6).

        Side effects:
            - If die == 1 and shield_active: turn_total = ceil(turn_total/2), shield cleared.
            - If die == 1 and no shield: reset turn, switch_player().
            - If die != 1: die value added to current player's turn_total.
        """
        pass

    def hold(self):
        """Bank the current player's turn_total into their score.

        Side effects:
            - Adds turn_total to current player's score.
            - Calls reset_turn() on current player.
            - If score >= target_score, sets self.game_over = True.
            - Otherwise, calls switch_player().
        """
        pass

    def switch_player(self):
        """Toggle to the other player (0 -> 1, 1 -> 0)."""
        pass

    def activate_shield(self) -> bool:
        """Activate a shield for the current player (costs 1 advantage).

        Returns:
            bool: True if activated, False if no advantages left.
        """
        pass

    def ai_decision(self) -> str:
        """AI randomly chooses 'r' (roll) or 'h' (hold).

        Returns:
            str: 'r' or 'h'.

        Algorithm:
            If turn_total == 0 → always roll.
            Else → random.choice(['r', 'h']).
        """
        pass

    def ai_should_convert_six_to_shield(self) -> bool:
        """Check if AI should convert the current 6 roll into a shield.

        Strategy:
            AI keeps one shield. If advantages==0 and shield not active,
            the first 6 becomes a shield. Later 6s are added normally.

        Returns:
            bool: True if AI should use the 6 for a shield.
        """
        pass

    def convert_six_to_shield(self):
        """Convert a rolled 6 into a shield (AI's first 6).

        Sets advantages=1 and shield_active=True.
        The play() method handles removing the 6 from turn_total.
        """
        pass

    @property
    def current_player(self):
        """Return the Player object whose turn it is."""
        pass

    @property
    def winner(self):
        """Return the winning Player, or None if game is not over."""
        pass

    def play(self):
        """Run the full coloured game loop.

        Flow:
            1. Print header and target score via self.display.
            2. Loop while not game_over:
               a. Print scoreboard.
               b. Print whose turn it is.
               c. If AI: auto-decide roll/hold.
               d. If human: prompt for (r)oll or (h)old.
               e. On roll: process result (pig-out, shield, normal).
                  On rolling 6: offer shield (human) or auto-convert (AI).
               f. On hold: bank points, check win.
               g. Validate input.
            3. Print winner.
        """
        pass
```

| Method | Algorithm |
|--------|-----------|
| `__init__` | Create `self.players = [Player("Player 1"), Player("Player 2", is_ai=True)]`. Create `self.dice = Dice()`. Create `self.display = PigDisplay()`. Set `self.current_index = 0`. Set `self.target_score = target_score`. Set `self.game_over = False`. |
| `roll` | Call `self.dice.roll()`. If value == 1 and player.shield_active: `turn_total = math.ceil(turn_total / 2)`, `shield_active = False`. If value == 1 and no shield: `reset_turn()`, `switch_player()`. Else: add value to `turn_total`. Return value. |
| `hold` | Add `turn_total` to `score`. Call `reset_turn()`. If `score >= target_score`: `game_over = True`. Else: `switch_player()`. |
| `switch_player` | `self.current_index = 1 - self.current_index`. |
| `activate_shield` | If `player.advantages > 0`: `advantages -= 1`, `shield_active = True`, return `True`. Else: return `False`. |
| `ai_decision` | If `turn_total == 0`: return `'r'`. Else: `random.choice(['r', 'h'])`. |
| `ai_should_convert_six_to_shield` | Return `player.is_ai and player.advantages == 0 and not player.shield_active`. |
| `convert_six_to_shield` | `player.advantages = 1`, `player.shield_active = True`. |
| `current_player` | Return `self.players[self.current_index]`. |
| `winner` | If `game_over`: return player with score ≥ target. Else: return `None`. |
| `play` | Print header via `self.display`. Loop while not game_over: print scoreboard, prompt human / auto-decide AI, call `roll()`/`hold()`, display results via `self.display` methods. |

---

### Step 4: `PigDisplay` Class (Coloured Output Helper)

Create `pig_display.py` in `PigDiceHW/`. This is an **instance-based display helper** - instantiate with color/style defaults, then call its methods for coloured output.

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
        pass

    def print_header(self, text: str):
        """Print a coloured banner with lines and centred text."""
        pass

    def print_scoreboard(self, p1, p2):
        """Display both players' scores and advantages.

        Example output:
            Score: Player 1 = 3 (🛡️:1), Player 2 = 10 (🛡️:0)
        """
        pass

    def print_die_roll(self, value: int, turn_total: int):
        """Show the die roll result and updated turn total.

        Example output:
            Rolled: 🎲 5  → turn total = 5
        """
        pass

    def print_pig_out(self):
        """Show pig-out message in red.

        Example output:
            Rolled: 🎲 1  → 🐷 PIG! Lost all turn points.
        """
        pass

    def print_banked(self, banked: int):
        """Show banked points in green.

        Example output:
            ✅ Banked 10 points!
        """
        pass

    def print_winner(self, name: str, score: int):
        """Show the winner in bright green."""
        pass

    def print_ai_message(self, decision: str):
        """Show the AI's choice in yellow.

        Example output:
            🤖 AI chooses to roll.
        """
        pass

    def print_shield_offer(self, advantages: int):
        """Prompt the player to use a shield on rolling a 6."""
        pass

    def print_shield_activated(self, advantages: int):
        """Show shield activation message in blue."""
        pass

    def print_shield_saved(self, half: int):
        """Show that the shield halved the damage from rolling a 1."""
        pass

    def print_no_advantages(self):
        """Show message when player has no advantages left."""
        pass
```

| Method | Algorithm |
|--------|-----------|
| `__init__` | Store all color/style parameters as instance attributes (`self.header_color`, `self.text_color`, etc.). |
| `print_header` | `self.header_color + self.bright_style + "=" * 50`, `self.text_color + self.bright_style + text.center(50)`, same footer. |
| `print_scoreboard` | `self.header_color + f"Score: {p1.name} = {p1.score} (🛡️:{p1.advantages}), {p2.name} = {p2.score} (🛡️:{p2.advantages})"`. |
| `print_die_roll` | `self.text_color + f"Rolled: 🎲 {value}  → turn total = {turn_total}"`. |
| `print_pig_out` | `self.danger_color + "Rolled: 🎲 1  → 🐷 PIG! Lost all turn points."`. |
| `print_banked` | `self.success_color + f"✅ Banked {banked} points!"`. |
| `print_winner` | `self.success_color + self.bright_style + f"\n🏆 {name} wins with {score} points!"`. |
| `print_ai_message` | `self.ai_color + f"🤖 AI chooses to {choice_text}."`. |
| `print_shield_offer` | `self.header_color + f"🛡️ Rolled 6! Activate shield? (y/n): "` (no newline). |
| `print_shield_activated` | `self.info_color + f"🛡️ Shield active! (advantages left: {n})"`. |
| `print_shield_saved` | `self.info_color + f"🛡️ Shield saved you! Turn total halved to {n}."`. |
| `print_no_advantages` | `self.danger_color + "❌ No advantages left! 6 added normally."`. |

---

### Step 5: `Menu` Class - Fully Implemented ✅

Create `menu.py` in `PigDiceHW/`.

```python
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
        print(Fore.GREEN + f"\u2713 {msg}")

    def _print_error(self, msg: str):
        print(Fore.RED + f"\u2717 {msg}")

    def _print_info(self, msg: str):
        print(Fore.BLUE + f"\u2139 {msg}")

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
```

---

## ✅ Final Integration

```python
from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    menu.run()
```

---

## 📌 Evaluation Criteria

| Criterion | What to check |
|-----------|---------------|
| `Player` class | `score`, `turn_total`, `advantages` (default 0), `shield_active`, `reset_turn()`. |
| `Dice.roll()` | Returns int 1–6. |
| `PigGame.roll()` | If 1+shield: `ceil(turn_total/2)` + clear. If 1+no shield: pig-out+switch. If 2-6: add. |
| `PigGame.hold()` | Banks turn_total, checks win, switches player. |
| `PigGame.activate_shield()` | Decrements advantages, sets shield_active, returns True/False. |
| `PigGame.ai_decision()` | Returns `'r'` if turn_total==0, else random `'r'`/`'h'`. |
| `PigGame.ai_should_convert_six_to_shield()` | True if AI has 0 advantages and no active shield. |
| `PigGame.convert_six_to_shield()` | Sets advantages=1, shield_active=True. |
| `PigGame.winner` | Returns correct player or `None`. |
| Player 2 is AI | Created with `is_ai=True`, auto-decides roll/hold. Converts first 6 to shield. |
| Shield offer on 6 | Human prompted when rolling 6 with advantages > 0. AI auto-converts. |
| Shield undoes the 6 | If shield activated, the 6 is NOT added to turn total. |
| `PigGame.play()` | Full game loop, coloured output via `self.display` (PigDisplay), human prompt for P1, AI auto-play for P2. |
| `PigDisplay` | Instance-based. Constructor stores color/style defaults. Methods use `self.*_color` attributes. |
| `Menu` works | Starts games, changes target score, exits cleanly. |
| Input validation | Rejects invalid roll/hold choices. |
