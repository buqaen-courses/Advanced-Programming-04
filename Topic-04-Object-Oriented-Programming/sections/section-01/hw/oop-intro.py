class SafeCalculator:
    """Calculator with proper error handling."""

    def __init__(self):
        self._result = 0.0

    def divide(self, dividend, divisor):
        try:
            return dividend / divisor
        except Exception as e:
            print(f"Error:{e}")

c = SafeCalculator()
print(c.divide(12,0))
print("-"*50)
print(c.divide("12",0))
print("-"*50)
print(c.divide(12,8))
print("-"*50)
