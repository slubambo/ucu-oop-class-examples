# Group submission

- Group number: CLASS
- Story: Campus Talent Show
- Group fork URL: https://github.com/mawubaskyblair-cmyk/campus-talent-show-group
- Final branch: `main`
- Deadline: Wednesday, 21 October 2026

## Part 1: Foundation Extensions (First Task)

A five-person group completes five different extensions.

| Member name | University access number | GitHub username | Extension number | Personal branch | Merged PR link |
|---|---|---|---|---|---|
| Blair | b33217 | mawubaskyblair-cmyk | Extension 1: Comedy duo | `blair-b33217` | [#1](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/1) |
| Lawrence | b33232 | arube371 | Extension 2: MC gets extra time | `lawrence-b33232` | [#2](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/2) |
| Victor | b30887 | kabuyevictor2-arch | Extension 4: Cancel last booking | `victor-b30887` | [#3](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/3) |
| Samuel | b33227 | Samuel-ahumuza | Extension 3: Thank-you speech | `samuel-b33227` | [#4](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/4) |
| Daphine | b35639 | kasanadaphine62-glitch | Extension 5: Running order | `daphine-b35639` | [#5](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/5) |

## Part 2: Later-Topic Options (Second Task)

We selected options A2, A4, and A5.

| Member name | University access number | GitHub username | Option | Contribution | Personal branch | Merged PR link |
|---|---|---|---|---|---|---|
| Samuel | b33227 | Samuel-ahumuza | A2 | Exceptions and Safe Booking | `samuel-b33227-a2` | [#6](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/6) |
| Lawrence | b33232 | arube371 | A2 | Strict Booking Tests | `lawrence-b33232` | [#2](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/2) |
| Blair | b33217 | mawubaskyblair-cmyk | A4 | Factory and Tests | `blair-b33217` | [#7](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/7) |
| Daphine | b35639 | kasanadaphine62-glitch | A5 | Running Order Tests | `daphine-b35639` | [#8](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/8) |
| Victor | b30887 | kabuyevictor2-arch | A2 / A4 | Code Review and Merge Fixes | `victor-b30887` | [#3](https://github.com/mawubaskyblair-cmyk/campus-talent-show-group/pull/3) |

## Run our work

Run these commands from the repository root on Windows:

```sh
py -3 stories/05_campus_talent_show/story.py
py -3 stories/05_campus_talent_show/demo_blair_b33217.py
py -3 stories/05_campus_talent_show/demo_lawrence_b33232.py
py -3 stories/05_campus_talent_show/demo_victor_b30887.py
py -3 stories/05_campus_talent_show/demo_samuel_b33227.py
py -3 stories/05_campus_talent_show/demo_daphine_b35639.py
py -3 stories/05_campus_talent_show/demo_blair_b33217_a4.py
py -3 stories/05_campus_talent_show/demo_samuel_b33227_a2.py
py -3 -m unittest discover -s stories/05_campus_talent_show -p "test_*.py"