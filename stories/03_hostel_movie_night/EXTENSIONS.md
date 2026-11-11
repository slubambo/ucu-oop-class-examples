# Hostel Movie Night: group extensions

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
py -3 stories/03_hostel_movie_night/demo_amina_26b12345.py
```

**macOS or Linux:**

```sh
python3 stories/03_hostel_movie_night/demo_amina_26b12345.py
```

Replace the demo file name with your own. Use separate objects for your checks so an earlier check does not accidentally affect a later one. You may use the numeric inputs already used in the story. You do not need a new package, a database or an online service.

## Choose your extension

### Extension 1: Short comedy clip

Add ComedyClip as a subclass of Entertainment. It uses 50 MB. Add it to show_options() and enjoy() without editing either.

### Extension 2: A friend shares data

Add add_data(amount) to DataBundle. Positive amounts add MB and return True. Zero or negative amounts return False without changing state.

### Extension 3: Ludo night

Add BoardGame without inheriting Entertainment. Set title to Ludo and implement data_cost() as 0 and describe() as a sentence. Use it through the existing loop and enjoy().

### Extension 4: What fits the bundle?

Add available(options, megabytes), a function returning a list of options whose data_cost() fits. Do not play them or change the options.

### Extension 5: Movie-night recap

Add recap() to MovieNight. Return activity titles, successful activity count and data left. Include a friendly message if nothing has happened.

### Extension 6: Ultra-low-data movie

Add TinyMovie as a subclass of DataSaverMovie. Its cost is half its parent cost, using // and super().data_cost().

## Before your group submits

- All chosen extensions work together on the group fork's `main` branch.
- The original story still runs, and every member's demo runs from the final `main` branch.
- Each member has their own foundation commit and merged pull request, plus a later-topic contribution as described in the common instructions.
- Every pull request has a useful review comment from each of its author's teammates.
- Your group has completed `GROUP.md` with the member, task, branch and pull request links.

The foundation work is one part of the combined assignment. Submit one link to your group fork. See the [full submission checklist](../../GROUP_ASSIGNMENT.md#10-submit-your-group-work).
