class DataAmount:
    """A whole, non-negative number of MB."""

    def __init__(self, amount):
        if isinstance(amount, bool):  # bool is a kind of int, so check it first.
            raise TypeError("amount cannot be a Boolean.")
        if not isinstance(amount, int):  # Refuses 2.5, 3.0 and "100".
            raise TypeError("amount must be a whole number.")
        if amount < 0:
            raise ValueError("amount cannot be negative.")
        self.__amount = amount

    @property
    def amount(self):  # No setter, so it is read-only.
        return self.__amount

    def __str__(self):  # 1. User-facing: 3,000 MB
        return f"{self.amount:,} MB"

    def __repr__(self):  # 2. Developer-facing: DataAmount(3000)
        return f"DataAmount({self.amount})"

    def __eq__(self, other):  # 3. Same amount means equal.
        if not isinstance(other, DataAmount):
            return NotImplemented
        return self.amount == other.amount

    def __add__(self, other):  # 4. Returns a new DataAmount.
        if not isinstance(other, DataAmount):
            return NotImplemented
        return DataAmount(self.amount + other.amount)