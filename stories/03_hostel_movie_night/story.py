"""Hostel Movie Night: the group must choose what fits its data budget.
Run: python3 story.py. Data costs are invented, not provider estimates.
"""
from abc import ABC, abstractmethod


# ACT 1: Data belongs to an object that controls how much can be used.
class DataBundle:
    def __init__(self, megabytes):
        self.remaining = megabytes  # Validate the initial value via the setter.

    @property
    def remaining(self):
        return self.__remaining  # Double underscore: name mangling, not secrecy.

    @remaining.setter
    def remaining(self, amount):
        if amount < 0:
            raise ValueError("Remaining data cannot be negative.")
        self.__remaining = amount

    def use(self, amount):
        if amount <= 0 or amount > self.remaining:
            return False
        self.remaining = self.remaining - amount
        return True


# ACT 2: Every entertainment option answers the same two questions.
class Entertainment(ABC):
    location = "Mukono hostel lounge"  # Shared class attribute.

    def __init__(self, title):
        self.title = title  # Instance attribute: each option has its own title.

    def describe(self):
        return f"{self.title}: {self.data_cost()} MB at {self.location}"

    @abstractmethod
    def data_cost(self):
        pass  # Can't create an incomplete Entertainment object.


class StreamedMovie(Entertainment):  # Single inheritance: IS-A Entertainment.
    def __init__(self, title, megabytes=700):
        super().__init__(title)  # Reuse the parent's constructor.
        self.megabytes = megabytes

    def data_cost(self):
        return self.megabytes  # Concrete override.


class MusicSession(Entertainment):  # Sibling: hierarchical inheritance.
    def data_cost(self):
        return 100


class DataSaverMovie(StreamedMovie):  # Three levels: multilevel inheritance.
    def data_cost(self):
        return super().data_cost() // 2  # Extend, rather than duplicate, pricing.


# ACT 3: The mixin adds presentation without becoming the whole movie.
class HypeMixin:
    def describe(self):
        return f"Bring your own popcorn! {super().describe()}"


class FeaturedMovie(HypeMixin, DataSaverMovie):
    pass  # Multiple inheritance + multilevel inheritance: hybrid.


class StorytellingCircle:  # Unrelated class with the expected methods.
    title = "Hostel storytelling circle"

    def data_cost(self):
        return 0

    def describe(self):
        return "Storytelling circle: zero MB, unlimited plot twists."


# ACT 4: MovieNight HAS-A bundle; it is not a kind of bundle.
class MovieNight:
    def __init__(self, host, megabytes):
        self.host = host
        self.bundle = DataBundle(megabytes)  # Owned part: composition.
        self._watched = []  # _ means internal by convention.
        self.entertainment = None

    @property
    def activities(self):  # Read-only; a count derived from the real list.
        return len(self._watched)

    def enjoy(self, entertainment):
        self.entertainment = entertainment  # Borrowed, swappable: aggregation.
        needed = entertainment.data_cost()  # Abstraction: HOW is hidden here.
        if needed == 0 or self.bundle.use(needed):
            self._watched.append(entertainment)  # Store actual collaborating objects.
            return f"{self.host}'s group enjoys {entertainment.title}."
        return f"{entertainment.title} needs too much data. Nobody hotspot secretly!"


def show_options(options):  # Week 1 function + list + loop.
    for option in options:
        print(option.describe())  # Same call, different results: polymorphism.


# Later-topic contribution — David:
# A2 custom exceptions for clear, state-safe movie request failures.
class MovieChoiceError(Exception):
    pass


class MovieRequestError(Exception):
    pass


class MovieResourceError(Exception):
    pass


# Later-topic contribution — David:
# A2 strict coordinator that validates requests before changing MovieNight state.
class StrictMovieNight(MovieNight):
    def safe_enjoy(self, choice):
        if choice is None:
            raise MovieChoiceError("Choose an activity before starting movie night.")

        needed = choice.data_cost()
        if type(needed) is not int or needed < 0:
            raise MovieRequestError(
                "The activity must quote a non-negative whole MB cost."
            )
        if needed > self.bundle.remaining:
            raise MovieResourceError(
                f"{choice.title} needs {needed} MB, but only "
                f"{self.bundle.remaining} MB remains."
            )
        return super().enjoy(choice)


def main():
    print("=== HOSTEL MOVIE NIGHT ===")
    print("Faith promised a movie night. Her bundle has other ideas.")
    options = [StreamedMovie("Mukono Mystery"), MusicSession("Afrobeats break"),
               FeaturedMovie("Mukono Mystery: data saver"), StorytellingCircle()]
    show_options(options)  # StorytellingCircle works too: duck typing.
    faith = MovieNight("Faith", 500)
    david = MovieNight("David", 200)  # Separate bundles; no shared list bug.
    print(faith.enjoy(options[0]))  # 700 MB: refused.
    print(faith.enjoy(options[2]))  # 350 MB.
    print(faith.enjoy(options[1]))  # 100 MB.
    print(faith.enjoy(options[3]))  # Swap to an offline activity.
    print(david.enjoy(options[1]))
    print(f"Faith: {faith.bundle.remaining} MB; activities: {faith.activities}")
    print(f"David: {david.bundle.remaining} MB; activities: {david.activities}")
    print("MRO (look left to right):")
    for parent in FeaturedMovie.__mro__:
        print(parent.__name__)
    print("Ending: the stories are dramatic; the data balance is peaceful.")


if __name__ == "__main__":
    main()
