"""Plan a fair running order without changing a TalentShow's state."""
from dataclasses import dataclass


@dataclass(frozen=True)
class PerformerAct:
    performer_id: str
    performance: object

    def __post_init__(self):
        if not isinstance(self.performer_id, str) or not self.performer_id.strip():
            raise ValueError("Performer ID must be a non-empty string.")
        if not callable(getattr(self.performance, "duration", None)):
            raise TypeError("Performance must provide a duration() method.")


@dataclass(frozen=True)
class RunningOrderPlan:
    scheduled: tuple
    skipped: tuple
    remaining_minutes: int

    @property
    def scheduled_minutes(self):
        return sum(act.performance.duration() for act in self.scheduled)


class FairRunningOrderPlanner:
    """Schedule fitting acts fairly, using submission order to break ties."""

    def plan(self, acts, available_minutes):
        if isinstance(available_minutes, bool) or not isinstance(available_minutes, int):
            raise TypeError("Available time must be a whole number of minutes.")
        if available_minutes < 0:
            raise ValueError("Available time cannot be negative.")

        acts = tuple(acts)
        durations = []
        for act in acts:
            if not isinstance(act, PerformerAct):
                raise TypeError("Every planned act must be a PerformerAct.")
            duration = act.performance.duration()
            if isinstance(duration, bool) or not isinstance(duration, int):
                raise TypeError("Performance duration must be a whole number.")
            if duration <= 0:
                raise ValueError("Performance duration must be positive.")
            durations.append(duration)

        remaining = list(range(len(acts)))
        scheduled = []
        time_left = available_minutes
        previous_performer = None

        while remaining:
            fitting = [index for index in remaining if durations[index] <= time_left]
            if not fitting:
                break

            alternatives = [
                index for index in fitting
                if acts[index].performer_id != previous_performer
            ]
            chosen = (alternatives or fitting)[0]
            scheduled.append(acts[chosen])
            remaining.remove(chosen)
            time_left -= durations[chosen]
            previous_performer = acts[chosen].performer_id

        return RunningOrderPlan(
            scheduled=tuple(scheduled),
            skipped=tuple(acts[index] for index in remaining),
            remaining_minutes=time_left,
        )