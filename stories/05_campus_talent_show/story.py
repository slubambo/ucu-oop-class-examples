
"""Campus Talent Show: a cheerful MC must keep the show on time.
Run: python3 story.py. All acts and timings are fictional classroom examples.
"""
from abc import ABC, abstractmethod


# ACT 1: Time is a resource with a rule: don't schedule negative minutes.
class ShowClock:
    def __init__(self, minutes):
        self.remaining = minutes

    @property
    def remaining(self):
        return self.__remaining

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


# ACT 2: Every performance must tell the MC its duration.
class Performance(ABC):
    venue = "UCU student talent afternoon"

    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name}: {self.duration()} minutes at {self.venue}."

    @abstractmethod
    def duration(self):
        pass


class Dance(Performance):
    def __init__(self, crew, minutes=6):
        super().__init__(f"{crew} dance")
        self.minutes = minutes

    def duration(self):
        return self.minutes


class Poetry(Performance):
    def duration(self):
        return 4


class ShortDance(Dance):
    def duration(self):
        return super().duration() // 2


# ACT 3: One extra capability joins the existing dance family.
class ApplauseMixin:
    def describe(self):
        return f"Mukono, make some noise! {super().describe()}"


class HeadlineDance(ApplauseMixin, ShortDance):
    pass


class AudienceWave:
    # No Performance inheritance: the shared behaviour is enough.
    name = "Audience wave"

    def duration(self):
        return 1

    def describe(self):
        return "Audience wave: one minute, everybody gets to be famous."


# EXTENSION 3: Thank-you speech.
# Does not inherit from Performance; it uses duck typing.
class ThankYouSpeech:
    def __init__(self, name):
        self.name = name

    def duration(self):
        return 1

    def describe(self):
        return (
            f"{self.name}: one minute, thanking everyone "
            "for making the show a success."
        )


# ACT 4: The show HAS-A clock and manages performance objects.
class TalentShow:
    def __init__(self, mc, minutes):
        self.mc = mc
        self.clock = ShowClock(minutes)
        self._lineup = []
        self.performance = None

    @property
    def act_count(self):
        return len(self._lineup)

    def book(self, performance):
        self.performance = performance
        minutes = performance.duration()

        if self.clock.reserve(minutes):
            self._lineup.append(performance)
            return f"MC {self.mc} books {performance.name}."

        return (
            f"No slot for {performance.name}. "
            "The timetable has entered the chat."
        )


def audition(performances):
    for performance in performances:
        print(performance.describe())


def main():
    print("=== CAMPUS TALENT SHOW ===")
    print("MC Joel promised to finish on time. The dancers brought an encore.")

    acts = [
        Dance("Mukono Movers"),
        Poetry("Achen's spoken word"),
        HeadlineDance("Mukono Movers: short set"),
        AudienceWave(),
        ThankYouSpeech("Closing Thank-You Speech")
    ]

    # All acts, including ThankYouSpeech, can be auditioned.
    audition(acts)

    joel = TalentShow("Joel", 8)
    faith = TalentShow("Faith", 6)

    print("\n=== JOEL'S SHOW ===")
    print(joel.book(acts[2]))  # 3 minutes: succeeds.
    print(joel.book(acts[0]))  # 6 minutes: refused; only 5 remain.
    print(joel.book(acts[1]))  # 4 minutes: succeeds.
    print(joel.book(acts[3]))  # 1 minute: succeeds.

    print(f"Joel: {joel.clock.remaining} minutes left; acts: {joel.act_count}")

    print("\n=== FAITH'S SHOW ===")
    print(faith.book(acts[0]))
    print(f"Faith: {faith.clock.remaining} minutes left; acts: {faith.act_count}")

    # Test the thank-you speech with exactly one minute available.
    print("\n=== THANK-YOU SPEECH TEST ===")
    speech_show = TalentShow("Speech MC", 1)
    print(speech_show.book(acts[4]))
    print(
        f"Speech show: {speech_show.clock.remaining} minutes left; "
        f"acts: {speech_show.act_count}"
    )

    # Boundary test: there is no time available.
    print("\n=== BOUNDARY TEST ===")
    full_show = TalentShow("Final MC", 0)
    print(full_show.book(acts[4]))
    print(
        f"Final show: {full_show.clock.remaining} minutes left; "
        f"acts: {full_show.act_count}"
    )

    print("\nMRO (look left to right):")
    for parent in HeadlineDance.__mro__:
        print(parent.__name__)

    print("Ending: everyone gets a turn, and the timetable survives.")


if __name__ == "__main__":
    main()
