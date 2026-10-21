# The Mukono Mission

Amina left her flash drive in Mukono town. She must collect it and return for a presentation without overspending.

This story includes all the OOP concepts from Weeks 1 to 6. The numbers are made up for learning.

## Group assignment

The combined assignment is due at the end of **Wednesday, 21 October 2026, Uganda time**. Keep your [foundation work](EXTENSIONS.md), then choose three [later-topic extensions](ADVANCED_EXTENSIONS.md). Each member contributes foundation work and new code or meaningful automated tests through reviewed PRs. The [common assignment](../../GROUP_ASSIGNMENT.md) explains the workflow and what to submit.

## Run this story

If you have not downloaded the files yet, follow [Start here](../../START_HERE.md).

1. Open the repository folder in VS Code.
2. Open `stories/02_mukono_mission/story.py`.
3. Choose **Run Python File in Terminal**, or use the command below.

From a terminal in the main repository folder:

**Windows:**

```sh
py -3 stories/02_mukono_mission/story.py
```

**macOS or Linux:**

```sh
python3 stories/02_mukono_mission/story.py
```

The whole story prints without asking you to type anything. Open [expected_output.txt](expected_output.txt) to see the output of the unchanged program.

## Read the five acts

**Act 1 — the rule keeper.** `TripPurse` keeps the changing resource. Its constructor sets a valid starting value. Its property getter reads that value. Its setter refuses a negative value. Its action method refuses a request that does not fit.

**Act 2 — the family.** `Transport` is an abstract class. It says that every concrete member of the family must provide `quote_fare(distance)`. `Boda` and `Taxi` provide different versions. `super().__init__()` reuses the parent's setup.

**Act 3 — the special choices.** `StudentBoda` extends `Boda`. `CheerfulStudentBoda` adds the description from `CheerfulMixin` using multiple inheritance. `WalkWithFriend` is not in the same family but provides the methods the program needs.

**Act 4 — the coordinator.** `Journey` creates and owns a `TripPurse`. It receives a choice object, asks it for its behaviour and lets the resource object check the request. Successful actions go into its own history list. `completed_legs` reads the length of that list and has no setter.

**Act 5 — the complete story.** `main()` creates the objects and runs their actions. Two coordinator objects show that one person's resource and history are separate from another's.

## One request, step by step

`amina.travel(options[2], 3)` stores the chosen transport, asks for its fare, and reaches `StudentBoda.quote_fare()`. `super()` gets the 3,000 boda fare; the discount makes it 2,500. The purse pays and the completed-leg list grows. The next trip uses a taxi with the same Journey method.

## The ending, with the numbers explained

| Event | Resource after the attempt | Completed count |
|---|---|---|
| Student boda out | 5,000 - (3 × 1,000 - 500) = 2,500 | 1 |
| Taxi back | 2,500 - 2,000 = 500 | 2 |
| One more boda trip | Refused: 3,000 > 500; still 500 | 2 |
| Peter walks | 2,000 - 0 = 2,000 | 1 (Peter only) |

A refused request changes neither the guarded resource nor the completed-action count.

## How the classes connect

```mermaid
classDiagram
    Transport <|-- Boda
    Transport <|-- Taxi
    Boda <|-- StudentBoda
    StudentBoda <|-- CheerfulStudentBoda
    CheerfulMixin <|-- CheerfulStudentBoda
    Journey *-- TripPurse : owns
    Journey --> Transport : uses
    Journey --> WalkWithFriend : uses same methods
```

`Boda` **is a kind of** `Transport`. That is inheritance.

`Journey` **has its own** `TripPurse`. That is composition. It is not a kind of that resource.

Choice objects are created outside the coordinator. Passing them in is association. Keeping references to those independent objects is aggregation.

## Where each concept appears

| Concept | In this story |
|---|---|
| Classes, objects, attributes and methods | The class definitions and the objects created in `main()` |
| Constructors and `self` | Each `__init__`; `self` means the object receiving that call |
| Class and instance attributes | The shared fact on `Transport` and the separate values kept by each object |
| Encapsulation | `TripPurse` stores a resource and checks its changes |
| Public, `_` and `__` names | Public methods, the internal history list and the name-mangled resource value |
| Getter, validating setter and read-only property | `balance` on the resource; `completed_legs` on the coordinator |
| Single and hierarchical inheritance | `Boda` and `Taxi` inherit `Transport` |
| Multilevel inheritance | `Transport → Boda → StudentBoda` |
| Multiple and hybrid inheritance | `CheerfulStudentBoda` combines the mixin with that family |
| Overriding and `super()` | The specialised calculation and the added description |
| Polymorphism | The mixed-object loop in `compare()` |
| Duck typing | `WalkWithFriend` works without inheriting `Transport` |
| MRO | The ordered class list printed near the ending |
| Abstraction and abstract classes | `Transport` requires `quote_fare(distance)`; the caller uses it without reproducing its calculation |
| Composition and object collaboration | `Journey` owns its resource and works with choice objects |
| UML relationships | The class diagram above |
| Python refresher | Functions, parameters, defaults, returned values, lists, loops, conditions and arithmetic |

Read [OOP in plain English](../../OOP_IN_PLAIN_ENGLISH.md) for a simple explanation of the terms.
