from story import Dance, Poetry, AudienceWave


def create_choice(key, **settings):
    if key == "dance":
        crew = settings.get("crew", "Campus dancers")
        minutes = settings.get("minutes", 6)
        return Dance(crew, minutes=minutes)

    if key == "poetry":
        name = settings.get("name", "Campus poet")
        return Poetry(name)

    if key == "audience_wave":
        return AudienceWave()

    raise ValueError(f"Unknown choice key: {key}")