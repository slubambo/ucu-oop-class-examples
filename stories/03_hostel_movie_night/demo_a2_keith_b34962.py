from story import StreamedMovie
from strict_movie import (
    MovieChoiceError,
    MovieRequestError,
    MovieResourceError,
    StrictMovieNight,
)


class BadChoice:
    title = "Bad choice"

    def data_cost(self):
        return -5


def attempt(night, choice, label):
    try:
        print(f"{label}: {night.safe_enjoy(choice)}")
    except MovieChoiceError as error:
        print(f"{label}: No choice supplied: {error}")
    except MovieRequestError as error:
        print(f"{label}: Invalid request: {error}")
    except MovieResourceError as error:
        print(f"{label}: Not enough data: {error}")
    finally:
        print(
            f"Attempt finished. Remaining: {night.bundle.remaining} MB, "
            f"activities: {night.activities}"
        )


def main():
    night = StrictMovieNight("Faith", 1000)
    attempt(night, StreamedMovie("Mukono Mystery"), "Valid movie")
    attempt(night, None, "Missing choice")
    attempt(night, BadChoice(), "Bad choice")
    attempt(night, StreamedMovie("Second movie"), "Too-large movie")


if __name__ == "__main__":
    main()
