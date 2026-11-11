"""A1 StageTime checks and demonstration.

Run from the repository root with:
    py -3 stories/05_campus_talent_show/demo_solomon_s25b13_108.py
"""
from story import StageTime


def check_invalid(amount, expected_error):
    try:
        StageTime(amount)
    except expected_error:
        return
    raise AssertionError(f"StageTime({amount!r}) should be rejected")


def main():
    opening = StageTime(3_000)
    encore = StageTime(4)
    total = opening + encore

    assert str(opening) == "3,000 minutes"
    assert repr(opening) == "StageTime(3000)"
    assert opening == StageTime(3_000)
    assert opening != encore
    assert total == StageTime(3_004)
    assert opening.amount == 3_000
    assert encore.amount == 4
    assert StageTime.__eq__(opening, 3_000) is NotImplemented
    assert StageTime.__add__(opening, 3_000) is NotImplemented

    check_invalid(-1, ValueError)
    check_invalid(1.5, TypeError)
    check_invalid(True, TypeError)

    try:
        opening.amount = 12
    except AttributeError:
        pass
    else:
        raise AssertionError("StageTime.amount must be read-only")

    print(" MUYINZA SOLOMON SEMPANGI:- A1 STAGE TIME ")
    print(f"Friendly display: {opening}")
    print(f"Developer display: {opening!r}")
    print(f"Combined requirement: {total}")
    print("All StageTime checks passed.")


if __name__ == "__main__":
    main()