# The Campus Photo-Day Rush

**Assigned to Catch-up Group C5**, which is Group 5 in the lecturer's additional group list. It has 7 members. This label is separate from the original class group numbers.

Joel is organising a campus photo afternoon. The camera has limited space and the queue is growing.

This is a made-up Ugandan student story. Its prices, resource use and events are learning examples. Your goal is to help the main character make choices without losing track of the resource.

## Your work

1. Run and understand the complete starting story below.
2. Complete [one foundation extension per member](EXTENSIONS.md). Your group has eight choices.
3. As a team, choose **three** [later-topic extensions](ADVANCED_EXTENSIONS.md).
4. Follow the [common group instructions](../../GROUP_ASSIGNMENT.md) and submission requirements.

**Deadline: end of Wednesday, 21 October 2026, Uganda time.**

## Run the story

Download or clone the repository using [Start here](../../START_HERE.md). Open the main repository folder in VS Code.

**Windows:**

```sh
py -3 stories/11_photo_day/story.py
```

**macOS or Linux:**

```sh
python3 stories/11_photo_day/story.py
```

No extra packages are needed. The whole story prints without asking for input. Compare with [expected_output.txt](expected_output.txt).

## Read it in five short acts

**Act 1: PhotoStorage.** This object owns the remaining MB. The property setter checks the starting value and later assignments. `use()` refuses an amount that does not fit before changing anything. A double underscore changes the internal attribute name; it is not a password lock.

**Act 2: PhotoPackage.** This abstract class requires `storage_needed()`. `PortraitSet` calculates a requirement from a quantity; `GroupShot` uses a fixed requirement. Each choice inherits its name and description interface. `super().__init__()` reuses common setup. Quantities must be positive whole numbers.

**Act 3: specialised choices.** `CompactPortraits` reuses its parent's calculation and adjusts it. `FeaturedPortraits` combines this class with `PhotoHype`. The mixin adds a cheerful description. `PhoneSelfie` has no shared parent but supplies the methods the caller needs. That is duck typing.

**Act 4: PhotoSession.** This coordinator creates and owns its `PhotoStorage`. It receives an independent choice and asks for its requirement. If the resource approves, the coordinator records the success. The history is `_entries`, a list of dictionaries containing the choice object and the cost **at the time of success**. This saved cost will help with accurate cancellation later.

**Act 5: the ending.** `main()` creates two separate coordinators. The first tries an ordinary choice, a special choice and a request that will not fit. The second has its own resource and history. The printed MRO shows the order Python uses to find methods.

## Follow one request

`session.capture(choice)` asks `choice.storage_needed()` for the needed amount. It then asks `session.storage.use(needed)` to check and spend that amount. Only a successful action goes into `_entries`. A zero-cost choice is explicitly allowed; a negative requirement is refused. A refusal leaves the resource and completed count unchanged.

The quantities and units are deliberately simple. Integer division `//` rounds down in the half-cost variants; these are toy whole-unit requirements, not real provider estimates.

## How the classes connect

```mermaid
classDiagram
    PhotoPackage <|-- PortraitSet
    PhotoPackage <|-- GroupShot
    PortraitSet <|-- CompactPortraits
    CompactPortraits <|-- FeaturedPortraits
    PhotoHype <|-- FeaturedPortraits
    PhotoSession *-- PhotoStorage : owns
    PhotoSession --> PhotoPackage : requests behaviour
    PhotoSession --> PhoneSelfie : matching methods
```

A triangle points to a parent. A filled diamond means an owned component. A plain arrow means collaboration. The choices are created outside the coordinator and can exist independently; storing them in history is aggregation.

## All the Week 1–6 ideas are here

| Idea | Where it appears |
|---|---|
| Classes and objects | Class definitions and the two coordinator objects in `main()` |
| Attributes, methods, constructors and `self` | Per-object state, `__init__`, and calls on each receiving object |
| Class versus instance attributes | Shared `unit` on the base class; each instance's name and quantity |
| Encapsulation | The resource keeps its value and checks together |
| Getter and validating setter | The `remaining` property, also used during construction |
| Read-only property | `completed_count` is derived from history and has no setter |
| Public / `_` / `__` | Public operations, `_entries`, and the name-mangled resource value |
| Single and hierarchical inheritance | Two concrete children of `PhotoPackage` |
| Multilevel inheritance | `PhotoPackage → PortraitSet → CompactPortraits` |
| Multiple and hybrid inheritance | `FeaturedPortraits(PhotoHype, CompactPortraits)` |
| Overriding and `super()` | Specialised requirement and added description |
| Polymorphism | `show_choices()` calls the same method on different objects |
| Duck typing | `PhoneSelfie` works without inheriting `PhotoPackage` |
| MRO | The class list printed at the end; `super()` follows this order |
| Abstraction | The caller uses `storage_needed()` without copying its formula |
| Composition | The coordinator creates its own resource |
| Association and aggregation | Passed-in choices and references retained in history |
| Python refresher | Functions, conditions, lists, dictionaries, loops and returned values |

[OOP in plain English](../../OOP_IN_PLAIN_ENGLISH.md) explains the vocabulary. The code is a starting example; the extension sheets describe the work your group must add.
