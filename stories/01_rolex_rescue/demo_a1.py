from later_topics import LunchMoney
from story import LunchBreak, Rolex, Kikomando

print("A1: LunchMoney demonstration")

money1 = LunchMoney(3000)
money2 = LunchMoney(3000)
money3 = LunchMoney(1500)

print("Display:", str(money1))
print("Representation:", repr(money1))
print("Equal amounts:", money1 == money2)
print("Unequal amounts:", money1 == money3)
print("Addition:", money1 + money3)

sarah = LunchBreak("Sarah", 10000)

before_balance = sarah.wallet.balance
before_orders = sarah.order_count

choices = [Rolex(), Kikomando()]
total = sarah.preview_total(choices)

print("Total preview:", total)
print("Balance unchanged:", sarah.wallet.balance == before_balance)
print("Order history unchanged:", sarah.order_count == before_orders)

for invalid in [-1, 2.5, True]:
    try:
        LunchMoney(invalid)
    except ValueError as error:
        print(f"Invalid value {invalid!r} refused: {error}")
        