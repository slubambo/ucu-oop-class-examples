"""Laundry Day Before the Presentation — a complete Weeks 1–6 story.
Run: python3 story.py. All numbers and events are invented for learning.
"""
from abc import ABC, abstractmethod


# ACT 1: The resource owns its value and the rules for changing it.
class WaterTank:
    def __init__(self, amount):
        self.remaining = amount  # Starting values go through the setter too.

    @property
    def remaining(self):
        return self.__remaining  # Name mangling, not a security lock.

    @remaining.setter
    def remaining(self, amount):
        if amount < 0:
            raise ValueError("Remaining litres cannot be negative.")
        self.__remaining = amount

    def use(self, amount):
        if amount <= 0 or amount > self.remaining:
            return False  # Refuse before changing state.
        self.remaining = self.remaining - amount
        return True


# ACT 2: The abstract family says what every concrete choice must provide.
class LaundryChoice(ABC):
    unit = "litres"  # Class attribute; every instance has its own name.

    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} needs {self.water_needed():,} {self.unit}."

    @abstractmethod
    def water_needed(self):
        pass


class MachineWash(LaundryChoice):
    def __init__(self, kilograms=2):
        if not isinstance(kilograms, int) or isinstance(kilograms, bool) or kilograms <= 0:
            raise ValueError("Kilograms must be a positive whole number.")
        super().__init__("Machine wash")
        self.kilograms = kilograms

    def water_needed(self):
        return self.kilograms * 5


class HandRinse(LaundryChoice):  # Siblings show hierarchical inheritance.
    def water_needed(self):
        return 4


class EcoWash(MachineWash):  # A third level in the same family.
    def __init__(self, kilograms=2):
        super().__init__(kilograms)
        self.name = "Eco wash"

    def water_needed(self):
        return super().water_needed() // 2  # Reuse, then specialise, the parent's calculation.


# ACT 3: Multiple inheritance adds a small descriptive ability.
class LaundryHype:
    def describe(self):
        return f"Fresh clothes, fresh start! {super().describe()}"


class FeaturedEcoWash(LaundryHype, EcoWash):
    pass  # The full hierarchy combines multiple and multilevel inheritance.


class SunDry:  # No shared parent: callers use its matching behaviour.
    name = "Sun drying"

    def water_needed(self):
        return 0

    def describe(self):
        return "Sun drying: 0 litres in this classroom model."


# ACT 4: The coordinator HAS-A resource, and USES-A chosen object.
class LaundrySession:
    def __init__(self, student, amount):
        self.student = student
        self.water = WaterTank(amount)  # Owned part: composition.
        self._entries = []  # Internal by convention; fresh for every instance.

    @property
    def completed_count(self):
        return len(self._entries)  # Read-only: it reflects actual history.

    def book(self, choice):
        needed = choice.water_needed()  # Each choice knows its own calculation.
        if needed < 0:
            return "Invalid negative requirement. Nothing recorded."
        if needed == 0 or self.water.use(needed):
            # Save the quoted cost now: later edits to the choice cannot change it.
            self._entries.append({"choice": choice, "cost": needed})
            return f"{self.student} completes {choice.name}: {needed:,} litres."
        return f"Not enough litres for {choice.name}. Nothing recorded."


def show_choices(choices):
    for choice in choices:
        print(choice.describe())  # Same call, different implementations.


# ACT 5: A complete story, including a refusal and independent object state.
def main():
    print("=== LAUNDRY DAY BEFORE THE PRESENTATION ===")
    print("Nambi needs clean clothes for a presentation. The hostel water tank is nearly empty.")
    choices = [MachineWash(), HandRinse("Hand rinse"),
               FeaturedEcoWash(), SunDry()]
    show_choices(choices)  # Includes an unrelated duck-typed guest.
    session = LaundrySession("Nambi", 18)
    other = LaundrySession("Alex", 18)
    print(session.book(choices[2]))
    print(session.book(choices[0]))
    print(session.book(choices[0]))  # Eventually the same request will not fit.
    print(session.book(choices[3]))
    print(other.book(choices[1]))
    print(f"{session.student}: {session.water.remaining:,} litres; completed: {session.completed_count}")
    print(f"{other.student}: {other.water.remaining:,} litres; completed: {other.completed_count}")
    print("MRO (method lookup order):")
    for parent in FeaturedEcoWash.__mro__:
        print(parent.__name__)
    print("Ending: The clothes are ready, and the remaining water is enough for the next person.")


if __name__ == "__main__":
    main()
