# Pig Dice Game — Homework

## What You'll Build

You vs the AI. Roll the die. Risk it all — or bank your points. A 6 can buy you a shield. A 1… well, that's pig-out.

You'll create **4 Python files**, two of which are fully written (just copy-paste). The other two you'll build **method by method**, testing each one immediately before moving on.

**Along the way you'll see:**
- Text charts and tables that explain what each method needs to do
- The `Display` helper printing your player's state in colour
- Every method tested right after you write it

---

## Files You Need

Create these 4 files in your `PigDiceHW/` folder:

| File | What to do |
|------|------------|
| `display.py` | **Copy-paste** — fully provided |
| `player.py` | **Build yourself** — step by step |
| `pig_game.py` | **Build yourself** — step by step |
| `menu.py` | **Copy-paste** — fully provided |

---

## 1. Display Helper — Copy This

Create `display.py` and paste this exactly. This class handles all coloured output so you can focus on game logic.

```python
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
```

No tests needed — it just works.

---

## 2. Build Player — Method by Method

Open `player.py`. Start with an empty file. We'll add one thing at a time.

### 2a. `__init__`

**What we need**

Every player stores 6 things:

```
┌──────────────┬──────────┬────────────────────────────────────┐
│ Attribute    │ Type     │ What it's for                      │
├──────────────┼──────────┼────────────────────────────────────┤
│ name         │ str      │ Display name ("Player 1", "Bot")   │
│ is_ai        │ bool     │ True if computer-controlled        │
│ score        │ int      │ Total banked points (starts at 0)  │
│ turn_total   │ int      │ Points this turn (starts at 0)     │
│ advantages   │ int      │ Shields available (starts at 0)    │
│ shield_active│ bool     │ Is a shield currently protecting?  │
└──────────────┴──────────┴────────────────────────────────────┘
```

**Write the code**

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
```

**Test it**

Add this at the bottom and run `python player.py`:

```python
if __name__ == "__main__":
    from display import Display
    d = Display()

    d.print_header("TEST: PLAYER __init__")
    p = Player("Alice")
    print(repr(p))
    print()

    ai = Player("Bot", is_ai=True)
    print(repr(ai))
```

Expected output (colours may vary):
```
==================================================
           TEST: PLAYER __init__
==================================================
Player(Alice, score=0, turn=0, adv=0, 🔓)

Player(Bot, score=0, turn=0, adv=0, 🔓)
```

Every field is set correctly — ✓!

---

### 2b. `__repr__`

**What we need**

When you `print(repr(p))` you want to see the player's whole state at a glance. We'll add a `__repr__` method that Python calls automatically.

Show a shield emoji if shield is active, a lock otherwise.

**Write the code**

Add this method inside the class (after `__init__`):

```python
    def __repr__(self):
        shield = "\U0001f6e1\ufe0f" if self.shield_active else "\U0001f513"
        return (f"Player({self.name}, score={self.score}, "
                f"turn={self.turn_total}, adv={self.advantages}, {shield})")
```

**Test it**

You already tested it above! Rerun `python player.py` — same expected output.

---

### 2c. `reset_turn`

**What we need**

When a player banks their points or pigs-out, the turn total goes back to 0. That's all this method does.

```
  ┌─────────────┐
  │ turn_total  │
  │    = 15     │
  └──────┬──────┘
         │ reset_turn()
         ▼
  ┌─────────────┐
  │ turn_total  │
  │    = 0      │
  └─────────────┘
```

**Write the code**

```python
    def reset_turn(self):
        """Reset turn_total to 0 after hold or pig-out."""
        self.turn_total = 0
```

**Test it**

Update the test block:

```python
if __name__ == "__main__":
    from display import Display
    d = Display()

    d.print_header("TEST: PLAYER __init__")
    p = Player("Alice")
    print(repr(p))

    ai = Player("Bot", is_ai=True)
    print(repr(ai))

    d.print_header("TEST: reset_turn")
    p.turn_total = 15
    print(f"Before reset: turn_total = {p.turn_total}")  # 15
    p.reset_turn()
    print(f"After reset:  turn_total = {p.turn_total}")  # 0
```

Run it:
```
python player.py
```

The second header shows "Before" (15) and "After" (0). Player done! ✓

---

## 3. Menu Helper — Copy This

Create `menu.py` and paste this exactly:

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
```

