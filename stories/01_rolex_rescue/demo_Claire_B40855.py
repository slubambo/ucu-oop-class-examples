#demo_Claire_B40855.py
from story import LunchBreak, Rolex

def run_demo():
    print("=== Demo for Extension 5:First purchase summary ===")

    #before any purchase
    print("\n--- Test 1: Empty Receipt(before purchase) ---")
    Sarah_empty = LunchBreak("Sarah", 5000)
    print(Sarah_empty.receipt())

    #After a successful purchase
    print("\n--- Test 2: Normal Receipt(after purchase) ---")
    Sarah_normal = LunchBreak("Sarah", 5000)
    rolex_item = Rolex(eggs=2)

    print("purchase result:",Sarah_normal.buy(rolex_item))
    print("\nGenerated Receipt:")
    print(Sarah_normal.receipt())

    #Ensuring receipt doesn't alter state/balance
    print("\n--- Test 3: Read-only verifiction---")
    balance_before = Sarah_normal.wallet.balance
    count_before = Sarah_normal.order_count

    #Call receipt multiple times
    _ = Sarah_normal.receipt()
    _ = Sarah_normal.receipt()

    Balance_after = Sarah_normal.wallet.balance
    Count_after = Sarah_normal.order_count

    print(f"balance before receipt calls: UGx {balance_before:,} After: UGX {Balance_after:,}")
    print(f"Order count before receipt calls: {count_before} After: {Count_after}")

    assert balance_before ==Balance_after, "Error: receipt() changed the wallet balance!"
    assert count_before == Count_after, "Error: receipt() changed the order count!"
    print("Check passed: State and balance remained completely unchanged.")

if __name__ == "__main__":
    run_demo()