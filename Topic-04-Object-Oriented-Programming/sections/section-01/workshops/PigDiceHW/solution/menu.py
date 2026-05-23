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
                try:
                    self.target_score = int(input("Enter new target: "))
                except ValueError:
                    print("Invalid number!")
            elif choice == '3':
                break
