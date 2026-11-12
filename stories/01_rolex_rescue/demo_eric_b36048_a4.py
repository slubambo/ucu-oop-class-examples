"""A4 demo: create choices, then pass them through LunchBreak.buy()."""
from story import LunchBreak, create_choice, show_menu


print("=== A4: THE CHOICE FACTORY ===")
menu = [
	create_choice("rolex", eggs=1),
	create_choice("kikomando"),
	create_choice("home_packed_lunch"),
]
show_menu(menu)

eric = LunchBreak("Eric", 2500)
print("\nNormal case: buy a one-egg Rolex")
print("Expected: purchase succeeds; balance UGX 500; orders 1")
print("Actual:", eric.buy(menu[0]))
print(f"Balance: UGX {eric.wallet.balance:,}; orders: {eric.order_count}")

before = (eric.wallet.balance, eric.order_count)
print("\nRefused case: buy Kikomando with UGX 500")
print("Expected: purchase refused; balance UGX 500; orders 1")
print("Actual:", eric.buy(menu[1]))
after = (eric.wallet.balance, eric.order_count)
print(f"Actual state unchanged: {before == after}; state: {after}")

print("\nFree choice: accept home-packed lunch")
print("Expected: purchase succeeds; balance stays UGX 500; orders 2")
print("Actual:", eric.buy(menu[2]))
print(f"Balance: UGX {eric.wallet.balance:,}; orders: {eric.order_count}")
