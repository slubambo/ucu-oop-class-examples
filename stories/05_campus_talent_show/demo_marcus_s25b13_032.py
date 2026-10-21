"""A4 demo: a factory creates choices while TalentShow handles booking rules."""

from choice_factory import create_choice
from story import TalentShow


def main():
    show = TalentShow("Marcus", 7)
    acts = [
        create_choice("dance", crew="Mukono Movers", minutes=6),
        create_choice("poetry", name="Achen's spoken word"),
        create_choice("audience_wave"),
    ]

    for act in acts:
        before = show.clock.remaining
        result = show.book(act)
        print(f"Expected booking to fit: {act.duration() <= before}")
        print(f"Actual result: {result}")
        print(f"Time left: {show.clock.remaining}; booked acts: {show.act_count}")

    try:
        create_choice("karaoke")
    except ValueError as error:
        print(f"Expected unknown choice to be refused: {error}")


if __name__ == "__main__":
    main()
