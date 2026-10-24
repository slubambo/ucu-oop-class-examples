from story import ThankYouSpeech, TalentShow, audition


print("=== EXTENSION 3: THANK-YOU SPEECH ===")

speech = ThankYouSpeech("Samuel's thank-you speech")

print("Name:", speech.name)
print("Expected duration: 1 minute")
print("Actual duration:", speech.duration())

print("\nDescription:")
print(speech.describe())

print("\nAudition:")
audition([speech])

print("\nNormal booking:")
show = TalentShow("Samuel", 1)
print(show.book(speech))

print("Expected acts: 1")
print("Actual acts:", show.act_count)

print("Expected minutes left: 0")
print("Actual minutes left:", show.clock.remaining)

print("\nBoundary case: another speech cannot fit")
second_speech = ThankYouSpeech("Second thank-you speech")
print(show.book(second_speech))

print("Expected acts: 1")
print("Actual acts:", show.act_count)

print("Expected minutes left: 0")
print("Actual minutes left:", show.clock.remaining)