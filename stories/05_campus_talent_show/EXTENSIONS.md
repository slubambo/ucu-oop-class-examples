# Campus Talent Show: group extensions

**Foundation stage: one extension per member.**

**Combined deadline: end of Wednesday, 21 October 2026, Uganda time.** Keep completed foundation work and its PR evidence. Your group must also choose three [later-topic extensions](ADVANCED_EXTENSIONS.md).

Your group works on this story only. There are six choices below.

- **Five members:** choose any five different extensions. Each member completes one.
- **Six members:** complete all six extensions. Each member completes one.
- Agree on who does what before you start. Two members should not claim the same extension.

Follow the [group GitHub instructions](../../GROUP_ASSIGNMENT.md): one group fork, all members with access, one personal branch and one merged pull request per member. Every member reviews every other member's pull request and leaves a useful comment before it is merged.

## What everyone must do

1. Read [the story explanation](README.md) and run the original `story.py`.
2. Make your extension in this story's `story.py` on your own branch. Keep the original classes and behaviour working. Leave the original `main()` story unchanged; show your new feature in your own demo file.
3. Add a short comment explaining your new class or method.
4. Create your own demo file beside `story.py`, for example `demo_amina_26b12345.py`. Use your own first name and access number. The example details are made up.
5. In that file, import the classes/functions you need from `story` and show your extension working. For a new choice, use the existing options function and coordinator in your demo instead of changing the original `main()` menu.
6. Show one normal case and one refused, empty or boundary case. Print what you expect and what actually happens. For a read-only function, show that the resource and history do not change.
7. Explain these checks in your pull request, then get comments from all the other members before merging.

For the demo file above, run from the main repository folder:

**Windows:**

```sh
py -3 stories/05_campus_talent_show/demo_amina_26b12345.py
```

**macOS or Linux:**

```sh
python3 stories/05_campus_talent_show/demo_amina_26b12345.py
```

Replace the demo file name with your own. Use separate objects for your checks so an earlier check does not accidentally affect a later one. You may use the numeric inputs already used in the story. You do not need a new package, a database or an online service.

## Choose your extension

### Extension 1: Comedy duo

Add Comedy as a subclass of Performance. Its duration is 2 minutes. Put it in the audition list and book it through the unchanged TalentShow.book().

### Extension 2: The MC gets extra time

Add extend(minutes) to ShowClock. A positive value adds minutes and returns True. Zero or negative values return False without changing state.

### Extension 3: Thank-you speech

Add ThankYouSpeech without inheriting Performance. Give it name, duration() returning 1, and describe(). Use audition() and book() unchanged.

### Extension 4: Cancel the last booking

Add cancel_last() to TalentShow. If no act is booked, return False. Otherwise remove the most recent act, return its minutes to the clock and return True. Do not change act durations after booking in this exercise.

### Extension 5: Running order

Add running_order() to TalentShow. Return the names of booked acts in order, the count and minutes left. Include a no-bookings message for a new show.

### Extension 6: Lightning dance

Add LightningDance as a subclass of ShortDance. Its duration is its parent duration minus 1, with a minimum of 1. Use super().duration().

## Before your group submits

- All chosen extensions work together on the group fork's `main` branch.
- The original story still runs, and every member's demo runs from the final `main` branch.
- Each member has their own foundation commit and merged pull request, plus a later-topic contribution as described in the common instructions.
- Every pull request has a useful review comment from each of its author's teammates.
- Your group has completed `GROUP.md` with the member, task, branch and pull request links.

The foundation work is one part of the combined assignment. Submit one link to your group fork. See the [full submission checklist](../../GROUP_ASSIGNMENT.md#10-submit-your-group-work).