Don't run it yet — `PigGame` doesn't exist. We'll build it next.

---

## 4. Build PigGame — The Main Event

Open `pig_game.py`. Start empty. First, add the imports and class skeleton:

```python
import math
import random
import time
from player import Player
from display import Display


class PigGame:
    """All game logic + game loop. Uses Display for coloured output."""

    def __init__(self, target_score: int = 20):
        pass

    def _roll_die(self) -> int:
        pass

    def roll(self) -> int:
        pass

    def hold(self):
        pass

    def switch_player(self):
        pass

    def activate_shield(self) -> bool:
        pass

    def ai_decision(self) -> str:
        pass

    def ai_should_convert_six_to_shield(self) -> bool:
        pass

    def convert_six_to_shield(self):
        pass

    @property
    def current_player(self):
        pass

    @property
    def winner(self):
        pass

    def play(self):
        pass
```

Now we'll implement and test each method, one at a time.

---

### 4a. `__init__`

**What we need**

PigGame owns everything. It needs:

```
┌──────────────────┬──────────────────────────────────────────┐
│ self.target_score│ Points needed to win (default 20)        │
│ self.players     │ [Player("Player 1"), Player("Player 2"   │
│                  │   , is_ai=True)]                         │
│ self.display     │ Display() — coloured output helper       │
│ self.current_idx │ 0 (Player 1 starts)                     │
│ self.game_over   │ False                                    │
└──────────────────┴──────────────────────────────────────────┘
```

**Write the code**

```python
    def __init__(self, target_score: int = 20):
        self.target_score = target_score
        self.players = [Player("Player 1"), Player("Player 2", is_ai=True)]
        self.display = Display()
        self.current_index = 0
        self.game_over = False
```

**Test it**

Add this test block below the class:

```python
if __name__ == "__main__":
    game = PigGame()
    game.display.print_header("TEST: PigGame __init__")
    print(f"Target: {game.target_score}")               # 20
    print(f"Players: {[p.name for p in game.players]}") # ['Player 1', 'Player 2']
    print(f"Player 2 is AI: {game.players[1].is_ai}")   # True
    print(f"Game over: {game.game_over}")               # False
    print()
    game.display.print_scoreboard(game.players[0], game.players[1])
```

Run `python pig_game.py`. You'll see the header "TEST: PigGame __init__" in colour, then the player names, AI status, and a scoreboard line.

---

### 4b. `_roll_die`

**What we need**

A six-sided die. One method. Returns 1, 2, 3, 4, 5, or 6.

```
   ┌────────────┐
   │  random    │
   │ .randint   │────► 1 | 2 | 3 | 4 | 5 | 6
   │ (1, 6)     │
   └────────────┘
```

**Write the code**

```python
    def _roll_die(self) -> int:
        return random.randint(1, 6)
```

**Test it**

Update the test block:

```python
if __name__ == "__main__":
    game = PigGame()

    # --- __init__ ---
    game.display.print_header("TEST: PigGame __init__")
    print(f"Target: {game.target_score}")
    print(f"Players: {[p.name for p in game.players]}")
    print(f"Player 2 is AI: {game.players[1].is_ai}")
    print(f"Game over: {game.game_over}")
    print()
    game.display.print_scoreboard(game.players[0], game.players[1])

    # --- _roll_die ---
    game.display.print_header("TEST: _roll_die")
    for i in range(10):
        val = game._roll_die()
        assert 1 <= val <= 6, f"Bad roll: {val}"
        print(f"  Roll {i+1}: {val}")
    print("All 10 rolls are between 1 and 6 — ✓")
```

Run it. All 10 rolls should be in range.

---

### 4c. `current_player` property

**What we need**

A property that returns whichever player is currently active.

```
self.current_index = 0  ──►  game.current_player = self.players[0] = Player 1
self.current_index = 1  ──►  game.current_player = self.players[1] = Player 2
```

**Write the code**

```python
    @property
    def current_player(self):
        return self.players[self.current_index]
```

**Test it**

