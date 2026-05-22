class Player:
    """Represents a player with a score and current turn total."""

    def __init__(self, name: str, is_ai: bool = False):
        # name: display name for this player (e.g. "Player 1")
        self.name = name
        # is_ai: True if this player is the computer (auto-decides roll/hold)
        self.is_ai = is_ai
        # score: total banked points accumulated across all turns
        self.score = 0
        # turn_total: points accumulated in the current turn (reset on pig-out or hold)
        self.turn_total = 0
        # advantages: number of shields the player can activate (by rolling a 6)
        self.advantages = 0
        # shield_active: True if a shield is currently protecting the turn total
        self.shield_active = False

    def __repr__(self):
        shield = "\U0001f6e1\ufe0f" if self.shield_active else "\U0001f513"
        return (f"Player({self.name}, score={self.score}, "
                f"turn={self.turn_total}, adv={self.advantages}, {shield})")

    def reset_turn(self):
        """Set turn_total = 0 after a hold (points banked) or pig-out."""
        pass
