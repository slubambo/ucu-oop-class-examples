
from story import Juice, LunchBreak, show_menu

# Create and display the Passion Juice menu item.
juice = Juice()
show_menu([juice])

# Test 1: Sarah has enough money.
sarah = LunchBreak("Sarah", 2000)

print("\nTEST 1: Successful purchase")
print("Expected: Sarah gets Passion Juice. Lunch is saved!")
print("Actual:", sarah.buy(juice))
print("Expected balance: UGX 500")
print("Actual balance: UGX", sarah.wallet.balance)
print("Expected orders: 1")
print("Actual orders:", sarah.order_count)

# Test 2: Joel does not have enough money.
joel = LunchBreak("Joel", 1000)

print("\nTEST 2: Refused purchase")
print("Expected: Purchase refused; balance stays UGX 1000.")
print("Actual:", joel.buy(juice))
print("Expected balance: UGX 1000")
print("Actual balance: UGX", joel.wallet.balance)
print("Expected orders: 0")
print("Actual orders:", joel.order_count)
