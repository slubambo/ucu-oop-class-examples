"""A2 - the three errors the story can explain (Week 8: exceptions).

Every class is derived from Exception and says one clear thing, so the
caller can catch exactly the failure it knows how to handle:

    LunchChoiceError   - no choice object was supplied at all (None);
    LunchRequestError  - the request itself is invalid (a broken quote);
    LunchResourceError - the request is valid but the wallet cannot cover it.

Written by Nsubuga Edrine (B34863) for later-topic option A2.
"""


class LunchChoiceError(Exception):
    """Raised when there is no lunch choice to act on (for example None)."""


class LunchRequestError(Exception):
    """Raised when the request is invalid, such as a negative requirement."""


class LunchResourceError(Exception):
    """Raised when the request is valid but needs more UGX than remain."""
