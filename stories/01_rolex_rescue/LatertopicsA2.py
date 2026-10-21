
from story import LunchBreak, Rolex, Kikomando, HomePackedLunch
#A2 Week 8 : Errors the story can explain
class LunchChoiceError(Exception):
    """no choice object was supplied."""
class LunchRequestError(Exception):
    """The calculated request is invalid."""
class LunchResourceError(Exception):
    """The request is valid but exceeds the remaining wallet balance."""
class StrictLunchBreak:
    """Strict validation wrapper; the original LunchBreak remains unchanged."""
    def __init__(self, lunch_break):
        if not isinstance(lunch_break, LunchBreak):
            raise TypeError("StrictLunchBreak requires a LunchBreak object.")
        self.lunch_break = lunch_break
    def safe_buy(self, choice):
            if choice is None:
                raise LunchChoiceError("Please choose a meal before purchasing.")
            try:
                        cost = choice.price()
            except Exception:
                        # Do not disguise arbitrary broken choice implementations as success.
                        raise
            
            if isinstance(cost, bool) or not isinstance(cost, int) or cost < 0:
                        raise LunchRequestError("The meal price must be a non-negative whole number.")
            
            if cost > self.lunch_break.wallet.balance:
                        raise LunchResourceError("There is not enough lunch money for this choice.")
            
            return self.lunch_break.buy(choice)

