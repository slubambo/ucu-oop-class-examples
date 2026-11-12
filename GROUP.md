Copy this file to `GROUP.md` in the root of your group fork and fill it in.

- Group number: CODEX
- Story: Rolex_rescue
- Group fork URL:https://github.com/mwesigwajoshuaprecious/Codex/
- Final branch: `main`
- Deadline: Thursday, 15 October 2026

A five-person group completes five different extensions. A six-person group completes all six. Remove the unused sixth row for a five-person group.

| Member name | University access number | GitHub username | Extension number | Personal branch | Merged PR link |
|---|---|---|---|---|---|
| Member 1 |Mwesigwa Joshua | B34592| mwesigwajoshuaprecious|1 |mwesigwa_joshua-b34592 |
| Member 1 |Mwesigwa Joshua Precious | B34592| mwesigwajoshuaprecious|1 |mwesigwa_joshua-b34592 |
| Member 2 | Kamukama Hope| b35401| kamukamahope|4 |hope-b35401 |
| Member 3 | Nsubuga Edrine| B34863|NsubugaEdrine| 5 |Gitedryne |
| Member 4 | Ariko Eric|b36048 |jace-eric |6 |Ariko-Eric-b36048 |
| Member 5 |Kakande Stacey |b35004 |StaceyKakande | 2| stacey-s25b13-079|
| Member 6 | | | | | |

## Later-topic stage (Weeks 7-10)

The group chose **A1, A2 and A4** from `stories/01_rolex_rescue/ADVANCED_EXTENSIONS.md`. The
chosen IDs are recorded in `stories/01_rolex_rescue/GROUP.md` before the later-topic coding.

| Option ID | Topic | Member responsible | Branch | Pull request |
|---|---|---|---|---|
| A1 | Values that can print, compare and add (Week 7) | Mwesigwa Joshua Precious | `mwesigwa_joshua-b34592` | [PR](https://github.com/mwesigwajoshuaprecious/Codex/pull/6) |
| A2 | Errors the story can explain (Week 8) | Nsubuga Edrine | `nsubuga_edrine_b34863` | [open PR](https://github.com/mwesigwajoshuaprecious/Codex/pull/new/nsubuga_edrine_b34863) |
| A4 | A small factory, clearer responsibilities and tests (Weeks 9-10) | _to be agreed_ | _to be agreed_ | _to be agreed_ |

### A2: Errors the story can explain (Week 8)

- **Member responsible:** Nsubuga Edrine (B34863), branch `nsubuga_edrine_b34863`.
- **What was added**
  - `stories/01_rolex_rescue/lunch_errors.py` — `LunchChoiceError` (no choice supplied),
    `LunchRequestError` (an invalid request, such as a negative requirement) and
    `LunchResourceError` (a valid request that needs more UGX than remain), all derived from
    `Exception`.
  - `stories/01_rolex_rescue/strict_lunch.py` — `StrictLunchBreak`, a child of `LunchBreak`.
    Its `safe_buy(choice)` checks the request **before** anything is spent or recorded and
    raises the matching error; a valid, affordable request is handed to the original
    `buy(choice)`, so money still moves in one place only. A zero-cost choice stays valid and
    is not confused with a missing choice.
  - `stories/01_rolex_rescue/demo_edrine_b34863_a2.py` — the demo, using `try`, specific
    `except` clauses and a `finally` message for every attempt.
  - `stories/01_rolex_rescue/checks_a2_errors.py` — the automated checks.
- **Demo command** (from the main repository folder)

  ```sh
  py -3 stories/01_rolex_rescue/demo_edrine_b34863_a2.py
  ```

- **Check command**

  ```sh
  py -3 stories/01_rolex_rescue/checks_a2_errors.py
  ```

- **Result** — the checks pass. All three exception types are triggered: a missing choice raises
  `LunchChoiceError`, a tiny fake choice that quotes -500 raises `LunchRequestError`, and a
  5-egg rolex that costs 6,000 raises `LunchResourceError`. After each failure the stored
  resource is still 5,000 and the successful-history count is still 0. A valid request still
  succeeds (balance 2,000, one order) and a zero-cost choice is bought without paying.
  The original `LunchBreak.buy()` behaviour for the baseline story is unchanged.

## Run our work

Write the command for the original story, then the command for each member's demo. Use the actual file names committed to this fork.

The original story:

```sh
py -3 stories/01_rolex_rescue/story.py
```

The A2 demo and its checks (later-topic option A2):

```sh
py -3 stories/01_rolex_rescue/demo_edrine_b34863_a2.py
py -3 stories/01_rolex_rescue/checks_a2_errors.py
```


## Final group check

- [ ] Every chosen feature works on `main`.
- [ ] The original story still runs and its expected output is unchanged.
- [ ] Every member's demo runs from `main`.
- [ ] Every member authored a PR that is now merged.
- [ ] Every member left a useful review comment on every other member's PR before merge.
- [ ] The group has checked that all the extensions work together.
