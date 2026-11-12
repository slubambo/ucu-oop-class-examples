from story import LightningDance, TalentShow, audition


def main():
    normal_dance = LightningDance("Mukono lightning crew")
    boundary_dance = LightningDance("One-minute lightning crew", 1)

    # Auditioning should describe the acts without changing a show's resources.
    show = TalentShow("Joel", 5)
    state_before_audition = (show.clock.remaining, show.act_count)
    print("=== Lightning Dance audition ===")
    print(f"Expected state before: {state_before_audition}")
    audition([normal_dance, boundary_dance])
    state_after_audition = (show.clock.remaining, show.act_count)
    print(f"Actual state after:   {state_after_audition}")

    assert state_after_audition == state_before_audition
    assert normal_dance.duration() == 2
    assert boundary_dance.duration() == 1

    # Normal case: a two-minute lightning dance fits and is booked.
    normal_show = TalentShow("Joel", 3)
    print("\n=== Normal booking ===")
    print("Expected: MC Joel books Mukono lightning crew; 1 minute remains.")
    print(f"Actual:   {normal_show.book(normal_dance)}")
    print(f"Actual state: {normal_show.clock.remaining} minute(s) remain; "
          f"{normal_show.act_count} act(s) booked.")

    assert normal_show.clock.remaining == 1
    assert normal_show.act_count == 1

    # Boundary case: a lightning dance cannot reduce below one minute.
    boundary_show = TalentShow("Joel", 1)
    boundary_before = (boundary_show.clock.remaining, boundary_show.act_count)
    print("\n=== One-minute boundary booking ===")
    print("Expected: the act lasts 1 minute and a one-minute show books it.")
    print(f"Actual duration: {boundary_dance.duration()} minute(s)")
    print(f"Actual: {boundary_show.book(boundary_dance)}")
    print(f"State before: {boundary_before}")
    print(f"State after:  {(boundary_show.clock.remaining, boundary_show.act_count)}")

    assert boundary_dance.duration() == 1
    assert boundary_show.clock.remaining == 0
    assert boundary_show.act_count == 1

    # Separate refused case: the act may fit only when it is too long for zero time.
    refused_show = TalentShow("Joel", 0)
    print("\n=== Refused booking ===")
    print("Expected: no slot is available; the state remains unchanged.")
    print(f"Actual: {refused_show.book(normal_dance)}")
    print(f"Actual state: {(refused_show.clock.remaining, refused_show.act_count)}")

    assert refused_show.clock.remaining == 0
    assert refused_show.act_count == 0


if __name__ == "__main__":
    main()
