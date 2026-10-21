
"""Demo for Extension 2: Mum Sends Lunch Money."""

from story import LunchWallet


# Test 1: A positive top-up should increase the balance.
wallet1 = LunchWallet(5000)

print("TEST 1: Positive top-up")
print("Expected: Returns True; balance is UGX 10,000")

result = wallet1.top_up(5000)

print(f"Actual: Returns {result}; balance is UGX {wallet1.balance:,}")
assert result is True
assert wallet1.balance == 10000


# Test 2: A zero top-up should be refused.
wallet2 = LunchWallet(5000)

print("\nTEST 2: Zero top-up")
print("Expected: Returns False; balance remains UGX 5,000")

result = wallet2.top_up(0)

print(f"Actual: Returns {result}; balance is UGX {wallet2.balance:,}")
assert result is False
assert wallet2.balance == 5000


# Test 3: A negative top-up should be refused.
wallet3 = LunchWallet(5000)

print("\nTEST 3: Negative top-up")
print("Expected: Returns False; balance remains UGX 5,000")

result = wallet3.top_up(-2000)

print(f"Actual: Returns {result}; balance is UGX {wallet3.balance:,}")
assert result is False
assert wallet3.balance == 5000


print("\nAll tests passed successfully.")
