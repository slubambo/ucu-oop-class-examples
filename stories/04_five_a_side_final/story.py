"""The Five-a-Side Final: a friendly UCU team selects its final attacks.
Run: python3 story.py. Energy costs and match events are a toy simulation.
"""
from abc import ABC, abstractmethod


# ACT 1: Energy and its rules stay together in one object.
class EnergyTank:
    def __init__(self, points):
        self.remaining = points  # Constructor calls the validating setter.

    @property
    def remaining(self):
        return self.__remaining  # Name mangling reduces accidental access.

    @remaining.setter
    def remaining(self, amount):
        if amount < 0 or amount > 100:
            raise ValueError("Energy must stay between 0 and 100.")
        self.__remaining = amount  # No change until checks pass.

    def spend(self, amount):
        if amount <= 0 or amount > self.remaining:
            return False
        self.remaining = self.remaining - amount
        return True
        
    def recover(self,amount):
        if amount <= 0:
           return False
        new_total = self.remaining + amount
        if new_total > 100:
           return False
        self.remaining = new_total
        return True 
# ACT 2: An attack must say what effort it needs; players can choose the style.
class Attack(ABC):
    team = "Mukono Meteors"  # Shared class state; each attack has its own name.

    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.team}: {self.name} needs {self.effort()} energy."

    @abstractmethod
    def effort(self):
        pass  # Attack("Mystery") has no concrete effort rule.


class Dribble(Attack):  # IS-A Attack: single inheritance.
    def __init__(self, player):
        super().__init__(f"{player}'s dribble")
        self.player = player

    def effort(self):
        return 30  # Override the abstract requirement.


class TeamPass(Attack):  # Hierarchical inheritance: a sibling of Dribble.
    def effort(self):
        return 10


class SmartDribble(Dribble):  # Attack -> Dribble -> SmartDribble: multilevel.
    def effort(self):
        return super().effort() - 10  # Reuse and extend the parent's method.


# ACT 3: The commentator adds excitement, not extra energy cost.
class CommentaryMixin:
    def describe(self):
        return f"The crowd is standing! {super().describe()}"


class CrowdFavourite(CommentaryMixin, SmartDribble):
    pass  # Two parents = multiple; combined with levels = hybrid inheritance.


class WaterBreak:  # Unrelated to Attack but supports the same calls.
    name = "Water break"

    def effort(self):
        return 0

    def describe(self):
        return "Water break: tactical discussion, zero energy cost in this model."


# ACT 4: The match HAS-A tank; actions are borrowed collaborators.
class Match:
    def __init__(self, captain, points):
        self.captain = captain
        self.energy = EnergyTank(points)  # Owned object: composition.
        self._actions = []  # Internal list, by single-underscore convention.
        self.action = None

    @property
    def completed_actions(self):  # Read-only; computed, not independently editable.
        return len(self._actions)

    def play(self, action):
        self.action = action  # A replaceable part: aggregation.
        effort = action.effort()  # Abstraction: Match doesn't calculate the skill.
        if effort == 0 or self.energy.spend(effort):
            self._actions.append(action)  # A list of objects: collaboration.
            return f"Captain {self.captain} chooses {action.name}. Done!"
        return f"Not enough energy for {action.name}. Pass the ball, please!"


def discuss_tactics(actions):  # Week 1 function, parameter, list, for loop.
    for action in actions:
        print(action.describe())  # Polymorphism: one request, varied responses.


def main():
    print("=== THE FIVE-A-SIDE FINAL ===")
    print("One final attack. Brian wants skills; the energy tank wants teamwork.")
    actions = [Dribble("Brian"), TeamPass("Quick team pass"),
               CrowdFavourite("Achen"), WaterBreak()]
    discuss_tactics(actions)  # WaterBreak fits by behaviour alone: duck typing.
    brian = Match("Brian", 35)
    ruth = Match("Ruth", 40)  # Independent state in a second object.
    print(brian.play(actions[2]))  # Smart dribble costs 20.
    print(brian.play(actions[0]))  # Refused; 15 cannot pay 30.
    print(brian.play(actions[1]))  # Teamwork costs 10.
    print(brian.play(actions[3]))  # Change collaborator without changing Match.
    print(ruth.play(actions[0]))
    print(f"Brian: {brian.energy.remaining} energy; actions: {brian.completed_actions}")
    print(f"Ruth: {ruth.energy.remaining} energy; actions: {ruth.completed_actions}")
    print("MRO (look left to right):")
    for parent in CrowdFavourite.__mro__:
        print(parent.__name__)
    print("Ending: the final pass creates the winner. Teamwork gets the celebration.")


if __name__ == "__main__":
    main()
