from story import TalentShow, ThankYouSpeech, audition


def main():
    print("=== THANK-YOU SPEECH DEMO ===")

    speech = ThankYouSpeech("Kevin")
    audition([speech])

    show = TalentShow("Joel", 1)
    expected_booking = "MC Joel books Kevin's thank-you speech."
    actual_booking = show.book(speech)
    print(f"Expected booking: {expected_booking}")
    print(f"Actual booking:   {actual_booking}")
    print(f"Minutes left: {show.clock.remaining}; booked acts: {show.act_count}")

    full_show = TalentShow("Faith", 0)
    refused_speech = ThankYouSpeech("Kevin")
    expected_refusal = (
        "No slot for Kevin's thank-you speech. The timetable has entered the chat."
    )
    actual_refusal = full_show.book(refused_speech)
    print(f"Expected refusal: {expected_refusal}")
    print(f"Actual refusal:   {actual_refusal}")
    print(
        f"Minutes left: {full_show.clock.remaining}; "
        f"booked acts: {full_show.act_count}"
    )


if __name__ == "__main__":
    main()