class LunchMoney:
    def __init__(self, amount):
        if (
            isinstance(amount, bool)
            or not isinstance(amount, int)
            or amount < 0
        ):
            raise ValueError(
                "Amount must be a non-negative whole number."
            )

        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def __str__(self):
        return f"UGX {self.amount:,}"

    def __repr__(self):
        return f"LunchMoney({self.amount})"

    def __eq__(self, other):
        if not isinstance(other, LunchMoney):
            return NotImplemented

        return self.amount == other.amount

    def __add__(self, other):
        if not isinstance(other, LunchMoney):
            return NotImplemented

        return LunchMoney(self.amount + other.amount)