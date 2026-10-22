"""
Extension 4 demo: Cheapest ride.
Author: Andia Rose 
Access number :B34928

Run from the main repository folder:
  Windows:        py -3 stories/02_mukono_mission/demo_NAME_ACCESSNUMBER.py
"""
from story import Boda, Taxi, CheerfulStudentBoda, WalkWithFriend, Journey,cheapest

print("=== Extension 4: Cheapest ride ===")

# Check 1 (normal case): the cheapest option is found.
print("\nCheck 1 (normal): boda UGX 3,000, taxi UGX 2,000, student boda UGX 2,500")
options = [Boda("Kato"), Taxi("Mukono taxi"), CheerfulStudentBoda("Nambi")]
winner = cheapest(options, 3)
print("Expected: Mukono taxi")
print(f"Actual:   {winner.name}")

# Check 2 (normal case): a free option beats paid options.
print("\nCheck 2 (normal): a walk with a friend costs UGX 0")
options = [Boda("Kato"), Taxi("Mukono taxi"), WalkWithFriend()]
winner = cheapest(options, 3)
print("Expected: Walk with a friend")
print(f"Actual:   {winner.name}")

# Check 3 (tie case): equal fares keep the first option.
print("\nCheck 3 (tie): two taxis, both UGX 2,000. The first one must win.")
first = Taxi("First taxi")
second = Taxi("Second taxi")
winner = cheapest([first, second], 3)
print("Expected: First taxi")
print(f"Actual:   {winner.name}")

# Check 4 (empty case): no options gives None.
print("\nCheck 4 (empty): an empty list")
print("Expected: None")
print(f"Actual:   {cheapest([], 3)}")

# Check 5 (read-only): cheapest() must not spend money or add legs.
print("\nCheck 5 (read-only): Amina has UGX 5,000 and nothing changes")
amina = Journey("Amina", 5000)
cheapest([Boda("Kato"), Taxi("Mukono taxi")], 3)
print("Expected: money left 5000, legs 0")
print(f"Actual:   money left {amina.purse.balance}, legs {amina.completed_legs}")