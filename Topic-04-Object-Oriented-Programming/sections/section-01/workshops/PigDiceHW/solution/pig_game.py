import math
import random
import time
from player import Player
from display import Display


class PigGame:
    """Main game logic with shield mechanics and AI behavior."""

    def __init__(self, target_score: int = 20):
        self.target_score = target_score
        self.players = [Player("You"), Player("AI", is_ai=True)]
        self.display = Display()
        self.current_index = 0
        self.game_over = False

    def _roll_die(self) -> int:
        return random.randint(1, 6)

    @property
    def current_player(self):
        return self.players[self.current_index]

    def switch_player(self):
        self.current_index = 1 - self.current_index
        self.current_player.shield_active = False

    @property
    def winner(self):
        if not self.game_over:
            return None
        for player in self.players:
            if player.score >= self.target_score:
                return player
        return None

    def activate_shield(self) -> bool:
        player = self.current_player
        if player.advantages > 0:
            player.advantages -= 1
            player.shield_active = True
            self.display.print_shield_activated(player.advantages)
            return True
        return False

    def ai_should_convert_six_to_shield(self) -> bool:
        player = self.current_player
        return (player.is_ai and player.advantages == 0
                and not player.shield_active)

    def convert_six_to_shield(self):
        player = self.current_player
        player.advantages += 1
        player.shield_active = True
        self.display.print_ai_converted_shield()

    def ai_decision(self) -> str:
        player = self.current_player
        if player.turn_total == 0:
            return "r"
        if player.score + player.turn_total >= self.target_score:
            return "h"
        if player.turn_total >= 15:
            return "h"
        return "r" if random.random() < 0.7 else "h"

    def roll(self):
        player = self.current_player
        val = self._roll_die()

        if val == 1:
            if player.shield_active:
                half = math.ceil(player.turn_total / 2)
                self.display.print_shield_saved(half)
                player.turn_total = half
                player.shield_active = False
            else:
                self.display.print_pig_out()
                player.reset_turn()
                self.switch_player()
        else:
            player.turn_total += val
            self.display.print_die_roll(val, player.turn_total)

            if val == 6:
                if self.ai_should_convert_six_to_shield():
                    self.convert_six_to_shield()
                elif not player.is_ai:
                    if player.advantages > 0:
                        self.display.print_shield_offer()
                        choice = input().strip().lower()
                        if choice == 'y':
                            player.turn_total -= 6
                            self.activate_shield()
                    else:
                        self.display.print_no_advantages()

    def hold(self):
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
        self.display.print_header(f"Pig Dice to {self.target_score}!")

        while not self.game_over:
            p1, p2 = self.players
            self.display.print_scoreboard(p1, p2)
            player = self.current_player

            if player.is_ai:
                time.sleep(1)
                decision = self.ai_decision()
                self.display.print_ai_message(decision)
            else:
                decision = input("(r)oll or (h)old? ").lower()

            if decision == 'r':
                self.roll()
            elif decision == 'h':
                self.hold()
            else:
                print("Invalid choice!")

        self.display.print_winner(self.winner.name, self.winner.score)
