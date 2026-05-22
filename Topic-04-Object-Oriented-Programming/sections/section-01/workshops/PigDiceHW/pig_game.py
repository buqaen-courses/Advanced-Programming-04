import math
import random
import time
from player import Player
from display import Display


class PigGame:
    """All game logic + game loop. Uses Display for coloured output."""

    def __init__(self, target_score: int = 20):
        # target_score: points needed to win (default 20)
        self.target_score = target_score
        # players: Player 1 is human, Player 2 is AI (computer)
        self.players = [Player("Player 1"), Player("Player 2", is_ai=True)]
        # display: fully-implemented helper for coloured output
        self.display = Display()
        # current_index: index in self.players whose turn it is (0 or 1)
        self.current_index = 0
        # game_over: becomes True when a player reaches target_score
        self.game_over = False

    def _roll_die(self) -> int:
        """Roll a six-sided die.

        Returns:
            int: A random integer between 1 and 6 (inclusive).
        """
        pass

    def roll(self) -> int:
        """Roll the die and process the result.

        Returns:
            int: The die value (1–6).

        Side effects:
            - If die == 1 and shield_active: turn_total = ceil(turn_total/2), shield cleared.
            - If die == 1 and no shield: pig-out (turn_total reset, player switched).
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
            bool: True if shield was activated, False if no advantages left.
        """
        pass

    def ai_decision(self) -> str:
        """AI player randomly decides to roll or hold.

        Algorithm:
            - Always roll if turn_total is 0.
            - Otherwise, random choice between 'r' and 'h'.
        """
        pass

    def ai_should_convert_six_to_shield(self) -> bool:
        """Check if AI should convert a rolled 6 into a shield.

        Strategy: Keep one shield at all times. If AI has 0 advantages
        and no active shield, convert the first 6. Later 6s added normally.
        """
        pass

    def convert_six_to_shield(self):
        """Convert a rolled 6 into a shield (AI's first 6).

        Sets advantages=1 and shield_active=True.
        The caller (play()) handles removing the 6 from turn_total.
        """
        pass

    def play(self):
        """Run the full coloured game loop using self.display for output.

        Flow:
            1. Print header and target score.
            2. Loop while not game_over:
               a. Print scoreboard.
               b. Print whose turn it is.
               c. If AI: auto-decide roll/hold.
               d. If human: prompt for (r)oll or (h)old.
               e. On roll: call self.roll(), display result.
                  On rolling 6: offer shield (human) or auto-convert (AI).
               f. On hold: call self.hold(), display banked.
               g. Validate input.
            3. Print winner.
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
