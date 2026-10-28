from fair_running_order import PerformerAct
from story import AudienceWave, Dance, TalentShow


show = TalentShow("Joel", 12)
acts = [
    PerformerAct("P-101", Dance("River Crew", minutes=4)),
    PerformerAct("P-101", Dance("River Crew short", minutes=2)),
    PerformerAct("P-202", Dance("Skyline Crew", minutes=4)),
    PerformerAct("P-303", AudienceWave()),
]

plan = show.plan_and_book(acts)

print("Scheduled:")
for slot, act in enumerate(plan.scheduled, start=1):
    print(f"{slot}. {act.performer_id}: {act.performance.name}")
print("Skipped:", ", ".join(act.performer_id for act in plan.skipped))
print(f"Minutes remaining: {show.clock.remaining}")