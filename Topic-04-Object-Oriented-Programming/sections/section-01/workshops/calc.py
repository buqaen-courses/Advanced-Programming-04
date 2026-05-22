# step4_menu_class.py

import colorama
from colorama import Fore, Back, Style

# Initialize colorama (works on Windows, macOS, Linux)
colorama.init(autoreset=True)

class Calculator:
    """Same as before, but we simplify formatting for clarity."""
    def __init__(self, base="decimal"):
        self._base = base
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, new_base):
        if new_base in ("decimal", "octal", "binary"):
            self._base = new_base
        else:
            raise ValueError("Base must be 'decimal', 'octal', or 'binary'")
    
    def _format(self, value):
        if self.base == "decimal":
            return str(value)
        elif self.base == "octal":
            return oct(int(value))[2:]
        elif self.base == "binary":
            return bin(int(value))[2:]
        return str(value)
    
    def add(self, a, b):
        return self._format(a + b)
    
    def subtract(self, a, b):
        return self._format(a - b)
    
    def multiply(self, a, b):
        return self._format(a * b)
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        result = a / b
        if result.is_integer():
            return self._format(int(result))
        return str(result)   # keep float as decimal

class Menu:
    """Handles all user interaction with coloured output."""
    
    def __init__(self):
        self.calc = Calculator()
    
    def display_header(self):
        """Show a coloured header."""
        print(Fore.CYAN + Back.BLACK + "=" * 40)
        print(Fore.YELLOW + "      ADVANCED CALCULATOR")
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
    
    def show_main_menu(self):
        """Display the main menu options."""
        print(Fore.GREEN + "\n--- MAIN MENU ---")
        print(Fore.WHITE + "1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Change output base")
        print("6. Exit")
    
    def show_base_menu(self):
        """Display base selection submenu."""
        print(Fore.MAGENTA + "\n--- BASE OPTIONS ---")
        print("1. Decimal")
        print("2. Octal")
        print("3. Binary")
        print("4. Back to main menu")
    
    def get_number(self, prompt):
        """Safely get a float from the user."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print(Fore.RED + "Invalid number. Please try again.")
    
    def get_choice(self, max_choice):
        """Get a valid menu choice."""
        while True:
            try:
                choice = int(input(Fore.YELLOW + "Your choice: " + Style.RESET_ALL))
                if 1 <= choice <= max_choice:
                    return choice
                else:
                    print(Fore.RED + f"Please enter a number between 1 and {max_choice}.")
            except ValueError:
                print(Fore.RED + "Invalid input. Enter a number.")
    
    def run(self):
        """Main program loop."""
        self.display_header()
        
        # Initial base selection
        print(Fore.CYAN + "Choose initial output base:")
        self.show_base_menu()
        base_choice = self.get_choice(3)
        if base_choice == 1:
            self.calc.base = "decimal"
        elif base_choice == 2:
            self.calc.base = "octal"
        else:
            self.calc.base = "binary"
        print(Fore.GREEN + f"Base set to {self.calc.base.upper()}")
        
        while True:
            self.show_main_menu()
            choice = self.get_choice(6)
            
            if choice == 6:
                print(Fore.BLUE + "Thank you for using the calculator. Goodbye!")
                break
            
            if choice == 5:
                # Change base
                self.show_base_menu()
                base_choice = self.get_choice(4)
                if base_choice == 4:
                    continue
                new_base = {1: "decimal", 2: "octal", 3: "binary"}[base_choice]
                try:
                    self.calc.base = new_base
                    print(Fore.GREEN + f"Base changed to {self.calc.base.upper()}")
                except ValueError as e:
                    print(Fore.RED + str(e))
                continue
            
            # For operations 1-4, ask for two numbers
            print(Fore.CYAN + "\nEnter two numbers:")
            a = self.get_number("First number: ")
            b = self.get_number("Second number: ")
            
            try:
                if choice == 1:
                    result = self.calc.add(a, b)
                    op = "+"
                elif choice == 2:
                    result = self.calc.subtract(a, b)
                    op = "-"
                elif choice == 3:
                    result = self.calc.multiply(a, b)
                    op = "*"
                elif choice == 4:
                    result = self.calc.divide(a, b)
                    op = "/"
                
                # Colourful output
                print(Fore.LIGHTGREEN_EX + f"\nResult: {a} {op} {b} = ", end="")
                print(Fore.LIGHTRED_EX + f"{result} (in {self.calc.base})" + Style.RESET_ALL)
            except ValueError as e:
                print(Fore.RED + f"Error: {e}")

def main():
    menu = Menu()
    menu.run()

if __name__ == "__main__":
    main()