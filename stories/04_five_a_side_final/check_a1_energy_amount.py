from energy_amount import EnergyAmount

# Normal case
a = EnergyAmount(3000)
b = EnergyAmount(500)
assert str(a) == "3,000 energy"
assert repr(a) == "EnergyAmount(3000)"
assert a == EnergyAmount(3000)
assert a != b
total = a + b
assert total.amount == 3500
assert a.amount == 3000 and b.amount == 500   # originals unchanged

# Boundary case
assert EnergyAmount(0).amount == 0
assert (EnergyAmount(0) + EnergyAmount(0)).amount == 0

# Invalid / refused cases
for bad in (-1, 1.5, True):
    try:
        EnergyAmount(bad)
        raise AssertionError(f"{bad!r} should have been refused")
    except (TypeError, ValueError):
        pass

assert (a == 3000) is False       # unsupported type is not equal
try:
    a + 5
    raise AssertionError("adding a plain int should fail")
except TypeError:
    pass

print("All A1 EnergyAmount checks passed.")