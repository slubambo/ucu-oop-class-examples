"""Demo for A4: a factory creates choices for the existing TalentShow."""
from factory import create_choice
from story import TalentShow


dance = create_choice("dance", crew="Apex", minutes=3)
poetry = create_choice("poetry", name="Mirembe's poem")
wave = create_choice("audience_wave")
print(f"Created: {dance.name}, {poetry.name}, and {wave.name}")

show = TalentShow("Joel", 4)
print(show.book(dance))
remaining_before_refusal = show.clock.remaining
count_before_refusal = show.act_count
print(show.book(poetry))
print(
    "Refused booking preserved state:",
    show.clock.remaining == remaining_before_refusal
    and show.act_count == count_before_refusal,
)

try:
    create_choice("unknown")
except ValueError as error:
    print(f"Unknown choice handled: {error}")
