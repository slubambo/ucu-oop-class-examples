"""A2 demo: errors the story can explain (Nsubuga Edrine, B34863).

Week 8 exceptions. Every attempt is wrapped in try / except / finally:
each failure gets its own friendly message, and the finally block reports
that the attempt is over whether it worked or not. A failed attempt is
never reported as a success.

Run: py -3 stories/01_rolex_rescue/demo_edrine_b34863_a2.py
"""
from lunch_errors import LunchChoiceError, LunchRequestError, LunchResourceError
from story import HomePackedLunch, Rolex
from strict_lunch import StrictLunchBreak


class NegativeQuoteChoice:
    """A tiny fake choice that quotes a negative requirement."""

    name = "Negative rolex"

    def price(self):
        return -500

    def describe(self):
        return "Negative rolex: a broken quote."


print("=== A2: errors the story can explain (Edrine, B34863) ===")

sarah = StrictLunchBreak("Sarah", 5000)

# 1. No choice object at all ---------------------------------------------
print("\nAttempt 1: no choice supplied")
try:
    sarah.safe_buy(None)
except LunchChoiceError as error:
    print("Caught LunchChoiceError:", error)
finally:
    print("Attempt finished.")

# 2. An invalid request --------------------------------------------------
print("\nAttempt 2: a choice with a broken negative quote")
try:
    sarah.safe_buy(NegativeQuoteChoice())
except LunchRequestError as error:
    print("Caught LunchRequestError:", error)
finally:
    print("Attempt finished.")

# 3. A valid request the wallet cannot cover ------------------------------
print("\nAttempt 3: a five-egg rolex that costs more than remains")
try:
    sarah.safe_buy(Rolex(eggs=5))
except LunchResourceError as error:
    print("Caught LunchResourceError:", error)
finally:
    print("Attempt finished.")

# 4. A valid request that works -------------------------------------------
print("\nAttempt 4: a rolex that the wallet can cover")
try:
    print("Bought:", sarah.safe_buy(Rolex()))
except (LunchChoiceError, LunchRequestError, LunchResourceError) as error:
    print("Unexpected failure:", error)
finally:
    print("Attempt finished.")

# 5. A free choice is valid ----------------------------------------------
print("\nAttempt 5: a free home-packed lunch")
try:
    print("Bought:", sarah.safe_buy(HomePackedLunch()))
except (LunchChoiceError, LunchRequestError, LunchResourceError) as error:
    print("Unexpected failure:", error)
finally:
    print("Attempt finished.")

# The three failed attempts changed nothing --------------------------------
print("\nAfter three failures and two successes")
print("Expected: balance 2,000 (only the rolex was paid for) and 2 orders")
print("Actual: balance", sarah.wallet.balance, "; orders", sarah.order_count)
