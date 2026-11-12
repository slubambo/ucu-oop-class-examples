"""An immutable value representing a non-negative number of show minutes."""


class StageTime:
    def __init__(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, int):
            raise TypeError("Stage time must be a whole number of minutes.")
        if amount < 0:
            raise ValueError("Stage time cannot be negative.")
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def __str__(self):
        return f"{self.amount:,} minutes"

    def __repr__(self):
        return f"StageTime({self.amount})"

    def __eq__(self, other):
        if not isinstance(other, StageTime):
            return NotImplemented
        return self.amount == other.amount

    def __add__(self, other):
        if not isinstance(other, StageTime):
            return NotImplemented
        return StageTime(self.amount + other.amount)