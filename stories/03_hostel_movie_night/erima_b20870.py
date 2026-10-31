empty = MovieNight("Member 5", 100)
print("Expected friendly empty message; actual:", empty.recap())
full = MovieNight("Member 5", 500)
movie = StreamedMovie("Too much movie")
print(full.enjoy(movie)) # refused; must not enter recap
print(full.enjoy(MusicSession("Music")))
print("Expected one title, one activity, 400 MB; actual:", full.recap())