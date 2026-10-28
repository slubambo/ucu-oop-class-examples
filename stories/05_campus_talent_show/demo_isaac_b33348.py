from story import Performance, TalentShow, audition


class Comedy(Performance):
    # A comedy act is a Performance with a fixed two-minute set.
    def duration(self):
        # Performance requires each concrete act to provide its duration.
        return 2


def main():
    comedy = Comedy("Isaac's comedy set")
    second_comedy = Comedy("Second comedy set")
    audition_list = [comedy]
    show = TalentShow("Joel", 3)

    # Audition displays the act but should not change the show's time or lineup.
    before_audition = (show.clock.remaining, show.act_count)
    print("Read-only audition check:")
    print(f"Expected state to stay: {before_audition}")
    audition(audition_list)
    after_audition = (show.clock.remaining, show.act_count)
    print(f"Actual state:           {after_audition}")

    # Normal case: the two-minute comedy act fits in the three-minute show.
    print("\nNormal booking case:")
    print("Expected: MC Joel books Isaac's comedy set.")
    print(f"Actual:   {show.book(comedy)}")
    print("Expected state: 1 minute left; 1 act booked.")
    print(f"Actual state:   {show.clock.remaining} minute(s) left; "
          f"{show.act_count} act(s) booked.")

    # Refused case: the next two-minute act cannot fit in the one minute left.
    print("\nRefused booking case:")
    print("Expected: no slot; time and booked-act count stay unchanged.")
    state_before_refusal = (show.clock.remaining, show.act_count)
    print(f"Actual:   {show.book(second_comedy)}")
    state_after_refusal = (show.clock.remaining, show.act_count)
    print(f"Expected state: {state_before_refusal}")
    print(f"Actual state:   {state_after_refusal}")


if __name__ == "__main__":
    main()