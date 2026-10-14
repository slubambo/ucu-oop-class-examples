from story import Comedy, TalentShow, audition


def main():
    comedy = Comedy("Campus comedy duo")
    audition([comedy])

    show = TalentShow("Joel", 2)
    expected_booking = "MC Joel books Campus comedy duo."
    actual_booking = show.book(comedy)
    print(f"Expected booking: {expected_booking}")
    print(f"Actual booking:   {actual_booking}")
    print(f"Minutes left: {show.clock.remaining}; booked acts: {show.act_count}")

    short_show = TalentShow("Faith", 1)
    refused_comedy = Comedy("Campus comedy duo")
    expected_refusal = (
        "No slot for Campus comedy duo. The timetable has entered the chat."
    )
    actual_refusal = short_show.book(refused_comedy)
    print(f"Expected refusal: {expected_refusal}")
    print(f"Actual refusal:   {actual_refusal}")
    print(
        f"Minutes left: {short_show.clock.remaining}; "
        f"booked acts: {short_show.act_count}"
    )


if __name__ == "__main__":
    main()
