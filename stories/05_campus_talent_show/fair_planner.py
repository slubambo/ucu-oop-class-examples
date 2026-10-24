class FairRunningOrder:
    def __init__(self, available_minutes):
        self.available_minutes = available_minutes

    def plan(self, acts):
        # acts is a list of tuples: (performer_id, act_name, duration)
        scheduled = []
        remaining_time = self.available_minutes
        last_performer = None

        for performer, name, duration in acts:
            if duration > remaining_time:
                continue  # Skip if it doesn't fit

            # Fairness rule: avoid consecutive slots for the same performer
            if performer == last_performer:
                continue

            scheduled.append(
                {"performer": performer, "act": name, "duration": duration}
            )
            remaining_time -= duration
            last_performer = performer

        return scheduled