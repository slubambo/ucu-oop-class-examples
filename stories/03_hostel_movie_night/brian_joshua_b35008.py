from story import DataAmount


left = DataAmount(100)
right = DataAmount(50)
total = left + right

print("Equal values:", DataAmount(150) == total)
print("Unequal values:", DataAmount(149) == total)
print("Display:", str(total))
print("Developer value:", repr(total))
print("Operands unchanged:", left.amount == 100 and right.amount == 50)

for invalid in (-1, 1.5, True):
    try:
        DataAmount(invalid)
    except ValueError:
        print("Refused invalid amount:", repr(invalid))