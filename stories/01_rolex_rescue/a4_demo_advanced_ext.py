from story import LunchBreak, show_menu
from a4_later_topics import create_choice

menu = [
    create_choice("rolex", eggs=1),
    create_choice("kikomando"),
    create_choice("home_packed_lunch"),
]
show_menu(menu)

sarah = LunchBreak("Sarah", 4000)
for choice in menu:
    print(sarah.buy(choice))
print(f"Remaining: UGX {sarah.wallet.balance:,}")
print(f"Successful orders: {sarah.order_count}")

try:
    create_choice("mystery_meal")
except ValueError as error:
    print("Unknown option refused:", error)