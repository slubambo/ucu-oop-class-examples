from story import LunchWallet

print("=== Extension 2: Mum sends lunch money (Stacey, S25B13/079) ===")

# Normal case: positive top-up
wallet = LunchWallet(5000)
print("\nNormal case: top up 2000 on a balance of 5000")
print("Expected: returns True, balance 7000")
result = wallet.top_up(2000)
print("Actual: returns", result, ", balance", wallet.balance)

# Refused case: zero
wallet2 = LunchWallet(5000)
print("\nRefused case: top up 0")
print("Expected: returns False, balance 5000")
result = wallet2.top_up(0)
print("Actual: returns", result, ", balance", wallet2.balance)

# Refused case: negative
wallet3 = LunchWallet(5000)
print("\nRefused case: top up -500")
print("Expected: returns False, balance 5000")
result = wallet3.top_up(-500)
print("Actual: returns", result, ", balance", wallet3.balance)