```python
if __name__ == "__main__":
    game = PigGame()

    # --- __init__ ---
    game.display.print_header("TEST: PigGame __init__")
    print(f"Target: {game.target_score}")
    print(f"Players: {[p.name for p in game.players]}")
    print(f"Player 2 is AI: {game.players[1].is_ai}")
    print(f"Game over: {game.game_over}")
    print()
    game.display.print_scoreboard(game.players[0], game.players[1])

    # --- _roll_die ---
    game.display.print_header("TEST: _roll_die")
    for i in range(5):
        print(f"  Roll {i+1}: {game._roll_die()}")
    print()

    # --- current_player ---
    game.display.print_header("TEST: current_player")
    print(repr(game.current_player))
```

---

### 4d. `switch_player`

**What we need**

Toggle between the two players:

```
current_index = 0  ──► switch_player() ──► current_index = 1
current_index = 1  ──► switch_player() ──► current_index = 0
```

A simple trick: `self.current_index = 1 - self.current_index`

**Write the code**

```python
    def switch_player(self):
        self.current_index = 1 - self.current_index
```

**Test it**

```python
    # --- switch_player ---
    game.display.print_header("TEST: switch_player")
    print(f"Before: {game.current_player.name}")     # Player 1
    game.switch_player()
    print(f"After:  {game.current_player.name}")     # Player 2
    game.switch_player()
    print(f"Back:   {game.current_player.name}")     # Player 1
```

---

### 4e. `ai_decision`

**What we need**

