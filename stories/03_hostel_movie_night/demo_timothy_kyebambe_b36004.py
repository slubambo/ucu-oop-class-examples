"""Demo for Timothy Kyebambe B36004.
Extension 4: What fits within the available megabytes without changing inputs."""

from story import (
    FeaturedMovie,
    MovieNight,
    MusicSession,
    StorytellingCircle,
    StreamedMovie,
    available,
    show_options,
)
def run_demo():
    print(" === EXTENSION 4 DEMO: available(options, megabytes) ===\n")

    # 1. Normal case: Check what fits a 350 MB budget using a MovieNight coordinator.
    print("-- Check 1: Normal Case (350 MB available) --  ")
    options_normal = [
        StreamedMovie("Mukono Mystery"),            # 700 MB
        MusicSession("Afrobeats break"),          # 100 MB
        FeaturedMovie("Mukono Mystery: data saver"),  # 350 MB
        StorytellingCircle(),  # 0 MB
    ]
    faith_night = MovieNight("Faith", 350)

    # Record state before calling available() to prove read-only behaviour
    options_before = list(options_normal)
    remaining_before = faith_night.bundle.remaining
    history_before = faith_night.activities

    fitting = available(options_normal, faith_night.bundle.remaining)
    fitting_titles = [opt.title for opt in fitting]

    print(
        "Expected fitting titles: "
        "['Afrobeats break', 'Mukono Mystery: data saver', 'Hostel storytelling circle']"
    )
    print(f"Actual fitting titles: {fitting_titles}")
    print("\nShowing fitting options using existing show_options ():")
    show_options(fitting)

    print("\n--- Read-Only Verification (Resource, History, and Options Unchanged) ---")
    print(f"Expected data remaining: {remaining_before} MB | Actual: {faith_night.bundle.remaining} MB")
    print(f"Expected activities count: {history_before} | Actual: {faith_night.activities}")
    print(f"Expected options list unchanged: True | Actual: {options_normal == options_before}")

    # 2. Boundary / Empty case: Separate objects so Check 1 does not affect Check 2
    print("\n-- Check 2: Boundary / Empty Case (0 MB available) --  ")
    options_boundary = [
        StreamedMovie("Mukono Mystery"),            # 700 MB
        MusicSession("Afrobeats break"),          # 100 MB
        StorytellingCircle(),  # 0 MB
    ]
    zero_fits = available(options_boundary, 0)
    print("Expected fitting titles for 0 MB: ['Hostel storytelling circle']")
    print(f"Actual fitting titles for 0 MB: {[opt.title for opt in zero_fits]}")

    print("\n--- Check 3: Empty Case (Paid options only with 50 MB budget) ---")
    paid_options = [
        StreamedMovie("Mukono Mystery"),            # 700 MB
        MusicSession("Afrobeats break"),          # 100 MB
    ]
    none_fit = available(paid_options, 50)
    print("Expected fitting titles for 50 MB: []")
    print(f"Actual fitting titles for 50 MB: {[opt.title for opt in none_fit]}")

if __name__ == "__main__":
    run_demo()

    