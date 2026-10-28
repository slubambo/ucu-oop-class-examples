class EnergyAmount:
    """A non-negative whole number of energy."""

    def __init__(self, amount):
        # bool counts as an int in Python, so refuse it explicitly
        if isinstance(amount, bool) or not isinstance(amount, int):
            raise TypeError("Energy must be a whole number (not a fraction or Boolean).")
        if amount < 0:
            raise ValueError("Energy cannot be negative.")
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def __str__(self):
        return f"{self._amount:,} energy"

    def __repr__(self):
        return f"EnergyAmount({self._amount})"

    def __eq__(self, other):
        if not isinstance(other, EnergyAmount):
            return NotImplemented
        return self._amount == other._amount

    def __hash__(self):
        return hash(self._amount)

    def __add__(self, other):
        if not isinstance(other, EnergyAmount):
            return NotImplemented
        return EnergyAmount(self._amount + other._amount)