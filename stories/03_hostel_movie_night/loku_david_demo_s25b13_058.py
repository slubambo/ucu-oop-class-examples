from story import DataBundle


bundle = DataBundle(100)
print(
    "Expected: True, 250 MB; actual:",
    bundle.add_data(150),
    bundle.remaining,
)

zero = DataBundle(100)
print(
    "Expected: False, 100 MB; actual:",
    zero.add_data(0),
    zero.remaining,
)

negative = DataBundle(100)
print(
    "Expected: False, 100 MB; actual:",
    negative.add_data(-20),
    negative.remaining,
)