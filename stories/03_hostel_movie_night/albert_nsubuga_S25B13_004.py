from story import BoardGame, MovieNight, show_options


game = BoardGame()

show_options([game])

night = MovieNight("Albert Nsubuga", 0)

print("Expected: Albert Nsubuga's grroup enjoys Ludo night.")
print("Actual:" night.enjoy(game))
print()