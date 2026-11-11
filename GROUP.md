# Group work record

- Group number: TBD
- Story: Campus Talent Show (`stories/05_campus_talent_show`)
- Group fork URL: https://github.com/marcusainebyona362/oop-campus-talent-show-work
- Final branch: `main`
- Deadline: Wednesday, 21 October 2026 (Uganda time)
- Selected later-topic options: A1, A2 and A4

## Member responsibilities

Assign every group member a name, university access number, GitHub username, one selected option, personal branch and their own later-topic PR before coding. Add rows if the group has more than three members; more than one member may share an option. Every member contributes code or meaningful automated tests, and reviews every other member's PR before merge.

| Member name | University access number | GitHub username | Option responsibility | Personal branch | PR link/status |
| --- | --- | --- | --- | --- | --- |
| Marcus Ainebyona | S25B13/032 | TBD | A2: failure-case checks and demo | `marcus-s25b13-032` | Not started |
| akankwatsakevin0-ctrl | S25B13/066 | TBD | A4: choice factory and unittest suite | `kevin-s25b13-066` | Not started |
| solomonsempangi20 | S25B13/108 | TBD | A1: implement `StageTime` | `solomon-s25b13-108` | Not started |
| mulyanti mark | S25B13/110 | TBD | A2: custom exceptions and `StrictTalentShow` | `mulyanti-s25b13-110` | Not started |
| sebela jeremy | S25B13/006 | TBD | A1: implement and check `preview_total()` | `jeremy-s25b13-006` | Not started |

## A1: Values that print, compare and add

**Responsible member(s):** solomonsempangi20 (`StageTime`), sebela jeremy (`preview_total()`)

- Add immutable/read-only `StageTime(amount)` for non-negative whole minutes; reject negatives, fractions and Booleans.
- Implement friendly `__str__`, distinct developer-facing `__repr__`, value equality and addition that returns a new value. Return `NotImplemented` for unsupported comparison/addition operands.
- Add `TalentShow.preview_total(choices)`. It combines each choice's `duration()` into `StageTime`, returns zero for an empty list, and does not spend time or change booking history.
- Provide a short explanation, a runnable demo, and automated checks for equal/unequal values, addition, unchanged operands, invalid construction, empty preview, and a preview containing different choice types.

**Demo command (Windows):** `py -3 stories/05_campus_talent_show/demo_<member>_<access-number>.py`

**Checks:** Include executable assertions in the demo or a focused test. Confirm preview leaves remaining time and successful history unchanged.

## A2: Errors the story can explain

**Responsible member(s):** Marcus Ainebyona (failure-case checks and demo), mulyanti mark (custom exceptions and `StrictTalentShow`)

- Add `ShowChoiceError`, `ShowRequestError` and `ShowResourceError`, each derived from `Exception`.
- Add `StrictTalentShow` or a separate service with `safe_book(choice)`. Refuse `None`, a negative calculated requirement, and an unaffordable request with the matching exception before resource/history mutation; delegate affordable valid requests to the existing `book(choice)`.
- Keep baseline `TalentShow.book()` behavior available and unchanged. A supported zero-cost choice is valid, not missing.
- Provide a short explanation and a runnable demo using specific `except` clauses and `finally` for every attempt. Do not report a failed booking as successful.
- Add automated checks that trigger all three errors and prove resource and successful-history count stay unchanged, using a tiny fake choice for the negative duration. Also verify a valid request succeeds.

**Demo command (Windows):** `py -3 stories/05_campus_talent_show/demo_<member>_<access-number>.py`

**Checks:** Assertions must inspect state before and after every refused booking, as well as the successful booking result.

## A4: Factory, responsibilities and tests

**Responsible member(s):** akankwatsakevin0-ctrl

- Add `create_choice(key, **settings)` for at least `Dance`, `Poetry` and `AudienceWave`; document required settings and raise a clear error for unknown keys.
- Use the returned choices through their existing interface and the real `TalentShow` caller; do not add per-class branches to the coordinator.
- Give creation, rule checking and display clear homes. Make one evidenced Single Responsibility improvement, such as keeping choice construction in the factory and resource spending in `ShowClock`.
- Add a short explanation, runnable demo and at least six meaningful `unittest` tests. Tests must cover factory-created objects through the caller, a refused booking with unchanged state, an unknown key and separate instance state. Assert results and state, not only types or printed output.

**Demo command (Windows):** `py -3 stories/05_campus_talent_show/demo_<member>_<access-number>.py`

**Required test command from the repository root (Windows):**

```sh
py -3 -m unittest discover -s stories/05_campus_talent_show -p "test_*.py"
```

The run must discover and execute tests; `Ran 0 tests` does not count as completion.

## Integration and completion checks

- [ ] Confirm each member's assignment, branch and own PR before coding; avoid overlapping edits by agreeing on shared interfaces first.
- [ ] `create_choice` returns objects that work with `TalentShow.book()` and `preview_total()` without coordinator type branches.
- [ ] Strict booking validates before delegating to baseline booking and preserves resource/history on every failure.
- [ ] A1 and A2 demos/checks are committed; A4 has at least six discovered `unittest` tests.
- [ ] Original `story.py` behavior and expected output remain intact.
- [ ] Run the original story: `py -3 stories/05_campus_talent_show/story.py`.
- [ ] Run every selected-option demo from the repository root and record actual filenames above or in each member's PR.
- [ ] Run the required unittest discovery command and record the result.
- [ ] Every PR has useful comments from all other members before merge; recheck changes and demos on the latest `main`.
- [ ] Replace all TBD values with actual group/member/PR details and record the merged PR links.

## Submission summary

**A1 result:** Pending implementation. `StageTime` represents whole-minute values and `preview_total()` computes a non-mutating requirement for mixed choice objects.

**A2 result:** Pending implementation. Strict booking reports missing, invalid and unaffordable requests distinctly without recording failed attempts.

**A4 result:** Pending implementation. A small factory centralizes choice construction, while `ShowClock` remains responsible for resource spending; automated behavior is checked with `unittest`.
