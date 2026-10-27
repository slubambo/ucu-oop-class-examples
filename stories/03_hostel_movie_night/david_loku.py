from story import (
    MovieChoiceError,
    MovieRequestError,
    MovieResourceError,
    StrictMovieNight,
    StorytellingCircle,
    StreamedMovie,
)


class InvalidQuote:
    title = "Invalid quote"

    def data_cost(self):
        return -1


attempts = [
    (None, MovieChoiceError),
    (InvalidQuote(), MovieRequestError),
    (StreamedMovie("Too large", 900), MovieResourceError),
    (StorytellingCircle(), None),
]

for choice, expected_error in attempts:
    night = StrictMovieNight("A2 demo", 100)
    before = (night.bundle.remaining, night.activities)
    try:
        result = night.safe_enjoy(choice)
    except MovieChoiceError as error:
        print("Handled:", type(error).__name__, str(error))
    except MovieRequestError as error:
        print("Handled:", type(error).__name__, str(error))
    except MovieResourceError as error:
        print("Handled:", type(error).__name__, str(error))
    else:
        print("Actual:", result)
        print("Expected: success")
    finally:
        print("State:", before, "->", (night.bundle.remaining, night.activities))