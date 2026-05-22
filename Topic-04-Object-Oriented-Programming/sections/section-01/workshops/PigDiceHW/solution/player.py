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
        self.turn_total = 0
