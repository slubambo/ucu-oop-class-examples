from story import ComedyClip, MovieNight, show_options


normal = ComedyClip("Campus comedy hour")

show_options([normal])

night = MovieNight("Brian Joshua", 50)
print("Expected: Brian Joshua's group enjoys Campus comedy hour.")
print("Actual:",night.enjoy(normal))

refused = ComedyClip("Comedy on an empty bundle")

empty_night = MovieNight("Brian Joshua", 0)
print(empty_night.enjoy(refused))

print(
    f"Expected: refused; actual activities={empty_night.activities},"
    f"data={empty_night.bundle.remaining}"
)