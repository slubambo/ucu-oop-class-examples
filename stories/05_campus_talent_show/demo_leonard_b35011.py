"""Demo for Extension 6: LightningDance."""
from story import LightningDance


# Normal case: Dance's default 6 minutes becomes ShortDance's 3,
# then LightningDance reduces it to 2 minutes.
normal = LightningDance("Flash Crew")
expected_normal = 2
actual_normal = normal.duration()
print(f"Normal case: expected {expected_normal}, got {actual_normal}")

# Boundary case: a 2-minute dance becomes 1 minute in ShortDance,
# so LightningDance must keep the result at the minimum of 1 minute.
boundary = LightningDance("Tiny Crew", minutes=2)
expected_boundary = 1
actual_boundary = boundary.duration()
print(f"Boundary case: expected {expected_boundary}, got {actual_boundary}")
