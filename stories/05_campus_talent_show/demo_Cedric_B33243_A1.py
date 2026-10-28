"""Demonstrate A1 value semantics and side-effect-free time previews."""
from story import Dance, StageTime, TalentShow, ThankYouSpeech


def main():
    three_thousand = StageTime(3000)
    another_three_thousand = StageTime(3000)
    five_hundred = StageTime(500)
    total = three_thousand + five_hundred

    print(f"Display: {three_thousand}")
    print(f"Developer: {three_thousand!r}")
    print(f"Equal: {three_thousand == another_three_thousand}; "
          f"unequal: {three_thousand != five_hundred}")
    print(f"Addition: {total}; operands unchanged: "
          f"{three_thousand.amount == 3000 and five_hundred.amount == 500}")

    try:
        three_thousand.amount = 99
    except AttributeError as error:
        print(f"Read-only amount: refused ({error})")

    print(f"Unsupported equality: "
          f"{StageTime.__eq__(three_thousand, 3000) is NotImplemented}")
    print(f"Unsupported addition: "
          f"{StageTime.__add__(three_thousand, 3000) is NotImplemented}")

    for invalid in (-1, 1.5, True):
        try:
            StageTime(invalid)
        except (TypeError, ValueError) as error:
            print(f"Invalid {invalid!r}: {error}")

    preview_show = TalentShow("Cedric", 20)
    choices = [Dance("Mukono Movers", 6), ThankYouSpeech()]

    class TimedChoice:
        def duration(self):
            return 4

    choices.append(TimedChoice())
    print(f"Preview: {preview_show.preview_total(choices)}")
    print(f"Preview state: {preview_show.clock.remaining} minutes left; "
          f"{preview_show.act_count} booked acts")
    print(f"Empty preview: {preview_show.preview_total([])}")


if __name__ == "__main__":
    main()