The AI is simple:
- If turn_total is 0 → always roll (can't bank zero!)
- If turn_total > 0 → randomly pick 'r' or 'h'

```
            ┌──────────────┐
            │ turn_total   │
            │   == 0 ?     │
            └──────┬───────┘
               Yes │           No
                   ▼            ▼
               return 'r'    random.choice(['r', 'h'])
```

**Write the code**

```python
    def ai_decision(self) -> str:
        if self.current_player.turn_total == 0:
            return 'r'
        return random.choice(['r', 'h'])
```

**Test it**

```python
    # --- ai_decision ---
    game.display.print_header("TEST: ai_decision")
    game.switch_player()  # go to Player 2 (AI)
    game.current_player.turn_total = 0
    print(f"At turn_total=0: {game.ai_decision()}")   # always 'r'
    game.current_player.turn_total = 10
    print(f"At turn_total=10: {game.ai_decision()}")  # 'r' or 'h'
    print(f"At turn_total=10: {game.ai_decision()}")  # 'r' or 'h'
```

---

### 4f. `activate_shield`

**What we need**

Spend 1 advantage to turn on the shield. Return True if activated, False if no advantages left.

```
advantages > 0 ?
    Yes ──► advantages -= 1, shield_active = True, return True
    No  ──► return False
```

**Write the code**

```python
    def activate_shield(self) -> bool:
        player = self.current_player
        if player.advantages > 0:
            player.advantages -= 1
            player.shield_active = True
            return True
        return False
```

**Test it**

```python
    # --- activate_shield ---
    game.display.print_header("TEST: activate_shield")
    game.switch_player()  # back to Player 1
    game.players[0].advantages = 2
    print(f"Before: {repr(game.players[0])}")
    r1 = game.activate_shield()
    print(f"Activated: {r1}")                              # True
    print(f"After 1st: {repr(game.players[0])}")           # adv=1, shield=True
    r2 = game.activate_shield()
    print(f"Activated: {r2}")                              # True
    print(f"After 2nd: {repr(game.players[0])}")           # adv=0, shield=True
    r3 = game.activate_shield()
    print(f"Activated: {r3}")                              # False
    print(f"After 3rd: {repr(game.players[0])}")           # unchanged
```

---

### 4g. `ai_should_convert_six_to_shield`

**What we need**

The AI keeps **one** shield. If it has 0 advantages and no active shield, the first 6 it rolls should be converted.

Condition:
- Player is AI
- advantages == 0
- shield_active == False

All three must be True.

**Write the code**

```python
    def ai_should_convert_six_to_shield(self) -> bool:
        player = self.current_player
        return player.is_ai and player.advantages == 0 and not player.shield_active
```

**Test it**

```python
    # --- ai_should_convert_six_to_shield ---
    game.display.print_header("TEST: ai_should_convert_6")
    game.switch_player()  # to Player 2 (AI)
    game.players[1].advantages = 0
    game.players[1].shield_active = False
    print(f"0 adv, no shield: {game.ai_should_convert_six_to_shield()}")  # True
    game.players[1].advantages = 1
    print(f"Has adv:          {game.ai_should_convert_six_to_shield()}")  # False
    game.players[1].advantages = 0
    game.players[1].shield_active = True
    print(f"Shield on:        {game.ai_should_convert_six_to_shield()}")  # False
```

---

### 4h. `convert_six_to_shield`

**What we need**

Give the AI 1 advantage and activate the shield. The game loop (in `play()`) will also undo the 6 from turn_total.

```
advantages = 1
shield_active = True
```

**Write the code**

```python
    def convert_six_to_shield(self):
        player = self.current_player
        player.advantages = 1
        player.shield_active = True
```

**Test it**

```python
    # --- convert_six_to_shield ---
    game.display.print_header("TEST: convert_six_to_shield")
    game.players[1].advantages = 0
    game.players[1].shield_active = False
    print(f"Before: {repr(game.players[1])}")            # adv=0, shield=False
    game.convert_six_to_shield()
    print(f"After:  {repr(game.players[1])}")            # adv=1, shield=True
```

---

### 4i. `roll`

**What we need**

This is the core mechanic. Roll the die, then react:

```
        ┌──────────┐
        │_roll_die │
        └────┬─────┘
             ▼
       ┌─────────┐
       │ value   │
       │ == 1 ?  │
       └────┬────┘
        Yes │         No
            ▼               ▼
    ┌──────────────┐    add value to
    │shield_active?│    turn_total
    └──────┬───────┘
       Yes │       No
          ▼          ▼
   turn_total =     reset_turn()
   ceil(total/2)    switch_player()
   shield_active
     = False
```

**Write the code**

```python
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
```

**Test it**

```python
    # --- roll ---
    game.display.print_header("TEST: roll")
    game2 = PigGame()
    for i in range(5):
        val = game2.roll()
        print(f"  Roll {i+1}: {val}, {repr(game2.current_player)}")

    # Test shield scenario (set up and roll once)
    game3 = PigGame()
    game3.players[0].shield_active = True
    game3.players[0].turn_total = 10
    print(f"\nShield test setup: {repr(game3.players[0])}")
    val = game3.roll()
    outcome = "shield saved!" if val == 1 else f"rolled {val} normally"
    print(f"After roll ({outcome}): {repr(game3.players[0])}")
```

---

### 4j. `hold`

**What we need**

Bank the turn points, check for a winner, switch players if the game continues.

```
┌──────────────┐
│ score +=     │
│ turn_total   │
└──────┬───────┘
       ▼
┌──────────────┐
│ reset_turn() │
└──────┬───────┘
       ▼
┌──────────────────┐
│ score >= target? │
└──────┬───────────┘
   Yes │             No
       ▼                 ▼
 game_over = True    switch_player()
```

**Write the code**

```python
    def hold(self):
        player = self.current_player
        player.score += player.turn_total
        player.reset_turn()
        if player.score >= self.target_score:
            self.game_over = True
        else:
            self.switch_player()
```

**Test it**

```python
    # --- hold ---
    game.display.print_header("TEST: hold")
    game4 = PigGame()
    game4.players[0].turn_total = 15
    print(f"Before hold: {repr(game4.players[0])}")
    game4.hold()
    print(f"After hold:  {repr(game4.players[0])}")     # score=15, turn=0
    print(f"Next player: {game4.current_player.name}")   # Player 2
    print(f"Game over:   {game4.game_over}")             # False

    # Win scenario
    game5 = PigGame(target_score=10)
    game5.players[0].turn_total = 12
    game5.hold()
    print(f"\nWin: game_over={game5.game_over}")          # True
    print(f"Winner: {game5.winner.name}")                 # Player 1
```

---

### 4k. `winner` property

**What we need**

When the game is over, return the player who reached (or passed) the target. Otherwise return None.

**Write the code**

```python
    @property
    def winner(self):
        if self.game_over:
            for p in self.players:
                if p.score >= self.target_score:
                    return p
        return None
```

(You already used `game5.winner` in the last test — it should have worked!)

---

### 4l. `play` — The Game Loop

**What we need**

The full game loop. Here's the flowchart:

```
1. Print header ("PIG DICE")
2. Print "Target: X points"

3. Loop while not game_over:
   │
   ├── Print scoreboard
   ├── Print "--- Player X's turn ---"
   │
   ├── Loop while not game_over:
   │   │
   │   ├── If AI: ai_decision() → auto-play
   │   │
   │   ├── If human: prompt "(r)oll or (h)old?"
   │   │
   │   ├── If 'r':
   │   │   roll()
   │   │   │
   │   │   ├── value == 1 with shield  → print_shield_saved()
   │   │   ├── value == 1 without      → print_pig_out(), break
   │   │   ├── value == 6:
   │   │   │   ├── human + adv > 0     → offer shield, y/n
   │   │   │   ├── AI first 6          → auto-convert
   │   │   │   ├── shield used         → subtract 6, print activated
   │   │   │   └── no shield           → print_die_roll()
   │   │   ├── value 2-5               → print_die_roll()
   │   │   └── AI turn → continue
   │   │
   │   ├── If 'h':
   │   │   hold(), print_banked(), break
   │   │
   │   └── If invalid: show error
   │
4. Print winner
```

That's a lot! Here's the complete code — read it through, then paste it:

```python
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

No test for `play()` — you'll see it in action when you run the game!

---

### 🧹 Clean Up the Test Code

Before the final run, **remove the entire `if __name__` block** from `pig_game.py`. Your file should be just the `PigGame` class with all its methods and no test code.

Keep the test block in `player.py` — it's small and harmless.

---

## 5. Run the Game!

Create `main.py` in the same folder:

```python
from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    menu.run()
```

Then run it:

```
python main.py
```

You'll see the menu. Hit **1** to start. Roll, hold, buy shields, and try to beat the AI!

---

## How It Should Look

```
==================================================
             PIG DICE GAME
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
Rolled:  5  -> turn total = 5
(r)oll or (h)old? r
Rolled:  6
Rolled 6! Activate shield? (y/n): y
Shield active! Turn total stays at 5 (advantages left: 1)
(r)oll or (h)old? r
Rolled:  1
Shield saved you! Turn total halved to 3.
(r)oll or (h)old? h
Banked 3 points!
Score: Player 1 = 3 (:1), Player 2 = 0 (:0)

--- Player 2's turn (AI) ---
AI chooses to roll.
Rolled:  6
AI converts first 6 to a shield! (advantages: 1)
AI chooses to roll.
Rolled:  4  -> turn total = 4
AI chooses to roll.
Rolled:  6  -> turn total = 10
AI chooses to hold.
Banked 10 points!
Score: Player 1 = 3 (:1), Player 2 = 10 (:1)
...
```

## Stuck? Check the Solution

Full implementations of all files are in the `solution/` folder. Peek if you get stuck, but try to write the code yourself first!

---

## Evaluation Checklist

| Criterion | What to check |
|-----------|---------------|
| `Player.__init__` | Sets all 6 attributes correctly |
| `Player.__repr__` | Shows name, score, turn, adv, shield emoji |
| `Player.reset_turn` | Sets turn_total to 0 |
| `PigGame.__init__` | Creates 2 players, Display, sets indices |
| `PigGame._roll_die` | Returns int 1-6 |
| `PigGame.current_player` | Returns correct player |
| `PigGame.switch_player` | Toggles between 0 and 1 |
| `PigGame.ai_decision` | Always 'r' at 0, else random |
| `PigGame.activate_shield` | Decrements advantages, returns True/False |
| `PigGame.ai_should_convert_six_to_shield` | True only when AI has 0 adv and no shield |
| `PigGame.convert_six_to_shield` | Sets advantages=1, shield_active=True |
| `PigGame.roll` | Handles 1+shield (halve), 1 (pig-out), 2-6 (add) |
| `PigGame.hold` | Banks score, checks win, switches |
| `PigGame.winner` | Returns player or None |
| `PigGame.play` | Full loop with all display calls |
| Shield offer on 6 | Human prompted when rolling 6 with advantages |
| Shield undoes the 6 | 6 NOT added to turn_total when shield activated |
| AI auto-converts first 6 | AI's first 6 becomes a shield |
| `display.py` | Present and correctly imported |
| `menu.py` | Present, runs game on option 1 |
