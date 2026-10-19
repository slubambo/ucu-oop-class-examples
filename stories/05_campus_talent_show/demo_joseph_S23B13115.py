class ThankYouSpeech:
    def __init__(self, name):
        self.name = name

    def duration(self):
        return 1

    def describe(self):
        return f"{self.name}: one minute, thanking everyone for making the show a success."


act = ThankYouSpeech("Closing Thank-You Speech")
joel = ["Joel", 1]

print(f"Joel has {joel[1]} minutes left.")
print(f"{act.describe()}")  # Output: Closing Thank-You Speech: one minute, thanking everyone for making the show a success.
