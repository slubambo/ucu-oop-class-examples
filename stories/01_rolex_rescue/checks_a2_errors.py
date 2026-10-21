"""A2 - automated checks for the strict lunch break (Nsubuga Edrine, B34863).

Run from the main repository folder:

    py -3 stories/01_rolex_rescue/checks_a2_errors.py

Plain `assert` checks are used, as the assignment allows for option A2.
All three exception types are triggered, the stored resource and the
successful-history count are proved unchanged on each failure, and a valid
request is proved to still succeed.

Written by Nsubuga Edrine (B34863) for later-topic option A2.
"""
from lunch_errors import LunchChoiceError, LunchRequestError, LunchResourceError
from story import HomePackedLunch, Rolex
from strict_lunch import StrictLunchBreak


class NegativeQuoteChoice:
    """A tiny fake choice that returns a negative requirement."""

    name = "Negative rolex"

    def price(self):
        return -500

    def describe(self):
        return "Negative rolex: a broken quote."


def refuses(action, error_type, label):
    """Run `action` and fail unless it raises `error_type`."""
    try:
        action()
    except error_type:
        print(f"PASS: {label}")
        return
    raise AssertionError(f"FAILED: {label} (no {error_type.__name__} was raised)")


print("=== A2 checks: StrictLunchBreak and the three errors ===")

# --- Refused case 1: no choice object at all -----------------------------
sarah = StrictLunchBreak("Sarah", 5000)
refuses(lambda: sarah.safe_buy(None), LunchChoiceError,
        "a missing choice raises LunchChoiceError")
assert sarah.wallet.balance == 5000, "a refusal must not spend money"
assert sarah.order_count == 0, "a refusal must not record an order"
print("PASS: the balance and the history are unchanged after the refusal")

# --- Refused case 2: an invalid request ---------------------------------
refuses(lambda: sarah.safe_buy(NegativeQuoteChoice()), LunchRequestError,
        "a negative requirement raises LunchRequestError")
assert sarah.wallet.balance == 5000, "a refusal must not spend money"
assert sarah.order_count == 0, "a refusal must not record an order"
print("PASS: the balance and the history are unchanged after the refusal")

# --- Refused case 3: not enough money ------------------------------------
refuses(lambda: sarah.safe_buy(Rolex(eggs=5)), LunchResourceError,
        "an unaffordable request raises LunchResourceError")
assert sarah.wallet.balance == 5000, "a refusal must not spend money"
assert sarah.order_count == 0, "a refusal must not record an order"
print("PASS: the balance and the history are unchanged after the refusal")

# --- Normal case: a valid, affordable request still succeeds -------------
message = sarah.safe_buy(Rolex())
assert "Lunch is saved" in message, f"the purchase should succeed, got {message!r}"
assert sarah.order_count == 1, "the order must be recorded once"
assert sarah.wallet.balance == 2000, "the price must be taken from the balance"
print("PASS: a valid request succeeds and updates the balance and the history")

# --- Boundary case: a zero-cost choice is valid --------------------------
free_message = sarah.safe_buy(HomePackedLunch())
assert "Lunch is saved" in free_message, "a free choice must not be refused"
assert sarah.order_count == 2, "the free choice must be recorded too"
assert sarah.wallet.balance == 2000, "a free choice must not cost any money"
print("PASS: a zero-cost choice is valid and is not confused with a missing choice")

# --- The errors are separate classes -------------------------------------
assert issubclass(LunchChoiceError, Exception)
assert issubclass(LunchRequestError, Exception)
assert issubclass(LunchResourceError, Exception)
assert not issubclass(LunchChoiceError, LunchResourceError)
assert not issubclass(LunchRequestError, LunchResourceError)
print("PASS: the three errors are separate classes")

print("All A2 checks for the strict lunch break passed.")
