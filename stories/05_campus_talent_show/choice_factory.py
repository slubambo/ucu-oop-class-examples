"""Create Campus Talent Show choices from documented keys and settings."""

from story import AudienceWave, Dance, Poetry


def create_choice(key, **settings):
    """Create a dance, poetry act, or audience wave.

    Use ``create_choice("dance", crew="Mukono Movers", minutes=6)``;
    ``minutes`` is optional and defaults to 6. Use
    ``create_choice("poetry", name="Achen's spoken word")`` or
    ``create_choice("audience_wave")`` for the other choices.
    """
    if key == "dance":
        unexpected = settings.keys() - {"crew", "minutes"}
        if unexpected:
            raise TypeError(f"Unexpected dance setting(s): {', '.join(sorted(unexpected))}")
        if "crew" not in settings:
            raise TypeError("Dance requires the 'crew' setting.")
        return Dance(settings["crew"], settings.get("minutes", 6))

    if key == "poetry":
        unexpected = settings.keys() - {"name"}
        if unexpected:
            raise TypeError(f"Unexpected poetry setting(s): {', '.join(sorted(unexpected))}")
        if "name" not in settings:
            raise TypeError("Poetry requires the 'name' setting.")
        return Poetry(settings["name"])

    if key == "audience_wave":
        if settings:
            unexpected = ", ".join(sorted(settings))
            raise TypeError(f"Audience wave takes no settings; received: {unexpected}")
        return AudienceWave()

    raise ValueError(
        f"Unknown choice key {key!r}. Choose 'dance', 'poetry', or 'audience_wave'."
    )
