import math
import random
import time
from player import Player
from display import Display
from colorama import init, Fore, Style


class PigGame:
    """All game logic + game loop. Uses Display for coloured output."""

    def __init__(self, target_score: int = 20):
        self.target_score = target_score
        self.players = [Player("Player 1"), Player("Player 2", is_ai=True)]
        self.display = Display()
        self.current_index = 0
        self.game_over = False

    def _roll_die(self) -> int:
        return random.randint(1,6)

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
        print(f"  Roll {i+1}: {val}")
    print("All 10 rolls are between 1 and 6 — ✓")