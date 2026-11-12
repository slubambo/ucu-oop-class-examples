"""Joy's demo for A1: previewing a mixed-choice running time."""
from story import AudienceWave, Dance, Poetry, TalentShow


show = TalentShow("Joel", 15)
show.book(AudienceWave())
choices = [
    Dance("Apex", minutes=6),
    Poetry("Mirembe's poem"),
    AudienceWave(),
]
remaining_before = show.clock.remaining
count_before = show.act_count

print(f"Mixed-choice preview: {show.preview_total(choices)}")
print(f"Empty preview: {show.preview_total([])}")
print(
    "Show unchanged:",
    show.clock.remaining == remaining_before and show.act_count == count_before,
)