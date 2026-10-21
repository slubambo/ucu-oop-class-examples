from story import MovieNight


class MovieChoiceError(Exception):
    """Raised when no movie-night choice is supplied."""


class MovieRequestError(Exception):
    """Raised when a choice requests an invalid amount of data."""


class MovieResourceError(Exception):
    """Raised when a valid choice needs more data than remains."""


class StrictMovieNight(MovieNight):
    def safe_enjoy(self, choice):
        if choice is None:
            raise MovieChoiceError("No entertainment choice was supplied.")

        needed = choice.data_cost()
        if needed < 0:
            raise MovieRequestError(
                f"{choice.title} has an invalid data requirement: {needed} MB."
            )
        if needed > self.bundle.remaining:
            raise MovieResourceError(
                f"{choice.title} needs {needed} MB, but only "
                f"{self.bundle.remaining} MB remain."
            )
        return self.enjoy(choice)
