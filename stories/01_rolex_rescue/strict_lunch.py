"""A2 - StrictLunchBreak: a lunch break that explains its refusals (Week 8).

The original LunchBreak.buy() keeps its behaviour for the baseline story:
it returns a friendly message when a purchase is refused. StrictLunchBreak
adds a stricter door, safe_buy(), for callers that want to handle a refusal
themselves instead of reading a message.

safe_buy() checks the request FIRST and raises a named error before any
money is spent or any order is recorded. A valid, affordable request is
handed to the original buy(), so there is still only one place where money
moves.

Written by Nsubuga Edrine (B34863) for later-topic option A2.
"""
from lunch_errors import LunchChoiceError, LunchRequestError, LunchResourceError
from story import LunchBreak


class StrictLunchBreak(LunchBreak):
    """A LunchBreak that reports a refusal as a clear, catchable error."""

    def safe_buy(self, choice):
        """Buy `choice`, or raise an error that explains the refusal.

        Raises:
            LunchChoiceError: no choice was supplied, or it cannot give a price.
            LunchRequestError: the quoted requirement is not a valid amount.
            LunchResourceError: the requirement is larger than the balance.
        """
        if choice is None:
            raise LunchChoiceError("No lunch choice was supplied.")

        try:
            cost = choice.price()
        except AttributeError:
            raise LunchChoiceError(
                f"{choice!r} cannot give a price, so it is not a usable choice.")

        if isinstance(cost, bool) or not isinstance(cost, int):
            raise LunchRequestError(
                f"{self._name_of(choice)} quoted an invalid requirement: {cost!r}.")
        if cost < 0:
            raise LunchRequestError(
                f"{self._name_of(choice)} quoted a negative requirement: {cost}.")
        if cost > self.wallet.balance:
            raise LunchResourceError(
                f"{self._name_of(choice)} needs UGX {cost:,} but only "
                f"UGX {self.wallet.balance:,} remains.")

        # A valid, affordable request: let the original story behaviour run.
        return self.buy(choice)

    @staticmethod
    def _name_of(choice):
        """The label of a choice, for a friendly error message."""
        return getattr(choice, "name", "The choice")
