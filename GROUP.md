# Group submission

- Group number / catch-up label: **TODO: add group number**
- Story: Campus Talent Show
- Group fork URL: https://github.com/Ndiku-leonald/OOP-WORK
- Final branch: `main`

## Members and foundation work

| Full name | Access number | Registration number | GitHub username | Foundation task | Personal branch | Commit link(s) | Merged foundation PR |
|---|---|---|---|---|---|---|---|
| Ndiku Leonald | B35011 | S25B13/086 | Ndiku-leonald | Extension 6: Lightning dance | leo_branch | [71fa20d](https://github.com/Ndiku-leonald/OOP-WORK/commit/71fa20d), [9248ebd](https://github.com/Ndiku-leonald/OOP-WORK/commit/9248ebd) | [PR #3](https://github.com/Ndiku-leonald/OOP-WORK/pull/3) |
| MARTHA MULWANYI | B34658 | S25B13/037 | marthamulwanyi-hash | Extension 5: Running order | martha-mulwanyi branch | TODO: add commit link | TODO: add PR link |
|  | | | | | | | |
| **TODO: member 4** | | | | | | | |
| **TODO: member 5** | | | | | | | |

## Three later-topic choices

Choose exactly three different IDs from A1-A5 and record each member's coding or testing responsibility.

| Selected option | Members and specific responsibilities | Merged later-topic PRs | Demo command | Automated-check command |
|---|---|---|---|---|
| A4 | Ndiku Leonald: factory implementation and meaningful automated tests | [PR #5](https://github.com/Ndiku-leonald/OOP-WORK/pull/5) | `py -3 stories/05_campus_talent_show/demo_leonald_b35011_a4.py` | `py -3 -m unittest discover -s stories/05_campus_talent_show -p "test_*.py"` |
| A5 | Martha MULWANYI: fair running-order planner functionality | TODO: add merged PR link | TODO: add A5 demo command | `py -3 -m unittest discover -s stories/05_campus_talent_show -p "test_*.py" -v` |
| **TODO: A1-A5** | **TODO** | **TODO** | **TODO** | **TODO** |

## Individual later-topic contributions and reviews

| Member | Later-topic responsibility | Personal branch | Commit link(s) | Merged later-topic PR(s) | Review/comment links on teammates' PRs |
|---|---|---|---|---|---|
| Ndiku Leonald | A4: factory, Single Responsibility improvement and automated tests | leo-advanced | [a20abc2](https://github.com/Ndiku-leonald/OOP-WORK/commit/a20abc2) | [PR #5](https://github.com/Ndiku-leonald/OOP-WORK/pull/5) | TODO: add review links |
| Martha Mulwanyi |A5:ensuring fair scheduling, proper time management, and reliable performance. | |
| **TODO: member 3** | | | | | |
| **TODO: member 4** | | | | | |
| **TODO: member 5** | | | | | |

## Explain the work

### A4: Choice factory, Single Responsibility, and automated tests

The factory creates `Dance`, `Poetry`, and `AudienceWave` objects from clear keys. This keeps object creation in `factory.py`, while `TalentShow` handles booking and `ShowClock` handles resource rules. The automated checks cover normal creation, use through `TalentShow`, refused booking without state changes, unknown choice keys, and independent show state.

## Run the final project

Original story:

```powershell
py -3 stories/05_campus_talent_show/story.py
```

Foundation demo:

```powershell
py -3 stories/05_campus_talent_show/demo_leonard_b35011.py
```

A4 demo:

```powershell
py -3 stories/05_campus_talent_show/demo_leonald_b35011_a4.py
```

A4 automated checks:

```powershell
py -3 -m unittest discover -s stories/05_campus_talent_show -p "test_*.py"
```

**TODO:** Add every other member's foundation demo, later-topic demo, automated-check command, and test results.

## Group evaluation - maximum 250 words

**TODO:** Add one evaluation for the whole group covering what was built, OOP ideas used, what worked, the main difficulty, how it was handled, and any remaining limitation.

Word count: **TODO**

## Final check

- [ ] All required foundation tasks work on `main`.
- [ ] Exactly three later-topic choices are nominated and work together.
- [ ] Every member has merged foundation and later-topic PR evidence.
- [ ] Each PR has useful comments from all its author's teammates before merge.
- [ ] The original story still runs and matches the original expected output.
- [ ] All demos and automated checks run from final `main`.
- [ ] All members are listed with full names, access numbers, registration numbers and GitHub usernames.
- [ ] The story title, individual commits, PRs and review links are complete.
- [ ] The group evaluation is no more than 250 words.
- [ ] Every member can explain their own work.
