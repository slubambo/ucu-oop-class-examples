##Demo file for extension 6##
from story import LunchBreak, GroundnutRolex, Rolex, show_menu

def main():
    print("Extension 6")

items = [
    Rolex(),
    GroundnutRolex(),
]
show_menu(items)

##With a sufficient balance##
sarah = LunchBreak("Sarah", 5000)
gnut_rolex = GroundnutRolex()
print(f"Item: {gnut_rolex.name}")
print(f"Price: {gnut_rolex.price():,}")

sarah_buy = sarah.buy(gnut_rolex)
print(f"Result: {sarah_buy}")
print(f"Balance: UGX{sarah.wallet.balance:,}")

##With an insufficient balance##
joel = LunchBreak("Joel", 2000)
joel_buy = joel.buy(gnut_rolex)
print(f"Result: {joel_buy}")
print(f"Balance: UGX{joel.wallet.balance:,}")

if __name__ == "__main__":
    main()

##How to run demo file##
##Am using linux:
# python3 stories/01_rolex_rescue/demo_jordan_S26B13-131.py