"""Demo for Extension 5: Movie-night recap - Alvin (access number b33226).
Run from the main repository folder:
    py -3 stories/03_hostel_movie_night/demo_alvin_b33226.py
The demo imports from story.py; the original main() is not changed.
"""
from story import DataSaverMovie, MusicSession, StorytellingCircle, StreamedMovie, MovieNight


def check(label, expected, actual):
    print(f"{label}\n  Expected: {expected}\n  Actual:   {actual}\n")


# CASE 1 (normal): a recap after three successful activities.
print("=== Case 1: recap after a real evening ===")
night = MovieNight("Faith", 500)
night.enjoy(DataSaverMovie("Mukono Mystery: data saver"))  # 350 MB.
night.enjoy(MusicSession("Afrobeats break"))               # 100 MB.
night.enjoy(StorytellingCircle())                          # 0 MB.
expected = ("Faith's recap:3 activity(ies).(Mukono Mystery: data saver,"
            "Afrobeats break,Hostel storytelling circle);50 MB Left.")
check("recap() after three successes", expected, night.recap())

# Recap only reads: show the resource and history are unchanged afterwards.
print(f"  Bundle still: {night.bundle.remaining} MB; activities still: {night.activities}")
print(f"  Same recap again: {night.recap()}\n")

# CASE 2 (empty): a recap before anything has happened.
print("=== Case 2: recap on a fresh night (nothing has happened) ===")
quiet = MovieNight("David", 200)
check("recap() with no activities",
      "David's group has not watched anything", quiet.recap())
print(f"  Bundle untouched: {quiet.bundle.remaining} MB; activities: {quiet.activities}\n")

# CASE 3 (refused attempt): a refused request must not appear in the recap.
print("=== Case 3: refused requests stay out of the recap ===")
refused = MovieNight("Grace", 500)
refused.enjoy(StreamedMovie("Mukono Mystery"))  # 700 MB: refused.
check("recap() after one refusal",
      "Grace's group has not watched anything", refused.recap())
print(f"  Bundle untouched: {refused.bundle.remaining} MB; activities: {refused.activities}\n")

# CASE 4 (boundary): recap still works when the bundle is exactly empty.
print("=== Case 4: recap with an empty bundle ===")
spent = MovieNight("Hope", 100)
spent.enjoy(MusicSession("Afrobeats break"))  # 100 MB: bundle drops to 0.
check("recap() at 0 MB",
      "Hope's recap:1 activity(ies).(Afrobeats break);0 MB Left.", spent.recap())

print("All recap checks finished: reads only, changes nothing.")