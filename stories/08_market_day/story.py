"""Mukono Market Basket — a complete Weeks 1–6 story.
Run: python3 story.py. All numbers and events are invented for learning.
"""
from abc import ABC, abstractmethod


# ACT 1: The resource owns its value and the rules for changing it.
class MarketWallet:
    def __init__(self, amount):
        self.remaining = amount  # Starting values go through the setter too.

    @property
    def remaining(self):
        return self.__remaining  # Name mangling, not a security lock.

    @remaining.setter
    def remaining(self, amount):
        if amount < 0:
            raise ValueError("Remaining UGX cannot be negative.")
        self.__remaining = amount

    def use(self, amount):
        if amount <= 0 or amount > self.remaining:
            return False  # Refuse before changing state.
        self.remaining = self.remaining - amount
        return True


# ACT 2: The abstract family says what every concrete choice must provide.
class MarketItem(ABC):
    unit = "UGX"  # Class attribute; every instance has its own name.

    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} needs {self.price():,} {self.unit}."

    @abstractmethod
    def price(self):
        pass


class MatookeBundle(MarketItem):
    def __init__(self, portions=2):
        if not isinstance(portions, int) or isinstance(portions, bool) or portions <= 0:
            raise ValueError("Portions must be a positive whole number.")
        super().__init__("Matooke bundle")
        self.portions = portions

    def price(self):
        return self.portions * 1500


class GroundnutPack(MarketItem):  # Siblings show hierarchical inheritance.
    def price(self):
        return 2000


class SharedMatooke(MatookeBundle):  # A third level in the same family.
    def __init__(self, portions=2):
        super().__init__(portions)
        self.name = "Shared matooke bundle"

    def price(self):
        return max(0, super().price() - 500)  # Reuse, then specialise, the parent's calculation.


# ACT 3: Multiple inheritance adds a small descriptive ability.
class MarketHype:
    def describe(self):
        return f"Mukono market special! {super().describe()}"


class FeaturedBundle(MarketHype, SharedMatooke):
    pass  # The full hierarchy combines multiple and multilevel inheritance.


class GardenGift:  # No shared parent: callers use its matching behaviour.
    name = "Garden gift"

    def price(self):
        return 0

    def describe(self):
        return "Garden gift: 0 UGX in this classroom model."


# ACT 4: The coordinator HAS-A resource, and USES-A chosen object.
class MarketTrip:
    def __init__(self, student, amount):
        self.student = student
        self.wallet = MarketWallet(amount)  # Owned part: composition.
        self._entries = []  # Internal by convention; fresh for every instance.

    @property
    def completed_count(self):
        return len(self._entries)  # Read-only: it reflects actual history.

    def buy(self, choice):
        needed = choice.price()  # Each choice knows its own calculation.
        if needed < 0:
            return "Invalid negative requirement. Nothing recorded."
        if needed == 0 or self.wallet.use(needed):
            # Save the quoted cost now: later edits to the choice cannot change it.
            self._entries.append({"choice": choice, "cost": needed})
            return f"{self.student} completes {choice.name}: {needed:,} UGX."
        return f"Not enough UGX for {choice.name}. Nothing recorded."


def show_choices(choices):
    for choice in choices:
        print(choice.describe())  # Same call, different implementations.


# ACT 5: A complete story, including a refusal and independent object state.
def main():
    print("=== MUKONO MARKET BASKET ===")
    print("Kato is shopping for the hostel cooking group. The shopping list is longer than the budget.")
    choices = [MatookeBundle(), GroundnutPack("Groundnut pack"),
               FeaturedBundle(), GardenGift()]
    show_choices(choices)  # Includes an unrelated duck-typed guest.
    session = MarketTrip("Kato", 7000)
    other = MarketTrip("Alex", 7000)
    print(session.buy(choices[2]))
    print(session.buy(choices[0]))
    print(session.buy(choices[0]))  # Eventually the same request will not fit.
    print(session.buy(choices[3]))
    print(other.buy(choices[1]))
    print(f"{session.student}: {session.wallet.remaining:,} UGX; completed: {session.completed_count}")
    print(f"{other.student}: {other.wallet.remaining:,} UGX; completed: {other.completed_count}")
    print("MRO (method lookup order):")
    for parent in FeaturedBundle.__mro__:
        print(parent.__name__)
    print("Ending: The basket has dinner ingredients, and no one has promised money they do not have.")


if __name__ == "__main__":
    main()
