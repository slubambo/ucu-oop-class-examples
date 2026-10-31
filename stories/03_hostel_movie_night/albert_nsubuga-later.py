from story import DataAmount, MovieNight, MusicSession, StorytellingCircle, StreamedMovie


night = MovieNight("A1 preview", 500)
choices = [
    StreamedMovie("Movie", 200),
    MusicSession("Music"),
    StorytellingCircle(),
]
before = (night.bundle.remaining, night.activities)
preview = night.preview_total(choices)

print("Preview:", preview)
print("Expected: 300 MB; actual:", preview.amount)
print("State unchanged:", before == (night.bundle.remaining, night.activities))
print("Empty preview:", night.preview_total([]) == DataAmount(0))
