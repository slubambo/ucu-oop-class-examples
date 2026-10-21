class BoardGame:
    title = "Ludo"

    def data_cost(self):
        return 0

    def describe(self):
        return "Ludo: a fun board game, zero MB."


class Movie:
    title = "Mukono Mystery"

    def data_cost(self):
        return 700

    def describe(self):
        return "Mukono Mystery: a movie, 700 MB."


def enjoy(item):
    print("Enjoying", item.title, "- costs", item.data_cost(), "MB")


options = [Movie(), BoardGame()]

for option in options:
    print(option.describe())  # the loop
    enjoy(option)             # enjoy()