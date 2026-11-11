# The Hostel Games Evening: foundation extensions

**Catch-up Group C3 — 8 members.** Deadline: end of Wednesday, 21 October 2026, Uganda time.

This is the foundation part of the [group assignment](../../GROUP_ASSIGNMENT.md). Complete this as well as three choices from [later-topic extensions](ADVANCED_EXTENSIONS.md).

- An eight-person group completes all eight tasks, one per member.
- A seven-person group chooses any seven different tasks, one per member.
- Each member uses their own branch, commits and merged PR. All teammates review and comment before merge, following [the group workflow](../../GROUP_ASSIGNMENT.md).

Read the complete [story](README.md) first. Add features to this story's `story.py`. Keep the original `main()` and original output working. Each member adds their own `demo_firstname_accessnumber.py` beside `story.py`. The demo imports the classes/functions it needs from `story` and shows the new feature. Use your own actual branch and file names.

Show a normal case, a boundary/refusal case and the resource/history before and after. For read-only work, prove nothing changes. These tasks use positive whole-number quantities unless stated otherwise. A Boolean is not a valid quantity, even though Python treats it as a kind of integer.

## Foundation 1: A new quantity-based choice

Add `RacingGame` as a subclass of `GameChoice`. Its constructor takes `races` and accepts only a positive whole number. Give it a clear name. `credit_cost()` returns `races × 2` credits. Use it through `show_choices()` and `GamesEvening.play()` without adding a type-checking branch to those callers.

## Foundation 2: Add more to the resource

Add `add_more(amount)` to `GameCredits`. Accept a positive whole number, add it through the `remaining` property and return `True`. Return `False` for zero, a negative amount, a fraction or a Boolean. Refusal must not change the remaining value.

## Foundation 3: A guest from a different family

Add `TriviaFromMemory` without inheriting `GameChoice`. Give it `name`, `describe()` and `credit_cost()` returning zero. It must work through the existing options function and coordinator. Show that a zero-resource session can complete it, record one success and keep a zero balance.

## Foundation 4: Find choices that fit

Add `affordable(choices, limit)`, returning a new list of choices whose `credit_cost()` is at most `limit`. Keep their original order. An empty input returns an empty list. Reject a negative limit with `ValueError`. Do not change the input list, resources or histories.

## Foundation 5: A useful summary

Add `summary()` to `GamesEvening`. Return a dictionary with `student`, `remaining`, `completed_count` and a `choices` list of successful choice names in order. Read `_entries`, whose items contain `choice` and `cost`. A new session returns an empty choices list. Refused attempts must not appear.

## Foundation 6: One more level of reuse

Add `QuickPractice` as a subclass of `PracticeGame`. Use `super().credit_cost()` and subtract 1 credits, with a minimum result of zero. Reuse the parent quantity constructor and give the instance a clear name. It must work through the unchanged callers. Check an ordinary quantity and a quantity that reaches the minimum if possible; otherwise explain why the minimum is not reached.

## Foundation 7: Cancel the latest success

Add `cancel_last()` to `GamesEvening`. For an empty history, return `False`. Otherwise remove the latest record and return its saved `cost` to `self.credits.remaining`, then return `True`. Refund the recorded amount, not a new quote from an object that may have changed. Cancel twice to prove that the same record cannot be refunded twice.

## Foundation 8: All together or not at all

Add `complete_bundle(choices)` to `GamesEvening`. Refuse an empty list or any negative requirement. Calculate the whole requirement first. If it fits, spend once and record every choice with its quoted cost; otherwise spend nothing and record nothing. Zero-cost bundles are allowed. Return `True` on complete success and `False` on refusal. Do not call the existing action method repeatedly and allow partial completion.

## After the foundation work

Agree on three later-topic choices as a group. Divide the new work so every member contributes code or meaningful automated tests and authors at least one later-topic PR. Several members may contribute to the same larger feature, but each must have a clear responsibility. Record the foundation tasks, chosen later-topic IDs and PR links in `GROUP.md`.
