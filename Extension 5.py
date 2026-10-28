class Match:
    def __init__(self, captain, points):
        self.captain = captain
        self.energy = EnergyTank(points)  # Owned object: composition.
        self._actions = []  # Internal list, by single-underscore convention.
        self.action = None

    @property
    def completed_actions(self):  # Read-only; computed, not independently editable.
        return len(self._actions)

    def play(self, action):
        self.action = action  # A replaceable part: aggregation.
        effort = action.effort()  # Abstraction: Match doesn't calculate the skill.
        if effort == 0 or self.energy.spend(effort):
            self._actions.append(action)  # A list of objects: collaboration.
            return f"Captain {self.captain} chooses {action.name}. Done!"
        return f"Not enough energy for {action.name}. Pass the ball, please!"

    def report(self):
        """Return captain name, successful action names, and energy left."""
        names = [action.name for action in self._actions]
        return {
            "captain": self.captain,
            "actions": names,
            "energy_left": self.energy.remaining,
        }