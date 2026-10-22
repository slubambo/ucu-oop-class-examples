"""The Mukono Mission: a forgotten flash drive and a transport decision.
Run: python3 story.py. Fares and distances are invented teaching values.
"""
from abc import ABC, abstractmethod


# ACT 1: One trip owns a purse; the purse protects its own money.
class TripPurse:
    def __init__(self, money):
        self.balance = money  # Constructor uses validation, too.

    @property
    def balance(self):
        return self.__balance  # Name-mangled; not a PIN or a security system.

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Trip money cannot be negative.")
        self.__balance = amount

    def pay(self, fare):
        if fare <= 0 or fare > self.balance:
            return False
        self.balance = self.balance - fare
        return True

    
# EXTENSION 2: Transport money top up
    def top_up(self, amount):
        "Adds a positive monetary amount to the balance."
        "ReturnsTrue if succesfull, False if zero or negative"
        if amount > 0:
            self.balance +=amount
            return True
        return False

    
# ACT 2: All transport must quote a fare, but the calculation can differ.
class Transport(ABC):
    currency = "UGX"  # Shared class attribute.

    def __init__(self, name):
        self.name = name  # Instance attribute: each vehicle has its own name.

    def describe(self):
        return f"{self.name} is ready for the Mukono mission."

    @abstractmethod
    def quote_fare(self, distance):
        pass  # Transport("Mystery") cannot be instantiated.


class Boda(Transport):  # IS-A Transport: single inheritance.
    def __init__(self, rider):
        super().__init__(f"{rider}'s boda")  # Initialise shared state once.
        self.rider = rider

    def quote_fare(self, distance):
        return distance * 1000  # Override the parent's abstract method.


class Taxi(Transport):  # Sibling classes: hierarchical inheritance.
    def quote_fare(self, distance):
        return 2000  # Flat classroom fare for this short route.


class StudentBoda(Boda):  # Transport -> Boda -> StudentBoda: multilevel.
    def quote_fare(self, distance):
        return max(1000, super().quote_fare(distance) - 500)


# ACT 3: An extra ability plus a vehicle: multiple inheritance.
class CheerfulMixin:
    def describe(self):
        return f"Helmet on, let's go! {super().describe()}"


class CheerfulStudentBoda(CheerfulMixin, StudentBoda):
    pass  # Hybrid hierarchy. super() follows this object's MRO.

# EXTENSION 3: A free lift and a walk with a friend
class CousinLift:
    def __init__(self, name="Cousin's car"):
        self.name = name

    def describe(self):
        return f"{self.name} Free lift from family, zero stress."
    def quote_fare(self, distance):
            return 0

class WalkWithFriend:  # No Transport parent: duck typing in the same story.
    name = "Walk with a friend"

    def quote_fare(self, distance):
        return 0

    def describe(self):
        return "Walk with a friend: free transport, premium conversation."


# ACT 4: A journey HAS-A purse and USES-A transport object.
class Journey:
    def __init__(self, student, money):
        self.student = student
        self.purse = TripPurse(money)  # Owned part: composition.
        self._legs = []  # Internal by convention; a list of transport objects.
        self.transport = None

    @property
    def completed_legs(self):  # Read-only, computed from actual completed trips.
        return len(self._legs)

    def travel(self, transport, distance):
        if distance <= 0:
            return "Distance must be positive. No trip started."
        self.transport = transport  # Borrowed/swappable part: aggregation.
        fare = self.transport.quote_fare(distance)  # Hide the pricing details.
        if fare == 0 or self.purse.pay(fare):
            self._legs.append(transport)
            return f"{self.student} travels by {transport.name}: UGX {fare:,}."
        return f"{self.student}: not enough money for {transport.name}."


def compare(options, distance):  # Function, parameter, loop: Week 1 tools.
    for option in options:
        print(option.describe())
        print(f"Quote: UGX {option.quote_fare(distance):,}")  # Polymorphism.

def cheapest(options, distance):
    best = None
    best_fare = None
    for option in options:
        fare = option.quote_fare(distance)
        if best is None or fare < best_fare:
            best = option
            best_fare = fare
    return best


def main():
    print("=== THE MUKONO MISSION ===")
    print("Amina left her flash drive in town. Her presentation is today!")
    options = [Boda("Kato"), Taxi("Mukono taxi"),
               CheerfulStudentBoda("Nambi"), WalkWithFriend()]
    compare(options, 3)  # The walk works without inheriting Transport.
    amina = Journey("Amina", 5000)
    peter = Journey("Peter", 2000)  # Independent object state.
    print(amina.travel(options[2], 3))  # Student boda: 2500.
    print(amina.travel(options[1], 3))  # Swap the part: taxi back, 2000.
    print(amina.travel(options[0], 3))  # Refused, only 500 left.
    print(peter.travel(options[3], 3))
    print(f"Amina: UGX {amina.purse.balance:,}; legs: {amina.completed_legs}")
    print(f"Peter: UGX {peter.purse.balance:,}; legs: {peter.completed_legs}")
    print("MRO (look left to right):")
    for parent in CheerfulStudentBoda.__mro__:
        print(parent.__name__)
    print("Ending: flash drive recovered. The slides live to present another day.")


if __name__ == "__main__":
    main()
