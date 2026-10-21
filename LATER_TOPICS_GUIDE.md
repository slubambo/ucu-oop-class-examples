# A short start on the later topics

These notes help you start Weeks 7–10 features. They are small illustrations, not finished answers to the story assignments. Read your own `ADVANCED_EXTENSIONS.md` for the full requirements. You can choose any three options, including innovation.

## 1. Dunder methods: give normal Python operations a meaning

A dunder method has two underscores on each side of its name. Python calls these methods for operations such as printing, comparing and adding objects.

| Operation | Method | Purpose |
|---|---|---|
| `str(value)` or `print(value)` | `__str__` | A friendly description for the user |
| `repr(value)` | `__repr__` | A precise description useful while debugging |
| `left == right` | `__eq__` | Compare the meaning of two values |
| `left + right` | `__add__` | Define what adding these values means |

`__str__` and `__repr__` must return strings, not print them. An addition should return a new result; it should not secretly spend money or alter either input. For an unsupported operand, `NotImplemented` lets Python try its normal fallback. It is a return value, not the `NotImplementedError` exception.

Read the official [Python data model](https://docs.python.org/3/reference/datamodel.html).

## 2. Exceptions: report a failure that the caller can handle

A custom exception is a class derived from `Exception`. `raise` reports it; a matching `except` handles it. `finally` runs as control leaves the `try` statement, whether or not the attempt succeeded. Avoid returning from `finally`, because that can hide the result or error.

This small example is separate from the story tasks:

```python
class InvalidPracticeAmount(Exception):
    pass


def check_amount(amount):
    if amount < 0:
        raise InvalidPracticeAmount("Use zero or a positive amount.")
    return amount


try:
    print(check_amount(-2))
except InvalidPracticeAmount as error:
    print(f"Please correct this: {error}")
finally:
    print("Practice attempt finished.")
```

Check a rule before changing state. Catch the specific failure you expect; do not hide every possible bug with an empty `except` block. Your story's strict wrapper should add new exception behaviour while leaving the original demonstration usable.

Read [Python's errors and exceptions tutorial](https://docs.python.org/3/tutorial/errors.html).

## 3. JSON: save data, then rebuild objects

JSON stores simple data such as dictionaries, lists, strings and numbers. It does not automatically save a live Python object and all its methods. A round trip has two jobs: convert the object state into data, then validate the data and reconstruct compatible objects.

For example, a plain record might look like this:

```json
{
  "student": "Demo Student",
  "remaining": 12,
  "history": [
    {"type": "standard", "settings": {"quantity": 2}, "recorded_cost": 8}
  ]
}
```

The field names are illustrative; use fields matching your story. Save enough to restore the features you actually use. A cancellation may need the original charged amount, not a recalculated price.

Use `with open(...)` for a file, `json.dump(...)` to write data and `json.load(...)` to read it. Build a loaded session separately, then return it only after validation succeeds. A failed load must not destroy an already-running session.

Read the official [JSON module documentation](https://docs.python.org/3/library/json.html).

## 4. Factory and Single Responsibility: give each part a clear job

A factory is a function or object that creates the requested kind of object. In your story, it can translate a simple key into a concrete choice. The returned object then uses the same interface as the other choices.

Keep creation separate from spending, booking or displaying. That is a small application of **Single Responsibility**: each part has a clear reason to change. Explain an actual responsibility you moved; do not only rename a file and claim a design improvement.

A fixed mapping or a short explicit selection is enough for this exercise. Unknown keys should fail clearly. The Factory choice does not require a Singleton. Singleton is another pattern mentioned in the plan; it is not an extra compulsory feature here.

## 5. Automated checks: make a wrong result noticeable

An assertion checks an expected result. A check that only prints “passed” without testing anything does not verify behaviour.

For an action that changes state, check the value and history before and after. For a refusal, check that neither changed. For addition, check the result and prove both inputs stayed unchanged. For loading, check the restored object's behaviour, not only that the file exists.

`unittest` is included with Python. A basic test has an expected result and a useful failure message:

```python
import unittest


def amount_left(balance, cost):
    if cost < 0 or cost > balance:
        raise ValueError("Cost must fit the balance.")
    return balance - cost


class AmountChecks(unittest.TestCase):
    def test_ordinary_cost(self):
        self.assertEqual(amount_left(10, 3), 7)

    def test_exact_balance(self):
        self.assertEqual(amount_left(10, 10), 0)

    def test_cost_too_large(self):
        with self.assertRaises(ValueError):
            amount_left(10, 11)


if __name__ == "__main__":
    unittest.main()
```

Write your own checks against the real classes in your chosen story. Name test files `test_*.py` and test methods `test_*`. In a test file beside `story.py`, you can import its classes using `from story import ClassName`.

From the main repository folder, discover one story's tests with:

```sh
python3 -m unittest discover -s stories/01_rolex_rescue -p "test_*.py"
```

Replace the story folder. On Windows use `py -3 -m unittest` with the same remaining arguments. Make sure tests were actually discovered. Keep file tests independent using temporary files/directories so a previous run cannot make a broken feature appear correct.

Read the official [unittest documentation](https://docs.python.org/3/library/unittest.html).

## A sensible order for a group

First agree on your three choices and their rules. Then build one small working case. Add the refused or boundary cases. Ask a teammate to read the code and try a different input. Merge only after reviews and checks, then run the combined project again.

Use the exact story method names. An idea copied from a different example will still need the right arguments, object relationships and resource rules for your story.
