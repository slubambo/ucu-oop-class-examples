"""Interactive Hostel Movie Night - Alvin (b33226), bonus demo for Extension 5.
You type the host name and bundle size, then pick activities by number.
The night ends with recap(), the Extension 5 feature, so you can see it live.
This file does NOT change story.py - it imports the classes from it.
Run from the main repository folder:
    py -3 stories/03_hostel_movie_night/interactive_alvin_b33226.py
"""
from story import (DataSaverMovie, FeaturedMovie, MovieNight, MusicSession,
                   StreamedMovie, StorytellingCircle)


def ask_number(prompt, minimum=0):
    """Keep asking until the user types a whole number of at least `minimum`."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)  # Week 1 skill: turning text into a number safely.
        except ValueError:
            print("Please type a whole number, not words.")
            continue
        if value < minimum:
            print(f"The number must be {minimum} or more.")
            continue
        return value


def build_menu():
    """The same choice family from the story, ready for the user to pick."""
    return [StreamedMovie("Mukono Mystery"),
            MusicSession("Afrobeats break"),
            DataSaverMovie("Mukono Mystery: data saver"),
            FeaturedMovie("Mukono Mystery: premiere"),
            StorytellingCircle()]


def run():
    print("=== HOSTEL MOVIE NIGHT: YOUR VERSION ===")
    host = input("Who is hosting tonight? ").strip() or "Faith"
    megabytes = ask_number("How many MB are on the bundle? ", minimum=0)
    night = MovieNight(host, megabytes)  # The coordinator owns the DataBundle.
    options = build_menu()

    print("\nTonight's options:")
    for number, option in enumerate(options, start=1):
        print(f"  {number}. {option.describe()}")
    print("  6. End the night")

    while True:
        choice = input("\nPick a number: ").strip()
        if choice == "6":
            break
        if not choice.isdigit() or not 1 <= int(choice) <= len(options):
            print("That is not one of the menu numbers. Try again.")
            continue
        option = options[int(choice) - 1]
        print(night.enjoy(option))  # DataBundle still refuses what does not fit.
        print(f"Bundle now: {night.bundle.remaining} MB; "
              f"activities so far: {night.activities}")

    print()  # The night ends with the Extension 5 recap.
    print(night.recap())
    print("Ending: the stories are dramatic; the data balance is peaceful.")


if __name__ == "__main__":
    run()