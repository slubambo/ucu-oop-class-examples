"""The Rolex Rescue: Sarah's lunch break becomes a tiny OOP adventure.
Run: python3 story.py. All prices are invented classroom values.
Read Acts 1-5 in order; each act gives the next concept a job.
"""
from abc import ABC, abstractmethod


# ACT 1: A wallet owns its balance and the rules for changing it.
class LunchWallet:
    def __init__(self, balance):
        self.balance = balance  # Use the setter even during construction.

    @property
    def balance(self):
        return self.__balance  # __ triggers name mangling, not real security.

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Lunch money cannot be negative.")
        self.__balance = amount  # Only change state AFTER checking the rule.

    def spend(self, amount):
        if amount <= 0 or amount > self.balance:
            return False  # A normal refused purchase; no exception lesson needed.
        self.balance = self.balance - amount
        return True

    # Extension 2: Mum sends lunch money.
    # A positive amount is added to the balance and the method returns True.
    # Zero or a negative amount is refused: returns False and the balance stays the same.
    def top_up(self, amount):
        if amount <= 0:
            return False
        self.balance = self.balance + amount
        return True

  


# ACT 2: Meal states WHAT every menu item must do; children supply HOW.
class Meal(ABC):
    currency = "UGX"  # Class attribute: shared; name belongs to each instance.

    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} costs {self.currency} {self.price():,}"

    @abstractmethod
    def price(self):
        pass  # Meal itself is incomplete; Meal("Mystery") is not allowed.


class Rolex(Meal):  # A Rolex IS-A Meal: single inheritance.
    def __init__(self, eggs=2):
        super().__init__("Rolex")  # Reuse Meal's constructor; self is this rolex.
        self.eggs = eggs

    def price(self):  # Override the abstract method with real behaviour.
        return 1000 + self.eggs * 1000


class Kikomando(Meal):  # Two children of Meal: hierarchical inheritance.
    def price(self):
        return 2500


class AvocadoRolex(Rolex):  # Meal -> Rolex -> AvocadoRolex: multilevel.
    def __init__(self):
        super().__init__(eggs=2)
        self.name = "Avocado rolex"

    def price(self):
        return super().price() + 500  # Extend a working parent's method.


# ACT 3: A small extra ability; two parents deliberately offer the SAME method.
class HypeMixin:
    def describe(self):
        return f"Chef's special! {super().describe()}"


class FeaturedRolex(HypeMixin, AvocadoRolex):  # Multiple + multilevel = hybrid.
    pass  # MRO sends describe() to HypeMixin, then Meal via super().


class HomePackedLunch:  # Unrelated to Meal; still has the behaviour we need.
    name = "Home-packed lunch"

    def price(self):
        return 0

    def describe(self):
        return "Home-packed lunch: the auntie sponsorship package."


# ACT 4: The customer HAS-A wallet, rather than IS-A wallet.
class LunchBreak:
    def __init__(self, student, money):
        self.student = student
        self.wallet = LunchWallet(money)  # Owned part: composition.
        self._orders = []  # _ means internal by convention, not enforced privacy.

    @property
    def order_count(self):  # Read-only: callers cannot assign an invented count.
        return len(self._orders)

    def buy(self, meal):  # Association: the meal is passed in, not inherited.
        cost = meal.price()  # Abstraction: ask for a price; don't count its eggs.
        if cost == 0 or self.wallet.spend(cost):
            self._orders.append(meal)  # A collection of objects, not just names.
            return f"{self.student} gets {meal.name}. Lunch is saved!"
        return f"{self.student}: {meal.name} is over budget. We shall admire it."


def show_menu(items):  # Ordinary function; a list + loop recall Week 1.
    for item in items:
        print(item.describe())  # Polymorphism: SAME call, DIFFERENT results.


# ACT 5: The complete story, from the first choice to the ending.
def main():
    print("=== THE ROLEX RESCUE ===")
    menu = [Rolex(), Kikomando("Kikomando"), FeaturedRolex(), HomePackedLunch()]
    show_menu(menu)  # The unrelated packed lunch works too: duck typing.
    sarah = LunchBreak("Sarah", 5000)
    joel = LunchBreak("Joel", 3000)  # A second object has a DIFFERENT wallet.
    print(sarah.buy(menu[2]))
    print(sarah.buy(menu[1]))  # Refused; balance and order count must stay put.
    print(joel.buy(menu[1]))
    print(f"Sarah: UGX {sarah.wallet.balance:,}; orders: {sarah.order_count}")
    print(f"Joel: UGX {joel.wallet.balance:,}; orders: {joel.order_count}")
    print("MRO (look left to right):")
    for parent in FeaturedRolex.__mro__:
        print(parent.__name__)
    print("Ending: Sarah has lunch, Joel has lunch, and nobody owes the chef.")


# This familiar run guard stops the story running when imported for checking.
if __name__ == "__main__":
    main()
