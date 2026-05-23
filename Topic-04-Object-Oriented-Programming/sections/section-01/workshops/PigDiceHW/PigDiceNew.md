# 🎲 Pig Dice Game — Complete OOP Workshop

## 📚 Table of Contents
1. [Introduction & Game Rules](#introduction)
2. [Project Architecture](#architecture)
3. [Setting Up the Project](#setup)
4. [Building Display Helper](#display)
5. [Building Player Class (Step-by-Step)](#player)
6. [Building PigGame Class (Step-by-Step)](#piggame)
7. [Building Menu System](#menu)
8. [Running the Complete Game](#running)
9. [Final Review & OOP Concepts](#review)

---

<a name="introduction"></a>
## 1. 🎯 Introduction & Game Rules

### What is Pig Dice?

Pig is a two-player dice game where you race to reach a target score (default: 20 points). On your turn, you can roll a die as many times as you want, accumulating points. But beware: if you roll a **1**, you lose all points for that turn!

### Core Mechanics

**Basic Rules:**
- Roll the die to add points to your **turn total**
- Choose to **hold** to bank your turn total into your permanent score
- Rolling a **1** = **Pig-out!** You lose all turn points and your turn ends
- First player to reach the target score wins

**Advanced Mechanics (Shields):**
- Rolling a **6** gives you a choice: add 6 points OR activate a **shield**
- A shield costs 1 **advantage** (you start with 0)
- When you activate a shield, you gain 1 advantage and the shield becomes active
- If you pig-out with an active shield, you only lose **half** your turn total (rounded up)
- The AI automatically converts its **first 6** into a shield

### Example Game Flow

Round 1 — You (0) vs AI (0)
Score: You = 0 (🛡️:0), AI = 0 (🛡️:0)

(r)oll or (h)old? r
Rolled: 🎲 4  → turn total = 4

(r)oll or (h)old? r
Rolled: 🎲 6  → turn total = 10
🛡️ Rolled 6! Activate shield? (y/n): y
🛡️ Shield active! Turn total protected (advantages left: 0)

(r)oll or (h)old? r
Rolled: 🎲 1  → 🐷 PIG!
🛡️ Shield saved you! Turn total halved to 5.

Score: You = 5 (🛡️:0), AI = 0 (🛡️:0)

🤖 AI chooses to roll.
Rolled: 🎲 6  → turn total = 6
🛡️ AI converted first 6 into a shield!

🤖 AI chooses to roll.
Rolled: 🎲 5  → turn total = 5

🤖 AI chooses to roll.
Rolled: 🎲 3  → turn total = 8

🤖 AI chooses to hold.
✅ Banked 8 points!

Score: You = 5 (🛡️:0), AI = 8 (🛡️:0)


---

<a name="architecture"></a>
## 2. 🏗️ Project Architecture

### File Structure

PigDiceHW/
├── display.py      # Helper class for colored console output
├── player.py       # Player data and behavior (YOU BUILD THIS)
├── pig_game.py     # Game logic and rules (YOU BUILD THIS)
├── menu.py         # Interactive menu system
└── main.py         # Entry point


### Class Diagram

┌─────────────────────────────────────────────────────────────────┐
│                    PIG DICE GAME — ARCHITECTURE                 │
└─────────────────────────────────────────────────────────────────┘

┌──────────────────┐
│     Display      │  ← Helper for colored output
├──────────────────┤
│ +header_color    │
│ +text_color      │
│ +success_color   │
│ +danger_color    │
│ +info_color      │
├──────────────────┤
│ +print_header()  │  Print game headers
│ +print_scoreboard│  Show current scores
│ +print_die_roll()│  Show dice results
│ +print_pig_out() │  Show pig-out message
│ +print_banked()  │  Show banked points
│ +print_winner()  │  Show game winner
│ +print_ai_msg()  │  Show AI decisions
│ +print_shield_*()│  Shield-related messages
└──────────────────┘
         ▲
         │ uses
         │
┌────────┴─────────┐
│     PigGame      │  ← Main game controller
├──────────────────┤
│ -target_score    │  Win condition
│ -players: list   │  [Player, Player]
│ -display         │  Display instance
│ -current_index   │  0 or 1 (whose turn)
│ -game_over       │  Boolean flag
│ -round_number    │  Current round
├──────────────────┤
│ +__init__()      │  Setup game
│ -_roll_die()     │  Random 1-6
│ +roll()          │  Handle roll outcomes
│ +hold()          │  Bank points
│ +switch_player() │  Toggle turns
│ +activate_shield │  Use advantage
│ +ai_decision()   │  AI strategy
│ +play()          │  Main game loop
│                  │
│ Properties:      │
│ +current_player  │  Get active player
│ +winner          │  Get winner if game over
└────────┬─────────┘
         │ owns 2
         ▼
┌──────────────────┐
│     Player       │  ← Player state
├──────────────────┤
│ +name: str       │  "You" or "AI"
│ +is_ai: bool     │  AI flag
│ +score: int      │  Permanent score
│ +turn_total: int │  Current turn points
│ +advantages: int │  Shield charges
│ +shield_active   │  Shield status
├──────────────────┤
│ +__init__()      │  Create player
│ +__repr__()      │  String representation
│ +reset_turn()    │  Clear turn_total
└──────────────────┘

┌──────────────────┐
│      Menu        │  ← User interface
├──────────────────┤
│ -target_score    │  Configurable target
│ -pig_game        │  PigGame instance
├──────────────────┤
│ +run()           │  Main menu loop
│ +start_new_game()│  Create & play game
│ +set_target_*()  │  Configure target
└──────────────────┘


### Design Principles

**Separation of Concerns:**
- `Display` → Handles ALL output formatting
- `Player` → Manages player state (score, shields, etc.)
- `PigGame` → Implements game rules and flow
- `Menu` → Provides user interface

**Encapsulation:**
- Private methods start with `_` (e.g., `_roll_die`)
- Properties use `@property` decorator for computed values
- Each class protects its own data

**Composition:**
- `PigGame` *has-a* `Display` (not inheritance)
- `PigGame` *has-a* list of `Player` objects
- Objects work together through well-defined interfaces

---

<a name="setup"></a>
## 3. 🛠️ Setting Up the Project

### Step 1: Create Project Directory

```bash
mkdir PigDiceHW
cd PigDiceHW
```

### Step 2: Install Dependencies

```bash
pip install colorama
```

**What is colorama?**
- Cross-platform library for colored terminal output
- Works on Windows, Mac, Linux
- Makes our game visually appealing

### Step 3: Create Empty Files

```bash
touch display.py player.py pig_game.py menu.py main.py
```

Now let's build each file step-by-step!

---

<a name="display"></a>
## 4. 🎨 Building Display Helper

The `Display` class is a **helper** that handles all colored output. This separates presentation logic from game logic.

### Why a Display Class?

**Without Display class:**
```python
# Scattered color codes everywhere
print(Fore.RED + "Pig out!" + Style.RESET_ALL)
print(Fore.GREEN + f"Banked {points}" + Style.RESET_ALL)
```

**With Display class:**
```python
# Clean, reusable methods
display.print_pig_out()
display.print_banked(points)
```

### Complete display.py

**Copy this entire file:**

```python
from colorama import init, Fore, Style

init(autoreset=True)


class Display:
    """Helper class for coloured game output.
    
    This class encapsulates all presentation logic, keeping game logic clean.
    Each method handles a specific type of output with consistent formatting.
    """

    def __init__(self, header_color=Fore.CYAN, text_color=Fore.YELLOW,
                 success_color=Fore.GREEN, danger_color=Fore.RED,
                 info_color=Fore.BLUE, bright_style=Style.BRIGHT):
        """Initialize display with customizable color scheme."""
        self.header_color = header_color
        self.text_color = text_color
        self.success_color = success_color
        self.danger_color = danger_color
        self.info_color = info_color
        self.bright_style = bright_style

    def print_header(self, text: str):
        """Print a centered header with decorative borders."""
        print(self.header_color + self.bright_style + "=" * 50)
        print(self.text_color + self.bright_style + text.center(50))
        print(self.header_color + self.bright_style + "=" * 50)

    def print_scoreboard(self, p1, p2):
        """Display current scores and advantages for both players."""
        print(self.header_color + 
              f"Score: {p1.name} = {p1.score} (\U0001f6e1\ufe0f:{p1.advantages}), "
              f"{p2.name} = {p2.score} (\U0001f6e1\ufe0f:{p2.advantages})")

    def print_die_roll(self, value: int, turn_total: int):
        """Show dice roll result and updated turn total."""
        print(self.text_color + 
              f"Rolled: \U0001f3b2 {value}  \u2192 turn total = {turn_total}")

    def print_pig_out(self):
        """Display pig-out message (rolled a 1)."""
        print(self.danger_color + 
              "Rolled: \U0001f3b2 1  \u2192 \U0001f437 PIG! Lost all turn points.")

    def print_banked(self, banked: int):
        """Show successfully banked points."""
        print(self.success_color + f"\u2705 Banked {banked} points!")

    def print_winner(self, name: str, score: int):
        """Display game winner with trophy emoji."""
        print(self.success_color + self.bright_style + 
              f"\n\U0001f3c6 {name} wins with {score} points!")

    def print_ai_message(self, decision: str):
        """Show AI's decision (roll or hold)."""
        text = "roll" if decision == "r" else "hold"
        print(self.text_color + f"\U0001f916 AI chooses to {text}.")

    def print_shield_offer(self):
        """Prompt human player to activate shield after rolling 6."""
        print(self.info_color + 
              "\U0001f6e1\ufe0f Rolled 6! Activate shield? (y/n): ", end="")

    def print_shield_activated(self, advantages: int):
        """Confirm shield activation and show remaining advantages."""
        print(self.info_color + 
              f"\U0001f6e1\ufe0f Shield active! Turn total protected "
              f"(advantages left: {advantages})")

    def print_shield_saved(self, half: int):
        """Show shield protection effect (halved turn total)."""
        print(self.info_color + 
              f"\U0001f6e1\ufe0f Shield saved you! Turn total halved to {half}.")

    def print_no_advantages(self):
        """Inform player they have no advantages left."""
        print(self.danger_color + 
              "\u274c No advantages left! 6 added to turn total normally.")

    def print_ai_converted_shield(self):
        """Show AI converting first 6 into a shield."""
        print(self.info_color + 
              "\U0001f6e1\ufe0f AI converted first 6 into a shield!")
```

### Key Concepts

**1. Encapsulation:**
- All color codes are hidden inside the class
- Game logic never needs to know about `Fore.RED` or `Style.BRIGHT`

**2. Single Responsibility:**
- This class has ONE job: format and display messages
- It doesn't know anything about game rules

**3. Reusability:**
- Any game can use this Display class
- Easy to change colors without touching game logic

---

<a name="player"></a>
## 5. 👤 Building Player Class (Step-by-Step)

The `Player` class represents a player's **state** (data) and simple **behaviors** (methods that modify that data).

### Class Overview

Player
├── Data (Attributes)
│   ├── name: str          # "You" or "AI"
│   ├── is_ai: bool        # True for AI player
│   ├── score: int         # Permanent banked points
│   ├── turn_total: int    # Points accumulated this turn
│   ├── advantages: int    # Shield charges available
│   └── shield_active: bool # Is shield currently protecting?
│
└── Behaviors (Methods)
    ├── __init__()         # Initialize player
    ├── __repr__()         # String representation
    └── reset_turn()       # Clear turn_total


### Step 1: Create the File Structure

Open `player.py` and start with the class definition:

```python
class Player:
    """Represents a player with score, turn total, and shield mechanics.
    
    This class is a pure data container with minimal logic.
    It knows about player state but NOT about game rules.
    """
    pass  # We'll add methods one by one
```

---

### Step 2: Implement `__init__` Method

**What does `__init__` do?**
- Called automatically when you create a new Player: `p = Player("Alice")`
- Initializes all attributes with starting values
- Sets up the player's initial state

**Add this method:**

```python
    def __init__(self, name: str, is_ai: bool = False):
        """Initialize player with name and AI flag.
        
        Args:
            name: Player's display name ("You" or "AI")
            is_ai: True if this player is controlled by AI
        
        All players start with:
        - 0 score (no points banked yet)
        - 0 turn_total (no points accumulated this turn)
        - 0 advantages (no shield charges)
        - shield_active = False (no protection)
        """
        self.name = name
        self.is_ai = is_ai
        self.score = 0
        self.turn_total = 0
        self.advantages = 0
        self.shield_active = False
```

**Key Concepts:**

1. **Default Parameters:** `is_ai=False` means you can call:
   - `Player("Alice")` → `is_ai` defaults to `False`
   - `Player("Bot", True)` → `is_ai` is `True`

2. **Self:** Every instance method's first parameter is `self`
   - `self` refers to the specific Player object
   - `self.score` means "this player's score"

3. **Initialization:** All attributes get default values
   - Prevents errors from accessing uninitialized variables

**Test it:**

```python
# Add at the bottom of player.py
if __name__ == "__main__":
    # Create a human player
    alice = Player("Alice")
    print(f"Name: {alice.name}")
    print(f"Is AI: {alice.is_ai}")
    print(f"Score: {alice.score}")
    print(f"Turn total: {alice.turn_total}")
    print()
    
    # Create an AI player
    bot = Player("Bot", is_ai=True)
    print(f"Name: {bot.name}")
    print(f"Is AI: {bot.is_ai}")
```

**Run:**
```bash
python player.py
```

**Expected output:**
Name: Alice
Is AI: False
Score: 0
Turn total: 0

Name: Bot
Is AI: True


---

### Step 3: Implement `__repr__` Method

**What is `__repr__`?**
- Special method that defines how an object is represented as a string
- Called when you use `print(player)` or `repr(player)`
- Useful for debugging and logging

**Add this method:**

```python
    def __repr__(self):
        """String representation showing all player state.
        
        Returns a detailed view of the player's current state,
        including a visual indicator (emoji) for shield status.
        
        Example output:
        Player(Alice, score=15, turn=8, adv=1, 🛡️)
        Player(Bob, score=10, turn=0, adv=0, 🔓)
        """
        shield = "\U0001f6e1\ufe0f" if self.shield_active else "\U0001f513"
        return (f"Player({self.name}, score={self.score}, "
                f"turn={self.turn_total}, adv={self.advantages}, {shield})")
```

**Key Concepts:**

1. **Conditional Expression:** `x if condition else y`
   - If shield is active → show 🛡️ (shield emoji)
   - If shield is inactive → show 🔓 (unlocked emoji)

2. **F-strings:** `f"text {variable}"` embeds variables in strings
   - More readable than `"text " + str(variable)`

3. **Multi-line Strings:** Use parentheses to split long strings
   - Python automatically concatenates adjacent strings

**Update your test:**

```python
if __name__ == "__main__":
    from display import Display
    d = Display()
    
    d.print_header("TEST: Player __init__ and __repr__")
    
    # Create players
    alice = Player("Alice")
    bot = Player("Bot", is_ai=True)
    
    # Test __repr__
    print(repr(alice))
    print(repr(bot))
    print()
    
    # Modify state and test again
    alice.score = 15
    alice.turn_total = 8
    alice.advantages = 1
    alice.shield_active = True
    
    print("After modifications:")
    print(repr(alice))
```

**Run:**
```bash
python player.py
```

**Expected output:**
==================================================
     TEST: Player __init__ and __repr__
==================================================
Player(Alice, score=0, turn=0, adv=0, 🔓)
Player(Bot, score=0, turn=0, adv=0, 🔓)

After modifications:
Player(Alice, score=15, turn=8, adv=1, 🛡️)


---

### Step 4: Implement `reset_turn` Method

**What does `reset_turn` do?**
- Clears the `turn_total` back to 0
- Called after a player banks points (holds) or pigs out (rolls 1)
- Simple but essential for game flow

**Add this method:**

```python
    def reset_turn(self):
        """Reset turn_total to 0 after hold or pig-out.
        
        This method is called when:
        1. Player chooses to hold (bank their points)
        2. Player rolls a 1 (pig-out)
        
        It does NOT modify score, advantages, or shield status.
        Those are handled by the game logic in PigGame class.
        """
        self.turn_total = 0
```

**Key Concepts:**

1. **Single Responsibility:** This method does ONE thing
   - It doesn't check game rules
   - It doesn't switch players
   - It just resets one attribute

2. **Separation of Concerns:**
   - Player class: "I manage my own data"
   - PigGame class: "I decide WHEN to reset the turn"

**Update your test:**

```python
if __name__ == "__main__":
    from display import Display
    d = Display()
    
    d.print_header("TEST: Player Methods")
    
    # Test __init__ and __repr__
    alice = Player("Alice")
    print("Initial state:")
    print(repr(alice))
    print()
    
    # Test reset_turn
    d.print_header("TEST: reset_turn")
    alice.turn_total = 15
    print(f"Before reset: turn_total = {alice.turn_total}")
    alice.reset_turn()
    print(f"After reset:  turn_total = {alice.turn_total}")
    print(repr(alice))
```

**Run:**
```bash
python player.py
```

**Expected output:**
==================================================
           TEST: Player Methods
==================================================
Initial state:
Player(Alice, score=0, turn=0, adv=0, 🔓)

==================================================
              TEST: reset_turn
==================================================
Before reset: turn_total = 15
After reset:  turn_total = 0
Player(Alice, score=0, turn=0, adv=0, 🔓)


---

### Complete player.py

Here's the full file with all methods:

```python
class Player:
    """Represents a player with score, turn total, and shield mechanics."""

    def __init__(self, name: str, is_ai: bool = False):
        """Initialize player with name and AI flag."""
        self.name = name
        self.is_ai = is_ai
        self.score = 0
        self.turn_total = 0
        self.advantages = 0
        self.shield_active = False

    def __repr__(self):
        """String representation showing all player state."""
        shield = "\U0001f6e1\ufe0f" if self.shield_active else "\U0001f513"
        return (f"Player({self.name}, score={self.score}, "
                f"turn={self.turn_total}, adv={self.advantages}, {shield})")

    def reset_turn(self):
        """Reset turn_total to 0 after hold or pig-out."""
        self.turn_total = 0


# ─────────────────────────────────────────────────────────────────
# TESTS
# ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    from display import Display
    d = Display()

    d.print_header("TEST: Player __init__ and __repr__")
    alice = Player("Alice")
    bot = Player("Bot", is_ai=True)
    print(repr(alice))
    print(repr(bot))
    print()

    alice.score = 15
    alice.turn_total = 8
    alice.advantages = 1
    alice.shield_active = True
    print("After modifications:")
    print(repr(alice))
    print()

    d.print_header("TEST: reset_turn")
    alice.turn_total = 20
    print(f"Before reset: turn_total = {alice.turn_total}")
    alice.reset_turn()
    print(f"After reset:  turn_total = {alice.turn_total}")
```

### Player Class Summary

**What we learned:**

1. **Data Modeling:** Player class models a real-world entity
2. **Initialization:** `__init__` sets up starting state
3. **Representation:** `__repr__` helps with debugging
4. **Encapsulation:** Player manages its own data
5. **Simplicity:** Each method does one thing well

**OOP Principles Applied:**
- ✅ Encapsulation (data + methods together)
- ✅ Single Responsibility (each method has one job)
- ✅ Clear interface (simple, predictable methods)

---

<a name="piggame"></a>
## 6. 🎮 Building PigGame Class (Step-by-Step)

The `PigGame` class is the **brain** of our game. It implements all game rules, manages turns, and orchestrates the interaction between players and display.

### Class Overview

PigGame
├── Data (Attributes)
│   ├── target_score: int      # Win condition (default 20)
│   ├── players: list          # [Player("You"), Player("AI")]
│   ├── display: Display       # For colored output
│   ├── current_index: int     # 0 or 1 (whose turn)
│   ├── game_over: bool        # Has someone won?
│   └── round_number: int      # Current round counter
│
├── Core Game Methods
│   ├── __init__()             # Setup game
│   ├── _roll_die()            # Random 1-6
│   ├── roll()                 # Handle roll outcomes
│   ├── hold()                 # Bank points & switch
│   └── play()                 # Main game loop
│
├── Turn Management
│   ├── switch_player()        # Toggle current_index
│   ├── current_player (prop)  # Get active player
│   └── winner (property)      # Get winner if game over
│
├── Shield Mechanics
│   ├── activate_shield()      # Use advantage
│   ├── ai_should_convert_*()  # Check AI shield logic
│   └── convert_six_to_shield()# Grant AI first shield
│
└── AI Logic
    └── ai_decision()          # AI strategy


### Step 1: Create Class Structure

Open `pig_game.py` and start with imports and class definition:

```python
import math
import random
import time
from player import Player
from display import Display
from colorama import Fore, Style


class PigGame:
    """Main game logic with proper shield mechanics and AI behavior.
    
    This class orchestrates the entire game:
    - Manages two players (human vs AI)
    - Implements all game rules
    - Handles turn progression
    - Coordinates with Display for output
    """
    pass  # We'll add methods step-by-step
```

---

### Step 2: Implement `__init__` Method

**What does `__init__` do?**
- Sets up a new game with all necessary components
- Creates two players (human and AI)
- Initializes game state variables

**Add this method:**

```python
    def __init__(self, target_score: int = 20):
        """Initialize game with target score and two players.
        
        Args:
            target_score: Points needed to win (default 20)
        
        Creates:
        - Two Player objects: "You" (human) and "AI"
        - Display object for colored output
        - Game state tracking variables
        """
        self.target_score = target_score
        self.players = [Player("You"), Player("AI", is_ai=True)]
        self.display = Display()
        self.current_index = 0  # 0 = human's turn, 1 = AI's turn
        self.game_over = False
        self.round_number = 1
```

**Key Concepts:**

1. **Composition:** PigGame *has-a* Display and *has-a* list of Players
   - Not inheritance (PigGame is NOT a Display or Player)
   - Objects work together through their interfaces

2. **Default Parameters:** `target_score=20` allows:
   - `PigGame()` → target is 20
   - `PigGame(50)` → target is 50

3. **List of Objects:** `self.players` is a list containing Player objects
   - `self.players[0]` is the human player
   - `self.players[1]` is the AI player

**Test it:**

```python
# Add at the bottom of pig_game.py
if __name__ == "__main__":
    game = PigGame()
    
    print("=== TEST: PigGame __init__ ===")
    print(f"Target score: {game.target_score}")
    print(f"Number of players: {len(game.players)}")
    print(f"Player 1: {game.players[0].name} (AI: {game.players[0].is_ai})")
    print(f"Player 2: {game.players[1].name} (AI: {game.players[1].is_ai})")
    print(f"Current index: {game.current_index}")
    print(f"Game over: {game.game_over}")
    print(f"Round: {game.round_number}")
```

**Run:**
```bash
python pig_game.py
```

---

### Step 3: Implement `_roll_die` and `current_player`

**Two simple but essential methods:**

1. **`_roll_die()`:** Simulates rolling a six-sided die
2. **`current_player`:** Property that returns the active player

**Add these methods:**

```python
    def _roll_die(self) -> int:
        """Roll a six-sided die.
        
        Returns:
            Random integer from 1 to 6 (inclusive)
        
        Note: The underscore prefix (_) indicates this is a
        "private" method meant for internal use only.
        """
        return random.randint(1, 6)

    @property
    def current_player(self):
        """Get the currently active player.
        
        Returns:
            Player object at self.players[self.current_index]
        
        This is a property (not a method), so you access it like:
            player = game.current_player  # N
OPARENTHESES
        """
        return self.players[self.current_index]

**Key Concepts:**

1. **Private Methods:** `_roll_die` is conventionally "private"
   - Users of `PigGame` should call `roll()`, not `_roll_die()`

2. **Properties:** `@property` decorator makes a method look like an attribute
   - `game.current_player` (clean) vs `game.current_player()` (less clean)
   - Read-only: you cannot assign to `game.current_player = x`

---

### Step 4: Implement `switch_player` and `winner`

**Turn management:**

1. **`switch_player`:** Move to the other player and increment rounds
2. **`winner`:** Returns the player object who won, or `None`

**Add these methods:**

python
    def switch_player(self):
        """Toggle current_index and increment round number."""
        self.current_index = 1 - self.current_index  # Toggles 0 <-> 1
        if self.current_index == 0:
            self.round_number += 1
        
        # Reset shield for new turn
        self.current_player.shield_active = False

    @property
    def winner(self):
        """Return the winner if game over, else None."""
        if not self.game_over:
            return None
        
        # Who reached the target?
        for player in self.players:
            if player.score >= self.target_score:
                return player
        return None

**Key Concepts:**

1. **Toggling Logic:** `1 - self.current_index`
   - If index is 0: `1 - 0 = 1`
   - If index is 1: `1 - 1 = 0`
   - Elegant way to switch between two values

2. **Encapsulation:** Shield logic is kept local
   - When switching, shield is automatically deactivated
   - Prevents stale shield state from persisting across turns

---

### Step 5: Implement Shield Mechanics

**The logic for protecting the turn total:**

1. **`activate_shield`:** Uses 1 advantage if available
2. **`ai_should_convert_six_to_shield`:** Decision logic for AI
3. **`convert_six_to_shield`:** Grant shield to AI

**Add these methods:**

python
    def activate_shield(self) -> bool:
        """Attempt to activate shield using an advantage."""
        player = self.current_player
        if player.advantages > 0:
            player.advantages -= 1
            player.shield_active = True
            self.display.print_shield_activated(player.advantages)
            return True
        return False

    def ai_should_convert_six_to_shield(self) -> bool:
        """Check if AI should activate its first shield."""
        player = self.current_player
        return (player.is_ai and player.advantages == 0 
                and not player.shield_active)

    def convert_six_to_shield(self):
        """Grant AI first advantage and activate shield."""
        player = self.current_player
        player.advantages += 1
        player.shield_active = True
        self.display.print_ai_converted_shield()

---

### Step 6: Implement `ai_decision`

**AI strategy:**

python
    def ai_decision(self) -> str:
        """AI determines whether to roll or hold."""
        player = self.current_player
        
        # If turn_total is 0, must roll
        if player.turn_total == 0:
            return "r"
        
        # If score + turn_total >= target, hold (win game)
        if player.score + player.turn_total >= self.target_score:
            return "h"
        
        # If turn_total >= 15, play it safe and hold
        if player.turn_total >= 15:
            return "h"
        
        # Otherwise, 70% chance to roll
        return "r" if random.random() < 0.7 else "h"

---

### Step 7: Implement `roll`

**The core rule logic (pig-out, shield, normal roll):**

python
    def roll(self):
        """Simulate a die roll and process outcomes."""
        player = self.current_player
        val = self._roll_die()
        
        if val == 1:
            # Handle Pig-out
            if player.shield_active:
                # Protect: halve turn total
                half = math.ceil(player.turn_total / 2)
                self.display.print_shield_saved(half)
                player.turn_total = half
                player.shield_active = False
            else:
                self.display.print_pig_out()
                player.reset_turn()
                self.switch_player()
        else:
            # Handle 2-6
            player.turn_total += val
            self.display.print_die_roll(val, player.turn_total)
            
            # Special handling for rolling a 6
            if val == 6:
                if self.ai_should_convert_six_to_shield():
                    player.turn_total -= 6
                    self.convert_six_to_shield()
                elif not player.is_ai:
                    if player.advantages == 0 and not player.shield_active:
                        player.advantages += 1
                    self.display.print_shield_offer()
                    choice = input().strip().lower()
                    if choice == 'y':
                        player.turn_total -= 6
                        self.activate_shield()

---

### Step 8: Implement `hold` and `play`

**Finalizing the game loop:**

python
    def hold(self):
        """Bank turn points and check for win."""
        player = self.current_player
        player.score += player.turn_total
        self.display.print_banked(player.turn_total)
        
        if player.score >= self.target_score:
            self.game_over = True
        else:
            player.reset_turn()
            player.shield_active = False
            self.switch_player()

    def play(self):
        """The main game loop."""
        self.display.print_header(f"Pig Dice to {self.target_score}!")
        
        while not self.game_over:
            p1, p2 = self.players
            self.display.print_scoreboard(p1, p2)
            player = self.current_player
            
            # Decide: AI or Human input
            if player.is_ai:
                time.sleep(1) # Dramatic pause
                decision = self.ai_decision()
                self.display.print_ai_message(decision)
            else:
                decision = input("(r)oll or (h)old? ").lower()
            
            # Process decision
            if decision == 'r':
                self.roll()
            elif decision == 'h':
                self.hold()
            else:
                print("Invalid choice!")
                
        self.display.print_winner(self.winner.name, self.winner.score)

---

<a name="menu"></a>
## 7. 📋 Building Menu System

The `menu.py` keeps the game setup logic outside of the game loop.

python
from pig_game import PigGame

class Menu:
    def __init__(self):
        self.target_score = 20

    def run(self):
        while True:
            print("\n--- PIG DICE MENU ---")
            print(f"1. Play (Target: {self.target_score})")
            print("2. Set target score")
            print("3. Exit")
            choice = input("Choice: ")
            
            if choice == '1':
                PigGame(self.target_score).play()
            elif choice == '2':
                self.target_score = int(input("Enter new target: "))
            elif choice == '3':
                break

---

<a name="running"></a>
## 8. 🚀 Running the Complete Game

Create `main.py` to start everything:

python
from menu import Menu

if __name__ == "__main__":
    Menu().run()

**Run the command:**
bash
python main.py

---

<a name="review"></a>
## 9. 🧠 Final Review & OOP Concepts

### What have you achieved?

1. **Modular Design:** Four files, each with one job
2. **Game Logic:** Complex rules (pig-outs, shields, AI) implemented correctly
3. **OOP Mastery:**
   - **Encapsulation:** State hidden inside objects
   - **Composition:** Objects working together (Game has Players, Display)
   - **Properties:** Managed access to object state
4. **Professional Coding Practices:**
   - Type hinting (`val: int`)
   - Docstrings (`"""..."""`)
   - Descriptive method names
   - Separation of concerns

This workshop has demonstrated how to move from messy script-based programming to clean, maintainable Object-Oriented Programming. Well done!