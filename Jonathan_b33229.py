from abc import ABC, abstractmethod
class TripPurse:
    def __init__(self, money):
        self.balance = money

    @property
    def balance(self):
        return self.__balance

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
      
class Transport(ABC):
    currency = "UGX"

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_fare(self, distance_km):
        pass

    def describe(self):
        return f"{self.name} uses currency in {self.currency}"

class BodaBoda(Transport):
    def __init__(self, name, rate_per_km=2000):
        super().__init__(name)
        self.rate_per_km = rate_per_km

    def calculate_fare(self, distance_km):
        return distance_km * self.rate_per_km


class Taxi(Transport):
    def __init__(self, name, flat_fare=5000):
        super().__init__(name)
        self.flat_fare = flat_fare

    def calculate_fare(self, distance_km):
        return self.flat_fare


# ACT 4: Test/Simulation
if __name__ == "__main__":
    purse = TripPurse(20000)
    boda = BodaBoda("SafeBoda")
    fare = boda.calculate_fare(5)
    print(f"Fare: {fare} {boda.currency}")
    if purse.pay(fare):
        print(f"Paid! Remaining balance: {purse.balance} UGX")
