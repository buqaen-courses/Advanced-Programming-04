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
                f"turn={self.turn_total}, adv={self.advantages}, {shield} )")
    
    def reset_turn(self):
        """Reset turn_total to 0 after hold or pig-out."""
        self.turn_total = 0
    
if __name__ == "__main__":
    from display import Display
    d = Display()

    d.print_header("TEST: PLAYER __init__")
    p = Player("Alice")
    print(p)

    ai = Player("Bot", is_ai=True)
    print(ai)
    p.shield_active =  True
    p.advantages = 1
    print(p)
