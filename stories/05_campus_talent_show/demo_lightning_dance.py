"""Demo for the Lightning Dance extension."""
from story import LightningDance, TalentShow


print("=== LIGHTNING DANCE DEMO ===")

# Normal case:- enough time for a shorter performance.
show = TalentShow("Joel", 8)
print("Normal case")
print(show.book(LightningDance("Storm Crew")))
print(f"Minutes left: {show.clock.remaining}; acts: {show.act_count}")

# Boundary case:- minimum duration must stay at 1 minute.
show2 = TalentShow("Joel", 1)
print("\nBoundary case")
print(show2.book(LightningDance("Flash Crew")))
print(f"Minutes left: {show2.clock.remaining}; acts: {show2.act_count}")

# Refused case:- no time left for a 1-minute act.
show3 = TalentShow("Joel", 0)
print("\nRefused case")
print(show3.book(LightningDance("Rain Crew")))
print(f"Minutes left: {show3.clock.remaining}; acts: {show3.act_count}")
