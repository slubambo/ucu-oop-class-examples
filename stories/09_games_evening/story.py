"""The Hostel Games Evening — a complete Weeks 1–6 story.
Run: python3 story.py. All numbers and events are invented for learning.
"""
from abc import ABC, abstractmethod


# ACT 1: The resource owns its value and the rules for changing it.
class GameCredits:
    def __init__(self, amount):
        self.remaining = amount  # Starting values go through the setter too.

    @property
    def remaining(self):
        return self.__remaining  # Name mangling, not a security lock.

    @remaining.setter
    def remaining(self, amount):
        if amount < 0:
            raise ValueError("Remaining credits cannot be negative.")
        self.__remaining = amount

    def use(self, amount):
        if amount <= 0 or amount > self.remaining:
            return False  # Refuse before changing state.
        self.remaining = self.remaining - amount
        return True


# ACT 2: The abstract family says what every concrete choice must provide.
class GameChoice(ABC):
    unit = "credits"  # Class attribute; every instance has its own name.

    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} needs {self.credit_cost():,} {self.unit}."

    @abstractmethod
    def credit_cost(self):
        pass


class FootballGame(GameChoice):
    def __init__(self, rounds=2):
        if not isinstance(rounds, int) or isinstance(rounds, bool) or rounds <= 0:
            raise ValueError("Rounds must be a positive whole number.")
        super().__init__("Football game")
        self.rounds = rounds

    def credit_cost(self):
        return self.rounds * 3


class LudoRound(GameChoice):  # Siblings show hierarchical inheritance.
    def credit_cost(self):
        return 2


class PracticeGame(FootballGame):  # A third level in the same family.
    def __init__(self, rounds=2):
        super().__init__(rounds)
        self.name = "Practice football game"

    def credit_cost(self):
        return super().credit_cost() // 2  # Reuse, then specialise, the parent's calculation.


# ACT 3: Multiple inheritance adds a small descriptive ability.
class GamesHype:
    def describe(self):
        return f"Controllers ready! {super().describe()}"


class FeaturedPractice(GamesHype, PracticeGame):
    pass  # The full hierarchy combines multiple and multilevel inheritance.


class CheeringContest:  # No shared parent: callers use its matching behaviour.
    name = "Cheering contest"

    def credit_cost(self):
        return 0

    def describe(self):
        return "Cheering contest: 0 credits in this classroom model."


# ACT 4: The coordinator HAS-A resource, and USES-A chosen object.
class GamesEvening:
    def __init__(self, student, amount):
        self.student = student
        self.credits = GameCredits(amount)  # Owned part: composition.
        self._entries = []  # Internal by convention; fresh for every instance.

    @property
    def completed_count(self):
        return len(self._entries)  # Read-only: it reflects actual history.

    def play(self, choice):
        needed = choice.credit_cost()  # Each choice knows its own calculation.
        if needed < 0:
            return "Invalid negative requirement. Nothing recorded."
        if needed == 0 or self.credits.use(needed):
            # Save the quoted cost now: later edits to the choice cannot change it.
            self._entries.append({"choice": choice, "cost": needed})
            return f"{self.student} completes {choice.name}: {needed:,} credits."
        return f"Not enough credits for {choice.name}. Nothing recorded."


def show_choices(choices):
    for choice in choices:
        print(choice.describe())  # Same call, different implementations.


# ACT 5: A complete story, including a refusal and independent object state.
def main():
    print("=== THE HOSTEL GAMES EVENING ===")
    print("Achen is running a hostel games evening. The group has limited game credits and many challengers.")
    choices = [FootballGame(), LudoRound("Ludo round"),
               FeaturedPractice(), CheeringContest()]
    show_choices(choices)  # Includes an unrelated duck-typed guest.
    session = GamesEvening("Achen", 10)
    other = GamesEvening("Alex", 10)
    print(session.play(choices[2]))
    print(session.play(choices[0]))
    print(session.play(choices[0]))  # Eventually the same request will not fit.
    print(session.play(choices[3]))
    print(other.play(choices[1]))
    print(f"{session.student}: {session.credits.remaining:,} credits; completed: {session.completed_count}")
    print(f"{other.student}: {other.credits.remaining:,} credits; completed: {other.completed_count}")
    print("MRO (method lookup order):")
    for parent in FeaturedPractice.__mro__:
        print(parent.__name__)
    print("Ending: Everyone has a turn, and the credit counter still tells the truth.")


if __name__ == "__main__":
    main()
