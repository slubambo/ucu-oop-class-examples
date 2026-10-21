from story import PhotoStorage, PhotoSession, PortraitSet


def main():
    print("=== Foundation 2: add_more ===")
    storage = PhotoStorage(10)
    print("Before:", storage.remaining)

    print("add_more(5), expect True ->", storage.add_more(5))
    print("Remaining, expect 15 ->", storage.remaining)

    for bad in (0, -3, 2.5, True):
        print(f"add_more({bad!r}), expect False ->", storage.add_more(bad))
    print("Remaining unchanged, expect 15 ->", storage.remaining)

    # Works with the real session: 10 MB is too little for a 15 MB portrait set.
    session = PhotoSession("Joel", 10)
    print(session.capture(PortraitSet()))   # refused
    session.storage.add_more(5)
    print(session.capture(PortraitSet()))   # now succeeds
    print("Remaining, expect 0 ->", session.storage.remaining)


if __name__ == "__main__":
    main()