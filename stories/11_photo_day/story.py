"""The Campus Photo-Day Rush — a complete Weeks 1–6 story.
Run: python3 story.py. All numbers and events are invented for learning.
"""
from abc import ABC, abstractmethod


# ACT 1: The resource owns its value and the rules for changing it.
class PhotoStorage:
    def __init__(self, amount):
        self.remaining = amount  # Starting values go through the setter too.

    @property
    def remaining(self):
        return self.__remaining  # Name mangling, not a security lock.

    @remaining.setter
    def remaining(self, amount):
        if amount < 0:
            raise ValueError("Remaining MB cannot be negative.")
        self.__remaining = amount

    def use(self, amount):
        if amount <= 0 or amount > self.remaining:
            return False  # Refuse before changing state.
        self.remaining = self.remaining - amount
        return True


# ACT 2: The abstract family says what every concrete choice must provide.
class PhotoPackage(ABC):
    unit = "MB"  # Class attribute; every instance has its own name.

    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} needs {self.storage_needed():,} {self.unit}."

    @abstractmethod
    def storage_needed(self):
        pass


class PortraitSet(PhotoPackage):
    def __init__(self, portraits=3):
        if not isinstance(portraits, int) or isinstance(portraits, bool) or portraits <= 0:
            raise ValueError("Portraits must be a positive whole number.")
        super().__init__("Portrait set")
        self.portraits = portraits

    def storage_needed(self):
        return self.portraits * 5


class GroupShot(PhotoPackage):  # Siblings show hierarchical inheritance.
    def storage_needed(self):
        return 10


class CompactPortraits(PortraitSet):  # A third level in the same family.
    def __init__(self, portraits=3):
        super().__init__(portraits)
        self.name = "Compact portraits"

    def storage_needed(self):
        return super().storage_needed() // 2  # Reuse, then specialise, the parent's calculation.


# ACT 3: Multiple inheritance adds a small descriptive ability.
class PhotoHype:
    def describe(self):
        return f"Mukono, smile! {super().describe()}"


class FeaturedPortraits(PhotoHype, CompactPortraits):
    pass  # The full hierarchy combines multiple and multilevel inheritance.


class PhoneSelfie:  # No shared parent: callers use its matching behaviour.
    name = "Phone selfie"

    def storage_needed(self):
        return 1

    def describe(self):
        return "Phone selfie: 1 MB in this classroom model."


# ACT 4: The coordinator HAS-A resource, and USES-A chosen object.
class PhotoSession:
    def __init__(self, student, amount):
        self.student = student
        self.storage = PhotoStorage(amount)  # Owned part: composition.
        self._entries = []  # Internal by convention; fresh for every instance.

    @property
    def completed_count(self):
        return len(self._entries)  # Read-only: it reflects actual history.

    def capture(self, choice):
        needed = choice.storage_needed()  # Each choice knows its own calculation.
        if needed < 0:
            return "Invalid negative requirement. Nothing recorded."
        if needed == 0 or self.storage.use(needed):
            # Save the quoted cost now: later edits to the choice cannot change it.
            self._entries.append({"choice": choice, "cost": needed})
            return f"{self.student} completes {choice.name}: {needed:,} MB."
        return f"Not enough MB for {choice.name}. Nothing recorded."


def show_choices(choices):
    for choice in choices:
        print(choice.describe())  # Same call, different implementations.


# ACT 5: A complete story, including a refusal and independent object state.
def main():
    print("=== THE CAMPUS PHOTO-DAY RUSH ===")
    print("Joel is organising a campus photo afternoon. The camera has limited space and the queue is growing.")
    choices = [PortraitSet(), GroupShot("Group shot"),
               FeaturedPortraits(), PhoneSelfie()]
    show_choices(choices)  # Includes an unrelated duck-typed guest.
    session = PhotoSession("Joel", 30)
    other = PhotoSession("Alex", 30)
    print(session.capture(choices[2]))
    print(session.capture(choices[0]))
    print(session.capture(choices[0]))  # Eventually the same request will not fit.
    print(session.capture(choices[3]))
    print(other.capture(choices[1]))
    print(f"{session.student}: {session.storage.remaining:,} MB; completed: {session.completed_count}")
    print(f"{other.student}: {other.storage.remaining:,} MB; completed: {other.completed_count}")
    print("MRO (method lookup order):")
    for parent in FeaturedPortraits.__mro__:
        print(parent.__name__)
    print("Ending: The photos are saved in the simulation, and the storage counter stays accurate.")


if __name__ == "__main__":
    main()
