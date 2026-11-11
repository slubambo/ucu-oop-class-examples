# The Mabira Picnic Plan: later-topic extensions

**Choose any three different options, A1–A5, and complete them as a group.**

**Due: end of Wednesday, 21 October 2026, Uganda time.** This menu applies to this story only. Existing groups keep their earlier foundation work; catch-up groups complete their assigned foundation tasks too.

These topics come from Weeks 7–10 of the class plan. Start with [the short learning guide](../../LATER_TOPICS_GUIDE.md), then use the standard Python documentation linked there. You are extending a small story, not building a website or connecting a real service.

## Rules for all three choices

- Record your three chosen option IDs in `GROUP.md` before coding. You do not need to complete extra options.
- Every member must contribute code or meaningful automated tests to at least one selected option, on their own branch and in their own later-topic PR. A larger option may be split among several members. Documentation alone is not a later-topic coding contribution.
- Do not submit the same code twice for two options. If a foundation feature is useful, extend it with genuinely new behaviour. A demo used for an earlier task alone does not complete a later-topic option.
- The options are independent: choosing JSON does not require you to choose Factory, and choosing exceptions does not require JSON. Explain how any options you combine work together.
- Keep the original story and foundation demos working. Add stricter behaviour through new methods/classes where necessary. Keep the existing public methods available if you move code into modules.
- For each option, submit a short explanation, a runnable demo and automated checks for a normal case, a boundary case and an invalid/refused case. Plain `assert` checks are acceptable for A1, A2, A3 and A5; A4 specifically uses `unittest`.
- Each PR needs useful comments from all the other members before merge, as in [the group workflow](../../GROUP_ASSIGNMENT.md).

## A1: Values that can print, compare and add — Week 7

Create `PicnicTime(amount)` for minutes. It accepts a non-negative whole number and exposes a read-only `amount` property. Refuse negative values, fractions and Booleans.

Implement all four methods:

1. `__str__`: a clear user-facing value such as `3,000 minutes`.
2. `__repr__`: a developer-facing value such as `PicnicTime(3000)`. It must be distinct from the friendly display.
3. `__eq__`: two `PicnicTime` objects with the same amount compare equal.
4. `__add__`: adding two `PicnicTime` values returns a **new** `PicnicTime` containing their total. Neither original is changed.

For an unsupported operand type, return `NotImplemented` from the comparison/addition method. This is different from raising `NotImplementedError`.

Integrate it: add `preview_total(choices)` to `PicnicPlan`. It asks each choice for `duration()` and returns the combined requirement as `PicnicTime`. An empty list returns a zero amount. Do not spend resources or change history during this preview. Use whole-number inputs in this exercise.

Show equal and unequal values, adding two values, unchanged operands, invalid construction and the preview with different choice types. A value class that is never used by the story is incomplete.

## A2: Errors the story can explain — Week 8

Create these three custom exception classes, derived from `Exception`:

- `PicnicChoiceError`: no choice object was supplied (`None`).
- `PicnicRequestError`: an invalid request, such as a negative calculated requirement.
- `PicnicResourceError`: the request is valid but needs more minutes than remain.

Add a small `StrictPicnicPlan` subclass or a separate service that wraps a `PicnicPlan`. Its `safe_schedule(choice)` must raise the appropriate custom exception **before** spending or recording anything. On a valid, affordable request, it delegates to the existing `schedule(choice)`. A zero-cost choice is valid where supported by the story; it must not be confused with a missing choice.

Keep the original `PicnicPlan` action behaviour for the baseline story. In a new demo, use `try` and specific `except` clauses to show friendly messages, and `finally` to print a completion message for every attempt. Do not catch an error and report a failed action as a success.

Automated checks must trigger all three exception types and prove the stored resource and successful-history count stay unchanged on each failure. Use a tiny fake choice returning a negative requirement to exercise the invalid-quote case. Also prove that a valid request still succeeds.

## A3: Save the story and continue later — Week 9

Add JSON saving and loading for `PicnicPlan`. Save the student, remaining minutes, successful history and any extra state required by your chosen foundation features. Each item in `_entries` contains a `choice` object and its saved `cost`; preserve both pieces of information.

Write ordinary data: dictionaries, lists, strings, numbers and Booleans. Use a `type` label and the necessary constructor fields for each saved choice. Support the choices actually present in your demo and explain that supported list. Use a fixed set of allowed labels when rebuilding objects; do not use `eval` or execute class names from the file.

Load into a **new** `PicnicPlan` with a fresh resource object and a compatible history. Validate all data before making a loaded session available. A saved-and-loaded session must preserve the resource, completed count and successful labels. It must also support the relevant foundation behaviour, such as a cancellation that needs a saved cost or duration. Do not merely print the loaded dictionary and call that a restored project.

Show a save/load round trip, then complete one more action on the loaded session. Also check a missing file, malformed JSON and a structurally invalid record such as a negative resource or unknown type label. These failures must produce a clear error and leave any already-running session unchanged. Use temporary files for automated checks so your tests do not depend on yesterday's files.

## A4: A small factory, clearer responsibilities and tests — Weeks 9–10

Create `create_choice(key, **settings)`, a factory that creates at least three choices for this story: `NatureWalk`, `TeamQuiz` and `GroupPhoto`. Choose clear keys and document any required settings. Unknown keys must raise a clear error. Callers use the returned object's existing interface; the coordinator should not need a separate branch for each class.

Give creation, rule checking and display clear homes. Refactor one small area using **Single Responsibility**: for example, keep choice creation in the factory and leave resource spending in `PicnicClock`. Explain the responsibility you moved and why. This is one practical SOLID improvement; a claim that you applied all five principles without evidence is not required.

Write at least **six meaningful `unittest` tests** covering factory-created objects through the real caller, a refused request with unchanged state, an unknown key, and separate instance state. Use assertions about results and state, not only class names or printed messages. This option can be completed without any other later-topic option.

From the main repository folder, run:

```sh
python3 -m unittest discover -s stories/10_picnic_plan -p "test_*.py"
```

On Windows use `py -3 -m unittest` with the same arguments. State the exact command in your submission. A green run must discover the tests; “Ran 0 tests” is not a completed test suite.

## A5: Innovation — A rain plan for the picnic

Add a weather-aware planner with outdoor activities and indoor alternatives. In rainy mode it substitutes a valid alternative and checks the time budget before scheduling. A preview must not spend time or rewrite the existing successful history.

You may instead propose your own useful feature for this same story. State its user need, inputs, rules and expected outcomes in `GROUP.md` before implementing it. It must add behaviour beyond the chosen foundation tasks and beyond A1–A4; renaming a class or changing a price alone is not enough.

Use at least one new class with a clear responsibility and integrate it with the current objects. Include at least four meaningful automated checks covering normal use, a boundary/refusal, unchanged state on failure and interaction with an existing feature. Keep the scope small and runnable offline. Explain what makes the feature useful and how its design uses OOP.

## What to submit for each selected option

Add an entry in `GROUP.md` containing the option ID, members responsible, merged PR links, demo command, check/test command and a short explanation of the result. Every member should be able to explain the part they contributed.

Follow the [common submission instructions](../../GROUP_ASSIGNMENT.md). Provide a demo and checks for each of your three choices; one demonstration does not replace the other two.
