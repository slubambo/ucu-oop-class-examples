"""Demonstrates saving, restoring and continuing a Mukono Mission journey.

Run from the repository root:
    py -3 stories/02_mukono_mission/demo_a3_json.py
"""
import json
import tempfile
from pathlib import Path

from story import Journey, StudentBoda, Taxi


def show_load_error(label, path, journey):
    # Take a snapshot to prove a failed load leaves the already-running session alone.
    before = (journey.purse.balance, journey.completed_legs)
    try:
        Journey.load_json(path)
    except (FileNotFoundError, ValueError) as error:
        print(f"{label}: {error}")
    else:
        # A bad input that loads successfully means the validation check failed.
        raise AssertionError(f"{label} should not load")
    after = (journey.purse.balance, journey.completed_legs)
    print(f"Running session unchanged: {after == before}")


def main():
    # Temporary storage keeps the demo repeatable and removes its files automatically.
    with tempfile.TemporaryDirectory() as temp_dir:
        folder = Path(temp_dir)
        save_path = folder / "amina_journey.json"

        # Complete one trip before saving so the file includes resource and history.
        amina = Journey("Amina", 5000)
        print(amina.travel(StudentBoda("Nambi"), 3))
        amina.save_json(save_path)
        print(f"Saved journey to {save_path.name}")

        # Loading rebuilds a usable Journey with a fresh purse and choice objects.
        loaded = Journey.load_json(save_path)
        labels = [leg.name for leg in loaded._legs]
        print(
            f"Restored {loaded.student}: UGX {loaded.purse.balance:,}; "
            f"{loaded.completed_legs} completed; labels: {labels}"
        )

        # Continue the restored story; the fare is charged and the history grows.
        print(loaded.travel(Taxi("Mukono taxi"), 3))
        print(
            f"After one more action: UGX {loaded.purse.balance:,}; "
            f"{loaded.completed_legs} completed"
        )

        # Missing files and malformed JSON are common input errors to handle.
        show_load_error("Missing file", folder / "missing.json", loaded)

        malformed_path = folder / "malformed.json"
        malformed_path.write_text('{"student": ', encoding="utf-8")
        show_load_error("Malformed JSON", malformed_path, loaded)

        # Valid JSON can still have invalid data, so check the record structure too.
        invalid_path = folder / "invalid.json"
        invalid_path.write_text(
            json.dumps({"student": "Amina", "balance": -1, "legs": []}),
            encoding="utf-8",
        )
        show_load_error("Negative balance", invalid_path, loaded)

        # Choice labels must come from the allowed set; unknown labels are rejected.
        invalid_path.write_text(
            json.dumps({
                "student": "Amina",
                "balance": 100,
                "legs": [{"type": "UnknownRide"}],
            }),
            encoding="utf-8",
        )
        show_load_error("Unknown type label", invalid_path, loaded)

        # Document supported choices and the constructor data saved for each.
        print(
            "Supported saved choices: Boda (rider), Taxi (name), "
            "StudentBoda (rider), CheerfulStudentBoda (rider), "
            "WalkWithFriend (no extra fields)."
        )


if __name__ == "__main__":
    main()