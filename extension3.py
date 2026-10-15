class Performance:
    def __init__(self, name, minutes):
        self.name = name
        self.minutes = minutes

    def duration(self):
        return self.minutes

    def describe(self):
        return f"{self.name}: a performance lasting {self.duration()} minutes"


class ThankYouSpeech:              # does NOT inherit from Performance
    def __init__(self, name):
        self.name = name

    def duration(self):
        return 1

    def describe(self):
        return f"{self.name}: a thank-you speech lasting {self.duration()} minute"


def audition(item):
    print(f"Auditioning -> {item.describe()}")


def book(item):
    print(f"Booked '{item.name}' for {item.duration()} minute(s)")


if __name__ == "__main__":
    items = [Performance("Violin solo", 5), ThankYouSpeech("Closing remarks")]

    for item in items:
        audition(item)
        book(item)

    print(isinstance(items[1], Performance))
