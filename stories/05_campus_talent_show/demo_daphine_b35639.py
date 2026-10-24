from story import TalentShow, Dance, Poetry


print("=== EXTENSION 5: RUNNING ORDER ===")

empty_show = TalentShow("Daphine", 10)

print("Empty show:")
print(empty_show.running_order())

show = TalentShow("Daphine", 10)
first = Dance("Opening dancers", minutes=3)
second = Poetry("Spoken word")

show.book(first)
show.book(second)

print("\nBooked show:")
print(show.running_order())

print("\nExpected acts: 2")
print("Expected minutes left: 3")
