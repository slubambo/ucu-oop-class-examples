"""Campus Talent Show: a cheerful MC must keep the show on time.
Run: python3 story.py. All acts and timings are fictional classroom examples.
"""
from abc import ABC, abstractmethod

class ShowChoiceError(Exception):
    """The selected object is not a usable talent-show act."""


class ShowRequestError(Exception):
    """The act contains an invalid booking request."""


class ShowResourceError(Exception):
    """The show does not have enough time for a valid act."""

# ACT 1: Time is a resource with a rule: don't schedule negative minutes.
class ShowClock:
    def __init__(self, minutes):
        self.remaining = minutes  # Initialisation goes through the setter.

    @property
    def remaining(self):
        return self.__remaining  # Name mangling; not an access-control system.

    @remaining.setter
    def remaining(self, amount):
        if amount < 0:
            raise ValueError("Show minutes cannot be negative.")
        self.__remaining = amount

    def reserve(self, minutes):
        if minutes <= 0 or minutes > self.remaining:
            return False
        self.remaining = self.remaining - minutes
        return True

    
    def extend(self, minutes):
        if minutes <= 0:
            return False

        self.remaining = self.remaining + minutes
        return True


# ACT 2: Every performance must tell the MC its duration.
class Performance(ABC):
    venue = "UCU student talent afternoon"  # Class attribute: shared fact.

    def __init__(self, name):
        self.name = name  # Instance attribute: this specific act's name.

    def describe(self):
        return f"{self.name}: {self.duration()} minutes at {self.venue}."

    @abstractmethod
    def duration(self):
        pass  # A bare Performance object is incomplete.


class Dance(Performance):  # IS-A Performance: single inheritance.
    def __init__(self, crew, minutes=6):
        super().__init__(f"{crew} dance")
        self.minutes = minutes

    def duration(self):
        return self.minutes  # Override the abstract method.

class Comedy(Performance):
    def duration(self):
        return 2


class Poetry(Performance):  # Shared parent: hierarchical inheritance.
    def duration(self):
        return 4


class ShortDance(Dance):  # Performance -> Dance -> ShortDance: multilevel.
    def duration(self):
        return super().duration() // 2  # Extend a parent's implementation.


# ACT 3: One extra capability joins the existing dance family.
class ApplauseMixin:
    def describe(self):
        return f"Mukono, make some noise! {super().describe()}"


class HeadlineDance(ApplauseMixin, ShortDance):
    pass  # Multiple parents and several levels: a hybrid hierarchy.


class AudienceWave:  # No Performance inheritance: the shared behaviour is enough.
    name = "Audience wave"

    def duration(self):
        return 1

    def describe(self):
        return "Audience wave: one minute, everybody gets to be famous."

class ThankYouSpeech:
    def __init__(self, name):
        self.name = name

    def duration(self):
        return 1

    def describe(self):
        return (
            f"{self.name}: one-minute thank-you speech "
            "at UCU student talent afternoon."
        )

# ACT 4: The show HAS-A clock; it borrows and swaps performance objects.
class TalentShow:
    def __init__(self, mc, minutes):
        self.mc = mc
        self.clock = ShowClock(minutes)  # Owned part: composition.
        self._lineup = []  # _ marks intended internal use, by convention.
        self.performance = None

    @property
    def act_count(self):  # Read-only: reflects the actual booked lineup.
        return len(self._lineup)

    def book(self, performance):
        self.performance = performance  # Borrowed part: aggregation.
        minutes = performance.duration()  # Abstraction: MC doesn't count dance steps.
        if self.clock.reserve(minutes):
            self._lineup.append(performance)  # Collaborating objects in a collection.
            return f"MC {self.mc} books {performance.name}."
        return f"No slot for {performance.name}. The timetable has entered the chat."

    def cancel_last(self):
        if not self._lineup:
            return False

        last = self._lineup.pop()
        self.clock.remaining += last.duration()
        return True

    def running_order(self):
        if not self._lineup:
            return (
                f"No acts booked. Acts: 0. "
                f"Minutes left: {self.clock.remaining}."
            )

        names = ", ".join(performance.name for performance in self._lineup)
        return (
            f"Running order: {names}. "
            f"Acts: {self.act_count}. "
            f"Minutes left: {self.clock.remaining}."
        )
class StrictTalentShow(TalentShow):
    """TalentShow variant that explains rejected bookings with exceptions."""

    def safe_book(self, performance):
        if performance is None:
            raise ShowChoiceError(
                "The selected choice cannot be None."
            )

        if not hasattr(performance, "name"):
            raise ShowChoiceError(
                "The selected choice must have a name."
            )

        duration_method = getattr(performance, "duration", None)
        if not callable(duration_method):
            raise ShowChoiceError(
                "The selected choice must provide duration()."
            )

        try:
            minutes = duration_method()
        except Exception as error:
            raise ShowRequestError(
                "The act duration could not be calculated."
            ) from error

        if (
            isinstance(minutes, bool)
            or not isinstance(minutes, (int, float))
            or minutes <= 0
        ):
            raise ShowRequestError(
                "An act duration must be a positive number."
            )

        if minutes > self.clock.remaining:
            raise ShowResourceError(
                f"The act needs {minutes} minutes, but only "
                f"{self.clock.remaining} remain."
            )

        self.performance = performance
        self.clock.reserve(minutes)
        self._lineup.append(performance)

        return f"MC {self.mc} books {performance.name}."


def audition(performances):  # Week 1's function, parameters, list, and loop.
    for performance in performances:
        print(performance.describe())  # One call, many versions: polymorphism.


def main():
    print("=== CAMPUS TALENT SHOW ===")
    print("MC Joel promised to finish on time. The dancers brought an encore.")
    acts = [Dance("Mukono Movers"), Poetry("Achen's spoken word"),
            HeadlineDance("Mukono Movers: short set"), AudienceWave()]
    audition(acts)  # AudienceWave works by duck typing, with no common parent.
    joel = TalentShow("Joel", 8)
    faith = TalentShow("Faith", 6)  # Another show owns a different clock and list.
    print(joel.book(acts[2]))  # 3 minutes.
    print(joel.book(acts[0]))  # 6 won't fit in 5: refuse without changing state.
    print(joel.book(acts[1]))  # 4 minutes.
    print(joel.book(acts[3]))  # 1 minute: the whole audience finishes the show.
    print(faith.book(acts[0]))
    print(f"Joel: {joel.clock.remaining} minutes left; acts: {joel.act_count}")
    print(f"Faith: {faith.clock.remaining} minutes left; acts: {faith.act_count}")
    print("MRO (look left to right):")
    for parent in HeadlineDance.__mro__:
        print(parent.__name__)
    print("Ending: everyone gets a turn, and Joel's timetable survives.")


if __name__ == "__main__":
    main()
