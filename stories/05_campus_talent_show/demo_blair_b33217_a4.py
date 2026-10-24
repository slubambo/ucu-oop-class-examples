from factory import create_choice
from story import TalentShow


print("=== A4: CHOICE FACTORY ===")

dance = create_choice("dance", crew="Blair dancers", minutes=3)
poetry = create_choice("poetry", name="Blair's poem")
wave = create_choice("audience_wave")

print(dance.describe())
print(poetry.describe())
print(wave.describe())

show = TalentShow("Blair", 3)
print(show.book(dance))
print("Acts:", show.act_count)
print("Minutes left:", show.clock.remaining)

try:
    create_choice("unknown")
except ValueError as error:
    print("Friendly error:", error)

print("Factory demo complete.")