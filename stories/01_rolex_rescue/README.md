# The Rolex Rescue

Sarah has UGX 5,000, a hungry friend, and a very persuasive avocado-rolex seller.

This story includes all the OOP concepts from Weeks 1 to 6. The numbers are made up for learning.

## Group assignment

The combined assignment is due at the end of **Wednesday, 21 October 2026, Uganda time**. Keep your [foundation work](EXTENSIONS.md), then choose three [later-topic extensions](ADVANCED_EXTENSIONS.md). Each member contributes foundation work and new code or meaningful automated tests through reviewed PRs. The [common assignment](../../GROUP_ASSIGNMENT.md) explains the workflow and what to submit.

## Run this story

If you have not downloaded the files yet, follow [Start here](../../START_HERE.md).

1. Open the repository folder in VS Code.
2. Open `stories/01_rolex_rescue/story.py`.
3. Choose **Run Python File in Terminal**, or use the command below.

From a terminal in the main repository folder:

**Windows:**

```sh
py -3 stories/01_rolex_rescue/story.py
```

**macOS or Linux:**

```sh
python3 stories/01_rolex_rescue/story.py
```

The whole story prints without asking you to type anything. Open [expected_output.txt](expected_output.txt) to see the output of the unchanged program.

## Read the five acts

**Act 1 — the rule keeper.** `LunchWallet` keeps the changing resource. Its constructor sets a valid starting value. Its property getter reads that value. Its setter refuses a negative value. Its action method refuses a request that does not fit.

**Act 2 — the family.** `Meal` is an abstract class. It says that every concrete member of the family must provide `price()`. `Rolex` and `Kikomando` provide different versions. `super().__init__()` reuses the parent's setup.

**Act 3 — the special choices.** `AvocadoRolex` extends `Rolex`. `FeaturedRolex` adds the description from `HypeMixin` using multiple inheritance. `HomePackedLunch` is not in the same family but provides the methods the program needs.

**Act 4 — the coordinator.** `LunchBreak` creates and owns a `LunchWallet`. It receives a choice object, asks it for its behaviour and lets the resource object check the request. Successful actions go into its own history list. `order_count` reads the length of that list and has no setter.

**Act 5 — the complete story.** `main()` creates the objects and runs their actions. Two coordinator objects show that one person's resource and history are separate from another's.

## One request, step by step

`sarah.buy(menu[2])` asks the featured meal for `price()`. Python finds `AvocadoRolex.price()`, which asks `Rolex.price()` for 3,000 and adds 500. The wallet checks and spends 3,500; only then is the meal added to Sarah’s orders.

## The ending, with the numbers explained

| Event | Resource after the attempt | Completed count |
|---|---|---|
| Sarah buys the featured rolex | 5,000 - 3,500 = 1,500 | 1 |
| Sarah asks for kikomando | Refused: 2,500 > 1,500; still 1,500 | 1 |
| Joel buys kikomando | 3,000 - 2,500 = 500 | 1 (Joel only) |

A refused request changes neither the guarded resource nor the completed-action count.

## How the classes connect

```mermaid
classDiagram
    Meal <|-- Rolex
    Meal <|-- Kikomando
    Rolex <|-- AvocadoRolex
    AvocadoRolex <|-- FeaturedRolex
    HypeMixin <|-- FeaturedRolex
    LunchBreak *-- LunchWallet : owns
    LunchBreak --> Meal : uses
    LunchBreak --> HomePackedLunch : uses same methods
```

`Rolex` **is a kind of** `Meal`. That is inheritance.

`LunchBreak` **has its own** `LunchWallet`. That is composition. It is not a kind of that resource.

Choice objects are created outside the coordinator. Passing them in is association. Keeping references to those independent objects is aggregation.

## Where each concept appears

| Concept | In this story |
|---|---|
| Classes, objects, attributes and methods | The class definitions and the objects created in `main()` |
| Constructors and `self` | Each `__init__`; `self` means the object receiving that call |
| Class and instance attributes | The shared fact on `Meal` and the separate values kept by each object |
| Encapsulation | `LunchWallet` stores a resource and checks its changes |
| Public, `_` and `__` names | Public methods, the internal history list and the name-mangled resource value |
| Getter, validating setter and read-only property | `balance` on the resource; `order_count` on the coordinator |
| Single and hierarchical inheritance | `Rolex` and `Kikomando` inherit `Meal` |
| Multilevel inheritance | `Meal → Rolex → AvocadoRolex` |
| Multiple and hybrid inheritance | `FeaturedRolex` combines the mixin with that family |
| Overriding and `super()` | The specialised calculation and the added description |
| Polymorphism | The mixed-object loop in `show_menu()` |
| Duck typing | `HomePackedLunch` works without inheriting `Meal` |
| MRO | The ordered class list printed near the ending |
| Abstraction and abstract classes | `Meal` requires `price()`; the caller uses it without reproducing its calculation |
| Composition and object collaboration | `LunchBreak` owns its resource and works with choice objects |
| UML relationships | The class diagram above |
| Python refresher | Functions, parameters, defaults, returned values, lists, loops, conditions and arithmetic |

Read [OOP in plain English](../../OOP_IN_PLAIN_ENGLISH.md) for a simple explanation of the terms.
