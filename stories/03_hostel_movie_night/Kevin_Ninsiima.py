from story import MovieNight, create_choice


movie = create_choice("movie", title="Factory movie", megabytes=200)
music = create_choice("music", title="Factory music")
story = create_choice("story")

night = MovieNight("A4 demo", 300)
print(movie.describe())
print(music.describe())
print(story.describe())
print(night.enjoy(movie))

try:
    create_choice("unknown")
except ValueError as error:
    print("Unknown key refused:", error)