from story import (
        FeaturedMovie,
        MusicSession,
        MovieNight,
        StorytellingCircle,
        StreamedMovie,
        available,
)


options = [
    StreamedMovie("Full Movie"),
    MusicSession("Music"),
    FeaturedMovie("Sver movie"),
    StorytellingCircle(),
]

night = MovieNight("Kevin Ninsiima", 500)
before = (night.bundle.remaining, night.activities)

print("Expected titles: Music, Sver movie, Storytelling circle")
print("Available titles:", [item.title for item in available(options, 350)])
print("Expected empty list:actual:", available(options, -1))
print("State unchanged:", before == (night.bundle.remaining, night.activities))