from story import CousinLift, Journey, compare

print("--- Extension 3 Demo ---")
lift = CousinLift("Cousin Brian's Vitz")


print("[Test 1: Quote Fare Verification]")
print(f"Expected: 0 | Actual: {lift.quote_fare(10)}")


print("\n[Test 2: Integration via compare() & Journey]")
compare([lift], 10)
journey = Journey("Amina", 500)
print(journey.travel(lift, 10))
print(f"Legs Completed: {journey.completed_legs} | Balance: {journey.purse.balance}")
