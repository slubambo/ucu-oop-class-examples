from story import LunchBreak, Rolex, Kikomando, HomePackedLunch
def create_choice(key, **settings):
    if key == "rolex":
        unknown = set(settings) - {"eggs"}
        if unknown:
            raise TypeError(f"Unknown rolex settings(s): {', '.join(sorted(unknown))}")
        eggs = settings.get("eggs", 2)
        if isinstance(eggs, bool) or not isinstance(eggs, int) or eggs <0:
            raise ValueError("eggs must be a positive")
        return Rolex(eggs=eggs)
    if key == "kikomando":
        if settings:
            raise TypeError("kikomando does not accept given settings")
        return Kikomando("kikomando")
    if key == "home_packed_lunch":
        if settings:
            raise TypeError("home_packed_lunch does not accept given settings")
        return HomePackedLunch()
    raise ValueError(f"Unknown key choice: {key}")