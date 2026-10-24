from story import ShowClock


print("=== EXTENSION 2: MC GETS EXTRA TIME ===")

clock = ShowClock(5)

print("Initial minutes:", clock.remaining)

print("\nNormal case: extend by 3 minutes")
result = clock.extend(3)
print("Expected result: True")
print("Actual result:", result)
print("Expected minutes: 8")
print("Actual minutes:", clock.remaining)

print("\nBoundary case: extend by zero minutes")
before_zero = clock.remaining
result = clock.extend(0)
print("Expected result: False")
print("Actual result:", result)
print("Expected minutes unchanged:", before_zero)
print("Actual minutes:", clock.remaining)

print("\nBoundary case: extend by negative minutes")
before_negative = clock.remaining
result = clock.extend(-2)
print("Expected result: False")
print("Actual result:", result)
print("Expected minutes unchanged:", before_negative)
print("Actual minutes:", clock.remaining)