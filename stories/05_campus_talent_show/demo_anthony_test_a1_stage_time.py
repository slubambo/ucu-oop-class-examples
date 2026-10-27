"""Anthony's demo for A1: the StageTime value object."""
from stage_time import StageTime


first = StageTime(12)
equal_value = StageTime(12)
different_value = StageTime(8)
total = first + different_value

print(f"Friendly display: {first}")
print(f"Developer display: {first!r}")
print(f"Equal values: {first == equal_value}")
print(f"Unequal values: {first == different_value}")
print(f"Sum: {total}")
print(f"Original values unchanged: {first.amount}, {different_value.amount}")

for invalid_amount in (-1, 1.5, True):
    try:
        StageTime(invalid_amount)
    except (TypeError, ValueError) as error:
        print(f"Rejected {invalid_amount!r}: {error}")