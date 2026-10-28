
from story import (
    StrictMatch,
    Dribble,
    TeamPass,
    InvalidEnergyError,
    InsufficientEnergyError,
)


def main():
    print("=== A2 EXCEPTION HANDLING DEMO ===")

    # Test 1: Invalid energy
    try:
        match = StrictMatch("Brian", 120)
    except InvalidEnergyError as error:
        print("Invalid energy caught:", error)

    # Test 2: Insufficient energy
    match = StrictMatch("Brian", 15)
    attack = Dribble("Brian")

    try:
        match.play(attack)
    except InsufficientEnergyError as error:
        print("Insufficient energy caught:", error)

    print("Energy remaining:", match.energy.remaining)
    print("Completed actions:", match.completed_actions)

    # Test 3: Successful attack
    match.play(TeamPass("Quick team pass"))

    print("Energy after team pass:", match.energy.remaining)
    print("Completed actions:", match.completed_actions)


if __name__ == "__main__":
    main()
