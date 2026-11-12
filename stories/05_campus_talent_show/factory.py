"""Choice creation for the Campus Talent Show."""
from story import AudienceWave, Dance, Poetry


def create_choice(key, **settings):
    """Create a supported choice without moving booking rules into the factory."""
    choices = {
        "dance": Dance,
        "poetry": Poetry,
        "audience_wave": AudienceWave,
    }
    choice_class = choices.get(key)
    if choice_class is None:
        raise ValueError(f"Unknown choice key: {key}")
    if choice_class is AudienceWave:
        if settings:
            raise ValueError("Audience wave does not accept settings.")
        return choice_class()
    return choice_class(**settings)
